import sys
import unittest
from .directory_reader import DirReader

class TestF(unittest.TestCase):
    def test_DirReader(self):
        for file in DirReader("test_dir"):
            self.assertEqual(file, "test_dir" + "\\test.txt")
