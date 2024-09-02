import unittest
import Runner as R

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r1 = R.Runner('Dima')
        for i in range(10):
            r1.walk()

        self.assertEqual(r1.distance, 50)

    def test_run(self):
        r2 = R.Runner('Max')
        for i in range(10):
            r2.run()

        self.assertEqual(r2.distance, 100)

    def test_challenge(self):
        r3 = R.Runner('Natasha')
        r4 = R.Runner('Zhenya')
        for i in range(10):
            r3.walk()
            r4.run()

        self.assertNotEqual(r3.distance, r4.distance)
        

if __name__ == '__main__':
    unittest.main()


