# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 02:11:35 2024

@author: Owner
"""

import os
import cv2
import numpy as np

def resize_and_normalize(image_dir, output_dir, target_size=(512, 512)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for image_name in os.listdir(image_dir):
        img_path = os.path.join(image_dir, image_name)
        img = cv2.imread(img_path)
        img_resized = cv2.resize(img, target_size)
        img_normalized = img_resized / 255.0
        output_path = os.path.join(output_dir, image_name)
        cv2.imwrite(output_path, img_normalized * 255)


resize_and_normalize('data/COCO/train2017', 'data/processed/train2017')
