import random

class SimpleTrafficGenerator():
    def __init__(self, carPerUpdate=1):
        self.queue = 0
        self.carPerUpdate = carPerUpdate

    def generate(self, road):
        """ Generar a lo mas 'carPerUpdate' carros """

        amount = random.randint(0, self.carPerUpdate)
        self.tryGenerate(road, amount)

    def tryGenerate(self, road, amount):
        """ Agregar los carros y los que estan esperando"""

        added = road.pushCarsRandomly(amount + self.queue)
        self.queue += (amount - added)
        
        print('queue : ' + str(self.queue))


