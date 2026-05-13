from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd


def sales_forecast(df):

    forecast_df = df.copy()

    forecast_df = forecast_df.sort_values(by="sales_date")

    forecast_df["day_number"] = np.arange(len(forecast_df))

    X = forecast_df[["day_number"]]
    y = forecast_df["units_sold"]

    model = LinearRegression()

    model.fit(X, y)

    future_days = pd.DataFrame(
        {
            "day_number": range(len(forecast_df), len(forecast_df) + 30),
        }
    )

    predictions = model.predict(future_days)

    return predictions
