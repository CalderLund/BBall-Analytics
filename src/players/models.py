from django.db import models
from django.db import connection

import pandas as pd
import math
from decimal import Decimal
# Create your models here.

def createPlayerTable():
    createPlayerTableString = """
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
    """
    c = connection.cursor()
    try:
        c.execute(createPlayerTableString)
        print("Player table created.")
    finally:
        c.close()

def dropTablePlayer():
    c = connection.cursor()
    try:
        c.execute("DROP TABLE Player")
        print("Player Table Dropped!")
    finally:
        c.close()

def deleteAllRowsFromPlayer():
    c = connection.cursor()
    try:
        c.execute("DELETE from Player")
        print("Deleted All rows from Player")
    finally:
        c.close()

def populatePlayerData():
    players = pd.read_csv("players/Players.csv")
    # unique_teams = players.drop_duplicates(["tmID"])
    counter = 0
    c = connection.cursor()
    try:
        for index,row in players.iterrows():
            counter += 1
            c.execute("INSERT into Player VALUES (%s, %s, %s, %s, %s, %s, %s)", [row["Player"], row["height"], row["weight"], row["collage"], row["born"], row["birth_city"], row["birth_state"]])
            print(counter)
        print("-----------------")
        print("c= {}".format(counter))
    finally:
        c.close()

def getAllPlayers():
    c = connection.cursor()
    try:
        c.execute("select count(*) from Player")
        count = c.fetchall()
        print(count)
        return count
    finally:
        c.close()


def createPlayerStatsTable():
    createPlayerStatsTableString = """
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
    """
    c = connection.cursor()
    try:
        c.execute(createPlayerStatsTableString)
        print("PlayerStats table created.")
    finally:
        c.close()

def dropTablePlayerStats():
    c = connection.cursor()
    try:
        c.execute("DROP TABLE PlayerStats")
        print("PlayerStats Table Dropped!")
    finally:
        c.close()

def deleteAllRowsFromPlayerStats():
    c = connection.cursor()
    try:
        c.execute("DELETE from PlayerStats")
        print("Deleted All rows from PlayerStats")
    finally:
        c.close()

def populatePlayerStatsData():
    playersData = pd.read_csv("players/Seasons_Stats.csv")
    # unique_teams = players.drop_duplicates(["tmID"])
    counter = 0
    c = connection.cursor()
    try:
        for index,row in playersData.iterrows():
            # print(row)
            counter += 1
            G, GS, MP, PER, TS_percent, PAr3, FTr, ORB_percent, DRB_percent, TRB_percent = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 #10
            AST_percent, STL_percent, BLK_percent, TOV_percent, USG_percent, blanl, OWS = 0, 0, 0, 0, 0, 0, 0 #7
            DWS, WS, WS_divide_48, blank2, OBPM, DBPM, BPM, VORP, FG, FGA, FG_percent, P3 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 #12
            PA3, P3_percent, P2, P2A, P2_percent, eFG_percent, FT, FTA, FT_percent, ORB, DRB, TRB = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 #12
            AST, STL, BLK, TOV, PF, PTS = 0, 0, 0, 0, 0, 0 #6
            if not math.isnan(row["G"]):
                G = row["G"]
            if not math.isnan(row["GS"]):
                GS = row["GS"]
            if not math.isnan(row["MP"]):
                MP = row["MP"]
            if not math.isnan(row["PER"]):
                PER = row["PER"]
            if not math.isnan(row["TS%"]):
                TS_percent = row["TS%"]
            if not math.isnan(row["3PAr"]):
                PAr3 = row["3PAr"]
            if not math.isnan(row["FTr"]):
                FTr = row["FTr"]
            if not math.isnan(row["ORB%"]):
                ORB_percent = row["ORB%"]
            if not math.isnan(row["DRB%"]):
                DRB_percent = row["DRB%"]
            if not math.isnan(row["TRB%"]):
                TRB_percent = row["TRB%"]
            if not math.isnan(row["AST%"]):
                AST_percent = row["AST%"]
            if not math.isnan(row["STL%"]):
                STL_percent = row["STL%"]
            if not math.isnan(row["BLK%"]):
                BLK_percent = row["BLK%"]
            if not math.isnan(row["TOV%"]):
                TOV_percent = row["TOV%"]
            if not math.isnan(row["USG%"]):
                USG_percent = row["USG%"]
            if not math.isnan(row["blanl"]):
                blanl = row["blanl"]
            if not math.isnan(row["OWS"]):
                OWS = row["OWS"]
            if not math.isnan(row["DWS"]):
                DWS = row["DWS"]
            if not math.isnan(row["WS"]):
                WS = row["WS"]
            if not math.isnan(row["WS/48"]):
                WS_divide_48 = row["WS/48"]
            if not math.isnan(row["blank2"]):
                blank2 = row["blank2"]
            if not math.isnan(row["OBPM"]):
                OBPM = row["OBPM"]
            if not math.isnan(row["DBPM"]):
                DBPM = row["DBPM"]
            if not math.isnan(row["BPM"]):
                BPM = row["BPM"]
            if not math.isnan(row["VORP"]):
                VORP = row["VORP"]
            if not math.isnan(row["FG"]):
                FG = row["FG"]
            if not math.isnan(row["FGA"]):
                FGA = row["FGA"]
            if not math.isnan(row["FG%"]):
                FG_percent = row["FG%"]
            if not math.isnan(row["3P"]):
                P3 = row["3P"]
            if not math.isnan(row["3PA"]):
                PA3 = row["3PA"]
            if not math.isnan(row["3P%"]):
                P3_percent = row["3P%"]
            if not math.isnan(row["2P"]):
                P2 = row["2P"]
            if not math.isnan(row["2PA"]):
                P2A = row["2PA"]
            if not math.isnan(row["2P%"]):
                P2_percent = row["2P%"]
            if not math.isnan(row["eFG%"]):
                eFG_percent = row["eFG%"]
            if not math.isnan(row["FT"]):
                FT = row["FT"]
            if not math.isnan(row["FTA"]):
                FTA = row["FTA"]
            if not math.isnan(row["FT%"]):
                FT_percent = row["FT%"]
            if not math.isnan(row["ORB"]):
                ORB = row["ORB"]
            if not math.isnan(row["DRB"]):
                DRB = row["DRB"]
            if not math.isnan(row["TRB"]):
                TRB = row["TRB"]
            if not math.isnan(row["AST"]):
                AST = row["AST"]
            if not math.isnan(row["STL"]):
                STL = row["STL"]
            if not math.isnan(row["BLK"]):
                BLK = row["BLK"]
            if not math.isnan(row["TOV"]):
                TOV = row["TOV"]
            if not math.isnan(row["PF"]):
                PF = row["PF"]
            if not math.isnan(row["PTS"]):
                PTS = row["PTS"]
            c.execute("INSERT into PlayerStats VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [row["Player"], row["Year"], row["Tm"], row["Pos"], row["Age"], G, GS, MP, PER, TS_percent, PAr3, FTr, ORB_percent, DRB_percent, TRB_percent, AST_percent, STL_percent, BLK_percent, TOV_percent, USG_percent, blanl, OWS, DWS, WS, WS_divide_48, blank2, OBPM, DBPM, BPM, VORP, FG, FGA, FG_percent, P3, PA3, P3_percent, P2, P2A, P2_percent, eFG_percent, FT, FTA, FT_percent, ORB, DRB, TRB, AST, STL, BLK, TOV, PF, PTS])
            print(counter)
        print("-----------------")
        print("c= {}".format(counter))
    finally:
        c.close()

def insertIntoPlayerStats():
    c = connection.cursor()
    try:
        c.execute("INSERT into PlayerStats VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ["Curly Armstrong", "1950", "FTW", "G-F", "31", "63", "0", "0", "0", "0.368", "0", "0.467"])
        print("Inserted one row in PlayerStats")
    finally:
        c.close()

def getPlayersFrom_Specific_Year(teamID, year):
    c = connection.cursor()
    try:
        c.execute("SELECT Player.name, PlayerStats.pos, Player.height, Player.weight, Player.born, Player.birthCity, Player.birthState, Player.collage from PlayerStats JOIN Player ON PlayerStats.name = Player.name WHERE PlayerStats.teamID=%s AND PlayerStats.year=%s", [teamID, year])
        playerNames = c.fetchall()
        print("Fetched player names that played in {} for {}".format(year, teamID))
        return playerNames
    finally:
        c.close()


def getPlayer_Stats_From_Specific_Year_For_Specific_team(teamID, year, playerName):
    c = connection.cursor()
    try:
        c.execute("SELECT G, PTS, AST, TRB, STL, BLK, TOV, FG_percent, P3_percent, FT_percent, eFG_percent from PlayerStats WHERE name LIKE $$" + str(playerName) + "%$$ AND year=" + str(year) + " AND teamID='" + str(teamID) + "'")
        print("SELECT G, PTS, AST, TRB, STL, BLK, TOV, FG_percent, P3_percent, FT_percent, eFG_percent from PlayerStats WHERE name LIKE $$" + str(playerName) + "%$$ AND year=" + str(year) + " AND teamID='" + str(teamID) + "'")
        playerStats = c.fetchall()

        modified = []
        for i in range(len(playerStats[0])):
            if i in range(1, 7):
                modified.append(round(playerStats[0][i]/playerStats[0][0], 1))
            else:
                modified.append(playerStats[0][i])
        playerStats = [tuple(modified)]

        print("Fetched stats for {} who played in {} for {}".format(playerName, year, teamID))
        return playerStats
    finally:
        c.close()

def create_PlayerName_Year_index():
    c = connection.cursor()
    try:
        c.execute("CREATE INDEX idx_playerName_year ON PlayerStats(name, year)")
        print("Created index on PlayerStats(name, year)")
    finally:
        c.close()

def get_all_yearsAndTeam_a_player_played_for(playerName):
    c = connection.cursor()
    try:
        c.execute("select year, R.teamID, TeamInfo.team_name from (select year, teamID from PlayerStats WHERE name LIKE $$" + playerName + "%$$) AS R JOIN TeamInfo ON R.teamID=TeamInfo.team_id")
        years = c.fetchall()
        return years
    finally:
        c.close()

def getSomePlayerStats():
    c = connection.cursor()
    try:
        c.execute("select * from PlayerStats WHERE name=%s", ["Keith Van"])
        stats = c.fetchall()
        print(stats)
        return stats
    finally:
        c.close()


def createWhereCondition(attributes):
    """
    Creates the where portion of filtering conditions.
    (So far, can only be used reliably for PlayerStats,
     but, it should work for most tables.)

    :param attributes: dict
    :return: str

    NEEDS AGGREGATION
    """
    where = " WHERE "
    orderBy = ""
    if len(attributes):
        keys = []
        for key, value in attributes.items():
            key = key.split("/")  # split on space
            if len(key) == 1:
                per = ""
            else:
                per = key[1]
            key = key[0]

            if key in ("Pos", "name"):
                where += " " + key + " LIKE $$" + value + "%$$ "
                keys.append(key)
            elif key == "teamID":
                where = ", TeamInfo as t " + where
                where += " t.team_name LIKE $$" + value + "%$$ AND t.team_id = teamID "
                keys.append(key)
            elif key == "start_year":
                where += " year >= " + value + " "
            elif key == "end_year":
                where += " year <= " + value + " "
            elif per == "G":
                where += " " + key + " / G::numeric >= " + value + " "
                keys.append(key + " / G::numeric")
            elif per == "36":
                where += " " + key + " / MP::numeric * 36  >= " + value + " "
                keys.append(key + " / MP::numeric * 36")
            elif key != "csrfmiddlewaretoken" and key != "sort":
                where += " " + key + " >= " + value + " "
                keys.append(key)
            where += "AND"
            if key == "sort":
                where = where[:-3]
                if value == "TRUE":
                    orderBy += " ORDER BY "
        where = where[:-4] + orderBy
        if orderBy == " ORDER BY ":
            for key in keys:
                where += key + " DESC, "
            where = where[:-2] + ";"
        return where

def round_rows(rows):
    new_rows = []
    for row in rows:
        new_entry = []
        for entry in row:
            if isinstance(entry, float) or isinstance(entry, Decimal):
                entry = round(float(entry), 2)
            new_entry.append(entry)
        new_rows.append(tuple(new_entry))
    return new_rows


def filterPlayers(attributes):
    c = connection.cursor()
    try:
        select = """
        name, year, teamID, pos, age, G, GS, MP / G::numeric, PER, TS_percent,
        USG_percent, OWS, DWS, WS, OBPM / G::numeric, DBPM / G::numeric, BPM / G::numeric,
        VORP, FG_percent, P3_percent, P2_percent, eFG_percent, FT_percent, ORB / G::numeric,
        DRB / G::numeric, TRB / G::numeric, AST / G::numeric, STL / G::numeric,
        BLK / G::numeric, TOV / G::numeric, PF / G::numeric, PTS / G::numeric"""
        where = createWhereCondition(attributes)
        if where is None:
            c.execute("SELECT " + select + " FROM PlayerStats;")
        else:
            print("SELECT " + select + " FROM PlayerStats" + where)
            c.execute("SELECT " + select + " FROM PlayerStats" + where)
        rows = c.fetchall()
        rows = round_rows(rows)
        return rows
    finally:
        c.close()

def createPlayerScoreViews():
    c = connection.cursor()
    try:
        c.execute("DROP VIEW IF EXISTS PlayerScore;")
        playerScoreView = "CREATE VIEW PlayerScore AS" \
                          "    SELECT AVG(TRB / G::numeric) AS TRB," \
                          "           AVG(AST / G::numeric) AS AST, AVG(STL / G::numeric) AS STL," \
                          "           AVG(BLK / G::numeric) AS BLK, AVG(TOV / G::numeric) AS TOV," \
                          "           AVG(TS_percent) AS TS, AVG(MP) AS MP, name" \
                          "    FROM PlayerStats" \
                          "    GROUP BY name;"
        c.execute(playerScoreView)

        for pos in ["PG", "SG", "SF", "PF", "C"]:
            c.execute("DROP VIEW IF EXISTS Avg{}Score;".format(pos))
            averageScoreView = "CREATE VIEW Avg{}Score AS" \
                               "    SELECT AVG(TRB / G::numeric) AS TRB," \
                               "           AVG(AST / G::numeric) AS AST, AVG(STL / G::numeric) AS STL," \
                               "           AVG(BLK / G::numeric) AS BLK, AVG(TOV / G::numeric) AS TOV," \
                               "           AVG(TS_percent) AS TS, AVG(MP) AS MP" \
                               "    FROM PlayerStats" \
                               "    WHERE pos LIKE '%{}%' AND G > 10 AND MP / G::numeric > 10 " \
                               "          AND STL > 0 AND BLK > 0;".format(pos, pos)
            c.execute(averageScoreView)

    finally:
        c.close()