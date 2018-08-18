INSERT INTO accountname 
SELECT games.account_name, SUM(games.score) AS totalpoints, COUNT(*) AS totalgames
FROM games
GROUP BY games.account_name