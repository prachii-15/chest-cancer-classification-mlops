import tensorflow as tf
import os

class DataTransformation:
    def __init__(self, config):
        self.config = config

    def create_data_generators(self):
        train_dir = os.path.join(self.config.data_dir, "train")
        valid_dir = os.path.join(self.config.data_dir, "valid")
        test_dir = os.path.join(self.config.data_dir, "test")

        train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=1./255
        )

        train_generator = train_datagen.flow_from_directory(
            train_dir,
            target_size=tuple(self.config.image_size),
            batch_size=self.config.batch_size,
            class_mode='categorical'
        )

        valid_generator = train_datagen.flow_from_directory(
            valid_dir,
            target_size=tuple(self.config.image_size),
            batch_size=self.config.batch_size,
            class_mode='categorical'
        )

        test_generator = train_datagen.flow_from_directory(
            test_dir,
            target_size=tuple(self.config.image_size),
            batch_size=self.config.batch_size,
            class_mode='categorical'
        )

        return train_generator, valid_generator, test_generator