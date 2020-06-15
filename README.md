# Golf Game Improvement Model

**Overview :**

Understanding stats about your golf game can help you improve. They can give you objective feedback about where to pracitce and how to play your game while out on the course. The purpose of this model is to help golfers understand how different stats relate to their final score.

The model is wrapped inside a simple Flask web application that can be deployed to Heroku for ease of use. See documentation for how to use the model below...

**Documentation :**

*Stats to Score*
Predict a golfers score based on his/her stats (Putts, Fairways, Greens).

```
GET {{url}}/stats-to-score?putts=32&fairways=7&greens=4

-->
{
  "score": 89.60187727842703
}
```

*Score to Stats*
Predict a golfers stats (Putts, Fairways, Greens) based on his/her score.

```
GET {{url}}/score-to-stats?score=79

-->
{
  "fairways": 7.292152340471098, 
  "greens": 8.224321683108784, 
  "putts": 30.231101484019675
}
```
