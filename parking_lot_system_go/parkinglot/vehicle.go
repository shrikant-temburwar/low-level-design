package parkinglot

type VehicleType int

const (
	VehicleTypeCar VehicleType = iota
	VehicleTypeMotorcycle
	VehicleTypeTruck
)

type Vehicle interface {
	GetLicensePlate() string
	GetType() VehicleType
}

type BaseVehicle struct {
	LicensePlate string
	Type         VehicleType
}

func (v *BaseVehicle) GetLicensePlate() string {
	return v.LicensePlate
}

func (v *BaseVehicle) GetType() VehicleType {
	return v.Type
}

type Car struct {
	BaseVehicle
}

func NewCar(licensePlate string) *Car {
	return &Car{BaseVehicle{LicensePlate: licensePlate, Type: VehicleTypeCar}}
}

type Motorcycle struct {
	BaseVehicle
}

func NewMotorcycle(licensePlate string) *Motorcycle {
	return &Motorcycle{BaseVehicle{LicensePlate: licensePlate, Type: VehicleTypeMotorcycle}}
}

type Truck struct {
	BaseVehicle
}

func NewTruck(licensePlate string) *Truck {
	return &Truck{BaseVehicle{LicensePlate: licensePlate, Type: VehicleTypeTruck}}
}
