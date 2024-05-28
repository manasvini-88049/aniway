from flask import Flask, request, jsonify
import pickle
from recommendation  import get_recommendations

with open('recommendation_system.pkl', 'rb') as file:
    functions_data = pickle.load(file)

# Extract functions and data

df3 = functions_data['df3']
cosine_sim = functions_data['cosine_sim']
app = Flask(__name__)


#title='Naruto'


@app.route('//recommendations', methods=['GET'])

def get_movie_recommendations():
    
    # Get the movie title from the request parameters
    #title = request.args.get('title')
    title = request.args.get('title')

    # Check if the title is provided
    #if not title:
        #return jsonify({'error': 'Movie title not provided'})
     
    # Get recommendations based on the user input
    recommendations = get_recommendations(title,   df3, cosine_sim)
                                        
    # Return the recommendations as JSON
    return jsonify({'recommended_movies': recommendations})


if __name__ == '__main__':
    app.run(debug=True)

#http://localhost:5000/recommendations