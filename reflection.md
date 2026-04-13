## Profile Comparisons

**High-Energy Pop vs Chill Lofi**
These two profiles produced completely different top results — Sunrise City for pop/happy versus Midnight Coding for lofi/chill. This makes sense because both genre and mood matched perfectly for each profile's top song, giving them a large +25 head start. The numerical features (energy, tempo) also aligned well in both cases, which is why both top scores were close to 35 points. The system correctly identified the "feel" of each profile.

**High-Energy Pop vs Deep Intense Rock**
Both profiles favor high energy and fast tempo, but their top recommendations were completely different because genre and mood dominate the scoring. Even though Iron Anthem (metal, rebellious) is numerically close to the rock profile's targets, it scored only 9.57 because there was no mood match. This shows the system prioritizes what genre a song belongs to over how it actually sounds — a real limitation for users who care more about vibe than label.

**Chill Lofi vs Middle-of-the-Road**
These two profiles returned nearly identical results even though the Middle-of-the-Road profile had neutral numerical preferences (all set to 0.5). The reason is that both profiles share the same genre (lofi) and mood (chill), and those two categories together are worth +25 points. This demonstrates the filter bubble problem clearly — a user with no strong numerical opinions still gets locked into the same genre/mood bubble as a highly specific user.

**Weight Experiment — Original vs Modified**
When energy weight was doubled and genre halved, Gym Hero dropped from #2 to #3 in the High-Energy Pop profile while Rooftop Lights moved up. This happened because Rooftop Lights has a mood match (+10) which partially compensated for losing some of the genre bonus, while Gym Hero relies heavily on the genre match alone. The experiment showed that even small weight changes can shift rankings, which means the choice of weights is a critical design decision — not just a technical detail.
