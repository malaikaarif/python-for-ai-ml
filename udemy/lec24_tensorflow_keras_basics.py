# ============================================================
# Lecture 24: Deep Learning Introduction
# Basics of TensorFlow and Keras
# Building a Neural Network to classify handwritten digits (MNIST)
# ============================================================

import tensorflow as tf
from tensorflow import keras

# ── STEP 1: BUILD THE MODEL ──────────────────────────────────
# Sequential = layers stacked one after another
# Dense = fully connected layer (every neuron connects to next)
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(784,)),
    # 784 = 28x28 pixels flattened, relu removes negative values

    keras.layers.Dense(32, activation='relu'),
    # hidden layer: extracts deeper patterns

    keras.layers.Dense(10, activation='softmax')
    # output layer: 10 neurons = 10 digit classes (0-9)
    # softmax converts to probabilities that sum to 1
])

model.summary()  # prints layer shapes and parameter count

# ── STEP 2: COMPILE THE MODEL ────────────────────────────────
# optimizer = how model updates weights (adam is most popular)
# loss = how model measures its error
# metrics = what we monitor during training
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# ── STEP 3: LOAD DATASET ─────────────────────────────────────
# MNIST: 70,000 handwritten digit images (28x28 pixels)
# 60,000 for training, 10,000 for testing
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# ── STEP 4: NORMALIZE DATA ───────────────────────────────────
# Pixel values 0-255 → 0-1 (helps model learn faster)
x_train, x_test = x_train / 255.0, x_test / 255.0

# ── STEP 5: TRAIN THE MODEL ──────────────────────────────────
# epochs=5 means model sees entire dataset 5 times
model.fit(x_train, y_train, epochs=5)