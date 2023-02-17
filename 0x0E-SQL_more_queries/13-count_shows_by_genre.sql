-- list all genres and number of linked shows
-- in db use one select
SELECT g.`name` AS genre, COUNT(sg.`show_id`) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg ON g.`id` = sg.`genre_id`
GROUP BY genre
HAVING COUNT(sg.`show_id`) > 0
ORDER BY number_of_shows DESC;
