# -*- coding: utf-8 -*-
"""
@author: Yugo
"""
from genetic_algorithm.Chromosome import Chromosome 
import random as rd

class Aga(object):

    def __init__(self):
        self.stop = True
        self.population = []
        self.populationFitness = 0.0
        self.mutationProbability = 0.005
        self.newPopulation = []
        self.ageCount = 0
        self.populationSize = 0
    
    def calculateSumFitness(self): 
        self.populationFitness = 0 
        for chromosome in self.population:
            self.populationFitness += chromosome.value
        return self.populationFitness
    
    def roulette(self):
        self.calculateSumFitness()
        limit = rd.random() * self.populationFitness
        index = 0 
        sumFitness = 0 
        while (index < len( self.population )) and (sumFitness < limit):
            sumFitness += self.population[index].fitness
            index += 1
        index -= 1
        return index  

    def execute(self): 
        self.initPopulation(10)
        while not self.stop:
            self.evaluatePopulation()
            self.selectParents()
            self.applyGeneticOperators()
            self.selectSurvivors()
        return self.getBestIndividualFound()

    def initPopulation(self, size):
        for i in range(size):
            self.population.append(Chromosome(10))

    def evaluatePopulation(self):
        pass
    def selectParents(self):
        pass
    def applyGeneticOperators(self):
        pass
    def selectSurvivors(self):
        pass
    def getBestIndividualFound(self): 
        pass
