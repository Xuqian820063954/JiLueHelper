import pandas as pd


def load_data(path):
    fm = pd.read_excel(path, sheet_name='Sheet1')
    return fm.values
