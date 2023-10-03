from src.model import Model


class Presenter:
    def __init__(self, view, height, width):
        self.view = view
        self.model = Model(height, width)
        self.height = height
        self.width = width
        self.game_over = False

    def move(self):
        if self.game_over:
            return
        snake_length, game_over = self.model.move()
        self.game_over = game_over
        self.view.update_speed(snake_length)
        self.view.display_grid(self.model.get_snake_head(), self.model.get_snake_body(),
                               self.model.get_apple_position())

    def key_up(self):
        self.model.queue_direction((-1, 0))

    def key_down(self):
        self.model.queue_direction((1, 0))

    def key_right(self):
        self.model.queue_direction((0, 1))

    def key_left(self):
        self.model.queue_direction((0, -1))

    def restart(self):
        self.model = Model(self.height, self.width)
        self.game_over = False
