import os
import tensorflow as tf

# Get absolute path of the model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "final_model.keras")

# Debugging: Print model path
print(f"Loading model from: {MODEL_PATH}")

# Load the trained model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

model = tf.keras.models.load_model(MODEL_PATH)
