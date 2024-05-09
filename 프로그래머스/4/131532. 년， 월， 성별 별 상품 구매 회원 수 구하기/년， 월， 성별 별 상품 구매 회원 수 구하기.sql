SELECT YEAR(B.SALES_DATE)AS YEAR,
MONTH(B.SALES_DATE)AS MONTH,
GENDER, COUNT(DISTINCT B.USER_ID)AS USERS
FROM USER_INFO A JOIN ONLINE_SALE B ON A.USER_ID = B.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER
