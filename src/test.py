import unittest

from src.model import Model


class Tests(unittest.TestCase):
    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)
    def test_model_queue(self):
        directions = [self.UP, self.RIGHT, self.DOWN, self.LEFT]
        model = Model(30, 30)
        self.assertEqual(len(model.get_direction_queue()), 1)
        initial_direction = model.get_direction_queue()[0]
        model.queue_direction(initial_direction)
        model.queue_direction(initial_direction)
        self.assertEqual(len(model.get_direction_queue()), 1)
        direction = directions[(directions.index(initial_direction)+1)%4]
        model.queue_direction(direction)
        model.queue_direction(direction)
        self.assertEqual(len(model.get_direction_queue()), 2)
        model.queue_direction((-direction[0], -direction[1]))
        self.assertEqual(len(model.get_direction_queue()), 2)
