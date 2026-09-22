SELECT
    province,
    SUM(CASE WHEN month = '2026-08' THEN amount ELSE 0 END) AS "2026-08",
    SUM(CASE WHEN month = '2026-09' THEN amount ELSE 0 END) AS "2026-09",
    SUM(amount) AS total
FROM sales
GROUP BY province
ORDER BY province;