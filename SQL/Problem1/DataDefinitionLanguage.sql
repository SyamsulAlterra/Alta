-- create database
CREATE DATABASE ata_online_shop;
USE ata_online_shop;
SHOW TABLES;
SHOW DATABASES;
-- create table operators

CREATE TABLE operators(
	id INT PRIMARY KEY,
    name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- create product_type table
CREATE TABLE product_type(
	id INT(11) PRIMARY KEY,
    name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- create payment_methods table
CREATE TABLE payment_methods(
	id INT(11),
    name VARCHAR(255),
    status SMALLINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
    
);

-- create users table
CREATE TABLE users(
	id INTEGER PRIMARY KEY,
    name VARCHAR(32),
    status SMALLINT,
    gender CHAR(1),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    dob DATE
);

-- create product table
CREATE TABLE product(
	id INT PRIMARY KEY,
    product_type_id INT(11),
    operator_id INT(11),
    code VARCHAR(50),
    price NUMERIC(25,2),
    name VARCHAR(100),
    status SMALLINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT product_product_type FOREIGN KEY (product_type_id) REFERENCES product_type(id),
    CONSTRAINT product_operators FOREIGN KEY (operator_id) REFERENCES operators(id)
    -- FOREIGN KEY (id) REFERENCES transaction_details(product_id)
);

-- create product_description table
CREATE TABLE product_description(
	id INT(11) PRIMARY KEY,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT product_description_product FOREIGN KEY (id) REFERENCES product(id)
);

-- create transactions table
CREATE TABLE transactions(
	id INT(11),
    user_id INT(11),
    payment_method_id INT(11),
    status VARCHAR(10),
    total_qty INT(11),
    total_price NUMERIC(25,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(id),
    CONSTRAINT transactions_users FOREIGN KEY(user_id) REFERENCES users(id),
    CONSTRAINT transactions_payment_methods FOREIGN KEY(payment_method_id) REFERENCES payment_methods(id)
);

-- create transaction_details table
CREATE TABLE transaction_details(
	transaction_id INT,
    product_id INT(11),
    status VARCHAR(10),
    qty INT(11),
    price NUMERIC(25,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (transaction_id, product_id),
    CONSTRAINT transaction_details_transactions FOREIGN KEY (transaction_id) REFERENCES transactions(id),
    CONSTRAINT transaction_details_product FOREIGN KEY (product_id) REFERENCES product(id)
);

-- create couriers table
CREATE TABLE couriers(
	courier_id INT PRIMARY KEY,
	name TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- create table address
CREATE TABLE address(
	id INT(11) PRIMARY KEY,
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- add addres_id column and assign it as foreign key in table users
ALTER TABLE users ADD COLUMN address_id INT(11);
ALTER TABLE users ADD CONSTRAINT users_address FOREIGN KEY (address_id) REFERENCES address(id);



-- create table payment_method_descriptions
CREATE TABLE payment_method_descriptions(
	id INT(11) PRIMARY KEY,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT payment_method_descriptions_payment_methods FOREIGN KEY (id) REFERENCES payment_methods(id)
);


-- create user_payment_method_details
CREATE TABLE user_payment_method_details(
	no INT(11) PRIMARY KEY,
    user_id INTEGER,
    payment_method_id INT(11),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT user_payment_method_details_users FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT user_payment_method_details_payment_methods FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id)
);

-- add ongkos_dasar column to couriers table
ALTER TABLE couriers ADD COLUMN ongkos_dasar INT;

-- rename couriers table to shipppings
RENAME TABLE couriers TO shippings;

DROP TABLE shippings;


-- auxiliary query
-- SELECT * FROM couriers;
-- SELECT * FROM shippings;
-- SELECT * FROM users;

-- DROP DATABASE ata_online_shop;
-- DROP TABLE users;
-- DROP TABLE product;
-- DROP TABLE product_type;
-- DROP TABLE product_description;
-- DROP TABLE operators;
-- DROP TABLE shippings;
-- DROP TABLE couriers;
-- DROP TABLE transactions;
-- DROP TABLE transaction_details;
-- DROP TABLE payment_methods;
-- DROP TABLE payment_method_descriptions;
