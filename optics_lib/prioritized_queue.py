class PrioritizedQueue(object):

    ORDERING_ASCENDING = 'acs'
    ORDERING_DESCENDING = 'desc'

    class __PrioritizedQueueIter(object):

        def __init__(self, items):
            self.__items = items
            self.__current_index = 0

        def next(self):
            if self.__current_index == len(self.__items):
                raise StopIteration()
            item_info = self.__items[self.__current_index]
            self.__current_index += 1
            return item_info.item

    class __ItemInfo(object):

        def __init__(self, item, priority):
            self.item = item
            self.priority = priority

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.item == other.item and self.priority == other.priority
            else:
                return self.item == other

        def __ne__(self, other):
            return not self.__eq__(other)

        def __repr__(self):
            return '(item={}, priority={})'.format(self.item, self.priority)

    def __init__(self, ordering_policy=ORDERING_ASCENDING):
        self.__check_ordering_policy(ordering_policy)

        self.__items = []
        self.__ordering_policy = ordering_policy

    def __repr__(self):
        return 'PrioritizedQueue(policy={}, items={})'.format(self.__ordering_policy, repr(self.__items))

    def __iter__(self):
        return self.__PrioritizedQueueIter(self.__items)

    def __len__(self):
        return len(self.__items)

    def __nonzero__(self):
        return bool(self.__items)

    def add(self, item, priority):
        index = 0
        for item_info in self.__items:
            if self.__has_better_priority(priority, item_info):
                break
            index += 1
        self.__items.insert(index, self.__ItemInfo(item, priority))

    def update(self, item, priority):
        item_current_index = None
        index = 0
        for item_info in self.__items:
            if item_info == item:
                item_current_index = index
                break
            if self.__has_better_priority(priority, item_info):
                break
            index += 1

        if item_current_index is None:
            self.__items.insert(index, self.__ItemInfo(item, priority))
            index += 1

            while index < len(self.__items):
                if self.__items[index] == item:
                    del self.__items[index]
                    break
                index += 1
        elif self.__has_better_priority(priority, self.__items[item_current_index]):
            self.__items[item_current_index].priority = priority

    def remove(self, item):
        index = None
        for item_index, item_info in enumerate(self.__items):
            if item_info == item:
                index = item_index
        if index is not None:
            del self.__items[index]

    def pop_next(self):
        item_info = self.__items.pop(0)
        return item_info.item

    def change_ordering_policy(self, ordering_policy):
        self.__check_ordering_policy(ordering_policy)

        if ordering_policy != self.__ordering_policy:
            self.__items.reverse()
            self.__ordering_policy = ordering_policy

    def __has_better_priority(self, priority, item_info):
        if self.__ordering_policy == self.ORDERING_ASCENDING \
                and priority < item_info.priority:
            return True
        elif self.__ordering_policy == self.ORDERING_DESCENDING \
                and priority > item_info.priority:
            return True

        return False

    def __check_ordering_policy(self, ordering_policy):
        if ordering_policy not in [self.ORDERING_ASCENDING, self.ORDERING_DESCENDING]:
            raise ValueError('Invalid ordering policy {}'.format(ordering_policy))
