# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:03:22 2021

@author: Ruru Dai
"""

class Settings:
    """save all classes in alien invasion"""
    
    def __init__(self):
        """save initialization settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)
        
        #ship setting
        self.ship_speed_factor = 1.5
        
        #bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 8
        self.bullet_height = 15
        self.bullet_color = 253,185,200
        