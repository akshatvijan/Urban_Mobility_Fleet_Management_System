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

        