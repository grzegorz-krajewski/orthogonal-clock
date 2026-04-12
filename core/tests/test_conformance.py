import unittest

from orthogonal_time.converter import reduce_half_turn, convert_hms


class ConformanceTest(unittest.TestCase):
    def test_reduce_half_turn(self):
        self.assertEqual(reduce_half_turn(180.0), 0.0)
        self.assertEqual(reduce_half_turn(270.0), 90.0)
        self.assertEqual(reduce_half_turn(30.0), 30.0)

    def test_cycle_technical_range(self):
        state = convert_hms(12, 0, 0)
        self.assertEqual(state.cycle, 0)

        state = convert_hms(11, 0, 0)
        self.assertEqual(state.cycle, 11)

    def test_sphere_is_transitional_but_present(self):
        self.assertEqual(convert_hms(3, 0, 0).sphere, "-")
        self.assertEqual(convert_hms(10, 0, 0).sphere, "+")


if __name__ == "__main__":
    unittest.main()
