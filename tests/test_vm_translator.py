import unittest
from VMTranslator import add_one

class TestVMTranslator(unittest.TestCase):
    def test(self):
        self.assertEqual(add_one(3), 4)
