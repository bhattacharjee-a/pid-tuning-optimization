# Basic PID controller implementation

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def compute(self, error, dt):
        """Compute PID output (simplified)."""
        p = self.kp * error
        i = self.ki * error * dt
        d = self.kd * (error / dt)
        return p + i + d
