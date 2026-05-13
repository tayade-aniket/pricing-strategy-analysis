/* Category Performance*/
CREATE VIEW category_performance AS

SELECT
    category,

    SUM(revenue) AS total_revenue,

    SUM(profit) AS total_profit,

    AVG(price) AS average_price,

    SUM(profit) /
    NULLIF(SUM(revenue), 0) * 100
        AS profit_margin_percentage

FROM sales_data

GROUP BY category;


/* Regional Performance View */
CREATE VIEW regional_performance AS

SELECT
    region,
    SUM(revenue) AS total_revenue,
    SUM(profit) AS total_profit

FROM sales_data

GROUP BY region;


/* Customer Segment Performance View */
CREATE VIEW customer_segment_performance AS

SELECT
    segment,
    SUM(revenue) AS total_revenue,
    SUM(profit) AS total_profit,
    AVG(price) AS average_price

FROM sales_data

GROUP BY segment;


/* Discount Effectiveness View */
CREATE VIEW discount_effectiveness AS

SELECT
    discount_percentage,
    AVG(revenue) AS average_revenue,
    AVG(profit) AS average_profit,
    AVG(units_sold) AS average_units_sold

FROM sales_data

GROUP BY discount_percentage;

/* Competitor Pricing View */
CREATE VIEW competitor_pricing_analysis AS

SELECT
    category,

    AVG(price) AS average_price,

    AVG(competitor_price)
        AS average_competitor_price,

    AVG(price - competitor_price)
        AS average_price_gap

FROM sales_data

GROUP BY category;


/* Monthly Revenue Trend View */
CREATE VIEW monthly_revenue_trend AS

SELECT
    YEAR(sales_date) AS sales_year,

    MONTH(sales_date) AS sales_month,

    SUM(revenue) AS monthly_revenue,

    SUM(profit) AS monthly_profit

FROM sales_data

GROUP BY
    YEAR(sales_date),
    MONTH(sales_date);

