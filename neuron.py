# Neuron.py

# neuron class to store weights and bias
# has forward(input_vector) method that calculates output

class Neuron:
    def __init__(self, weights : list, bias=0.0):
        self.weights = weights
        self.bias = bias

    def forward(self, inputs):
        """
        calculate neuron output: (input[0]*weight[0]) + (input[1]*weight[1]) + ... + bias  
        args inputs takes a list [x1, x2, x3, ...]
        returns the raw output before activation
        """
        if len(inputs) != len(self.weights):
            raise ValueError(f"The number of inputs ({len(inputs)}) doesnt maths the number of weights ({len(self.weights)})")

        weight_sum = 0
        for i in range(len(inputs)):
            weight_sum += inputs[i] * self.weights[i]

        output = weight_sum + self.bias

        return output