from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Average Calculator Microserver!"

@app.route('/calculate_average', methods=['POST'])
def calculate_average():
    data = request.get_json()
    
    if not data or 'numbers' not in data:
        return jsonify({"error": "Please provide a list of numbers in JSON format under the key 'numbers'"}), 400

    numbers = data['numbers']

    if not all(isinstance(x, (int, float)) for x in numbers):
        return jsonify({"error": "All elements in the list must be numbers"}), 400

    if len(numbers) == 0:
        return jsonify({"error": "The list of numbers must not be empty"}), 400

    average = sum(numbers) / len(numbers)
    
    return jsonify({"average": average})

if __name__ == '__main__':
    app.run(debug=True)
