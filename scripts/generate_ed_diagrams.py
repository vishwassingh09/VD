"""Generate clean, vector-path SVG physics diagrams for MSc Electrodynamics notes."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Ellipse, Polygon, Arc
import numpy as np

plt.rcParams["svg.fonttype"] = "path"
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["font.family"] = "STIXGeneral"

OUT_SVG = Path("public/diagrams/ed")
OUT_PNG = Path(r"C:\Users\vishw\.gemini\antigravity-cli\brain\aa513cda-2dc5-47aa-8b51-a481ce289d49\scratch\diag_preview")
OUT_SVG.mkdir(parents=True, exist_ok=True)
OUT_PNG.mkdir(parents=True, exist_ok=True)


def save_fig(fig, name: str):
    fig.savefig(OUT_SVG / f"{name}.svg", format="svg", transparent=True, bbox_inches="tight", pad_inches=0.18)
    fig.savefig(OUT_PNG / f"{name}.png", format="png", dpi=160, facecolor="white", bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)


def arrow(ax, p1, p2, color="#1e293b", lw=1.8, style="-|>", mutation_scale=13, ls="-", alpha=1.0, zorder=3):
    patch = FancyArrowPatch(
        p1, p2,
        arrowstyle=style,
        mutation_scale=mutation_scale,
        color=color,
        linewidth=lw,
        linestyle=ls,
        alpha=alpha,
        zorder=zorder,
    )
    ax.add_patch(patch)


def make_coulomb_vectors():
    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    ax.set_xlim(-0.9, 5.6)
    ax.set_ylim(-0.9, 3.6)
    ax.set_aspect("equal")
    ax.axis("off")

    origin = (0.3, 0.2)
    arrow(ax, origin, (0.3, 3.2), color="#64748b", lw=1.3, mutation_scale=11)
    arrow(ax, origin, (4.7, 0.2), color="#64748b", lw=1.3, mutation_scale=11)
    arrow(ax, origin, (-0.55, -0.55), color="#64748b", lw=1.3, mutation_scale=11)
    ax.text(0.15, 3.25, r"$y$", fontsize=14, color="#475569")
    ax.text(4.8, 0.14, r"$x$", fontsize=14, color="#475569")
    ax.text(-0.75, -0.74, r"$z$", fontsize=14, color="#475569")

    for px, py, lbl in [(1.10, 2.05, r"$q_1$"), (1.42, 2.40, r"$q_2$")]:
        ax.scatter([px], [py], s=26, color="#64748b", zorder=4)
        ax.text(px - 0.25, py + 0.12, lbl, fontsize=12, color="#475569")

    qi = (1.75, 1.50)
    Q = (4.25, 2.45)
    ax.scatter([qi[0]], [qi[1]], s=55, color="#dc2626", zorder=5)
    ax.text(qi[0] - 0.08, qi[1] + 0.18, r"$q_i$", fontsize=14, color="#dc2626")

    ax.scatter([Q[0]], [Q[1]], s=55, color="#0066cc", zorder=5)
    ax.text(Q[0] + 0.12, Q[1] + 0.05, r"$Q$ (Field Point)", fontsize=13, color="#0066cc")

    arrow(ax, origin, qi, color="#1e293b", lw=1.9)
    ax.text(0.74, 1.04, r"$\vec{r}\,'_i$", fontsize=14, color="#1e293b")

    arrow(ax, origin, Q, color="#1e293b", lw=1.9)
    ax.text(2.45, 1.08, r"$\vec{r}$", fontsize=14, color="#1e293b")

    arrow(ax, qi, Q, color="#0066cc", lw=2.2, mutation_scale=14)
    ax.text(2.25, 2.38, r"$\vec{\mathfrak{r}}_i = \vec{r} - \vec{r}\,'_i$", fontsize=14, color="#0066cc")

    save_fig(fig, "coulomb-vectors")


def make_gaussian_pillbox():
    fig, ax = plt.subplots(figsize=(5.8, 3.3))
    ax.set_xlim(0.0, 6.0)
    ax.set_ylim(-0.3, 3.5)
    ax.set_aspect("equal")
    ax.axis("off")

    sheet = Polygon(
        [(0.3, 1.12), (1.6, 1.95), (5.5, 1.95), (4.2, 1.12)],
        closed=True, facecolor="#dbeafe", edgecolor="#1e293b", linewidth=1.6, alpha=0.65, zorder=1
    )
    ax.add_patch(sheet)
    ax.text(3.98, 1.48, r"$\sigma$ (surface charge)", fontsize=12.5, color="#dc2626")

    cx, rx, ry = 2.35, 0.56, 0.18
    y_top, y_bot = 2.08, 1.00

    top_cap = Ellipse((cx, y_top), 2 * rx, 2 * ry, facecolor="#dcfce7", edgecolor="#1e293b", linewidth=1.6, alpha=0.85, zorder=4)
    ax.add_patch(top_cap)
    ax.plot([cx - rx, cx - rx], [y_bot, y_top], color="#1e293b", lw=1.6, zorder=3)
    ax.plot([cx + rx, cx + rx], [y_bot, y_top], color="#1e293b", lw=1.6, zorder=3)

    theta = np.linspace(np.pi, 2 * np.pi, 80)
    ax.plot(cx + rx * np.cos(theta), y_bot + ry * np.sin(theta), color="#1e293b", lw=1.6, zorder=3)
    theta_back = np.linspace(0, np.pi, 80)
    ax.plot(cx + rx * np.cos(theta_back), y_bot + ry * np.sin(theta_back), color="#1e293b", lw=1.2, ls="--", zorder=2)

    ax.text(cx - 0.95, 2.38, r"Area $A$", fontsize=11.5, color="#15803d")
    arrow(ax, (cx - 0.52, 2.34), (cx - 0.25, 2.12), color="#15803d", lw=1.1, mutation_scale=9, zorder=5)

    # Height indicator epsilon -> 0 cleanly between pillbox and sigma text
    ax.plot([3.10, 3.10], [y_bot, y_top], color="#475569", lw=1.1)
    ax.plot([3.03, 3.17], [y_top, y_top], color="#475569", lw=1.1)
    ax.plot([3.03, 3.17], [y_bot, y_bot], color="#475569", lw=1.1)
    ax.text(3.20, 1.48, r"$\epsilon \to 0$", fontsize=12.5, color="#334155")

    arrow(ax, (cx, y_top), (cx + 0.35, 3.15), color="#0066cc", lw=2.2, zorder=6)
    ax.text(cx + 0.42, 2.95, r"$\vec{E}_{\mathrm{above}}$", fontsize=14, color="#0066cc")

    arrow(ax, (cx, y_bot - 0.05), (cx + 0.28, -0.05), color="#0066cc", lw=2.2, zorder=6)
    ax.text(cx + 0.36, 0.05, r"$\vec{E}_{\mathrm{below}}$", fontsize=14, color="#0066cc")

    arrow(ax, (1.18, 1.54), (1.18, 2.48), color="#15803d", lw=2.0, zorder=5)
    ax.text(0.92, 2.38, r"$\hat{n}$", fontsize=14, color="#15803d")

    save_fig(fig, "gaussian-pillbox")


def make_uniqueness_conductors():
    fig, ax = plt.subplots(figsize=(5.8, 3.3))
    ax.set_xlim(0.0, 5.6)
    ax.set_ylim(0.1, 3.4)
    ax.set_aspect("equal")
    ax.axis("off")

    t = np.linspace(0, 2 * np.pi, 300)
    x = 2.65 + (1.85 + 0.14 * np.cos(2 * t) + 0.08 * np.sin(3 * t)) * np.cos(t)
    y = 1.65 + (1.22 + 0.10 * np.sin(2 * t) - 0.05 * np.cos(3 * t)) * np.sin(t)
    outer = Polygon(np.column_stack([x, y]), closed=True, facecolor="#eff6ff", edgecolor="#1e293b", lw=1.9, alpha=0.85)
    ax.add_patch(outer)

    ax.text(0.25, 2.98, r"Outer surface $S_0$", fontsize=12.5, color="#334155")
    arrow(ax, (1.15, 2.92), (1.42, 2.65), color="#475569", lw=1.1, mutation_scale=9)

    ax.text(4.35, 0.42, r"Volume $\mathcal{V}$", fontsize=13.5, color="#1e293b")

    conductors = [
        (1.68, 2.08, 0.78, 0.46, r"$Q_a$"),
        (3.22, 2.22, 0.80, 0.46, r"$Q_b$"),
        (1.92, 1.06, 0.76, 0.44, r"$Q_c$"),
        (3.38, 1.18, 0.78, 0.44, r"$Q_d$"),
    ]
    for cx, cy, w, h, lbl in conductors:
        ell = Ellipse((cx, cy), w, h, facecolor="#fee2e2", edgecolor="#dc2626", lw=1.7, zorder=4)
        ax.add_patch(ell)
        ax.text(cx - 0.12, cy - 0.06, lbl, fontsize=13, color="#b91c1c", zorder=5)

    ax.text(2.42, 1.60, r"$\rho(\vec{r})$", fontsize=14, color="#0066cc", zorder=5)
    ax.text(4.78, 1.75, r"Interior surfaces $S_i$", fontsize=11.5, color="#475569")
    arrow(ax, (4.74, 1.78), (3.78, 1.24), color="#64748b", lw=1.1, mutation_scale=9)

    save_fig(fig, "uniqueness-conductors")


def make_method_of_images():
    fig, ax = plt.subplots(figsize=(5.8, 3.1))
    ax.set_xlim(0.0, 6.2)
    ax.set_ylim(0.0, 3.2)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.text(0.55, 2.95, "Situation A (Actual)", fontsize=12.5, fontweight="bold", color="#1e293b")
    plane = Polygon([(0.2, 1.25), (0.85, 1.75), (2.65, 1.75), (2.0, 1.25)], closed=True,
                    facecolor="#cbd5e1", edgecolor="#1e293b", lw=1.6, alpha=0.8)
    ax.add_patch(plane)
    ax.plot([1.42, 1.42], [1.50, 2.52], color="#475569", lw=1.3, ls="--")
    ax.scatter([1.42], [2.52], s=65, color="#dc2626", zorder=5)
    ax.text(1.56, 2.50, r"$+q$", fontsize=14, color="#dc2626")
    ax.text(1.22, 1.98, r"$d$", fontsize=13, color="#1e293b")
    ax.text(1.75, 1.00, r"$V = 0\;(z=0)$", fontsize=11.5, color="#334155")

    ax.plot([0.55, 0.55], [1.25, 0.90], color="#1e293b", lw=1.5)
    ax.plot([0.38, 0.72], [0.90, 0.90], color="#1e293b", lw=1.5)
    ax.plot([0.44, 0.66], [0.81, 0.81], color="#1e293b", lw=1.5)
    ax.plot([0.49, 0.61], [0.72, 0.72], color="#1e293b", lw=1.5)

    ax.text(2.92, 1.45, r"$\equiv$", fontsize=22, color="#0066cc")

    ax.text(3.75, 2.95, "Situation B (Image)", fontsize=12.5, fontweight="bold", color="#1e293b")
    ax.plot([3.55, 5.95], [1.50, 1.50], color="#1e293b", lw=1.6)
    ax.text(5.15, 1.60, r"$z=0\;(V=0)$", fontsize=11.5, color="#334155")
    ax.plot([4.65, 4.65], [0.48, 2.52], color="#475569", lw=1.3, ls="--")

    ax.scatter([4.65], [2.52], s=65, color="#dc2626", zorder=5)
    ax.text(4.80, 2.50, r"$+q$", fontsize=14, color="#dc2626")
    ax.text(4.44, 1.98, r"$d$", fontsize=13, color="#1e293b")

    ax.scatter([4.65], [0.48], s=65, color="#0066cc", zorder=5)
    ax.text(4.80, 0.44, r"$-q$ (image)", fontsize=13.5, color="#0066cc")
    ax.text(4.44, 0.95, r"$d$", fontsize=13, color="#1e293b")

    save_fig(fig, "method-of-images")


def make_separation_slot():
    fig, ax = plt.subplots(figsize=(5.6, 3.1))
    ax.set_xlim(-0.3, 5.8)
    ax.set_ylim(-0.1, 3.1)
    ax.set_aspect("equal")
    ax.axis("off")

    top = Polygon([(1.3, 2.1), (2.1, 2.65), (4.7, 2.65), (3.9, 2.1)], closed=True,
                  facecolor="#dbeafe", edgecolor="#1e293b", lw=1.6, alpha=0.65)
    bot = Polygon([(1.3, 0.7), (2.1, 1.25), (4.7, 1.25), (3.9, 0.7)], closed=True,
                  facecolor="#dbeafe", edgecolor="#1e293b", lw=1.6, alpha=0.65)
    strip = Polygon([(1.3, 0.7), (1.3, 2.1), (2.1, 2.65), (2.1, 1.25)], closed=True,
                    facecolor="#fee2e2", edgecolor="#dc2626", lw=1.8, alpha=0.8)
    ax.add_patch(bot)
    ax.add_patch(strip)
    ax.add_patch(top)

    ax.text(2.55, 2.32, r"$V = 0\;(y = a)$", fontsize=12.5, color="#1e293b")
    ax.text(2.55, 0.92, r"$V = 0\;(y = 0)$", fontsize=12.5, color="#1e293b")
    ax.text(-0.15, 1.48, r"$V_0(y)$ at $x=0$", fontsize=13, color="#dc2626")

    arrow(ax, (1.3, 0.7), (1.3, 2.85), color="#475569", lw=1.4, mutation_scale=11)
    ax.text(1.12, 2.82, r"$y$", fontsize=14, color="#334155")

    arrow(ax, (4.2, 0.97), (5.2, 0.97), color="#475569", lw=1.4, mutation_scale=11)
    ax.text(5.26, 0.92, r"$x \to \infty$", fontsize=13, color="#334155")

    arrow(ax, (1.3, 0.7), (0.65, 0.25), color="#475569", lw=1.4, mutation_scale=11)
    ax.text(0.45, 0.16, r"$z$", fontsize=14, color="#334155")

    # Height bracket at x = 4.08
    ax.plot([4.08, 4.08], [0.7, 2.1], color="#475569", lw=1.2, ls="--")
    ax.plot([4.01, 4.15], [2.1, 2.1], color="#475569", lw=1.2)
    ax.plot([4.01, 4.15], [0.7, 0.7], color="#475569", lw=1.2)
    ax.text(4.16, 1.42, r"$a$", fontsize=13.5, color="#334155")

    save_fig(fig, "separation-slot")


def make_multipole_geometry():
    fig, ax = plt.subplots(figsize=(5.5, 3.2))
    ax.set_xlim(0.1, 5.4)
    ax.set_ylim(0.1, 3.1)
    ax.set_aspect("equal")
    ax.axis("off")

    t = np.linspace(0, 2 * np.pi, 220)
    bx = 1.42 + (0.85 + 0.12 * np.cos(2 * t) - 0.08 * np.sin(3 * t)) * np.cos(t)
    by = 1.72 + (0.78 + 0.08 * np.sin(2 * t) + 0.06 * np.cos(3 * t)) * np.sin(t)
    blob = Polygon(np.column_stack([bx, by]), closed=True, facecolor="#fee2e2", edgecolor="#dc2626", lw=1.7, alpha=0.65)
    ax.add_patch(blob)
    ax.text(0.76, 2.08, r"$\rho(\vec{r}\,')\,d\tau'$", fontsize=13, color="#b91c1c")

    origin = (1.15, 0.42)
    ax.scatter([origin[0]], [origin[1]], s=35, color="#1e293b", zorder=5)
    ax.text(0.95, 0.22, r"$O$", fontsize=13, color="#1e293b")

    dV = (1.65, 1.70)
    ax.add_patch(Polygon([(1.57, 1.62), (1.73, 1.62), (1.73, 1.78), (1.57, 1.78)],
                         closed=True, facecolor="#fca5a5", edgecolor="#b91c1c", lw=1.4, zorder=4))

    P = (4.65, 2.25)
    ax.scatter([P[0]], [P[1]], s=55, color="#0066cc", zorder=5)
    ax.text(4.78, 2.23, r"$P$", fontsize=14, color="#0066cc")

    arrow(ax, origin, dV, color="#1e293b", lw=1.9)
    ax.text(1.48, 1.16, r"$\vec{r}\,'$", fontsize=14, color="#1e293b")

    arrow(ax, origin, P, color="#1e293b", lw=1.9)
    ax.text(2.95, 1.14, r"$\vec{r}$", fontsize=14, color="#1e293b")

    arrow(ax, dV, P, color="#0066cc", lw=2.2, mutation_scale=14)
    ax.text(2.95, 2.15, r"$\mathfrak{r} = |\vec{r} - \vec{r}\,'|$", fontsize=13.5, color="#0066cc")

    arc = Arc(origin, 0.92, 0.92, angle=0, theta1=27, theta2=69, color="#1e293b", lw=1.4)
    ax.add_patch(arc)
    ax.text(1.50, 0.85, r"$\alpha$", fontsize=13, color="#1e293b")

    save_fig(fig, "multipole-geometry")


def make_ch2_gauss_surfaces():
    fig, axes = plt.subplots(1, 3, figsize=(8.2, 2.5))
    for a in axes:
        a.set_aspect("equal")
        a.axis("off")

    # 1. Spherical Gaussian surface
    ax = axes[0]
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.5, 1.4)
    ax.add_patch(plt.Circle((0, 0), 0.55, facecolor="#fee2e2", edgecolor="#dc2626", lw=1.6))
    ax.add_patch(plt.Circle((0, 0), 1.05, facecolor="none", edgecolor="#0066cc", lw=1.6, ls="--"))
    arrow(ax, (0, 0), (0.74, 0.74), color="#0066cc", lw=1.6, mutation_scale=11)
    ax.text(0.28, 0.52, r"$r$", fontsize=13, color="#0066cc")
    ax.text(-0.18, -0.10, r"$R$", fontsize=12, color="#dc2626")
    ax.text(0, -1.38, r"Spherical ($4\pi r^2$)", ha="center", fontsize=11.5, color="#1e293b")

    # 2. Cylindrical Gaussian surface
    ax = axes[1]
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.5, 1.4)
    ax.plot([-1.15, 1.15], [0, 0], color="#dc2626", lw=2.4)
    rect_x = [-0.65, 0.65, 0.65, -0.65, -0.65]
    rect_y = [-0.65, -0.65, 0.65, 0.65, -0.65]
    ax.plot(rect_x, rect_y, color="#0066cc", lw=1.5, ls="--")
    arrow(ax, (0, 0), (0, 0.65), color="#0066cc", lw=1.5, mutation_scale=10)
    ax.text(0.10, 0.28, r"$s$", fontsize=13, color="#0066cc")
    ax.text(0, 0.80, r"$l$", ha="center", fontsize=12, color="#0066cc")
    ax.text(0, -1.38, r"Coaxial ($2\pi s l$)", ha="center", fontsize=11.5, color="#1e293b")

    # 3. Overlapping spheres (+rho, -rho)
    ax = axes[2]
    ax.set_xlim(-1.5, 1.6)
    ax.set_ylim(-1.5, 1.4)
    c1 = (-0.42, 0.0)
    c2 = (0.48, 0.0)
    ax.add_patch(plt.Circle(c1, 0.78, facecolor="#fee2e2", edgecolor="#dc2626", lw=1.5, alpha=0.55))
    ax.add_patch(plt.Circle(c2, 0.78, facecolor="#dbeafe", edgecolor="#0066cc", lw=1.5, alpha=0.55))
    ax.scatter([c1[0], c2[0]], [0, 0], s=25, color="#1e293b", zorder=5)
    arrow(ax, c1, c2, color="#1e293b", lw=1.6, mutation_scale=11, zorder=6)
    ax.text(-0.02, 0.14, r"$\vec{d}$", fontsize=13, color="#1e293b")
    ax.text(-0.92, 0.72, r"$+\rho$", fontsize=12, color="#dc2626")
    ax.text(0.68, 0.72, r"$-\rho$", fontsize=12, color="#0066cc")
    ax.text(0.05, -1.38, r"Overlap ($\vec{E}=\frac{\rho}{3\epsilon_0}\vec{d}$)", ha="center", fontsize=11.5, color="#1e293b")

    fig.tight_layout(w_pad=1.2)
    save_fig(fig, "ch2-gauss-surfaces")


def make_ch2_triangle():
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    ax.set_xlim(-0.4, 5.4)
    ax.set_ylim(-0.4, 3.9)
    ax.set_aspect("equal")
    ax.axis("off")

    top = (2.5, 3.35)
    left = (0.55, 0.45)
    right = (4.45, 0.45)

    for p, lbl, c in [(top, r"$\rho$", "#dc2626"), (left, r"$V$", "#15803d"), (right, r"$\vec{E}$", "#0066cc")]:
        ax.add_patch(plt.Circle(p, 0.34, facecolor="#f8fafc", edgecolor=c, lw=2.0, zorder=5))
        ax.text(p[0], p[1], lbl, ha="center", va="center", fontsize=16, color=c, zorder=6)

    # Top <-> Right (rho <-> E)
    arrow(ax, (2.82, 3.15), (4.25, 0.85), color="#1e293b", lw=1.6, mutation_scale=11)
    arrow(ax, (4.05, 0.70), (2.62, 3.00), color="#64748b", lw=1.5, mutation_scale=11)
    ax.text(3.75, 2.25, r"$\vec{E} = \frac{1}{4\pi\epsilon_0}\int\frac{\rho}{\mathfrak{r}^2}\hat{\mathfrak{r}}\,d\tau'$", fontsize=11.5, color="#1e293b", rotation=-56, ha="center", va="center")
    ax.text(3.05, 1.85, r"$\nabla\cdot\vec{E} = \frac{\rho}{\epsilon_0}$", fontsize=11.5, color="#475569", rotation=-56, ha="center", va="center")

    # Top <-> Left (rho <-> V)
    arrow(ax, (2.18, 3.15), (0.75, 0.85), color="#1e293b", lw=1.6, mutation_scale=11)
    arrow(ax, (0.95, 0.70), (2.38, 3.00), color="#64748b", lw=1.5, mutation_scale=11)
    ax.text(1.18, 2.22, r"$V = \frac{1}{4\pi\epsilon_0}\int\frac{\rho}{\mathfrak{r}}\,d\tau'$", fontsize=11.5, color="#1e293b", rotation=56, ha="center", va="center")
    ax.text(1.88, 1.82, r"$\nabla^2 V = -\frac{\rho}{\epsilon_0}$", fontsize=11.5, color="#475569", rotation=56, ha="center", va="center")

    # Left <-> Right (V <-> E)
    arrow(ax, (0.98, 0.56), (4.02, 0.56), color="#1e293b", lw=1.6, mutation_scale=11)
    arrow(ax, (4.02, 0.34), (0.98, 0.34), color="#64748b", lw=1.5, mutation_scale=11)
    ax.text(2.5, 0.76, r"$\vec{E} = -\vec{\nabla}V$", ha="center", fontsize=12.5, color="#1e293b")
    ax.text(2.5, 0.02, r"$V(\vec{r}) = -\int_{\mathcal{O}}^{\vec{r}}\vec{E}\cdot d\vec{l}$", ha="center", fontsize=12, color="#475569")

    save_fig(fig, "ch2-electrostatics-triangle")


def make_ch2_conductors_cavities():
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0))
    for a in axes:
        a.set_aspect("equal")
        a.axis("off")

    # Left: Concentric metal sphere + shell (Prob 2.38)
    ax = axes[0]
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.7, 1.5)
    ax.add_patch(plt.Circle((0, 0), 1.25, facecolor="#cbd5e1", edgecolor="#1e293b", lw=1.6))
    ax.add_patch(plt.Circle((0, 0), 0.82, facecolor="white", edgecolor="#1e293b", lw=1.4))
    ax.add_patch(plt.Circle((0, 0), 0.42, facecolor="#fca5a5", edgecolor="#dc2626", lw=1.6))
    arrow(ax, (0, 0), (0.30, 0.28), color="#1e293b", lw=1.2, mutation_scale=9)
    ax.text(0.18, 0.02, r"$R$", fontsize=11, color="#1e293b")
    arrow(ax, (0, 0), (-0.58, 0.58), color="#1e293b", lw=1.2, mutation_scale=9)
    ax.text(-0.55, 0.25, r"$a$", fontsize=11, color="#1e293b")
    arrow(ax, (0, 0), (0.88, -0.88), color="#1e293b", lw=1.2, mutation_scale=9)
    ax.text(0.55, -0.78, r"$b$", fontsize=11, color="#1e293b")
    ax.text(-0.12, -0.15, r"$q$", fontsize=12, color="#b91c1c")
    ax.text(0, -1.55, "Concentric Shell (Prob. 2.38)", ha="center", fontsize=11.5, color="#1e293b")

    # Right: Conductor with two spherical cavities (Prob 2.39)
    ax = axes[1]
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.7, 1.5)
    ax.add_patch(plt.Circle((0, 0), 1.25, facecolor="#cbd5e1", edgecolor="#1e293b", lw=1.6))
    ax.add_patch(plt.Circle((-0.48, 0.12), 0.42, facecolor="white", edgecolor="#1e293b", lw=1.4))
    ax.add_patch(plt.Circle((0.48, -0.10), 0.36, facecolor="white", edgecolor="#1e293b", lw=1.4))
    ax.scatter([-0.48, 0.48], [0.12, -0.10], s=32, color="#dc2626", zorder=5)
    ax.text(-0.54, 0.26, r"$q_a$", fontsize=11.5, color="#dc2626")
    ax.text(-0.30, -0.12, r"$a$", fontsize=10.5, color="#334155")
    ax.text(0.42, 0.02, r"$q_b$", fontsize=11.5, color="#dc2626")
    ax.text(0.60, -0.32, r"$b$", fontsize=10.5, color="#334155")
    arrow(ax, (0, 0), (0, 1.25), color="#1e293b", lw=1.2, mutation_scale=9)
    ax.text(0.08, 0.90, r"$R$", fontsize=11.5, color="#1e293b")
    ax.text(0, -1.55, "Two Cavities (Prob. 2.39)", ha="center", fontsize=11.5, color="#1e293b")

    fig.tight_layout(w_pad=1.5)
    save_fig(fig, "ch2-conductors-cavities")


def make_ch2_two_wires():
    fig, ax = plt.subplots(figsize=(5.2, 3.0))
    ax.set_xlim(-2.6, 2.6)
    ax.set_ylim(-1.5, 1.7)
    ax.set_aspect("equal")
    ax.axis("off")

    arrow(ax, (-2.3, 0), (2.3, 0), color="#64748b", lw=1.3, mutation_scale=10)
    arrow(ax, (0, -1.3), (0, 1.45), color="#64748b", lw=1.3, mutation_scale=10)
    ax.text(2.35, -0.05, r"$y$", fontsize=13, color="#475569")
    ax.text(0.08, 1.42, r"$z$", fontsize=13, color="#475569")

    # Wires at y = +a and y = -a
    a = 0.85
    ax.scatter([a], [0], s=55, color="#dc2626", zorder=5)
    ax.scatter([-a], [0], s=55, color="#0066cc", zorder=5)
    ax.text(a - 0.08, -0.26, r"$+\lambda$", fontsize=12.5, color="#dc2626")
    ax.text(-a - 0.16, -0.26, r"$-\lambda$", fontsize=12.5, color="#0066cc")

    # Circular cylindrical equipotentials (x^2 doesn't matter; y0 = a coth, R = a csch)
    for u in [0.7, 1.1]:
        y0 = a / np.tanh(u)
        R = a / np.sinh(u)
        ax.add_patch(plt.Circle((y0, 0), R, facecolor="none", edgecolor="#dc2626", lw=1.2, alpha=0.7))
        ax.add_patch(plt.Circle((-y0, 0), R, facecolor="none", edgecolor="#0066cc", lw=1.2, alpha=0.7))

    ax.text(1.80, 1.38, r"$(y_0, 0)$, radius $R$", fontsize=11.5, color="#dc2626")
    save_fig(fig, "ch2-two-wires")


if __name__ == "__main__":
    make_coulomb_vectors()
    make_gaussian_pillbox()
    make_uniqueness_conductors()
    make_method_of_images()
    make_separation_slot()
    make_multipole_geometry()
    make_ch2_gauss_surfaces()
    make_ch2_triangle()
    make_ch2_conductors_cavities()
    make_ch2_two_wires()
    print("Regenerated all SVG diagrams and PNG previews.")
