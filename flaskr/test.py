#!/usr/bin/env python
# -*- encoding:utf-8 -*-



from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(host='192.168.221.128', port=80)
