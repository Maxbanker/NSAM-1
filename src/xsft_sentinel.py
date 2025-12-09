from dataclasses import dataclass
from typing import Optional

@dataclass
class SentinelConfig:
    threshold_twist: float = 0.67
    epsilon_psi: float = 0.60
    T_gamma: float = 0.15
    T_Omega: float = 0.75

class CollapseSentinel:
    """Symbolic collapse detector.
    OR-clause: psi < ε  OR  (gamma > Tγ AND omega < TΩ)  OR  twist > threshold_twist
    """
    def __init__(self, threshold_twist: float = 0.67,
                 epsilon_psi: float = 0.60,
                 T_gamma: float = 0.15,
                 T_Omega: float = 0.75):
        self.cfg = SentinelConfig(threshold_twist, epsilon_psi, T_gamma, T_Omega)

    def detect(self, brane: 'TriTemporalBrane') -> bool:  # forward ref ok
        m = brane.metrics()
        o = brane.last_oisf
        psi = float(o.get("psi", 1.0))
        gamma = float(o.get("gamma", 0.0))
        omega = float(o.get("omega", 1.0))
        if psi < self.cfg.epsilon_psi:
            return True
        if (gamma > self.cfg.T_gamma) and (omega < self.cfg.T_Omega):
            return True
        if m.twist > self.cfg.threshold_twist:
            return True
        return False
