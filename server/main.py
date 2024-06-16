from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import random
import time

app = FastAPI()

origins = [
    "http://localhost:5173",  # Vue.js dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

svg_images = [
    {
        "id": 1,
        "svg": """
        <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
            <rect x="10" y="10" width="20" height="20" style="fill:rgb(255,0,0);" />
            <rect x="40" y="10" width="20" height="20" style="fill:rgb(0,255,0);" />
            <rect x="70" y="10" width="20" height="20" style="fill:rgb(0,0,255);" />
            <rect x="10" y="40" width="20" height="20" style="fill:rgb(255,255,0);" />
            <rect x="40" y="40" width="20" height="20" style="fill:rgb(0,255,255);" />
        </svg>
        """,
        "tags": ["colorful", "squares"]
    },
    {
        "id": 2,
        "svg": """
        <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
            <rect x="20" y="20" width="15" height="15" style="fill:rgb(255,0,255);" />
            <rect x="50" y="20" width="15" height="15" style="fill:rgb(128,0,128);" />
            <rect x="80" y="20" width="15" height="15" style="fill:rgb(255,165,0);" />
            <rect x="20" y="50" width="15" height="15" style="fill:rgb(75,0,130);" />
            <rect x="50" y="50" width="15" height="15" style="fill:rgb(0,128,128);" />
        </svg>
        """,
        "tags": ["small", "rectangles"]
    },
    {
        "id": 3,
        "svg": """
        <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
            <rect x="15" y="15" width="10" height="10" style="fill:rgb(173,216,230);" />
            <rect x="35" y="15" width="10" height="10" style="fill:rgb(255,20,147);" />
            <rect x="55" y="15" width="10" height="10" style="fill:rgb(60,179,113);" />
            <rect x="75" y="15" width="10" height="10" style="fill:rgb(255,105,180);" />
            <rect x="15" y="35" width="10" height="10" style="fill:rgb(124,252,0);" />
        </svg>
        """,
        "tags": ["tiny", "squares"]
    },
    {
        "id": 4,
        "svg": """
        <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
            <rect x="10" y="10" width="10" height="10" style="fill:rgb(255,69,0);" />
            <rect x="30" y="10" width="10" height="10" style="fill:rgb(50,205,50);" />
            <rect x="50" y="10" width="10" height="10" style="fill:rgb(0,191,255);" />
            <rect x="70" y="10" width="10" height="10" style="fill:rgb(255,140,0);" />
            <rect x="90" y="10" width="10" height="10" style="fill:rgb(238,130,238);" />
        </svg>
        """,
        "tags": ["tiny", "rectangles"]
    },
    {
        "id": 5,
        "svg": """
        <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
            <rect x="5" y="5" width="20" height="20" style="fill:rgb(220,20,60);" />
            <rect x="30" y="5" width="20" height="20" style="fill:rgb(0,255,127);" />
            <rect x="55" y="5" width="20" height="20" style="fill:rgb(70,130,180);" />
            <rect x="80" y="5" width="20" height="20" style="fill:rgb(255,0,255);" />
            <rect x="5" y="30" width="20" height="20" style="fill:rgb(255,215,0);" />
        </svg>
        """,
        "tags": ["medium", "squares"]
    }
]


@app.get("/images")
async def get_images():
    return JSONResponse(content=svg_images)


@app.get("/images/{image_id}")
async def get_image(image_id: int):
    # Simulate a delay
    time.sleep(random.uniform(0.5, 5.0))  # Delay between 0.5 and 2.0 seconds
    
    # Randomly decide to fail
    if random.random() < 0.2:  # 20% chance of failure
        raise HTTPException(status_code=500, detail="Internal server error")
    
    # Find the image by ID
    for image in svg_images:
        if image["id"] == image_id:
            return JSONResponse(content=image)
    
    raise HTTPException(status_code=404, detail="Image not found")
