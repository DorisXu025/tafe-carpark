
"""
Display Module
--------------

This module defines the `Display` class, which represents a display unit in the car park system.
Displays are responsible for showing information such as available bays or other messages.

Classes:
    Display: Represents a car park display unit.

Usage:
    display = Display(id=1, car_park="Main Street Car Park")
    display.update({"message": "Welcome!", "is_on": True})
    print(display)
"""

class Display:
    def __init__(self, id, message="", is_on=False, car_park="Unknown"):
        # Initiate the display unit in a car park
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        display_info = f"{id}: Welcome to the {car_park}"
        return display_info

    def update(self, data):
        # Method that updates the display with the given data
        for key, value in data.items():
            setattr(self, key, value)
            # print(f"{key}: {value}")
