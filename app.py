from flask import Flask, jsonify, render_template
import subprocess

app = Flask(__name__)


@app.route('/oversikt', methods=['GET'])
def get_oversikt():
    
    return render_template('index.html')

#def writeFile():

#def readFile():


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)