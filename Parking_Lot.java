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


import java.util.ArrayList;
import java.util.List;

class Vehicle {
    private String licensePlate;
    private String vehicleType;

    public Vehicle(String licensePlate, String vehicleType) {
        this.licensePlate = licensePlate;
        this.vehicleType = vehicleType;
    }

    public String getLicensePlate() {
        return licensePlate;
    }

    public String getVehicleType() {
        return vehicleType;
    }
}

class ParkingSpot {
    private int spotNumber;
    private String spotType;
    private boolean isAvailable;
    private Vehicle parkedVehicle; // To keep track of the parked vehicle

    public ParkingSpot(int spotNumber, String spotType, boolean isAvailable) {
        this.spotNumber = spotNumber;
        this.spotType = spotType;
        this.isAvailable = isAvailable;
        this.parkedVehicle = null;
    }

    public int getSpotNumber() {
        return spotNumber;
    }

    public String getSpotType() {
        return spotType;
    }

    public boolean isAvailable() {
        return isAvailable;
    }

    public Vehicle getParkedVehicle() {
        return parkedVehicle;
    }

    public void parkVehicle(Vehicle vehicle) {
        this.isAvailable = false;
        this.parkedVehicle = vehicle;
    }

    public void removeVehicle() {
        this.isAvailable = true;
        this.parkedVehicle = null;
    }
}

class ParkingLot {
    private String name;
    private int capacity;
    private List<ParkingSpot> availableSpots;
    private List<ParkingSpot> occupiedSpots;

    public ParkingLot(String name, int capacity) {
        this.name = name;
        this.capacity = capacity;
        this.availableSpots = new ArrayList<>();
        this.occupiedSpots = new ArrayList<>();
        initializeSpots();
    }

    private void initializeSpots() {
        // Initialize the parking spots (for simplicity, assume half for cars, half for bikes)
        for (int i = 1; i <= capacity / 2; i++) {
            availableSpots.add(new ParkingSpot(i, "car", true));
        }
        for (int i = capacity / 2 + 1; i <= capacity; i++) {
            availableSpots.add(new ParkingSpot(i, "bike", true));
        }
    }

    public void parkVehicle(Vehicle vehicle) {
        ParkingSpot spot = findAvailableSpot(vehicle.getVehicleType());
        if (spot != null) {
            spot.parkVehicle(vehicle);
            occupiedSpots.add(spot);
            availableSpots.remove(spot);
            System.out.println("Vehicle with license plate " + vehicle.getLicensePlate() + " parked at spot " + spot.getSpotNumber() + ".");
        } else {
            System.out.println("No available spots for vehicle type " + vehicle.getVehicleType() + ".");
        }
    }

    public void removeVehicle(Vehicle vehicle) {
        for (ParkingSpot spot : occupiedSpots) {
            if (spot.getParkedVehicle().getLicensePlate().equals(vehicle.getLicensePlate())) {
                spot.removeVehicle();
                availableSpots.add(spot);
                occupiedSpots.remove(spot);
                System.out.println("Vehicle with license plate " + vehicle.getLicensePlate() + " removed from spot " + spot.getSpotNumber() + ".");
                return;
            }
        }
        System.out.println("Vehicle with license plate " + vehicle.getLicensePlate() + " not found in the parking lot.");
    }

    public ParkingSpot findAvailableSpot(String vehicleType) {
        for (ParkingSpot spot : availableSpots) {
            if (spot.getSpotType().equals(vehicleType) && spot.isAvailable()) {
                return spot;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        ParkingLot parkingLot = new ParkingLot("Main Parking Lot", 10);

        Vehicle vehicle1 = new Vehicle("ABC123", "car");
        Vehicle vehicle2 = new Vehicle("XYZ789", "bike");

        parkingLot.parkVehicle(vehicle1);
        parkingLot.parkVehicle(vehicle2);

        parkingLot.removeVehicle(vehicle1);
        parkingLot.removeVehicle(vehicle2);
    }
}
