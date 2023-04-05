#!/usr/bin/env python3

from flask import Flask
from flask import jsonify

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'{param}'

@app.route('/count/<int:num>')
def count(num):
    nums = [i for i in range(num)]
    items = '\n'.join(map(str, nums))
    return items + '\n'
 
@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        raise Exception('Invalid operation.')