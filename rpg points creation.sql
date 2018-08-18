CREATE TABLE games ( 
    name          BLOB, 
    account_name  BLOB, 
    time 		  BLOB,
	score   INTEGER
);
CREATE TABLE `stats` (
    `name`  TEXT PRIMARY KEY ON CONFLICT REPLACE,
    `totalpoints`   INTEGER,
    `totalgames`    INTEGER
);
CREATE TABLE accountname (
	account_name  BLOB,
	totalpoints	  INTEGER,
	totalgames	  INTEGER
)