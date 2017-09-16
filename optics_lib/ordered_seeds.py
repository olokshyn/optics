from prioritized_queue import PrioritizedQueue


class OrderedSeeds(object):

    def __init__(self):
        self.__queue = PrioritizedQueue(PrioritizedQueue.ORDERING_ASCENDING)

    def __nonzero__(self):
        return bool(self.__queue)

    def update(self, objects_manager, neighbors, center_object):
        core_dist = center_object.core_distance
        assert core_dist is not None, 'center_object must be core object'

        for obj in neighbors:
            if obj.processed:
                continue

            reachability_dist = max(core_dist,
                                    objects_manager.objects_distance(center_object, obj))
            if obj.reachability_distance is None:
                obj.reachability_distance = reachability_dist
                self.__queue.add(obj, reachability_dist)
            elif reachability_dist < obj.reachability_distance:
                obj.reachability_distance = reachability_dist
                self.__queue.update(obj, reachability_dist)

    def pop_next(self):
        return self.__queue.pop_next()
