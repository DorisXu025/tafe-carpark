from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display



# TODO: create a car park object with the location Moondalup, capacity 100, and log_file "moondalup.txt"
car_park = CarPark(location="Moondalup", capacity=500, log_file="moondalup_YX.txt")

# TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor(id=1, is_active=True, car_park=car_park)

# TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExitSensor(id=2, is_active=True, car_park=car_park)

# TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
display = Display(id=1, message="Welcome to Moondalup", is_on=True, car_park=car_park)

# TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
for i in range(10):
    entry_sensor.update_car_park(f"CAR-{i:03d}")

# TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
for i in range(2):
    exit_sensor.update_car_park(f"CAR-{i:03d}")