"""cs348_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from teams.views import home_view, teamsInYear_view, yearsOfATeam_view, teamInfoInYear_view
from players.views import playerSetup, playerInfo_view, playerStats_view, topplayers_view, player_select_result_view, player_years_played_view
from accounts.views import (accountSetup, create_account_view, all_accounts_view, account_details, already_know_account_details,
                            signIn_view, account_delete_view, account_update_view)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view),
    path("teams/year/<int:year>", teamsInYear_view),
    path("players/setup", playerSetup),
    path("team/<str:tmId>/<str:tmName>/", yearsOfATeam_view),
    path("team/<str:tmId>/<str:tmName>/<int:year>/", teamInfoInYear_view),
    path("players/", topplayers_view),
    path("players/player_select_result", player_select_result_view),
    # path("players/filter/<str:json>", playerFiltering),
    path("player_stats/<str:tmId>/<str:tmName>/<int:year>/", playerInfo_view),
    path("player_stats/<str:tmId>/<str:tmName>/<int:year>/<str:playerName>/", playerStats_view),
    path("accounts/", accountSetup),
    path("accounts/create/", create_account_view),
    path("accounts/all", all_accounts_view),
    path("accounts/<int:uid>/<str:username>", account_details),
    path("accounts/<int:uid>/<str:username>/<str:tmId>/<str:tmName>/<str:playerName>", already_know_account_details),
    path("players/<str:playerName>", player_years_played_view),
    path("accounts/signin/<int:uid>/<str:username>/<str:tmId>/<str:tmName>/<str:playerName>", signIn_view),
    path("accounts/update/<int:uid>", account_update_view),
    path("accounts/delete/<int:uid>", account_delete_view),
]
