-- RELEASE 1
-- INSERT
-- A
INSERT INTO operators (name, id) VALUES('Telkomsel',1);
INSERT INTO operators (name, id) VALUES('Indosat',2);
INSERT INTO operators (name, id) VALUES('XL',3);
INSERT INTO operators (name, id) VALUES('Esia',4);
INSERT INTO operators (name, id) VALUES('Smartfren',5);
-- B
INSERT INTO product_type (id, name) VALUES(1,'Data Internet');
INSERT INTO product_type (id, name) VALUES(2,'Pulsa Pascabayar');
INSERT INTO product_type (id, name) VALUES(3,'Pulsa Prabayar');

-- C
INSERT INTO product (id, product_type_id, operator_id, price, name, status) VALUES (1,1,3,20000,'Internet 1 minggu',1);
INSERT INTO product (id, product_type_id, operator_id, price, name, status) VALUES (2,1,3,60000,'Internet 1 bulan',1);

-- D
INSERT INTO product (id, product_type_id, operator_id, price, name, status) VALUES (3,2,1,20000,'Pulsa 1 minggu',1);
INSERT INTO product (id, product_type_id, operator_id, price, name, status) VALUES (4,2,1,60000,'Pulsa 1 bulan',1);
INSERT INTO product (id, product_type_id, operator_id, price, name, status) VALUES (5,2,1,100000,'Pulsa 2 bulan',1);

-- E
INSERT INTO product (id, product_type_id, operator_id, price, name, status) VALUES (6,3,4,25000,'Pulsa 20.000',1);
INSERT INTO product (id, product_type_id, operator_id, price, name, status) VALUES (7,3,4,52000,'Pulsa 50.000',1);
INSERT INTO product (id, product_type_id, operator_id, price, name, status) VALUES (8,3,4,100000,'Pulsa 100.000',1);

-- F
INSERT INTO product_description (id, description) VALUES (1, 'ini internet buat 1 minggu');
INSERT INTO product_description (id, description) VALUES (2, 'ini internet buat 1 bulan');
INSERT INTO product_description (id, description) VALUES (3, 'ini pulsa buat 1 minggu bayar nanti');
INSERT INTO product_description (id, description) VALUES (4, 'ini pulsa buat 1 bulan bayar nanti');
INSERT INTO product_description (id, description) VALUES (5, 'ini pulsa buat 2 bulan bayar nanti');
INSERT INTO product_description (id, description) VALUES (6, 'ini pulsa 20.000 maksimal buat 1 bulan');
INSERT INTO product_description (id, description) VALUES (7, 'ini pulsa 50.000 maksimal buat 1 bulan');
INSERT INTO product_description (id, description) VALUES (8, 'ini pulsa 100.000 maksimal buat 1 bulan');

-- G
INSERT INTO payment_methods(id, name, status) VALUES (1,'tunai',1);
INSERT INTO payment_methods(id, name, status) VALUES (2,'debit',1);
INSERT INTO payment_methods(id, name, status) VALUES (3,'kredit',1);

-- H
INSERT INTO users (id, status, gender, name) VALUES (1,1,'m','Syamsul');
INSERT INTO users (id, status, gender, name) VALUES (2,1,'f','Arifin');
INSERT INTO users (id, status, gender, name) VALUES (3,1,'m','Muhammad');
INSERT INTO users (id, status, gender, name) VALUES (4,1,'f','Udin');
INSERT INTO users (id, status, gender, name) VALUES (5,1,'m','Fikri');

-- I
INSERT INTO transactions (id,user_id,payment_method_id,status,total_qty, total_price) VALUES
(1,1,1,1,1, 20000),
(2,1,2,1,1, 60000),
(3,1,3,1,1, 60000),
-- user_id 2
(4,2,1,1,2, 160000),
(5,2,2,1,2, 20000),
(6,2,3,1,2, 160000),
-- user_id 3
(7,3,1,1,3, 172000),
(8,3,2,1,3, 180000),
(9,3,3,1,3, 60000),
-- user_id 4
(10,4,1,1,2, 80000),
(11,4,2,1,2, 40000),
(12,4,3,1,2, 50000),
-- user_id 5
(13,5,1,1,1, 20000),
(14,5,2,1,1, 60000),
(15,5,3,1,1, 25000);

-- J
INSERT INTO transaction_details(transaction_id, product_id, status, qty) VALUES
(1,1,1,1),
(2,4,1,1),
(3,2,1,1),
(4,2,1,1),
(4,8,1,1),
(5,4,1,1),
(5,3,1,1),
(6,5,1,1),
(6,2,1,1),
(7,7,1,1),
(7,2,1,2),
(8,8,1,1),
(8,2,1,1),
(8,3,1,1),
(9,1,1,3),
(10,1,1,1),
(10,2,1,1),
(11,3,1,2),
(12,6,1,2),
(13,1,1,1),
(14,2,1,1),
(15,6,1,1);
UPDATE transaction_details, product SET transaction_details.price=product.price WHERE transaction_details.product_id=product.id;

-- SHOW TABLE, AUXILIARY QUERY
select * from operators;
SELECT * FROM product_type;
SELECT * FROM product;
SELECT * FROM product_description;
SELECT * FROM payment_methods;
SELECT * FROM users;
SELECT * FROM transactions;
SELECT * FROM transaction_details;


-- SELECT
SELECT * FROM users WHERE gender='m'; -- A
SELECT * FROM product WHERE id=3; -- B
SELECT * FROM users WHERE name LIKE '%a%' OR '%a' OR 'a%'; -- C
SELECT COUNT(*) FROM users WHERE gender='f'; -- D
SELECT * FROM users ORDER BY name; -- E
SELECT * FROM product WHERE id=3 LIMIT 5; -- F

-- UPDATE
UPDATE product SET name='product dummy' WHERE id=1; -- A
-- delete every row in child table that link to product.id=1
DELETE FROM transaction_details WHERE product_id=1; -- B
DELETE FROM product_description WHERE id=1; -- B
DELETE FROM product WHERE id=1; -- B

-- DELETE
DELETE FROM transaction_details WHERE product_id=2; -- A
DELETE FROM product_description WHERE id=2; -- A
DELETE FROM product WHERE product_type_id=1; -- A

-- RELEASE 2
-- 1
SELECT transactions.id, user_id, payment_method_id, transactions.status, name, gender FROM 
transactions JOIN users ON transactions.user_id = users.id
WHERE users.id=1 OR users.id=2;
-- 2
SELECT SUM(total_price) FROM transactions WHERE user_id=1;
-- 3
SELECT COUNT(1) FROM
product JOIN transaction_details ON product.id = transaction_details.product_id
WHERE product_type_id=2;

-- 4
SELECT product.*, product_type.name FROM
product JOIN product_type ON product.product_type_id = product_type.id;

-- 5
SELECT transactions.*, users.name, product.name  FROM transactions 
JOIN users ON users.id = transactions.user_id 
JOIN transaction_details ON transactions.id = transaction_details.transaction_id 
JOIN product ON transaction_details.product_id = product.id;

-- 6
DELIMITER $$
CREATE TRIGGER before_delete_data_transaction
		BEFORE DELETE ON transactions
        FOR EACH ROW
BEGIN
	DECLARE id_deleted INT(11);
    SET id_deleted=OLD.id;
	DELETE FROM transaction_details WHERE transaction_id=id_deleted;
END$$
DELIMITER ;

DELETE FROM transactions WHERE id=1;

-- 7
DELIMITER $$
CREATE TRIGGER after_delete_transaction_detail
	BEFORE DELETE ON transaction_details FOR EACH ROW
BEGIN
	DECLARE remove_qty INT(11);
    DECLARE remove_price NUMERIC(25,2);
    
    SET remove_qty = OLD.qty;
    SET remove_price = OLD.price*OLD.qty;
    
    UPDATE transactions SET total_qty=total_qty-remove_qty WHERE id=OLD.transaction_id;
    UPDATE transactions SET total_price=total_price-remove_price WHERE id=OLD.transaction_id;
    
END$$
DELIMITER ;

DELETE FROM transaction_details WHERE transaction_id=1;

-- 8
SELECT * FROM product WHERE id NOT IN (SELECT product_id FROM transaction_details);


    