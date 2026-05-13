/* Stored Procedures */
CREATE PROCEDURE GetTopRevenueProducts
AS
BEGIN

    SELECT TOP 10
        product_name,
        SUM(revenue) AS total_revenue
    FROM sales_data
    GROUP BY product_name
    ORDER BY total_revenue DESC;

END;
GO

/* Category Performance Procedure */
CREATE PROCEDURE GetCategoryPerformance
AS
BEGIN

    SELECT
        category,
        SUM(revenue) AS total_revenue,
        SUM(profit) AS total_profit
    FROM sales_data
    GROUP BY category
    ORDER BY total_revenue DESC;

END;
GO

/* Regional Sales Procedure */
CREATE PROCEDURE GetRegionalSales
AS
BEGIN

    SELECT
        region,
        SUM(revenue) AS total_revenue,
        SUM(profit) AS total_profit
    FROM sales_data
    GROUP BY region
    ORDER BY total_revenue DESC;

END;
GO

/* Discount Analysis Procedure */
CREATE PROCEDURE GetDiscountAnalysis
AS
BEGIN

    SELECT
        discount_percentage,
        AVG(revenue) AS average_revenue,
        AVG(profit) AS average_profit
    FROM sales_data
    GROUP BY discount_percentage
    ORDER BY average_revenue DESC;

END;
GO

/* Competitor Pricing Procedure */
CREATE PROCEDURE GetCompetitorPricingGap
AS
BEGIN

    SELECT
        category,
        AVG(price - competitor_price)
            AS average_price_gap
    FROM sales_data
    GROUP BY category
    ORDER BY average_price_gap DESC;

END;
GO

/* Monthly Revenue Trend Procedure */ 
CREATE PROCEDURE GetMonthlyRevenueTrend
AS
BEGIN

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

END;
GO
