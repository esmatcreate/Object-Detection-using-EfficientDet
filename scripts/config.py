# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 02:14:27 2024

@author: Owner
"""

class Config:
    def __init__(self):
        self.epochs = 50
        self.batch_size = 16
        self.learning_rate = 0.001
        self.input_size = (512, 512)
        self.num_classes = 80
