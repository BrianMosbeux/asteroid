import pygame
from circleshape import CircleShape 
from constants import DRAG_COEFICIENT, PLAYER_ACCELERATION, PLAYER_RADIUS, LINE_WIDTH, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED, PLAYER_TURN_SPEED
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        self.speed = 0
        self.scraps = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(surface=screen, color="white", points=self.triangle(), width=LINE_WIDTH)

    def rotate(self, dt:float):
        self.rotation += PLAYER_TURN_SPEED * dt
        return self.rotation
    
    def update(self, dt: float) -> None:
        self.cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.speed += PLAYER_ACCELERATION
        if keys[pygame.K_s]:
            self.speed -= PLAYER_ACCELERATION
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.move(dt)
        self.speed *= DRAG_COEFICIENT


    def move(self, dt:float):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_vector_with_speed = rotated_vector * self.speed * dt
        self.position += rotated_vector_with_speed

    def shoot(self):
        if self.cooldown > 0:
            return 
        self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED 





