SELECT customers, Umsatz from customers where umsatz > (select avg(umsatz) from customers);
