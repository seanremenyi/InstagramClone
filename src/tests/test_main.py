import unittest
import sys
sys.path.append("..")
from main import add

class TestObject(unittest.TestCase):
    """Test Object"""
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(3,9),12)

    def test_add2(self):
        self.assertEqual(add(6,1),7)
        self.assertEqual(add(9,2),11)