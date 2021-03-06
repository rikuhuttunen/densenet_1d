""" 
classifiers/one_d.py
Author: Ankit Gupta

Implementations of classifiers using DenseNet

This module contains subclasses of keras.models.Model that implement DenseNet through the Keras API. This works by calling the functions in densenet.models.one_d.py, adding the appropriate classification Keras functions, and wrapping the transformation in keras.models.Model objects.
"""

import tensorflow.keras.models
from tensorflow.keras.layers import Input, Conv1D, Dense
import densenet.models.one_d


def DenseNet121(input_shape,
                num_outputs=1000,
                k=32,
                conv_kernel_width=3,
                bottleneck_size=4,
                transition_pool_size=2,
                transition_pool_stride=2,
                theta=0.5,
                initial_conv_width=7,
                initial_stride=2,
                initial_filters=64,
                initial_pool_width=3,
                initial_pool_stride=2,
                include_top=False):
    """  
    Create a Keras Model Object that is an implementation of DenseNet121
    :param input_shape: The shape of the inputs without the batch dimension.
        This should be a valid 1D sequence, such as (244, 25). 
    :param num_outputs: the number of classes to predict
    :param k: The "growth rate" of the DenseNet model
    :param conv_kernel_width: The kernel width of each convolution in the dense blocks.
    :param bottleneck_size: The size of the bottleneck, as a multiple of k. Set to 0 for no bottleneck.
    :param transition_pool_size: pool_size in the transition layer
    :param transition_pool_stride: pooling stride in the transition layer
    :param theta: Amount of compression in the transition layer. Set to 1 for no compression.
    :param initial_conv_width: Kernel width for the one convolution before the dense blocks
    :param initial_stride: Stride for the one convolution before the dense blocks
    :param initial_filters: Number of filters for the one convolution before the dense blocks
    :param initial_pool_width: pool_size for the one pooling before the dense blocks
    :param initial_pool_stride: stride for the one pooling before the dense blocks 
    """
    model_input = Input(shape=input_shape)
    output = densenet.models.one_d.DenseNet121(
        k,
        conv_kernel_width,
        bottleneck_size,
        transition_pool_size,
        transition_pool_stride,
        theta,
        initial_conv_width,
        initial_stride,
        initial_filters,
        initial_pool_width,
        initial_pool_stride,
        use_global_pooling=True)(model_input)
    if include_top:
        output = Dense(num_outputs, activation="softmax")(output)
    return tensorflow.keras.models.Model(inputs=model_input, outputs=output)


def DenseNet169(input_shape,
                num_outputs=1000,
                k=32,
                conv_kernel_width=3,
                bottleneck_size=4,
                transition_pool_size=2,
                transition_pool_stride=2,
                theta=0.5,
                initial_conv_width=7,
                initial_stride=2,
                initial_filters=64,
                initial_pool_width=3,
                initial_pool_stride=2,
                include_top=False):
    """  
    Create a Keras Model Object that is an implementation of DenseNet169
    :param input_shape: The shape of the inputs without the batch dimension.
        This should be a valid 1D sequence, such as (244, 25). 
    :param num_outputs: the number of classes to predict
    :param k: The "growth rate" of the DenseNet model
    :param conv_kernel_width: The kernel width of each convolution in the dense blocks.
    :param bottleneck_size: The size of the bottleneck, as a multiple of k. Set to 0 for no bottleneck.
    :param transition_pool_size: pool_size in the transition layer
    :param transition_pool_stride: pooling stride in the transition layer
    :param theta: Amount of compression in the transition layer. Set to 1 for no compression.
    :param initial_conv_width: Kernel width for the one convolution before the dense blocks
    :param initial_stride: Stride for the one convolution before the dense blocks
    :param initial_filters: Number of filters for the one convolution before the dense blocks
    :param initial_pool_width: pool_size for the one pooling before the dense blocks
    :param initial_pool_stride: stride for the one pooling before the dense blocks 
    """
    model_input = Input(shape=input_shape)
    output = densenet.models.one_d.DenseNet169(
        k,
        conv_kernel_width,
        bottleneck_size,
        transition_pool_size,
        transition_pool_stride,
        theta,
        initial_conv_width,
        initial_stride,
        initial_filters,
        initial_pool_width,
        initial_pool_stride,
        use_global_pooling=True)(model_input)
    if include_top:
        output = Dense(num_outputs, activation="softmax")(output)
    return tensorflow.keras.models.Model(inputs=model_input, outputs=output)


def DenseNet201(input_shape,
                num_outputs=1000,
                k=32,
                conv_kernel_width=3,
                bottleneck_size=4,
                transition_pool_size=2,
                transition_pool_stride=2,
                theta=0.5,
                initial_conv_width=7,
                initial_stride=2,
                initial_filters=64,
                initial_pool_width=3,
                initial_pool_stride=2,
                include_top=False):
    """  
    Create a Keras Model Object that is an implementation of DenseNet201
    :param input_shape: The shape of the inputs without the batch dimension.
        This should be a valid 1D sequence, such as (244, 25). 
    :param num_outputs: the number of classes to predict
    :param k: The "growth rate" of the DenseNet model
    :param conv_kernel_width: The kernel width of each convolution in the dense blocks.
    :param bottleneck_size: The size of the bottleneck, as a multiple of k. Set to 0 for no bottleneck.
    :param transition_pool_size: pool_size in the transition layer
    :param transition_pool_stride: pooling stride in the transition layer
    :param theta: Amount of compression in the transition layer. Set to 1 for no compression.
    :param initial_conv_width: Kernel width for the one convolution before the dense blocks
    :param initial_stride: Stride for the one convolution before the dense blocks
    :param initial_filters: Number of filters for the one convolution before the dense blocks
    :param initial_pool_width: pool_size for the one pooling before the dense blocks
    :param initial_pool_stride: stride for the one pooling before the dense blocks 
    """
    model_input = Input(shape=input_shape)
    output = densenet.models.one_d.DenseNet201(
        k,
        conv_kernel_width,
        bottleneck_size,
        transition_pool_size,
        transition_pool_stride,
        theta,
        initial_conv_width,
        initial_stride,
        initial_filters,
        initial_pool_width,
        initial_pool_stride,
        use_global_pooling=True)(model_input)
    if include_top:
        output = Dense(num_outputs, activation="softmax")(output)
    return tensorflow.keras.models.Model(inputs=model_input, outputs=output)


def DenseNet264(input_shape,
                num_outputs=1000,
                k=32,
                conv_kernel_width=3,
                bottleneck_size=4,
                transition_pool_size=2,
                transition_pool_stride=2,
                theta=0.5,
                initial_conv_width=7,
                initial_stride=2,
                initial_filters=64,
                initial_pool_width=3,
                initial_pool_stride=2,
                include_top=False):
    """  
    Create a Keras Model Object that is an implementation of DenseNet264
    :param input_shape: The shape of the inputs without the batch dimension.
        This should be a valid 1D sequence, such as (244, 25). 
    :param num_outputs: the number of classes to predict
    :param k: The "growth rate" of the DenseNet model
    :param conv_kernel_width: The kernel width of each convolution in the dense blocks.
    :param bottleneck_size: The size of the bottleneck, as a multiple of k. Set to 0 for no bottleneck.
    :param transition_pool_size: pool_size in the transition layer
    :param transition_pool_stride: pooling stride in the transition layer
    :param theta: Amount of compression in the transition layer. Set to 1 for no compression.
    :param initial_conv_width: Kernel width for the one convolution before the dense blocks
    :param initial_stride: Stride for the one convolution before the dense blocks
    :param initial_filters: Number of filters for the one convolution before the dense blocks
    :param initial_pool_width: pool_size for the one pooling before the dense blocks
    :param initial_pool_stride: stride for the one pooling before the dense blocks 
    """
    model_input = Input(shape=input_shape)
    output = densenet.models.one_d.DenseNet264(
        k,
        conv_kernel_width,
        bottleneck_size,
        transition_pool_size,
        transition_pool_stride,
        theta,
        initial_conv_width,
        initial_stride,
        initial_filters,
        initial_pool_width,
        initial_pool_stride,
         use_global_pooling=True)(model_input)
    if include_top:
        output = Dense(num_outputs, activation="softmax")(output)
    return tensorflow.keras.models.Model(inputs=model_input, outputs=output)


def DenseFCN(input_shape,
             num_outputs=5,
             k=32,
             block_sizes=[6, 12, 24, 16],  # Default to DenseNet121
             conv_kernel_width=3,
             bottleneck_size=4,
             transition_pool_size=2,
             transition_pool_stride=2,
             theta=0.5,
             initial_conv_width=7,
             initial_stride=2,
             initial_filters=64,
             initial_pool_width=3,
             initial_pool_stride=2):
    """  
    Create a Keras Model Object that is an implementation of DenseNet with a
    custom number of parameters. The number of layers per dense block can be 
    specified by block_sizes.
    :param input_shape: The shape of the inputs without the batch dimension.
                        This should be a valid 1D sequence, such as (244, 25). 
    :param num_outputs: the number of classes to predict
    :param k: The "growth rate" of the DenseNet model
    :param block_sizes: A list of ints with the number of layers in each block. Example: [5, 10, 25, 17].
    :param conv_kernel_width: The kernel width of each convolution in the dense blocks.
    :param bottleneck_size: The size of the bottleneck, as a multiple of k. Set to 0 for no bottleneck.
    :param transition_pool_size: pool_size in the transition layer
    :param transition_pool_stride: pooling stride in the transition layer
    :param theta: Amount of compression in the transition layer. Set to 1 for no compression.
    :param initial_conv_width: Kernel width for the one convolution before the dense blocks
    :param initial_stride: Stride for the one convolution before the dense blocks
    :param initial_filters: Number of filters for the one convolution before the dense blocks
    :param initial_pool_width: pool_size for the one pooling before the dense blocks
    :param initial_pool_stride: stride for the one pooling before the dense blocks 
    """
    if not block_sizes:
        raise ValueError("block_sizes must be specified")
    model_input = Input(shape=input_shape)
    output = densenet.models.one_d.DenseNet(k,
        block_sizes,
        conv_kernel_width,
        bottleneck_size,
        transition_pool_size,
        transition_pool_stride,
        theta,
        initial_conv_width,
        initial_stride,
        initial_filters,
        initial_pool_width,
        initial_pool_stride,
        use_global_pooling=False)(model_input)
     
    output = Conv2D(num_outputs, (1, 1), padding='same', activation='sigmoid')(x)
    return tensorflow.keras.models.Model(inputs=model_input, outputs=output)


def DenseNetCustom(#tensorflow.keras.models.Model):
            input_shape,
            num_outputs=1000,
            k=32,
            block_sizes=None,
            conv_kernel_width=3,
            bottleneck_size=4,
            transition_pool_size=2,
            transition_pool_stride=2,
            theta=0.5,
            initial_conv_width=7,
            initial_stride=2,
            initial_filters=64,
            initial_pool_width=3,
            initial_pool_stride=2,
            include_top=False,
            se=True):
    """  
    Create a Keras Model Object that is an implementation of DenseNet with a custom number of parameters. The number of layers per dense block can be specified by block_sizes.
    :param input_shape: The shape of the inputs without the batch dimension. This should be a valid 1D sequence, such as (244, 25). 
    :param num_outputs: the number of classes to predict
    :param k: The "growth rate" of the DenseNet model
    :param block_sizes: A list of ints with the number of layers in each block. Example: [5, 10, 25, 17].
    :param conv_kernel_width: The kernel width of each convolution in the dense blocks.
    :param bottleneck_size: The size of the bottleneck, as a multiple of k. Set to 0 for no bottleneck.
    :param transition_pool_size: pool_size in the transition layer
    :param transition_pool_stride: pooling stride in the transition layer
    :param theta: Amount of compression in the transition layer. Set to 1 for no compression.
    :param initial_conv_width: Kernel width for the one convolution before the dense blocks
    :param initial_stride: Stride for the one convolution before the dense blocks
    :param initial_filters: Number of filters for the one convolution before the dense blocks
    :param initial_pool_width: pool_size for the one pooling before the dense blocks
    :param initial_pool_stride: stride for the one pooling before the dense blocks 
    """
    if not block_sizes:
        raise ValueError("block_sizes must be specified")
    inputs = Input(shape=input_shape)
    outputs = densenet.models.one_d.DenseNet(
        k,
        block_sizes,
        conv_kernel_width,
        bottleneck_size,
        transition_pool_size,
        transition_pool_stride,
        theta,
        initial_conv_width,
        initial_stride,
        initial_filters,
        initial_pool_width,
        initial_pool_stride,
        use_global_pooling=True,
        se=se)(inputs)
    if include_top:
        outputs = Dense(num_outputs, activation="softmax")(outputs)
    return tensorflow.keras.models.Model(inputs=inputs, outputs=outputs)
