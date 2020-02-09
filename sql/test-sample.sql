--get all teams in a year(say 2010 in this case)
SELECT TeamInfo.team_id, team_name, yr from TeamInfo NATURAL JOIN TeamStats WHERE yr=2010

--count the number of teams in a year (say 2010 in this case)
SELECT count(*) from (SELECT TeamInfo.team_id, team_name, yr from TeamInfo NATURAL JOIN TeamStats WHERE yr=2010) AS R

--user modify db
--insert team info
INSERT into TeamInfo VALUES ('pqr', 'Test Team 3')

--insert team stats
INSERT into TeamStats VALUES ('2020', 'BOS')

--delete team info
DELETE from TeamInfo

--delete team stats
DELETE from TeamStats