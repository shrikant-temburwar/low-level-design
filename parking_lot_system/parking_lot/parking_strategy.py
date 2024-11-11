class ParkingStrategy:
    def find_spot(self, level, vehicle_type):
        raise NotImplementedError

class DefaultParkingStrategy(ParkingStrategy):
    def find_spot(self, level, vehicle_type):
        for spot in level.spots:
            if not spot.is_occupied and spot.spot_type == vehicle_type:
                return spot
        return None
