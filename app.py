import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Human Activity Recognition API is running!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Get PORT from Render, default to 8000
    print(f"Starting server on port {port}")  # Debugging log
    uvicorn.run(app, host="0.0.0.0", port=port)
