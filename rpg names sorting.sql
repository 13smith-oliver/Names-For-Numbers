INSERT INTO stats 
SELECT games.name, SUM(games.score) AS totalpoints, COUNT(*) AS totalgames
FROM games
GROUP BY games.name