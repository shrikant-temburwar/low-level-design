package parkinglot

type ParkingLevel struct {
	LevelID int
	Spots   []*ParkingSpot
}

func NewParkingLevel(levelID, numSpots int) *ParkingLevel {
	level := &ParkingLevel{
		LevelID: levelID,
	}
	for i := 0; i < numSpots; i++ {
		var spotType VehicleType
		switch i % 3 {
		case 0:
			spotType = VehicleTypeCar
		case 1:
			spotType = VehicleTypeMotorcycle
		case 2:
			spotType = VehicleTypeTruck
		}
		level.Spots = append(level.Spots, NewParkingSpot(i, spotType, levelID))
	}
	return level
}

func (pl *ParkingLevel) FindAvailableSpot(vehicleType VehicleType) *ParkingSpot {
	for _, spot := range pl.Spots {
		if !spot.IsOccupied && spot.SpotType == vehicleType {
			return spot
		}
	}
	return nil
}

func (pl *ParkingLevel) FindVehicleSpot(vehicle Vehicle) *ParkingSpot {
	for _, spot := range pl.Spots {
		if spot.Vehicle == vehicle {
			return spot
		}
	}
	return nil
}
