
"""
Test Module for Display
------------------------

This module contains unit tests for the `Display` class to verify its functionality and interactions with the `CarPark` class.

Classes:
    TestDisplay: A unittest test case class for testing the `Display` class.

Test Methods:
    setUp(): Prepares a `Display` instance and associated `CarPark` for testing.
    test_display_initialized_with_all_attributes(): Tests the initialization of a `Display` object with default and custom attributes.
    test_update(): Verifies that the `update` method correctly updates the display's attributes.

Usage:
    Run the tests using the unittest module.
"""


import unittest
from display import Display
from car_park import CarPark


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.display = Display(
            id=1,
            message="Welcome to the car park",
            is_on=True,
            car_park=self.car_park
        )

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")


if __name__ == '__main__':
    unittest.main()