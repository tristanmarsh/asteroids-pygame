from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(20, 20, 20)
        # self.__velocity

    def draw(self, screen: pygame.surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position * self.velocity * dt
