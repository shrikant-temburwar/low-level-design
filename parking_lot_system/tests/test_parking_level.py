import unittest
from parking_lot.parking_level import ParkingLevel
from parking_lot.vehicle import Car, Motorcycle, Truck

class TestParkingLevel(unittest.TestCase):
    def setUp(self):
        self.level = ParkingLevel(1, 10)

    def test_find_available_spot(self):
        car = Car("ABC123")
        spot = self.level.find_available_spot(car.vehicle_type)
        self.assertIsNotNone(spot)

    def test_find_vehicle_spot(self):
        motorcycle = Motorcycle("M1234")
        spot = self.level.find_available_spot(motorcycle.vehicle_type)
        spot.park_vehicle(motorcycle)
        found_spot = self.level.find_vehicle_spot(motorcycle)
        self.assertEqual(spot, found_spot)

if __name__ == "__main__":
    unittest.main()
