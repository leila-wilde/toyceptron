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
    
    def feedforward(self, inputs): 
        # start will original input
        outputs = inputs
        
        # pass through each layer one by one
        for layer in self.layers:
            # get raw outputs from layer
            raw_outputs = layer.forward(outputs)
            
            #apply activation fuction to each output
            outputs = [self.activation(i) for i in raw_outputs]
        
        return outputs
        # Network is like a pipeline:
        # input -> layer 1 -> activate -> layer 2 -> activate -> layer 3 -> activate -> output
        # each layer's output (after activation) becomes the next layer's input

    def summary(self):
        """
        Print network architecture summary
        Show input size, activation function and each layer's neuron count.
        """
        print(f"Network summary:\n")
        print(f"Input size: {self.input_size}\n")
        print(f"Activation: {self.activation.__name__}\n")
        print(f"Layers: {len(self.layers)}\n")
        for i, layer in enumerate(self.layers):
            print(f"- layer {i + 1}: {len(layer.neurons)} neurons")