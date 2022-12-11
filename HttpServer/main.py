# This is a sample Python script.
import math

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request, jsonify, json
import requests

server = Flask(__name__)


@server.route("/independent/calculate", methods=['POST'])
def independent_operation():
    content = request.get_json()
    operation = content['operation']
    args = content['arguments']
    operation = operation.lower()
    if operation == 'plus':
        if len(args) == 2:
            res = int(args[0] + args[1])
        elif len(args) > 2:
            res = "Error: Too many arguments to perform the operation " + operation
        else:
            res = "Error: Not enough arguments to perform the operation " + operation
    elif operation == 'minus':
        if len(args) == 2:
            res = int(args[0] - args[1])
        elif len(args) > 2:
            res = "Error: Too many arguments to perform the operation " + operation
        else:
            res = "Error: Not enough arguments to perform the operation " + operation
    elif operation == 'times':
        if len(args) == 2:
            res = int(args[0] * args[1])
        elif len(args) > 2:
            res = "Error: Too many arguments to perform the operation " + operation
        else:
            res = "Error: Not enough arguments to perform the operation " + operation
    elif operation == 'divide':
        if len(args) == 2:
            res = int(args[0] / args[1])
        elif len(args) > 2:
            res = "Error: Too many arguments to perform the operation " + operation
        else:
            res = "Error: Not enough arguments to perform the operation " + operation
    elif operation == 'pow':
        if len(args) == 2:
            res = int(math.pow(args[0], args[1]))
        elif len(args) > 2:
            res = "Error: Too many arguments to perform the operation " + operation
        else:
            res = "Error: Not enough arguments to perform the operation " + operation
    elif operation == 'abs':
        if len(args) == 1:
            res = int(math.abs(args[0]))
        elif len(args) > 1:
            res = "Error: Too many arguments to perform the operation " + operation
        else:
            res = "Error: Not enough arguments to perform the operation " + operation
    elif operation == 'fact':
        if len(args) == 1:
            res = int(math.factorial(args[0]))
        elif len(args) > 1:
            res = "Error: Too many arguments to perform the operation " + operation
        else:
            res = "Error: Not enough arguments to perform the operation " + operation
    else:
        res = "Error: unknown operation: " + operation
    return jsonify({"result": res})


if __name__ == '__main__':
    server.run(host="localhost", port=8496, debug =True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
