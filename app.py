from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "ok , thenga aaan , neech podoo", "message": "poda kalla thendii , ninakkokke valla kazhivumundodaa kalla kazhuverii!"})

@app.route("/health")
def health():
    return jsonify({"healthy": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)