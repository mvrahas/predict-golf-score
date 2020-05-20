# Golf Game Improvement Model

**Overview :**

Understanding stats about your golf game can help you improve. They can give you objective feedback about where to pracitce and how to play your game while out on the course. The purpose of this model is to help golfers understand how different stats relate to their final score.

**Function :**

- Predict a golfers score based on his/her stats (Input: Putts, Fairways, Greens) (Output: Score)
- Predict a golfer's stats based on his/her score (Input: Score) (Output: Putts, Greens, Fairways)

**Definitions :**

- Score (INT): The total number of shots taken in the round.
- Greens (INT): The number of greens in regulation (out of 18). [More Info](https://www.liveabout.com/what-is-green-in-regulation-gir-1560864)
- Putts (INT): The total number of putts taken in the round.
- Fairways (INT): The total number of fairways hit in a round (out of 14 assuming a course with 14 fairways)