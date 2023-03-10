-- 코드를 입력하세요
SELECT a.CATEGORY,SUM(b.SALES) AS TOTAL_SALES
FROM BOOK a, BOOK_SALES b
WHERE (
    a.BOOK_ID = b.BOOK_ID
    AND b.SALES_DATE LIKE '2022-01%'
    )
GROUP BY CATEGORY
ORDER BY CATEGORY ASC;
