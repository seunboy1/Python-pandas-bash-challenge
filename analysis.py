import json 
import pandas as pd


def load_csv():
    df = pd.read_csv('assets/file.csv')
    df.columns = ["Name", "Size"]
    return df

def analyze_data():
    df = load_csv()

    value = {
        "Average": int(df["Size"].mean()),
        "Maximum": int(df["Size"].max()),
        "Minimum": int(df["Size"].min())
        # "Histogram": df["Size"].plot(kind='hist')
    }
    return value
