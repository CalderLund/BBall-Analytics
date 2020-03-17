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
        print("Account table created.")
    finally:
        c.close()


def dropTableAccount():
    c = connection.cursor()
    try:
        c.execute("DROP TABLE Account")
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

def getAllAccounts():
    c = connection.cursor()
    try:
        c.execute("SELECT * from Account")
        all_Accounts = c.fetchall()
        print("Fetched all rows from Account")
        return all_Accounts
    finally:
        c.close()