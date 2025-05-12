import pygame

import game_engine
from .base_state import BaseState
from game_objects.ball import Ball
from game_objects.player_bar import PlayerBar


class MenuState(BaseState):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font = pygame.font.Font(None, 74)
        self.title = self.font.render("Pong Game", True, (255, 255, 255))
        self.start_text = self.font.render(
            "Press SPACE to Start", True, (255, 255, 255)
        )
        self.guide_text = self.font.render("Press G for Guide", True, (255, 255, 255))
        self.settings_text = self.font.render(
            "Press S for Settings", True, (255, 255, 255)
        )

    def update(self, delta_time):
        pass

    def draw(self, screen):
        screen.fill("BLACK")
        screen.blit(
            self.title, (screen.get_width() // 2 - self.title.get_width() // 2, 100)
        )
        screen.blit(
            self.start_text,
            (screen.get_width() // 2 - self.start_text.get_width() // 2, 300),
        )
        screen.blit(
            self.guide_text,
            (screen.get_width() // 2 - self.guide_text.get_width() // 2, 400),
        )
        screen.blit(
            self.settings_text,
            (screen.get_width() // 2 - self.settings_text.get_width() // 2, 500),
        )

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.game_engine.state_manager.change_state("gameplay")
            elif event.key == pygame.K_g:
                self.game_engine.state_manager.change_state("guide")
            elif event.key == pygame.K_s:
                self.game_engine.state_manager.change_state("settings")

    def enter(self) -> None:
        pass


class GameplayState(BaseState):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.context = game_engine.context  # this is a refgame_engine
        self.player_bar = PlayerBar(game_engine.queue, game_engine.context)
        init_speed = (3, 3) if (self.context["difficulty"]) == 1 else (5, 5)
        self.ball = Ball(
            init_speed,
            1,
            self.context,
        )
        self.objects = [self.ball, self.player_bar]
        self.font = pygame.font.Font(None, 74)

    def update(self, delta_time):
        self.player_bar.move()
        self.ball.move(delta_time / 10000, self.player_bar)

        if self.ball.is_over():
            self.game_engine.state_manager.change_state("game_over")

    def draw(self, screen):
        screen.fill("BLACK")
        text = self.font.render(
            f"Score: {self.context['counter']}", True, (255, 255, 255)
        )
        text_rect = text.get_rect(center=(screen.get_width() // 2, 50))
        screen.blit(text, text_rect)

        for obj in self.objects:
            obj.draw(screen)

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game_engine.state_manager.change_state("menu")

    def enter(self) -> None:
        # Reset the ball and player bar positions
        self.context["counter"] = 0  # reset the counter
        init_speed = (3, 3) if (self.context["difficulty"]) == 1 else (5, 5)
        accel = self.context["difficulty"]
        self.ball.reset(
            init_speed,
            accel,
        )


class GameOverState(BaseState):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font = pygame.font.Font(None, 74)
        self.game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        self.restart_text = self.font.render(
            "Press R to Restart", True, (255, 255, 255)
        )
        self.menu_text = self.font.render("Press ESC for Menu", True, (255, 255, 255))

    def update(self, delta_time):
        pass

    def draw(self, screen):
        screen.fill("RED")
        screen.blit(
            self.game_over_text,
            (screen.get_width() // 2 - self.game_over_text.get_width() // 2, 200),
        )
        screen.blit(
            self.restart_text,
            (screen.get_width() // 2 - self.restart_text.get_width() // 2, 300),
        )
        screen.blit(
            self.menu_text,
            (screen.get_width() // 2 - self.menu_text.get_width() // 2, 400),
        )

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.game_engine.state_manager.change_state("gameplay")
            elif event.key == pygame.K_ESCAPE:
                self.game_engine.state_manager.change_state("menu")
    def enter(self):
        pass


class GuideState(BaseState):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 74)
        self.title = self.title_font.render("How to Play", True, (255, 255, 255))
        self.instructions = [
            "1. Use your index finger to control the bar",
            "2. Keep the ball from reaching the left side of the screen",
            "3. Each successful hit increases your score",
            "4. Try to achieve the highest score possible!",
            "",
            "Controls:",
            "- Move your index finger up/down to control the bar",
            "- ESC: Return to menu",
            "- SPACE: Start game",
            "- S: Settings",
            "- G: This guide",
        ]
        self.return_text = self.font.render(
            "Press ESC to Return", True, (255, 255, 255)
        )

    def update(self, delta_time):
        pass

    def draw(self, screen):
        screen.fill("BLACK")
        # Draw title
        screen.blit(
            self.title, (screen.get_width() // 2 - self.title.get_width() // 2, 50)
        )

        # Draw instructions
        for i, line in enumerate(self.instructions):
            text = self.font.render(line, True, (255, 255, 255))
            screen.blit(
                text, (screen.get_width() // 2 - text.get_width() // 2, 150 + i * 40)
            )

        # Draw return text
        screen.blit(
            self.return_text,
            (screen.get_width() // 2 - self.return_text.get_width() // 2, 550),
        )

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game_engine.state_manager.change_state("menu")

    def enter(self) -> None:
        pass


class SettingsState(BaseState):
    def __init__(self, game_engine):
        super().__init__(game_engine)
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 74)
        self.title = self.title_font.render("Settings", True, (255, 255, 255))
        self.volume = 50
        self.difficulty = 1
        self.return_text = self.font.render(
            "Press ESC to Return", True, (255, 255, 255)
        )

    def update(self, delta_time):
        pass

    def draw(self, screen):
        screen.fill("BLACK")
        # Draw title
        screen.blit(
            self.title, (screen.get_width() // 2 - self.title.get_width() // 2, 50)
        )

        # Draw volume settings
        volume_text = self.font.render(f"Volume: {self.volume}%", True, (255, 255, 255))
        volume_help = self.font.render(
            "Use UP/DOWN arrows to adjust", True, (255, 255, 255)
        )
        screen.blit(
            volume_text, (screen.get_width() // 2 - volume_text.get_width() // 2, 200)
        )
        screen.blit(
            volume_help, (screen.get_width() // 2 - volume_help.get_width() // 2, 240)
        )

        # Draw difficulty settings
        difficulty_text = self.font.render(
            f"Difficulty: {'Easy' if self.difficulty == 1 else 'Hard'}",
            True,
            (255, 255, 255),
        )
        difficulty_help = self.font.render(
            "Press D to toggle difficulty", True, (255, 255, 255)
        )
        screen.blit(
            difficulty_text,
            (screen.get_width() // 2 - difficulty_text.get_width() // 2, 300),
        )
        screen.blit(
            difficulty_help,
            (screen.get_width() // 2 - difficulty_help.get_width() // 2, 340),
        )

        # Draw return text
        screen.blit(
            self.return_text,
            (screen.get_width() // 2 - self.return_text.get_width() // 2, 550),
        )

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game_engine.state_manager.change_state("menu")
            elif event.key == pygame.K_UP:
                self.volume = min(100, self.volume + 5)
                pygame.mixer.music.set_volume(self.volume / 100)
            elif event.key == pygame.K_DOWN:
                self.volume = max(0, self.volume - 5)
                pygame.mixer.music.set_volume(self.volume / 100)
            elif event.key == pygame.K_d:
                self.difficulty = 2 if self.difficulty == 1 else 1

    def enter(self) -> None:
        pass
