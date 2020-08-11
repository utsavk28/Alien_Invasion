import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(stats, aliens,event, ship, screen, ai_settings, bullets,sb):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a Bullet and adds it in bullet group
        fire_bullets(bullets, ai_settings, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p :
        button = True
        check_play_button(stats ,aliens,bullets,ai_settings,screen,ship,button,sb)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship, screen, ai_settings, bullets, play_button, stats,aliens,sb):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(stats, aliens,event, ship, screen, ai_settings, bullets,sb)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button = play_button.rect.collidepoint(mouse_x, mouse_y)
            check_play_button(stats,aliens,bullets,ai_settings,screen,ship,button,sb)


def check_play_button(stats ,aliens,bullets,ai_settings,screen,ship,button,sb):
    if button and not stats.game_active :
        stats.reset_stats()
        pygame.mouse.set_visible(False)
        ai_settings.initialize_dynamic_settings()
        stats.game_active = True
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

def update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats,sb):
    # Update images on the screen and flip to the new screen.
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets
    sb.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullet(bullets, aliens, ai_settings, screen, ship,stats,sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check if any bullets have hit an alien
    # if any , get rid of the alien and bullet
    check_bullet_alien_collision(aliens, bullets, ai_settings,stats,sb)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()

def check_bullet_alien_collision(aliens, bullets, ai_settings,stats,sb):
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)
    if collisions :
        for i in collisions.values() :
            stats.score += ai_settings.alien_points
        sb.prep_score()
        check_high_score(stats, sb)


def fire_bullets(bullets, ai_settings, screen, ship):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens, ship):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    n = get_number_alien_x(ai_settings, alien_width)
    m = get_number_rows(ai_settings, alien_height, ship_height)
    for i in range(n):
        for j in range(m):
            create_alien(ai_settings, screen, alien_width, alien_height, aliens, i, j)


def get_number_alien_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, alien_height, ship_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, alien_width, alien_height, aliens, i, j):
    alien = Alien(ai_settings, screen)
    alien.x = alien_width + 2 * i * alien_width
    alien.rect.x = alien.x
    alien.y = alien_height + 1.25 * j * alien_height
    alien.rect.y = alien.y
    aliens.add(alien)

def check_high_score(stats,sb) :
    if stats.score > stats.high_score :
        stats.high_score = stats.score
        sb.prep_high_score()



def update_aliens(ai_settings, stats, aliens, ship, screen, bullets,sb):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    check_aliens_bottom(ai_settings, stats, aliens, ship, screen, bullets,sb)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, aliens, ship, screen, bullets,sb)
        print("Ship hit!!!")


def check_aliens_bottom(ai_settings, stats, aliens, ship, screen, bullets,sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, aliens, ship, screen, bullets,sb)
            break


def ship_hit(ai_settings, stats, aliens, ship, screen, bullets,sb):
    stats.ship_left -= 1
    sb.prep_ships()
    bullets.empty()
    aliens.empty()
    create_fleet(ai_settings, screen, aliens, ship)
    ship.center_ship()
    if stats.ship_left < 0:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    sleep(1)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
