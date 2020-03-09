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
from players.views import playerSetup, playerFiltering

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view),
    path("teams/year/<int:year>", teamsInYear_view),
    path("players/", playerSetup),
    path("players/filter/<str:json>", playerFiltering),
    path("team/<str:tmId>/<str:tmName>/", yearsOfATeam_view),
    path("team/<str:tmId>/<str:tmName>/<int:year>/", teamInfoInYear_view),
]
