-- lists no. of records with same score
-- display score, number of records with label sorted
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score desc;
