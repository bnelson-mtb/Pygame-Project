import pygame, sys, math, random
# Starter code for an adventure game. Written by David Johnson for CS 1400 University of Utah.

# Finished game authors:
# Jessica Sutherland, Brady Nelson


def pixel_collision(mask1, rect1, mask2, rect2):
    """
    Check if the non-transparent pixels of one mask contacts the non-transparent pixels of another.
    """
    offset_x = rect2[0] - rect1[0]
    offset_y = rect2[1] - rect1[1]
    # See if the two masks at the offset are overlapping.
    overlap = mask1.overlap(mask2, (offset_x, offset_y))
    return overlap != None

def level1():
    """
    Level 1

    :return:
    """

    # Initialize pygame
    pygame.init()

    # Store window width and height in a tuple.
    level_1_map = pygame.image.load("map.png")
    level_1_map_size = level_1_map.get_size()
    level_1_map_rect = level_1_map.get_rect()

    # create the window based on the map size
    screen = pygame.display.set_mode(level_1_map_size)
    level_1_map = level_1_map.convert_alpha()
    level_1_map.set_colorkey((255, 255, 255))
    level_1_map_mask = pygame.mask.from_surface(level_1_map)

    # Create level 1 background
    background_1 = pygame.image.load("background_1.png").convert_alpha()
    background_1 = pygame.transform.smoothscale(background_1, level_1_map.get_size())  # Resize to MATCH the maze
    background_1_rect = background_1.get_rect()
    background_1_mask = pygame.mask.from_surface(background_1)

    # Create the player data
    player = pygame.image.load("diver.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (30, 30))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    # Create the trident
    trident = pygame.image.load("blacktridentt.png").convert_alpha()
    trident = pygame.transform.smoothscale(trident, (40, 40))
    trident_rect = trident.get_rect()
    trident_rect.center = (426, 103)
    trident_mask = pygame.mask.from_surface(trident)

    # Create poseidon
    poseidon = pygame.image.load("poseidon.png").convert_alpha()
    poseidon = pygame.transform.smoothscale(poseidon, (120, 120))
    poseidon_rect = poseidon.get_rect()
    poseidon_rect.center = (189, 649)
    poseidon_mask = pygame.mask.from_surface(poseidon)

    # Create start button
    start_button = pygame.image.load("start.png").convert_alpha()
    start_button = pygame.transform.smoothscale(start_button, (90, 60))
    start_button_rect = start_button.get_rect()
    start_button_rect.center = (145, 126)
    start_button_mask = pygame.mask.from_surface(start_button)

    # The frame tells which sprite frame to draw
    frame_count = 0

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # Get a font to use to write on the screen.
    message_font = pygame.font.SysFont('monospace', 24)

    # The started variable records if the start color has been clicked and the level started
    started = False
    trident_found = False

    # The is_alive variable records if anything bad has happened (off the path, touch guard, etc.)
    is_alive = True

    # Hide the arrow cursor and replace it with a sprite.
    pygame.mouse.set_visible(False)

    # This is the main game loop. In it, we must:
    # - check for events
    # - update the scene
    # - draw the scene
    while is_alive:
        # Check events by looping over the list of events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_alive = False
            if pixel_collision(player_mask, player_rect, start_button_mask, start_button_rect):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    started = True

        # Position the player to the mouse location
        pos = pygame.mouse.get_pos()
        player_rect.center = pos

        # If the start button is clicked
        if started:
            # Check for collision with the door if it is not opened by the key.
            if not trident_found and pixel_collision(player_mask, player_rect, poseidon_mask, poseidon_rect):
                return False

            # Check for a collision with the trident.
            if not trident_found and pixel_collision(player_mask, player_rect, trident_mask, trident_rect):
                trident_found = True

            # Check for a collision with poseidon if he is brought the trident.
            if trident_found and pixel_collision(player_mask, player_rect, poseidon_mask, poseidon_rect):
                return True

            # See if we touch the maze walls
            if pixel_collision(player_mask, player_rect, level_1_map_mask, level_1_map_rect):
                return False

            # If the trident is found, it follows the player
            if trident_found:
                pos = pygame.mouse.get_pos()
                trident_rect.center = pos

        # Do updates above and drawing below.

        # Draw the background
        screen.fill((150,150,150)) # This helps check if the image path is transparent
        screen.blit(background_1, background_1_rect)
        screen.blit(level_1_map, level_1_map_rect)

        # Draw the start button only if it hasn't been clicked
        if not started:
            screen.blit(start_button, start_button_rect)

        # Draw the player character
        screen.blit(player, player_rect)

        # Draw poseidon and the trident
        screen.blit(poseidon, poseidon_rect)
        screen.blit(trident, trident_rect)

        # Write some text to the screen. You can do something like this to show some hints or whatever you want.
        label = message_font.render("Find the trident and bring it to Poseidon to escape! ",
                                    True, (0,0,0))
        screen.blit(label, (20,20))

        # Every time through the loop, increase the frame count.
        frame_count += 1

        # Bring drawn changes to the front
        pygame.display.update()

        # This tries to force the loop to run at 60 fps
        clock.tick(60)
