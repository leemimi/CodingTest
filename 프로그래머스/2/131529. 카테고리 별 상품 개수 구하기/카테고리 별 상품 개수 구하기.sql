-- 코드를 입력하세요
SELECT SUBSTRING(PRODUCT_CODE,1,2)AS CATEGORY, COUNT(*)
FROM PRODUCT
GROUP BY CATEGORY