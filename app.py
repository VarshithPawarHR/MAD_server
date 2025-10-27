from flask import Flask, send_file, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Code download API is live."

@app.route('/download', methods=['GET'])
def download_txt():
    return send_file('code.txt', as_attachment=True)


@app.route('/keep-alive', methods=['GET', 'POST'])
def keep_alive():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        return jsonify({
            "status": "alive",
            "method": "POST",
            "received": data or {}
        })
    else:
        return jsonify({
            "status": "alive",
            "method": "GET"
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
