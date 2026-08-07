from hub import Hub
from electricCar import electricCar
from electricScooter import electricScooter
from collections import defaultdict
class Fleet:
    def __init__(self):
        self.hubs=[]
    def add_hub(self,hub_name):
        for hub in self.hubs:
            if hub.hub_name==hub_name:
                print("Hub already exist")
                return
        new_hub=Hub(hub_name)
        self.hubs.append(new_hub)

    def add_vehicle(self,hub_name,vehicle):
        for hub in self.hubs:
            if hub.hub_name==hub_name:
               existing=[x for x in hub.vehicles if x==vehicle]
               if existing:
                print("vehicle already exist")
                return
               else:
                hub.vehicles.append(vehicle)
                return
        
             
                
        print("Hub not found")

    def show_hubs(self):
        for hub in self.hubs:
            print(hub.hub_name)

            
    def show_vehicles(self,hub_name):
        for hub in self.hubs:
            if hub.hub_name==hub_name:
                for v in hub.vehicles:
                    print(v)
                return
        print("hub not found")

    def search_hub(self,hub_name):
        for hub in self.hubs:
            if hub.hub_name==hub_name:
                for v in hub.vehicles:
                    print(v)
                return
        print("hub not found")

    def search_battery(self):
        vehicle_list=[]
        for hub in self.hubs:
            vehicle_list.extend(hub.vehicles)
        battery_80=list(filter(lambda x: x.get_battery_percentage()>80,vehicle_list))
        for b in battery_80:
            print(b)

    def category(self):
        category=defaultdict(list)
        vehicle_list=[]
        for hub in self.hubs:
            vehicle_list.extend(hub.vehicles)
        for v in vehicle_list:
            if isinstance(v,electricCar):
                category['car'].append(v)
            elif isinstance(v,electricScooter):
                category['scooter'].append(v)
        print(category)

    def Fleet_Analytics(self):
        status_vehicle=[]
        avail=0
        ontrp=0
        notavail=0
        for hub in self.hubs:
            status_vehicle.extend(hub.vehicles)
        for v in status_vehicle:
            if v.get_maintenance_status()=="Available":
                avail+=1
            elif v.get_maintenance_status()=="On Trip":
                ontrp+=1
            else:
                notavail+=1
        print("Total number of available",avail)
        print("Total number of on trip",ontrp)
        print("Total number of under maintainence",notavail)

    def alphabatic_sorting(self):
        for hub in self.hubs:
            hub.vehicles.sort(key=lambda x:x.model)
        for hub in self.hubs:
            print(hub.hub_name, "Vehicles are (sorted)")
            for v in hub.vehicles:
               
                print(v)
        
        


            

        