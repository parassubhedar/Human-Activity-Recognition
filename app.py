import os
import uvicorn
import tensorflow as tf
from fastapi import FastAPI, File, UploadFile
import numpy as np
import cv2

app = FastAPI()

# Get absolute path of the model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "final_model.keras")

# Load the trained model
model = tf.keras.models.load_model(MODEL_PATH)

@app.get("/")
def home():
    return {"message": "Human Activity Recognition API is running!"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        file_bytes = np.asarray(bytearray(contents), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        frame = cv2.resize(frame, (160, 160))  # Resize for model input
        frame = np.expand_dims(frame, axis=0)  # Add batch dimension
        frame = frame / 255.0  # Normalize

        predictions = model.predict(frame)
        predicted_class = np.argmax(predictions)

        return {"prediction": int(predicted_class), "confidence": float(np.max(predictions))}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if not set
    uvicorn.run(app, host="0.0.0.0", port=port)
