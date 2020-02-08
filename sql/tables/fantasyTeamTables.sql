CREATE TABLE FantasyTeam (
    name VARCHAR(50) NOT NULL,
    uid INT NOT NULL,
    PRIMARY KEY(name, uid),
    FOREIGN KEY(uid) REFERENCES Accounts(uid)
);

CREATE TABLE FantasyTeamMember (
    team_name VARCHAR(50) NOT NULL,
    uid INT NOT NULL,
    player_name VARCHAR(50) NOT NULL,
    PRIMARY KEY(team_name, uid, player_name),
    FOREIGN KEY(team_name, uid) REFERENCES FantasyTeam(name, uid),
    FOREIGN KEY(player_name) REFERENCES Player(name)
);