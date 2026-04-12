from src.recommender import load_songs, recommend_songs
def main() -> None:
    songs = load_songs("data/songs.csv") 
    
    # Starter example profile improved with more attributes for better recommendations
    user_prefs = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.80,
    "tempo_bpm": 120,
    "valence": 0.75,
    "danceability": 0.80,
    "acousticness": 0.20
}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # Header
    print("\n" + "="*60)
    print("🎵 MUSIC RECOMMENDER - PERSONALIZED FOR YOU")
    print("="*60)
    print(f"Genre: {user_prefs['genre'].title()} | Mood: {user_prefs['mood'].title()}")
    print("="*60 + "\n")

    # Recommendations
    for rank, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"#{rank} - {song['title']} by {song.get('artist', 'Unknown')}")
        print(f"Score: {score:.2f}/40")
        
        # Handle explanation as string or list
        explanation_list = explanation.split(", ")
        for reason in explanation_list:
            print(f"  • {reason}")
        
        print("-" * 60 + "\n")


if __name__ == "__main__":
    main()
