# Optimizer for multi-objective PID tuning

class WeightedSumOptimizer:
    def __init__(self, weights):
        self.weights = weights

    def evaluate(self, metrics):
        """Return weighted sum of objectives."""
        return sum(w * m for w, m in zip(self.weights, metrics))
