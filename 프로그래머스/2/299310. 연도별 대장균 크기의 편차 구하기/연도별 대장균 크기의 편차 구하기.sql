WITH MAX_S AS (SELECT YEAR(DIFFERENTIATION_DATE)AS YEAR, MAX(SIZE_OF_COLONY) AS SIZE
FROM ECOLI_DATA
GROUP BY YEAR)

SELECT M.YEAR, (M.SIZE - E.SIZE_OF_COLONY)AS YEAR_DEV, E.ID
FROM MAX_S M INNER JOIN ECOLI_DATA E
ON YEAR(E.DIFFERENTIATION_DATE)= M.YEAR
ORDER BY M.YEAR, YEAR_DEV


