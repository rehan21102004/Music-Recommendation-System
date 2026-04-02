import streamlit as st
import pickle

# Page config
st.set_page_config(page_title="Music Recommender", layout="wide")

# Load data
df = pickle.load(open("songs_df.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #1DB954;
            
    }
    .card {
        background-color: #181818;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        transition: 0.3s;
    }
    .card:hover {
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='
text-align: center;
font-size: 60px;
background: linear-gradient(90deg, #1DB954, #1ed760);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
margin-bottom: 10px;
'>
🎵 Music Recommendation System
</h1>
""", unsafe_allow_html=True)

# Input
user_input = st.text_input("🔍 Search your favorite song")

# Recommendation function
def recommendation(song):
    song = song.lower()
    try:
        index = df[df['song_name'].str.lower() == song].index[0]
    except:
        return []

    distance = similarity[index]
    song_list = sorted(list(enumerate(distance)),
                       reverse=True, key=lambda x: x[1])[1:6]

    rec = []
    for i in song_list:
        rec.append({
            "song": df.iloc[i[0]]["song_name"],
            "artist": df.iloc[i[0]]["artist"],
            "thumbnail": df.iloc[i[0]]["thumbnail"] if "thumbnail" in df.columns else None
        })
    return rec

# Button
if st.button("Recommend Songs"):
    result = recommendation(user_input)

    if not result:
        st.error("Song not found")
    else:
        st.subheader("🎧 Recommended for you")

        # Create 5 columns (grid style)
        cols = st.columns(5)

        for idx, item in enumerate(result):
            with cols[idx]:
                st.markdown('<div class="card">', unsafe_allow_html=True)

                if item["thumbnail"]:
                    st.image(item["thumbnail"], width="stretch")

                st.markdown(f"**{item['song']}**")
                st.caption(item["artist"])

                st.markdown('</div>', unsafe_allow_html=True)
