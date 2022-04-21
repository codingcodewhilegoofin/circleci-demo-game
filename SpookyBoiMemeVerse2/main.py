# Imports 

# TF
import tensorflow as tf 
import tensorflow_datasets as tfds

# Pandas
import pandas as pd 

# Numpy
import numpy as np 

# Matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt

# Normal
import math
import logging

# Function to give each image a value between .0 and 1
def normalize( images, labels):
    images = tf.cast(images,tf.float32)
    images /= 255
    return images,labels

# Log an error 
logger = tf.get_logger()
logger.setLevel(logging.ERROR)

# Grab meta/data set from tfds API
dataset , metadata = tfds.load('fashion_mnist', as_supervised=True, with_info=True)

# Split data into training and test sets
train_dataset, test_dataset = dataset['train'], dataset['test']

# Normalize the images, and cache them for performance
train_dataset =  train_dataset.map(normalize)
test_dataset  =  test_dataset.map(normalize)
train_dataset =  train_dataset.cache()
test_dataset  =  test_dataset.cache()

# BUILD MODEL 
model = tf.keras.Sequential(
    # Layer 1 INPUT
    # The process of converting a 2d image into 1d vector
    tf.keras.layers.Flatten( input_shape=(28,28,1)),
    # Layer 2 HIDDEN
    # Regular densely-connected NN layer.
    # Rectified Linear Unit activation function.
    tf.keras.layers.Dense( 128 , activation = tf.nn.relu),
    # Layer 3 OUTPUT
    # Regular densely-connected NN layer.
    # Softmax activation function.
    tf.keras.layers.Dense( 10 , activation= tf.nn.softmax)
)

# COMPILE MODEL 
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

# TRAIN MODEL 

    # Define Iterations for training

    # Train with Fit()