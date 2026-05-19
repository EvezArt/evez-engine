#!/bin/bash
# BROKE BOI $0 OPENCLAW DEPLOYMENT
# Uses OLLAMA (free local LLM), reverse-engineered proxies, free tiers

mkdir -p /opt/brokeboi

# 1. LOCAL LLM via OLLAMA
curl -fsSL https://ollama.com/install.sh | sh
ollama pull tinyllama  # 1.1GB RAM friendly

# 2. FREE PROXY WRAPPER
cat > /opt/brokeboi/server.py << 'PY'
from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

@app.route("/v1/chat/completions", methods=["POST"])
def chat():
    payload = request.json
    payload["model"] = "tinyllama"
    r = requests.post("http://localhost:11434/v1/chat/completions", json=payload)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
PY

# 3. RUN OPENCLAW WITH LOCAL LLM
openclaw gateway start --config '{
  "model": {
    "base_url": "http://localhost:8080/v1",
    "api_key": "fake-key-for-local"
  }
}'

echo "BROKE BOI DEPLOYED - $0 cost"