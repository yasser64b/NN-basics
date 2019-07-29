import numpy as np
# Matrix Operations
A=np.array([[1,2,3],[4,2,7]])
A
B=np.array([[4,8],[6,2],[5,3]])
C=np.matmul(A,B)
np.dot(A,B)
# elem by elem operation for same size matrices  
A=np.array([[1,2,3],[4,2,7]])
B=np.array([[4,8,6],[2,5,3]])
A+B
A-B
A/B
A*B
np.multiply(A,B)

np.maximum(A, B)
np.minimum(A, B)
np.exp(A)  # e^ 1,2,34
np.tanh(A) # (exp(2x)-1)/(exp(2x)+1)
np.log(A)
# generate random numbers 
np.random.normal(0, 1, (5, 4))

#reshaping the matrix 
np.array([A]).reshape((2,3)) 

np.sum(B)
np.zeros([10,10]) 
np.zeros(A.shape) 
np.sqrt(A)

# What to do with 1/0 or nan , etc 
A=np.array([[1,2,3],[4,2,7]])
B=np.array([[0,8,6],[2,5,3]])
C=A/B
np.nan_to_num(C)
np.nan_to_num(np.nan)

E=np.array([np.inf, -np.inf, np.nan, -128, 128])
np.nan_to_num(E)

# Activation functions 
# Sigmoid=1/(1+exp(-x))
S=1.0 / (1.0+ np.exp(-1))
S
#derivative of sigmoid function : 
S_prime= S*(1-S)

def sigmoid(z):
    S=1.0 / (1.0+ np.exp(-z))
    return S


def sigmoid_prime(z):
    S=1.0/(1.0+ np.exp(-z))
    S_prime= S*(1-S)
    return S_prime

A
sigmoid(A)
sigmoid_prime(A)

# Cost function 
def cost_fn(a,y):
    c=a-y 
    return c

cost_fn(10,2)