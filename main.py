from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks once (you can hardcode or read from data.json)
with open("data.json") as f:
    marks_data = json.load(f)

@app.get("/api")
async def get_marks(name: list[str] = []):
    return {"marks": [marks_data.get(n, 0) for n in name]}

