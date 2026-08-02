# Generated on 2026-08-02T08:50:50.181992

def calculate_loss(y_true, y_pred):
    import numpy as np
    return np.mean((y_true - y_pred)**2)
