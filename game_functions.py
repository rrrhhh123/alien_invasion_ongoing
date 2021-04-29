# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 19:10:07 2021

@author: Ruru Dai
"""

import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True                
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    elif event.key ==pygame.K_q:
        sys.exit()
         
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False     
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False 
    elif event.key == pygame.K_UP:
        ship.moving_up = False  
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False  
    
    
def check_events(ai_settings, screen, ship, bullets):
    """respone to click and mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
                
                
def update_screen(ai_settings,screen,ship, bullets):
    #repaint the screen everytime it starts
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    
    #show the latest screen
    pygame.display.flip()

