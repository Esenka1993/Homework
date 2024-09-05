import Runner_2 as tr
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = tr.Runner('Усейн', 10)
        self.Andrey = tr.Runner('Андрей', 9)
        self.Nick = tr.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for place, runner in sorted(cls.all_results.items()):
            print(f"Место {place}: {runner}")


    def test_run_Usain_Nick(self):
        comp1 = tr.Tournament(90, self.Usain, self.Nick)
        self.all_results = comp1.start()
        last_place = max(self.all_results)
        self.assertTrue(self.all_results[last_place] == self.Nick)

    def test_run_Andrey_Nick(self):
        comp2 = tr.Tournament(90, self.Andrey, self.Nick)
        self.all_results = comp2.start()
        last_place = max(self.all_results)
        self.assertTrue(self.all_results[last_place] == self.Nick)

    def test_run_Usain_Andrey_Nick(self):
        comp3 = tr.Tournament(90, self.Usain, self.Andrey, self.Nick)
        self.all_results = comp3.start()
        last_place = max(self.all_results)
        self.assertTrue(self.all_results[last_place] == self.Nick)

if __name__ == '__main__':
    unittest.main()
