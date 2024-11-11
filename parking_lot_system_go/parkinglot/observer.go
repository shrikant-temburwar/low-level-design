package parkinglot

import "fmt"

type Observer interface {
	Update(message string)
}

type ParkingLotObserver struct{}

func (o *ParkingLotObserver) Update(message string) {
	fmt.Println("Notification:", message)
}

type Subject struct {
	observers []Observer
}

func (s *Subject) AddObserver(observer Observer) {
	s.observers = append(s.observers, observer)
}

func (s *Subject) RemoveObserver(observer Observer) {
	for i, obs := range s.observers {
		if obs == observer {
			s.observers = append(s.observers[:i], s.observers[i+1:]...)
			break
		}
	}
}

func (s *Subject) NotifyObservers(message string) {
	for _, observer := range s.observers {
		observer.Update(message)
	}
}
