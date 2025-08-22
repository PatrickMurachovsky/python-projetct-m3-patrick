# mean_var_std.py
import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    a = np.array(lst).reshape(3, 3)

    cols_mean = a.mean(axis=0).tolist()
    rows_mean = a.mean(axis=1).tolist()
    flat_mean = a.mean().item()

    cols_var = a.var(axis=0).tolist()
    rows_var = a.var(axis=1).tolist()
    flat_var = a.var().item()

    cols_std = a.std(axis=0).tolist()
    rows_std = a.std(axis=1).tolist()
    flat_std = a.std().item()

    cols_max = a.max(axis=0).tolist()
    rows_max = a.max(axis=1).tolist()
    flat_max = a.max().item()

    cols_min = a.min(axis=0).tolist()
    rows_min = a.min(axis=1).tolist()
    flat_min = a.min().item()

    cols_sum = a.sum(axis=0).tolist()
    rows_sum = a.sum(axis=1).tolist()
    flat_sum = a.sum().item()

    calculations = {
        'mean': [cols_mean, rows_mean, flat_mean],
        'variance': [cols_var, rows_var, flat_var],
        'standard deviation': [cols_std, rows_std, flat_std],
        'max': [cols_max, rows_max, flat_max],
        'min': [cols_min, rows_min, flat_min],
        'sum': [cols_sum, rows_sum, flat_sum]
    }
    return calculations

