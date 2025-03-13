import os
import httpx
from flask import Flask, render_template, jsonify

# Initialize the Flask application.
app = Flask("voice_app")

# Serve the HTML page at the root route.
@app.route("/")
def index():
    try:
        return render_template("ui.html")
    except Exception as e:
        return "ui.html not found", 404

# The /session endpoint
@app.route("/session", methods=["GET"])
def session_endpoint():
    openai_api_key = ""

    # openai_api_key = os.environ.get("OPENAI_API_KEY")
    # if not openai_api_key:
    #     return jsonify({"error": "OPENAI_API_KEY not set"}), 500

    # Make a synchronous POST request to the OpenAI realtime sessions endpoint
    with httpx.Client() as client:
        r = client.post(
            "https://api.openai.com/v1/realtime/sessions",
            headers={
                "Authorization": f"Bearer {openai_api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-4o-mini-realtime-preview",
                "voice": "verse",
            },
        )
        data = r.json()
        print(data)
        return jsonify(data)

if __name__ == "__main__":
    # Run the Flask app on port 8116
    app.run(host="0.0.0.0", port=8116, debug=True)

# chmod +x chrome_local.sh
# ./chrome_local.sh
