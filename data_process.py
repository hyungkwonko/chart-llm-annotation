import json
import pandas as pd
import numpy as np
from glob import glob


vl_files = './assets/chart/*.json'
data_dir = './assets/data_raw/*'

vl_files = np.sort(glob(vl_files))
data_files = np.sort(glob(data_dir))

for i in range(len(vl_files)):
    with open(vl_files[i], "r") as file:
        vl = json.load(file)

    print(f"i: {i}, data_files[i]: {data_files[i]}")

    if data_files[i].endswith('.json'):
        df = pd.read_json(data_files[i])
        df.to_csv(data_files[i].replace('.json', '.csv').replace('data_raw', 'data_process'), index=False)
    elif data_files[i].endswith('.csv'):
        df = pd.read_csv(data_files[i])
        df.to_csv(data_files[i].replace('data_raw', 'data_process'), index=False)

