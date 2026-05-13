from src.preprocessing import (
    clean_retail_price_data,
    clean_superstore_data,
    clean_price_survey_data,
)

from src.merge_datasets import merge_datasets
from src.elasticity import calculate_elasticity
from src.optimization import simulate_price_change
from src.competitor_analysis import competitor_gap_analysis
from src.customer_segmentation import customer_segmentation
from src.forecasting import sales_forecast
from src.database import upload_dataframe
from src.utils import save_csv


def main():

    print("Starting Pricing Strategy Analysis Pipeline...")

    # =========================
    # LOAD DATASETS
    # =========================

    retail_df = clean_retail_price_data("data/raw/retail_price_optimization.csv")

    superstore_df = clean_superstore_data("data/raw/superstore.csv")

    survey_df = clean_price_survey_data("data/raw/retail_price_survey.csv")

    print("Datasets loaded successfully.")

    # =========================
    # MERGE DATASETS
    # =========================

    merged_df = merge_datasets(retail_df, superstore_df, survey_df)

    print("Dataset merge completed.")

    # =========================
    # ELASTICITY ANALYSIS
    # =========================

    elasticity_df = calculate_elasticity(merged_df)

    print("Elasticity analysis completed.")

    # =========================
    # PRICE OPTIMIZATION
    # =========================

    optimized_df = simulate_price_change(merged_df, 5)

    print("Revenue optimization simulation completed.")

    # =========================
    # COMPETITOR ANALYSIS
    # =========================

    competitor_df = competitor_gap_analysis(merged_df)

    print("Competitor analysis completed.")

    # =========================
    # CUSTOMER SEGMENTATION
    # =========================

    customer_segments = customer_segmentation(merged_df)

    print("Customer segmentation completed.")

    # =========================
    # SALES FORECASTING
    # =========================

    predictions = sales_forecast(merged_df)

    print("Sales forecasting completed.")

    # =========================
    # SAVE CSV OUTPUTS
    # =========================

    save_csv(merged_df, "data/processed/merged_dataset.csv")

    save_csv(elasticity_df, "data/processed/elasticity_output.csv")

    save_csv(optimized_df, "data/processed/optimized_output.csv")

    save_csv(competitor_df, "data/processed/competitor_analysis.csv")

    save_csv(customer_segments, "data/processed/customer_segments.csv")

    print("All processed files saved.")

    # =========================
    # SQL SERVER UPLOAD
    # =========================

    upload_dataframe(merged_df, "sales_data")

    print("Data uploaded to SQL Server.")

    print("\\nPROJECT PIPELINE EXECUTED SUCCESSFULLY")


if __name__ == "__main__":
    main()
