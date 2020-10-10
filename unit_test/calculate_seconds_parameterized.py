import unittest
from typing import Any

from parameterized import parameterized


class CalculateSecondsTestCase(unittest.TestCase):
    @parameterized.expand([
        ("non_zero_hours_and_minutes", 1, 3, 3780),
        ("decimal_hours_and_minutes", 0.8, 2.5, 3030),
        ("negative_minutes", 1, -3, "The provided input '-3' for minutes is not valid, please enter a positive number"),
        ("negative_hours", -5, 1, "The provided input '-5' for hours is not valid, please enter a positive number")
    ])
    def test_calculate_seconds(self, test_name, hours, minutes, expected):
        try:
            actual_seconds = self.get_seconds(hours, minutes)
            self.assertEqual(expected, actual_seconds)
        except TypeError as e:
            self.assertEqual(expected, str(e))

    def get_seconds(self, hours, minutes) -> Any:
        if minutes < 0:
            return "The provided input '{0}' for minutes is not valid, please enter a positive number".format(minutes)
        if hours < 0:
            raise TypeError(
                "The provided input '{0}' for hours is not valid, please enter a positive number".format(hours))

        # hours * 60 * 60 + minutes * 60
        return (hours * 60 + minutes) * 60


if __name__ == '__main__':
    unittest.main()
