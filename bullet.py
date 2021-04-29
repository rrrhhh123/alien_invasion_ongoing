# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 17:00:50 2021

@author: Ruru Dai
"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class that manage the bullet"""
    
    def __init__(self, ai_settings, screen, ship):
        """create a bullet object at the ship location"""
        super().__init__()
        self.screen = screen
    
        # create the rec of the bullet at (0,0), and then set the correct direction
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
        
    def draw_bullet(self):
        """draw the bullet"""
        pygame.draw.rect(self.screen,self.color,self.rect)
        