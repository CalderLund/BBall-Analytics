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

def topplayers_view(request):
    if request.method == "POST":
        print(request.POST)
      #  return render(request, "/players/player_select_result")

    return render(request, "topplayers.html")

def player_select_result_view(request):
    return render(request, "player_select_result.html")