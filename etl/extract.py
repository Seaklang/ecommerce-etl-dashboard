import pandas as pd
from config import Config

def extract():
  df = pd.read_csv(Config.FILE_PATH,encoding="ISO-8859-1")
  print("Extracted Data:")
  print(df.head())
  return df