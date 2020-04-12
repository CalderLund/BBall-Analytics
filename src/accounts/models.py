from django.db import models
from django.db import connection
from django.db import IntegrityError
from django.shortcuts import render, redirect


# Create your models here.

def createAccountTable():
    createAccountTableString = """
    CREATE TABLE Account
    (
        uid SERIAL NOT NULL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(50) NOT NULL
    )
    """
    c = connection.cursor()
    try:
        c.execute(createAccountTableString)
        print("Account Table created.")
    finally:
        c.close()


def dropTableAccount():
    c = connection.cursor()
    try:
        c.execute("DROP TABLE Account CASCADE")
        print("Account Table Dropped!")
    finally:
        c.close()

def deleteAllRowsFromAccount():
    c = connection.cursor()
    try:
        c.execute("DELETE from Account")
        print("Deleted All rows from Account")
    finally:
        c.close()

def insertIntoAccount(username, password):
    c = connection.cursor()
    try:
        c.execute("INSERT INTO Account (username, password) VALUES (%s, %s)", [username, password])
        print("Inserted one row into Account")
    finally:
        c.close()

def get_latest_Uid():
    c = connection.cursor()
    try:
        c.execute("SELECT MAX(uid) from Account")
        print("Fetched the latest uid from Account")
        return c.fetchall()
    finally:
        c.close()

def getAllAccounts():
    c = connection.cursor()
    try:
        c.execute("SELECT * from Account")
        all_Accounts = c.fetchall()
        print("Fetched all rows from Account")
        return all_Accounts
    finally:
        c.close()

def createFavouriteTeamTable():
    createFavouriteTeamTableString = """
    CREATE TABLE FavouriteTeam
    (
        team_id VARCHAR(3) NOT NULL,
        uid INT NOT NULL,
        yr INT,
        FOREIGN KEY(team_id) REFERENCES TeamInfo(team_id) ON DELETE CASCADE,
        FOREIGN KEY(uid) REFERENCES Account(uid) ON DELETE CASCADE,
        PRIMARY KEY(team_id, uid)
    )
    """
    c = connection.cursor()
    try:
        c.execute(createFavouriteTeamTableString)
        print("FavouriteTeam table created.")
    finally:
        c.close()

def insertIntoFavouriteTeam(team_id, uid, yr):
    c = connection.cursor()
    try:
        if yr == -1:
            c.execute("INSERT INTO FavouriteTeam VALUES (%s, %s)", [team_id, uid])
        else:
            c.execute("INSERT INTO FavouriteTeam VALUES (%s, %s, %s)", [team_id, uid, yr])
        print("Inserted one row into FavouriteTeam")
    except IntegrityError as e:
        redirect("/accounts/all")
    finally:
        c.close()

def dropTableFavouriteTeam():
    c = connection.cursor()
    try:
        c.execute("DROP TABLE FavouriteTeam")
        print("FavouriteTeam Table Dropped!")
    finally:
        c.close()

def deleteAllRowsFromFavouriteTeam():
    c = connection.cursor()
    try:
        c.execute("DELETE from FavouriteTeam")
        print("Deleted All rows from FavouriteTeam")
    finally:
        c.close()

def getAllFavouriteTeamRows():
    c = connection.cursor()
    try:
        c.execute("SELECT * from FavouriteTeam")
        all_Accounts = c.fetchall()
        print("Fetched all rows from FavouriteTeam")
        return all_Accounts
    finally:
        c.close()

def get_A_Given_Users_FavouriteTeam(uid):
    c = connection.cursor()
    try:
        c.execute("SELECT TeamInfo.team_name from (FavouriteTeam NATURAL JOIN (SELECT uid from Account WHERE uid={}) AS R_subquery) AS R1 NATURAL JOIN TeamInfo".format(uid))
        favouriteTeam = c.fetchall()
        print("Fetched user's favourite team")
        return favouriteTeam
    finally:
        c.close()


def createFavouritePlayerTable():
    createFavouritePlayerTableString = """
    CREATE TABLE FavouritePlayer
    (
        name VARCHAR(100) NOT NULL,
        uid INT NOT NULL,
        FOREIGN KEY(name) REFERENCES Player(name) ON DELETE CASCADE,
        FOREIGN KEY(uid) REFERENCES Account(uid) ON DELETE CASCADE,
        PRIMARY KEY(name, uid)
    )
    """
    c = connection.cursor()
    try:
        c.execute(createFavouritePlayerTableString)
        print("FavouritePlayer table created.")
    finally:
        c.close()

def dropTableFavouritePlayer():
    c = connection.cursor()
    try:
        c.execute("DROP TABLE FavouritePlayer")
        print("FavouritePlayer Table Dropped!")
    finally:
        c.close()

def deleteAllRowsFromFavouritePlayer():
    c = connection.cursor()
    try:
        c.execute("DELETE from FavouritePlayer")
        print("Deleted All rows from FavouritePlayer")
    finally:
        c.close()

def insertIntoFavouritePlayer(name, uid):
    c = connection.cursor()
    try:
        c.execute("INSERT INTO FavouritePlayer VALUES ((SELECT DISTINCT name FROM Player WHERE name LIKE $$" + str(name) + "%$$), " + str(uid) + ")")
        print("Inserted one row into FavouritePlayer")
    except IntegrityError as e:
        # redirect("/accounts/all")
        print(e)
    finally:
        c.close()

def getAllUsers_And_Their_FavouriteTeams():
    c = connection.cursor()
    try:
        c.execute("SELECT Account.uid, username, team_id, TeamInfo.team_name,\
                   FavouritePlayer.name, FantasyTeam.fantasy_team_name \
                   from (((FavouriteTeam NATURAL JOIN Account) NATURAL JOIN TeamInfo) \
                   NATURAL JOIN FavouritePlayer) NATURAL JOIN FantasyTeam")
        users_favouriteTeams = c.fetchall()
        print("Fetched all users and their favourite teams from FavouriteTeam, Account & TeamInfo")
        return users_favouriteTeams
    finally:
        c.close()

def get_password_for_uid(uid):
    c = connection.cursor()
    try:
        c.execute("SELECT password from Account WHERE uid=%s", [uid])
        pswd = c.fetchall()
        print("Fetched password from Account")
        return pswd[0][0]
    finally:
        c.close()

def deleteAccount(uid):
    c = connection.cursor()
    try:
        c.execute("DELETE from Account WHERE uid=%s", [uid])
        print("Deleted one row from Account")
    finally:
        c.close()

def updateAccount_fav_team(uid, fav_team):
    c = connection.cursor()
    try:
        c.execute("UPDATE FavouriteTeam SET team_id=%s WHERE uid=%s", [fav_team, uid])
        print("Updated team_id of one row from FavouriteTeam")
    finally:
        c.close()

def updateAccount_fav_player(uid, fav_player):
    c = connection.cursor()
    try:
        c.execute("UPDATE FavouritePlayer SET name=(SELECT DISTINCT name FROM Player WHERE name LIKE $$" + str(fav_player) + "%$$) WHERE uid=" + str(uid))
        print("Updated name of one row from FavouritePlayer")
    except IntegrityError as e:
        redirect("/accounts/all")
    finally:
        c.close()


# Code for fantasy team
def createFantasyTeamTable():
    createFantasyTeamTableString = """
    CREATE TABLE FantasyTeam
    (
        uid INT NOT NULL,
        fantasy_team_name VARCHAR(50),
        FOREIGN KEY(uid) REFERENCES Account(uid) ON DELETE CASCADE,
        PRIMARY KEY(uid)
    )
    """
    c = connection.cursor()
    try:
        c.execute(createFantasyTeamTableString)
        print("FantasyTeam table created.")
    finally:
        c.close()

def insertIntoFantasyTeam(uid, fantasy_team_name):
    c = connection.cursor()
    try:
        if (fantasy_team_name is None):
            c.execute("INSERT INTO FantasyTeam VALUES (%s, NULL)", [uid])
        else:
            c.execute("INSERT INTO FantasyTeam VALUES (%s, %s)", [uid, fantasy_team_name])
        print("Inserted one row into FantasyTeam")
    finally:
        c.close()

def updateFantasyTeam(uid, fantasy_team_name):
    c = connection.cursor()
    try:
        c.execute("UPDATE FantasyTeam SET fantasy_team_name=%s WHERE uid=%s", [fantasy_team_name, uid])
        print("Updated fantasy_team_name of one row from FantasyTeam")
    finally:
        c.close()

def deleteFantasyTeam(uid, fantasy_team_name):
    c = connection.cursor()
    try:
        c.execute("DELETE from FantasyTeam WHERE uid=%s AND fantasy_team_name=%s", [uid, fantasy_team_name])
        print("Deleted one row from FantasyTeam")
    finally:
        c.close()

def createFantasyIsMemTable():
    createFantasyIsMemTableString = """
    CREATE TABLE FantasyIsMem
    (
        uid INT NOT NULL,
        name VARCHAR(50) NOT NULL,
        pos VARCHAR(50) NOT NULL,
        FOREIGN KEY(uid) REFERENCES FantasyTeam(uid) ON DELETE CASCADE,
        FOREIGN KEY(name) REFERENCES Player(name) ON DELETE CASCADE,
        PRIMARY KEY(uid, name)
    )
    """
    c = connection.cursor()
    try:
        c.execute(createFantasyIsMemTableString)
        print("FantasyTeam table created.")
    finally:
        c.close()

def insertIntoFantasyIsMem(uid, player_name, pos):
    c = connection.cursor()
    try:
        c.execute("INSERT INTO FantasyIsMem VALUES (" + str(uid) + ", (SELECT DISTINCT name FROM Player WHERE name LIKE $$" + str(player_name) + "%$$), '" + str(pos) + "')")
        print("Inserted one row into FantasyIsMem")
    finally:
        c.close()

def updateFantasyIsMem(uid, player_name, pos):
    c = connection.cursor()
    try:
        c.execute("SELECT pos FROM FantasyIsMem WHERE uid=" + str(uid))
        positions = c.fetchall()[0]
        if pos in positions:
            c.execute("UPDATE FantasyIsMem SET name=(SELECT DISTINCT name FROM Player WHERE name LIKE $$" + str(player_name) + "%$$) WHERE uid=" + str(uid) + " AND pos='" + str(pos) + "'")
            print("Updated one player from FantasyIsMem")
        else:
            insertIntoFantasyIsMem(uid, player_name, pos)
    finally:
        c.close()

# Extract season stats for all players for the given uid and fantasy_team_name
def getFantasyPlayerStats(uid, fantasy_team_name):
    c = connection.cursor()
    try:
        c.execute("SELECT DISTINCT * From FantasyTeam, FantasyIsMem, Player \
                   WHERE FantasyTeam.fantasy_team_name = FantasyIsMem.fantasy_team_name AND \
                         FantasyIsMem.name LIKE CONCAT('%', Player.name, '%') AND \
                         uid=" + str(uid) + " AND fantasy_team_name='" + fantasy_team_name + "'")
        print("Extract player stats for fantasy team {0} created by user {1}".format(fantasy_team_name, uid))
        return c.fetchall()
    finally:
        c.close()

# Extract a list of fantasy team name created by a specified user
def getFantasyTeam(uid):
    c = connection.cursor()
    try:
        c.execute('SELECT fantasy_team_name From FantasyTeam WHERE uid=%s', [uid])
        print("Extract Fantasy team info for user {0}".format(uid))
        return c.fetchall()
    finally:
        c.close()

def getFantasyPlayers(uid):
    c = connection.cursor()
    try:
        c.execute('SELECT name, pos \
                   FROM (FantasyTeam NATURAL JOIN FantasyIsMem) \
                   WHERE uid=%s', [uid])
        content = c.fetchall()
        return content
    finally:
        c.close()

def findUsageOrder(teamScores, positions = {"PG", "SG", "SF", "PF", "C"}):
    if not positions:
        return []
    maxi = -1000000
    first = ""
    for pos in positions:
        if teamScores[pos]["TS_percent"] > maxi:
            maxi = teamScores[pos]["TS_percent"]
            first = pos
    return [first] + findUsageOrder(teamScores, positions - {first})


def weightScores(teamScores):
    weights = {"PG": {'TRB':0.4, 'AST':1.2, 'STL':0.9, 'BLK':0.5, 'TOV':0.75, 'TS_percent':40},
               "SG": {'TRB':0.3, 'AST':1, 'STL':0.8, 'BLK':0.5, 'TOV':0.7, 'TS_percent':40},
               "SF": {'TRB':0.5, 'AST':0.7, 'STL':0.7, 'BLK':0.7, 'TOV':0.65, 'TS_percent':40},
               "PF": {'TRB':1, 'AST':0.4, 'STL':0.4, 'BLK':1, 'TOV':0.6, 'TS_percent':40},
               "C":  {'TRB':1.5, 'AST':0.4, 'STL':0.3, 'BLK':1.1, 'TOV':0.5, 'TS_percent':40}}

    total = {"Shooting":0, "Passing":0, "Rebounding":0, "Defense":0, "Overall":0}
    for pos in ["PG", "SG", "SF", "PF", "C"]:
        for attr in ["TRB", "AST", "STL", "BLK", "TOV", "TS_percent"]:
            teamScores[pos][attr] *= weights[pos][attr]
        total["Passing"]    += teamScores[pos]["AST"] - teamScores[pos]["TOV"]
        total["Rebounding"] += teamScores[pos]["TRB"]
        total["Defense"]    += teamScores[pos]["STL"] + teamScores[pos]["BLK"]

    usageOrder = findUsageOrder(teamScores)
    total["Shooting"] += teamScores[usageOrder[0]]["TS_percent"] * 0.3
    total["Shooting"] += teamScores[usageOrder[1]]["TS_percent"] * 0.25
    total["Shooting"] += teamScores[usageOrder[2]]["TS_percent"] * 0.2
    total["Shooting"] += teamScores[usageOrder[3]]["TS_percent"] * 0.15
    total["Shooting"] += teamScores[usageOrder[4]]["TS_percent"] * 0.1
    total["Shooting"] *= 5

    grades = {}
    overall = 0
    for cat in ("Shooting", "Passing", "Rebounding", "Defense"):
        if total[cat] > 10:
            grades[cat] = "A+"
            overall += 0.25 * 100
        elif total[cat] > 7:
            grades[cat] = "A"
            overall += 0.25 * 96
        elif total[cat] > 5:
            grades[cat] = "A-"
            overall += 0.25 * 92
        elif total[cat] > 3:
            grades[cat] = "B+"
            overall += 0.25 * 89
        elif total[cat] > 1:
            grades[cat] = "B"
            overall += 0.25 * 86
        elif total[cat] > -1:
            grades[cat] = "B-"
            overall += 0.25 * 82
        elif total[cat] > -3:
            grades[cat] = "C+"
            overall += 0.25 * 79
        elif total[cat] > -5:
            grades[cat] = "C"
            overall += 0.25 * 76
        elif total[cat] > -7:
            grades[cat] = "C-"
            overall += 0.25 * 72
        elif total[cat] > -9:
            grades[cat] = "D+"
            overall += 0.25 * 69
        elif total[cat] > -11:
            grades[cat] = "D"
            overall += 0.25 * 66
        elif total[cat] > -14:
            grades[cat] = "D-"
            overall += 0.25 * 62
        else:
            grades[cat] = "F"
            overall += 0.25 * 32

    if overall > 95:
        grades["Overall"] = "A+"
    elif overall > 90:
        grades["Overall"] = "A"
    elif overall > 85:
        grades["Overall"] = "B+"
    elif overall > 80:
        grades["Overall"] = "B"
    elif overall > 75:
        grades["Overall"] = "C+"
    elif overall > 70:
        grades["Overall"] = "C"
    elif overall > 65:
        grades["Overall"] = "D+"
    elif overall > 60:
        grades["Overall"] = "D"
    else:
        grades["Overall"] = "F"

    return grades


def evaluateScore(team):
    c = connection.cursor()
    try:
        teamScores = {}
        for pos in ["PG", "SG", "SF", "PF", "C"]:
            player = team[pos]
            c.execute("SELECT * FROM PlayerScore WHERE name LIKE $$" + player + "%$$")
            playerAverages = c.fetchall()[0]

            c.execute("SELECT * FROM Avg{}Score".format(pos))
            positionAverages = c.fetchall()[0]

            playerVsPos = {}
            for i, attr in enumerate(["TRB", "AST", "STL", "BLK", "TOV", "TS_percent", "MP"]):
                if float(playerAverages[i]) > 0:
                    playerVsPos[attr] = float(playerAverages[i]) - float(positionAverages[i])
                else:
                    playerVsPos[attr] = 0

            teamScores[pos] = playerVsPos

        teamGrades = weightScores(teamScores)
        return teamGrades

    finally:
        c.close()
