from vehicle import Vehicle
from electricCar import electricCar
from electricScooter import electricScooter
from fleetmanagement import Fleet
if __name__=="__main__":
    car1=electricCar(201,"car202",80,4)
    car2=electricCar(203,"car202",80,4)
    scooter1=electricScooter(10,"cs202",90,100)
    scooter2=electricScooter(10,"cs203",81,100)
    scooter3=electricScooter(11,"cs203",81,100)
    car1.set_maintenance_status("Available")
    car2.set_maintenance_status("On Trip")
    scooter1.set_maintenance_status("Available")
    scooter2.set_maintenance_status("Available")
    scooter3.set_maintenance_status("Under Maintenance")
    f1=Fleet()
    f1.add_hub("Airport")
    f1.add_hub("Bus-Stand")
    f1.add_vehicle("Airport",car1)
    f1.add_vehicle("Airport",car2)
    f1.add_vehicle("Airport",scooter1)
    f1.add_vehicle("Bus-Stand",scooter1)
    f1.add_vehicle("Bus-Stand",scooter2)
    f1.show_hubs()
    f1.show_vehicles("Airpo(rt")
    f1.search_hub("Airport")
    f1.search_battery()
    f1.category()
    f1.Fleet_Analytics()
    f1.alphabatic_sorting()
    string=input("Enter the choice of sorting (battery,fare)")
    f1.advance_sorting(string)
    f1.save_to_csv("data.csv")
    f1.load_csv("data.csv")

 
  
   

    