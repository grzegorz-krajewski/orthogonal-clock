import unittest

from orthogonal_time.converter import convert_hms


class ReferenceCasesTest(unittest.TestCase):
    def assertOrth(self, h: int, m: int, s: int, expected: float):
        state = convert_hms(h, m, s)
        self.assertAlmostEqual(state.orth, expected, places=7)

    def test_reference_hours(self):
        self.assertOrth(12, 0, 0, 90.0)
        self.assertOrth(3, 0, 0, 0.0)
        self.assertOrth(6, 0, 0, 90.0)
        self.assertOrth(9, 0, 0, 0.0)
        self.assertOrth(1, 0, 0, 60.0)
        self.assertOrth(2, 0, 0, 30.0)
        self.assertOrth(4, 0, 0, 30.0)
        self.assertOrth(5, 0, 0, 60.0)


if __name__ == "__main__":
    unittest.main()
