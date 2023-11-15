"""
Simulates a traffic light using a
Finite State Machine

@author: Ms. Namasivayam
@version: 2023
"""

from fsm import FSM
import pygame
import time
import sys

class TrafficLight:
    # States
    RED, GREEN, YELLOW = "r", "g", "y"

    # Inputs
    TIMER_UP = "tu"

    # Constants
    WIDTH, HEIGHT = 300, 600
    LIGHT_RADIUS = 50
    BLACK = "b"
    COLORS = {RED: (255, 0, 0), GREEN: (0, 255, 0), YELLOW: (255, 255, 0), BLACK: (0, 0, 0)}

    def __init__(self):
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Traffic Light")

        # Initialize FSM
        self.fsm = FSM(self.RED)
        self.init_fsm()
        self.timer_duration = 2

        # Start on Red
        self.turn_red()
        pygame.display.flip()

    def init_fsm(self):
        """
        Adds all states to the FSM
        """
        self.fsm.add_transition(self.TIMER_UP, self.RED, self.turn_green, self.GREEN)
        self.fsm.add_transition(self.TIMER_UP, self.GREEN, self.turn_yellow, self.YELLOW)
        self.fsm.add_transition(self.TIMER_UP, self.YELLOW, self.turn_red, self.RED)

    def turn_green(self):
        self.draw_traffic_light()
        pygame.draw.circle(self.screen, self.COLORS[self.GREEN], (self.WIDTH // 2, 500), self.LIGHT_RADIUS)
        self.timer_duration = 5


    def turn_red(self):
        self.draw_traffic_light()
        pygame.draw.circle(self.screen, self.COLORS[self.RED], (self.WIDTH // 2, 100), self.LIGHT_RADIUS)
        self.timer_duration = 5

    def turn_yellow(self):
        self.draw_traffic_light()
        pygame.draw.circle(self.screen, self.COLORS[self.YELLOW], (self.WIDTH // 2, 300), self.LIGHT_RADIUS)
        self.timer_duration = 2

    def draw_traffic_light(self):
        self.screen.fill((120, 120, 120))
        pygame.draw.circle(self.screen, self.COLORS[self.RED], (self.WIDTH // 2, 100), self.LIGHT_RADIUS, width=2)
        pygame.draw.circle(self.screen, self.COLORS[self.YELLOW], (self.WIDTH // 2, 300), self.LIGHT_RADIUS, width=2)
        pygame.draw.circle(self.screen, self.COLORS[self.GREEN], (self.WIDTH // 2, 500), self.LIGHT_RADIUS, width=2)

    def run(self):
        start_time = time.time()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            elapsed_time = time.time() - start_time
            print(elapsed_time)
            if elapsed_time > self.timer_duration:
                self.fsm.process(self.TIMER_UP)
                start_time = time.time()
                pygame.display.flip()

            time.sleep(0.5)


if __name__ == "__main__":
    tl = TrafficLight()
    tl.run()
