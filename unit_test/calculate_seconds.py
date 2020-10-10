"""
Unit Test –> Calculate Seconds TestCase
"""
import unittest
from typing import Any


class CalculateSecondsTestCase(unittest.TestCase):

    def test_non_zero_hours_and_minutes(self):
        minutes = 3
        hours = 1
        expected_seconds = 3780

        actual_seconds = self.get_seconds(hours, minutes)
        self.assertEqual(expected_seconds, actual_seconds)

    def test_decimal_hours_and_minutes(self):
        minutes = 2.5
        hours = 4/5
        expected_seconds = 3030.0

        actual_seconds = self.get_seconds(hours, minutes)
        self.assertEqual(expected_seconds, actual_seconds)

    def test_negative_minutes(self):
        minutes = -3
        hours = 1
        expected_message = "The provided input '{0}' for minutes is not valid, please enter a positive number".format(minutes)

        actual_message = self.get_seconds(hours, minutes)
        self.assertEqual(expected_message, actual_message)

    def test_negative_hours(self):
        minutes = 1
        hours = -5
        expected_message = "The provided input '{0}' for hours is not valid, please enter a positive number".format(hours)

        try:
            self.get_seconds(hours, minutes)
        except TypeError as e:
            self.assertEqual(expected_message, str(e))

    def get_seconds(self, hours, minutes) -> Any:
        if minutes < 0:
            return "The provided input '{0}' for minutes is not valid, please enter a positive number".format(minutes)
        if hours < 0:
            raise TypeError("The provided input '{0}' for hours is not valid, please enter a positive number".format(hours))

        # hours * 60 * 60 + minutes * 60
        return (hours * 60 + minutes) * 60


if __name__ == '__main__':
    unittest.main()

