WITH SCORE ( EMP_NO, TOT_SCORE, BONUS ) AS (
    SELECT EMP_NO, 
    CASE WHEN AVG(SCORE) >= 96 THEN 'S'
         WHEN AVG(SCORE) >= 90 THEN 'A'
         WHEN AVG(SCORE) >= 80 THEN 'B'
         ELSE 'C' END, 
    CASE WHEN AVG(SCORE) >= 96 THEN 0.2
         WHEN AVG(SCORE) >= 90 THEN 0.15
         WHEN AVG(SCORE) >= 80 THEN 0.1
         ELSE 0 END
    FROM HR_GRADE
    GROUP BY EMP_NO
)

SELECT E.EMP_NO, E.EMP_NAME, S.TOT_SCORE AS 'GRADE', (E.SAL * S.BONUS) AS 'BONUS'
FROM HR_EMPLOYEES E
JOIN SCORE S
ON E.EMP_NO = S.EMP_NO
ORDER BY EMP_NO