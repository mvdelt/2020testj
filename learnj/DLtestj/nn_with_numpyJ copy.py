# i. from pytorch official site tutorial.

# -*- coding: utf-8 -*-
import numpy as np

# N is batch size; D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
N, D_in, H, D_out = 10, 40, 60, 5

# Create random input and output data
x = np.random.randn(N, D_in)
y = np.random.randn(N, D_out)

# Randomly initialize weights
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)

learning_rate = 1e-6  # i. 1e-5 로 하면 발산돼버림.
for t in range(1000):
    # Forward pass: compute predicted y
    h = x.dot(w1)
    h_relu = np.maximum(h, 0)
    y_pred = h_relu.dot(w2)
    if t%100==99:
        print('--------forward pass--------------------------------------------------------')
        print(f'h:{h}')
        print(f'h_relu:{h_relu}')
        print(f'y_pred:{y_pred}')

    # Compute and print loss
    loss = np.square(y_pred - y).sum()
    if t%100==99:
        print(f't:{t}, loss:{loss}')

    # Backprop to compute gradients of w1 and w2 with respect to loss  # i. -> gradients of Loss w.r.t. w1 and w2 라고해야 맞음.
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.T.dot(grad_y_pred)
    grad_h_relu = grad_y_pred.dot(w2.T)
    grad_h = grad_h_relu.copy()
    grad_h[h < 0] = 0
    grad_w1 = x.T.dot(grad_h)
    if t%100==99:
        print('----------backward pass-----------------------------------------------------')
        print(f'grad_y_pred:{grad_y_pred}')
        print(f'grad_w2:{grad_w2}')
        print(f'grad_h_relu:{grad_h_relu}')
        print(f'grad_h:{grad_h}')
        print(f'grad_w1:{grad_w1}')

    # Update weights
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2