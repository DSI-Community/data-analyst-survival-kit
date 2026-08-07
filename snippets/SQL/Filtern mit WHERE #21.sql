-- Schreibe eine Query, die alle Kunden aus der Tabelle \customers\ holt, die in 'Berlin' wohnen.

SELECT *
FROM customers
WHERE city ILIKE '%BERLIN%'
;