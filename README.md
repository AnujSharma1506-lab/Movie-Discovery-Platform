# 🎬 Movie Recommender System

A **content-based Movie Recommendation System** built using **Python, Machine Learning, and Streamlit**.  
This web application recommends movies similar to the one selected by the user and fetches real-time movie details using the **TMDB API**.


## 🚀 Features

- 🎥 Select a movie from a dropdown list
- ⭐ Get top 5 recommended movies
- 🖼️ Movie posters fetched using TMDB API
- 📄 Detailed movie information:
  - Overview
  - Release Date
  - Genres
  - Rating
- ⚡ Interactive UI using Streamlit
- 🔗 Clickable movie posters (enhanced version)


## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Pickle
- Requests
- TMDB API
- Machine Learning (Cosine Similarity)


## 📂 Project Structure

├── app.py
├── a.py
├── movies_dict.pkl
├── similarity.pkl
├── README.md


## 🔑 TMDB API Key

This project uses **The Movie Database (TMDB) API** to fetch movie posters and details.
Replace the API key in the code if required:

python
TMDB_API_KEY = "your_api_key_here"

Get your API key from:  
https://www.themoviedb.org/


## ▶️ How to Run the Project

### 1️⃣ Install Required Libraries
bash
pip install streamlit pandas requests

### 2️⃣ Run the Application
bash
streamlit run app.py

### 3️⃣ Open in Browser

Streamlit will automatically open the app in your browser.  
If not, visit:
http://localhost:8501


## 🧠 Recommendation Logic

- Movie data is vectorized
- Similarity between movies is calculated using cosine similarity
- Top 5 most similar movies are recommended
- Similarity matrix is stored in `similarity.pkl`


## 📸 Output Preview

- Movie selection dropdown
- Recommended movies with posters
- Detailed movie information on click
- Clean and interactive UI
