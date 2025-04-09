WITH MAX_USER AS (
    SELECT MEMBER_ID
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    ORDER BY COUNT(REVIEW_ID) DESC
    LIMIT 1
)
SELECT 
    (SELECT MEMBER_NAME
     FROM MEMBER_PROFILE AS P
     INNER JOIN MAX_USER AS M
     ON P.MEMBER_ID = M.MEMBER_ID) AS MEMBER_NAME, 
    REVIEW_TEXT, 
    DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') 'REVIEW_DATE'
FROM REST_REVIEW AS R 
INNER JOIN MAX_USER AS M 
ON R.MEMBER_ID = M.MEMBER_ID
ORDER BY REVIEW_DATE, REVIEW_TEXT
