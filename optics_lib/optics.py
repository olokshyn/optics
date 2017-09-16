from optics_objects_manager import OpticsObjectsManager
from ordered_seeds import OrderedSeeds


def optics(points, eps, min_pts):
    objects_storage = []
    objects_manager = OpticsObjectsManager(points)
    for obj in objects_manager:
        if not obj.processed:
            _expand_cluster_order(objects_manager, obj, eps, min_pts, objects_storage)
    return objects_storage


def _expand_cluster_order(objects_manager, obj, eps, min_pts, objects_storage):
    neighbors = objects_manager.find_neighbors(obj, eps)
    obj.processed = True
    objects_manager.set_core_distance(obj, neighbors, eps, min_pts)
    objects_storage.append(obj)

    if obj.core_distance is not None:
        ordered_seeds = OrderedSeeds()
        ordered_seeds.update(objects_manager, neighbors, obj)
        while ordered_seeds:
            current_obj = ordered_seeds.pop_next()
            neighbors = objects_manager.find_neighbors(current_obj, eps)
            current_obj.processed = True
            objects_manager.set_core_distance(current_obj, neighbors, eps, min_pts)
            objects_storage.append(current_obj)
            if current_obj.core_distance is not None:
                ordered_seeds.update(objects_manager, neighbors, current_obj)
