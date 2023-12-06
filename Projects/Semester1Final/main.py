import pygame
from scenes.kitchen import *

main_scene = Kitchen()

pygame.init()

while True:
    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Handle events
    main_scene.handle_events(events)

    # Update
    main_scene.update(0)

    # Render
    main_scene.render()

    pygame.display.flip()
    pygame.time.Clock().tick(60)