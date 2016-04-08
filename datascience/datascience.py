from datascience.collect import Collect
#from datascience.predict import *
#from datascience.visualization import *

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
        #self.visualization = Visualization(collect)

    def showParameters(self):
        self.collect.showParameters()

    def update(self, dt):
        #It is used for collecting data
        self.collecting(dt)
        
    
    def collecting(self, dt):
        self.acc += dt
        if self.acc >= self.updateFrame:
            self.collect.showRoad()
            self.collect.showDisplayerInfo()
        self.acc = self.acc % (self.updateFrame + 0)

