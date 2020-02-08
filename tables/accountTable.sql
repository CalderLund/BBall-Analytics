CREATE TABLE Accounts
  (
     uid  INT NOT NULL PRIMARY KEY,
     name VARCHAR(25) NOT NULL,
     pwd  VARCHAR(25) NOT NULL
  );

  CREATE TABLE FavouriteTeams
  (
     uid  INT NOT NULL,
     team_id VARCHAR(3) NOT NULL,
     year INT NOT NULL,
     PRIMARY KEY(uid, team_id, year),
     FOREIGN KEY(uid) REFERENCES Accounts
  );

  CREATE TABLE FavouritePlayers
  (
     uid  INT NOT NULL,
     player_id VARCHAR(3) NOT NULL,
     PRIMARY KEY(uid, player_id),
     FOREIGN KEY(uid) REFERENCES Accounts
  );