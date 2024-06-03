# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 02:11:31 2024

@author: Owner
"""

import tensorflow as tf
from efficientdet import EfficientDet

def evaluate():
    model = tf.keras.models.load_model('models/efficientdet_trained_model')

    # Load validation dataset
    val_dataset = ...

    # Evaluate the model
    results = model.evaluate(val_dataset)
    print(f'Evaluation results: {results}')

if __name__ == '__main__':
    evaluate()
