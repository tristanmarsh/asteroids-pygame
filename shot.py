from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, LINE_WIDTH, PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, x: int, y: int, rotation: float, velocity: int):
        super().__init__(x, y, SHOT_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = rotation
        self.velocity = velocity

    def update(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_vector_with_speed = rotated_vector * PLAYER_SHOOT_SPEED * dt
        self.position += rotated_vector_with_speed

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
