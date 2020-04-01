from django.db import models
from django.db import connection

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
        c.execute("INSERT INTO FavouritePlayer VALUES (%s, %s)", [name, uid])
        print("Inserted one row into FavouritePlayer")
    finally:
        c.close()

def getAllUsers_And_Their_FavouriteTeams():
    c = connection.cursor()
    try:
        c.execute("SELECT Account.uid, username, team_id, TeamInfo.team_name, FavouritePlayer.name from ((FavouriteTeam NATURAL JOIN Account) NATURAL JOIN TeamInfo) NATURAL JOIN FavouritePlayer")
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
        c.execute("UPDATE FavouritePlayer SET name=%s WHERE uid=%s", [fav_player, uid])
        print("Updated name of one row from FavouritePlayer")
    finally:
        c.close()


# Code for fantasy team
def createFantasyTeamTable():
    createFantasyTeamTableString = """
    CREATE TABLE FantasyTeam
    (
        uid INT NOT NULL,
        fantasy_team_name VARCHAR(50) NOT NULL,
        FOREIGN KEY(uid) REFERENCES Account(uid) ON DELETE CASCADE,
        PRIMARY KEY(uid, fantasy_team_name)
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
        c.execute("INSERT INTO FantasyTeam VALUES (%s, %s)", [uid, fantasy_team_name])
        print("Inserted one row into FantasyTeam")
    finally:
        c.close()

def updateFatasyTeam(uid, fantasy_team_name):
    c = connection.cursor()
    try:
        c.execute("UPDATE FantasyTeam SET fantasy_team_name=%s WHERE uid=%s", [fantasy_team_name, uid])
        print("Updated fantasy_team_name of one row from FantasyTeam")
    finally:
        c.close()

def deleteFantasyTeam(uid, fantasy_team_name):
    c = connection.cursor()
    try:
        c.execute("DELETE from Account WHERE uid=%s AND fantasy_team_name=%s", [uid, fantasy_team_name])
        print("Deleted one row from FantasyTeam")
    finally:
        c.close()

def createFantasyIsMemTable():
    createFantasyIsMemTableString = """
    CREATE TABLE FantasyIsMem
    (
        uid INT NOT NULL,
        fantasy_team_name VARCHAR(50) NOT NULL,
        name VARCHAR(50) NOT NULL,
        pos VARCHAR(50) NOT NULL,
        FOREIGN KEY(uid, fantasy_team_name) REFERENCES FantasyTeam(uid, fantasy_team_name) ON DELETE CASCADE,
        FOREIGN KEY(name) REFERENCES Player(name) ON DELETE CASCADE,
        PRIMARY KEY(uid, fantasy_team_name, player_name)
    )
    """
    c = connection.cursor()
    try:
        c.execute(createFantasyTeamTableString)
        print("FantasyTeam table created.")
    finally:
        c.close()

def insertIntoFantasyIsMem(uid, fantasy_team_name, player_name, pos):
    c = connection.cursor()
    try:
        c.execute("INSERT INTO FantasyIsMem VALUES (%s, %s, %s, %s)", [uid, fantasy_team_name, player_name, pos])
        print("Inserted one row into FantasyIsMem")
    finally:
        c.close()

def updateFatasyIsMem(uid, fantasy_team_name, player_name, pos):
    c = connection.cursor()
    try:
        c.execute("UPDATE FantasyIsMem SET name=%s WHERE uid=%s AND fantasy_team_name=%s AND pos=%s", [player_name, uid, fantasy_team_name, pos])
        print("Updated one player from FantasyIsMem")
    finally:
        c.close()

def getFantasyPlayerStats(uid, fantasy_team_name):
    c = connection.cursor()
    try:
        c.execute('SELECT * From FantasyTeam, FantasyIsMem, Player WHERE uid=%s AND fantasy_team_name=%s', [uid, fantasy_team_name])
        print("Extract player stats for fantasy team {0} created by user {1}".format(fantasy_team_name, uid))
        return c.fetchall()
    finally:
        c.close()

def getFantasyTeam(uid):
    c = connection.cursor()
    try:
        c.execute('SELECT  From FantasyTeam WHERE uid=%s', [uid])
        print("Extract Fantasy team info for user {0}".format(uid))
        return c.fetchall()
    finally:
        c.close()
