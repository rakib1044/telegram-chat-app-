from flask import Flask, request, render_template, jsonify
import requests, os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    msg = data.get('message', '')
    if not msg:
        return jsonify({'message': 'Message is required'}), 400

    res = requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                        data={'chat_id': CHAT_ID, 'text': msg})
    if res.ok:
        return jsonify({'message': '✅ Sent!'})
    else:
        return jsonify({'message': '❌ Failed'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
