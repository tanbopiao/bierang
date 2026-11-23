"""别壤（BIERANG）算子单测：名帖完整、行为达标、只增不覆盖。"""
import unittest

from bierang import Bierang


class TestBierang(unittest.TestCase):
    def setUp(self):
        self.op = Bierang()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "bierang")
        self.assertEqual(d["code"], "BIERANG")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_branch(self):
        soil_id = self.op.branch("实验壤甲")
        self.assertTrue(soil_id.startswith("BR-"))

    def test_diff(self):
        soil_id = self.op.branch("实验壤甲")
        d = self.op.diff(soil_id)
        self.assertEqual(d["base"], "gui")
        self.assertFalse(d["diverged"])
        with self.assertRaises(KeyError):
            self.op.diff("BR-9999")


if __name__ == "__main__":
    unittest.main()
