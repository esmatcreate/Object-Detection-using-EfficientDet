# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 02:11:32 2024

@author: Owner
"""

import tensorflow as tf
from efficientdet import EfficientDet
from config import Config

def train():
    config = Config()
    model = EfficientDet(config)
    model.compile(optimizer=tf.keras.optimizers.Adam(), loss='categorical_crossentropy')

    # Load dataset
    train_dataset = ...
    val_dataset = ...

    # Train the model
    model.fit(train_dataset, validation_data=val_dataset, epochs=config.epochs)

    # Save the trained model
    model.save('models/efficientdet_trained_model')

if __name__ == '__main__':
    train()
