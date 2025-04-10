import pygame
import level1
import game
import sys


def display_loss_screen():
    print("You lost")  # Replace this with a fail screen
    # Initialize pygame

    pygame.init()

    game_over = pygame.image.load("game_over.png")
    # Store window width and height in a tuple.
    game_over_size = game_over.get_size()
    game_over_rect = game_over.get_rect()

    # create the window based on the map size
    screen = pygame.display.set_mode(game_over_size)
    game_over = game_over.convert_alpha()
    # game_over.set_colorkey((255, 255, 255))
    game_over_mask = pygame.mask.from_surface(game_over)
    # screen.fill((150, 150, 150))  # This helps check if the image path is transparent
    space_not_pressed = True


    while space_not_pressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_alive = False
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        screen.blit(game_over, game_over_rect)
        pygame.display.update()
        if keys[pygame.K_SPACE]:
            space_not_pressed = False
            game.main()
           

def display_win_screen():
    print("You win")  # Replace this with a fail screen
    # Initialize pygame

    pygame.init()

    you_win = pygame.image.load("you_win.png")
    # you_win = pygame.transform.smoothscale(you_win, (300, 300))

    # Store window width and height in a tuple.
    you_win_size = you_win.get_size()
    you_win_rect = you_win.get_rect()
    you_win_rect.center = (630, 388)

    # create the window based on the map size
    screen = pygame.display.set_mode((1265, 778))
    you_win = you_win.convert_alpha()
    # game_over.set_colorkey((255, 255, 255))
    you_win_mask = pygame.mask.from_surface(you_win)
    screen.fill((150, 150, 150))  # This helps check if the image path is transparent
    space_not_pressed = True


    while space_not_pressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_alive = False
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        screen.blit(you_win, you_win_rect)
        pygame.display.update()
        if keys[pygame.K_SPACE]:
            space_not_pressed = False
            pygame.quit()
            game.main()
    # print("You win")  # Replace this with a win screen
