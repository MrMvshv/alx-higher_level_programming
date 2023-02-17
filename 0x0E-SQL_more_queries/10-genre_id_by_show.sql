-- list shows that have at least 1 genre
-- use only one select
SELECT s.`title`, sg.`genre_id`
FROM tv_shows AS s
JOIN tv_show_genres AS sg ON s.`id` = sg.`show_id`
JOIN tv_genres AS g ON sg.`genre_id` = g.`id`
GROUP BY s.`title`, sg.`genre_id`
HAVING COUNT(*) >= 1 ORDER BY s.`title`, sg.`genre_id`;
