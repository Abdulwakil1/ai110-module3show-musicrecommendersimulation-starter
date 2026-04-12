
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:

    """Read songs from a CSV file and return a list of dicts with numeric fields cast to float/int."""

    songs: List[Dict] = []
    float_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            song = dict(row)
            song["id"] = int(song["id"])
            for field in float_fields:
                song[field] = float(song[field])
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """Compute a relevance score and explanation for a single song given user preferences."""

    score = 0.0
    reasons = []
    
    # Genre match
    if song['genre'].lower() == user_prefs['genre'].lower():
        score += 15.0
        reasons.append("genre match (+15.0)")
    
    # Mood match
    if song['mood'].lower() == user_prefs['mood'].lower():
        score += 10.0
        reasons.append("mood match (+10.0)")
    
    # Numerical features with proximity scoring
    features = [
        ('energy', 3.0, 1.0),
        ('tempo_bpm', 2.5, 176),
        ('valence', 2.0, 1.0),
        ('danceability', 2.0, 1.0),
        ('acousticness', 0.8, 1.0)
    ]
    
    for feature_name, weight, range_val in features:
        user_val = user_prefs.get(feature_name, 0.5)
        song_val = song[feature_name]
        proximity = weight * (1 - abs(user_val - song_val) / range_val)
        score += proximity
        reasons.append(f"{feature_name} proximity ({proximity:.2f})")
    
    explanation = ", ".join(reasons)
    return (score, explanation)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs against user preferences and return the top k results sorted by score."""
    scored_songs = [
        (song, score, explanation)
        for song in songs
        for score, explanation in [score_song(user_prefs, song)]
    ]
    return sorted(scored_songs, key=lambda item: item[1], reverse=True)[:k]
