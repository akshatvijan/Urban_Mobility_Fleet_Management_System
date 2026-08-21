from hub import Hub
import csv
import json
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
        raise ValueError("Hub not found")     
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
        return category


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
            


    def advance_sorting(self,choice):
        if(choice=='battery'):
            self.sort_battery()
        else:
            self.fare_price()


    def sort_battery(self):
        print("Sorted on basis of battery")
        for hub in self.hubs:
            hub.vehicles.sort(key=lambda x:x.get_battery_percentage(),reverse=True)
        for hub in self.hubs:
            print(hub.hub_name)
            for v in hub.vehicles:
                print(v)


    def fare_price(self):
        
        print("Sorted on basis of fare")
        for hub in self.hubs:
            hub.vehicles.sort(key=lambda x :x.get_rental_price(),reverse=True)
        for hub in self.hubs:
            print(hub.hub_name)
            for v in hub.vehicles:
                print(v)


    def save_to_csv(self,filename):
        with open(filename,"w") as f:
            writer=csv.writer(f)
            writer.writerow(['hub','type','vehicle_id','model','battery','extra'])
            for hub in self.hubs:
                for v in hub.vehicles:
                    if isinstance(v,electricCar):
                        writer.writerow([hub.hub_name,'car',v.vehicle_id,v.model,v.get_battery_percentage(),v.seating_capacity])
                    elif isinstance(v,electricScooter):
                        writer.writerow([hub.hub_name,'scooter',v.vehicle_id,v.model,v.get_battery_percentage(),v.max_speed_limit])


        print("Data uploaded")


    def load_csv(self, filename):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            
            for r in reader:
    
                hub_name = r["hub"]

                if r["type"] == "car":
                    vehicle = electricCar(
                        r["vehicle_id"],
                        r["model"],
                        int(r["battery"]),
                        int(r["extra"])
                    )

                elif r["type"] == "scooter":
                    vehicle = electricScooter(
                        r["vehicle_id"],
                        r["model"],
                        int(r["battery"]),
                        int(r["extra"])
                    )

                self.add_hub(hub_name)
                self.add_vehicle(hub_name, vehicle)

        print("Data loaded")

    def save_json(self,filename):
        data={
            "hubs":[]
        }

        

        for hub in self.hubs:
            hub_data={
                "hubname":hub.hub_name,
                "vehicles":[]
            }
            for v in hub.vehicles:
               
                if isinstance(v,electricCar):
                    vehicle_data={
                        'type':'Car',
                        'vehicle_id':v.vehicle_id,
                        'model':v.model,
                        'batter':v.get_battery_percentage(),
                        'extra':v.seating_capacity
                    }
                elif isinstance(v,electricScooter):
                    vehicle_data={
                        'type':'Scooter',
                        'vehicle_id':v.vehicle_id,
                        'model':v.model,
                        'batter':v.get_battery_percentage(),
                        'extra':v.max_speed_limit
                    }
                hub_data["vehicles"].append(vehicle_data)
            data["hubs"].append(hub_data)

        with open(filename,'w') as f:
            json.dump(data,f,indent=4)
            print('data uploaded')

            


                

            