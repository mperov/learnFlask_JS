#!/bin/env python3

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/add', methods=["POST"])
def add():
    a = request.form.get('a', 0, type=int)
    b = request.form.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/')
def index():
    return render_template('plain.html')

if __name__ == '__main__':
    app.run(port=8080)
