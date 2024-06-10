 ___________________                     _______________________
|     Vehicle       |                   |      ParkingSpot       |
|___________________|                   |________________________|
| - licensePlate   |                   | - spotNumber           |
| - vehicleType    |                   | - spotType             |
|__________________|                   | - isAvailable          |
| + Vehicle()      |                   |________________________|
|__________________|                   | + ParkingSpot()       |
                                       |________________________|

                    ___________________
                   |     ParkingLot    |
                   |___________________|
                   | - name            |
                   | - capacity        |
                   | - availableSpots  |
                   | - occupiedSpots   |
                   |___________________|
                   | + parkVehicle()   |
                   | + removeVehicle() |
                   | + findAvailableSpot()|
                   |___________________|


class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

class ParkingSpot:
    def __init__(self, spot_number, spot_type, is_available=True):
        self.spot_number = spot_number
        self.spot_type = spot_type
        self.is_available = is_available
        self.vehicle = None  # To keep track of which vehicle is parked

class ParkingLot:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.available_spots = []
        self.occupied_spots = []
        self.initialize_spots()

    def initialize_spots(self):
        # Initialize the parking spots (for simplicity, assume half for cars, half for bikes)
        for i in range(1, self.capacity // 2 + 1):
            self.available_spots.append(ParkingSpot(i, 'car'))
        for i in range(self.capacity // 2 + 1, self.capacity + 1):
            self.available_spots.append(ParkingSpot(i, 'bike'))

    def park_vehicle(self, vehicle):
        spot = self.find_available_spot(vehicle.vehicle_type)
        if spot:
            spot.is_available = False
            spot.vehicle = vehicle
            self.occupied_spots.append(spot)
            self.available_spots.remove(spot)
            print(f"Vehicle with license plate {vehicle.license_plate} parked at spot {spot.spot_number}.")
        else:
            print(f"No available spots for vehicle type {vehicle.vehicle_type}.")

    def remove_vehicle(self, vehicle):
        for spot in self.occupied_spots:
            if spot.vehicle.license_plate == vehicle.license_plate:
                spot.is_available = True
                spot.vehicle = None
                self.available_spots.append(spot)
                self.occupied_spots.remove(spot)
                print(f"Vehicle with license plate {vehicle.license_plate} removed from spot {spot.spot_number}.")
                return
        print(f"Vehicle with license plate {vehicle.license_plate} not found in the parking lot.")

    def find_available_spot(self, vehicle_type):
        for spot in self.available_spots:
            if spot.spot_type == vehicle_type and spot.is_available:
                return spot
        return None

# Example usage
if __name__ == "__main__":
    parking_lot = ParkingLot("Main Parking Lot", 10)

    vehicle1 = Vehicle("ABC123", "car")
    vehicle2 = Vehicle("XYZ789", "bike")

    parking_lot.park_vehicle(vehicle1)
    parking_lot.park_vehicle(vehicle2)

    parking_lot.remove_vehicle(vehicle1)
    parking_lot.remove_vehicle(vehicle2)
