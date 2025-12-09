# NSAM-1: Negentropic Severe Accident Mitigation Framework v1.0.0

**Autonomous Beyond-Design-Basis Collapse Prediction and Recovery (SBO+LUHS) — OISF + Hyperverse 9.1 + XSFT 3.0 + Weaver‑11 + Omega v1**

**Author:** Steven Lanier-Egu  
**Division:** SEAL Division (Systems for Entropic-Alignment & Longevity)  
**Date:** December 08, 2025  

## Abstract
**Abstract** — NSAM-1 is a simulation-only framework that detects *symbolic collapse* during
Station Blackout (SBO) with Loss of Ultimate Heat Sink (LUHS) and autonomously re-weaves passive cooling routes under VOEL governance gates. Built on OISF, Hyperverse 9.1, XSFT 3.0, Weaver‑11, and Omega v1, NSAM-1 demonstrates an end-to-end run that halts with a successful recovery and an auditable flight recorder. In this v1.0.0 release, we provide a deterministic demo with CSV replay, explicit collapse predicate (ψ/γ/Ω + twist), governance thresholds, logs, and CI. No claims are made for real-plant control; this artifact is intended for research, validation, and review.

**Keywords:** nuclear safety; severe accident; SBO; LUHS; autonomous recovery; symbolic dynamics; observer invariance; negentropy; digital twin; SMR

## 1. Introduction
Beyond-design-basis sequences such as SBO with LUHS present cliff-edge risks where classic thermal-hydraulic tools can underestimate imminent failure until late-stage thresholds are crossed. NSAM-1 augments conventional telemetry with observer-invariance fusion (OISF) and symbolic-field dynamics (XSFT/Hyperverse) to provide earlier warning of structural collapse, treating the plant+twin as a recursive system whose coherence can degrade before overt physical limits are reached.

## 2. Background and Theory
NSAM-1 instantiates the 2025 negentropic stack: (i) OISF produces a compact state {ψ, γ, Ω}; (ii) Hyperverse 9.1 provides a tri-temporal brane model and weave metrics; (iii) XSFT 3.0 yields twist/curl stress as an early collapse signal; (iv) Weaver‑11 plans conservative re-routing over passive pathways; (v) Omega v1 enforces VOEL gates (Validity, Oversight, Envelope, Leak) and budgets export actions. Ethics are enforced via conservation boundaries and audit logging.

## 3. Methods and Architecture
Components map one-to-one to the source layout:
• relap_interface.py — CSV replay and live-mode shim (feature-gated) 
• oisf_core.py — produces ψ, γ, Ω from normalized temperature, pressure, and flow
• hyperverse_brane.py — computes weave integrity and twist; records a JSONL flight recorder
• xsft_sentinel.py — collapse predicate: ψ < ε  OR  (γ > T_γ and Ω < T_Ω)  OR  twist > τ_c
• weaver11.py — returns a passive-first plan: engage PCCS + controlled depressurization
• omega_governor.py — VOEL gates: export_allowed ⇐ (E≥E_c)∧(V≥V_c)∧(O≥O_c)∧(L<L_c)
Parameters live in configs/ and are deterministic by default (seeded runs).

## 4. Implementation Notes
Determinism: RNG seeding via PYTHONHASHSEED. Reproducibility: pinned minimal requirements, Makefile target, CI smoke run.
Telemetry: /logs/flight_recorder.jsonl and /logs/omega_gate.jsonl. Configuration: configs/nuscale_sbo.yaml carries thresholds 
{ε_ψ, T_γ, T_Ω, V_c, O_c, E_c, L_c} and the tri_temporal toggle (off by default).

## 5. Scenario and Data
The demo replays a public stub CSV trace approximating SBO+LUHS: flow decays after 5.5 h while temperature rises and pressure falls.
This drives γ upward; twist accumulates via γ-gradients. The sentinel typically triggers between ~6.3 and 6.9 h with default thresholds.

## 6. Results (Demo Configuration)
Upon sentinel trigger, Weaver‑11 proposes PassiveCooling_Depressurize. The Omega kernel evaluates VOEL; when gates pass, execution reduces twist and restores weave integrity. The run prints final integrity, max twist observed, and a completion message while recording an auditable decision trail.

## 7. Validation and Limitations
This artifact demonstrates *symbolic* early-warning and recovery in a reproducible simulation. It does not validate plant licensure, code coupling performance, or operator procedures. Live-mode adapters are gated and require user-implemented sockets and compliance with
licensed tools. Thresholds and scaling are illustrative and should be tuned with domain data.

## 8. Ethics, Safety, and Dual-Use
NSAM-1 is simulation-only. Governance gates and conservation boundaries are included to prevent unsafe export actions within the demo.
No plant-specific proprietary data is included. Users must avoid representing the demo as operational guidance.

## 9. Reproducibility Checklist
(1) Create a fresh Python 3.11+ environment; (2) pip install -r requirements.txt; (3) make demo; (4) inspect logs/ and configs/;
(5) optionally toggle NSAM_ENABLE_LIVE=1 only for non-production experimentation with user-implemented sockets.

## 10. Related Work
Severe Accident Management Guidelines (SAMGs); digital twins for nuclear systems; passive safety systems in integral PWRs; anomaly detection via reduced-order observers; auditability and safety envelopes in autonomous control research.

## 11. Conclusion
NSAM-1 v1.0.0 packages a compact, auditable demonstration of early symbolic-collapse detection and passive recovery planning under SBO+LUHS. The artifact is designed for quick inspection, replication, and community critique, paving the way for deeper integration with high-fidelity TH models and regulator-facing validation protocols.

## Acknowledgments
The author thanks the SEAL Division (Systems for Entropic-Alignment & Longevity) for research support and ethics review. This research received no external funding.

## References (indicative)
[1] ERF/Observer Field Theory/Weaver‑11/Hyperverse/XSFT 2025 internal specifications (open-source uploads).
[2] Severe Accident Management Guidelines (industry literature). 
[3] Digital twin and anomaly detection literature in nuclear systems engineering.

## Appendix A: Default Thresholds
epsilon_psi=0.60; T_gamma=0.15; T_Omega=0.75; V_c=0.65; O_c=0.80; E_c=0.80; L_c=0.20; tri_temporal=false

