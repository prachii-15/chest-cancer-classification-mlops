import tensorflow as tf
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from src.chest_cancer.entity.config_entity import ModelTrainerConfig
from sklearn.utils.class_weight import compute_class_weight

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self, train_ds, val_ds, test_ds):
        if self.config.base_model == "ResNet50":
            base_model = tf.keras.applications.ResNet50(
                weights="imagenet",
                include_top=False,
                input_shape=tuple(self.config.params_image_size)
            )

        for layer in base_model.layers[:-10]:
            layer.trainable = False
        for layer in base_model.layers[-10:]:
            layer.trainable = True

        x = tf.keras.layers.GlobalAveragePooling2D()(base_model.output)
        x = tf.keras.layers.Dense(128, activation="relu")(x)
        x = tf.keras.layers.Dropout(0.5)(x)
        output = tf.keras.layers.Dense(4, activation="softmax")(x)

        model = tf.keras.Model(inputs=base_model.input, outputs=output)
        loss = tf.keras.losses.CategoricalFocalCrossentropy(gamma=2.0)

        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.00005),
            loss=loss,
            metrics=["accuracy"]
        )

        y_train = np.concatenate([y for x, y in train_ds], axis=0)
        y_train = np.argmax(y_train, axis=1)

        # 🔥 Compute weights
        class_weights = compute_class_weight(
            class_weight="balanced",
            classes=np.unique(y_train),
            y=y_train
        )

        class_weights = dict(enumerate(class_weights))

        # 🔥 Manual boost (IMPORTANT)
        class_weights[1] = class_weights[1] * 2.0   # less aggressive
        class_weights[0] = class_weights[0] * 1.2
        class_weights[3] = class_weights[3] * 1.2

        print("Class Weights:", class_weights)

        early_stop = tf.keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=5,
            restore_best_weights=True
        )

        model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=self.config.params_epochs,
            callbacks=[early_stop],
            class_weight=class_weights
        )

        test_loss, test_acc = model.evaluate(test_ds)
        print("/nTest Accuracy: ", test_acc)
        
        y_pred = model.predict(test_ds)
        y_pred = np.argmax(y_pred, axis=1)

        y_true = np.concatenate([y for x, y in test_ds], axis=0)
        y_true = np.argmax(y_true, axis=1)

        print("\n Confusion Matrix: ")
        cm = confusion_matrix(y_true, y_pred)

        print("\n Classification Report: ")
        report = classification_report(y_true, y_pred, zero_division=0)
        print(report)

        with open("metrics.txt", "w") as f:
            f.write("Test Accuracy: "+ str(test_acc) + "\n\n")
            f.write("Confusion Metrix\n: "+ str(cm) + "\n\n")
            f.write("Classification Report: "+ report)

        print("\n Metrics saved in metrics.txt")

        model.save(self.config.trained_model_path, save_format="h5")
        print("\n Model saved at: ", self.config.trained_model_path)