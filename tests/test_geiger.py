""" Test case for """

import unittest
import re

# matches positive integers
RE_INT = re.compile(r"\d+")

from geiger_counter import print_poisson

class Test_geiger(unittest.TestCase):
    def test_print_poisson(self):
        res = print_poisson(20, 10)
        # Check we have the right number of lines
        self.assertEqual(res.count("\n"), 10)
        # check
        for i, line in enumerate(res.split()):
            self.assertEqual(line.startswith(str(i+1)+","))
            parts = line.split(",")
            # Line has two parts
            self.assertEqual(len(parts), 2)
            self.assertEqual(RE_INT.matches(parts[1]))

