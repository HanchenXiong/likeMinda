from flask import Flask, Response
import json
import random

app = Flask(__name__)

@app.route('/api/search')
def index(): 
   random.shuffle(content)
   tweetIDs = [{"id": id} for id in content[:10]]
   js = json.dumps(tweetIDs)
   resp = Response(js, status=200, mimetype='application/json')
   return resp  


if __name__ == '__main__':
   with open('likeminds_sample.tsv') as f:
      content = f.readlines()
   content = ["https://twitter.com/jack/status/" + x.strip('\n') for x in content]
   app.run(debug=True, port=2222)

