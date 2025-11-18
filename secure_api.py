#Import  required modules
from flask import Flask, jsonify, request

# Initialize the flask app
app = Flask(__name__)

#Define home route (endoint 1)
app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'GET':
        data = 'HELLO WORLD!'
        return jsonify({'data':data})

#Define the display number route (endpoint 2)
@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
    return jsonify({'data': num **2})

#Run app
if __name__ == '__main__':
    app.run(debug = True)
