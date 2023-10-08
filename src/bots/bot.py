from abc import ABC, abstractmethod


class SnakeBot(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @abstractmethod
    def get_next_move(self, snake_head, snake_body, apple_position, snake_direction):
        pass
