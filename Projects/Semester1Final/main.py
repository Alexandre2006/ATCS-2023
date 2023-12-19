import pygame
from scenes.kitchen import *
from scenes.store import *

kitchen = Kitchen()
store = Store()

pygame.init()

while True:

    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Handle events
    if globals.current_scene == "kitchen":
        kitchen.handle_events(events)
        kitchen.render()
    elif globals.current_scene == "store":
        store.handle_events(events)
        store.render()
    
    # Check customer status
    if globals.customer != None and globals.customer.customer_fsm.current_state == "fail":
        pygame.quit()
        print("You failed to serve a customer! Your final score is: $" + str(globals.money))
        quit()

    pygame.display.flip()
    pygame.time.Clock().tick(60)