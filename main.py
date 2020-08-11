import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize the game and creates screen objects
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(screen, ai_settings,"PLAY")
    # Make a ship
    ship = Ship(screen, ai_settings)

    # Make a group to store the bullets
    stats = Gamestats(ai_settings)
    sb = Scoreboard(screen,ai_settings,stats)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)
    while True:
        gf.check_events(ship, screen, ai_settings, bullets, play_button, stats,aliens,sb)
        if stats.game_active :
            ship.update()
            gf.update_bullet(bullets, aliens, ai_settings, screen, ship,stats,sb)
            gf.update_aliens(ai_settings, stats, aliens, ship, screen, bullets,sb)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats,sb)


run_game()
