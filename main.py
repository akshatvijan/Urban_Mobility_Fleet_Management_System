from electricCar import electricCar
from electricScooter import electricScooter
from fleetmanagement import Fleet


if __name__ == "__main__":

    # -----------------------------
    # Create Vehicles
    # -----------------------------

    car1 = electricCar("c21", "car-200", 80, 4)
    car2 = electricCar("c22", "car-300", 90, 4)

    scooter1 = electricScooter("s12", "s-302", 90, 80)
    scooter2 = electricScooter("s13", "s-303", 81, 100)

    # -----------------------------
    # Set Maintenance Status
    # -----------------------------

    car1.set_maintenance_status("Available")
    car2.set_maintenance_status("On Trip")

    scooter1.set_maintenance_status("Available")
    scooter2.set_maintenance_status("Under Maintenance")

    # -----------------------------
    # Create Fleet
    # -----------------------------

    fleet = Fleet()

    # -----------------------------
    # UC1 / UC2
    # Add Hubs
    # -----------------------------

    fleet.add_hub("Airport")
    fleet.add_hub("Bus-Stand")

    # -----------------------------
    # Add Vehicles
    # -----------------------------

    fleet.add_vehicle("Airport", car1)
    fleet.add_vehicle("Airport", scooter1)

    fleet.add_vehicle("Bus-Stand", car2)
    fleet.add_vehicle("Bus-Stand", scooter2)

    # -----------------------------
    # Display Hubs
    # -----------------------------

    print("\n--- Hubs ---")
    fleet.show_hubs()

    # -----------------------------
    # Display Vehicles
    # -----------------------------

    print("\n--- Airport Vehicles ---")
    fleet.show_vehicles("Airport")

    print("\n--- Bus-Stand Vehicles ---")
    fleet.show_vehicles("Bus-Stand")

    # -----------------------------
    # UC8 - Battery Search
    # -----------------------------

    print("\n--- Vehicles with Battery > 80% ---")
    fleet.search_battery()

    # -----------------------------
    # UC9 - Category
    # -----------------------------

    print("\n--- Vehicle Categories ---")
    fleet.category()

    # -----------------------------
    # Fleet Analytics
    # -----------------------------

    print("\n--- Fleet Analytics ---")
    fleet.Fleet_Analytics()

    # -----------------------------
    # UC11 - Alphabetical Sorting
    # -----------------------------

    print("\n--- Alphabetical Sorting ---")
    fleet.alphabatic_sorting()

    # -----------------------------
    # UC12 - Advanced Sorting
    # -----------------------------

    print("\n--- Battery Sorting ---")
    fleet.advance_sorting("battery")

    print("\n--- Fare Sorting ---")
    fleet.advance_sorting("fare")

    # -----------------------------
    # UC13 - CSV Persistence
    # -----------------------------

    print("\n--- Saving Fleet to CSV ---")
    fleet.save_to_csv("fleet.csv")

    print("\n--- Loading Fleet from CSV ---")

    new_fleet = Fleet()
    new_fleet.load_csv("fleet.csv")

    new_fleet.show_hubs()

    # -----------------------------
    # UC14 - JSON Persistence
    # -----------------------------

    print("\n--- Saving Fleet to JSON ---")
    fleet.save_json("fleet.json")  