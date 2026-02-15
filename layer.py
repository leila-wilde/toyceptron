# Layer.py
# an ordered collection of identical neurons that :
# - creates/stores many neurons
# - applies a vector of input to all its neurons and produce a vector of output

from neuron import Neuron

class Layer:
    def __init__(self, weights_list : list, biases_list : list ):
        self.neurons = [] # init empty list
        for i in range(len(weights_list)):
            neuron = Neuron(weights=weights_list[i], bias=biases_list[i])
            self.neurons.append(neuron)

    def forward(self, inputs : list):
        """
        pass input through all neurons in the layer
        args: inputs as a vector of numbers
        returns: list of outputs, one from each neuron
        """
        outputs = []
        for neuron in self.neurons:
            output = neuron.forward(inputs)
            outputs.append(output)
        return outputs