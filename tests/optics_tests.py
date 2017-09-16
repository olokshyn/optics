import unittest

from optics_lib import optics
from optics_lib.utils import read_multivariative_input_data, read_input_data


def _fisher_iris(eps, min_pts):
    fisher_iris_data_filename = 'data/fisher_iris.data'
    fisher_iris_result_filename = 'results/fisher_iris.data.result_{}_{}'.format(eps, min_pts)

    def __fisher_iris(self):
        result = optics(read_multivariative_input_data(fisher_iris_data_filename), eps, min_pts)
        reachability_distances = [x.reachability_distance for x in result if x.reachability_distance is not None]
        test_reachability_distances = read_input_data(fisher_iris_result_filename)
        self.assertEqual(len(reachability_distances), len(test_reachability_distances))
        for i in xrange(len(reachability_distances)):
            self.assertAlmostEqual(reachability_distances[i], test_reachability_distances[i])

    return __fisher_iris


class TestOPTICS(unittest.TestCase):
    test_fisher_iris_5_1 = _fisher_iris(5, 1)
    test_fisher_iris_5_2 = _fisher_iris(5, 2)
    test_fisher_iris_5_3 = _fisher_iris(5, 3)

    test_fisher_iris_12_1 = _fisher_iris(1.2, 1)
    test_fisher_iris_12_2 = _fisher_iris(1.2, 2)
    test_fisher_iris_12_3 = _fisher_iris(1.2, 3)

    test_fisher_iris_05_1 = _fisher_iris(0.5, 1)
    test_fisher_iris_05_2 = _fisher_iris(0.5, 2)
    test_fisher_iris_05_3 = _fisher_iris(0.5, 3)
