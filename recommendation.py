import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Define the get_recommendations function
def get_recommendations(title, df3, cosine_sim):
    
    if  title=='':
          return "title not entered"

    elif title not in df3['Title'].values:
        return "Movie not found in the dataset."
    idx = df3[df3['Title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:7]  # Top 5 recommendations
    movie_indices = [i[0] for i in sim_scores]
    
    recommendations = df3.iloc[movie_indices][['Title', 'Summary']]
    #output = ''
    output={}
    names=[]
    for index, row in recommendations.iterrows():
        #output += f"Title: {row['Title']}\n\nSummary: {row['Summary']}\n\n"
    #return output
        if (title!=row['Title']):       
            names = row['Title']
            summary = row['Summary']
            output[names] = summary
    return output
    