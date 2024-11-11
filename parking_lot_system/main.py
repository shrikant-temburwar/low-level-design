from parking_lot.parking_lot import ParkingLot
from parking_lot.vehicle_factory import VehicleFactory
from parking_lot.observer import ParkingLotObserver
from parking_lot.parking_level import ParkingLevel

class ParkingLotDemo:
    @staticmethod
    def run():
        parking_lot = ParkingLot.get_instance()
        observer = ParkingLotObserver()
        parking_lot.add_observer(observer)

        parking_lot.add_level(ParkingLevel(1, 100))
        parking_lot.add_level(ParkingLevel(2, 80))

        car = VehicleFactory.create_vehicle("car", "ABC123")
        truck = VehicleFactory.create_vehicle("truck", "XYZ789")
        motorcycle = VehicleFactory.create_vehicle("motorcycle", "M1234")

        car2 = VehicleFactory.create_vehicle("car", "ABC1234")
        truck2 = VehicleFactory.create_vehicle("truck", "XYZ7894")
        motorcycle2 = VehicleFactory.create_vehicle("motorcycle", "M12345")

        # Park vehicles
        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(truck)
        parking_lot.park_vehicle(motorcycle)
        parking_lot.park_vehicle(car2)
        parking_lot.park_vehicle(truck2)
        parking_lot.park_vehicle(motorcycle2)

        # Display availability
        parking_lot.display_availability()

        # Find and display vehicle spots
        car_spot = parking_lot.find_vehicle_spot(car)
        truck_spot = parking_lot.find_vehicle_spot(truck)
        motorcycle_spot = parking_lot.find_vehicle_spot(motorcycle)


        if car_spot:
            print(f"Car is parked at spot {car_spot.spot_id} on level {car_spot.level_id}")
        if truck_spot:
            print(f"Truck is parked at spot {truck_spot.spot_id} on level {truck_spot.level_id}")
        if motorcycle_spot:
            print(f"Motorcycle is parked at spot {motorcycle_spot.spot_id} on level {motorcycle_spot.level_id}")

        # Unpark vehicle
        parking_lot.remove_vehicle(motorcycle)

        # Display updated availability
        parking_lot.display_availability()

if __name__ == "__main__":
    ParkingLotDemo.run()
