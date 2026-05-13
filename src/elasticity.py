import pandas as pd


def calculate_elasticity(df):

    elasticity_df = df.copy()

    elasticity_df = elasticity_df.sort_values(by="price")

    elasticity_df["pct_change_quantity"] = elasticity_df["units_sold"].pct_change()

    elasticity_df["pct_change_price"] = elasticity_df["price"].pct_change()

    elasticity_df["elasticity"] = (
        elasticity_df["pct_change_quantity"] / elasticity_df["pct_change_price"]
    )

    elasticity_df.replace([float("inf"), -float("inf")], 0, inplace=True)

    elasticity_df.fillna(0, inplace=True)

    return elasticity_df
