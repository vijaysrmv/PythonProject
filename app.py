from flask import Flask,jsonify,request

import ast

from flask_cors import cross_origin
from googletrans import Translator
app = Flask(__name__)


@app.route("/hello")
def hello():
    translate = Translator()
    list = ["Vijya", "Vinay", "Ajay"]
    list = str(list)
    result = translate.translate(list, dest='hi')
    print(result.text)
    print(type(result.text))
    print(ast.literal_eval(result.text))

    dic = {"data":ast.literal_eval(result.text)}
    return jsonify(dic)



@app.route('/')
@cross_origin
def hello_world():

    list = "Vijay"

    translate = Translator()


    results = translate.translate("vijay", dest='hi')

    dic = {"data":results.text}
    return jsonify(dic)


if __name__ == '__main__':
    app.run()
