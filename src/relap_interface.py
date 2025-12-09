import csv
import os
from typing import Dict, Iterator, Tuple, Optional

class RelapLive:
    """
    Dual-mode plant data source:
      • CSV replay (public sample) — deterministic and reproducible
      • Socket/live mode placeholder (feature-gated)
    Expects a CSV with a 'time_hours' column. Any additional columns are
    passed through as telemetry state.
    """
    def __init__(self, source: str, live: bool = False, rate_hz: float = 1.0):
        self.source = source
        self.live = live and (os.getenv("NSAM_ENABLE_LIVE") == "1")
        self.rate_hz = rate_hz
        self._validate()

    def _validate(self) -> None:
        if self.live:
            # Placeholder: real plant/solver socket would be initialized here.
            # We intentionally gate this behind NSAM_ENABLE_LIVE=1
            return
        if not os.path.exists(self.source):
            raise FileNotFoundError(f"CSV replay not found: {self.source}")

    def stream(self) -> Iterator[Tuple[float, Dict[str, float]]]:
        if self.live:
            # Placeholder for live socket streaming — intentionally disabled by default
            raise RuntimeError("Live mode is not enabled in this build. Set NSAM_ENABLE_LIVE=1 and implement socket.")
        with open(self.source, "r", newline="") as f:
            reader = csv.DictReader(f)
            if "time_hours" not in reader.fieldnames:
                raise ValueError("CSV must contain a 'time_hours' column")
            for row in reader:
                t = float(row["time_hours"])  # hours
                # Convert remaining fields to floats when possible
                state: Dict[str, float] = {}
                for k, v in row.items():
                    if k == "time_hours":
                        continue
                    try:
                        state[k] = float(v)
                    except (TypeError, ValueError):
                        continue
                yield t, state

def __repr__(self):
    return f"<RelapLive source={self.source} mode={'LIVE' if self.live else 'REPLAY'}>"
