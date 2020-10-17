DROP TABLE IF EXISTS ranking;
DROP TABLE IF EXISTS matches ;
DROP TABLE IF EXISTS teams ;

CREATE TABLE teams(
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE matches (
    id INTEGER PRIMARY KEY ,
    team0 INTEGER  NOT NULL,
    team1 INTEGER  NOT NULL,
    score0 INTEGER NOT NULL,
    score1 INTEGER NOT NULL,
    date  DATETIME NOT NULL,
    FOREIGN KEY (team0) REFERENCES teams(id),
    FOREIGN KEY (team1) REFERENCES teams(id),
    UNIQUE (team0,team1),
    check(score0>=0),
    check(score1>=0)
);

CREATE TABLE ranking(
    team_id INTEGER PRIMARY KEY NOT NULL,
    rank INTEGER UNIQUE NOT NULL ,
    match_played_count INTEGER NOT NULL,
    draw_match_count INTEGER NOT NULL,
    goal_for_count INTEGER NOT NULL ,
    goal_difference INTEGER NOT NULL,
    points INTEGER NOT NULL ,
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

       