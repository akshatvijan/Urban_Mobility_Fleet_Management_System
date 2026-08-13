import pytest
from fleetmanagement import Fleet
from electricCar import electricCar
from electricScooter import electricScooter
def test_hub():
    fleet=Fleet()
    fleet.add_hub("airport")
    assert fleet.hubs[0].hub_name=="airport"

def test_hub_duplicatwe():
    fleet=Fleet()
    fleet.add_hub("airport")
    fleet.add_hub("airport")
    assert len(fleet.hubs)==1

def test_add_vehicle():
    fleet=Fleet()
    fleet.add_hub("airport")
    v=electricCar('cs202','bmw',80,4)
    fleet.add_vehicle('airport',v)
    assert len(fleet.hubs[0].vehicles)==1
    assert fleet.hubs[0].vehicles[0]==v

def test_add_vehicle_duplicate():
    fleet=Fleet()
    fleet.add_hub('airport')
    car1=electricCar('cs202','bmw',80,4)
    car2=electricCar('cs202','bw',10,8)
    fleet.add_vehicle('airport',car1)
    fleet.add_vehicle('airport',car2)
    assert len(fleet.hubs[0].vehicles)==1


def test_hub_not_found():
    fleet=Fleet()
    car=electricCar('cs202','bmw',80,4)
    with pytest.raises(ValueError):
        fleet.add_vehicle('airport',car)

def test_search_battery(capsys):
    fleet=Fleet()
    fleet.add_hub('airport')
    car1=electricCar('cs202','bmw',90,4)
    car2=electricCar('cs402','audi',70,4)
    fleet.add_vehicle('airport',car1)
    fleet.add_vehicle('airport',car2)
    fleet.search_battery()
    captured=(capsys.readouterr())
    print(captured)
    assert 'bmw' in captured.out
    assert 'audi' not in captured.out

def test_category():
    fleet=Fleet()
    fleet.add_hub('airport')
    car=electricCar('cs202','bmw',80,4)
    scooter=electricScooter('s202','ola',90,100)
    fleet.add_vehicle('airport',car)
    fleet.add_vehicle('airport',scooter)
    result=fleet.category()
    assert car in result["car"]
    assert scooter in result["scooter"]


def test_fleet_analytics(capsys): 
    fleet=Fleet()
    fleet.add_hub('airport')
    car1=electricCar('cs202','bmw',80,4)
    car2=electricCar('cs002','audi',80,8)
    scooter=electricScooter('s202','ola',90,100)
    
    car1.set_maintenance_status('Available')
    car2.set_maintenance_status('On Trip')
    scooter.set_maintenance_status('Available')

    fleet.add_vehicle('airport',car1)
    fleet.add_vehicle('airport',car2)
    fleet.add_vehicle('airport',scooter)

    fleet.Fleet_Analytics()
    captured=capsys.readouterr()
    assert 'Total number of available 2' in captured.out
    assert 'Total number of on trip 1' in captured.out


def test_alphabatic_sorting(capsys):
    fleet=Fleet()
    fleet.add_hub('airport')
    car1=electricCar('cs202','xmw',80,4)
    car2=electricCar('cs404','bmw',90,2)
    fleet.add_vehicle('airport',car1)
    fleet.add_vehicle('airport',car2)
    fleet.alphabatic_sorting()
    assert fleet.hubs[0].vehicles[0].model=='bmw'
    assert fleet.hubs[0].vehicles[1].model=='xmw'

def test_battery_percentage():
    fleet=Fleet()
    fleet.add_hub('airport')
    car1=electricCar('cs202','xmw',80,4)
    car2=electricCar('cs404','bmw',90,2)
    car1.set_battery_percentage(80)
    car2.set_battery_percentage(50)
    fleet.add_vehicle('airport',car2)
    fleet.add_vehicle('airport',car1)
    fleet.sort_battery()
    assert fleet.hubs[0].vehicles[0].get_battery_percentage()==80
    assert fleet.hubs[0].vehicles[1].get_battery_percentage()==50

def test_fare_price():
    @pytest.fixture
    def fleet():
        fleet=Fleet()
        fleet.add_hub('airport')
        fleet.add_hub('busstand')
        return fleet

    def test_method1(fleet):
        car1=electricCar('cs202','xmw',80,4)
        car2=electricCar('cs404','bmw',90,2)
        car1.set_rental_price(1000)
        car2.set_rental_price(2000)
        fleet.add_vehicle('airport',car1)
        fleet.add_vehicle('airport',car2)

        assert fleet.hubs[0].vehicles[0].get_rental_price()>fleet.hubs[0].vehicles[1].get_rental_price()
    

    def test_method2(fleet):
        car1=electricCar('cs202','xmw',80,4)
        scooter=electricScooter('s404','bmw',90,100)
        car1.set_rental_price(1000)
        scooter.set_rental_price(200)
        fleet.add_vehicle('airport',scooter)
        fleet.add_vehicle('airport',car1)

        assert fleet.hubs[0].vehicles[0].get_rental_price()>fleet.hubs[0].vehicles[1].get_rental_price()

    
@pytest.mark.parametrize("x,y",[(10,2.5),(20,4.0),(50,8.5),(100,16.0)])
def test_calculate_trip_cost(x,y):
    s1=electricScooter('s1','m1',80,100)
    
    assert s1.calculate_trip_cost(x)==y


@pytest.mark.parametrize("x,y",[ (10, 10.0),(20, 15.0),(50, 30.0),(100, 55.0)])
def test_calculate_trip_cost_car(x,y):
    car1=electricCar('cs202','nmw',90,4)
    assert car1.calculate_trip_cost(x)==y


@pytest.fixture
def fleet():
        fleet=Fleet()
        fleet.add_hub('airport')
        fleet.add_hub('busstand')
        return fleet

@pytest.mark.parametrize('vehicle',[electricCar('cs202','bmw',89,2),electricScooter('cs203','zmw',12,100)])
def test_parameter_fixture(fleet,vehicle):
    fleet.add_vehicle('airport',vehicle)
    assert vehicle in fleet.hubs[0].vehicles
    


def test_save_to_csv(tmp_path, fleet):
    car = electricCar("c1", "bmw", 80, 4)
    fleet.add_vehicle("airport", car)
    file = tmp_path / "fleet1.csv"
    fleet.save_to_csv(file)
    assert file.exists()

def test_get_battery_percentage():
    car = electricCar("c1", "bmw", 80, 4)
    assert car.get_battery_percentage()==80

def test_set_battery_percentage():
    car = electricCar("c1", "bmw", 80, 4)
    battery=car.set_battery_percentage(90)
    assert 90==car.get_battery_percentage()
    with pytest.raises(ValueError):
        assert car.set_battery_percentage(110)


def test_set_battery_percentage_validation():
    car = electricCar("c1", "bmw", 80, 4)
    battery=car.set_battery_percentage(90)
    
    with pytest.raises(ValueError):
        assert car.set_battery_percentage(110)

def test_get_maintenance_status():
    car = electricCar("c1", "bmw", 80, 4)
    assert car.get_maintenance_status()=='Available'


def test_set_maintenance_status():
    car = electricCar("c1", "bmw", 80, 4)
    car.set_maintenance_status('On Trip')
    assert 'On Trip'==car.get_maintenance_status()
    

def test_get_rental_price():
    car = electricCar("c1", "bmw", 80, 4)
    assert car.get_rental_price()==0

def test_set_rental_price():
    car = electricCar("c1", "bmw", 80, 4)
    car.set_rental_price(100)
    assert car.get_rental_price()==100
    
    