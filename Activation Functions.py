import numpy as np 
# Sigmoid 
def Sigmoid(z):
    return 1.0 / (1.0+ np.exp(-z))

def Sigmoid_prime(z):
    s=1.0 / (1.0+ np.exp(-z))
    return s*(1-s) 

#Tanh
def tanh(z):
    return np.tanh(z)

def tanh_prime(z):
    return (1 - (np.tanh(z)** 2))

# relu
def relu(z):
    return np.maximum(0, z)

def relu_prime(z):
        if z==0 or z<0 : 
            z=0
        else:
            z=1
        return z

relu_prime(-10)


# leaky relu
def leakyrelu(z):
    return np.maximum(0.01*z, z)

def leakyrelu_prime(z):
        if z==0 or z<0 : 
            z=0.01
        else:
            z=1
        return z

leakyrelu_prime(-10)

import numpy as np 
def activation_fn(z,activation= "tanh"):
    if activation == "leaky_relu":
        return np.maximum(0.01 * z, z)
    elif activation == "relu":
        return np.maximum(0, z)
    elif activation == "sigmoid":
        return 1.0 / (1.0+ np.exp(-z))
    elif activation == "tanh":
        return np.tanh(z)


def activation_fn_prime(z,activation="tanh"):
    if activation == "leaky_relu":
        if z==0 or z<0 : 
            z=0.01
        else:
            z=1
        return z
    elif activation == "relu":
        if z==0 or z<0 : 
            z=0
        else:
            z=1
        return z
    elif activation == "sigmoid":
        return activation_fn(z) * (1 - activation_fn(z))
    elif activation == "tanh":
        return (1 - (np.tanh(z)** 2))


# See full Toturial at my Youtube Channel(YB TV): https://www.youtube.com/channel/UCvnhhDKv5takEN412dmVW8g/featured
# GitHab Page:https://github.com/yasser64b/Machine-Learning- 
#Email: big3del@gmail.com