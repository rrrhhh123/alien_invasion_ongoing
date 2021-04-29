# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
from pygame.sprite import Group
import sys
from setting import Settings
from ship import Ship
import game_functions as qf


def run_game():
    """ Start the game and pop up a window for the game"""
    pygame.init()
    ai_settings = Settings()    
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    #create a ship
    ship = Ship(ai_settings, screen)
    
    #create the bullet for grouping
    bullets = Group()
    
    #开始循环
    while True:
        qf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        
        # delete disappearing bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        
        qf.update_screen(ai_settings,screen,ship, bullets)

run_game()
