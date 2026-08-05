from hub import Hub
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

      