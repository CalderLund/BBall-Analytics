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

def topplayers_view(request):

    if request.method == "POST":
        input_value = request.POST.copy()
        input_value.pop('csrfmiddlewaretoken', None)
        length = len(input_value) - 2
        print(input_value)
        query_result = filterPlayers(input_value)
        input_value.pop('start_year', None)
        input_value.pop('end_year', None)
        print(query_result)

        return render(request, "player_select_result.html", {"query_result": query_result,
                                                             "attributes": input_value,
                                                             "column_num": range(length)})

    return render(request, "topplayers.html")

def player_select_result_view(request):
    return render(request, "player_select_result.html")

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
