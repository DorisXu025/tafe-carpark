"""
CarPark Module
--------------

This module provides the `CarPark` class for managing a car park system. It allows for the registration of
sensors and displays, tracking of vehicles entering and exiting, and real-time updates on the number of
available parking bays. The car park can also log activities and handle configuration files for persistent settings.

Classes:
    CarPark: Represents a car park system with sensors, displays, and vehicle tracking functionality.

Dependencies:
    - `Sensor`: Represents sensors monitoring the car park.
    - `Display`: Represents displays showing car park information.
    - `Path` (from pathlib): Used to handle file paths for logging and configuration.
    - `datetime`: Used for timestamping car activity logs.
    - `json`: Used for reading and writing configuration files.

Usage:
    carpark = CarPark(location="Downtown", capacity=300)
    carpark.add_car("ABC123")
    carpark.remove_car("ABC123")
    carpark.write_config()
    new_carpark = CarPark.from_config()
"""


from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json


class CarPark:
    def __init__(self, location='Unknown', capacity=500, plates=None, sensors=None, displays=None, log_file=Path("log.txt")):
        # Initializes the CarPark instance with maximum capacity at 500 car bays
        self.location = location
        self.capacity = capacity
        self.sensors = sensors or []  # uses the first value if not None, otherwise uses the second value
        self.plates = plates or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        # create the file if it doesn't exist:
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        carpark_info = f"Car Park at {location}, with {capacity}"
        return carpark_info

    def register(self, component):
        # Method that can register a component (Sensor or Display) to the car park
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        # Method that adds a car to the car park, updates displays, and logs the activity
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        # Method that removes a car from the car park, updates displays, and logs the activity
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    def update_displays(self):
        # Method that updates connected displays with real-time info including available bays and temperature
        data = {
            "available_bays": self.available_bays,
            "temperature": 25
        }
        for display in self.displays:
            display.update(data)

    @property
    def available_bays(self):
        # Method calculates the number of available parking bays
        if self.capacity - len(self.plates) <= 0:
            return 0
        else:
            return self.capacity - len(self.plates)

    def _log_car_activity(self, plate, action):
        # Method that logs the entry or exit of a car to the log file
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now()}\n")

    def write_config(self):
        # Method that writes the car park's configuration to a JSON file
        with open("config.json", "w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        # Method that creates a `CarPark` instance from a configuration file
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])


