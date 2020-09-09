import unittest

test_dir = r'C:\airtest_script\case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py',top_level_dir=None)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)