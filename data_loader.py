# Generated on 2026-08-09T12:09:06.535872

def calculate_loss(y_true, y_pred):
    import numpy as np
    return np.mean((y_true - y_pred)**2)
