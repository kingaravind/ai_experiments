# Generated on 2026-08-10T09:15:03.706193

def calculate_loss(y_true, y_pred):
    import numpy as np
    return np.mean((y_true - y_pred)**2)
