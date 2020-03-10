--get all years where Chicago Stags has data
SELECT yr from TeamStats WHERE team_id='CHS'

--get team info for Chicago Stags in 1946
SELECT tm_rank, won, lost, games, homeWon, homeLost, awayWon, awayLost, neutWon, neutLoss
 from TeamStats WHERE team_id='CHS' AND yr='{}'

--create player table
CREATE TABLE Player
  (
     name VARCHAR(100) NOT NULL PRIMARY KEY,
     height INT,
     weight INT,
     collage VARCHAR(100),
     born INT,
     birthCity VARCHAR(100),
     birthState VARCHAR(100)
  )

--drop player table
DROP TABLE Player

--delete all rows form player
DELETE from Player

--create player stat table
CREATE TABLE PlayerStats (
      name VARCHAR(100) NOT NULL REFERENCES Player(name),
      year INT NOT NULL,
      teamID VARCHAR(3) NOT NULL,
      pos VARCHAR(50),
      age INT,
      G INT DEFAULT 0,
      GS INT DEFAULT 0,
      MP INT DEFAULT 0,
      PER FLOAT DEFAULT 0,
      TS_percent FLOAT DEFAULT 0,
      PAr3 FLOAT DEFAULT 0,
      FTr FLOAT DEFAULT 0,
      ORB_percent FLOAT DEFAULT 0,
      DRB_percent FLOAT DEFAULT 0,
      TRB_percent FLOAT DEFAULT 0,
      AST_percent FLOAT DEFAULT 0,
      STL_percent FLOAT DEFAULT 0,
      BLK_percent FLOAT DEFAULT 0,
      TOV_percent FLOAT DEFAULT 0,
   , WS   USG_percent FLOAT DEFAULT 0,
      blanl FLOAT DEFAULT 0,
      OWS FLOAT DEFAULT 0,
      DWS FLOAT DEFAULT 0,
      WS FLOAT DEFAULT 0,
      WS_divide_48 FLOAT DEFAULT 0,
      blank2 FLOAT DEFAULT 0,
      OBPM FLOAT DEFAULT 0,
      DBPM FLOAT DEFAULT 0,
      BPM FLOAT DEFAULT 0,
      VORP FLOAT DEFAULT 0,
      FG FLOAT DEFAULT 0,
      FGA FLOAT DEFAULT 0,
      FG_percent FLOAT DEFAULT 0,
      P3 FLOAT DEFAULT 0,
      PA3 FLOAT DEFAULT 0,
      P3_percent FLOAT DEFAULT 0,
      P2 INT DEFAULT 0,
      P2A INT DEFAULT 0,
      P2_percent FLOAT DEFAULT 0,
      eFG_percent FLOAT DEFAULT 0,
      FT INT DEFAULT 0,
      FTA INT DEFAULT 0,
      FT_percent FLOAT DEFAULT 0,
      ORB INT DEFAULT 0,
      DRB INT DEFAULT 0,
      TRB INT DEFAULT 0,
      AST INT DEFAULT 0,
      STL INT DEFAULT 0,
      BLK INT DEFAULT 0,
      TOV INT DEFAULT 0,
      PF INT DEFAULT 0,
      PTS INT DEFAULT 0,
      PRIMARY KEY(name, year, teamID)
  )

-- drop playerStats table
DROP TABLE PlayerStats

--insert into player stats
INSERT into PlayerStats VALUES("Curly Armstrong", "1950", "FTW", "G-F", "31", "63", "0", "0", "0", "0.368", "0", "0.467")

--get all players' info who play for Boston Celtics in the year 2010
SELECT Player.name, PlayerStats.pos, Player.height, Player.weight, Player.born, Player.birthCity, Player.birthState, Player.collage
from PlayerStats JOIN Player
ON PlayerStats.name = Player.name
WHERE PlayerStats.teamID='BOS' AND PlayerStats.year=2010

--get Michael Finley's 2010 summary data for Boston Celtics
SELECT G, PTS, AST, FG, FG_percent, FT, FT_percent, eFG_percent from PlayerStats WHERE name='Michael Finley' AND year=2010 AND teamID='BOS'
