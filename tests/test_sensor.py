
"""
Test Module for Sensor
------------------------

This module contains unit tests for the `EntrySensor` and `ExitSensor` classes to verify their functionality and interactions with the `CarPark` class.

Classes:
    TestSensor: A unittest test case class for testing the `EntrySensor` and `ExitSensor` classes.

Test Methods:
    setUp(): Prepares `EntrySensor`, `ExitSensor`, and `CarPark` instances for testing.
    test_entry_sensor_detection(): Verifies that the `EntrySensor` correctly adds a car to the car park.
    test_exit_sensor_detection(): Verifies that the `ExitSensor` correctly removes a car from the car park.

Usage:
    Run the tests using the unittest module.
"""


import unittest
from sensor import Sensor, EntrySensor, ExitSensor
from car_park import CarPark


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark(location="Test Location", capacity=100)
        self.entry_sensor = EntrySensor(id=1, is_active=True, car_park=self.car_park)
        self.exit_sensor = ExitSensor(id=2, is_active=True, car_park=self.car_park)

    def test_entry_sensor_detection(self):
        # Simulate detecting a car entering the car park
        self.entry_sensor.update_car_park("CAR-001")
        self.assertIn("CAR-001", self.car_park.plates)
        self.assertEqual(self.car_park.available_bays, 99)

    def test_exit_sensor_detection(self):
        # simulate detecting a car exiting the car park
        self.car_park.add_car("CAR-002")
        self.exit_sensor.update_car_park("CAR-002")
        self.assertNotIn("CAR-002", self.car_park.plates)
        self.assertEqual(self.car_park.available_bays, 100)


if __name__ == '__main__':
    unittest.main()
