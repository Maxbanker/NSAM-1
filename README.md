    # NSAM-1 — Negentropic Severe Accident Mitigation Framework v1.0

    **Author:** Steven Lanier-Egu  
**Division:** SEAL Division (Systems for Entropic-Alignment & Longevity)  
**License:** MIT  
**Status:** Demo-ready, simulation-only

 **Safety & Regulatory Disclaimer**  

 This repository is a **research simulation**. It is **not** a plant control system and must not be used for operational decision-making. Some adapters may interface with licensed codes (RELAP5/TRACE). You are responsible for complying with all license, export, and site rules.

## What it does
NSAM-1 detects **symbolic collapse** during a Station Blackout + Loss of Ultimate Heat Sink and **autonomously re-weaves** passive cooling pathways. In the demo configuration, the run halts with a successful recovery and a full audit trail.

## Quickstart (one-command demo)
```bash
python -m venv .venv && source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
make demo
```

You should see output like:
- steady operation → rising twist stress around ~6–7 h
- `COLLAPSE DETECTED` → autonomous recovery engaged
- final lines report weave integrity, max twist, and a success message

  ## Repo layout (essentials)
- `src/relap_interface.py` — CSV replay/live-gated socket

- `src/oisf_core.py` — observer-invariance signal fusion → {psi, gamma, omega}

- `src/hyperverse_brane.py` — brane engine, twist & integrity metrics, audit logs

- `src/xsft_sentinel.py` — collapse predicate (psi/γ/Ω + twist)

- `src/weaver11.py` — passive-first recovery plan generator

- `src/omega_governor.py` — VOEL gates & conservation boundary

- `examples/demo_sbo_luhs.py` — end-to-end runnable demo

- `simulation_data/sample_relap5_sbo.csv` — public stub trace

- `configs/nuscale_sbo.yaml` — thresholds & toggles

- `configs/recovery_substrates.yaml` — ranked passive pathways

  ## Configuration
`configs/nuscale_sbo.yaml` holds demo defaults:
- collapse thresholds (`epsilon_psi`, `T_gamma`, `T_Omega`)

- governance gates (`V_c`, `O_c`, `E_c`, `L_c`)

- `tri_temporal` toggle (off by default)

  ## Live mode (off by default)
  The `RelapLive` socket pathway is feature-gated. To experiment:

  ```bash
  export NSAM_ENABLE_LIVE=1  # or set in your environment

  ```
  Implement your plant/solver socket in `relap_interface.py` before use.

  ## Authorship & credit
- Primary author: **Steven Lanier-Egu**

- With gratitude to the **SEAL Division** (Systems for Entropic-Alignment & Longevity) for research support and review.

- Community contributions welcome via PRs.

  ## Citation
  If you use this work, please cite:

  > Steven Lanier-Egu (2025). *NSAM-1: Negentropic Severe Accident Mitigation Framework v1.0*. GitHub. [https://doi.org/10.5281/zenodo.17862457](https://doi.org/10.5281/zenodo.17862457)

  ## Ethics & dual-use
  NSAM-1 includes governance gates (VOEL) and audit trails. Please keep the simulation context clear in publications and demos.

