from django.shortcuts import render, redirect
from .models import filterPlayers

from .models import (createPlayerTable, dropTablePlayer, deleteAllRowsFromPlayer, populatePlayerData, getAllPlayers, createPlayerStatsTable,
dropTablePlayerStats, deleteAllRowsFromPlayerStats, populatePlayerStatsData, insertIntoPlayerStats, getSomePlayerStats, 
getPlayersFrom_Specific_Year, getPlayer_Stats_From_Specific_Year_For_Specific_team)

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
    # convert to dictionary
    vals = dict(json)

    # do stuff to filter players in players/models.py using vals
    # return query_result
    query_result = filterPlayers(vals)

    return render(request, "topplayers.html", {"query_result": query_result})


def playerInfo_view(request, tmId, tmName, year):
    player_stats = getPlayersFrom_Specific_Year(tmId, year)
    modified_player_stats = []
    for stats in player_stats:
        new_stats = list(stats)
        if stats[5] == "NaN" and stats[6] == "NaN":
            new_stats[5] = "N/A"
            new_stats[6] = ""
        elif stats[5] == "NaN":
            new_stats[5] = ""
        elif stats[6] == "NaN":
            new_stats[6] = ""
        else:
            new_stats[5] = stats[5] + ","
        modified_stats = tuple(new_stats)
        modified_player_stats.append(modified_stats)
    return render(request, "playersStatsInYear.html", {"tmId": tmId, "tmName": tmName, "year": year, "player_stats": modified_player_stats})

def playerStats_view(request, tmId, tmName, year, playerName):
    player_stats = getPlayer_Stats_From_Specific_Year_For_Specific_team(tmId, year, playerName)
    return render(request, "playerInfoFromAYear.html", {"tmId": tmId, "tmName": tmName, "year": year, "playerName": playerName, "player_stats": player_stats})

