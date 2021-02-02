import sys
import unittest
from src import directory_reader as d_r



class TestF(unittest.TestCase):
    def test_DirReader(self):
        for file in d_r.DirReader("test_dir"):
            self.assertEqual(file, "test_dir" + "\\test.txt")
