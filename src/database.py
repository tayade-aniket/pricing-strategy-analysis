from sqlalchemy import create_engine
from src.config import CONNECTION_STRING
import pandas as pd

engine = create_engine(CONNECTION_STRING)


def upload_dataframe(df, table_name):

    try:
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)

        print(f"Data uploaded successfully to {table_name}")

    except Exception as e:
        print("Database Upload Error:", e)


def fetch_data(query):

    try:
        df = pd.read_sql(query, engine)

        return df

    except Exception as e:
        print("Database Fetch Error:", e)
