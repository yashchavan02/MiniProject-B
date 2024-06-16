CREATE DATABASE bank;

USE bank;

CREATE TABLE customerdata(
name VARCHAR(25),
email VARCHAR(15),
gender CHAR,
pin INT,
bank_acc BIGINT
);

SELECT * FROM customerdata;

DROP TABLE cusromerdata;

CREATE TABLE customerdata(
name VARCHAR(30),
email VARCHAR(30),
gender CHAR,
pin INT,
bank_acc BIGINT
);

SELECT * FROM customerdata;

