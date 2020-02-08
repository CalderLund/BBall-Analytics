<<<<<<< HEAD:src/teams/tables/teamTables.sql
CREATE TABLE TeamInfo
(
    team_id VARCHAR(3) NOT NULL PRIMARY KEY,
    team_name VARCHAR(25)
);

CREATE TABLE TeamStats
(
    yr INT NOT NULL,
    team_id VARCHAR(3) NOT NULL,
    o_fgm INT,
    o_fga INT,
    o_ftm INT,
    o_fta INT,
    o_3pm INT,
    o_3pa INT,
    o_oreb INT,
    o_dreb INT,
    o_reb INT,
    o_asts INT,
    o_pf INT,
    o_stl INT,
    o_to INT,
    o_blk INT,
    o_pts INT,
    d_fgm INT,
    d_fga INT,
    d_ftm INT,
    d_fta INT,
    d_3pm INT,
    d_3pa INT,
    d_oreb INT,
    d_dreb INT,
    d_reb INT,
    d_asts INT,
    d_pf INT,
    d_stl INT,
    d_to INT,
    d_blk INT,
    d_pts INT,
    o_tmRebound INT,
    d_tmRebound INT,
    homeWon INT,
    homeLost INT,
    awayWon INT,
    awayLost INT,
    neutWon INT,
    neutLoss INT,
    confWon INT,
    confLoss INT,
    divWon INT,
    divLoss INT,
    pace INT,
    won INT,
    lost INT,
    games INT,
    PRIMARY KEY(yr, team_id),
    FOREIGN KEY(team_id) REFERENCES TeamInfo(team_id)
);
=======
CREATE TABLE TeamInfo
(
    team_id VARCHAR(3) NOT NULL PRIMARY KEY,
    team_name VARCHAR(25)
);

CREATE TABLE TeamStats
(
    yr INT NOT NULL,
    team_id VARCHAR(3) NOT NULL,
    rank INT,
    confRank INT,
    o_fgm INT,
    o_fga INT,
    o_ftm INT,
    o_fta INT,
    o_3pm INT,
    o_3pa INT,
    o_oreb INT,
    o_dreb INT,
    o_reb INT,
    o_asts INT,
    o_pf INT,
    o_stl INT,
    o_to INT,
    o_blk INT,
    o_pts INT,
    d_fgm INT,
    d_fga INT,
    d_ftm INT,
    d_fta INT,
    d_3pm INT,
    d_3pa INT,
    d_oreb INT,
    d_dreb INT,
    d_reb INT,
    d_asts INT,
    d_pf INT,
    d_stl INT,
    d_to INT,
    d_blk INT,
    d_pts INT,
    o_tmRebound INT,
    d_tmRebound INT,
    homeWon INT,
    homeLost INT,
    awayWon INT,
    awayLost INT,
    neutWon INT,
    neutLoss INT,
    confWon INT,
    confLoss INT,
    divWon INT,
    divLoss INT,
    pace INT,
    won INT,
    lost INT,
    games INT,
    PRIMARY KEY(yr, team_id),
    FOREIGN KEY(team_id) REFERENCES TeamInfo(team_id)
);

CREATE TABLE TeamStatAndInfo (
    yr INT NOT NULL,
    stats_team_id VARCHAR(3) NOT NULL,
    team_id VARCHAR(3),
    PRIMARY KEY(yr, stat_team_id),
    FOREIGN KEY(team_id) REFERENCES TeamInfo(team_id),
    FOREIGN KEY(yr, stats_team_id) REFERENCES TeamStats(yr, team_id)
);
>>>>>>> 1abc1b0d4d69e6f8b10e88b45d885525104a7810:tables/teamTables.sql
