CREATE DATABASE ANALYTICS_DB;
CREATE SCHEMA STAGE;
CREATE TABLE STG_CLIENT
(
    ClientID INT,
    DateKey DATE NOT NULL,
    ProductKey INT NOT NULL,
    CustomerKey INT NOT NULL,
    StoreKey INT NOT NULL,
    SalesAmount DECIMAL(10, 2) NOT NULL,
    Quantity INT NOT NULL,
);
