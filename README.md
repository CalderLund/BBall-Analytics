# To host the app locally:

### change to source code directory
cd src/

### download all required libraries
pip3 install -r requirements.txt

### host server locally
python3 manage.py runserver

### NOTE: You might not be able to host the app locally because the Lib folder is not present.
### We removed Lib folder in order to keep the size within Markus upload maximum.


# To access the app deployed by GCP:
Go to: https://bball-analytics.appspot.com/

# Information regarding Milestone 02:

Files related to Database Design Schema can be found under /Report directory

You can find the schema definition of all the tables under /sql/tables 
You can find test-sample.sql and test-sample.output under /sql

### Within our application, see /src/teams/models.py and /src/players/models.py:
  1. For code that creates our tables
  2. For code that uses pandas to scrape real data from csv files to populate the tables "TeamsInfo", "TeamStats", "Player" and "PlayerStats"
### url for data found in: 
  (https://www.kaggle.com/drgilermo/nba-players-stats?fbclid=IwAR3Ch4TslrxGwKE4iaEBuwidrFVzsQ6oY4oQMJu_X5xjo__5svRcowjyHgo) - and (https://www.kaggle.com/open-source-sports/mens-professional-basketball) - we have csv's in github already

### Features implemented so far (We used Django to implement a simple Database-Driven Application):
  1. That displays all unique basketball teams that have played since the 1930's
  2. That takes year as a user input and displays all basketball teams that played in that particular year. User Input comes through a drop-down menu of years
  3. Click on a team to see what years the team played in. This displays all years the team has played in. Then select a year which will then display the selected team's performance summary for that year. You may then click the button to display all players who played for this team in the selected year. (NOTE: List of players may be missing for some of the earlier years ex: 1930's '40's etc.) Finally, you can click on each of the users to view their stats for the selected team in the selected year.

### Relevant source code can be found under:
  1. /src/teams/models.py 
  2. /src/teams/views.py
  3. /src/players/models.py
  4. /src/players/views.py  directory
  
  
  ### Features 
  # Advanced Matrix /src/teams/tables/advanceMetricsView.sql
  The view 36 min caculates the average data(include, PER, TS%, offensive rating, defensive rating, rebound rate, game
score, etc) in a period of 36 min. This advanced metrix is very helpful when interpreting given data for each player and team. 
