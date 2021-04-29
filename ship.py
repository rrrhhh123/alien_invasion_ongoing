# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:19:02 2021

@author: Ruru Dai
"""

import pygame

class Ship():
    
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load('images/bear_head.jpeg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #put the image at the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        #self.rect.bottom = self.screen_rect.bottom
        
        #在飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        #move the ship
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """adjust ship's location according to the event"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
            
        # 根据self.center更新rect对象    
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)