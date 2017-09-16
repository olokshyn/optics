import sys

import matplotlib.pyplot as plt

from optics_lib import optics
from optics_lib.utils import read_multivariative_input_data


def main(argv):
    data_filename = argv[1]
    eps = argv[2]
    min_pts = argv[3]

    result = optics(read_multivariative_input_data(data_filename), float(eps), int(min_pts))
    plt.plot([x.reachability_distance for x in result if x.reachability_distance is not None])
    plt.show()

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
