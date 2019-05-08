# -*- coding: utf-8 -*-
"""
@author: Yugo
"""
import random as rd

class Chromosome(object):   
    #Construtor     
    def __init__(self, size=0, value=""):
        self.fitness = 0 
        self.value = value
        if int( size ) != 0:
            self.init(size)
    
    #Operador de comparacao (==)
    def __eq__(self, other): 
        if not isinstance(other, Chromosome):
            return False 
        return self.value == other.value

    def evaluate(self, fitness_function):
        self.fitness = fitness_function(self.value)
        return self.fitness

    def init(self, size):
        for i in range(size):
            if rd.random() < 0.5 :
                self.value += "0"
            else :
                self.value += "1" 

    def mutation(self, probability): 
        for i in range( len(self.value) ):
            if rd.random() < probability:
                bit = 0 if int( self.value[i] ) else 0 
                inicio = self.value[0:i]
                fim = self.value[i+1 : len(self.value)]
                self.value = inicio + str(bit) + fim

    def crossover(self, dad):
        child = Chromosome()
        cutoff = int( rd.random() * len(self.value) )
        if rd.random() < 0.5: 
            child.value = self.value[0:cutoff] + dad.value[cutoff : len(dad.value)]
        else: 
            child.value = dad.value[0:cutoff] + self.value[cutoff : len(dad.value)]
        return child
