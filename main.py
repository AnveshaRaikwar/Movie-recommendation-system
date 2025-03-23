import pandas as pd
from sklearn.neighbors import NearestNeighbors


data = pd.read_csv('dataset.csv') 
data = data.head(1000)  # Selecting only 1000 movies from dataset

df = data[['name', 'rating', 'genre', 'score']].copy()
df['id'] = range(1, len(df) + 1)

# Converting categorical ratings to numerical values 
rating_map = {'G': 1, 'PG': 3, 'PG-13': 4, 'R': 5, 'Not Rated': 0}
df['rating'] = df['rating'].map(rating_map).fillna(2)  # default 2 for values other than in rating map

print("Data preview:")

# user-movie matrix
user_movie_matrix = df.pivot(index='id', columns='name', values='rating').fillna(0)

# KNN model
model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=6)
model_knn.fit(user_movie_matrix)

# Function to recommend movies
def recommend_movies(user_index):
    distances, indices = model_knn.kneighbors(user_movie_matrix.iloc[user_index, :].values.reshape(1, -1))
    recommended_movies = user_movie_matrix.columns[indices.flatten()]
    
    print(f"\nRecommended movies for User {user_index + 1}:")
    for movie in recommended_movies:
        print(movie)

# Adjusting recommendations based on mood
def adjust_recommendation_based_on_sentiment(user_index, sentiment):
    if sentiment == "Positive":
        print(f"\nUser {user_index + 1} has a positive sentiment. Recommending movies with positive ratings...")
    elif sentiment == "Negative":
        print(f"\nUser {user_index + 1} has a negative sentiment. Recommending movies with higher ratings...")
    else:
        print(f"\nUser {user_index + 1} has neutral sentiment. Recommending based on usual preferences...")
    
    recommend_movies(user_index)

# Main function
if __name__ == "__main__":
    while True:
        try:
            user_index = int(input("\nEnter user index (movie ID) to get recommendations: "))

            # IMP = Adjust index:
            user_index = abs(user_index)  # Convert negative index to positive
            user_index = (user_index - 1) % 1000  # Bring it within range 0-999

            user_sentiment = input("How's your mood? (Enter Positive, Negative, or Neutral): ").strip().capitalize()
            if user_sentiment not in ["Positive", "Negative", "Neutral"]:
                print("Invalid input. Defaulting to 'Neutral'.")
                user_sentiment = "Neutral"

            adjust_recommendation_based_on_sentiment(user_index, user_sentiment)
            break  # Exit the loop if input is valid

        except ValueError:
            print("Invalid input. Please enter a numeric value.")
