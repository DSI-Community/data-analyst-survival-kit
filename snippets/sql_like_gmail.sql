-- Issue #27: SQL - Suchen mit LIKE
-- Findet alle Benutzer, deren E-Mail_Adresse auf @gmail.com endet
-- Anname: Die Spalte mit E-Mail-Adresse heißt email

SELECT * FROM users
WHERE email LIKE '%@gmail.com';