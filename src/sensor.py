
"""
Sensor Module
-------------

This module defines the `Sensor` class and its subclasses for managing entry and exit sensors in a car park system.
Sensors detect vehicles, update the car park's state, and can simulate plate scanning.

Classes:
    Sensor: An abstract base class representing a generic car park sensor.
    EntrySensor: A subclass of `Sensor` that handles incoming vehicles.
    ExitSensor: A subclass of `Sensor` that handles outgoing vehicles.

Usage:
    entry_sensor = EntrySensor(id=1, car_park=carpark_instance)
    entry_sensor.detect_vehicle()

    exit_sensor = ExitSensor(id=2, car_park=carpark_instance)
    exit_sensor.detect_vehicle()
"""

from abc import ABC, abstractmethod


class Sensor:
    # Initiate the abstract base class for sensors in the car park.
    def __init__(self, id, is_active=False, car_park="Unknown"):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        sensor_info = f"Sensor of {id} at {car_park} with activity status of {is_active}"
        return sensor_info

    @abstractmethod
    def update_car_park(self, plate):
        # Abstract method to update the car park with vehicle information
        pass

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        # Method that detects a vehicle and updates the car park
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    # A sensor that detects vehicles entering the car park
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    # A sensor that detects vehicles exiting the car park
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

    def _scan_plate(self):
        return random.choice(self.car_park.plates)

