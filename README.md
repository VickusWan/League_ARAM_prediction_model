![](https://github.com/VickusWan/League_ARAM_prediction_model/blob/EDA/images/league.jpg)

# League_ARAM_prediction_model

League of Legends is team-based game where players form a team of five and assume the role of a champion, characters with unique abilities, generally varying around a type of class, and battle against another team of five players. ARAM (all random, all mid) is a game mode where the champions are randomly selected (rather than picked).

## Goal/Hypothesis
Since the champions of each players are randomly selected, the goal of this data analysis is to find whether certain parameters affected the winning rate of games. Several factors that are included in the data set are: 
- Team kills
- Team deaths
- Total Damage Dealt
- Total Damage Taken
- Total Time CC'ed (how long is the champion stunned/unable to move)
- Total Gold Earned
- First turret
- Champion Tag

## Data Scrapping/Collection
Since there were no available dataset on the specific hypothesis, the data had to be collected through the RIOT developed API (https://developer.riotgames.com/apis) (note: users need a personal API key in order to access the API). The steps to obtain the dataset were:
1. Obtain a summoner's encrypted ID, which can be found using a summoner's name.
2. Using the summoner's encrypted ID, obtain the match history for the past 100 games.
3. Obtain each match's ID and filter out games that are ARAM game modes only.
4. Using the matchID, extract the information mentioned above.

The final dataset contains approximately 2000 points, which is found under (Match_history.csv) https://github.com/VickusWan/League_ARAM_prediction_model/blob/EDA/Match_history.csv

## Exploratory Data Analysis (EDA)

After the data is cleaned up, parameters were visualized against each other to find trends or patterns.

![](https://github.com/VickusWan/League_ARAM_prediction_model/blob/EDA/images/damage.png)
