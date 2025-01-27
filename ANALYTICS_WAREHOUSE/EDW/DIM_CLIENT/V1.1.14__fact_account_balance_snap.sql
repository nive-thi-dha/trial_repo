CREATE TABLE FACT_ACCOUNT_BALANCE_SNAP
(
    SalesID INT,
    DateKey DATE NOT NULL,
    ProductKey INT NOT NULL,
    CustomerKey INT NOT NULL,
    StoreKey INT NOT NULL,
    SalesAmount DECIMAL(10, 2) NOT NULL,
    Quantity INT NOT NULL,
    Discount DECIMAL(5, 2)
);
