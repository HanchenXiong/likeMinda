from flask import Flask, Response
import json
import random

app = Flask(__name__)

@app.route('/api/search')
def index(): 
   tweet = Request.data.tweet 
   vec = embedding(tweet)
   neighbours = findKNeighbours(vec, k)
   content = ["https://twitter.com/jack/status/"  + str(neighbour) for neighbour in neighbours]
   tweetIDs = [{"id": id} for id in content]
   js = json.dumps(tweetIDs)  
   resp = Response(js, status=200, mimetype='application/json')
   return resp  


def embedding(tweet): 
  // to do: BY FMASSA
  return numpy.ones(2000)



def findKNeighbours(vec, k):
  // to do: BY FMASSA
  return (01232323343432432,  4554342332323123, 992132131244234343,  4454352345433434) 


if __name__ == '__main__':
   with open('likeminds_sample.tsv') as f:
      content = f.readlines()
   content = ["https://twitter.com/jack/status/" + x.strip('\n') for x in content]
   app.run(debug=True, port=2222)

