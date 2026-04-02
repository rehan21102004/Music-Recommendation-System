# 🎵 Music Recommendation System

##  Overview
This project is a Music Recommendation System that suggests songs based on user input. It uses content-based filtering to recommend songs with similar features such as artist, genre, and lyrics.

---

##  Features
- Recommend top 5 similar songs
- Uses TF-IDF Vectorization
- Cosine Similarity for matching songs
- Simple and interactive Streamlit UI
- Displays song details and thumbnails

---

##  Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

##  Dataset
- Bollywood Songs Dataset
- Contains song name, artist, album, genre, and lyrics

---

## ⚙️ How It Works
1. Data is preprocessed and cleaned  
2. Important features are combined into a single column (tags)  
3. TF-IDF converts text into numerical form  
4. Cosine similarity finds similar songs  
5. Top 5 similar songs are recommended  

---

##  How to Run
1. Clone the repository:
git clone https://github.com/your-username/your-repo-name.git

2. Install dependencies:
pip install -r requirements.txt

3. Run the app:
streamlit run app.py

---

##  Output
- Displays top 5 recommended songs based on user selection

---

##  Future Improvements
- Add Spotify API integration  
- Include user-based recommendations  
- Improve UI design  

---

## 👨‍💻 Author
Rehan Asif Shaikh