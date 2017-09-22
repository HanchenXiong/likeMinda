from flask import Flask, Response
import json
import random

app = Flask(__name__)

@app.route('/api/search', methods=['POST'])
def index(): 
   tweets = request.json.get('tweets') 
   tweet_ids = [e.id for e in tweets]
   tweet_txt = [e.text for e in tweets]

   vecs = embedding(tweet_txt)
   query_vec = vecs[0,:]
   blender_vecs = vecs[1:, :]
  
   faiss_neighbours = faiss_findKNeighbours(query_vec, k)
   blender_neighbours = blender_findKNeighbours(query_vec, blender_vecs, tweet_ids, k)
   neighbours = list(set([faiss_neighbours, blender_neighbours]))
   random.shuffle(neighbours)
   

   content = ["https://twitter.com/jack/status/"  + str(neighbour) for neighbour in neighbours]
   tweetIDs = [{"id": id} for id in content]
   js = json.dumps(tweetIDs)  
   resp = Response(js, status=200, mimetype='application/json')
   return resp  


def embedding(tweets_txt): 
  // to do: BY FMASSA
  return numpy.ones(2000)


def faiss_neighbours(query_vec, k):
   // to do: BY FMASSA
  return (01232323343432432,  4554342332323123, 992132131244234343,  4454352345433434) 

def blender_findKNeighbours(query_vec, blender_vecs, tweet_ids, k):
  // to do: BYFMASSA

def findKNeighbours(vec, k):
  
if __name__ == '__main__':
   with open('likeminds_sample.tsv') as f:
      content = f.readlines()
   content = ["https://twitter.com/jack/status/" + x.strip('\n') for x in content]
   app.run(debug=True, port=2222)

