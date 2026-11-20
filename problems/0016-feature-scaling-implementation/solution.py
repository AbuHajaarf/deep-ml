import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Your code here

    x_max  = np.max(data,  axis=0)
    x_min  = np.min(data,  axis=0)
    x_mean = np.mean(data, axis=0)
    x_std  = np.std(data,  axis=0)
    
    standardized_data = np.round((data - x_mean) / x_std, 4)
    normalized_data = np.round((data - x_min) / (x_max - x_min), 4)


    return standardized_data, normalized_data