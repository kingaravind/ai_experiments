# Generated on 2026-08-12T21:29:28.250937

def calculate_loss(y_true, y_pred):
    import numpy as np
    return np.mean((y_true - y_pred)**2)
