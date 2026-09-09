import pygame



class Score:
    def draw(self, screen, scraps):
        font = pygame.font.SysFont("Mono", 18)
        ren = font.render(f"scraps: {scraps}", 0, "white", "black")
        screen.blit(ren, (10, 10))
