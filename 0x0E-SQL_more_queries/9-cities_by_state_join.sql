-- lists all cities of california
-- should not use JOIN
SELECT `cities.id`, `cities.name`, `states.name` FROM `cities`, `states`
ORDER BY `cities.id`;
