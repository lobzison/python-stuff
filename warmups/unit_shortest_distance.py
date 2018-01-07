import shortest_distance as sd
import unittest
import math
import random


class DistanceTest(unittest.TestCase):
    """Class for testing euclidian distance function"""

    def test_x1(self):
        """Distance between 0,0 and 1,0 == 1"""
        self.assertEqual(sd.e_distance((0, 0), (1, 0)), 1)

    def test_x2(self):
        """Distance between 0,0 and -1,0 == 1"""
        self.assertEqual(sd.e_distance((0, 0), (-1, 0)), 1)

    def test_x3(self):
        """Distance between 0,0 and 3,0 == 3"""
        self.assertEqual(sd.e_distance((0, 0), (3, 0)), 3)

    def test_x4(self):
        """Distance between 0,0 and -3,0 == 3"""
        self.assertEqual(sd.e_distance((0, 0), (-3, 0)), 3)

    def test_y1(self):
        """Distance between 0,0 and 0,1 == 1"""
        self.assertEqual(sd.e_distance((0, 0), (1, 0)), 1)

    def test_y2(self):
        """Distance between 0,0 and 0,-1 == 1"""
        self.assertEqual(sd.e_distance((0, 0), (-1, 0)), 1)

    def test_y3(self):
        """Distance between 0,0 and 0,3 == 3"""
        self.assertEqual(sd.e_distance((0, 0), (3, 0)), 3)

    def test_y4(self):
        """Distance between 0,0 and 0,-3 == 3"""
        self.assertEqual(sd.e_distance((0, 0), (-3, 0)), 3)

    def test_x_y1(self):
        """Distance between 1,1 and 0,0 == sqrt(2)"""
        self.assertEqual(sd.e_distance((1, 1), (0, 0)), math.sqrt(2))

    def test_x_y2(self):
        """Distance between 18,-3 and -2,6 == sqrt(481)"""
        self.assertEqual(sd.e_distance((18, -3), (-2, 6)), math.sqrt(481))


def gen_tuple_list(num):
    """Generates list of random tuples in format
    (x, y) where x and y >-100 and <100"""
    return [(random.randint(-99, 99), random.randint(-99, 99))
            for _ in range(num)]


class BruteForaceDistanceTest(unittest.TestCase):
    """Test case for bnrute force search for minimum pistance pair"""

    def test_empty(self):
        """Empty list returns infinity as a distance and None as coordinats"""
        self.assertEqual(sd.brute_force([]),
                         (float("inf"), (None, None), (None, None)))

    def test_zero(self):
        """Same points == 0 distance"""
        self. assertEqual(sd.brute_force([(0, 0), (0, 0), (0, 0)]),
                          (0, (0, 0), (0, 0)))

    def test_nonzero1(self):
        """Same distance, return first"""
        self.assertEqual(sd.brute_force([(0, 0), (1, 1), (2, 2), (3, 3)]),
                         (math.sqrt(2), (0, 0), (1, 1)))

    def test_nonzero2(self):
        """different distance"""
        self.assertEqual(sd.brute_force([(64, -59), (-1, -15),
                                         (34, 32), (51, 55),
                                         (65, 14), (-98, 80),
                                         (-21, -23)]),
                         (math.sqrt(20 ** 2 + 8 ** 2), (-1, -15), (-21, -23)))


sd.divide_and_conquer(gen_tuple_list(100))
if __name__ == '__main__':
    unittest.main()
