from simulation.speedLimits import *
from simulation.trafficGenerators import * 

maxFps= 40
size = width, heigth = 1280, 800
# in miliseconds
updateFrame = 500

seed = None

lanes = 4
length = 220

maxSpeed = 7

maxLength = speedLimits = [ 
                SpeedLimit(range=((58.4, 0), (74.2,0)), limit=4, ticks=0),
                SpeedLimit(range=((58.4, 1), (74.2,1)), limit=4, ticks=0),
                SpeedLimit(range=((58.4, 2), (74.2,2)), limit=4, ticks=0),
                SpeedLimit(range=((58.4, 3), (74.2,3)), limit=4, ticks=0),
                
                SpeedLimit(range=((172, 0), (177,0)), limit=4, ticks=0),
                SpeedLimit(range=((172, 1), (177,1)), limit=4, ticks=0),
                SpeedLimit(range=((172, 2), (177,2)), limit=4, ticks=0),
                SpeedLimit(range=((172, 3), (177,3)), limit=4, ticks=0)
              ]

trafficGenerator = SimpleTrafficGenerator(4)
slowDownProbability, laneChangeProbability = 0.3, 0.2
