SELECT COUNT(*)AS FISH_COUNT, MAX(LENGTH)AS MAX_LENGTH, FISH_TYPE
FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING AVG(IF(LENGTH<10,10,LENGTH))>=33
ORDER BY FISH_TYPE
