-- 코드를 입력하세요
SELECT L.USER_ID, L.NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS F
INNER JOIN USED_GOODS_USER AS L ON F.WRITER_ID = L.USER_ID
WHERE F.STATUS LIKE 'DONE'
GROUP BY USER_ID
HAVING SUM(PRICE) >= 700000
ORDER BY TOTAL_SALES
