CREATE TABLE Accounts
  (
     uid  DECIMAL(9, 0) NOT NULL PRIMARY KEY,
     user VARCHAR(25) NOT NULL,
     pwd  VARCHAR(25) NOT NULL
  );

  CREATE TABLE FavouriteTeams
  (
     uid  DECIMAL(9, 0) NOT NULL,
     team_id VARCHAR(3) NOT NULL,
     year DECIMAL(4, 0) NOT NULL,
     PRIMARY KEY(uid, team_id, year),
     FOREIGN KEY(uid) REFERENCES Accounts
  );

  CREATE TABLE FavouritePlayers
  (
     uid  DECIMAL(9, 0) NOT NULL,
     player_id VARCHAR(3) NOT NULL,
     PRIMARY KEY(uid, player_id),
     FOREIGN KEY(uid) REFERENCES Accounts
  );