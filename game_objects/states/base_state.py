from abc import ABC, abstractmethod
import pygame

class BaseState(ABC):
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.next_state = None

    @abstractmethod
    def update(self, delta_time):
        pass

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def handle_events(self, event):
        pass

    @abstractmethod
    def enter(self):
        pass


