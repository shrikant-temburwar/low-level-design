import unittest
from parking_lot.vehicle_factory import VehicleFactory
from parking_lot.vehicle import VehicleType

class TestVehicleFactory(unittest.TestCase):
    def test_create_car(self):
        car = VehicleFactory.create_vehicle("car", "ABC123")
        self.assertEqual(car.license_plate, "ABC123")
        self.assertEqual(car.vehicle_type, VehicleType.CAR)

    def test_create_motorcycle(self):
        motorcycle = VehicleFactory.create_vehicle("motorcycle", "M1234")
        self.assertEqual(motorcycle.license_plate, "M1234")
        self.assertEqual(motorcycle.vehicle_type, VehicleType.MOTORCYCLE)

    def test_create_truck(self):
        truck = VehicleFactory.create_vehicle("truck", "XYZ789")
        self.assertEqual(truck.license_plate, "XYZ789")
        self.assertEqual(truck.vehicle_type, VehicleType.TRUCK)

    def test_create_unknown_vehicle(self):
        with self.assertRaises(ValueError):
            VehicleFactory.create_vehicle("bicycle", "B1234")

if __name__ == "__main__":
    unittest.main()
