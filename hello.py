import flask
import pickle
import numpy as np

app = flask.Flask(__name__)

@app.route("/stats-to-score", methods=['GET'])

#http://localhost:5000/stats-to-score?putts=34&fairways=2&greens=5

def returnscore():
    putts = int(flask.request.args.get('putts'))
    fairways = int(flask.request.args.get('fairways'))
    greens = int(flask.request.args.get('greens'))

    model = pickle.load(open('./exports/Score.pkl','rb'))
    target_score = model.predict(np.array([[putts, fairways,greens]]))[0]

    return str(target_score)


@app.route("/score-to-stats")

#http://localhost:5000/score-to-stats?score=79

def returnstats():
    
    features = ['Putts','Greens','Fairways']

    target_stats = []
    target_score = int(flask.request.args.get('score'))

    print(type(target_score))

    for feature in features:
        model = pickle.load(open('./exports/'+feature+'.pkl','rb'))
        target_stat = model.predict(np.array([target_score]).reshape(-1, 1))
        target_stats.append(target_stat[0])

    return str(target_stats)


if __name__ == '__main__':
    app.run(debug=True)
