from optics_object import OpticsObject
from utils import euclidean_distance


class OpticsObjectsManager(object):

    def __init__(self, points):
        self.__objects = [OpticsObject(index, point) for index, point in enumerate(points)]
        self.__distance_matrix = []

        for obj_i in self.__objects:
            obj_distances = []
            for obj_j in self.__objects:
                if id(obj_i) == id(obj_j):
                    obj_distances.append(0.0)
                else:
                    obj_distances.append(euclidean_distance(obj_i.point, obj_j.point))
            self.__distance_matrix.append(obj_distances)

    def __iter__(self):
        return iter(self.__objects)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, repr(self.__objects))

    def find_neighbors(self, obj, eps):
        self.__check_obj_index(obj)

        neighbors = []
        for d_obj in self.__objects:
            if id(obj) == id(d_obj):
                continue
            if self.__distance_matrix[obj.index][d_obj.index] <= eps:
                neighbors.append(d_obj)
        return neighbors

    def set_core_distance(self, obj, neighbors, eps, min_pts):
        self.__check_obj_index(obj)

        if len(neighbors) >= min_pts:
            obj.core_distance = sorted(self.__distance_matrix[obj.index])[min_pts]
        else:
            obj.core_distance = None

    def set_reachability_distance(self, core_obj, obj):
        self.__check_obj_index(core_obj)
        self.__check_obj_index(obj)

        if core_obj.core_distance is not None:
            obj.reachability_distance = max(core_obj.core_distance,
                                            self.__distance_matrix[core_obj.index][obj.index])
        else:
            obj.reachability_distance = None

    def objects_distance(self, obj_i, obj_j):
        self.__check_obj_index(obj_i)
        self.__check_obj_index(obj_j)

        return self.__distance_matrix[obj_i.index][obj_j.index]

    def __check_obj_index(self, obj):
        if obj.index < 0 or obj.index >= len(self.__objects):
            raise IndexError('Object index {} is out of range'.format(obj.index))
        if id(obj) != id(self.__objects[obj.index]):
            raise ValueError('Object is not in the objects list')
