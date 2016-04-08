import json
import numpy as np
import urllib.parse as urllib
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


class Collect():

    def __init__(self, config, road, simulation, representation):
        self.config = config
        self.road = road
        self.simulation = simulation
        self.representation = representation

        #self.matrix = np.zeros(shape=(self.road.getLanesCount(), self.road.getLength()))
        self.matrix = []

    def showParameters(self):
        #print(self.config.maxFps)
        parameters = {}
        parameters['lanes'] = self.config.lanes 
        parameters['lenght'] = self.config.length 
        parameters['maxSpeed'] = float("{0:.2f}".format(self.config.maxSpeed))
        try:
            parameters['maxLength'] = self.config.maxLength 
        except:
            print('No tiene maxLength')


        parameters['lanesPos'] = self.config.speedLimits[0].lanes 
        parameters['xPos'] = self.config.speedLimits[0].xPos 
        parameters['ticks'] = self.config.speedLimits[0].xPos 
        parameters['active'] = self.config.speedLimits[0].active 
        parameters['slowDownProbability'] = self.config.slowDownProbability
        parameters['laneChangeProbability'] = self.config.laneChangeProbability
        parameters['carPerUpdate'] = self.config.trafficGenerator.carPerUpdate

        #self.writeJSON(parameters, 'parameters')

        parametros = urllib.urlencode(parameters)
        url = 'https://dweet.io/dweet/for/simulation-parameters'
        full_url = url + '?' + parametros

        data = urllib2.urlopen(full_url)

        #print(json.dumps(parameters, indent=4))
        #print(json.dumps(self.simulation.trafficGenerator, default=self.jdefault))
        #print(parameters)

    #def jdefault(self, o):
        #return o.__dict__
        
    def writeJSON(self, obj, name):
        with open(name+'.json', 'w+') as f:
            json.dump(obj, f, indent=4)

    def writeCSV(self, obj):
        pass

    def showDisplayerInfo(self):

        info_d = self.representation.infoDisplayer 
        info = {}
        info['speedSimulation'] = info_d.timeFactor 
        totalCars, avgSpeed = self.road.getAvgCarSpeed()
        info['avg_speed_cars'] = float("{0:.2f}".format(avgSpeed))
        info['updates'] = self.road.updates 
        info['totalcars'] = totalCars
        info['deadcars'] = self.road.deadCars 
        congestion = totalCars*100/info_d.cells
        info['congestion'] = float("{0:.2f}".format(congestion))
        #info['cells'] = info_d.cells

        #self.writeJSON(info, 'displayer_info')
        parametros = urllib.urlencode(info)
        url = 'https://dweet.io/dweet/for/simulation'
        full_url = url + '?' + parametros

        data = urllib2.urlopen(full_url)
        #print(self.representation.infoDisplayer.text[0])
        #print(info_d.timeFactor)

    def showQueue(self):
        print(self.simulation.trafficGenerator.queue)
      
    def showRoad(self):
        lanes = self.simulation.road.lanes

        temp_lanes = []

        for car in lanes[0]:
            temp_lanes.append(0 if car is None else 1)

        
        self.matrix.append(temp_lanes)

        
        #print(self.matrix)
        self.writeJSON(self.matrix, 'road')
        #self.matrix = np.vstack((np.array(self.matrix),np.array(temp_lanes)))
        #print()
        #print(matrix)

    def sendDashboard(self):
        pass

    def showSpeedLimits(self):
        #print(self.simulation.road.speedLimits.maxSpeed)
        print('lanes: ' + str(self.simulation.road.speedLimits.speedLimits[0].lanes))
        print('xPos: ' + str(self.simulation.road.speedLimits.speedLimits[0].xPos))
        print('speedLimit: ' + str(self.simulation.road.speedLimits.speedLimits[0].speedLimit))
        print('ticks: ' + str(self.simulation.road.speedLimits.speedLimits[0].ticks))


