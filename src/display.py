


class Display:
    def __init__(self, id, message="", is_on=False, car_park="Unknown"):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        display_info = f"{id}: Welcome to the {car_park}"
        return display_info

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")
