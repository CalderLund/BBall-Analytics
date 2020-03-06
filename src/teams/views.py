from django.shortcuts import render, redirect

from .models import (getGuestbookRows, insertIntoTeamInfo, insertIntoTeamStats, populateData, populateTeamStatsData, deleteAllTeams, deleteAllTeamStats, dropTeamsInfo, createTeamsInfo, createTeamStats, getTeamStats, countTeamStats, getAllteamsInAYear, countTeamsInAYear,
dropTeamStats, getAllYearsOfATeam, getTeamInfoFromAYear)

# Create your views here.

def home_view(request):
    if request.method=="POST":
        print(request.POST["year"])
        year = request.POST["year"]
        return redirect("teams/year/{}".format(year))
    else:
        # createTeamsInfo()
        # populateData()
        # insertIntoTeamInfo()
        # deleteAllTeams()
        # dropTeamsInfo()
        # createTeamStats()
        # insertIntoTeamStats()
        # getTeamStats()
        # deleteAllTeamStats()
        # dropTeamStats()
        # populateTeamStatsData()
        teamsInfo = getGuestbookRows()
        # countTeamStats()
        # teamsInfo = []
    return render(request, "home.html", {"teamsInfo": teamsInfo})


def teamsInYear_view(request, year):
    print("-------YEAR = {}-------".format(year))
    teams = getAllteamsInAYear(year)
    countOfTeams = countTeamsInAYear(year)
    return render(request, "teamsInYear.html", {"year": year, "teams": teams, "countOfTeams": countOfTeams[0][0]})


def yearsOfATeam_view(request, tmId, tmName):
    years = getAllYearsOfATeam(tmId)
    print("Team Name: {}".format(tmName))
    print("Team Id: {}".format(tmId))
    print(years)
    return render(request, "yearsOfATeam.html", {"years": years, "teamName": tmName, "tmId": tmId})

def teamInfoInYear_view(request, tmId, tmName, year):
    teamInfo = getTeamInfoFromAYear(tmId, year)
    print("Team Name: {}".format(tmName))
    print("Team Id: {}".format(tmId))
    print("In Year: {}".format(year))
    return render(request, "teamInfoInYear.html", {"year": year, "teamName": tmName, "tmId": tmId, "teamInfo": teamInfo})