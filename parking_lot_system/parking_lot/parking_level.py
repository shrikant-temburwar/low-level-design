from .parking_spot import ParkingSpot
from .vehicle import VehicleType

class ParkingLevel:
    def __init__(self, level_id, num_spots):
        self.level_id = level_id
        self.spots = []
        for i in range(num_spots):
            if i % 3 == 0:
                self.spots.append(ParkingSpot(i, VehicleType.CAR, level_id))
            elif i % 3 == 1:
                self.spots.append(ParkingSpot(i, VehicleType.MOTORCYCLE, level_id))
            else:
                self.spots.append(ParkingSpot(i, VehicleType.TRUCK, level_id))

    def find_available_spot(self, vehicle_type):
        for spot in self.spots:
            if not spot.is_occupied and spot.spot_type == vehicle_type:
                return spot
        return None

    def find_vehicle_spot(self, vehicle):
        for spot in self.spots:
            if spot.vehicle == vehicle:
                return spot
        return None
