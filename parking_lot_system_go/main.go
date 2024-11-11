package main

import (
	"fmt"
	"parking_lot_system_go/parkinglot"
)

func main() {
	parkingLot := parkinglot.GetInstance()
	observer := &parkinglot.ParkingLotObserver{}
	parkingLot.AddObserver(observer)

	parkingLot.AddLevel(parkinglot.NewParkingLevel(1, 100))
	parkingLot.AddLevel(parkinglot.NewParkingLevel(2, 80))

	car := parkinglot.VehicleFactory("car", "ABC123")
	truck := parkinglot.VehicleFactory("truck", "XYZ789")
	motorcycle := parkinglot.VehicleFactory("motorcycle", "M1234")

	// Park vehicles
	parkingLot.ParkVehicle(car)
	parkingLot.ParkVehicle(truck)
	parkingLot.ParkVehicle(motorcycle)

	// Display availability
	parkingLot.DisplayAvailability()

	// Find and display vehicle spots
	carSpot := parkingLot.FindVehicleSpot(car)
	truckSpot := parkingLot.FindVehicleSpot(truck)
	motorcycleSpot := parkingLot.FindVehicleSpot(motorcycle)

	if carSpot != nil {
		fmt.Printf("Car is parked at spot %d on level %d\n", carSpot.SpotID, carSpot.LevelID)
	}
	if truckSpot != nil {
		fmt.Printf("Truck is parked at spot %d on level %d\n", truckSpot.SpotID, truckSpot.LevelID)
	}
	if motorcycleSpot != nil {
		fmt.Printf("Motorcycle is parked at spot %d on level %d\n", motorcycleSpot.SpotID, motorcycleSpot.LevelID)
	}

	// Unpark vehicle
	parkingLot.RemoveVehicle(motorcycle)

	// Display updated availability
	parkingLot.DisplayAvailability()
}
