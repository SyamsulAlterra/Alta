SELECT * FROM payment_methods;
SELECT * FROM transactions;
SELECT * FROM product_types;
SELECT * FROM users;
SELECT * FROM transaction_detail;
SELECT * FROM supplier;
SELECT * FROM products;
SELECT * FROM product_descriptions;
-- 1
SELECT * FROM users WHERE created_at>DATE_SUB(current_time, INTERVAL 7 day) ORDER BY id DESC;

-- 2
SELECT t.id , p.id, p.product_type_id, p.nama_product, td.qty, u.nama FROM
products p JOIN transaction_detail td ON p.id = td.product_id
JOIN transactions t ON t.id = td.transaction_id
JOIN users u ON u.id = t.user_id;

-- 3
SELECT u.nama AS nama, COUNT(1) AS total_transaksi, SUM(total_qty) AS total_quantity FROM 
users u JOIN transactions t ON u.id = t.user_id 
GROUP BY u.nama
HAVING total_quantity>5 AND total_transaksi>2;

-- 4  
SELECT u.nama, p.nama_product, pt.nama, COUNT(1) AS total_transaksi, SUM(qty) AS total_qty -- t.id, t.total_qty, td.transaction_id, td.qty, p.id, p.nama_product, p.product_type_id, pt.nama
FROM users u JOIN transactions t ON u.id=t.user_id
JOIN transaction_detail td ON td.transaction_id = t.id
JOIN products p ON p.id = td.product_id
JOIN product_types pt ON pt.id = p.product_type_id
WHERE p.nama_product LIKE '%p%'
GROUP BY u.nama, p.nama_product
ORDER BY total_qty DESC;

-- 5
DELIMITER $$
CREATE TRIGGER after_insert_transaction_detail
	AFTER INSERT ON transaction_detail FOR EACH ROW
BEGIN
	DECLARE added_qty INT(11);
    DECLARE added_price DECIMAL(25,2);
    DECLARE updated_time TIMESTAMP;
    SET updated_time = NEW.updated_at;
    SET added_qty = NEW.qty;
    SET added_price = NEW.price;
    UPDATE transactions SET total_qty = total_qty + added_qty WHERE transactions.id = NEW.transaction_id;
    UPDATE transactions SET total_price = total_price + added_price WHERE transactions.id = NEW.transaction_id;
    UPDATE transactions SET updated_at = updated_time WHERE transactions.id = NEW.transaction_id;
END $$
DELIMITER ;

SHOW TRIGGERS;

INSERT INTO transaction_detail (transaction_id, product_id, status, qty, price) VALUES
(1,1,1,1,50000);

SELECT * FROM transactions;