import unittest
from parking_lot.parking_spot import ParkingSpot
from parking_lot.vehicle import Car, VehicleType

class TestParkingSpot(unittest.TestCase):
    def setUp(self):
        self.spot = ParkingSpot(1, VehicleType.CAR, 1)  # Add level_id

    def test_park_vehicle(self):
        car = Car("ABC123")
        result = self.spot.park_vehicle(car)
        self.assertTrue(result)
        self.assertTrue(self.spot.is_occupied)

    def test_remove_vehicle(self):
        car = Car("ABC123")
        self.spot.park_vehicle(car)
        self.spot.remove_vehicle()
        self.assertFalse(self.spot.is_occupied)

if __name__ == "__main__":
    unittest.main()
