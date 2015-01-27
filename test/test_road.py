import unittest, functools
import config
from simulation.road import Road
from simulation.car import Car
from simulation.speedLimits import *

class TestRoad(unittest.TestCase):
    def setUp(self):
        speedLimits = SpeedLimits([])
        self.road = Road(3, 100, speedLimits)

    def test_init(self):
        r = Road(3, 20, None)
        self.assertEqual(3, r.getLanesCount())
        self.assertEqual(20, r.getLength())
        self.assertEqual(r.carCount(), 0)

        # road is empty, so we should be able to add a car
        self.assertTrue(r.addCar())
        self.assertEqual(1, r.carCount())

    def test__getMaxSpeedAt(self):
        speedLimits = SpeedLimits( [ SpeedLimit(range=((25, 0), (30, 0)), limit=1, ticks=0) ] )
        road = Road(1, 50, speedLimits)
        self.assertEqual(config.maxSpeed, road.getMaxSpeedAt((0,0)))
        self.assertEqual(config.maxSpeed, road.getMaxSpeedAt((24,0)))
        self.assertEqual(config.maxSpeed, road.getMaxSpeedAt((31,0)))
        self.assertEqual(1, road.getMaxSpeedAt((25,0)))
        self.assertEqual(1, road.getMaxSpeedAt((26,0)))
        self.assertEqual(1, road.getMaxSpeedAt((30,0)))


    def test_inBounds(self):
        r = Road(3, 100, None)
        self.assertFalse(r.inBounds((-1, -1)))
        self.assertFalse(r.inBounds((1, -1)))
        self.assertFalse(r.inBounds((-1, 2)))
        self.assertFalse(r.inBounds((100, 3)))
        self.assertTrue(r.inBounds((1, 1)))
        self.assertTrue(r.inBounds((0, 0)))
        self.assertTrue(r.inBounds((99, 2)))

    def test_placeObject(self):
        r = Road(3, 40, None)
        car1, car2 = Car(r, (20, 0)), Car(r, (30, 0))
        self.assertTrue(r.placeObjects([car1, car2]))
        self.assertEqual(2, r.carCount())
        self.assertEqual(9, r.distanceToNextThing(car1.pos))
        self.assertTrue(r.distanceToNextThing(car2.pos) >= r.getLength())
        car3 = Car(r, (21, 0))
        self.assertTrue( r.placeObject(car3) )
        self.assertEqual(3, r.carCount())
        self.assertEqual(0, r.distanceToNextThing(car1.pos))
        self.assertEqual(8, r.distanceToNextThing(car3.pos))

    def test_tunneling(self):
        # obstacle
        speedLimits = SpeedLimits( [SpeedLimit.createObstacle((10,0))] )
        r = Road(1, 20, speedLimits)
        car = Car(r, (0,0))
        self.assertTrue(r.placeObject(car))
        for x in range(100):
            r.update()
        self.assertEqual(0, car.velocity)
        self.assertEqual((9, 0), car.pos)
