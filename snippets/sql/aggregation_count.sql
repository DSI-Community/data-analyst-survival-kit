-- Issue #22: Aggregation mit COUNT
-- Zähle, wie viele Bestellungen jeder Kunde in der Tabelle orders getätigt hat
-- Nutzung von GROUP BY

SELECT
    customerNumber,
    COUNT(*) AS total_orders
FROM orders
GROUP BY customerNumber;