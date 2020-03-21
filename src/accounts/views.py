from django.shortcuts import render, redirect

from .models import (createAccountTable, dropTableAccount, deleteAllRowsFromAccount, insertIntoAccount, getAllAccounts, get_latest_Uid,
createFavouriteTeamTable, insertIntoFavouriteTeam, dropTableFavouriteTeam, deleteAllRowsFromFavouriteTeam, getAllUsers_And_Their_FavouriteTeams,
get_A_Given_Users_FavouriteTeam, getAllFavouriteTeamRows)

# Create your views here.


def accountSetup(request):
    # deleteAllRowsFromAccount()
    # dropTableAccount()
    # createAccountTable()
    # print("All FavouriteTeams:")
    # print(getAllFavouriteTeamRows())
    # deleteAllRowsFromFavouriteTeam()
    # dropTableFavouriteTeam()
    # createFavouriteTeamTable()
    # print("Account View's accountSetup() function called.")
    return redirect("/")

def create_account_view(request):
    print("CREATE ACCOUNT VIEW")
    if request.method == "POST":
        print(request.POST["username"])
        print(request.POST["password"])
        username = request.POST["username"]
        insertIntoAccount(request.POST["username"], request.POST["password"])
        uid_list = get_latest_Uid()
        uid = uid_list[0][0]
        print(uid)
        return render(request, "account_initialize_details.html", {"username": username, "uid": uid})
    return render(request, "create_account_form.html", {})

def account_details(request, uid, username):
    print("UID: {}".format(uid))
    # print(request)
    if request.method == "POST":
        print(request.POST["team"])
        # For now, year will not be inserted into the "FavouriteTeam" table since I'm not sure where to get this year value from :(
        yr = -1
        insertIntoFavouriteTeam(request.POST["team"], uid, yr)
        favouriteTeam = get_A_Given_Users_FavouriteTeam(uid)[0][0]
        return render(request, "account_details.html", {"uid": uid, "username": username, "tmId": request.POST["team"],  "favouriteTeam": favouriteTeam})
    return redirect("/")

def already_know_account_details(request, uid, username, tmId, tmName):
    return render(request, "account_details.html", {"uid": uid, "username": username, "tmId": tmId, "favouriteTeam": tmName})

def all_accounts_view(request):
    # favouriteTeams is a list of tuples
    # each tuple is of the form: (uid, username, team_id, team_name)
    favouriteTeams = getAllUsers_And_Their_FavouriteTeams()
    print(favouriteTeams)
    return render(request, "all_accounts.html", {"favouriteTeams": favouriteTeams})