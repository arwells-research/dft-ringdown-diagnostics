#!/usr/bin/env python3
"""
Minimal placeholder generator for Figure 1:
Creates a PDF named 'closure_energy_vs_time.pdf' showing three closure-energy curves:
E_(0)(t), E_(0,1)(t), E_(0,1,2)(t)

- Uses matplotlib (no seaborn)
- No explicit color/style settings
- Produces a single plot (no subplots)
"""

import numpy as np
import matplotlib.pyplot as plt


def smooth_step(x: np.ndarray, x0: float, k: float) -> np.ndarray:
    """Logistic smooth step from ~1 (x<<x0) to ~0 (x>>x0)."""
    return 1.0 / (1.0 + np.exp(k * (x - x0)))


def main() -> None:
    # Time axis in units of M (dimensionless), matching caption language.
    t0 = 0.0
    t = np.linspace(0.0, 30.0, 1200)
    tau = t - t0

    # Ringdown onset (synthetic)
    t_star = 8.0

    # Baseline monotone decay envelope (all curves share a common late-time decay)
    E_base = 0.5 * np.exp(-0.12 * tau)

    # Early-time "pseudospectral overlap" bump/oscillation that decays away by ~t_star
    gate = smooth_step(tau, x0=t_star, k=1.2)  # ~1 before t_star, ~0 after
    osc1 = 0.08 * gate * np.exp(-0.25 * tau) * (1.0 + 0.7 * np.sin(2.6 * tau))
    osc2 = 0.14 * gate * np.exp(-0.18 * tau) * (1.0 + 1.1 * np.sin(2.9 * tau + 0.6))

    # Construct three "closure energy" curves:
    # (0): monotone
    E_0 = E_base

    # (0,1): mild early oscillations but mostly decreasing
    E_01 = E_base + np.maximum(osc1, -0.02 * E_base)

    # (0,1,2): stronger early oscillations / transient growth (violations of monotonicity)
    # Add a transient growth lobe early on (Gaussian bump) + oscillations.
    bump = 0.10 * np.exp(-0.5 * ((tau - 4.2) / 1.2) ** 2) * gate
    E_012 = E_base + osc2 + bump

    # Ensure non-negativity (energies)
    E_0 = np.clip(E_0, 0.0, None)
    E_01 = np.clip(E_01, 0.0, None)
    E_012 = np.clip(E_012, 0.0, None)

    # Plot
    fig = plt.figure()
    ax = plt.gca()
    ax.plot(t, E_0,   label=r"$\mathcal{E}_{(0)}(t)$")
    ax.plot(t, E_01,  label=r"$\mathcal{E}_{(0,1)}(t)$")
    ax.plot(t, E_012, label=r"$\mathcal{E}_{(0,1,2)}(t)$")

    # --- Mark t_star (robust indexing + consistent naming) ---
    t_star_abs = float(t0 + t_star)
    ax.axvline(t_star_abs, linestyle="--", linewidth=1.0)

    # Choose a reference energy for label placement (use E_0; avoid undefined E_base)
    i = int(np.searchsorted(t, t_star_abs))
    i = max(0, min(i, len(t) - 1))  # clamp

    y_ref = float(E_0[i])
    # keep label inside axes even if y_ref is ~0
    y_text = y_ref * 0.9 if y_ref > 0 else 0.05 * float(np.nanmax(E_0))

    ax.text(t_star_abs + 0.3, y_text, r"$t_\star$", va="center")

    ax.set_xlabel(r"$(t-t_0)/M$")
    ax.set_ylabel(r"$\mathcal{E}(\hat{x}(t))$ (arb.\ units)")
    ax.legend()
    ax.set_xlim(float(np.min(t)), float(np.max(t)))

    fig.tight_layout()
    fig.savefig("closure_energy_vs_time.pdf")
    print("Wrote: closure_energy_vs_time.pdf")

if __name__ == "__main__":
    main()
