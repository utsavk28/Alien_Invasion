import pygame
from pygame.sprite import Sprite
class Alien(Sprite) :
    """A Class to represent the fleet of alien"""
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load image of alien
        self.image = pygame.image.load("alien.bmp")
        self.rect = self.image.get_rect()

        self.x = self.rect.width
        self.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the aliens right left"""
        self.x += self.ai_settings.aliens_speed_factor*self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self) :
        """Return True if the alien is at edges of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right :
            return True
        elif self.rect.left <= 0 :
            return True
