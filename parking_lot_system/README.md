# Parking Lot System

## Description
This project implements a parking lot system with multiple levels, each containing a certain number of parking spots. The system supports different types of vehicles, such as cars, motorcycles, and trucks. Each parking spot can accommodate a specific type of vehicle. The system assigns a parking spot to a vehicle upon entry and releases it when the vehicle exits. It tracks the availability of parking spots and provides real-time information to customers. The system handles multiple entry and exit points and supports concurrent access.

## Requirements
- The parking lot should have multiple levels, each level with a certain number of parking spots.
- The parking lot should support different types of vehicles, such as cars, motorcycles, and trucks.
- Each parking spot should be able to accommodate a specific type of vehicle.
- The system should assign a parking spot to a vehicle upon entry and release it when the vehicle exits.
- The system should track the availability of parking spots and provide real-time information to customers.
- The system should handle multiple entry and exit points and support concurrent access.

## Design Patterns Used
- **Singleton Pattern**: Ensures only one instance of the `ParkingLot` class exists.
- **Factory Pattern**: Used to create instances of different vehicle types.
- **Strategy Pattern**: Used to determine the parking strategy for different types of vehicles.
- **Observer Pattern**: Used to notify customers about the availability of parking spots.


## Steps to Run

### Prerequisites
- Python 3.x installed on your machine.

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/parking_lot_system.git
    cd parking_lot_system
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application
1. Navigate to the project directory:
    ```sh
    cd parking_lot_system
    ```

2. Run the main application:
    ```sh
    python main.py
    ```

### Running the Tests
1. Navigate to the project directory:
    ```sh
    cd parking_lot_system
    ```

2. Run the tests using `unittest`:
    ```sh
    python -m unittest discover tests
    ```

## Usage
The `ParkingLotDemo` class in `main.py` demonstrates the usage of the parking lot system, including parking and unparking vehicles and displaying the availability of spots.


