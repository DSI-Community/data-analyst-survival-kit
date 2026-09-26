SELECT
    revenue,
    CASE
        WHEN revenue > 1000 THEN 'Hoch'
        ELSE 'Niedrig'
    END AS revenue_category
FROM sales;