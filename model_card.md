# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**

---

## 2. Intended Use

Describe what your recommender is designed to do and who it is for.

Prompts:

- What kind of recommendations does it generate
- What assumptions does it make about the user
- Is this for real users or classroom exploration

---

## 3. How the Model Works

Explain your scoring approach in simple language.

Prompts:

- What features of each song are used (genre, energy, mood, etc.)
- What user preferences are considered
- How does the model turn those into a score
- What changes did you make from the starter logic

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data

Describe the dataset the model uses.

Prompts:

- How many songs are in the catalog
- What genres or moods are represented
- Did you add or remove data
- Are there parts of musical taste missing in the dataset

---

## 5. Strengths

Where does your system seem to work well

Prompts:

- User types for which it gives reasonable results
- Any patterns you think your scoring captures correctly
- Cases where the recommendations matched your intuition

---

## 6. Limitations and Bias

Where the system struggles or behaves unfairly.

<!-- Prompts:

- Features it does not consider
- Genres or moods that are underrepresented
- Cases where the system overfits to one preference
- Ways the scoring might unintentionally favor some users   -->

## 6. Limitations and Bias

The most significant limitation of this recommender is its strong filter bubble tendency. Because genre match awards +15 points and mood match awards +10 points, categorical features together contribute up to +25 out of a maximum ~40 points, while all five numerical features combined contribute only ~10.3 points at best. This means the system almost always recommends songs within the same genre and mood, suppressing cross-genre discovery even when a song from a different genre might be a near-perfect numerical match.

The dataset composition introduces additional bias. Lofi and pop are the only genres with more than one song each, meaning users who prefer lofi or pop receive meaningfully better recommendations than users who prefer metal, classical, afrobeat, or latin — genres represented by only a single song. A Deep Intense Rock user, for example, has only one song (Storm Runner) that can earn the full genre+mood bonus, causing a sharp drop-off after the first recommendation.

The scoring logic also disadvantages users with extreme energy preferences. While the energy proximity formula is mathematically symmetric, the catalog contains far more high-energy tracks than low-energy ones, leaving low-energy users with fewer strong numerical matches. Furthermore, even a perfect energy match contributes only +3.0 points — far too small to overcome a genre or mood mismatch, meaning users with strong energy preferences are systematically under-served.

Finally, the system only supports a single genre and mood preference per user profile, making it unsuitable for multi-genre listeners or users who want to explore new styles outside their stated preferences.

---

## 7. Evaluation

How you checked whether the recommender behaved as expected.

<!-- Prompts:

- Which user profiles you tested
- What you looked for in the recommendations
- What surprised you
- Any simple tests or comparisons you ran

No need for numeric metrics unless you created some. -->

I tested the recommender with four user profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and Middle-of-the-Road. For each profile, I ran the full catalog of 18 songs through the scoring function and reviewed the top 5 results.

The most surprising result came from the Deep Intense Rock profile — only one song in the catalog (Storm Runner) earned the full genre and mood bonus, causing a sharp drop from 35.13 points at #1 to 18.82 at #2. This exposed a clear dataset gap: underrepresented genres produce weak recommendation lists after the first result.

The Middle-of-the-Road profile confirmed the filter bubble risk. Despite setting all numerical preferences to neutral midpoint values, the system still returned the same lofi/chill songs as the Chill Lofi profile — the genre and mood bonuses completely dominated the score, making neutral numerical preferences meaningless.

I also ran a weight experiment by doubling energy (3.0 → 6.0) and halving genre (15.0 → 7.5). This caused Gym Hero and Rooftop Lights to swap positions in the High-Energy Pop profile, showing the system is sensitive to weight changes. The original weights were then restored.

---

## 8. Future Work

Ideas for how you would improve the model next.

Prompts:

- Additional features or preferences
- Better ways to explain recommendations
- Improving diversity among the top results
- Handling more complex user tastes

---

## 9. Personal Reflection

A few sentences about your experience.

Prompts:

- What you learned about recommender systems
- Something unexpected or interesting you discovered
- How this changed the way you think about music recommendation apps
