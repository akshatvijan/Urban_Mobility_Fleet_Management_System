from vehicle import Vehicle
from electricCar import electricCar
from electricScooter import electricScooter
from fleetmanagement import Fleet
if __name__=="__main__":
    car1=electricCar(201,"car202",80,4)
    scooter1=electricScooter(10,"cs202",80,100)
    scooter2=electricScooter(10,"cs203",81,100)
    scooter3=electricScooter(11,"cs203",81,100)
    f1=Fleet()
    f1.add_hub("Airport")
    f1.add_hub("Bus Stand")
    f1.add_vehicles("Airport",car1)
    f1.add_vehicles("Bus Stand",scooter1)
    f1.add_vehicles("Bus Stand",scooter2)
    f1.add_vehicles("Bus Stand",scooter3)
    print(f1.hubs)
    
    
  
   

    