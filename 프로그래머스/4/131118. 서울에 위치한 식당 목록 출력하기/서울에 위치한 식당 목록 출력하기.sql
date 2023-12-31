-- 코드를 입력하세요
SELECT R.REST_ID, R.REST_NAME, R.FOOD_TYPE, R.FAVORITES, R.ADDRESS, ROUND(AVG(L.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO AS R
JOIN REST_REVIEW AS L ON R.REST_ID = L.REST_ID
WHERE ADDRESS LIKE '서울%'
GROUP BY REST_ID
ORDER BY SCORE DESC, FAVORITES DESC