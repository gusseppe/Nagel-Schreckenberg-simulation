from simulation.speedLimits import *
from simulation.trafficGenerators import * 

maxFps= 100
size = width, heigth = 1280, 800
# in miliseconds
updateFrame = 0.01

seed = None

step = 1
lanes = 4
length = 220*step


maxSpeed = 5
yellowSpeed = 3
redSpeed = 1
t = 10

maxLength = speedLimits = [ 
                SpeedLimit(range=((58.4*step, 0), (74.2*step,0)), limit=yellowSpeed, ticks=0),
                SpeedLimit(range=((58.4*step, 1), (74.2*step,1)), limit=yellowSpeed, ticks=0),
                SpeedLimit(range=((58.4*step, 2), (74.2*step,2)), limit=yellowSpeed, ticks=0),
                SpeedLimit(range=((58.4*step, 3), (74.2*step,3)), limit=yellowSpeed, ticks=0),
                
                SpeedLimit(range=((83.7*step, 0), (84*step,0)), limit=0, ticks=t, active=False),#semaforo
                SpeedLimit(range=((83.7*step, 1), (84*step,1)), limit=0, ticks=t, active=False),#semaforo
                SpeedLimit(range=((83.7*step, 2), (84*step,2)), limit=0, ticks=t, active=False),#semaforo
                SpeedLimit(range=((83.7*step, 3), (84*step,3)), limit=0, ticks=t, active=False),#semaforo
                
                SpeedLimit(range=((143*step, 0), (144*step,0)), limit=0, ticks=t, active=False),#semaforo
                SpeedLimit(range=((143*step, 1), (144*step,1)), limit=0, ticks=t, active=False),#semaforo
                SpeedLimit(range=((143*step, 2), (144*step,2)), limit=0, ticks=t, active=False),#semaforo
                SpeedLimit(range=((143*step, 3), (144*step,3)), limit=0, ticks=t, active=False),#semaforo
                
                SpeedLimit(range=((172*step, 0), (177*step,0)), limit=yellowSpeed, ticks=0),
                SpeedLimit(range=((172*step, 1), (177*step,1)), limit=yellowSpeed, ticks=0),
                SpeedLimit(range=((172*step, 2), (177*step,2)), limit=yellowSpeed, ticks=0),
                SpeedLimit(range=((172*step, 3), (177*step,3)), limit=yellowSpeed, ticks=0)
              ]

trafficGenerator = SimpleTrafficGenerator(1)
slowDownProbability, laneChangeProbability = 0.3, 0.2
