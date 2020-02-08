-- Displaying all teams in our database since 1940's
select distinct team_name from
    (TeamInfo join TeamStatAndInfo on TeamInfo.team_id = TeamStatAndInfo.stats_team_id)
where yr >= 1940

--filtering teams by year
--given input
select distinct team_name from
    (TeamInfo join TeamStatAndInfo on TeamInfo.team_id = TeamStatAndInfo.stats_team_id)
where yr = <input>

--user modify db
--create account
INSERT INTO Accounts VALUES (1, 'administrator', 'cs348family');

--add Favourite Teams
INSERT INTO FavouriteTeams VALUES(1, 'TMD', 1940);

--add Favourite Player
INSERT INTO FavouritePlayers VALUES(1, 'TMD');

--add fantasy team
INSERT INTO FantasyTeam VALUES('My Fantasy Team', 1);