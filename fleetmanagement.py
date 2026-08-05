class Fleet:
    def __init__(self):
        self.hubs={}
    def add_hub(self,hub):
        if hub not in self.hubs:
            self.hubs[hub]=[]
    def add_vehicles(self,hub,vehicle):
        if hub in self.hubs:
            exsisting_vehicle=[v for v in self.hubs[hub] if v==vehicle]
            if exsisting_vehicle:
                print("Vehicle already exist")
            else:
                self.hubs[hub].append(vehicle)
                
            
        else:
            print("Hub not exist")


    def search_hub(self,hub):
        if hub in self.hubs:
            for v in self.hubs[hub]:
                print(v)
        else:
            print("Hub not found")
    
    def show_all_hubs(self):
       for hub,value in self.hubs.items():
        print(f"{hub}  {value}")
 
    def search_battery(self):
        list_vehicle=[]
        for v in self.hubs.values():
            list_vehicle.extend(v)
        battery_80 = list(filter(lambda x: x.get_battery_percentage() > 80, list_vehicle))
        print("vehicle with battery greater than 80 ",)
        for v in battery_80:
            
            print(v,end=' ')




        


        