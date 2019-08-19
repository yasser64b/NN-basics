import numpy as np 
class Network(object):
	def __init__(self,sizes): #the list sizes contains the number of neurons in the respective layers.
		self.num_layers = len(sizes)  #the number of the layers in Network
		self.sizes = sizes
		self.biases = [np.random.randn(y,1) for y in sizes[1:]]
		self.weights = [np.random.randn(y,x) for y,x in zip(sizes[1:],sizes[:-1])]
        
    
A=Network(sizes=[1,2,1])
# B,W=A.wb()
