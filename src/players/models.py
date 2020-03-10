from django.db import models
from django.db import connection

import pandas as pd
import math
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
        c.execute("SELECT G, PTS, AST, FG, FG_percent, FT, FT_percent, eFG_percent from PlayerStats WHERE name=%s AND year=%s AND teamID=%s", [playerName, year, teamID])
        playerStats = c.fetchall()
        print("Fetched stats for {} who played in {} for {}".format(playerName, year, teamID))
        return playerStats
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
    where = ""
    if len(attributes):
        for key, value in attributes:
            '''
            # THIS CODE IS IGNORED FOR NOW. EVENTUALLY WE WILL WANT MORE FUNCTIONALITY.
            if key.endswith("_greater"):
                key = key.strip("_greater")
                # probably need error checking here
                where += key + " >= " + value + ", "
            elif key.endswith("_less"):
                key = key.strip("_less")
                # probably need error checking here
                where += key + " < " + value + ", "
            elif key in ("name", "teamID", "pos"):
                where += key + " == '" + value + "', "
            else:
                where += key + " == " + value + ", "
            '''
            if key == "Pos":
                values = value.split("-")
                if len(values) == 2:
                    where += "(Pos == '" + values[0] + "' OR Pos == '" + values[1] + \
                             "' OR Pos == '" + value + "') AND "
                if len(values) == 1:
                    where += "Pos == '" + values[0] + "' AND "
            elif key in ("name", "teamID"):
                where += key + " == '" + value + "' AND "
            else:
                where += key + " < " + value + " AND "

        where = where[:-5] + ";"
        return where

def filterPlayers(attributes):
    c = connection.cursor()
    try:
        where = createWhereCondition(attributes)
        if where is None:
            rows = c.execute("SELECT * from PlayerStats;")
        else:
            rows = c.execute("SELECT * from PlayerStats WHERE " + where)
        rows = c.fetchall()
        return rows
    finally:
        c.close()