import flask

app = flask.Flask(__name__)

@app.route("/score", methods=['GET'])
def hello():
    return "Predict score"


@app.route("/stats")
def new():
    return "Predict stats"



if __name__ == '__main__':
    app.run(debug=True)
