-- 코드를 입력하세요
SELECT R.INGREDIENT_TYPE, SUM(B.TOTAL_ORDER) AS 'TOTAL_ORDER'
FROM FIRST_HALF AS B
JOIN ICECREAM_INFO AS R
ON B.FLAVOR = R.FLAVOR
GROUP BY INGREDIENT_TYPE
ORDER BY TOTAL_ORDER