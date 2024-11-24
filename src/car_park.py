from sensor import Sensor
from display import Display


class CarPark:
    def __init__(self, location='Unknown', capacity=500, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.sensors = sensors or []  # uses the first value if not None, otherwise uses the second value
        self.plates = plates or []
        self.displays = displays or []

    def __str__(self):
        carpark_info = f"Car Park at {location}, with {capacity}"
        return carpark_info

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()

    def update_displays(self):
        data = {
            "available_bays": self.available_bays,
            "temperature": 25
        }
        for display in self.displays:
            display.update(data)

    @property
    def available_bays(self):
        if self.capacity - len(self.plates) <= 0:
            return 0
        else:
            return self.capacity - len(self.plates)


