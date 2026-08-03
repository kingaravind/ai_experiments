# Generated on 2026-08-03T07:46:58.805569

def calculate_loss(y_true, y_pred):
    import numpy as np
    return np.mean((y_true - y_pred)**2)
