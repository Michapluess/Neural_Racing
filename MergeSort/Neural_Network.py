from random import weibullvariate
from sys import api_version
from turtle import window_height


class Neural_Network:
    def __init__(self, inputsize):
        print("createNeuralNetwork")
        self.inputsize = inputsize
        self.weights = []
        self.biases = []
        self.activations = []
        self.lastLayerSize = inputsize
        self.countLayers = 0

    def feedForward(self, inputs):
        for layer in range(self.countLayers):
            previousactivations = inputs if layer == 0 else self.activations[layer-1]
            neurons = self.weights[layer]
            for neuron in range(len(neurons)):
                arrows = neurons[neuron]
                activation = 0
                for arrow in range(len(arrows)):
                    weight = arrows[arrow]
                    activation += weight*previousactivations[arrow]
                activation += self.biases[layer][neuron]
                self.activations[layer][neuron] = activation

        print("feedForward")
        return self.activations[self.countLayers-1]

    def addLayer(self, size):
        newweights = []
        newactivations = []
        newbiases = []
        for i in range(size):
            newarrows = []
            for j in range(self.lastLayerSize):
                newarrows.append(0.5)
            newweights.append(newarrows)
            newactivations.append(0)
            newbiases.append(0.1)
        self.weights.append(newweights) 
        self.activations.append(newactivations)
        self.biases.append(newbiases)
        self.lastLayerSize = size
        self.countLayers += 1
        print("addLayer")


nn = Neural_Network(6)
nn.addLayer(4)
nn.addLayer(2)
nn.addLayer(3)
output = nn.feedForward([0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
print(nn.weights)
print(output)