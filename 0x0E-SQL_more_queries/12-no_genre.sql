-- list all shows in db without genre
-- use only one select
SELECT s.`title`, sg.`genre_id`
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS sg ON s.`id` = sg.`show_id`
WHERE sg.`show_id` IS NULL
ORDER BY s.`title`, sg.`genre_id`;
