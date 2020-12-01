SELECT * FROM levelupapi_gametype;
SELECT * FROM auth_user;
SELECT * FROM authtoken_token;
SELECT * FROM levelupapi_gamer;

SELECT * from;

SELECT 
e.id,
e.time,
e.description,
e.organizer_id,
e.date,
u.id as user_id,
g.title as game_name,
u.first_name || ' ' || u.last_name AS full_name
FROM levelupapi_event e
JOIN levelupapi_gamer o 
ON o.id = e.organizer_id
JOIN auth_user u on u.id = o.user_id
JOIN levelupapi_game g ON g.id = e.game_id;


