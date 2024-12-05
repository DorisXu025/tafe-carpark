
"""
Test Module for CarPark
------------------------

This module contains unit tests for the `CarPark` class to ensure its functionality and correctness.
The tests cover initialization, car entry/exit operations, logging, and registration of components.

Classes:
    TestCarPark: A unittest test case class for testing the `CarPark` class.

Test Methods:
    setUp(): Prepares a `CarPark` instance for testing.
    test_car_park_initialized_with_all_attributes(): Tests the initialization of a `CarPark` object with default and custom attributes.
    test_add_car(): Verifies adding a car updates the plates and available bays.
    test_remove_car(): Verifies removing a car updates the plates and available bays.
    test_overfill_the_car_park(): Ensures overfilling the car park doesn't affect the available bays.
    test_removing_a_car_that_does_not_exist(): Confirms that removing a non-existent car raises a `ValueError`.
    test_register_raises_type_error(): Ensures only valid sensors or displays can be registered.
    test_log_file_created(): Verifies that the log file is created when a new car park instance is initialized.
    test_car_logged_when_entering(): Confirms the log file records a car's entry.
    test_car_logged_when_exiting(): Confirms the log file records a car's exit.
    tearDown(): Cleans up by removing any created test log files.

Usage:
    Run the tests using the unittest module.
"""


import unittest
from car_park import CarPark
from pathlib import Path

class TestCarPark(unittest.TestCase):
      def setUp(self):
         self.car_park = CarPark("123 Example Street", 100)

      def test_car_park_initialized_with_all_attributes(self):
         self.assertIsInstance(self.car_park, CarPark)
         self.assertEqual(self.car_park.location, "123 Example Street")
         self.assertEqual(self.car_park.capacity, 100)
         self.assertEqual(self.car_park.plates, [])
         self.assertEqual(self.car_park.sensors, [])
         self.assertEqual(self.car_park.displays, [])
         self.assertEqual(self.car_park.available_bays, 100)
         self.assertEqual(self.car_park.log_file, Path("log.txt"))

      def test_add_car(self):
         self.car_park.add_car("FAKE-001")
         self.assertEqual(self.car_park.plates, ["FAKE-001"])
         self.assertEqual(self.car_park.available_bays, 99)

      def test_remove_car(self):
         self.car_park.add_car("FAKE-001")
         self.car_park.remove_car("FAKE-001")
         self.assertEqual(self.car_park.plates, [])
         self.assertEqual(self.car_park.available_bays, 100)

      def test_overfill_the_car_park(self):
         for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
         self.assertEqual(self.car_park.available_bays, 0)
         self.car_park.add_car("FAKE-100")
         # Overfilling the car park should not change the number of available bays
         self.assertEqual(self.car_park.available_bays, 0)

         # Removing a car from an overfilled car park should not change the number of available bays
         self.car_park.remove_car("FAKE-100")
         self.assertEqual(self.car_park.available_bays, 0)

      def test_removing_a_car_that_does_not_exist(self):
         with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

      def test_register_raises_type_error(self): # for sensor unit test
         with self.assertRaises(TypeError):
            self.car_park.register("Not a Sensor or Display")

      def test_log_file_created(self):
          new_carpark = CarPark("123 Example Street", 100, log_file="new_log.txt")
          self.assertTrue(Path("new_log.txt").exists())

      def tearDown(self):
          Path("new_log.txt").unlink(missing_ok=True)

      def test_car_logged_when_entering(self):
          new_carpark = CarPark("123 Example Street", 100,
                                log_file="new_log.txt")  # TODO: change this to use a class attribute or new instance variable
          self.car_park.add_car("NEW-001")
          with self.car_park.log_file.open() as f:
              last_line = f.readlines()[-1]
          self.assertIn("NEW-001", last_line)  # check plate entered
          self.assertIn("entered", last_line)  # check description
          self.assertIn("\n", last_line)  # check entry has a new line

      def test_car_logged_when_exiting(self):
          new_carpark = CarPark("123 Example Street", 100,
                                log_file="new_log.txt")  # TODO: change this to use a class attribute or new instance variable
          self.car_park.add_car("NEW-001")
          self.car_park.remove_car("NEW-001")
          with self.car_park.log_file.open() as f:
              last_line = f.readlines()[-1]
          self.assertIn("NEW-001", last_line)  # check plate entered
          self.assertIn("exited", last_line)  # check description
          self.assertIn("\n", last_line)  # check entry has a new line


if __name__ == "__main__":
   unittest.main()
