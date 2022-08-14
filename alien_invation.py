import pygame
from settings import Settings
from bullet import Bullet
import sys
from ship import Ship

class AlienInvation:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('here is my first game')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def rungame(self):
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullet()
            self._updating_screen()



    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
               
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
                

    def _check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self.fire_bullet()

    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right =  False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def fire_bullet(self):
        if len(self.bullets) < self.settings.allowed_bullet:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)


    def _updating_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    AI = AlienInvation()
    AI.rungame()