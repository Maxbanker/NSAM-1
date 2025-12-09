import json
import os
from dataclasses import dataclass
from typing import Dict, Optional

try:
    import yaml  # type: ignore
except Exception:
    yaml = None

@dataclass
class WeaveMetrics:
    integrity: float
    twist: float

class TriTemporalBrane:
    """
    Minimal tri-temporal brane engine. In demo mode, tri-temporal is off by
    default; we compute synthetic twist from OISF gamma gradients.
    Config (YAML) keys honored if present:
      thresholds: {epsilon_psi, T_gamma, T_Omega, V_c, O_c, E_c, L_c}
      tri_temporal: bool
    """
    def __init__(self, config: Optional[str] = None):
        self.cfg = self._load_config(config)
        self.tri = bool(self.cfg.get("tri_temporal", False))
        self._last_gamma = None
        self._weave_int = 0.98
        self._twist = 0.0
        # Telemetry & logs
        os.makedirs("logs", exist_ok=True)
        self._log_path = os.path.join("logs", "flight_recorder.jsonl")
        # State cache for last emitted oisf
        self._last_oisf = None

    def _load_config(self, path: Optional[str]) -> Dict:
        defaults = {
            "thresholds": {
                "epsilon_psi": 0.60,
                "T_gamma": 0.15,
                "T_Omega": 0.75,
                "V_c": 0.65,
                "O_c": 0.80,
                "E_c": 0.80,
                "L_c": 0.20,
            },
            "tri_temporal": False,
        }
        if not path:
            return defaults
        if yaml is None:
            return defaults
        try:
            with open(path, "r") as f:
                user_cfg = yaml.safe_load(f) or {}
            # Shallow merge
            for k, v in (user_cfg or {}).items():
                if isinstance(v, dict) and isinstance(defaults.get(k), dict):
                    defaults[k].update(v)
                else:
                    defaults[k] = v
        except Exception:
            pass
        return defaults

    def ingest(self, state: Dict[str, float], oisf: Optional[Dict[str, float]] = None) -> None:
        # Update twist metric from gamma gradient (if oisf provided)
        if oisf is not None:
            g = float(oisf.get("gamma", 0.0))
            if self._last_gamma is None:
                dg = 0.0
            else:
                dg = max(0.0, g - self._last_gamma)
            self._last_gamma = g
            # Twist: rising gamma increases twist; decay otherwise
            self._twist = max(0.0, min(1.0, 0.9*self._twist + 0.8*dg))
            # Weave integrity decays slowly with gamma and twist
            self._weave_int = max(0.0, min(1.0, 0.995*self._weave_int - 0.01*g - 0.005*self._twist + 0.002))
            self._last_oisf = oisf
        # Log a compact line for audit
        try:
            with open(self._log_path, "a") as f:
                rec = {
                    "psi": self._last_oisf.get("psi") if self._last_oisf else None,
                    "gamma": self._last_oisf.get("gamma") if self._last_oisf else None,
                    "omega": self._last_oisf.get("omega") if self._last_oisf else None,
                    "weave_integrity": self._weave_int,
                    "twist": self._twist,
                }
                f.write(json.dumps(rec) + "\n")
        except Exception:
            pass

    def weave_integrity(self) -> float:
        return float(self._weave_int)

    def metrics(self) -> WeaveMetrics:
        return WeaveMetrics(integrity=self._weave_int, twist=self._twist)

@property
def last_oisf(self):
    return self._last_oisf or {}
