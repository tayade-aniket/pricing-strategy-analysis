import pandas as pd


def clean_retail_price_data(path):

    df = pd.read_csv(path)

    df.drop_duplicates(inplace=True)

    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

    df.ffill(inplace=True)

    return df


def clean_superstore_data(path):

    df = pd.read_csv(path, encoding="latin1")

    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

    df["order_date"] = pd.to_datetime(df["order_date"])

    return df


def clean_price_survey_data(path):

    df = pd.read_csv(path)

    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

    return df
