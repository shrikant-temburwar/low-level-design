package parkinglot

import (
	"fmt"
	"sync"
)

type ParkingLot struct {
	levels       []*ParkingLevel
	strategy     ParkingStrategy
	observers    []Observer
	currentLevel int
	sync.Mutex
}

var instance *ParkingLot
var once sync.Once

func GetInstance() *ParkingLot {
	once.Do(func() {
		instance = &ParkingLot{
			strategy:     &DefaultParkingStrategy{},
			currentLevel: 0,
		}
	})
	return instance
}

func (pl *ParkingLot) AddLevel(level *ParkingLevel) {
	pl.levels = append(pl.levels, level)
}

func (pl *ParkingLot) ParkVehicle(vehicle Vehicle) *ParkingSpot {
	pl.Lock()
	defer pl.Unlock()
	for i := 0; i < len(pl.levels); i++ {
		level := pl.levels[pl.currentLevel]
		spot := pl.strategy.FindSpot(level, vehicle.GetType())
		if spot != nil {
			spot.ParkVehicle(vehicle)
			pl.notifyObservers(fmt.Sprintf("Vehicle %s parked at spot %d on level %d", vehicle.GetLicensePlate(), spot.SpotID, spot.LevelID))
			pl.currentLevel = (pl.currentLevel + 1) % len(pl.levels)
			return spot
		}
		pl.currentLevel = (pl.currentLevel + 1) % len(pl.levels)
	}
	return nil
}

func (pl *ParkingLot) RemoveVehicle(vehicle Vehicle) {
	pl.Lock()
	defer pl.Unlock()
	spot := pl.FindVehicleSpot(vehicle)
	if spot != nil {
		spot.RemoveVehicle()
		pl.notifyObservers(fmt.Sprintf("Vehicle %s removed from spot %d on level %d", vehicle.GetLicensePlate(), spot.SpotID, spot.LevelID))
	}
}

func (pl *ParkingLot) FindVehicleSpot(vehicle Vehicle) *ParkingSpot {
	for _, level := range pl.levels {
		spot := level.FindVehicleSpot(vehicle)
		if spot != nil {
			return spot
		}
	}
	return nil
}

func (pl *ParkingLot) DisplayAvailability() {
	for _, level := range pl.levels {
		availableSpots := 0
		for _, spot := range level.Spots {
			if !spot.IsOccupied {
				availableSpots++
			}
		}
		fmt.Printf("Level %d: %d available spots\n", level.LevelID, availableSpots)
	}
}

func (pl *ParkingLot) AddObserver(observer Observer) {
	pl.observers = append(pl.observers, observer)
}

func (pl *ParkingLot) notifyObservers(message string) {
	for _, observer := range pl.observers {
		observer.Update(message)
	}
}
