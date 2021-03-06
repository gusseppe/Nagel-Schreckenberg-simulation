import sys, pygame, simulation.road, simulation.speedLimits, random, importlib, config
from simulation.car import Car
from representation import Representation
from simulationManager import SimulationManager
from simulation.trafficGenerators import *

#DataScience
from datascience.datascience import *

if len(sys.argv) != 2:
    print("Usage: python pyTraffic.py module_with_config")
    exit()

#Aqui se generan las distintas configuraciones
config = importlib.import_module(sys.argv[1])

random.seed(config.seed)
pygame.init()
screen = pygame.display.set_mode(config.size)

clock = pygame.time.Clock()

simulation.car.Car.slowDownProbability = config.slowDownProbability
simulation.car.Car.laneChangeProbability = config.laneChangeProbability
speedLimits = simulation.speedLimits.SpeedLimits(config.speedLimits, config.maxSpeed)
road = simulation.road.Road(config.lanes, config.length, speedLimits)
simulation = SimulationManager(road, config.trafficGenerator, config.updateFrame)
representation = Representation(screen, road, simulation)

#[M]DataScience
datascience = DataScience(config, road, simulation, representation)

datascience.writeInput()
#[M]Fin DataScience

while simulation.running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            simulation.processKey(event.key)
            
    clock.tick_busy_loop(config.maxFps)
    dt = clock.get_time()
    #Aqui aparecen los datos de la simulacion.
    simulation.update(dt)
    representation.draw(dt * simulation.timeFactor)
    datascience.update(dt * simulation.timeFactor)

    pygame.display.flip()

print("Goodbye")
