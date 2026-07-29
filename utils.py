# Generated on 2026-07-29T18:04:50.729152

def calculate_loss(y_true, y_pred):
    import numpy as np
    return np.mean((y_true - y_pred)**2)
