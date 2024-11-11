import threading

class ParkingSpot:
    def __init__(self, spot_id, spot_type, level_id):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.level_id = level_id  # Add level_id to the ParkingSpot
        self.is_occupied = False
        self.vehicle = None
        self.lock = threading.Lock()

    def park_vehicle(self, vehicle):
        with self.lock:
            if not self.is_occupied and self.spot_type == vehicle.vehicle_type:
                self.vehicle = vehicle
                self.is_occupied = True
                return True
            return False

    def remove_vehicle(self):
        with self.lock:
            self.vehicle = None
            self.is_occupied = False
