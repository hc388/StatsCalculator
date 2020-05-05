import unittest
from randoms import Randoms

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.random = Randoms()


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.random, Randoms)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.random, Randoms)

    def test_randRangeSeed(self):
        self.assertEquals((Randoms.rand_range(1,100,5)),(Randoms.rand_range(1,100,5)))

    def test_randRange(self):
        self.assertTrue(0 < Randoms.rand_range(1,100) < 100)

    def test_randList(self):
        self.assertTrue(isinstance(Randoms.rand_list(1,100,10,11), list))


    def test_randSelectorseed(self):
        list = Randoms.rand_list(0,100,30,99)
        self.assertEquals((Randoms.rand_selector(list,4)), Randoms.rand_selector(list, 4))

    def test_randSelector(self):
        list = Randoms.rand_list(0,100,30,99)
        self.assertTrue(Randoms.rand_selector(list) in list)

    def test_rand_N_Selector(self):
        list = Randoms.rand_list(0,100,30,99)
        self.assertTrue(all(elem in list  for elem in Randoms.rand_N_selector(list,3)))

    def test_rand_N_Selectorseed(self):
        list = Randoms.rand_list(0,100,30,99)
        self.assertEquals((Randoms.rand_N_selector(list, 3, 7)), Randoms.rand_N_selector(list, 3, 7))


if __name__ == '__main__':
    unittest.main()
