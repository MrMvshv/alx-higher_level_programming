-- lists no. of records with same score
-- display score, number of records with label sorted
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number;
