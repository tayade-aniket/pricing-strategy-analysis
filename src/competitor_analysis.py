import pandas as pd


def competitor_gap_analysis(df):

    analysis_df = df.copy()

    analysis_df["price_gap"] = analysis_df["price"] - analysis_df["competitor_price"]

    summary = analysis_df.groupby("category")["price_gap"].mean().reset_index()

    return summary
