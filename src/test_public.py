import sys
import unittest
#from src import directory_reader as d_r
from . import directory_reader as dr

class TestF(unittest.TestCase):
    def test_DirReader(self):
        for file in dr.DirReader("test_dir"):
            self.assertEqual(file, "test_dir" + "\\test.txt")
