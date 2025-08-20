# src/tools/image_tool.py
import os
import uuid
from langchain_google_genai import GoogleGenerativeAI

def generate_image(prompt: str, filename_prefix: str = "agent") -> str:
    """Generate an image from a text prompt using Gemini and save it locally."""
    model = GoogleGenerativeAI(model="gemini-2.0-flash", task="image-generation")

    # Ensure output directory exists
    os.makedirs("outputs", exist_ok=True)
    filename = f"outputs/{filename_prefix}_{uuid.uuid4().hex[:8]}.png"

    # Call Gemini to generate an image (adjust if API returns base64 instead of bytes)
    result = model.generate(prompt=prompt)

    # Save result — placeholder (depends on API’s return type!)
    with open(filename, "wb") as f:
        f.write(result)

    return filename
