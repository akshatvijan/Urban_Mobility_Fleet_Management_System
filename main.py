from vehicle import Vehicle
if __name__=="__main__":
    v1=Vehicle("v-1","car-1",80)
    print(v1.model)
    v1.set_battery_percentage(80)
    v1.set_maintenance_status("Available")
    v1.set_rental_price(1000)
    print("battery is ",v1.get_battery_percentage())
    print("maintenance status is ",v1.get_maintenance_status())
    print("rental price is ",v1.get_rental_price())