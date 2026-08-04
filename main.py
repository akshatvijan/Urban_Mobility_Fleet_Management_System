from vehicle import Vehicle
from electricCar import electricCar
from electricScooter import electricScooter
if __name__=="__main__":
   car1=electricCar("201","car-v200",80,4)
   scooter1=electricScooter("33","s-c123",20,100)
   print(car1.get_battery_percentage())
   car1.set_battery_percentage(20)
   print(car1.get_battery_percentage())
   print("status ",scooter1.get_maintenance_status()) 
   scooter1.set_maintenance_status("Not available")
   print("status ",scooter1.get_maintenance_status())
   print(car1.seating_capacity)
   print(scooter1.max_speed_limit)

   

    