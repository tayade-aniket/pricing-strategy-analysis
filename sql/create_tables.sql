USE PricingStrategyAnalysis;
GO

CREATE TABLE sales_data (
    id INT IDENTITY(1,1) PRIMARY KEY,
    order_id VARCHAR(100),
    product_id VARCHAR(100),
    product_name VARCHAR(255),
    category VARCHAR(100),
    region VARCHAR(100),
    sales_date DATE,
    price DECIMAL(10,2),
    competitor_price DECIMAL(10,2),
    discount DECIMAL(5,2),
    units_sold INT,
    revenue DECIMAL(12,2),
    profit DECIMAL(12,2),
    customer_segment VARCHAR(100),
    holiday BIT,
    season VARCHAR(50)
);
GO