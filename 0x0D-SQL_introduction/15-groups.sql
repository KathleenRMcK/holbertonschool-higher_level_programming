-- Lists number of records with the same score in table
SELECT score, COUNT(score) AS number FROM second_table DESC;
