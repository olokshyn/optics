import unittest

from optics_lib.prioritized_queue import PrioritizedQueue


def _add_forward_order(ordering_policy):
    result = [0, 1, 2]
    if ordering_policy == PrioritizedQueue.ORDERING_DESCENDING:
        result.reverse()

    def __add_forward_order(self):
        queue = PrioritizedQueue(ordering_policy)
        queue.add(0, 1)
        queue.add(1, 2)
        queue.add(2, 3)
        self.assertEqual(result, list(queue))

    return __add_forward_order


def _add_backward_order(ordering_policy):
    result = [2, 1, 0]
    if ordering_policy == PrioritizedQueue.ORDERING_DESCENDING:
        result.reverse()

    def __add_asc_backward_order(self):
        queue = PrioritizedQueue(ordering_policy)
        queue.add(0, 3)
        queue.add(1, 2)
        queue.add(2, 1)
        self.assertEqual(result, list(queue))

    return __add_asc_backward_order


def _add_chess_order(ordering_policy):
    result = [5, 1, 0, 3, 2, 4]
    if ordering_policy == PrioritizedQueue.ORDERING_DESCENDING:
        result = [4, 2, 0, 3, 1, 5]

    def __add_chess_order(self):
        queue = PrioritizedQueue(ordering_policy)
        queue.add(0, 3)
        queue.add(1, 2)
        queue.add(2, 4)
        queue.add(3, 3)
        queue.add(4, 5)
        queue.add(5, 1)
        self.assertEqual(result, list(queue))

    return __add_chess_order


def _add_corner_cases(ordering_policy):
    result = [1, 4, 0, 3]
    if ordering_policy == PrioritizedQueue.ORDERING_DESCENDING:
        result = [0, 3, 4, 1]

    def __add_corner_cases(self):
        queue = PrioritizedQueue(ordering_policy)
        queue.add(0, 0.3)
        queue.add(1, 0.2)
        queue.add(3, 0.3)
        queue.add(4, 0.25)
        self.assertEqual(result, list(queue))

    return __add_corner_cases


def _update_no_item(ordering_policy):
    result = [0, 1, 2, 3]
    if ordering_policy == PrioritizedQueue.ORDERING_DESCENDING:
        result.reverse()

    def __update_no_item(self):
        queue = PrioritizedQueue(ordering_policy)
        queue.add(0, 1)
        queue.add(1, 2)
        queue.add(3, 4)

        queue.update(2, 3)
        self.assertEqual(result, list(queue))

    return __update_no_item


def _update_increase(ordering_policy):
    result1 = [0, 1, 3, 2, 4]
    result2 = [0, 1, 3, 2, 2.5, 4]
    result3 = [0, 3, 1, 2, 2.5, 4]

    if ordering_policy == PrioritizedQueue.ORDERING_DESCENDING:
        result1 = [4, 3, 2, 1, 0]
        result2 = [4, 3, 2, 2.5, 1, 0]
        result3 = result2

    def __update_increase(self):
        queue = PrioritizedQueue(ordering_policy)
        queue.add(0, 1)
        queue.add(1, 2)
        queue.add(2, 3)
        queue.add(3, 4)
        queue.add(4, 5)

        queue.update(3, 2)
        self.assertEqual(result1, list(queue))
        queue.add(2.5, 3)
        self.assertEqual(result2, list(queue))
        queue.update(3, 1)
        self.assertEqual(result3, list(queue))

    return __update_increase


def _update_decrease(ordering_policy):
    result1 = [0, 1, 2, 3, 4]
    result2 = [0, 1, 2, 2.5, 3, 4]
    result3 = result2

    if ordering_policy == PrioritizedQueue.ORDERING_DESCENDING:
        result1.reverse()
        result2 = [4, 3, 2, 2.5, 1, 0]
        result3 = [4, 2, 3, 2.5, 1, 0]

    def __update_decrease(self):
        queue = PrioritizedQueue(ordering_policy)
        queue.add(0, 1)
        queue.add(1, 2)
        queue.add(2, 3)
        queue.add(3, 4)
        queue.add(4, 5)

        queue.update(2, 4)
        self.assertEqual(result1, list(queue))
        queue.add(2.5, 3)
        self.assertEqual(result2, list(queue))
        queue.update(2, 5)
        self.assertEqual(result3, list(queue))

    return __update_decrease


def _update_the_same(ordering_policy):
    result = [0, 1, 2, 3]

    if ordering_policy == PrioritizedQueue.ORDERING_DESCENDING:
        result.reverse()

    def __update_the_same(self):
        queue = PrioritizedQueue(ordering_policy)
        queue.add(0, 1)
        queue.add(1, 2)
        queue.add(2, 3)
        queue.add(3, 4)

        queue.update(1, 2)
        self.assertEqual(result, list(queue))
        queue.update(3, 4)
        self.assertEqual(result, list(queue))
        queue.update(2, 3)
        self.assertEqual(result, list(queue))
        queue.update(0, 1)
        self.assertEqual(result, list(queue))

    return __update_the_same


class TestPrioritizedQueue(unittest.TestCase):

    test_add_forward_order_asc = _add_forward_order(PrioritizedQueue.ORDERING_ASCENDING)
    test_add_forward_order_desc = _add_forward_order(PrioritizedQueue.ORDERING_DESCENDING)

    test_add_backward_order_asc = _add_backward_order(PrioritizedQueue.ORDERING_ASCENDING)
    test_add_backward_order_desc = _add_backward_order(PrioritizedQueue.ORDERING_DESCENDING)

    test_add_chess_order_asc = _add_chess_order(PrioritizedQueue.ORDERING_ASCENDING)
    test_add_chess_order_desc = _add_chess_order(PrioritizedQueue.ORDERING_DESCENDING)

    test_add_corner_cases_asc = _add_corner_cases(PrioritizedQueue.ORDERING_ASCENDING)
    test_add_corner_cases_desc = _add_corner_cases(PrioritizedQueue.ORDERING_DESCENDING)

    test_update_no_item_asc = _update_no_item(PrioritizedQueue.ORDERING_ASCENDING)
    test_update_no_item_desc = _update_no_item(PrioritizedQueue.ORDERING_DESCENDING)

    test_update_increase_asc = _update_increase(PrioritizedQueue.ORDERING_ASCENDING)
    test_update_increase_desc = _update_increase(PrioritizedQueue.ORDERING_DESCENDING)

    test_update_decrease_asc = _update_decrease(PrioritizedQueue.ORDERING_ASCENDING)
    test_update_decrease_desc = _update_decrease(PrioritizedQueue.ORDERING_DESCENDING)

    test_update_the_same_asc = _update_the_same(PrioritizedQueue.ORDERING_ASCENDING)
    test_update_the_same_desc = _update_the_same(PrioritizedQueue.ORDERING_DESCENDING)


if __name__ == '__main__':
    unittest.main()
