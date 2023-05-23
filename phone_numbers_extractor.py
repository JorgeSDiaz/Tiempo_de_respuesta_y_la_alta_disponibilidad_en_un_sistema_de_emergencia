import pandas as pd


def extract_numbers_from_google_csv(path: str) -> list:
    data_frame = pd.read_csv(path)

    return list(map(lambda x: str(x), data_frame["Phone 1 - Value"]))
