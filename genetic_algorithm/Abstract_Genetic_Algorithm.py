# -*- coding: utf-8 -*-
"""
@author: Yugo
"""

# Classe para Analise Lexica
class AGA(object):

    def __init__(self):
        self.stop = False
        while not self.stop:
            self.initPopulation()
            self.selectParents()
            self.produceChildren()
            self.mutate()
            self.extendPopulation()
            self.reduceExtendedPopulation()
        self.outputBestIndividualFount()

    def initPopulation(self):
        print('initPopulation \n')
    def selectParents(self):
        print('selectParents \n')
    def produceChildren(self):
        print('produceChildren \n')
    def mutate(self): 
        print('mutate \n')
    def extendPopulation(self):
        print('extendPopulation \n')
    def reduceExtendedPopulation(self):
        print('reduceExtendedPopulation \n')
        self.stop = True
    def outputBestIndividualFount(self):
        print('outputBestIndividualFount \n')
        

    
    
            
