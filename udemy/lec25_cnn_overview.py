# ============================================================
# Lecture 25: Convolutional Neural Networks (CNNs)
# CNNs extract spatial features from images using filters
# Example: Handwritten digit classification using MNIST
# ============================================================

import tensorflow as tf
from tensorflow.keras import layers, models

# ── STEP 1: LOAD AND PREPROCESS DATASET ──────────────────────
# MNIST: 70,000 handwritten digit images (28x28 pixels)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Reshape: add channel dimension (1 = grayscale)
# CNN expects shape (samples, height, width, channels)
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0  # normalize 0-1
x_test  = x_test.reshape(-1, 28, 28, 1)  / 255.0

# ── STEP 2: BUILD THE CNN MODEL ──────────────────────────────
model = models.Sequential([

    # Conv2D: applies 32 filters (3x3) to detect edges/patterns
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),

    # MaxPooling: reduces size by taking max value in 2x2 window
    # reduces computation, keeps important features
    layers.MaxPooling2D((2, 2)),

    # Flatten: converts 2D feature maps → 1D vector
    layers.Flatten(),

    # Dense: fully connected layer for high-level reasoning
    layers.Dense(64, activation='relu'),

    # Output: 10 neurons for 10 digit classes (0-9)
    layers.Dense(10, activation='softmax')
])

# ── STEP 3: COMPILE ──────────────────────────────────────────
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# ── STEP 4: TRAIN ────────────────────────────────────────────
# verbose=2 prints one line per epoch
model.fit(x_train, y_train, epochs=5, verbose=2)

# ── STEP 5: EVALUATE ─────────────────────────────────────────
# Test on unseen data to measure real performance
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f'Test accuracy: {test_acc * 100:.2f}%')