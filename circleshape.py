import pygame
from constants import LINE_WIDTH

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Override in Class Asteroid
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def update(self, dt):
        # Override in Asteroid
        pass

    def collides_with(self, other):
        #Finding if the Circles collide by seeing if the distance betweem their center point is equal to or less than the sum of their radius
        if pygame.math.Vector2.distance_to(self.position, other.position) <= self.radius + other.radius:
            return True
        return False