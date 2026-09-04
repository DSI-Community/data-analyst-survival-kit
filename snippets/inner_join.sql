DROP TABLE IF EXISTS users;

CREATE TABLE users(

    user_id SERIAL PRIMARY KEY,
    first_name TEXT,
	last_name TEXT,
	email TEXT
);

INSERT INTO users (user_id, first_name, last_name, email)
VALUES (1, 'Nataliya', 'Yavon', 'natasha.yavon@gmail.com');

INSERT INTO users (user_id, first_name, last_name, email)
VALUES (2, 'Eric', 'Dragon', 'eric.dragon@gmail.com');

INSERT INTO users (user_id, first_name, last_name, email)
VALUES (3, 'Orio', 'Mandella', 'orio.mandella@gmail.com');


DROP TABLE IF EXISTS orders;

CREATE TABLE orders(

    order_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
	order_number INT,
	price NUMERIC
);

INSERT INTO orders (order_id, user_id, order_number, price)
VALUES (1, 1, 12345, 138);

INSERT INTO orders (order_id, user_id, order_number, price)
VALUES (2, 2, 12346, 156);

INSERT INTO orders (order_id, user_id, order_number, price)
VALUES (3, 3, 12347, 173);

SELECT * 
FROM users
INNER JOIN orders USING (user_id);