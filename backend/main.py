from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    num1 = data.get('a', 0)
    num2 = data.get('b', 0)
    result = num1 + num2
    return jsonify({"result": result, "message": "Слова з backend: Здорова, я все порахував!"})

if __name__ == '__main__':
    # Запускається на порту 5001
    app.run(host='0.0.0.0', port=5001)