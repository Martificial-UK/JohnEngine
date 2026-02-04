from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run():
    # Example: run a product or engine function
    data = request.json
    return jsonify({"status": "ok", "received": data})

if __name__ == "__main__":
    app.run(port=5000)
