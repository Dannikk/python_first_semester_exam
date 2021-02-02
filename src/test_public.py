import sys
import unittest
#from src import directory_reader as d_r
from src.directory_reader import *

class TestF(unittest.TestCase):
    def test_DirReader(self):
        for file in DirReader("test_dir"):
            self.assertEqual(file, "test_dir" + "\\test.txt")
