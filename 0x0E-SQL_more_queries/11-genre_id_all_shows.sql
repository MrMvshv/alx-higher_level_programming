-- list all shows in db
-- use only one select
SELECT s.`title`, COALESCE(sg.`genre_id`, 'NULL') AS genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS sg ON s.`id` = sg.`show_id`
LEFT JOIN tv_genres AS g ON sg.`genre_id` = g.`id`
GROUP BY s.`title`, sg.`genre_id`
ORDER BY s.`title`, sg.`genre_id`;
