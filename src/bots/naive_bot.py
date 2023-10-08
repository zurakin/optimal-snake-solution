from src.bots.bot import SnakeBot

class NaiveBot(SnakeBot):
    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)

    def __init__(self, width, height):
        super().__init__(width, height)
        self.moves_queue = []

    def calculate_moves_queue(self, snake_head, snake_body, apple_position, snake_direction):
        if snake_head[1] == 0:
            self.moves_queue.insert(0, self.DOWN)
            self.moves_queue.insert(0, self.RIGHT)
        elif snake_head[1] == self.width - 1:
            self.moves_queue.insert(0, self.DOWN)
            self.moves_queue.insert(0, self.LEFT)
        else:
            self.moves_queue.insert(0, snake_direction)

    def get_next_move(self, snake_head, snake_body, apple_position, snake_direction):
        if len(self.moves_queue) == 0:
            self.calculate_moves_queue(snake_head, snake_body, apple_position, snake_direction)
        move = self.moves_queue.pop()
        print("move: ", move)
        return move


