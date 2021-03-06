""" 
blocks/one_d.py
Author: Ankit Gupta

Implementations of various DenseNet blocks for 1D sequences

This module contains helper functions that define the various subcomponents of a DenseNet.
This includes dense blocks and transition blocks.

"""

from tensorflow.keras.layers import BatchNormalization, Activation, Conv1D, \
                                    Concatenate, AveragePooling1D
from tensorflow.keras import backend, layers


def squeeze_excite_block(input_tensor, ratio=8):
    """Create a channel-wise squeeze-excite block.
    Args:
        input_tensor: input Keras tensor
        ratio: number of output filters
    Returns: a Keras tensor
    
    References
    -   [Squeeze and Excitation Networks](https://arxiv.org/abs/1709.01507)
    """
    init = input_tensor
    channel_axis = 1 if backend.image_data_format() == "channels_first" else -1
    filters = init.shape[channel_axis]#_tensor_shape(init)[channel_axis]
    se_shape = (1, filters)

    se = layers.GlobalAvgPool1D()(init)
    se = layers.Reshape(se_shape)(se)
    se = layers.Dense(filters // ratio, activation='relu', kernel_initializer='he_normal', use_bias=False)(se)
    se = layers.Dense(filters, activation='sigmoid', kernel_initializer='he_normal', use_bias=False)(se)

    if backend.image_data_format() == 'channels_first':
        se = layers.Permute((3, 1, 2))(se)

    x = layers.multiply([init, se])
    return x


def H_l(k, bottleneck_size, kernel_width):
    """ 
    A single convolutional "layer" as defined by Huang et al.
    Defined as H_l in the original paper
    
    :param k: int representing the "growth rate" of the DenseNet
    :param bottleneck_size: int representing the size of the bottleneck,
                            as a multiple of k. Set to 0 for no bottleneck.
    :param kernel_width: int representing the width of the main convolutional kernel
    :return a function wrapping the keras layers for H_l
    """

    use_bottleneck = bottleneck_size > 0
    num_bottleneck_output_filters = k * bottleneck_size

    def f(x):
        if use_bottleneck:
            x = BatchNormalization()(x)
            x = Activation("relu")(x)
            x = Conv1D(
                num_bottleneck_output_filters,
                1,
                strides=1,
                padding="same",
                dilation_rate=1)(x)
        x = BatchNormalization()(x)
        x = Activation("relu")(x)
        x = Conv1D(
            k,
            kernel_width,
            strides=1,
            padding="same",
            dilation_rate=1)(x)
        return x
    return f


def dense_block(k, num_layers, kernel_width, bottleneck_size, se=False):
    """
    A single dense block of the DenseNet
    
    :param k: int representing the "growth rate" of the DenseNet
    :param num_layers: int represending the number of layers in the block
    :param kernel_width: int representing the width of the main convolutional kernel
    :param bottleneck_size: int representing the size of the bottleneck,
                            as a multiple of k. Set to 0 for no bottleneck.
    :return a function wrapping the entire dense block
    """
    def f(x):
        layers_to_concat = [x]
        for _ in range(num_layers):
            x = H_l(k, bottleneck_size, kernel_width)(x)
            layers_to_concat.append(x)
            # https://github.com/tensorflow/tensorflow/issues/30355
            x = Concatenate(axis=-1)(layers_to_concat[:])
            if se:
                x = squeeze_excite_block(x)
        return x
    return f


def transition_block(pool_size=2, stride=2, theta=0.5, se=False):
    """
    A single transition block of the DenseNet
    
    :param pool_size: int represending the width of the average pool
    :param stride: int represending the stride of the average pool
    :param theta: int representing the amount of compression in the 1x1 convolution.
                  Set to 1 for no compression.
    :return a function wrapping the entire transition block
    """    
    assert theta > 0 and theta <= 1

    def f(x):
        num_transition_output_filters = int(int(x.shape[2]) * float(theta))
        x = BatchNormalization()(x)
        x = Activation("relu")(x)
        x = Conv1D(
            num_transition_output_filters,
            1,
            strides=1,
            padding="same",
            dilation_rate=1)(x)
        x = AveragePooling1D(
            pool_size=pool_size,
            strides=stride,
            padding="same")(x)
        if se:
            x = squeeze_excite_block(x)
        return x
    return f
