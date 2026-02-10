from tensorflow.keras.models import Model
from tensorflow.keras.layers import (
    Input, Dense, Flatten,
    LayerNormalization, MultiHeadAttention
)

def build_transformer(input_shape):
    """
    Transformer Encoder for Acoustic Feature Learning
    input_shape = (num_features, 1)
    """

    inputs = Input(shape=input_shape)

    # Self-attention block
    attn_output = MultiHeadAttention(
        num_heads=2,
        key_dim=16
    )(inputs, inputs)

    # Add & Normalize
    x = LayerNormalization()(attn_output)

    # Flatten & classify
    x = Flatten()(x)
    outputs = Dense(1, activation="sigmoid")(x)

    model = Model(inputs, outputs)

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model
