from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/")
def home():
    return "API is running. POST /api/generate", 200

@app.post("/api/generate")
def generate():
    data = request.get_json(force=True)

    prompt = data.get("prompt", "")
    sketch = data.get("sketch", "")

    dummy_image_url = "https://placehold.co/512x512?text=Generated+Image"

    return jsonify({
        "ok": True,
        "received_prompt": prompt,
        "received_sketch_prefix": sketch[:50],
        "image_url": dummy_image_url
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
