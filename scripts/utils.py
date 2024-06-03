# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 02:14:51 2024

@author: Owner
"""

import os
import cv2

def load_image(image_path):
    return cv2.imread(image_path)

def preprocess_image(image, target_size):
    image_resized = cv2.resize(image, target_size)
    image_normalized = image_resized / 255.0
    return image_normalized
