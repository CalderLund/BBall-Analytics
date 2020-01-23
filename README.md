Tasks:
- populate data into google
      - data found in (https://www.kaggle.com/drgilermo/nba-players-stats?fbclid=IwAR3Ch4TslrxGwKE4iaEBuwidrFVzsQ6oY4oQMJu_X5xjo__5svRcowjyHgo) 
      - and (https://www.kaggle.com/open-source-sports/mens-professional-basketball)
      - we have csvs in github already
      
- Python, Django, Postgres
- Come up with feature based on available data
- Design Database schema



- accounts table, track favourite teams, track favourite players, favourite queries  <-- add to accounts, track things
- make your own team, see how it would do against another team.    <-- ability to add into fantasy teams table and potentially use ML 
- compare teams from different years
- list of teams should be clickable (like https://www.basketball-reference.com/) <-- tons of queries
- queries for best players in every category
--> ex. Give the top 10 players from the years 1990-2000 who played SG, more than 20 minutes a game, on specify teams, 
- advanced analytics using regular data


Tables:

Accounts
FavouriteTeams
FavouritePlayers
FantasyTeams

Teams
PlayerInfo
Season  TBD
PlayerStats


Table Schema:

# Tianchang
Accounts (PERIMARY KEY INT uid, VARCHAR(25) user, VARCHAR(25) pwd) \\
FavouriteTeams ((INT uid, CHAR(3) team_id, INT year) PRIMARY KEY) \\
FavouritePlayers ((INT uid, int player_id) PRIMARY KEY) \\
FantasyTeam

# Dhanish
// From basketball_team.csv

TeamInfo (CHAR(3) PRIMARY KEY team_id, VARCHAR(25) team_name)


// From basketball_tea.csv, later on turn 0 from confRank column into NUL \\
// ... -> all columns from o_fgm to games


TeamStats ((INT year, CHAR(3) team_id) PRIMARY KEY, INT rank, INT confRank, VARCHAR(2) playoff, ...)


# Alex
// From nba-players-stats/Players.csv and nba-players-stats/player_data.csv

PlayerInfo (SERIAL PRIMARY KEY pid, 

# Calder
// From nba-players-stats/Seasons_Stats.csv
// Everything from Seasons_Stats.csv, with (year, player, Tm) be the primary key

PlayerStats(...)
