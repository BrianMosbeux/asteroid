import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SCRAP_RADIUS


class Scrap(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SCRAP_RADIUS)
        self.value = 1
        self.cooldown = 5

    def draw(self, screen):
        pygame.draw.rect(surface=screen, color="white", rect=pygame.Rect(self.position.x-self.radius, self.position.y-self.radius, self.radius*2, self.radius*2), width=LINE_WIDTH)

    def update(self, dt):
        self.cooldown -= dt
        if self.cooldown > 0:
            return
        self.kill()


