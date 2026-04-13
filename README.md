# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

<!-- Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful. -->

Real-world platforms like Spotify and YouTube Music primarily use two approaches: collaborative filtering, which infers taste from shared behavior across many users (plays, skips, playlist adds) without needing to know anything about the songs themselves, and content-based filtering, which compares song attributes like genre, mood, and energy against a user's known preferences to find the closest matches. This simulator uses a content-based approach — each song is scored by how closely its features align with a user's taste profile, and songs are ranked by that score to produce a personalized list.

**`Song` features:**

- `genre` — taste category (e.g., Pop, Lofi, Jazz)
- `mood` — emotional tone (e.g., Chill, Energetic, Sad)
- `energy` — intensity level (0.0–1.0)
- `tempo_bpm` — pace of the track in beats per minute
- `valence` — musical positivity (0.0–1.0)
- `danceability` — rhythmic suitability for dancing (0.0–1.0)
- `acousticness` — acoustic vs. electronic quality (0.0–1.0)

**`UserProfile` features:**

- `preferred_genre`, `preferred_mood` — categorical taste preferences
- `preferred_energy`, `preferred_tempo_bpm`, `preferred_valence`, `preferred_danceability`, `preferred_acousticness` — target numerical values the recommender scores each song against

### Algorithm Recipe

Each song is scored against the user profile using the following weights:

| Feature                | Type        | Points                            |
| ---------------------- | ----------- | --------------------------------- |
| Genre match            | Categorical | +15                               |
| Mood match             | Categorical | +10                               |
| Energy proximity       | Numerical   | 3.0 × (1 - \|user − song\|)       |
| Tempo proximity        | Numerical   | 2.5 × (1 - \|user − song\| / 176) |
| Valence proximity      | Numerical   | 2.0 × (1 - \|user − song\|)       |
| Danceability proximity | Numerical   | 2.0 × (1 - \|user − song\|)       |
| Acousticness proximity | Numerical   | 0.8 × (1 - \|user − song\|)       |

**Maximum possible score: ~40 points.** Songs are ranked by total score and the top-K results are returned as recommendations.

### Expected Bias

## Because genre and mood together account for up to 25 out of 40 possible points, this system may over-prioritize categorical matches — a song with the right genre and mood but poor numerical alignment could outrank a song that is a near-perfect numerical match in a different genre. Additionally, acousticness carries the lowest weight intentionally, meaning highly produced songs are not unfairly penalized for lacking acoustic qualities.

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

<!-- Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users -->

### Profile Test Results

![High-Energy Pop](screenshots/high_energy_pop.png)
![Chill Lofi](screenshots/chill_lofi.png)
![Deep Intense Rock](screenshots/deep_intense_rock.png)
![Middle-of-the-Road](screenshots/middle_of_the_road.png)

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:

- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:

- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:

- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"
```
