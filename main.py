import sys

import matplotlib.pyplot as plt

from optics_lib import optics, extract_clusters_and_noise
from optics_lib.utils import read_multivariative_input_data


def main(argv):
    data_filename = argv[1]
    eps = float(argv[2])
    min_pts = int(argv[3])

    cluster_ordering = optics(read_multivariative_input_data(data_filename), eps, min_pts)
    plt.plot([x.reachability_distance for x in cluster_ordering if x.reachability_distance is not None])
    plt.show()

    clusters, noise = extract_clusters_and_noise(cluster_ordering, eps)
    print 'Clusters: {}, noise points: {}'.format(len(clusters), len(noise))
    for cluster in clusters:
        print '\tcluster size:', len(cluster)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
