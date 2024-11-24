


class Sensor:
    def __init__(self, id, is_active=False, car_park="Unknown"):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        sensor_info = f"Sensor of {id} at {car_park} with activity status of {is_active}"
        return sensor_info


class EntrySensor(Sensor):
    pass


class ExitSensor(Sensor):
    pass
