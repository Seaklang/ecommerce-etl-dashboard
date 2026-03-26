import pandas as pd

def transform(df):
    print("Original shape:", df.shape)

    # Check missing
    missing_ratio = df.isnull().mean()
    print("Missing ratio:\n", missing_ratio)

    # Drop critical missing
    df = df.dropna(subset=[
        "InvoiceNo",
        "StockCode",
        "Quantity",
        "UnitPrice",
        "InvoiceDate"
    ])

    # Fill non-critical
    df["Description"] = df["Description"].fillna("Unknown")
    df["Country"] = df["Country"].fillna(df["Country"].mode()[0])
    df["CustomerID"] = df["CustomerID"].fillna(0)

    # Convert types
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Remove invalid values
    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]

    # Remove duplicates
    df = df.drop_duplicates()

    # Clean text
    df["Description"] = df["Description"].str.strip()

    # Add business column
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    # Outlier flag (keep but mark)
    Q3 = df["Quantity"].quantile(0.75)
    IQR = Q3 - df["Quantity"].quantile(0.25)
    upper = Q3 + 1.5 * IQR

    df["is_bulk_order"] = df["Quantity"] > upper

    # Limit for testing
    df = df.head(1000)

    print("Transformed shape:", df.shape)
    return df