from tensorflow.keras.models import Model
from tensorflow.keras.layers import (
    Input, Dense, Dropout,
    LayerNormalization, MultiHeadAttention,
    Add, Flatten
)

def transformer_block(x, head_size, num_heads, ff_dim, dropout):
    attn = MultiHeadAttention(num_heads=num_heads, key_dim=head_size)(x, x)
    attn = Dropout(dropout)(attn)
    x = Add()([x, attn])
    x = LayerNormalization()(x)

    ff = Dense(ff_dim, activation="relu")(x)
    ff = Dense(x.shape[-1])(ff)
    ff = Dropout(dropout)(ff)

    x = Add()([x, ff])
    return LayerNormalization()(x)

def build_transformer(input_shape):
    inputs = Input(shape=input_shape)
    x = inputs

    for _ in range(2):
        x = transformer_block(x, 32, 4, 128, 0.3)

    x = Flatten()(x)
    x = Dense(128, activation="relu")(x)
    x = Dropout(0.4)(x)
    outputs = Dense(1, activation="sigmoid")(x)

    model = Model(inputs, outputs)

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model
