import unittest
from auto_test.my_cases import MyCases

suite = unittest.TestSuite()
suite.addTests(unittest.makeSuite(MyCases))

runner = unittest.TextTestRunner()
runner.run(suite)
