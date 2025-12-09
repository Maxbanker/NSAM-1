from dataclasses import dataclass
from typing import Dict

@dataclass
class OISFState:
    psi: float   # recursion coherence (0..1)
    gamma: float # drift/collapse pressure (0..1)
    omega: float # global route budget / negentropy state (0..1)

class OISFCore:
    """Observer-Invariance Signal Fusion (minimal working stub).
    Computes {psi, gamma, omega} from incoming plant state using
    simple, transparent transforms. Replace with your full model later.
    """
    def __init__(self):
        # Deterministic parameters
        self.alpha = 0.03  # smoothing
        self._psi = 0.95
        self._gamma = 0.05
        self._omega = 0.85

    def update(self, state: Dict[str, float]) -> OISFState:
        # Very lightweight proxies for demo purposes
        # Use normalized temperature/pressure deltas to shape gamma
        t_core = state.get("core_temp_K", 600.0)
        p_pri  = state.get("primary_pressure_MPa", 12.0)
        f_cool = state.get("flow_rate_kg_s", 0.0)

        # Drift pressure rises when cooling flow falls while T rises
        gamma_obs = max(0.0, min(1.0, 0.5*(t_core-580.0)/200.0 + 0.5*(12.0 - min(p_pri, 12.0))/6.0 + 0.3*(1.0 - min(f_cool/50.0, 1.0))))
        self._gamma = (1-self.alpha)*self._gamma + self.alpha*gamma_obs

        # Psi coherence decreases with rising gamma
        self._psi = max(0.0, min(1.0, 1.0 - 0.7*self._gamma))

        # Omega (negentropy reserve) drains with gamma, recovers slowly
        self._omega = max(0.0, min(1.0, self._omega + 0.01 - 0.03*self._gamma))
        return OISFState(psi=self._psi, gamma=self._gamma, omega=self._omega)
