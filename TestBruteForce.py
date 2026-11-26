import io
import unittest
from contextlib import redirect_stdout

import BruteForceSim as brute_force


class TestBruteForce(unittest.TestCase):
    """Automated tests for the Brute-Force Password Simulator."""

    def test_character_set_has_72(self):
        # The algorithm should have all 72 characters to guess from.
        self.assertEqual(len(brute_force.characters), 72)

    def test_readable_time_seconds(self):
        self.assertEqual(brute_force.readable_time(5), "5 seconds")

    def test_readable_time_minutes(self):
        self.assertEqual(brute_force.readable_time(120), "2.0 minutes")

    def test_readable_time_hours(self):
        self.assertEqual(brute_force.readable_time(7200), "2.0 hours")

    def test_readable_time_days(self):
        self.assertEqual(brute_force.readable_time(172800), "2.0 days")

    def test_crack_finds_lowercase_password(self):
        # crack() should find a short password and print it.
        output = io.StringIO()
        with redirect_stdout(output):
            brute_force.crack("ab")
        self.assertIn("Password found: ab", output.getvalue())

    def test_crack_finds_mixed_password(self):
        # Works for mixed upper/lower + digit too.
        output = io.StringIO()
        with redirect_stdout(output):
            brute_force.crack("A1")
        self.assertIn("Password found: A1", output.getvalue())

    def test_estimate_time_prints_combinations(self):
        # estimate_time() should report the number of combinations.
        output = io.StringIO()
        with redirect_stdout(output):
            brute_force.estimate_time("ab")
        self.assertIn("Total combinations to try:", output.getvalue())


if __name__ == "__main__":
    unittest.main()