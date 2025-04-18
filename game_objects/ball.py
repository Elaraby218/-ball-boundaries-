from typing import Tuple
from game_engine import  SCREEN_WIDTH, SCREEN_HEIGHT

from game_objects.player_bar import PlayerBar
import pygame


class Ball:

    def __init__(self, init_speed: Tuple[float, float], speed_inc: float ,context) -> None:
        self._x = PlayerBar.BAR_WIDTH + 50
        self._y = 30
        self._speed = init_speed
        self._sppend_inc = speed_inc
        self._context = context

    def _collide(self, on_X: bool):
        """
        Collide with a wall, change the direction of the Ball
        :param on_X: True if the ball collides with a wall on the X axis
        :return: None

        """

        self._speed = (
            self._speed[0] * -1 if on_X else self._speed[0],
            self._speed[1] * -1 if not on_X else self._speed[1],
        )

    def _increase_speed(self):
        """
        Increase the speed of the ball by the speed increment
        :return: None
        """
        self._speed = (
            abs(self._speed[0]) + self._sppend_inc,
            abs(self._speed[1]) + self._sppend_inc,
        )

        sign = (1 if self._speed[0] > 0 else -1, 1 if self._speed[1] > 0 else -1)

        self._speed = (sign[0] * self._speed[0], sign[1] * self._speed[1])

    def move(self, delta_time:float, player_bar: PlayerBar):
        """
        Move the ball by the speed value
        :return: None
        """
        self._x += self._speed[0] * delta_time
        self._y += self._speed[1] * delta_time
        if (
            self._x <= PlayerBar.BAR_WIDTH and
            player_bar.y <= self._y <= player_bar.y + player_bar.BAR_HEIGHT
        ):
            self._x = PlayerBar.BAR_WIDTH + 1
            self._collide(True)
            self._context['counter'] +=1
            # self._increase_speed()

        elif self._x >= SCREEN_WIDTH:
            self._x = SCREEN_WIDTH
            self._collide(True)
        if self._y <= 0:
            self._y = 0
            self._collide(False)
        elif self._y >= SCREEN_HEIGHT:
            self._y = SCREEN_HEIGHT
            self._collide(False)

    def draw(self, screen: pygame.Surface):
        """
        Draw the ball on the screen
        :param screen: The screen to draw on
        :return: None
        """
        pygame.draw.circle(screen, "RED", (int(self._x), int(self._y)), 10)

    def is_over(self) -> bool:
        """
        Check if the ball is over the bar
        """
        return self._x < PlayerBar.BAR_WIDTH
