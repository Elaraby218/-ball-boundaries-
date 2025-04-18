import pygame


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


from game_objects.player_bar import PlayerBar

from game_objects.ball import Ball


def game(queue):

    context = {
            "counter" : 0}


    ball = Ball((3,3), 0.001, context)
    player_bar = PlayerBar(queue,context)
    objects = [ball, player_bar]
    ms = 0

    pygame.init()
    font = pygame.font.Font(None, 74)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Pygame Window")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        delta_time = pygame.time.get_ticks() - ms
        ms = pygame.time.Clock().tick(60)
        player_bar.move()
        ball.move(delta_time / 10000, player_bar)

        screen.fill("BLACK")


        text = font.render(f"Score :{context['counter']}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)

        if ball.is_over():
            screen.fill("RED")
            text = font.render("Game Over", True, (255, 255, 255))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(10000)

        for obj in objects:
            obj.draw(screen)

        # show counter 

        

        pygame.display.flip()


