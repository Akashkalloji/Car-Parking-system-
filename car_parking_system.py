# =============================
# CAR PARKING SYSTEM IN PYTHON
# =============================


# Base Vehicle Class
class Vehicle:

    def __init__(self, vehicle_number, owner_name, parking_hours):
        self.vehicle_number = vehicle_number
        self.owner_name = owner_name
        self.parking_hours = parking_hours


# Car Class using Inheritance
class Car(Vehicle):

    def __init__(self, vehicle_number, owner_name, parking_hours):
        super().__init__(vehicle_number, owner_name, parking_hours)


# Parking Slot Class
class ParkingSlot:

    def __init__(self, slot_number):
        self.slot_number = slot_number
        self.occupied = False
        self.vehicle = None

    # Park Vehicle
    def park_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.occupied = True

    # Remove Vehicle
    def remove_vehicle(self):
        self.vehicle = None
        self.occupied = False


# Parking System Class
class ParkingSystem:

    def __init__(self, total_slots):
        self.slots = []

        for i in range(1, total_slots + 1):
            self.slots.append(ParkingSlot(i))

    # Park Car
    def park_car(self, car):

        for slot in self.slots:

            if not slot.occupied:

                slot.park_vehicle(car)

                print("\nCar Parked Successfully!")
                print("Allocated Slot Number:", slot.slot_number)

                return

        print("\nParking is Full!")

    # Remove Car
    def remove_car(self, vehicle_number):

        for slot in self.slots:

            if slot.occupied and slot.vehicle.vehicle_number.lower() == vehicle_number.lower():

                vehicle = slot.vehicle

                fee = self.calculate_parking_fee(vehicle.parking_hours)

                print("\nVehicle Removed Successfully!")
                print("Vehicle Number :", vehicle.vehicle_number)
                print("Owner Name     :", vehicle.owner_name)
                print("Parking Fee    : ₹", fee)

                slot.remove_vehicle()

                return

        print("\nVehicle Not Found!")

    # Parking Fee Calculation
    def calculate_parking_fee(self, hours):
        return hours * 50

    # Display Parking Status
    def display_parking_status(self):

        print("\n========== Parking Status ==========")

        for slot in self.slots:

            if slot.occupied:

                vehicle = slot.vehicle

                print(
                    f"Slot {slot.slot_number} | "
                    f"Vehicle No: {vehicle.vehicle_number} | "
                    f"Owner: {vehicle.owner_name}"
                )

            else:

                print(f"Slot {slot.slot_number} is Empty")


# Main Program
def main():

    parking_system = ParkingSystem(5)

    while True:

        print("\n========== CAR PARKING SYSTEM ==========")
        print("1. Park Car")
        print("2. Remove Car")
        print("3. Display Parking Status")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        # Park Car
        if choice == "1":

            vehicle_number = input("Enter Vehicle Number: ")
            owner_name = input("Enter Owner Name: ")

            try:
                hours = int(input("Enter Parking Hours: "))

                if hours <= 0:
                    print("Invalid Parking Hours!")
                    continue

            except ValueError:
                print("Please Enter Valid Number!")
                continue

            car = Car(vehicle_number, owner_name, hours)

            parking_system.park_car(car)

        # Remove Car
        elif choice == "2":

            remove_vehicle = input("Enter Vehicle Number to Remove: ")

            parking_system.remove_car(remove_vehicle)

        # Display Status
        elif choice == "3":

            parking_system.display_parking_status()

        # Exit
        elif choice == "4":

            print("\nThank You for Using Car Parking System!")
            break

        else:

            print("\nInvalid Choice! Please Try Again.")


# Run Program
main()