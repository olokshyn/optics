import sys

import matplotlib.pyplot as plt

from optics_lib import optics, extract_clusters_and_noise
from optics_lib.utils import read_multivariative_input_data


def read_sample_input_data(data_filename):
    points = []
    with open(data_filename, 'r') as data_file:
        for line in data_file:
            if line.startswith('%'):
                continue
            points.append([float(x) for x in line.split()[1:]])
    return points


def read_class_labels(cls_filename):
    labels = []
    with open(cls_filename, 'r') as cls_file:
        for line in cls_file:
            if line.startswith('%'):
                continue
            labels.append(int(line.split()[1]))
    return labels


def count_erroneously_clustered_points(clusters, noise, class_labels):
    class_labels_converter = {}

    erroneously_clustered_points_count = len(noise)
    for cluster_index, cluster in enumerate(clusters):
        if cluster and cluster_index not in class_labels_converter:
            class_labels_converter[cluster_index] = class_labels[cluster[0].index]
        for obj in cluster:
            if class_labels_converter[cluster_index] != class_labels[obj.index]:
                erroneously_clustered_points_count += 1
    return erroneously_clustered_points_count


def perform_clustering(data_filename, eps, min_pts, class_labels_filename='', build_plot=False):
    points = read_sample_input_data(data_filename)
    cluster_ordering = optics(points, eps, min_pts)
    if build_plot:
        plt.plot([x.reachability_distance for x in cluster_ordering
                  if x.reachability_distance is not None])
        plt.show()

    clusters, noise = extract_clusters_and_noise(cluster_ordering, eps)
    print 'Clusters: {}, noise points: {}'.format(len(clusters), len(noise))
    erroneously_clustered_points_count = 0
    if class_labels_filename:
        class_labels = read_class_labels(class_labels_filename)
        erroneously_clustered_points_count = count_erroneously_clustered_points(clusters, noise, class_labels)
        print 'Erroneously clustered points: {}' \
            .format(erroneously_clustered_points_count)
    return clusters, noise, erroneously_clustered_points_count


def main(argv):
    data_filename = argv[1]
    min_eps = float(argv[2])
    max_eps = float(argv[3])
    step_eps = float(argv[4])
    min_min_pts = int(argv[5])
    max_min_pts = int(argv[6])
    class_labels_filename = ''
    if len(argv) >= 8:
        class_labels_filename = argv[7]

    best_eps = 0.0
    best_min_pts = 0.0
    best_err_clust_points = None

    eps = min_eps
    while eps <= max_eps:
        for min_pts in xrange(min_min_pts, max_min_pts + 1):
            print 'eps:', eps
            print 'min_pts:', min_pts
            _, _, err_clust_points = perform_clustering(data_filename, eps, min_pts, class_labels_filename)
            if best_err_clust_points is None or err_clust_points < best_err_clust_points:
                best_eps = eps
                best_min_pts = min_pts
                best_err_clust_points = err_clust_points
            print ''
        eps += step_eps

    print ''
    print 'Best eps:', best_eps
    print 'Best min_pts:', best_min_pts
    print 'Best erroneously clustered points:', best_err_clust_points

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
