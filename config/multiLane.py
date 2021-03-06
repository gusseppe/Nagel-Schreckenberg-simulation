from simulation.speedLimits import *
from simulation.trafficGenerators import * 

maxFps= 40
size = width, heigth = 1280, 800
# in miliseconds
updateFrame = 500

seed = None

lanes = 4
length = 190

maxSpeed = 7
maxLength = 1000

speedLimits = []
trafficGenerator = SimpleTrafficGenerator(10)
slowDownProbability, laneChangeProbability = 0.3, 0.2
