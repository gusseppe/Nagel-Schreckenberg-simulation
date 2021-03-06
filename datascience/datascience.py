from datascience.collect import Collect
from datascience.analyze import *
#from datascience.predict import *

class DataScience():

    def __init__(self, config, road, simulation, representation):
        self.config = config
        self.road = road
        self.simulation = simulation
        self.representation = representation
        self.updateFrame = simulation.updateFrame
        self.acc = 0

        self.collect = Collect(config, road, simulation, representation)
        #self.ml = MachineLearning(collect)
        #self.analize = Analize(collect)

    def writeInput(self):
        """ Guardar los parametros de entrada"""

        #self.collect.writeInput()

    def writeOutput(self):
        """ Guardar los parametros de salida"""

        self.collect.writeOutput()

    def update(self, dt):
        """ Actualizar los valores de los parametros de salida"""

        self.collecting(dt)
        
    
    def collecting(self, dt):
        """ Recaudar los parametros de salida"""
        self.acc += dt
        if self.acc >= self.updateFrame:
            #self.collect.showRoad()
            self.collect.writeOutput()
            #self.collect.showSpeedLimits()
        self.acc = self.acc % (self.updateFrame + 0)

