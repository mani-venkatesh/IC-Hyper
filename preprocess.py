import time 
import numpy as np

def preprocess(patient_dict):   
    start = time.time()

    charis1 = patient_dict['charis1']['s']
    icp_data = charis1[:,2]

    w = 60000 # window length, 20 mins default (60000 samples)
    st = 3000 # 5% of window length - steps
    d = 60 # downsample factor 
    u = 50 # upper bound 50mmHg for ICP
    l = -5 # lower bound -5mmHg for ICP

    i = 1 # while loop counter
    while i + w < len(icp_data):
        seg = icp_data[i:i+w] # window segment

        # Create a mask for values outside the acceptable ICP bound
        icp_mask = ((seg > 50) | (seg < -5))
        seg[icp_mask] = np.nan

        m = np.nanmean(seg) # segment mean
        s = np.nanstd(seg) # segment standard deviation
        s_bounds = (m+3*s, m-3*s) # outlier boundaries (+/-3 times standard deviation)

        # Create a mask for values outside the std bounds
        std_mask = ((seg > s_bounds[0]) | (seg < s_bounds[1]))
        seg[std_mask] = m

        # Create a mask to replace nan values with segment mean 
        nan_mask = (np.isnan(seg))
        seg[nan_mask] = m

        # Store modified segment back into ICP data
        icp_data[i:i+w] = seg

        # Step to next segment position
        i += st

    # Downsample data by d steps
    d_icp_data = icp_data[::d]

    end = time.time()

    print("Preprocessing step complete")
    print(f"Trial length: {len(icp_data)}. Downsampled to: {len(d_icp_data)}")
    print(f"Time elapsed: {end-start} seconds")
    return d_icp_data
