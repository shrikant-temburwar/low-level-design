import unittest
from parking_lot.vehicle import Car, Motorcycle, Truck

class TestVehicle(unittest.TestCase):
    def test_car_creation(self):
        car = Car("ABC123")
        self.assertEqual(car.license_plate, "ABC123")
        self.assertEqual(car.vehicle_type.value, "car")

    def test_motorcycle_creation(self):
        motorcycle = Motorcycle("M1234")
        self.assertEqual(motorcycle.license_plate, "M1234")
        self.assertEqual(motorcycle.vehicle_type.value, "motorcycle")

    def test_truck_creation(self):
        truck = Truck("XYZ789")
        self.assertEqual(truck.license_plate, "XYZ789")
        self.assertEqual(truck.vehicle_type.value, "truck")

if __name__ == "__main__":
    unittest.main()
