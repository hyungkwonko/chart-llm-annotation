import os
import numpy as np
from glob import glob

files = glob("./sample/*.json")
files = np.sort(files)

for i, file in enumerate(files):
    new_filename = f"./vl_{str(i).zfill(2)}.vl.json"
    os.rename(file, new_filename)