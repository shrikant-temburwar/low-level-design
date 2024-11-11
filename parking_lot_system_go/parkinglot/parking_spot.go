package parkinglot

import "sync"

type ParkingSpot struct {
	SpotID     int
	SpotType   VehicleType
	LevelID    int
	IsOccupied bool
	Vehicle    Vehicle
	sync.Mutex
}

func NewParkingSpot(spotID int, spotType VehicleType, levelID int) *ParkingSpot {
	return &ParkingSpot{
		SpotID:   spotID,
		SpotType: spotType,
		LevelID:  levelID,
	}
}

func (ps *ParkingSpot) ParkVehicle(vehicle Vehicle) bool {
	ps.Lock()
	defer ps.Unlock()
	if !ps.IsOccupied && ps.SpotType == vehicle.GetType() {
		ps.Vehicle = vehicle
		ps.IsOccupied = true
		return true
	}
	return false
}

func (ps *ParkingSpot) RemoveVehicle() {
	ps.Lock()
	defer ps.Unlock()
	ps.Vehicle = nil
	ps.IsOccupied = false
}
