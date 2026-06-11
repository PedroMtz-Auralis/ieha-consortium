#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_projected_figures.py — Figuras ILUSTRATIVAS (datos sintéticos) para el
suplemento de outcomes proyectados del Consorcio IEH-A.

ADVERTENCIA: TODO lo que produce este script son DATOS SINTÉTICOS generados con
una semilla fija. NO son resultados, NO provienen de ningún levantamiento, y NO
deben presentarse como hallazgos. Sirven para ILUSTRAR qué tipo de evidencia
podría producir una validación multi-sitio. Cada figura lleva el rótulo
"ILUSTRATIVO · DATOS SINTÉTICOS".
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(20260610)

# Okabe-Ito (daltónico-seguro)
OI = {"blue": "#0072B2", "vermillion": "#D55E00", "green": "#009E73",
      "orange": "#E69F00", "sky": "#56B4E9", "grey": "#999999", "purple": "#CC79A7"}
PROFILE_COLORS = {1: OI["sky"], 2: OI["vermillion"], 3: OI["green"], 4: OI["orange"]}
PROFILE_LABEL = {1: "P1 · sano / IEH-A bajo", 2: "P2 · alterado / IEH-A alto",
                 3: "P3 · sano / IEH-A alto", 4: "P4 · alterado / IEH-A bajo"}
plt.rcParams.update({"font.family": "serif", "font.size": 11})

CITIES = ["Ciudad A", "Ciudad B", "Ciudad C"]
# Prevalencias sintéticas por perfil y ciudad (filas suman 1) — varían por contexto
PREV = {
    "Ciudad A": [0.42, 0.22, 0.14, 0.22],
    "Ciudad B": [0.38, 0.18, 0.21, 0.23],
    "Ciudad C": [0.47, 0.20, 0.10, 0.23],
}


def banner(fig):
    fig.text(0.99, 0.012, "ILUSTRATIVO · DATOS SINTÉTICOS — no son resultados",
             ha="right", va="bottom", fontsize=8, style="italic", color="#B00020")


# --- Fig 1: distribución de los 4 perfiles por ciudad (barras apiladas) -------
def fig_profiles_by_city():
    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    bottoms = np.zeros(len(CITIES))
    for p in [1, 2, 3, 4]:
        vals = np.array([PREV[c][p - 1] * 100 for c in CITIES])
        bars = ax.bar(CITIES, vals, bottom=bottoms, color=PROFILE_COLORS[p],
                      edgecolor="white", label=PROFILE_LABEL[p],
                      linewidth=0.8, width=0.55)
        for b, v, bo in zip(bars, vals, bottoms):
            if p == 3:
                ax.text(b.get_x() + b.get_width() / 2, bo + v / 2, f"{v:.0f}%",
                        ha="center", va="center", fontsize=10, fontweight="bold", color="black")
        bottoms += vals
    ax.set_ylabel("% de la muestra")
    ax.set_ylim(0, 100)
    ax.set_title("Distribución hipotética de los cuatro perfiles por contexto\n"
                 "(el Perfil 3 — sano + IEH-A alto — es el foco)", fontsize=12)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=2, frameon=False, fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    banner(fig)
    fig.tight_layout(rect=[0, 0.02, 1, 1])
    fig.savefig(os.path.join(OUT, "fig1_perfiles_por_ciudad.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# --- Fig 2: ortogonalidad — IEH-A vs clínica, cluster del Perfil 3 ------------
def fig_orthogonality():
    n = 700
    # asignar perfiles según prevalencia media
    base = np.mean([PREV[c] for c in CITIES], axis=0)
    profs = rng.choice([1, 2, 3, 4], size=n, p=base / base.sum())
    clin = np.empty(n); ieha = np.empty(n)
    for i, p in enumerate(profs):
        if p == 1:   c, e = rng.normal(-1.0, 0.5), rng.normal(0.18, 0.07)
        elif p == 2: c, e = rng.normal(1.1, 0.5),  rng.normal(0.62, 0.08)
        elif p == 3: c, e = rng.normal(-0.9, 0.45), rng.normal(0.58, 0.08)  # el cluster clave
        else:        c, e = rng.normal(1.0, 0.5),  rng.normal(0.20, 0.07)
        clin[i] = c; ieha[i] = np.clip(e, 0, 1)
    fig, ax = plt.subplots(figsize=(6.8, 5.2))
    for p in [1, 2, 4, 3]:
        m = profs == p
        ax.scatter(clin[m], ieha[m], s=18, alpha=0.55, color=PROFILE_COLORS[p],
                   edgecolor="none", label=PROFILE_LABEL[p], zorder=3 if p == 3 else 2)
    ax.axhline(0.40, ls="--", color=OI["grey"], lw=1)
    ax.axvline(0.0, ls="--", color=OI["grey"], lw=1)
    ax.annotate("Perfil 3\nclínica normal, IEH-A alto",
                xy=(-0.9, 0.58), xytext=(-2.3, 0.86), fontsize=10, fontweight="bold",
                color=OI["green"], arrowprops=dict(arrowstyle="->", color=OI["green"]))
    ax.set_xlabel("Estado clínico (compuesto PSQI/PSS-10, estandarizado) →")
    ax.set_ylabel("IEH-A (0–1) →")
    ax.set_title("Ortogonalidad ilustrativa: el IEH-A no es redundante con la clínica\n"
                 "(el Perfil 3 ocupa una región que las escalas estándar declaran 'sana')", fontsize=11.5)
    ax.legend(loc="lower right", fontsize=8.5, frameon=True)
    ax.spines[["top", "right"]].set_visible(False)
    banner(fig)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig2_ortogonalidad_perfil3.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# --- Fig 3: invarianza ilustrativa — ítems universales vs context-specific ----
def fig_invariance():
    items = [f"{d}-{i}" for d in ["OC", "PR", "CU"] for i in range(1, 5)]
    # 0 = invariante (universal), 1 = parcial, 2 = específico del contexto
    status = np.zeros((len(items), len(CITIES)), dtype=int)
    # introducir algunos ítems context-specific de forma sintética
    status[2, 1] = 2; status[2, 2] = 1      # OC-3 (espacio exterior) varía
    status[6, 2] = 2                        # PR-3 (recomendar el lugar)
    status[10, 0] = 1; status[10, 1] = 2    # CU-3 (cuidado de menores)
    cmap = matplotlib.colors.ListedColormap([OI["green"], OI["orange"], OI["vermillion"]])
    fig, ax = plt.subplots(figsize=(6.2, 6.0))
    ax.imshow(status, cmap=cmap, vmin=0, vmax=2, aspect="auto")
    ax.set_xticks(range(len(CITIES))); ax.set_xticklabels(CITIES)
    ax.set_yticks(range(len(items))); ax.set_yticklabels(items, fontsize=9)
    for i in range(len(items)):
        for j in range(len(CITIES)):
            ax.text(j, i, "•", ha="center", va="center", color="white", fontsize=8)
    ax.set_title("Invarianza de medición ilustrativa por ítem y contexto\n"
                 "(verde = universal · naranja = parcial · rojo = específico del contexto)", fontsize=11)
    legend = [Patch(facecolor=OI["green"], label="invariante (universal)"),
              Patch(facecolor=OI["orange"], label="parcial"),
              Patch(facecolor=OI["vermillion"], label="específico del contexto")]
    ax.legend(handles=legend, loc="upper center", bbox_to_anchor=(0.5, -0.07),
              ncol=1, frameon=False, fontsize=9)
    banner(fig)
    fig.tight_layout(rect=[0, 0.02, 1, 1])
    fig.savefig(os.path.join(OUT, "fig3_invarianza_items.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


# --- Fig 4: prevalencia del Perfil 3 por contexto con IC ilustrativos ---------
def fig_prevalence():
    p3 = np.array([PREV[c][2] * 100 for c in CITIES])
    ci = np.array([4.0, 4.5, 3.5])  # IC sintéticos
    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    x = np.arange(len(CITIES))
    ax.bar(x, p3, yerr=ci, color=OI["green"], width=0.5, capsize=6,
           edgecolor="white", linewidth=0.8, alpha=0.9)
    for xi, v in zip(x, p3):
        ax.text(xi, v + 5.2, f"{v:.0f}%", ha="center", fontsize=11, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(CITIES)
    ax.set_ylabel("Prevalencia del Perfil 3 (%)")
    ax.set_ylim(0, 32)
    ax.set_title("Prevalencia ilustrativa del Perfil 3 entre contextos\n"
                 "(población 'funcional' con habitar erosionado — la que nadie cuenta)", fontsize=11.5)
    ax.spines[["top", "right"]].set_visible(False)
    banner(fig)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "fig4_prevalencia_perfil3.png"), dpi=200, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig_profiles_by_city()
    fig_orthogonality()
    fig_invariance()
    fig_prevalence()
    print("OK — 4 figuras ILUSTRATIVAS (datos sintéticos) en", OUT)
