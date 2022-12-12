# This is a sample Python script.
import math

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request, jsonify, json
from collections import deque
import requests

server = Flask(__name__)
stack = deque()


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
            return jsonify({"error-message": "Error: Too many arguments to perform the operation " + operation}), 409
        else:
            return jsonify({"error-message": "Error: Not enough arguments to perform the operation " + operation}), 409
    elif operation == 'minus':
        if len(args) == 2:
            res = int(args[0] - args[1])
        elif len(args) > 2:
            return jsonify({"error-message": "Error: Too many arguments to perform the operation " + operation}), 409
        else:
            return jsonify({"error-message": "Error: Not enough arguments to perform the operation " + operation}), 409
    elif operation == 'times':
        if len(args) == 2:
            res = int(args[0] * args[1])
        elif len(args) > 2:
            return jsonify({"error-message": "Error: Too many arguments to perform the operation " + operation}), 409
        else:
            return jsonify({"error-message": "Error: Not enough arguments to perform the operation " + operation}), 409
    elif operation == 'divide':
        if len(args) == 2:
            if args[1] == 0:
                return jsonify({"error-message": "Error while performing operation Divide: division by 0"}), 409
            res = int(args[0] / args[1])
        elif len(args) > 2:
            return jsonify({"error-message": "Error: Too many arguments to perform the operation " + operation}), 409
        else:
            return jsonify({"error-message": "Error: Not enough arguments to perform the operation " + operation}), 409
    elif operation == 'pow':
        if len(args) == 2:
            res = int(math.pow(args[0], args[1]))
        elif len(args) > 2:
            return jsonify({"error-message": "Error: Too many arguments to perform the operation " + operation}), 409
        else:
            return jsonify({"error-message": "Error: Not enough arguments to perform the operation " + operation}), 409
    elif operation == 'abs':
        if len(args) == 1:
            res = int(math.abs(args[0]))
        elif len(args) > 1:
            return jsonify({"error-message": "Error: Too many arguments to perform the operation " + operation}), 409
        else:
            return jsonify({"error-message": "Error: Not enough arguments to perform the operation " + operation}), 409
    elif operation == 'fact':
        if len(args) == 1:
            res = int(math.factorial(args[0]))
        elif len(args) > 1:
            return jsonify({"error-message": "Error: Too many arguments to perform the operation " + operation}), 409
        else:
            return jsonify({"error-message": "Error: Not enough arguments to perform the operation " + operation}), 409
    else:
        return jsonify({"error-message": "Error: unknown operation: " + operation}), 409
    return jsonify({"result": res}), 200


@server.route("/stack/size", methods=['GET'])
def get_stack_size():
    return jsonify({"result": len(stack)}), 200


@server.route("/stack/operate", methods=['GET'])
def calculate_stack_operation():
    query_args = request.args
    operation = query_args['operation'].lower()
    if operation == 'abs' or operation == 'fact':
        if len(stack) > 0:
            if operation == 'abs':
                result = math.abs(stack.pop())
            else:
                result = math.factorial(stack.pop())
        else:
            return jsonify({"error-message": "Error: cannot implement operation " + operation +
                                             ". It requires 1 arguments and the stack has only " + str(len(stack))
                                             + " arguments"}), 409
    elif operation == 'plus' or operation == 'minus' or operation == 'times' or operation == 'divide' or operation == 'pow':
        if len(stack) > 1:
            if operation == 'plus':
                result = stack.pop() + stack.pop()
            elif operation == 'minus':
                result = stack.pop() - stack.pop()
            elif operation == 'times':
                result = stack.pop() * stack.pop()
            elif operation == 'divide':
                x = stack.pop()
                y = stack.pop()
                if y == 0:
                    return jsonify({"error-message": "Error while performing operation Divide: division by 0"}), 409
                else:
                    result = stack.pop() / stack.pop()
            elif operation == 'pow':
                result = math.pow(stack.pop(), stack.pop())
        else:
            return jsonify({"error-message": "Error: cannot implement operation " + operation +
                                             ". It requires 2 arguments and the stack has only " + str(len(stack))
                                             + " arguments"}), 409
    else:
        return jsonify({"error-message": "Error: unknown operation: " + operation}), 409
    return jsonify({"result": int(result)}), 200


@server.route("/stack/arguments", methods=['PUT', 'DELETE'])
def add_arguments_to_stack():
    if request.method == 'PUT':
        content = request.get_json()
        for arg in content['arguments']:
            stack.append(arg)
    else:
        query_args = request.args
        count = int(query_args['count'])
        if count > len(stack):
            return jsonify({"error-message": "Error: cannot remove" + str(count) +
                                             "from the stack. It has only " + str(len(stack)) + " arguments"}), 409
        else:
            while count > 0:
                stack.pop()
                count = count-1
    return jsonify({"result": len(stack)}), 200


if __name__ == '__main__':
    server.run(host="localhost", port=8496, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
