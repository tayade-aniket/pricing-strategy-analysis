import matplotlib.pyplot as plt
import seaborn as sns


def revenue_by_category(df):

    category_revenue = (
        df.groupby("category")["revenue"].sum().sort_values(ascending=False)
    )

    plt.figure(figsize=(12, 6))

    sns.barplot(x=category_revenue.index, y=category_revenue.values)

    plt.xticks(rotation=45)

    plt.title("Revenue by Category")

    plt.show()


def price_vs_demand(df):

    plt.figure(figsize=(10, 6))

    sns.scatterplot(data=df, x="price", y="units_sold", hue="category")

    plt.title("Price vs Demand")

    plt.show()
