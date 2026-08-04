from vehicle import Vehicle
from electricCar import electricCar
from electricScooter import electricScooter
if __name__=="__main__":
   car1=electricCar("c21","car-200",80,4)
scooter1=electricScooter("s12","s-302",20,80)
vehicle=[car1,scooter1]
for v in vehicle:
    if isinstance(v,electricCar):
        print(f"{v.model} fare={v.calculate_trip_cost(20)}")
    else:
        print(f"{v.model} fare={v.calculate_trip_cost(10)}")

   

    