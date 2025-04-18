from game_engine import  SCREEN_HEIGHT
import pygame


class PlayerBar:

    BAR_HEIGHT = 100
    BAR_WIDTH = 30
    

    def __init__(self, queue, context) -> None:
        self._x = 0
        self._y = 0
        self._queue = queue
        self._context = context

    def move(self):

        queue = self._queue

        # take only the last one
        while not queue.empty():
            self._y = queue.get()

    def draw(self, screen: pygame.Surface):
        bar_cords = (0, self._y * SCREEN_HEIGHT, PlayerBar.BAR_WIDTH, PlayerBar.BAR_HEIGHT)
        pygame.draw.rect(screen, "BLUE", bar_cords,0)



    @property
    def y(self):
        return self._y*SCREEN_HEIGHT



