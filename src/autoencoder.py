from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Input
import numpy as np

def build_autoencoder(input_dim):
    inp = Input(shape=(input_dim,))
    x = Dense(128, activation="relu")(inp)
    x = Dense(64, activation="relu")(x)
    latent = Dense(32, activation="relu")(x)

    x = Dense(64, activation="relu")(latent)
    x = Dense(128, activation="relu")(x)
    out = Dense(input_dim, activation="linear")(x)

    model = Model(inp, out)
    model.compile(optimizer="adam", loss="mse")
    return model

def severity_score(autoencoder, X):
    recon = autoencoder.predict(X, verbose=0)
    error = np.mean((X - recon) ** 2)
    return round(error * 100, 2)
