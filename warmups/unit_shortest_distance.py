import shortest_distance as sd
import unittest


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


if __name__ == '__main__':
    unittest.main()
