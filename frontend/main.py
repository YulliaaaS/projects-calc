from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL нашого Backend-сервісу (поки що на localhost)
#BACKEND_URL = "http://127.0.0.1:5001/add"

import os
#BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:5001/add") #це не було підключено
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:5001/add") #це працювало
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['GET'])
def calculate():
    # Беремо числа з запиту або ставимо 10 і 20 за замовчуванням
    a = int(request.args.get('a', 10))
    b = int(request.args.get('b', 20))

    # Спілкування по API: Frontend робить POST-запит на Backend!
    try:
        response = requests.post(BACKEND_URL, json={"a": a, "b": b})
        backend_data = response.json()
        return jsonify({
            "frontend_status": "Запит успішно відправлено на Backend!",
            "received_from_backend": backend_data
        })
    except Exception as e:
        return jsonify({"error": f"Не вдалося зв'язатися з Backend: {str(e)}"}), 500

if __name__ == '__main__':
    # Запускається на порту 5000
    app.run(host='0.0.0.0', port=5000)



