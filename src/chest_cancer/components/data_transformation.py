import tensorflow as tf
import os

class DataTransformation:
    def __init__(self, config):
        self.config = config

    def get_dataset(self):
        preprocess = tf.keras.applications.resnet50.preprocess_input

        train_dir = os.path.join(self.config.data_dir, "train")
        valid_dir = os.path.join(self.config.data_dir, "valid")
        test_dir = os.path.join(self.config.data_dir, "test")

        data_augmentation = tf.keras.Sequential([
            tf.keras.layers.RandomFlip("horizontal"),
            tf.keras.layers.RandomRotation(0.1),
            tf.keras.layers.RandomZoom(0.1),
        ])

        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            train_dir, 
            image_size = tuple(self.config.image_size),
            batch_size = self.config.batch_size,
            label_mode = "categorical",
            shuffle = True
        )

        valid_ds = tf.keras.preprocessing.image_dataset_from_directory(
            valid_dir, 
            image_size = tuple(self.config.image_size),
            batch_size = self.config.batch_size,
            label_mode = "categorical",
            shuffle=False
        )

        test_ds = tf.keras.preprocessing.image_dataset_from_directory(
            test_dir, 
            image_size = tuple(self.config.image_size),
            batch_size = self.config.batch_size,
            label_mode = "categorical",
            shuffle=False
        )

        train_ds = train_ds.map(lambda x,y:(preprocess(data_augmentation(x)),y))
        valid_ds = valid_ds.map(lambda x,y:(preprocess(x),y))
        test_ds = test_ds.map(lambda x,y:(preprocess(x),y))

        AUTOTUNE = tf.data.AUTOTUNE

        train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
        valid_ds = valid_ds.cache().prefetch(buffer_size=AUTOTUNE)
        test_ds = test_ds.cache().prefetch(buffer_size=AUTOTUNE)

        return train_ds, valid_ds, test_ds