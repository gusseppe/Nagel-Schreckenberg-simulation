from simulation.speedLimits import *
from simulation.trafficGenerators import * 

maxFps= 40
size = width, heigth = 1280, 800
# in miliseconds
updateFrame = 500

seed = None

lanes = 4
length = 2200

maxSpeed = 6

maxLength = speedLimits = [ 
                SpeedLimit(range=((50, 1), (80,1)), limit=0, ticks=0),
                SpeedLimit(range=((50, 2), (80,2)), limit=0, ticks=0),
                SpeedLimit(range=((150, 2), (280,2)), limit=1, ticks=40),
                SpeedLimit(range=((150, 3), (280,3)), limit=1, ticks=40)
              ]

trafficGenerator = SimpleTrafficGenerator(7)
slowDownProbability, laneChangeProbability = 0.3, 0.2
