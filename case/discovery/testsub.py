
import unittest


class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")

    def test_sub(self):
        print("test sub 01")

    def test_sub2(self):
        print("test sub 02")

if __name__ == '__main__':
    unittest.main()