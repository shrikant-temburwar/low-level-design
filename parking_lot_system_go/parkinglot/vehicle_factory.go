package parkinglot

import "fmt"

func VehicleFactory(vehicleType, licensePlate string) Vehicle {
	switch vehicleType {
	case "car":
		return NewCar(licensePlate)
	case "motorcycle":
		return NewMotorcycle(licensePlate)
	case "truck":
		return NewTruck(licensePlate)
	default:
		panic(fmt.Sprintf("Unknown vehicle type: %s", vehicleType))
	}
}
