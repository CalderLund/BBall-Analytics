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

def getAllUsers_And_Their_FavouriteTeams():
    c = connection.cursor()
    try:
        c.execute("SELECT Account.uid, username, team_id, TeamInfo.team_name from (FavouriteTeam NATURAL JOIN Account) NATURAL JOIN TeamInfo")
        users_favouriteTeams = c.fetchall()
        print("Fetched all users and their favourite teams from FavouriteTeam, Account & TeamInfo")
        return users_favouriteTeams
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