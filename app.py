import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return jsonify("hello world")
app.run()
if __name__=="__main__":
    app.run(debug=True)
