from .vehicle import Car, Motorcycle, Truck

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type, license_plate):
        if vehicle_type == "car":
            return Car(license_plate)
        elif vehicle_type == "motorcycle":
            return Motorcycle(license_plate)
        elif vehicle_type == "truck":
            return Truck(license_plate)
        else:
            raise ValueError("Unknown vehicle type")
