import pygame
import numpy as np
import time

from src.presenter import Presenter


class ViewPyGame:
    GRID_W = 20
    GRID_H = 15
    TILE_SIZE = 40
    WINDOW_NAME = "Snake AI"
    HEAD_COLOR = (255, 0, 0)
    BODY_COLOR = (0, 255, 0)
    APPLE_COLOR = (0, 0, 255)

    def __init__(self):
        pygame.init()

        self.delay_between_moves = 0.2
        self.running = True
        self.presenter = Presenter(self, self.GRID_H, self.GRID_W)

        # Create a Pygame window
        self.screen = pygame.display.set_mode((self.GRID_W * self.TILE_SIZE, self.GRID_H * self.TILE_SIZE))
        pygame.display.set_caption(self.WINDOW_NAME)

    def display_tile(self, i, j, tile_color):
        x1, y1 = i * self.TILE_SIZE, j * self.TILE_SIZE
        pygame.draw.rect(self.screen, tile_color, (x1, y1, self.TILE_SIZE, self.TILE_SIZE))
        pygame.draw.rect(self.screen, (0, 0, 0), (x1, y1, self.TILE_SIZE, self.TILE_SIZE), 2)

    def display_grid(self, snake_head, snake_body, apple_position):
        self.screen.fill((255, 255, 255))

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
                self.display_tile(j, i, color)

        pygame.display.flip()

    def game_loop(self):
        current_time = time.time()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.on_key(event.key)

            new_time = time.time()
            if new_time - current_time >= self.delay_between_moves:
                current_time = new_time
                self.presenter.move()

    def on_key(self, key):
        if key == pygame.K_RETURN:
            self.presenter.restart()
        elif key == pygame.K_UP:
            self.presenter.key_up()
        elif key == pygame.K_RIGHT:
            self.presenter.key_right()
        elif key == pygame.K_DOWN:
            self.presenter.key_down()
        elif key == pygame.K_LEFT:
            self.presenter.key_left()
        elif key == pygame.K_h:
            pass
        elif key == pygame.K_ESCAPE:
            self.running = False

    def update_speed(self, snake_length):
        if snake_length < 10:
            self.delay_between_moves = 0.2
        elif snake_length < 20:
            self.delay_between_moves = 0.15
        elif snake_length < 30:
            self.delay_between_moves = 0.10
        elif snake_length < 20:
            self.delay_between_moves = 0.05
        else:
            self.delay_between_moves = 0.03
