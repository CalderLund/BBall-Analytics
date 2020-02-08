from django.shortcuts import render, redirect

from .models import getGuestbookRows, insertIntoTeamInfo, insertIntoTeamStats, populateData, populateTeamStatsData, deleteAllTeams, deleteAllTeamStats, dropTeamsInfo, createTeamsInfo, createTeamStats, getTeamStats, countTeamStats, getAllteamsInAYear, countTeamsInAYear

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
        # populateTeamStatsData()
        # getTeamStats()
        teamsInfo = getGuestbookRows()
        # countTeamStats()
        # teamsInfo = []
    return render(request, "home.html", {"teamsInfo": teamsInfo})


def teamsInYear_view(request, year):
    print("-------YEAR = {}-------".format(year))
    teams = getAllteamsInAYear(year)
    countOfTeams = countTeamsInAYear(year)
    return render(request, "teamsInYear.html", {"year": year, "teams": teams, "countOfTeams": countOfTeams[0][0]})