from electricCar import electricCar
from electricScooter import electricScooter
from fleetmanagement import Fleet


if __name__ == "__main__":

    

    car1 = electricCar("c21", "car-200", 80, 4)
    car2 = electricCar("c22", "car-300", 90, 4)

    scooter1 = electricScooter("s12", "s-302", 90, 80)
    scooter2 = electricScooter("s13", "s-303", 81, 100)

    

    car1.set_maintenance_status("Available")
    car2.set_maintenance_status("On Trip")

    scooter1.set_maintenance_status("Available")
    scooter2.set_maintenance_status("Under Maintenance")

   

    fleet = Fleet()

    

    fleet.add_hub("Airport")
    fleet.add_hub("Bus-Stand")

    

    fleet.add_vehicle("Airport", car1)
    fleet.add_vehicle("Airport", scooter1)

    fleet.add_vehicle("Bus-Stand", car2)
    fleet.add_vehicle("Bus-Stand", scooter2)

    

    print("\n--- Hubs ---")
    fleet.show_hubs()


    print("\n--- Airport Vehicles ---")
    fleet.show_vehicles("Airport")

    print("\n--- Bus-Stand Vehicles ---")
    fleet.show_vehicles("Bus-Stand")

    

    print("\n--- Vehicles with Battery > 80% ---")
    fleet.search_battery()

    

    print("\n--- Vehicle Categories ---")
    fleet.category()

   

    print("\n--- Fleet Analytics ---")
    fleet.Fleet_Analytics()

   

    print("\n--- Alphabetical Sorting ---")
    fleet.alphabatic_sorting()

   

    print("\n--- Battery Sorting ---")
    fleet.advance_sorting("battery")

    print("\n--- Fare Sorting ---")
    fleet.advance_sorting("fare")

    

    print("\n--- Saving Fleet to CSV ---")
    fleet.save_to_csv("fleet.csv")

    print("\n--- Loading Fleet from CSV ---")

    new_fleet = Fleet()
    new_fleet.load_csv("fleet.csv")

    new_fleet.show_hubs()

    

    print("\n--- Saving Fleet to JSON ---")
    fleet.save_json("fleet.json")  