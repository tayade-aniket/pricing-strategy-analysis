USE PricingStrategyAnalysis;
GO

/*  Top Revenue Products */
SELECT TOP 10
    product_name,
    SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY product_name
ORDER BY total_revenue DESC;

/* Category Performance Analysis */
SELECT
    category,
    SUM(revenue) AS total_revenue,
    SUM(profit) AS total_profit,
    AVG(price) AS average_price
FROM sales_data
GROUP BY category
ORDER BY total_revenue DESC;

/* Discount Effectiveness Analysis */
SELECT
    discount_percentage,
    AVG(revenue) AS average_revenue,
    AVG(profit) AS average_profit,
    AVG(units_sold) AS average_units_sold
FROM sales_data
GROUP BY discount_percentage
ORDER BY average_revenue DESC;

/* Competitor Gap Analysis */
SELECT
    category,
    AVG(price - competitor_price) AS avg_price_gap,
    AVG(revenue) AS avg_revenue,
    AVG(profit) AS avg_profit
FROM sales_data
GROUP BY category
ORDER BY avg_price_gap DESC;

/* Regional Sales Performance */
SELECT
    region,
    SUM(revenue) AS total_revenue,
    SUM(profit) AS total_profit
FROM sales_data
GROUP BY region
ORDER BY total_revenue DESC;

/* Customer Segment Profitability */
SELECT
    segment,
    SUM(revenue) AS total_revenue,
    SUM(profit) AS total_profit,
    AVG(price) AS avg_price
FROM sales_data
GROUP BY segment
ORDER BY total_profit DESC;

/* Most Discounted Products */
SELECT TOP 10
    product_name,
    AVG(discount_percentage) AS avg_discount,
    SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY product_name
ORDER BY avg_discount DESC;

/* Profit Margin Analysis */
SELECT
    category,
    SUM(profit) / NULLIF(SUM(revenue), 0) * 100
        AS profit_margin_percentage
FROM sales_data
GROUP BY category
ORDER BY profit_margin_percentage DESC;

/* Revenue Trend Analysis */
SELECT
    YEAR(sales_date) AS sales_year,
    MONTH(sales_date) AS sales_month,
    SUM(revenue) AS monthly_revenue
FROM sales_data
GROUP BY
    YEAR(sales_date),
    MONTH(sales_date)
ORDER BY
    sales_year,
    sales_month;

/* Price Sensitivity Analysis */
SELECT
    category,
    AVG(price) AS avg_price,
    AVG(units_sold) AS avg_units_sold,
    AVG(revenue) AS avg_revenue
FROM sales_data
GROUP BY category
ORDER BY avg_price DESC;
