import pygame


class ScrapCount:
    def draw(self, screen, scraps):
        font = pygame.font.SysFont("Mono", 18)
        ren = font.render(f"scraps: {scraps}", 0, "white", "black")
        screen.blit(ren, (10, 10))

class EnergyCount:
    def draw(self, screen, energy_value):
        font = pygame.font.SysFont("Mono", 18)
        ren = font.render(f"energy: {energy_value}", 0, "white", "black")
        screen.blit(ren, (10, 50))
