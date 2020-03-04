from django.db import models
from django.db import connection

import pandas as pd
# from .Data import basketball_teams.csv

def populateData():
    teams = pd.read_csv("teams/basketball_teams.csv")
    unique_teams = teams.drop_duplicates(["tmID"])
    counter = 0
    c = connection.cursor()
    try:
        for index,row in unique_teams.iterrows():
            counter += 1
            c.execute("INSERT into TeamInfo VALUES (%s, %s)", [row["tmID"], row["name"]])
            # print(row["tmID"], row["name"])
        print("-----------------")
        print("c= {}".format(counter))
    finally:
        c.close()

def populateTeamStatsData():
    teams = pd.read_csv("teams/basketball_teams.csv")
    counter = 0
    c = connection.cursor()
    try:
        for index,row in teams.iterrows():
            counter += 1
            c.execute("INSERT into TeamStats VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [row["year"], row["tmID"], row["rank"], row["confRank"], row["playoff"], row["o_fgm"], row["o_fga"], row["o_ftm"], row["o_fta"], row["o_3pm"], row["o_3pa"], row["o_oreb"], row["o_dreb"], row["o_reb"], row["o_asts"], row["o_pf"], row["o_stl"], row["o_to"], row["o_blk"], row["o_pts"], row["d_fgm"], row["d_fga"], row["d_ftm"], row["d_fta"], row["d_3pm"], row["d_3pa"], row["d_oreb"], row["d_dreb"], row["d_reb"], row["d_asts"], row["d_pf"], row["d_stl"], row["d_to"], row["d_blk"], row["d_pts"], row["o_tmRebound"], row["d_tmRebound"], row["homeWon"], row["homeLost"], row["awayWon"], row["awayLost"], row["neutWon"], row["neutLoss"], row["confWon"], row["confLoss"], row["divWon"], row["divLoss"], row["pace"], row["won"], row["lost"], row["games"]])
            # print(row["tmID"], row["name"])
        print("-----------------")
        print("c= {}".format(counter))
    finally:
        c.close()


def deleteAllTeams():
    c = connection.cursor()
    try:
        c.execute("DELETE from TeamInfo")
        print("Deleted TeamInfo")
    finally:
        c.close()

def deleteAllTeamStats():
    c = connection.cursor()
    try:
        c.execute("DELETE from TeamStats")
        print("Deleted TeamStats")
    finally:
        c.close()

def insertIntoTeamInfo():
    c = connection.cursor()
    try:
        c.execute("INSERT into TeamInfo VALUES (%s, %s)", ["pqr", "Test Team 3"])
        print("Inserted TeamInfo")
    finally:
        c.close()

def insertIntoTeamStats():
    c = connection.cursor()
    try:
        c.execute("INSERT into TeamStats VALUES (%s, %s)", ["2020", "BOS"])
        print("Inserted TeamStats")
    finally:
        c.close()

def dropTeamsInfo():
    c = connection.cursor()
    try:
        c.execute("DROP TABLE TeamInfo")
        print("Dropped!")
    finally:
        c.close()

def createTeamsInfo():
    c = connection.cursor()
    try:
        createTeamTable = """
        CREATE TABLE TeamInfo
(
    team_id VARCHAR(3) NOT NULL PRIMARY KEY,
    team_name VARCHAR(50)
)
        """

        c.execute(createTeamTable)
    finally:
        c.close()

def dropTeamStats():
    c = connection.cursor()
    try:
        c.execute("DROP TABLE TeamStats")
        print("Dropped!")
    finally:
        c.close()

def createTeamStats():
    c = connection.cursor()
    try:
        createTeamStatsTable = """
        CREATE TABLE TeamStats
(
    yr INT NOT NULL,
    team_id VARCHAR(3) NOT NULL,
    tm_rank INT,
    confRank INT,
    playoff VARCHAR(3),
    o_fgm INT,
    o_fga INT,
    o_ftm INT,
    o_fta INT,
    o_3pm INT,
    o_3pa INT,
    o_oreb INT,
    o_dreb INT,
    o_reb INT,
    o_asts INT,
    o_pf INT,
    o_stl INT,
    o_to INT,
    o_blk INT,
    o_pts INT,
    d_fgm INT,
    d_fga INT,
    d_ftm INT,
    d_fta INT,
    d_3pm INT,
    d_3pa INT,
    d_oreb INT,
    d_dreb INT,
    d_reb INT,
    d_asts INT,
    d_pf INT,
    d_stl INT,
    d_to INT,
    d_blk INT,
    d_pts INT,
    o_tmRebound INT,
    d_tmRebound INT,
    homeWon INT,
    homeLost INT,
    awayWon INT,
    awayLost INT,
    neutWon INT,
    neutLoss INT,
    confWon INT,
    confLoss INT,
    divWon INT,
    divLoss INT,
    pace INT,
    won INT,
    lost INT,
    games INT,
    PRIMARY KEY(yr, team_id),
    FOREIGN KEY(team_id) REFERENCES TeamInfo(team_id)
)
        """

        c.execute(createTeamStatsTable)
    finally:
        c.close()

def getGuestbookRows():
    # print(connection.cursor)
    c = connection.cursor()
    try:
        rows = c.execute("SELECT * from TeamInfo")
        rows = c.fetchall()
        # print(rows)
        return rows
    finally:
        c.close()

def getTeamStats():
    # print(connection.cursor)
    c = connection.cursor()
    try:
        rows = c.execute("SELECT * from TeamStats")
        rows = c.fetchall()
        # print(rows)
        return rows
    finally:
        c.close()

def countTeamStats():
    c = connection.cursor()
    try:
        rows = c.execute("SELECT count(*) from TeamStats")
        rows = c.fetchall()
        print("No. of Team Stats = {}".format(rows))
    finally:
        c.close()


def getAllteamsInAYear(year):
    c = connection.cursor()
    try:
        rows = c.execute("SELECT TeamInfo.team_id, team_name, yr from TeamInfo NATURAL JOIN TeamStats WHERE yr={}".format(year))
        rows = c.fetchall()
        print(rows)
        return rows
    finally:
        c.close()

def countTeamsInAYear(year):
    c = connection.cursor()
    try:
        rows = c.execute("SELECT count(*) from (SELECT TeamInfo.team_id, team_name, yr from TeamInfo NATURAL JOIN TeamStats WHERE yr={}) AS R".format(year))
        rows = c.fetchall()
        print(rows)
        return rows
    finally:
        c.close()

def getAllYearsOfATeam(tmId):
    c = connection.cursor()
    try:
        years = c.execute("SELECT yr from TeamStats WHERE team_id='{}'".format(tmId))
        years = c.fetchall()
        print("Fetched all years for team {}".format(tmId))
        return years
    finally:
        c.close()

def getTeamInfoFromAYear(tmId, year):
    c = connection.cursor()
    try:
        teamInfo = c.execute("SELECT tm_rank, won, lost, games, homeWon, homeLost, awayWon, awayLost, neutWon, neutLoss from TeamStats WHERE team_id='{}' AND yr='{}'".format(tmId, year))
        teamInfo = c.fetchall()
        print("Fetched team info for {} from {}".format(tmId, year))
        return teamInfo
    finally:
        c.close() 