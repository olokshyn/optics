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


def read_cluster_labels(cls_filename):
    labels = []
    with open(cls_filename, 'r') as cls_file:
        for line in cls_file:
            if line.startswith('%'):
                continue
            labels.append(int(line.split()[1]))
    return labels


def count_erroneously_clustered_points(found_clusters, noise, cluster_labels):
    # Reorganize cluster_labels so every label will denote
    # a set of object`s indexes which it contains
    clusters = {}
    for index in xrange(len(cluster_labels)):
        if cluster_labels[index] not in clusters:
            clusters[cluster_labels[index]] = set()
        clusters[cluster_labels[index]].add(index)

    # For every cluster find the biggest found_cluster that matches it
    clusters_matched_count = {}
    for cluster_label, cluster in clusters.iteritems():
        clusters_matched_count[cluster_label] = 0

        found_cluster_matches = {}
        for found_cluster_index, found_cluster in enumerate(found_clusters):
            found_cluster_matches[found_cluster_index] = 0
            for obj in found_cluster:
                if obj.index in cluster:
                    found_cluster_matches[found_cluster_index] += 1
        if not found_cluster_matches:
            continue

        clusters_matched_count[cluster_label] = max(found_cluster_matches.itervalues())

    erroneously_clustered_points_count = 0
    for cluster_label, matched_count in clusters_matched_count.iteritems():
        erroneously_clustered_points_count += len(clusters[cluster_label]) - matched_count

    return erroneously_clustered_points_count


def perform_clustering(data_filename, eps, min_pts, cluster_labels_filename='', build_plot=False):
    points = read_sample_input_data(data_filename)
    cluster_ordering = optics(points, eps, min_pts)
    if build_plot:
        plt.plot([x.reachability_distance for x in cluster_ordering
                  if x.reachability_distance is not None])
        plt.show()

    clusters, noise = extract_clusters_and_noise(cluster_ordering, eps)
    print 'Clusters: {}, noise points: {}'.format(len(clusters), len(noise))
    erroneously_clustered_points_count = 0
    if cluster_labels_filename:
        cluster_labels = read_cluster_labels(cluster_labels_filename)
        erroneously_clustered_points_count = count_erroneously_clustered_points(clusters, noise, cluster_labels)
        print 'Erroneously clustered points: {} ({}%)' \
            .format(erroneously_clustered_points_count,
                    float(erroneously_clustered_points_count) / len(cluster_labels) * 100)
    return clusters, noise, erroneously_clustered_points_count


def main(argv):
    data_filename = argv[1]
    min_eps = float(argv[2])
    max_eps = float(argv[3])
    step_eps = float(argv[4])
    min_min_pts = int(argv[5])
    max_min_pts = int(argv[6])
    cluster_labels_filename = ''
    if len(argv) >= 8:
        cluster_labels_filename = argv[7]

    best_eps = 0.0
    best_min_pts = 0.0
    best_err_clust_points = None
    best_err_clust_perc = 0.0
    best_noise_count = 0

    eps = min_eps
    while eps <= max_eps:
        for min_pts in xrange(min_min_pts, max_min_pts + 1):
            print 'eps:', eps
            print 'min_pts:', min_pts
            clusters, noise, err_clust_points = perform_clustering(data_filename, eps, min_pts, cluster_labels_filename)
            if best_err_clust_points is None or err_clust_points < best_err_clust_points:
                best_eps = eps
                best_min_pts = min_pts
                best_err_clust_points = err_clust_points
                best_err_clust_perc = float(best_err_clust_points) \
                                      / (sum((len(x) for x in clusters)) + len(noise)) * 100
                best_noise_count = len(noise)
            print ''
            if best_err_clust_points == 0:
                break
        if best_err_clust_points == 0:
            break
        eps += step_eps

    print ''
    print 'Best eps:', best_eps
    print 'Best min_pts:', best_min_pts
    print 'Best erroneously clustered points: {} ({}%)'.format(best_err_clust_points, best_err_clust_perc)
    print 'Best noise count:', best_noise_count

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
