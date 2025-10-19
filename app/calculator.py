"""
Simple Calculator API using Flask
Provides basic arithmetic operations via REST endpoints
testing git private account
"""

from flask import Flask, jsonify

app = Flask(__name__)


class Calculator:
    """Calculator class with basic arithmetic operations"""
    
    @staticmethod
    def add(a, b):
        """Add two numbers"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Subtract b from a"""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers"""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    @staticmethod
    def power(base, exponent):
        """Raise base to the power of exponent"""
        return base ** exponent
    


# Initialize calculator instance
calc = Calculator()


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'calculator-api',
        'version': '1.0.0'
    }), 200


@app.route('/add/<a>/<b>', methods=['GET'])
def add(a, b):
    """Addition endpoint"""
    try:
        a, b = float(a), float(b)
        result = calc.add(a, b)
        return jsonify({
            'operation': 'addition',
            'a': a,
            'b': b,
            'result': result
        }), 200
    except ValueError:
        return jsonify({'error': 'Invalid number format'}), 400


@app.route('/subtract/<a>/<b>', methods=['GET'])
def subtract(a, b):
    """Subtraction endpoint"""
    try:
        a, b = float(a), float(b)
        result = calc.subtract(a, b)
        return jsonify({
            'operation': 'subtraction',
            'a': a,
            'b': b,
            'result': result
        }), 200
    except ValueError:
        return jsonify({'error': 'Invalid number format'}), 400


@app.route('/multiply/<a>/<b>', methods=['GET'])
def multiply(a, b):
    """Multiplication endpoint"""
    try:
        a, b = float(a), float(b)
        result = calc.multiply(a, b)
        return jsonify({
            'operation': 'multiplication',
            'a': a,
            'b': b,
            'result': result
        }), 200
    except ValueError:
        return jsonify({'error': 'Invalid number format'}), 400


@app.route('/divide/<a>/<b>', methods=['GET'])
def divide(a, b):
    """Division endpoint"""
    try:
        a, b = float(a), float(b)
        result = calc.divide(a, b)
        return jsonify({
            'operation': 'division',
            'a': a,
            'b': b,
            'result': result
        }), 200
    except ValueError as e:
        if "Cannot divide by zero" in str(e):
            return jsonify({'error': str(e)}), 400
        return jsonify({'error': 'Invalid number format'}), 400


@app.route('/', methods=['GET'])
def home():
    """Home endpoint with API information"""
    return jsonify({
        'message': 'Calculator API',
        'endpoints': {
            'health': '/health',
            'add': '/add/<a>/<b>',
            'subtract': '/subtract/<a>/<b>',
            'multiply': '/multiply/<a>/<b>',
            'divide': '/divide/<a>/<b>',
            'power': '/power/<base>/<exponent>'
        }
    }), 200

@app.route('/power/<a>/<b>', methods=['GET'])
def power_route(a, b):
    """Power calculation endpoint"""
    try:
        a, b = float(a), float(b)
        result = calc.power(a, b)
        return jsonify({
            'operation': 'power',
            'base': a,
            'exponent': b,
            'result': result
        }), 200
    except ValueError:
        return jsonify({
            'error': 'Invalid number format'
        }), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)