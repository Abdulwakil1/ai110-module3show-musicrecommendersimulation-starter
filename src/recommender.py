
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
    float_fields = {
        "energy",
        "tempo_bpm",
        "valence",
        "danceability",
        "acousticness",
        "instrumentalness",
        "loudness",
        "speechiness",
    }
    int_fields = {"id", "popularity", "release_decade"}

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            song = dict(row)
            for field in int_fields:
                if field in song and song[field] != "":
                    song[field] = int(song[field])
            for field in float_fields:
                if field in song and song[field] != "":
                    song[field] = float(song[field])
            songs.append(song)

    return songs

def _get_scoring_weights(mode: Optional[str] = None) -> Dict[str, float]:
    """Return scoring weights for the selected recommendation mode."""
    normalized_mode = (mode or "default").strip().lower()

    mode_weights = {
        "default": {"genre": 15.0, "mood": 10.0, "energy": 3.0},
        "genre-first": {"genre": 30.0, "mood": 5.0, "energy": 3.0},
        "mood-first": {"genre": 7.5, "mood": 20.0, "energy": 3.0},
        "energy-focused": {"genre": 7.5, "mood": 5.0, "energy": 9.0},
    }

    if normalized_mode not in mode_weights:
        valid_modes = ", ".join(mode_weights.keys())
        raise ValueError(f"Unknown mode '{mode}'. Valid modes: {valid_modes}")

    return mode_weights[normalized_mode]

def score_song(user_prefs: Dict, song: Dict, mode: Optional[str] = None) -> Tuple[float, str]:
    """Compute a relevance score and explanation for a single song given user preferences."""

    weights = _get_scoring_weights(mode)
    score = 0.0
    reasons = []
    
    # Genre match
    if song['genre'].lower() == user_prefs['genre'].lower():
        score += weights['genre']
        reasons.append(f"genre match (+{weights['genre']:.1f})")
    
    # Mood match
    if song['mood'].lower() == user_prefs['mood'].lower():
        score += weights['mood']
        reasons.append(f"mood match (+{weights['mood']:.1f})")
    
    # Numerical features with proximity scoring
    features = [
        ('energy', weights['energy'], 1.0),
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

    popularity_score = 1.5 * (1 - abs(user_prefs.get('popularity', 50) - song['popularity']) / 100)
    score += popularity_score
    reasons.append(f"popularity proximity ({popularity_score:.2f})")

    user_decade = user_prefs.get('release_decade', song['release_decade'])
    decade_gap = abs(user_decade - song['release_decade']) // 10
    if decade_gap == 0:
        release_decade_score = 1.0
    elif decade_gap == 1:
        release_decade_score = 0.5
    else:
        release_decade_score = 0.0
    score += release_decade_score
    reasons.append(f"release_decade proximity ({release_decade_score:.2f})")

    user_tags_raw = user_prefs.get('mood_tags', '')
    if isinstance(user_tags_raw, str):
        user_tags = [tag.strip().lower() for tag in user_tags_raw.split(',') if tag.strip()]
    else:
        user_tags = [str(tag).strip().lower() for tag in user_tags_raw if str(tag).strip()]

    song_tags_raw = song.get('mood_tags', '')
    if isinstance(song_tags_raw, str):
        song_tags = [tag.strip().lower() for tag in song_tags_raw.split(',') if tag.strip()]
    else:
        song_tags = [str(tag).strip().lower() for tag in song_tags_raw if str(tag).strip()]

    matching_tags = len(set(user_tags) & set(song_tags))
    mood_tags_score = 2.0 * (matching_tags / len(user_tags)) if user_tags else 0.0
    score += mood_tags_score
    reasons.append(f"mood_tags overlap ({mood_tags_score:.2f})")

    instrumentalness_score = 1.5 * (1 - abs(user_prefs.get('instrumentalness', 0.5) - song['instrumentalness']))
    score += instrumentalness_score
    reasons.append(f"instrumentalness proximity ({instrumentalness_score:.2f})")

    loudness_score = 1.5 * (1 - abs(user_prefs.get('loudness', 0.5) - song['loudness']))
    score += loudness_score
    reasons.append(f"loudness proximity ({loudness_score:.2f})")

    speechiness_score = 1.0 * (1 - abs(user_prefs.get('speechiness', 0.5) - song['speechiness']))
    score += speechiness_score
    reasons.append(f"speechiness proximity ({speechiness_score:.2f})")
    
    explanation = ", ".join(reasons)
    return (score, explanation)

def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
    mode: Optional[str] = None,
) -> List[Tuple[Dict, float, str]]:
    """Score all songs against user preferences and return the top k results sorted by score."""
    scored_songs = [
        (song, score, explanation)
        for song in songs
        for score, explanation in [score_song(user_prefs, song, mode=mode)]
    ]
    remaining = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    selected: List[Tuple[Dict, float, str]] = []

    while remaining and len(selected) < k:
        selected_artists = {song["artist"] for song, _, _ in selected}
        selected_genres: Dict[str, int] = {}
        for song, _, _ in selected:
            genre = song["genre"]
            selected_genres[genre] = selected_genres.get(genre, 0) + 1

        adjusted_remaining = []
        for song, score, explanation in remaining:
            adjusted_score = score
            penalty_notes = []

            if song["artist"] in selected_artists:
                adjusted_score -= 5.0
                penalty_notes.append("artist diversity penalty (-5.0)")

            if selected_genres.get(song["genre"], 0) >= 2:
                adjusted_score -= 3.0
                penalty_notes.append("genre diversity penalty (-3.0)")

            if penalty_notes:
                explanation = f"{explanation}; {', '.join(penalty_notes)}"

            adjusted_remaining.append((song, adjusted_score, explanation, penalty_notes))

        ranked_candidates = sorted(adjusted_remaining, key=lambda item: item[1], reverse=True)
        selected_song, selected_score, selected_explanation, selected_penalty_notes = ranked_candidates.pop(0)
        selected.append((selected_song, selected_score, selected_explanation))
        remaining = [(song, score, explanation) for song, score, explanation, _ in ranked_candidates]

    return selected
