import math
import unittest

from optics_lib.utils import euclidean_distance


class TestEuclideanDistance(unittest.TestCase):

    def test_same_point(self):
        self.assertEqual(0.0, euclidean_distance([0.1], [0.1]))
        self.assertEqual(0.0, euclidean_distance([0.2, 0.2], [0.2, 0.2]))
        self.assertEqual(0.0, euclidean_distance([-0.3, 0.3, -0.3], [-0.3, 0.3, -0.3]))

    def test_different_points(self):
        self.assertAlmostEqual(math.sqrt(2), euclidean_distance([1, 1], [2, 2]))
        self.assertAlmostEqual(5 * math.sqrt(2), euclidean_distance([2, 2], [-3, -3]))


if __name__ == '__main__':
    unittest.main()
