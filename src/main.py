from src.recommender import load_songs, recommend_songs
def main() -> None:
    songs = load_songs("data/songs.csv") 
    
    # Multiple named profiles
    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.90,
            "tempo_bpm": 130,
            "valence": 0.85,
            "danceability": 0.88,
            "acousticness": 0.10,
            "popularity": 85,
            "release_decade": 2020,
            "mood_tags": "uplifting,energetic,anthemic",
            "instrumentalness": 0.08,
            "loudness": 0.88,
            "speechiness": 0.09
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.38,
            "tempo_bpm": 76,
            "valence": 0.58,
            "danceability": 0.60,
            "acousticness": 0.78,
            "popularity": 66,
            "release_decade": 2020,
            "mood_tags": "calm,study,nocturnal",
            "instrumentalness": 0.70,
            "loudness": 0.32,
            "speechiness": 0.04
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.92,
            "tempo_bpm": 155,
            "valence": 0.45,
            "danceability": 0.65,
            "acousticness": 0.08,
            "popularity": 72,
            "release_decade": 2010,
            "mood_tags": "aggressive,driving,charged",
            "instrumentalness": 0.10,
            "loudness": 0.91,
            "speechiness": 0.06
        }, 
        "Middle-of-the-Road": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.50,
        "tempo_bpm": 120,
        "valence": 0.50,
        "danceability": 0.50,
        "acousticness": 0.50,
        "popularity": 60,
        "release_decade": 2010,
        "mood_tags": "balanced,steady,chill",
        "instrumentalness": 0.50,
        "loudness": 0.50,
        "speechiness": 0.10
        }
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        # Header
        print("\n" + "="*60)
        print("🎵 MUSIC RECOMMENDER - PERSONALIZED FOR YOU")
        print(f"Profile: {profile_name}")
        print("="*60)
        print(f"Genre: {user_prefs['genre'].title()} | Mood: {user_prefs['mood'].title()}")
        print("="*60 + "\n")

        # Recommendations
        for rank, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print(f"#{rank} - {song['title']} by {song.get('artist', 'Unknown')}")
            print(f"Score: {score:.2f}")
            
            # Handle explanation as string or list
            explanation_list = explanation.split(", ")
            for reason in explanation_list:
                print(f"  • {reason}")
            
            print("-" * 60 + "\n")


if __name__ == "__main__":
    main()
