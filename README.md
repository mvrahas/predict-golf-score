# Predict Golf Score

## About

Understanding stats about your golf game can help you improve. This linear regression model (built with Scikit-learn) can predict a golfer's expected score based on their stats, or vice versa. I created this as my final project in a General Assembly boot camp.

My project was featured on Towards Data Science! [View on Medium](https://towardsdatascience.com/scikit-learn-linear-regression-for-predicting-golf-performance-c92f31b69f92)

## Run The Project

Review the model using Jupyter Notebook. 

-OR-

Deploy the model to Heroku and access the functionality using a REST API. Documentation below.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Documentation

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
