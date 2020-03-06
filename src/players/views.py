from django.shortcuts import render, redirect

from .models import (createPlayerTable, dropTablePlayer, deleteAllRowsFromPlayer, populatePlayerData, getAllPlayers, createPlayerStatsTable,
dropTablePlayerStats, deleteAllRowsFromPlayerStats, populatePlayerStatsData, insertIntoPlayerStats, getSomePlayerStats)

# Create your views here.

def playerSetup(request):
    # createPlayerTable()
    # dropTablePlayer()
    # populatePlayerData()
    # deleteAllRowsFromPlayer()
    # getAllPlayers()
    # createPlayerStatsTable()
    # deleteAllRowsFromPlayerStats()
    # dropTablePlayerStats()
    # populatePlayerStatsData()
    # insertIntoPlayerStats()
    # getSomePlayerStats()
    print("Player View's playerSetup() function called.")
    return redirect("/")