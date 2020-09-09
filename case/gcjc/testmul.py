
import unittest


class TestMul(unittest.TestCase):
    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")

    def test_add(self):
        print("test mul 01")

    def test_add2(self):
        print("test mul 02")

if __name__ == '__main__':
    unittest.main()