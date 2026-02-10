from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, Flatten, Dense

def build_cnn(input_shape):
    model = Sequential([
        Conv1D(32, 3, activation="relu", input_shape=input_shape),
        Flatten(),
        Dense(1, activation="sigmoid")
    ])
    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )
    return model
