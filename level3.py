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

# def draw(self, screen):
#     screen.blit(self.image, self.rectangle)
def level3():
    """
    Level 3

    :return:
        """

    # Initialize pygame
    pygame.init()

    # Store window width and height in a tuple.
    level_3_map = pygame.image.load("Level 3.png")
    level_3_map_size = level_3_map.get_size()
    print(level_3_map_size)
    level_3_map_rect = level_3_map.get_rect()

    # create the window based on the map size
    screen = pygame.display.set_mode(level_3_map_size)
    level_3_map = level_3_map.convert_alpha()
    level_3_map.set_colorkey((255, 255, 255))
    level_3_map_mask = pygame.mask.from_surface(level_3_map)

    # Create the level 3 background
    background_3 = pygame.image.load("background_3.png").convert_alpha()
    background_3 = pygame.transform.smoothscale(background_3, level_3_map.get_size())  # Resize to MATCH the maze
    background_3_rect = background_3.get_rect()
    background_3_mask = pygame.mask.from_surface(background_3)

    # Create the player data
    player = pygame.image.load("diver.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (30, 30))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    # Create the trident
    trident = pygame.image.load("blacktridentt.png").convert_alpha()
    trident = pygame.transform.smoothscale(trident, (40, 40))
    trident_rect = trident.get_rect()
    trident_rect.center = (151, 140)
    trident_mask = pygame.mask.from_surface(trident)

    # Create poseidon
    poseidon = pygame.image.load("poseidon.png").convert_alpha()
    poseidon = pygame.transform.smoothscale(poseidon, (120, 120))
    poseidon_rect = poseidon.get_rect()
    poseidon_rect.center = (650, 600)
    poseidon_mask = pygame.mask.from_surface(poseidon)

    # Create the fish
    fish = pygame.image.load("fish.png").convert_alpha()
    fish = pygame.transform.smoothscale(fish, (120, 120))
    fish_rect = poseidon.get_rect()
    fish_rect.center = (367, 471)
    fish_mask = pygame.mask.from_surface(fish)

    # Create the sword
    sword = pygame.image.load("sword.png").convert_alpha()
    sword = pygame.transform.smoothscale(sword, (80, 80))
    sword_rect = poseidon.get_rect()
    sword_rect.center = (805, 633)
    sword_mask = pygame.mask.from_surface(sword)

    # Create start button
    start_button = pygame.image.load("start.png").convert_alpha()
    start_button = pygame.transform.smoothscale(start_button, (90, 60))
    start_button_rect = start_button.get_rect()
    start_button_rect.center = (1001, 125)
    start_button_mask = pygame.mask.from_surface(start_button)

    # Create the poseidon guards
    poseidon_guard = pygame.image.load("poseidon_guard.png").convert_alpha()
    poseidon_guard = pygame.transform.smoothscale(poseidon_guard, (70,70))
    poseidon_guard_rect = poseidon_guard.get_rect()
    poseidon_guard_rect.center = (461, 568)
    poseidon_guard_mask = pygame.mask.from_surface(poseidon_guard)

    poseidon_guard_2 = pygame.image.load("poseidon_guard.png").convert_alpha()
    poseidon_guard_2 = pygame.transform.smoothscale(poseidon_guard_2, (70, 70))
    poseidon_guard_2_rect = poseidon_guard_2.get_rect()
    poseidon_guard_2_rect.center = (638, 243)
    poseidon_guard_2_mask = pygame.mask.from_surface(poseidon_guard_2)

    # Guard movement attributes
    poseidon_guard_direction = 1  # 1 for right, -1 for left
    poseidon_guard_speed = 3  # How many pixels to move each frame
    poseidon_guard_2_direction = 1  # 1 for right, -1 for left
    poseidon_guard_2_speed = 3  # How many pixels to move each frame

    # The frame tells which sprite frame to draw
    frame_count = 0

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # Get a font to use to write on the screen.
    message_font = pygame.font.SysFont('helvetica', 24)

    # The started variable records if the start color has been clicked and the level started
    started = False
    trident_found = False
    fish_locked = True
    sword_not_found = True

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
                if event.type == pygame.MOUSEBUTTONUP:
                    started = True

        # Position the player to the mouse location
        pos = pygame.mouse.get_pos()
        player_rect.center = pos

        # If the start button is clicked
        if started:
            # See if we touch the poseidon_guard
            if pixel_collision(player_mask, player_rect, poseidon_guard_mask, poseidon_guard_rect):
                return False
            if pixel_collision(player_mask, player_rect, poseidon_guard_2_mask, poseidon_guard_2_rect):
                return False
            # Check for collision with the fish if it is not opened by the sword.
            if not trident_found and pixel_collision(player_mask, player_rect, poseidon_mask, poseidon_rect):
                return False

            # Check for a collision with the trident.
            if not trident_found and pixel_collision(player_mask, player_rect, trident_mask, trident_rect):
                trident_found = True

            # Check for a collision with poseidon if he is brought the trident.
            if trident_found and pixel_collision(player_mask, player_rect, poseidon_mask, poseidon_rect):
                return True

            # See if we touch the maze walls
            if pixel_collision(player_mask, player_rect, level_3_map_mask, level_3_map_rect):
                return False

            # See if we touch the sword
            if pixel_collision(player_mask, player_rect, sword_mask, sword_rect):
                sword_not_found = False

            # See if we touch the fish
            if sword_not_found:
                if pixel_collision(player_mask, player_rect, fish_mask, fish_rect):
                    return False
            else:
                if pixel_collision(player_mask, player_rect, fish_mask, fish_rect):
                    fish_locked = False

            # If the trident is found, it follows the player
            if trident_found:
                pos = pygame.mouse.get_pos()
                trident_rect.center = pos

            # Seaweed movement

            # Check if it needs to change direction
            if poseidon_guard_rect.left < 244 or poseidon_guard_rect.right > 705:
                poseidon_guard_direction *= -1  # Reverse direction

            # Check if it needs to change direction
            if poseidon_guard_2_rect.y < 154 or poseidon_guard_2_rect.y > 240:
                poseidon_guard_2_direction *= -1  # Reverse direction

            poseidon_guard_rect.centerx += poseidon_guard_direction * poseidon_guard_speed
            poseidon_guard_2_rect.centery += poseidon_guard_2_direction * poseidon_guard_2_speed

        # Do updates above and drawing below.

        # Draw the background
        screen.fill((150, 150, 150))  # This helps check if the image path is transparent
        screen.blit(background_3, background_3_rect)
        screen.blit(level_3_map, level_3_map_rect)

        # Draw the start button only if it hasn't been clicked
        if not started:
            screen.blit(start_button, start_button_rect)

        # Draw poseidon and the trident
        screen.blit(poseidon, poseidon_rect)
        screen.blit(trident, trident_rect)

        # Draw the player character
        screen.blit(player, player_rect)

        # Draw the poseidon_guard
        screen.blit(poseidon_guard, poseidon_guard_rect)
        screen.blit(poseidon_guard_2, poseidon_guard_2_rect)

        # Draw the fish
        if fish_locked:
            screen.blit(fish, fish_rect)

        # Draw the sword
        if sword_not_found:
            screen.blit(sword, sword_rect)

        # Write some text to the screen. You can do something like this to show some hints or whatever you want.
        label = message_font.render("Find the sword to get past the fish!",
                                        True, (0, 0, 0))
        screen.blit(label, (20, 20))

        # Every time through the loop, increase the frame count.
        frame_count += 1

        # Bring drawn changes to the front
        pygame.display.update()

        # This tries to force the loop to run at 60 fps
        clock.tick(60)


