from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

def get_classification_callbacks(model_name):
    return [
        EarlyStopping(
            monitor="val_accuracy",
            patience=8,
            mode="max",
            restore_best_weights=True
        ),
        ModelCheckpoint(
            filepath=f"../models/{model_name}.h5",
            monitor="val_accuracy",
            mode="max",
            save_best_only=True
        )
    ]

def get_autoencoder_callbacks(model_name):
    return [
        EarlyStopping(
            monitor="val_loss",
            patience=8,
            mode="min",
            restore_best_weights=True
        ),
        ModelCheckpoint(
            filepath=f"../models/{model_name}.h5",
            monitor="val_loss",
            mode="min",
            save_best_only=True
        )
    ]
