# Generated on 2026-08-07T18:09:17.340773

def calculate_loss(y_true, y_pred):
    import numpy as np
    return np.mean((y_true - y_pred)**2)
