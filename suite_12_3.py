import unittest
import tests_12_3 as rt


whole_test = unittest.TestSuite()
whole_test.addTest(unittest.TestLoader().loadTestsFromTestCase(rt.RunnerTest))
whole_test.addTest(unittest.TestLoader().loadTestsFromTestCase(rt.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(whole_test)