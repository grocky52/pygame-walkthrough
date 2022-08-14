import pygame

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 1000
        self.bg_color = (230,230,230)
        self.ship_speed = 2.5
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (60,60,60)
        self.bullet_speed = 2.0
        self.allowed_bullet = 5