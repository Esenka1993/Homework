import unittest
import Runner as R
import Runner_2 as tr


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r1 = R.Runner('Dima')
        for i in range(10):
            r1.walk()

        self.assertEqual(r1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        r2 = R.Runner('Max')
        for i in range(10):
            r2.run()

        self.assertEqual(r2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r3 = R.Runner('Natasha')
        r4 = R.Runner('Zhenya')
        for i in range(10):
            r3.walk()
            r4.run()

        self.assertNotEqual(r3.distance, r4.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.Usain = tr.Runner('Усейн', 10)
        self.Andrey = tr.Runner('Андрей', 9)
        self.Nick = tr.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for place, runner in sorted(cls.all_results.items()):
            print(f"Место {place}: {runner}")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_Usain_Nick(self):
        comp1 = tr.Tournament(90, self.Usain, self.Nick)
        self.all_results = comp1.start()
        last_place = max(self.all_results)
        self.assertTrue(self.all_results[last_place] == self.Nick)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_Andrey_Nick(self):
        comp2 = tr.Tournament(90, self.Andrey, self.Nick)
        self.all_results = comp2.start()
        last_place = max(self.all_results)
        self.assertTrue(self.all_results[last_place] == self.Nick)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_Usain_Andrey_Nick(self):
        comp3 = tr.Tournament(90, self.Usain, self.Andrey, self.Nick)
        self.all_results = comp3.start()
        last_place = max(self.all_results)
        self.assertTrue(self.all_results[last_place] == self.Nick)

if __name__ == '__main__':
    unittest.main()


