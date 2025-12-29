from circleshape import CircleShape
import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        spread = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS
        a = Asteroid(self.position.x, self.position.y, radius)
        b = Asteroid(self.position.x, self.position.y, radius)
        a.velocity = self.velocity.rotate(-spread) * 1.2
        b.velocity = self.velocity.rotate(spread) * 1.2
