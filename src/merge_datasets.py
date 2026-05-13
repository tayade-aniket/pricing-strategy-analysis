import pandas as pd


def merge_datasets(retail_df, superstore_df, survey_df):

    # =========================
    # PRIMARY DATASET
    # =========================

    merged_df = superstore_df.copy()

    print("Using Superstore dataset as primary fact table...")

    # =========================
    # CREATE BUSINESS METRICS
    # =========================

    merged_df["revenue"] = merged_df["sales"]

    merged_df["units_sold"] = merged_df["quantity"]

    merged_df["price"] = merged_df["sales"] / merged_df["quantity"]

    # Simulated competitor pricing
    merged_df["competitor_price"] = merged_df["price"] * 1.05

    # Discount %
    merged_df["discount_percentage"] = merged_df["discount"] * 100

    # Standardized sales date
    merged_df["sales_date"] = merged_df["order_date"]

    # =========================
    # RETAIL DATASET AGGREGATION
    # =========================

    if "product_category" in retail_df.columns and "value" in retail_df.columns:
        retail_summary = (
            retail_df.groupby("product_category")["value"].mean().reset_index()
        )

        retail_summary.rename(
            columns={"product_category": "category", "value": "market_average_value"},
            inplace=True,
        )

        merged_df = pd.merge(merged_df, retail_summary, on="category", how="left")

        print("Retail dataset merged successfully.")

    else:
        merged_df["market_average_value"] = 0

        print("Retail dataset aggregation skipped.")

    # =========================
    # SURVEY DATASET AGGREGATION
    # =========================

    if "sku_category" in survey_df.columns and "sales_amount" in survey_df.columns:
        survey_summary = (
            survey_df.groupby("sku_category")
            .agg({"sales_amount": "mean", "quantity": "mean"})
            .reset_index()
        )

        survey_summary.rename(
            columns={
                "sku_category": "category",
                "sales_amount": "avg_market_sales",
                "quantity": "avg_market_quantity",
            },
            inplace=True,
        )

        merged_df = pd.merge(merged_df, survey_summary, on="category", how="left")

        print("Survey dataset merged successfully.")

    else:
        merged_df["avg_market_sales"] = 0
        merged_df["avg_market_quantity"] = 0

        print("Survey dataset aggregation skipped.")

    # =========================
    # HANDLE NULL VALUES
    # =========================

    merged_df.fillna(0, inplace=True)

    # =========================
    # FINAL COLUMN CLEANUP
    # =========================

    final_columns = [
        "order_id",
        "product_id",
        "product_name",
        "category",
        "sub_category",
        "region",
        "segment",
        "sales_date",
        "price",
        "competitor_price",
        "discount_percentage",
        "units_sold",
        "revenue",
        "profit",
        "market_average_value",
        "avg_market_sales",
        "avg_market_quantity",
    ]

    # Create missing columns safely
    for column in final_columns:
        if column not in merged_df.columns:
            merged_df[column] = 0

    merged_df = merged_df[final_columns]

    print("Dataset merging completed successfully.")

    return merged_df
