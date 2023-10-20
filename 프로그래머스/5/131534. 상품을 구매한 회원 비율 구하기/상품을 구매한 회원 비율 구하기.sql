-- 코드를 입력하세요
SELECT YEAR(B.SALES_DATE)AS YEAR, MONTH(B.SALES_DATE)AS MONTH,
        COUNT(DISTINCT B.USER_ID)AS PUCHASED_USERS, ROUND(COUNT(DISTINCT B.USER_ID)/
                                                         (SELECT COUNT(DISTINCT USER_ID)
                                                         FROM USER_INFO
                                                         WHERE JOINED LIKE '2021%'
                                                         GROUP BY YEAR(JOINED)), 1)AS PUCHASED_RATIO
FROM (SELECT USER_ID FROM USER_INFO WHERE JOINED LIKE '2021%')AS A
JOIN ONLINE_SALE AS B
ON A.USER_ID = B.USER_ID
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH;