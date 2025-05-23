SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

from typing import TypedDict
import pygame


from game_objects.states.state_manager import StateManager
from game_objects.states.game_states import MenuState, GameplayState, GameOverState, GuideState, SettingsState


class GameContext(TypedDict):
    counter: int
    volume: int
    difficulty: int

class GameEngine:
    def __init__(self, queue):
        self.queue = queue
        self.state_manager = StateManager()
        self.context: GameContext = {
            "counter": 0,
            "volume": 50,
            "difficulty": 1
        }
        self._initialize_states()
        self._initialize_audio()
        
    def _initialize_audio(self):
        pygame.mixer.init()
        pygame.mixer.music.load('assets/sounds/background.mp3')
        pygame.mixer.music.set_volume(0.5)  # Set initial volume to 50%
        pygame.mixer.music.play(-1)  # -1 means loop indefinitely
        
    def _initialize_states(self):
        self.state_manager.add_state("menu", MenuState(self))
        self.state_manager.add_state("gameplay", GameplayState(self))
        self.state_manager.add_state("game_over", GameOverState(self))
        self.state_manager.add_state("guide", GuideState(self))
        self.state_manager.add_state("settings", SettingsState(self))
        self.state_manager.change_state("menu")

    def update(self, delta_time):
        self.state_manager.update(delta_time)

    def draw(self, screen):
        self.state_manager.draw(screen)

def game(queue):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong Game")
    
    game_engine = GameEngine(queue)
    clock = pygame.time.Clock()
    ms = 0

    while True:
        delta_time = pygame.time.get_ticks() - ms
        ms = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            game_engine.state_manager.handle_event(event)

        game_engine.update(delta_time)
        game_engine.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
