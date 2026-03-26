from db import connect

def load(df):
    conn = connect()
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute(
            """
            INSERT INTO sales 
            (invoice_no, stock_code, description, quantity, invoice_date, price, customer_id, country)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                row["InvoiceNo"],
                row["StockCode"],
                row["Description"],
                int(row["Quantity"]),
                row["InvoiceDate"],
                float(row["UnitPrice"]),
                int(row["CustomerID"]),
                row["Country"]
            )
        )

    conn.commit()
    cur.close()
    conn.close()

    print("Data loaded!")