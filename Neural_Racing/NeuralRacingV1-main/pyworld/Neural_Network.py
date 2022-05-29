from random import weibullvariate
from random import random, normalvariate
from sys import api_version
from turtle import window_height
from math import exp
from copy import deepcopy
import json
import os


nnpath = "../data"




def sigmoid(x):
    "Numerically-stable sigmoid function."
    if x >= 0:
        z = exp(-x)
        return 1 / (1 + z)
    else:
        z = exp(x)
        return z / (1 + z)

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
                self.activations[layer][neuron] = sigmoid(activation)

        return self.activations[self.countLayers-1]

    def addLayer(self, size):
        newweights = []
        newactivations = []
        newbiases = []
        for i in range(size):
            newarrows = []
            for j in range(self.lastLayerSize):
                newarrows.append(4*random()-2)
            newweights.append(newarrows)
            newactivations.append(0)
            newbiases.append(4*random()-2)
        self.weights.append(newweights) 
        self.activations.append(newactivations)
        self.biases.append(newbiases)
        self.lastLayerSize = size
        self.countLayers += 1
        print("addLayer")

    def clone(self):
        nn = Neural_Network(self.inputsize)
        nn.activations = deepcopy(self.activations)
        nn.weights = deepcopy(self.weights)
        nn.biases = deepcopy(self.biases)
        nn.lastLayerSize = self.lastLayerSize
        nn.countLayers = self.countLayers
        return nn

    def randomAdjust(self, amount):
        for layer in range(self.countLayers):
            for neuron in range(len(self.weights[layer])):
                self.biases[layer][neuron] += normalvariate(0, amount)
                for arrow in range(len(self.weights[layer][neuron])):
                    self.weights[layer][neuron][arrow]+= normalvariate(0, amount)
    def savenn(self):
        files = os.listdir(nnpath)
        if len(files) > 0:
            os.remove(nnpath + "/nn.json")
        nndata = []
        nndata.append(self.weights)
        nndata.append(self.biases)
        f = open(nnpath + "/nn"+".json", "w")
        json.dump(nndata, f)
        f.close()
	
    






nn = Neural_Network(6)
nn.addLayer(4)
nn.addLayer(2)
output = nn.feedForward([0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
print("----------")
print(nn.weights)
print("----------")
print(nn.biases)
print("----------")
