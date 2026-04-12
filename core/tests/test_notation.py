import unittest

from orthogonal_time.converter import convert_hms
from orthogonal_time.notation import format_standard, format_short, format_full, to_machine_dict


class NotationTest(unittest.TestCase):
    def test_standard_format(self):
        state = convert_hms(3, 0, 0)
        self.assertEqual(format_standard(state), "[-] C3 O0.00 ?")

    def test_short_format(self):
        state = convert_hms(5, 0, 0)
        self.assertEqual(format_short(state), "-5:60.00?")

    def test_full_format_contains_core_fields(self):
        state = convert_hms(12, 0, 0)
        text = format_full(state)
        self.assertIn("Orth=90.00", text)
        self.assertIn("C=0", text)

    def test_machine_dict(self):
        state = convert_hms(1, 0, 0, scale="UTC")
        payload = to_machine_dict(state)
        self.assertEqual(payload["version"], "0.1")
        self.assertEqual(payload["base"]["scale"], "UTC")
        self.assertEqual(payload["orth_int"], 60)


if __name__ == "__main__":
    unittest.main()
