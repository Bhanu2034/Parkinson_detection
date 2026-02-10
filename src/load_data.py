import pandas as pd

def load_dataset(path):
    data = pd.read_csv(path)
    data = data.drop("name", axis=1)
    return data
