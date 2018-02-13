import tensorflow as tf
import numpy as np

xdata = np.random.rand(100).astype(np.float32)
ydate = xdata*0.1+0.3

Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*xdata+biases
loss = tf.reduce_mean(tf.square(y-ydate))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step,sess.run(Weights),sess.run(biases))