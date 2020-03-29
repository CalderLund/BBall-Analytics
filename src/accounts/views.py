from django.shortcuts import render, redirect

from .models import (createAccountTable, dropTableAccount, deleteAllRowsFromAccount, insertIntoAccount, getAllAccounts, get_latest_Uid,
createFavouriteTeamTable, insertIntoFavouriteTeam, dropTableFavouriteTeam, deleteAllRowsFromFavouriteTeam, getAllUsers_And_Their_FavouriteTeams,
get_A_Given_Users_FavouriteTeam, getAllFavouriteTeamRows, createFavouritePlayerTable, dropTableFavouritePlayer, 
deleteAllRowsFromFavouritePlayer, insertIntoFavouritePlayer)

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
    # deleteAllRowsFromFavouritePlayer()
    # dropTableFavouritePlayer()
    # createFavouritePlayerTable()
    print("Account View's accountSetup() function called.")
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
        print(request.POST["player"])
        # For now, year will not be inserted into the "FavouriteTeam" table since I'm not sure where to get this year value from :(
        yr = -1
        insertIntoFavouriteTeam(request.POST["team"], uid, yr)
        favouriteTeam = get_A_Given_Users_FavouriteTeam(uid)[0][0]
        favouritePlayer = request.POST["player"]
        insertIntoFavouritePlayer(favouritePlayer, uid)
        return render(request, "account_details.html", {"uid": uid, "username": username, "tmId": request.POST["team"],  "favouriteTeam": favouriteTeam, "favouritePlayer": favouritePlayer})
    return redirect("/")

def already_know_account_details(request, uid, username, tmId, tmName, playerName):
    # Also retrieve and send favourite player for this account (uid) to account_details.html
    return render(request, "account_details.html", {"uid": uid, "username": username, "tmId": tmId, "favouriteTeam": tmName, "favouritePlayer": playerName})

def all_accounts_view(request):
    # favouriteTeams is a list of tuples
    # each tuple is of the form: (uid, username, team_id, team_name, player_name)
    favouriteTeams = getAllUsers_And_Their_FavouriteTeams()
    print(favouriteTeams)
    # Also retrieve and send favourite player for all accounts to all_aaounts.html
    return render(request, "all_accounts.html", {"favouriteTeams": favouriteTeams})