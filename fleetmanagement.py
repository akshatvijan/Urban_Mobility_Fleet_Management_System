from hub import Hub
class Fleet:
    def __init__(self):
        self.hubs={}
    def add_hub(self,hub):
        if hub not in self.hubs:
            self.hubs[hub]=[]
    def add_vehicles(self,hub,vehicle):
        if hub in self.hubs:
            if vehicle not in self.hubs[hub]:
                self.hubs[hub].append(vehicle)
            else:
                print("Vehicle already exist")
        else:
            print("NO hub found")