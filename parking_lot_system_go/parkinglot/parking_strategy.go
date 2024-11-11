package parkinglot

type ParkingStrategy interface {
	FindSpot(level *ParkingLevel, vehicleType VehicleType) *ParkingSpot
}

type DefaultParkingStrategy struct{}

func (s *DefaultParkingStrategy) FindSpot(level *ParkingLevel, vehicleType VehicleType) *ParkingSpot {
	for _, spot := range level.Spots {
		if !spot.IsOccupied && spot.SpotType == vehicleType {
			return spot
		}
	}
	return nil
}
