# Movie Recommendation System (Content-Based Filtering)

This project builds a content-based movie recommendation system that suggests similar movies using text-based features such as genres, keywords, overview, cast, and director.

The system computes similarity between movies using vectorization and cosine similarity.

---

## Project Overview

- **Problem Type:** Recommendation System  
- **Approach:** Content-Based Filtering  
- **Techniques Used:** CountVectorizer + Cosine Similarity  
- **Framework:** scikit-learn  
- **Deployment:** Streamlit  

---

## Dataset

The dataset consists of movie metadata from TMDB, including:

- Overview (plot summary)
- Genres
- Keywords
- Cast
- Director

After preprocessing and merging datasets:

- Final dataset size: **1831 movies**

---

## Data Preprocessing

### Feature Engineering

The following features were combined to represent each movie:

- Overview  
- Genres  
- Keywords  
- Cast (top 3 actors)  
- Director  

### Text Processing Steps

- Converted JSON-like columns into lists  
- Extracted director information  
- Removed spaces from names  
- Combined all features into a single text column (`tags`)  
- Lowercased all text  

These steps allowed effective similarity-based recommendations.

---

## Modeling

This project uses a content-based filtering approach.

### Vectorization

Text features were converted into numerical form using:

- **CountVectorizer (max_features = 5000)**

### Similarity Computation

Movie similarity was calculated using:

- **Cosine Similarity**

The system recommends movies based on the closest similarity scores.

---

## Results

The recommendation engine produces meaningful suggestions.

Example:

Input: **Avatar**

Recommendations:

- Titan A.E.  
- Small Soldiers  
- Independence Day  
- Aliens vs Predator: Requiem  
- Ender's Game  

The results demonstrate strong content similarity.

---

## Deployment

The processed movie dataset and similarity matrix were saved using pickle.

The Streamlit application allows users to:

- Select a movie  
- Receive 5 similar recommendations  

---

## Conclusion

This project demonstrates how content-based recommendation systems can be built using text features and similarity measures.

It highlights the importance of preprocessing, feature engineering, and similarity-based modeling in building practical recommendation systems.

---

## How to Run Locally

git clone https://github.com/enesbayraktar61/movie-recommendation-system.git

cd movie-recommendation-system
pip install -r requirements.txt
streamlit run app.py

---

