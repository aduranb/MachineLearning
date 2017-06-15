from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data .read_data_sets('MNIST_data',one_hot = True)


#TensorFlow relies on a highly efficient C++ backend to do its computation. The connection to this backend is called a session.
#The common usage is to first create a graph and then launch it in a session.

import tensorflow as tf
sess = tf.InteractiveSession()# more flexible

#ComputationGraph

#Numpy does expensive operations outside Python