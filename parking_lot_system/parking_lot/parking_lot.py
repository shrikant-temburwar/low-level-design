import threading
from .parking_level import ParkingLevel
from .parking_strategy import DefaultParkingStrategy
from .observer import Subject

class ParkingLot(Subject):
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, num_levels=None, spots_per_level=None):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ParkingLot, cls).__new__(cls)
                if num_levels is not None and spots_per_level is not None:
                    cls._instance.__init__(num_levels, spots_per_level)
            return cls._instance

    def __init__(self, num_levels, spots_per_level):
        if not hasattr(self, 'initialized'):  # Ensure __init__ is only called once
            super().__init__()
            self.levels = [ParkingLevel(i + 1, spots_per_level) for i in range(num_levels)]
            self.strategy = DefaultParkingStrategy()
            self.current_level = 0
            self.initialized = True

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ParkingLot(0, 0)  # Default initialization
        return cls._instance

    def add_level(self, level):
        self.levels.append(level)

    def park_vehicle(self, vehicle):
        for _ in range(len(self.levels)):
            level = self.levels[self.current_level]
            spot = self.strategy.find_spot(level, vehicle.vehicle_type)
            if spot:
                spot.park_vehicle(vehicle)
                self.notify_observers(f"Vehicle {vehicle.license_plate} parked at spot {spot.spot_id} on level {spot.level_id}")
                self.current_level = (self.current_level + 1) % len(self.levels)
                return spot
            self.current_level = (self.current_level + 1) % len(self.levels)
        return None

    def remove_vehicle(self, vehicle):
        spot = self.find_vehicle_spot(vehicle)
        if spot:
            spot.remove_vehicle()
            self.notify_observers(f"Vehicle {vehicle.license_plate} removed from spot {spot.spot_id} on level {spot.level_id}")

    def find_vehicle_spot(self, vehicle):
        for level in self.levels:
            spot = level.find_vehicle_spot(vehicle)
            if spot:
                return spot
        return None

    def display_availability(self):
        for level in self.levels:
            available_spots = sum(not spot.is_occupied for spot in level.spots)
            print(f"Level {level.level_id}: {available_spots} available spots")
