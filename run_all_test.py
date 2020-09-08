import unittest

test_dir = r'D:\android_airtest\case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py',top_level_dir=r'D:\android_airtest\case')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)