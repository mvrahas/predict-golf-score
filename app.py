from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

@app.route("/stats-to-score", methods=['GET'])

def returnscore():


    try:
        putts = int(request.args.get('putts'))
        fairways = int(request.args.get('fairways'))
        greens = int(request.args.get('greens'))

        model = pickle.load(open('./exports/Score.pkl','rb'))
        target_score = model.predict(np.array([[putts, fairways,greens]]))[0]

        return jsonify(score=target_score)
    except:
        return 'Something went wrong'


@app.route("/score-to-stats")

def returnstats():
    try:
        features = ['Putts','Fairways','Greens']

        target_stats = []
        target_score = int(request.args.get('score'))

        print(type(target_score))

        for feature in features:
            model = pickle.load(open('./exports/'+feature+'.pkl','rb'))
            target_stat = model.predict(np.array([target_score]).reshape(-1, 1))
            target_stats.append(target_stat[0])

        return jsonify(putts=target_stats[0],fairways=target_stats[1], greens=target_stats[2])
    except:
        return 'Something went wrong'


if __name__ == '__main__':
    app.run(debug=True)
