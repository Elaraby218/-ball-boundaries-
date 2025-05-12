import pygame

class Button:
    def __init__(self, x, y, width, height, text, color=(100, 100, 100), hover_color=(150, 150, 150)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)  # White border

        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered:
                return True
        return False

class Menu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.buttons = []
        self.setup_buttons()

    def setup_buttons(self):
        button_width = 200
        button_height = 50
        spacing = 20
        start_y = self.screen_height // 2 - (button_height * 1.5 + spacing)

        # Create buttons
        self.play_button = Button(
            self.screen_width // 2 - button_width // 2,
            start_y,
            button_width,
            button_height,
            "Play"
        )
        
        self.guide_button = Button(
            self.screen_width // 2 - button_width // 2,
            start_y + button_height + spacing,
            button_width,
            button_height,
            "Guide"
        )
        
        self.settings_button = Button(
            self.screen_width // 2 - button_width // 2,
            start_y + (button_height + spacing) * 2,
            button_width,
            button_height,
            "Settings"
        )

        self.buttons = [self.play_button, self.guide_button, self.settings_button]

    def draw(self, screen):
        # Draw title
        title_font = pygame.font.Font(None, 74)
        title_text = title_font.render("Ball Boundaries", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(self.screen_width // 2, self.screen_height // 4))
        screen.blit(title_text, title_rect)

        # Draw buttons
        for button in self.buttons:
            button.draw(screen)

    def handle_event(self, event):
        for button in self.buttons:
            if button.handle_event(event):
                if button == self.play_button:
                    return "play"
                elif button == self.guide_button:
                    return "guide"
                elif button == self.settings_button:
                    return "settings"
        return None 