from sklearn.cluster import KMeans
import pandas as pd


def customer_segmentation(df):

    segment_df = df.copy()

    # =========================
    # HANDLE COLUMN DIFFERENCES
    # =========================

    if "customer_segment" in segment_df.columns:
        segment_column = "customer_segment"

    elif "segment" in segment_df.columns:
        segment_column = "segment"

    else:
        segment_df["segment"] = "Consumer"

        segment_column = "segment"

    # =========================
    # CREATE CUSTOMER FEATURES
    # =========================

    customer_features = segment_df.groupby(segment_column)[["revenue", "profit"]].sum()

    # =========================
    # KMEANS CLUSTERING
    # =========================

    model = KMeans(n_clusters=3, random_state=42, n_init=10)

    customer_features["cluster"] = model.fit_predict(customer_features)

    customer_features.reset_index(inplace=True)

    print("Customer segmentation completed successfully.")

    return customer_features
