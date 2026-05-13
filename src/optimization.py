import pandas as pd


def simulate_price_change(df, percentage):

    simulation_df = df.copy()

    simulation_df["new_price"] = simulation_df["price"] * (1 + percentage / 100)

    elasticity_factor = -1.2

    simulation_df["new_units_sold"] = simulation_df["units_sold"] * (
        1 + elasticity_factor * (percentage / 100)
    )

    simulation_df["new_revenue"] = (
        simulation_df["new_price"] * simulation_df["new_units_sold"]
    )

    return simulation_df
