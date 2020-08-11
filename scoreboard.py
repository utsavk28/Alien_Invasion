import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    """A Class to report the scoring information"""

    def __init__(self, screen, ai_settings, stats):
        # Initialize Score attribute
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for score information
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)

        # Prepare te initial Score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 30

    def prep_high_score(self):
        """Turn the high score in render image"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self) :
        lvl = f"Lv : {self.stats.level}"
        self.level_image = self.font.render(lvl,True,self.text_color,self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right
        self.level_rect.top = self.screen_rect.top

    def prep_ships(self):
        self.ships = Group()
        for i in range(self.stats.ship_left) :
            ship = Ship(self.screen, self.ai_settings)
            ship.rect.x = 10 + i*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)