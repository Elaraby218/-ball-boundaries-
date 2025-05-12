import pygame
from menu import Menu


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


from game_objects.player_bar import PlayerBar

from game_objects.ball import Ball


def game(queue):

    context = {
        "counter" : 0
    }


    ball = Ball((3,3), 1, context)
    player_bar = PlayerBar(queue,context)
    objects = [ball, player_bar]
    ms = 0

    pygame.init()
    font = pygame.font.Font(None, 74)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ball Boundaries")

    # Initialize menu
    menu = Menu(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Game states
    current_state = "menu"  # Can be "menu", "playing", "guide", "settings"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if current_state == "menu":
                action = menu.handle_event(event)
                if action == "play":
                    current_state = "playing"
                elif action == "guide":
                    current_state = "guide"
                elif action == "settings":
                    current_state = "settings"
            elif current_state == "playing":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    current_state = "menu"
                    ball.reset()
                    context['counter'] = 0

        screen.fill("BLACK")

        if current_state == "menu":
            menu.draw(screen)
        elif current_state == "playing":
            delta_time = pygame.time.get_ticks() - ms
            ms = pygame.time.Clock().tick(60)
            player_bar.move()
            ball.move(delta_time / 10000, player_bar)

            text = font.render(f"Score: {context['counter']}", True, (255, 255, 255))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 50))
            screen.blit(text, text_rect)

            if ball.is_over():
                screen.fill("RED")
                text = font.render(f"Game Over\nYour Score is {context['counter']}", True, (255, 255, 255))
                text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                screen.blit(text, text_rect)
                
                # Show restart instructions
                restart_font = pygame.font.Font(None, 36)
                restart_text = restart_font.render("Press R to restart or ESC to return to menu", True, (255, 255, 255))
                restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
                screen.blit(restart_text, restart_rect)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            ball.reset()
                            context['counter'] = 0
                        elif event.key == pygame.K_ESCAPE:
                            current_state = "menu"
                            ball.reset()
                            context['counter'] = 0
            else:
                for obj in objects:
                    obj.draw(screen)
        elif current_state == "guide":
            guide_font = pygame.font.Font(None, 36)
            guide_text = [
                "How to Play:",
                "1. Use arrow keys to move the paddle",
                "2. Keep the ball from falling",
                "3. Each successful hit increases your score",
                "",
                "Press ESC to return to menu"
            ]
            
            for i, line in enumerate(guide_text):
                text = guide_font.render(line, True, (255, 255, 255))
                text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 150 + i * 40))
                screen.blit(text, text_rect)
                
        elif current_state == "settings":
            settings_font = pygame.font.Font(None, 36)
            settings_text = [
                "Settings",
                "Coming soon...",
                "",
                "Press ESC to return to menu"
            ]
            
            for i, line in enumerate(settings_text):
                text = settings_font.render(line, True, (255, 255, 255))
                text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 150 + i * 40))
                screen.blit(text, text_rect)

        pygame.display.flip()


