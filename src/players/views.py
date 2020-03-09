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

def playerFiltering(request, json):
    """
    I don't know how you will deal with spaces.

    Example json:
    ?json={pos:SG,year_greater:2000,year_less:2010,FG_percent_greater:0.5,STL_percent_less:1.5}

    I process it to return a
    """
    vals = dict(json)

    # do stuff to filter players in players/models.py using vals
    # return query_result
    query_result = ()

    return render(request, "topplayers.html", {"query_result": query_result})
