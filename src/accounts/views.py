from django.shortcuts import render, redirect

from .models import (createAccountTable, dropTableAccount, deleteAllRowsFromAccount, insertIntoAccount, getAllAccounts, get_latest_Uid,
createFavouriteTeamTable, insertIntoFavouriteTeam, dropTableFavouriteTeam, deleteAllRowsFromFavouriteTeam, getAllUsers_And_Their_FavouriteTeams,
get_A_Given_Users_FavouriteTeam, getAllFavouriteTeamRows, createFavouritePlayerTable, dropTableFavouritePlayer, 
deleteAllRowsFromFavouritePlayer, insertIntoFavouritePlayer, get_password_for_uid, deleteAccount, updateAccount_fav_team,
updateAccount_fav_player)

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
        print(request.POST["player"])
        team_name = request.POST["team"]
        team_id = team_name[0:3]
        print("Team: {}".format(team_name))
        print("Team ID: {}".format(team_id))
        # For now, year will not be inserted into the "FavouriteTeam" table since I'm not sure where to get this year value from :(
        yr = -1
        insertIntoFavouriteTeam(team_id, uid, yr)
        favouriteTeam = get_A_Given_Users_FavouriteTeam(uid)[0][0]
        favouritePlayer = request.POST["player"]
        insertIntoFavouritePlayer(favouritePlayer, uid)
        return render(request, "account_details.html", {"uid": uid, "username": username, "tmId": team_id,  "favouriteTeam": favouriteTeam, "favouritePlayer": favouritePlayer})
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

def signIn_view(request, uid, username, tmId, tmName, playerName):
    if request.method == "POST":
        pswd = get_password_for_uid(uid)
        print("Password: {}".format(pswd))
        if request.POST["password"] == pswd:
            return render(request, "update_account_form.html", {"uid": uid, "username": username, "tmId": tmId, "favouriteTeam": tmName, "favouritePlayer": playerName})
        else:
            return redirect("/accounts/all")
    return render(request, "signin.html", {"uid": uid, "username": username, "tmId": tmId, "favouriteTeam": tmName, "favouritePlayer": playerName})

def account_delete_view(request, uid):
    deleteAccount(uid)
    return redirect("/accounts/all")

def account_update_view(request, uid):
    if request.method == "POST":
        team_name = request.POST["team"]
        team_id = team_name[0:3]
        print("Team: {}".format(team_name))
        print("Team ID: {}".format(team_id))
        updateAccount_fav_team(uid, team_id)
        updateAccount_fav_player(uid, request.POST["player"])
    return redirect("/accounts/all")
# def update_account_view(request, uid, username, tmId, tmName, playerName):
#     return render(request, "update_account_form.html", {"uid": uid, "username": username, "tmId": tmId, "favouriteTeam": tmName, "favouritePlayer": playerName})