from django.shortcuts import render, redirect

from .models import (createAccountTable, dropTableAccount, deleteAllRowsFromAccount, insertIntoAccount, getAllAccounts, get_latest_Uid,
createFavouriteTeamTable, insertIntoFavouriteTeam, dropTableFavouriteTeam, deleteAllRowsFromFavouriteTeam, getAllUsers_And_Their_FavouriteTeams,
get_A_Given_Users_FavouriteTeam, getAllFavouriteTeamRows, createFavouritePlayerTable, dropTableFavouritePlayer, 
deleteAllRowsFromFavouritePlayer, insertIntoFavouritePlayer, get_password_for_uid, deleteAccount, updateAccount_fav_team,
updateAccount_fav_player, insertIntoFantasyTeam, createFantasyTeamTable, createFantasyIsMemTable, insertIntoFantasyIsMem, getFantasyPlayers,
getFantasyTeam, updateFantasyTeam, updateFantasyIsMem, evaluateScore)

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
    # createFantasyTeamTable()
    # createFantasyIsMemTable()
    print("Account View's accountSetup() function called.")
    return redirect("/")

def create_account_view(request):
    print("CREATE ACCOUNT VIEW")
    if request.method == "POST":
        #print(request.POST["username"])
        #print(request.POST["password"])
        #print(request.POST)
        username = request.POST["username"]
        insertIntoAccount(request.POST["username"], request.POST["password"])
        uid_list = get_latest_Uid()
        uid = uid_list[0][0]
        #print(uid)
        return render(request, "account_initialize_details.html", {"username": username, "uid": uid})
    return render(request, "create_account_form.html", {})

def account_details(request, uid, username):
    print("UID: {}".format(uid))
    # print(request)
    if request.method == "POST":
        #print(request.POST["player"])
        team_name = request.POST["team"]
        team_id = team_name[0:3]
        #print("Team: {}".format(team_name))
        #print("Team ID: {}".format(team_id))
        # For now, year will not be inserted into the "FavouriteTeam" table since I'm not sure where to get this year value from :(
        yr = -1
        insertIntoFavouriteTeam(team_id, uid, yr)
        favouriteTeam = get_A_Given_Users_FavouriteTeam(uid)[0][0]
        favouritePlayer = request.POST["player"]
        insertIntoFavouritePlayer(favouritePlayer, uid)
        
        # Fantasy Team Code Starts Here
        fantasy_team_name = "None"
        fantasyPlayers = None
        if "teamName" in request.POST:
            fantasy_team_name = request.POST["teamName"]
            PG_player_name = request.POST["PG"]
            SG_player_name = request.POST["SG"]
            SF_player_name = request.POST["SF"]
            PF_player_name = request.POST["PF"]
            C_player_name = request.POST["C"]
            insertIntoFantasyTeam(uid, fantasy_team_name)
            insertIntoFantasyIsMem(uid, PG_player_name, "PG")
            insertIntoFantasyIsMem(uid, SG_player_name, "SG")
            insertIntoFantasyIsMem(uid, SF_player_name, "SF")
            insertIntoFantasyIsMem(uid, PF_player_name, "PF")
            insertIntoFantasyIsMem(uid, C_player_name, "C")
            fantasyPlayers = {"PG": PG_player_name,
                              "SG": SG_player_name,
                              "SF": SF_player_name,
                              "PF": PF_player_name,
                              "C": C_player_name,}

            teamScore = {}
            if len(fantasyPlayers) == 5:
                teamScore = evaluateScore(fantasyPlayers)

        else:
            insertIntoFantasyTeam(uid, None)
        print("--------------------------------------")
        print(request.POST)
        return render(request, "account_details.html", {"uid": uid, "username": username, "tmId": team_id,  "favouriteTeam": favouriteTeam, "favouritePlayer": favouritePlayer, "fantasyTeam":fantasy_team_name, "fantasyPlayers":fantasyPlayers, "teamScore":teamScore})
    return redirect("/")

def already_know_account_details(request, uid, username, tmId, tmName, playerName, fantasyTeam):
    result = getFantasyPlayers(uid)
    fantasyPlayers = {}
    for player in result:
        fantasyPlayers[player[1]] = player[0]
    print(fantasyPlayers)

    teamScore = {}
    if len(fantasyPlayers) == 5:
        teamScore = evaluateScore(fantasyPlayers)

    # Also retrieve and send favourite player for this account (uid) to account_details.html
    return render(request, "account_details.html", {"uid": uid, "username": username, "tmId": tmId, "favouriteTeam": tmName, "favouritePlayer": playerName, "fantasyTeam":fantasyTeam, "fantasyPlayers":fantasyPlayers, "teamScore":teamScore})

def all_accounts_view(request):
    # favouriteTeams is a list of tuples
    # each tuple is of the form: (uid, username, team_id, team_name, player_name)
    favouriteTeams = getAllUsers_And_Their_FavouriteTeams()
    print("=========")
    print(favouriteTeams)
    # Also retrieve and send favourite player for all accounts to all_aaounts.html
    return render(request, "all_accounts.html", {"favouriteTeams": favouriteTeams})

def signIn_view(request, uid, username, tmId, tmName, playerName):
    if request.method == "POST":
        pswd = get_password_for_uid(uid)
        print("Password: {}".format(pswd))
        if request.POST["password"] == pswd:
            fantasyTeam = getFantasyTeam(uid)[0][0]
            fantasyPlayers = None
            if fantasyTeam is not None:
                result = getFantasyPlayers(uid)
                fantasyPlayers = {}
                for player in result:
                    fantasyPlayers[player[1]] = player[0]
            return render(request, "update_account_form.html", {"uid": uid, "username": username, "tmId": tmId, "favouriteTeam": tmName, "favouritePlayer": playerName, "fantasyTeam":fantasyTeam, "fantasyPlayers":fantasyPlayers})
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
        # print("Team: {}".format(team_name))
        # print("Team ID: {}".format(team_id))
        updateAccount_fav_team(uid, team_id)
        updateAccount_fav_player(uid, request.POST["player"])
        if 'decision' not in request.POST:
            updateFantasyTeam(uid, request.POST["teamName"])
            updateFantasyIsMem(uid, request.POST["SG"], "SG")
            updateFantasyIsMem(uid, request.POST["PG"], "PG")
            updateFantasyIsMem(uid, request.POST["SF"], "SF")
            updateFantasyIsMem(uid, request.POST["PF"], "PF")
            updateFantasyIsMem(uid, request.POST["C"], "C")
        elif 'teamName' in request.POST:
            fantasy_team_name = request.POST["teamName"]
            PG_player_name = request.POST["PG"]
            SG_player_name = request.POST["SG"]
            SF_player_name = request.POST["SF"]
            PF_player_name = request.POST["PF"]
            C_player_name = request.POST["C"]
            insertIntoFantasyTeam(uid, fantasy_team_name)
            insertIntoFantasyIsMem(uid, PG_player_name, "PG")
            insertIntoFantasyIsMem(uid, SG_player_name, "SG")
            insertIntoFantasyIsMem(uid, SF_player_name, "SF")
            insertIntoFantasyIsMem(uid, PF_player_name, "PF")
            insertIntoFantasyIsMem(uid, C_player_name, "C")
    return redirect("/accounts/all")
# def update_account_view(request, uid, username, tmId, tmName, playerName):
#     return render(request, "update_account_form.html", {"uid": uid, "username": username, "tmId": tmId, "favouriteTeam": tmName, "favouritePlayer": playerName})
