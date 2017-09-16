import math


def euclidean_distance(point_a, point_b):
    if len(point_a) != len(point_b):
        raise ValueError('Points must be of the same length')

    return math.sqrt(sum(map(lambda x, y: (x - y) ** 2, point_a, point_b)))


def read_input_data(filename):
    with open(filename, 'r') as input_file:
        return [float(line) for line in input_file]


def read_multivariative_input_data(filename):
    data = []
    with open(filename, 'r') as input_file:
        for line in input_file:
            if line:
                data.append([float(x) for x in line.split()])

    return data
