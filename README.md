# Pseudospectral Legitimacy in Black Hole Ringdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18425950.svg)](https://doi.org/10.5281/zenodo.18425950)

**Author:** A. R. Wells  
**Affiliation:** Dual-Frame Research Group  
**License:** CC BY 4.0  
**Contact:** No solicitation for correspondence or media contact  
**Paper email:** arwells.research@proton.me  

---

## Overview

This repository contains the LaTeX source for the methods paper  
**_Pseudospectral Legitimacy in Black Hole Ringdown_**.

The paper introduces an **operator-theoretic diagnostic framework** for assessing when
quasinormal-mode (QNM) descriptions of black hole ringdown are **physically interpretable**,
rather than merely effective fitting bases.

The central claim is **interpretive rather than statistical**:

> In non-normal relaxation systems, additional modal components can improve waveform fits
> without corresponding to independent physical relaxation channels.
> Determining when modal descriptions are legitimate requires operator-level diagnostics,
> not fit quality alone.

The framework reframes long-standing ambiguities in ringdown start-time selection and
overtone interpretation as consequences of **pseudospectral structure**.

---

## Core Idea: Legitimacy vs. Fit Quality

Black hole ringdown is commonly modeled as a superposition of damped sinusoids.
In practice, however:

- inferred mode content depends sensitively on the chosen start time
- early-time fits improve when overtones are added
- different bases yield incompatible physical interpretations

This work argues that these issues arise because the linearized post-merger evolution
operator is **non-normal**.

In non-normal systems:

- eigenvalues alone do not control stability or interpretability
- transient amplification and strong mode mixing can occur
- additional basis elements may be required to reconstruct the signal
  without corresponding to physical decay channels

The paper introduces diagnostics that distinguish:

- **fitting functions** used to patch early-time non-normal mixing  
from
- **genuine relaxation modes** associated with resolvent-isolated dynamics.

---

## The Σ₂ Legitimacy Criterion

Two operator-level diagnostics are introduced:

### 1. Pseudospectral Isolation and Ringdown Onset

An objective ringdown onset time t⋆ is defined using **resolvent isolation**:
the time at which the fundamental mode becomes separated from nearby pseudospectral structure
within a reduced angular sector.

Before t⋆, modal coefficients are unstable and basis-dependent.
After t⋆, modal interpretations stabilize under window shifts and refinements.

### 2. Closure-Energy Monotonicity

A **closure residual** operator quantifies projection inconsistency between:

- a local radiative description of the waveform, and
- an asymptotically stationary (Kerr-consistent) representation.

A truncated modal reconstruction is considered **Σ₂-legitimate** if its associated
closure energy decays monotonically in time.

This provides a physically motivated criterion for when adding modes corresponds to
genuine relaxation channels rather than pseudospectral reconstruction artifacts.

---

## What This Paper Demonstrates

The paper establishes that:

1. **Overtones can improve early-time fits while violating physical legitimacy**  
   Synthetic NR-like demonstrations show closure-energy growth or oscillation despite
   reduced waveform residuals.

2. **Ringdown onset is an operator property, not a fitting heuristic**  
   The pseudospectral onset time explains why conventional start-time stabilization
   methods succeed only beyond a certain regime.

3. **Legitimacy diagnostics complement existing pipelines**  
   The framework integrates naturally with mismatch minimization and Bayesian model
   selection, especially in high–signal-to-noise ratio events where systematics dominate.

---

## What This Paper Does *Not* Claim

- It does **not** modify General Relativity or Kerr geometry
- It does **not** dispute the existence of Kerr QNMs
- It does **not** propose a new waveform model or inference algorithm
- It does **not** claim empirical validation on real detector data (yet)

Instead, it provides a **diagnostic and interpretive framework** for determining
when modal descriptions are physically meaningful.

---

## Repository Contents

- `paper/pseudospectral_legitimacy_black_hole_ringdown.tex` — master LaTeX source
- `paper/sections/` — paper sections
- `paper/refs.bib` — bibliography
- `paper/closure_energy_vs_time.pdf` — representative diagnostic figure
- `paper/make_closure_energy_figure.py` — figure generation script

Key appendix:

- **Appendix A** — concrete realization of the closure residual in Kerr ringdown,
  using Newman–Penrose scalars and Kerr-consistent angular projections, plus a toy
  non-normal matrix analogy.

---

## Build Instructions

Requirements: latexmk with a standard LaTeX installation.

Build the paper:

    cd paper
    latexmk -pdf -interaction=nonstopmode -halt-on-error pseudospectral_legitimacy_black_hole_ringdown.tex

Clean build artifacts:

    cd paper
    latexmk -C

The compiled PDF will be located at:

    paper/pseudospectral_legitimacy_black_hole_ringdown.pdf

---

## Status

- Conceptual framework finalized
- Operator-theoretic definitions complete
- Synthetic demonstrations included
- Robustness considerations addressed
- Scope and limitations explicitly stated

Release: Published on Zenodo (versioned)

- Version v1 DOI: https://doi.org/10.5281/zenodo.18425951
- All versions DOI: https://doi.org/10.5281/zenodo.18425950

---

## Citation

If you use or reference this work, please cite the Zenodo record corresponding to the
version used.

Recommended citation (v1):

A. R. Wells (2026).  
Pseudospectral Legitimacy in Black Hole Ringdown (v1).  
Zenodo. https://doi.org/10.5281/zenodo.18425951

For citation independent of version, use the all-versions DOI.

This work is released under Creative Commons Attribution 4.0 (CC BY 4.0).
