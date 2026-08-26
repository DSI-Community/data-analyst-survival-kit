/*
Query for ClassicModels
Aufgabe: Nutze \ROW_NUMBER(), um pro Kunde die jeweils neueste Bestellung zu ermitteln.
*/

/* WITH CTE */
WITH CTE_DateRankedOrders AS
(
		SELECT 
			customernumber,
			ordernumber,
			orderdate,
			ROW_NUMBER() OVER (PARTITION BY customernumber ORDER BY orderdate DESC) as row_num
		FROM orders
)
SELECT  
	c.customername,
	o.ordernumber,
	o.orderdate
FROM customers c
INNER JOIN CTE_DateRankedOrders o 
USING (customernumber)
WHERE o.row_num = 1
ORDER BY c.customername
;

/* WITH Subquery */
SELECT  
	c.customername,
	o.ordernumber,
	o.orderdate
FROM customers c
INNER JOIN
	(
		SELECT 
			customernumber,
			ordernumber,
			orderdate,
			ROW_NUMBER() OVER (PARTITION BY customernumber ORDER BY orderdate DESC) as row_num
		FROM orders
	) AS o 
USING (customernumber)
WHERE o.row_num = 1
ORDER BY c.customername
;
