"""别壤（BIERANG）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
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

    def test_branch_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.branch(None)

    def test_diff_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.diff(None)


if __name__ == "__main__":
    unittest.main()
