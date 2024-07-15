import wfdb
from IPython.display import display
import os
import numpy as np
import time
from load_data import load_data
from preprocess import preprocess

if __name__ == "__main__":
    records_path = "database/RECORDS"
    patient_dict = load_data(records_path)
    icp_data = preprocess(patient_dict)