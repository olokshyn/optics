class OpticsObject(object):

    def __init__(self, index, point):
        self.index = index
        self.point = point
        self.core_distance = None
        self.reachability_distance = None
        self.processed = False

    def __repr__(self):
        return '{}(i={}, p={}, cd={}, rd={}, pr={})'.format(self.__class__.__name__, self.index,
                                                            self.point, self.core_distance,
                                                            self.reachability_distance, self.processed)
