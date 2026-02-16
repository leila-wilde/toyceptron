# Network.py

# store many layers
# has feedforward(input_vector) method that passes data through all

from layer import Layer

class Network:
    def __init__(self, input_size, activation):
        self.input_size = input_size 
        self.activation = activation 
        self.layers = [] # empty list to hold layers

    def add(self, weights, biases): # add layers
        """
        add a new layer to the network
        args: 
        - list of weight lists for each neuron
        - list of biases for each neuron 
        """
        # create new layer with weights and biases
        layer =  Layer(weights_list=weights, biases_list=biases)
        self.layers.append(layer)
