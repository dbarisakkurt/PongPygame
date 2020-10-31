import pygame
import Constants
import Player
import Ball
from pygame.locals import (
    K_UP, K_DOWN,
    K_ESCAPE, K_SPACE,
    K_w, K_s,
    K_b, K_g
)

pygame.init()
pygame.display.set_caption(Constants.APP_NAME)

screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

font1 = pygame.font.SysFont(Constants.FONT_NAME, Constants.LETTER_SIZE_SMALL)
game_title = font1.render(Constants.START_TEXT_TITLE, True, Constants.BLUE)
game_explanation1 = font1.render(Constants.START_TEXT_EXPLANATION1, True, Constants.BLUE)
game_explanation2 = font1.render(Constants.START_TEXT_EXPLANATION2, True, Constants.BLUE)

player1 = Player.Player(30, 100, K_w, K_s, 0, 0)
player2 = Player.Player(30, 100, K_UP, K_DOWN, Constants.SCREEN_WIDTH-30, 0)

ball = Ball.Ball()

all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)

balls = pygame.sprite.Group()
balls.add(ball)

clock = pygame.time.Clock()
bg_Color = Constants.RED

is_menu_open=True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_b:
                bg_Color=Constants.BLACK
            if event.key == K_g:
                bg_Color=Constants.GRAY
            if event.key == K_SPACE:
                is_menu_open = False

    if is_menu_open:
        screen.fill(bg_Color)
        screen.blit(game_title, (50, 200))
        screen.blit(game_explanation1, (50, 300))
        screen.blit(game_explanation2, (50, 350))
    else:
        screen.fill(bg_Color)
        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        ball.draw(screen)
        

        pressed_keys = pygame.key.get_pressed()

        player1.update(pressed_keys)
        player2.update(pressed_keys)
        ball.update()

        # Check collisions

        if pygame.sprite.spritecollideany(player1, balls):
            if ball.y > Constants.SCREEN_HEIGHT - Constants.BALL_SIZE  or ball.y < Constants.BALL_SIZE+100:
                ball.change_y *= -1
            if ball.x > Constants.SCREEN_WIDTH - Constants.BALL_SIZE  or ball.x < Constants.BALL_SIZE+30:
                ball.change_x *= -1

        if pygame.sprite.spritecollideany(player2, balls):
            if ball.y > Constants.SCREEN_HEIGHT - Constants.BALL_SIZE -100 or ball.y < Constants.BALL_SIZE:
                ball.change_y *= -1
            if ball.x > Constants.SCREEN_WIDTH - Constants.BALL_SIZE -30 or ball.x < Constants.BALL_SIZE:
                ball.change_x *= -1

        if ball.x > Constants.SCREEN_WIDTH - Constants.BALL_SIZE or ball.x < Constants.BALL_SIZE:
            running=False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
