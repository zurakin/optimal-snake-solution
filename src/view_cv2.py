import cv2
import numpy as np
import time

from src.presenter import Presenter


class View:
    GRID_W = 20
    GRID_H = 15
    TILE_SIZE = 40
    WINDOW_NAME = "Snake AI"
    HEAD_COLOR = (255, 0, 0)
    BODY_COLOR = (0, 255, 0)
    APPLE_COLOR = (0, 0, 255)

    def __init__(self):
        self.delay_between_moves = .2
        self.presenter = Presenter(self, self.GRID_H, self.GRID_W)
        self.canvas = np.zeros((self.GRID_H * self.TILE_SIZE, self.GRID_W * self.TILE_SIZE, 3), dtype=np.uint8)
        self.init_window()

    def init_window(self):
        cv2.namedWindow(self.WINDOW_NAME)
        cv2.imshow(self.WINDOW_NAME, self.canvas)

    def display_tile(self, i, j, im_array, tile_color):
        border_color = (0, 0, 0)

        x1, y1 = i * self.TILE_SIZE, j * self.TILE_SIZE
        x2, y2 = x1 + self.TILE_SIZE, y1 + self.TILE_SIZE

        tile = np.zeros((self.TILE_SIZE, self.TILE_SIZE, 3), dtype=np.uint8)
        tile[:] = tile_color
        cv2.rectangle(tile, (0, 0), (self.TILE_SIZE - 1, self.TILE_SIZE - 1), border_color, 2)

        im_array[y1:y2, x1:x2] = tile

    def display_grid(self, snake_head, snake_body, apple_position):
        im_array = np.copy(self.canvas)
        for i in range(self.GRID_H):
            for j in range(self.GRID_W):
                if (i, j) in snake_body:
                    color = self.BODY_COLOR
                elif (i, j) == apple_position:
                    color = self.APPLE_COLOR
                elif (i, j) == snake_head:
                    color = self.HEAD_COLOR
                else:
                    color = (255, 255, 255)
                self.display_tile(j, i, im_array, color)
        cv2.imshow(self.WINDOW_NAME, im_array)
    def game_loop(self):
        current_time = time.time()
        while True:
            new_time = time.time()
            if new_time - current_time >= self.delay_between_moves:
                current_time = new_time
                self.presenter.move()

            key = cv2.pollKey()
            if key == 13:  # Enter key
                self.presenter.restart()
            elif key == 2490368:  # Up key
                self.presenter.key_up()
            elif key == 2555904:  # Right key
                self.presenter.key_right()
            elif key == 2621440:  # Down key
                self.presenter.key_down()
            elif key == 2424832:  # Left key
                self.presenter.key_left()
            elif key == 104:  # H key (Help)
                pass
            elif key == 27:  # Escape key
                break

    def update_speed(self, snake_length):
        if snake_length < 10:
            self.delay_between_moves = .2
        elif snake_length < 20:
            self.delay_between_moves = .15
        elif snake_length < 30:
            self.delay_between_moves = .10
        elif snake_length < 20:
            self.delay_between_moves = .05
        else:
            self.delay_between_moves = .03

