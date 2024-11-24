from abc import ABC, abstractmethod


class Sensor:
    def __init__(self, id, is_active=False, car_park="Unknown"):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        sensor_info = f"Sensor of {id} at {car_park} with activity status of {is_active}"
        return sensor_info

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

    def _scan_plate(self):
        return random.choice(self.car_park.plates)

