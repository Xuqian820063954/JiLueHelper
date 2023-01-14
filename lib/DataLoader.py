import pandas as pd


def load_data(path, sheet_name):
    fm = pd.read_excel(path, sheet_name=sheet_name)
    return fm.values
