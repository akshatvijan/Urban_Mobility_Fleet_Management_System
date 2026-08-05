from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self,vehicle_id,model,battery_percentage):
        self.vehicle_id=vehicle_id
        self.model=model
        self.__battery_percentage=battery_percentage 
        self.__maintenance_status="Available"
        self.__rental_price=0
        
#getter for battery percentage
    def get_battery_percentage(self):
        return self.__battery_percentage

#setter for battery percentage
    def set_battery_percentage(self,battery):
        if not (0<=battery<=100):
            raise ValueError("Invalid battery percentage!")
        self.__battery_percentage=battery

#getter for maintenance status
    def get_maintenance_status(self):
        return self.__maintenance_status

#setter for maintenance status
    def set_maintenance_status(self,status):
        self.__maintenance_status=status

#getter for rental price
    def get_rental_price(self):
        return self.__rental_price

#setter for rental price         
    def set_rental_price(self,rent):
        self.__rental_price=rent

#abstractmethod    
    @abstractmethod
    def calculate_trip_cost(self,distance):
        pass

#eq function

    def __eq__(self,other):
        return self.vehicle_id==other.vehicle_id
    
