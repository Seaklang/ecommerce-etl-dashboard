from etl import extract, transform, load

def run_pipeline():
    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    run_pipeline()