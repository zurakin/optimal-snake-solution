import random


class Model:
    TELEPORT_ON = True

    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.snake_head = (height // 2, width // 2)
        self.snake_body = [self.__get_position(self.snake_head, (0, 1))]
        self.direction_queue = []
        self.current_direction = (0, -1)
        self.apple_position = (0, 0)
        self.spawn_apple()

    def get_direction_queue(self):
        return self.direction_queue

    def spawn_apple(self):
        self.apple_position = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
        while self.apple_position in self.snake_body or self.apple_position == self.snake_head:
            self.apple_position = random.randint(0, self.height - 1), random.randint(0, self.width - 1)

    def move(self):
        self.snake_body.insert(0, self.snake_head)
        if len(self.direction_queue) > 0:
            direction = self.direction_queue.pop()
            self.current_direction = direction
        else:
            direction = self.current_direction
        self.snake_head = self.__get_position(self.snake_head, direction)
        if self.snake_head is None:
            game_over = True
            return len(self.snake_body) + 1, game_over
        if self.snake_head == self.apple_position:
            self.spawn_apple()
        else:
            self.snake_body.pop()
        game_over = self.snake_head in self.snake_body
        return len(self.snake_body) + 1, game_over

    def queue_direction(self, direction):
        if len(self.direction_queue) > 0 and (self.direction_queue[0] == direction or self.direction_queue[0] == (-direction[0], -direction[1])):
            return
        if len(self.direction_queue) == 0 and (self.current_direction == direction or self.current_direction == (-direction[0], -direction[1])):
            return

        self.direction_queue.insert(0, direction)

    def __get_position(self, position, direction):
        y, x = position[0] + direction[0], position[1] + direction[1]
        if 0 <= y < self.height and 0 <= x < self.width:
            return y, x
        if self.TELEPORT_ON:
            return y % self.height, x % self.width
        return None

    def get_snake_head(self):
        return self.snake_head

    def get_snake_body(self):
        return self.snake_body

    def get_apple_position(self):
        return self.apple_position

    def get_current_direction(self):
        return self.current_direction
