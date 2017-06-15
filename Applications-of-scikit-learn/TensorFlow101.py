from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data/', one_hot = True)

###

#MNIST data is split into:

# 55,000 training data points
# 10,000 test points
#  5,000 validation points

# Every data point has two parts:

# image : x (28px*28px) = array of 784 numbers
# label : y

# mnist.train.images is a tensor with a shape of [55000,784]
# softmax regression is a natural, simple model to give probabilities of each image being each digit.

import tensorflow as tf

x = tf.placeholder(tf.float32, [None, 784])#placeholder with undefined length

W = tf.Variable(tf.zeros([784,10]))#matrix to be fine-tuned
b = tf.Variable(tf.zeros([10])) #vector to be fine-tuned

# y = W*x + b

y = tf.nn.softmax(tf.matmul(x,W)+b)

# cross-entropy - how inefficient our predictions are for describing the truth

y_ = tf.placeholder(tf.float32,[None,10])

## cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))#reduction indices means "add elements in the second dimension of y

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = y_, logits = y))

#next step is: move a little bit in the direction of the gradient to find a minimum

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess= tf.InteractiveSession()

tf.global_variables_initializer().run()

#We run the training step 1000 times (stochastic approach)
for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100) #instead of using all our data on each step, we use small batches of random data as an unexpensive way to train our algorithm (Doing this is cheap and has much of the same benefit).
    sess.run(train_step,feed_dict={x: batch_xs, y_:batch_ys})

## Evaluate

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
#argmax gives the index of the highest entry in a tensor
    # argmax(y,1) is the label our model thinks is most likely
    # argmax(y_,1) is the correct label
    # tf.equal checks if the prediction match the truth

#correct_prediction is a list of booleans, that we need to reduce to a percentage:

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#print (sess.run(accuracy, feed_dict={x: mnist.test.images, y_:mnist.test.labels}))

#91%