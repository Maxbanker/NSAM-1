from dataclasses import dataclass
from typing import Any

@dataclass
class OmegaGate:
    V_c: float = 0.65
    O_c: float = 0.80
    E_c: float = 0.80
    L_c: float = 0.20

class OmegaKernel:
    """Proof-obligation kernel & conservation boundary checks.
    For demo: V (validity) derives from weave integrity; O (oversight) is 1.0;
    E (safety envelope) is 0.9; L (leak) derives from twist.
    """
    def __init__(self, gates: 'OmegaGate'|None=None):
        self.g = gates or OmegaGate()

    def _compute_voel(self, brane: 'TriTemporalBrane'):
        m = brane.metrics()
        V = float(m.integrity)
        O = 1.0
        E = 0.90
        L = float(0.5*m.twist)  # higher twist → higher leak proxy
        return V, O, E, L

    def validate(self, plan: Any, brane: 'TriTemporalBrane'|None=None) -> bool:
        if brane is None:
            return True
        V, O, E, L = self._compute_voel(brane)
        export_allowed = (E >= self.g.E_c) and (V >= self.g.V_c) and (O >= self.g.O_c) and (L < self.g.L_c)
        # record a simple audit line
        try:
            with open("logs/omega_gate.jsonl", "a") as f:
                f.write(str({"V":V, "O":O, "E":E, "L":L, "export_allowed": export_allowed})+"\n")
        except Exception:
            pass
        return export_allowed
