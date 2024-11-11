import unittest
from parking_lot.parking_lot import ParkingLot
from parking_lot.parking_level import ParkingLevel
from parking_lot.vehicle import Car, Truck, Motorcycle

class TestParkingLot(unittest.TestCase):
    def setUp(self):
        self.parking_lot = ParkingLot.get_instance()
        self.parking_lot.add_level(ParkingLevel(1, 100))
        self.parking_lot.add_level(ParkingLevel(2, 80))

    def test_park_vehicle(self):
        car = Car("ABC123")
        spot = self.parking_lot.park_vehicle(car)
        self.assertIsNotNone(spot)

    def test_remove_vehicle(self):
        motorcycle = Motorcycle("M1234")
        self.parking_lot.park_vehicle(motorcycle)
        self.parking_lot.remove_vehicle(motorcycle)
        spot = self.parking_lot.find_vehicle_spot(motorcycle)
        self.assertIsNone(spot)

    def test_display_availability(self):
        self.parking_lot.display_availability()

if __name__ == "__main__":
    unittest.main()
