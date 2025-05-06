
https://github.com/user-attachments/assets/7414dbca-acaf-4af9-8900-4cb41eb1b489
# 🎬 Movie Recommender System

## This project is a **content-based movie recommender system** built with Python and Streamlit. It recommends movies similar to a user's selected movie using cosine similarity on movie metadata.

---

## 🚀 Features

* ## Select a movie and get 5 similar movie recommendations
* ## Uses precomputed cosine similarity on movie vectors
* ## Lightweight frontend powered by Streamlit
* ## Clean UI with poster images fetched via TMDb API

---
✨ Demo


https://github.com/user-attachments/assets/d8ad5cf1-c9ca-4a8c-8f3e-164646d5dc65



---
## 📂 Project Structure

```bash
├── App.py                      # Main Streamlit app
├── similarity_pkl_downloader.py  # Downloads the large similarity.pkl file
├── movies.pkl                  # Movie details
├── movies_dict.pkl             # Dictionary version of movies data
├── requirements.txt            # Python dependencies
├── Procfile, setup.sh          # For deployment (e.g., Heroku)
└── README.md                   # You're here
```

🔧 Setup Instructions
## Clone the repository
```
git clone https://github.com/SwarangiSawant2702/Movie_Recommender_System.git
cd Movie_Recommender_System
```
## Install the required packages
```
pip install -r requirements.txt
```
## Download the similarity matrix (similarity.pkl)
## Since similarity.pkl is too large for GitHub, run:

```
python similarity_pkl_downloader.py
```
## This script will download and save the file locally.

## Run the app

```
streamlit run App.py
```

# 🧠 How It Works
* ## Movie features are vectorized using genres, keywords, and cast/crew data.

* ## Cosine similarity is precomputed between movie vectors.

* ## The app finds top 5 most similar movies based on the similarity score.

# 🛠️ Tech Stack
## Frontend: Streamlit

## Backend: Python, Scikit-learn

## Data Handling: Pandas, Pickle

## Deployment-ready: Procfile, setup.sh included



# 📁 Note
## The similarity.pkl file is excluded from GitHub due to size constraints. Please run similarity_pkl_downloader.py to get it locally.


👩‍💻 Author
Swarangi Sawant
GitHub: @SwarangiSawant2702 give a read me file for all this

