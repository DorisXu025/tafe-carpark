
"""
Main Module for Car Park Simulation
------------------------------------

This script demonstrates the functionality of the `CarPark`, `EntrySensor`, `ExitSensor`, and `Display` classes
by simulating vehicle entry and exit operations in a car park.

Objects:
    car_park: An instance of `CarPark` representing the car park at Moondalup with a capacity of 500 and custom log file.
    entry_sensor: An instance of `EntrySensor` representing the entry point of the car park.
    exit_sensor: An instance of `ExitSensor` representing the exit point of the car park.
    display: An instance of `Display` showing a welcome message for the car park.

Simulation:
    - Simulates 10 cars entering the car park using the `EntrySensor`.
    - Simulates 2 cars exiting the car park using the `ExitSensor`.

Usage:
    Run this script to observe the interactions between car park components.
"""

from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display
import json



# Create a car park object with the location Moondalup, capacity 100, and log_file "moondalup.txt"
car_park = CarPark(location="Moondalup", capacity=500, log_file="moondalup_YX.txt")

# write configuration to config.json
car_park.write_config()  # Saves the car park's configuration

# Create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor(id=1, is_active=True, car_park=car_park)

# Create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExitSensor(id=2, is_active=True, car_park=car_park)

# Create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
display = Display(id=1, message="Welcome to Moondalup", is_on=True, car_park=car_park)

# Drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
for i in range(10):
    entry_sensor.update_car_park(f"CAR-{i:03d}")

# Drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
for i in range(2):
    exit_sensor.update_car_park(f"CAR-{i:03d}")