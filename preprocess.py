import json
import pandas as pd
import numpy as np
from glob import glob


def get_fields_and_types(json_data):
    fields = []
    types = []
    if isinstance(json_data, dict):
        if "field" in json_data:
            if isinstance(json_data["field"], str):
                fields.append(json_data["field"])
                if "type" in json_data and isinstance(json_data["type"], str):
                    types.append(json_data["type"])
                else:
                    types.append("unknown")
        for _, v in json_data.items():
            if isinstance(v, (dict, list)):
                f, t = get_fields_and_types(v)
                fields.extend(f)
                types.extend(t)
    elif isinstance(json_data, list):
        for item in json_data:
            if isinstance(item, (dict, list)):
                f, t = get_fields_and_types(item)
                fields.extend(f)
                types.extend(t)
    return fields, types

vl_files = './assets/chart/*.json'
data_dir = './assets/data_raw/*'

vl_files = np.sort(glob(vl_files))
data_files = np.sort(glob(data_dir))

for i in range(len(vl_files)):
	with open(vl_files[i], "r") as file:
		vl = json.load(file)
	keys, _ = get_fields_and_types(vl)

	print(f"i: {i}, data_files[i]: {data_files[i]}, keys: {keys}")

	if data_files[i].endswith('.json'):
		df = pd.read_json(data_files[i])
		new_keys = [key for key in keys if key in df.columns]
		subset = df[new_keys]
		subset.to_csv(data_files[i].replace('.json', '.csv').replace('data_raw', 'data_process'), index=False)
	elif data_files[i].endswith('.csv'):
		df = pd.read_csv(data_files[i])
		new_keys = [key for key in keys if key in df.columns]
		subset = df[new_keys]
		subset.to_csv(data_files[i].replace('data_raw', 'data_process'), index=False)

