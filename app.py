from flask import Flask
from flask import request, jsonify
from optim.DetailParser import DetailParser
from optim.Optimizer import Optimizer

import json
from pulp import *

app = Flask(__name__)


# Тут буде зберігатись інформація з запиту


@app.route('/')
def hello_world():
    return "Hello twts!"


@app.route("/recipient", methods=['GET', 'POST'])
def recipient():
    if request.method == 'GET':
        return jsonify("You send get HTTP")
    elif request.method == 'POST':
        jsoninfo = str(request.data.decode('utf-8'))
        data = json.loads(jsoninfo)
        # DetailParser(data)
        return "<html> You send some info <b>" + str(data) + "</html>"


@app.route("/optimization", methods=['GET', 'POST'])
def optimization():
    if request.method == 'GET':
        return jsonify("You send get HTTP")
    elif request.method == 'POST':
        jsoninfo = str(request.data.decode('utf-8'))
        data = json.loads(jsoninfo)
        parser = DetailParser(data)
        optimizator = Optimizer(parser.parsVideocard(), parser.parsMotherBoard(), parser.parsPowerSupply(),
                                parser.parsProcessor(), parser.parsRam(), parser.parsStorage())

        optimizator.initializeDictionarys()
        result = optimizator.optimize();

    string = "{"

    for variable in result.variables():
        if variable.varValue == 1:
            string += str(optimizator.dictionaryVariableAndDeatilInfo[variable.name]) + ",\n"

    string += "\"pc_price\": " + str(value(result.objective))
    string += "}"

    # strs = ""
    # for elem in optimizator.ramList:
    #     strs += str(elem) + '\n'

    return str(string)


if __name__ == '__main__':
    app.run()
