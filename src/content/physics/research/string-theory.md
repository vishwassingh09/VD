---
title: "3. String Theory"
tab: "research"
sectionId: "research-string"
group: "Active Topics"
order: 3
---

## String Theory

A theoretical framework in which the point-like particles of particle physics are replaced by one-dimensional objects called strings.

<hr style="margin: 20px 0; border: 0; border-top: 1px solid var(--sidebar-border, #e2e8f0);">

### Fundamental Strings & Extra Dimensions

Currently developing notes on the quantization of the relativistic string, D-branes, and the necessity of extra spatial dimensions for mathematical consistency.

<hr style="margin: 40px 0; border: 0; border-top: 1px solid var(--sidebar-border, #e2e8f0);">

## 1. The Relativistic Point Particle

Consider a point particle propagating in a $d$-dimensional target spacetime, tracing out a 1D worldline $x^\mu(\tau)$ where $\tau$ is the proper time. In classical physics, the principle of least action dictates that a free particle follows the path of extremal length. The proper length interval is $dl = \sqrt{-ds^2} = \sqrt{-\eta_{\mu\nu}dx^\mu dx^\nu}$.

The action is strictly proportional to the length of this worldline, with the particle's mass $m$ serving as the proportionality constant:

$$
S[x] = -m \int dl = -m \int d\tau \sqrt{-\eta_{\mu\nu} \dot{x}^\mu \dot{x}^\nu}
$$

*Note:* The negative sign inside the square root ensures a real value, as massive particles travel on timelike trajectories ($ds^2 < 0$). The negative sign outside ensures that maximizing the proper time (the straightest path in Minkowski space) minimizes the classical action.

Varying this action yields the canonical momentum $p_\mu = \frac{\partial L}{\partial \dot{x}^\mu} = \frac{m\dot{x}_\mu}{\sqrt{-\dot{x}^2}}$. Squaring this momentum vector inherently produces the classical mass-shell constraint:

$$
p^\mu p_\mu = \frac{m^2 \dot{x}^\mu \dot{x}_\mu}{-\dot{x}^\alpha \dot{x}_\alpha} = -m^2 \implies p^2 + m^2 = 0
$$

Upon applying Dirac quantization constraints ($\hat{p}_\mu \to -i\partial_\mu$), we demand that physical quantum states are annihilated by this constraint: $(\hat{p}^2 + m^2)|\psi\rangle = 0$, flawlessly recovering the Klein-Gordon equation.

---

## 2. The Bosonic String Actions

We now elevate our 0D point particle to a 1D string. As it moves through time, it sweeps out a 2D surface called a **worldsheet**, parameterized by $\sigma^a = (\tau, \sigma)$. The target spacetime coordinates are now scalar fields on this worldsheet: $X^\mu(\tau, \sigma)$.

### The Nambu-Goto Action

Generalizing the point particle, the string's action must be proportional to the proper *area* of the worldsheet. Geometrically, the area of a parallelogram spanned by two vectors $\vec{a}$ and $\vec{b}$ is $A = |\vec{a}||\vec{b}|\sin\theta$. Using $\sin^2\theta = 1 - \cos^2\theta$, we can rewrite this strictly using dot products:

$$
A = \sqrt{|\vec{a}|^2|\vec{b}|^2 - (\vec{a} \cdot \vec{b})^2}
$$

On the worldsheet, the tangent vectors are $\partial_\tau X^\mu$ and $\partial_\sigma X^\mu$. Their dot products form the **induced metric** $h_{ab} = \eta_{\mu\nu} \partial_a X^\mu \partial_b X^\nu$. The term under the square root is exactly the negative determinant of this metric. Therefore, the Nambu-Goto action is:

<div style="background: var(--sidebar-border, #f9f9f9); padding: 15px; border-radius: 8px;">

$$
S_{NG} = -T \int d\tau d\sigma \sqrt{-\det(h_{ab})}
$$

</div>

Here, $T = \frac{1}{2\pi\alpha'}$ is the string tension, where $\alpha'$ is the Regge slope.

### The Polyakov Action

The Nambu-Goto action is highly non-linear due to the square root, making path-integral quantization notoriously difficult. To solve this, Polyakov introduced an independent, auxiliary worldsheet metric $\gamma_{ab}(\tau, \sigma)$ to eliminate the square root:

<div style="background: var(--sidebar-border, #f9f9f9); padding: 15px; border-radius: 8px;">

$$
S_{P} = -\frac{T}{2} \int d^2\sigma \sqrt{-\gamma} \, \gamma^{ab} \partial_a X^\mu \partial_b X_\mu
$$

</div>

---

## 3. Symmetries and the Conformal Gauge

The Polyakov action is invariant under three critical symmetries:

1. **Global Poincaré Invariance:** Spacetime translations and rotations ($X^\mu \to \Lambda^\mu_\nu X^\nu + a^\mu$).
2. **Local Diffeomorphism:** Worldsheet coordinate reparameterizations.
3. **Weyl Invariance:** Local scale transformations of the metric: $\gamma_{ab} \to e^{2\omega(\tau, \sigma)}\gamma_{ab}$.

<div style="background: var(--sidebar-border, #f8f9fa); padding: 15px; border-left: 4px solid var(--accent-color, #007bff); margin: 25px 0; border-radius: 4px;">

<h4 style="margin-top: 0; color: var(--accent-color, #007bff);">The Magic of 2D Weyl Invariance</h4>

Why does Weyl scaling work so perfectly? If $\gamma_{ab} \to e^{2\omega}\gamma_{ab}$, the inverse metric scales as $\gamma^{ab} \to e^{-2\omega}\gamma^{ab}$. Meanwhile, the determinant $\gamma$ scales as $e^{4\omega}\gamma$, so its square root scales as $\sqrt{-\gamma} \to e^{2\omega}\sqrt{-\gamma}$. Plugging this into the action: $(e^{2\omega})(e^{-2\omega}) = 1$. The scaling factors exactly cancel out! This remarkable cancellation is unique to 2-dimensional worldsheets.

</div>

A $2 \times 2$ symmetric metric $\gamma_{ab}$ has 3 independent components. We can use our 2 diffeomorphism freedoms and 1 Weyl freedom to completely fix the metric to the flat Minkowski metric multiplied by a conformal factor: $\gamma_{ab} = e^\phi \eta_{ab}$. Because of Weyl invariance, $e^\phi$ drops out entirely, leaving the **Conformal Gauge**:

$$
S = \frac{T}{2} \int d\tau d\sigma (\dot{X}^2 - X'^2)
$$

The equations of motion are simply the 2D wave equation: $(\partial_\tau^2 - \partial_\sigma^2)X^\mu = 0$.

However, fixing the gauge means we must impose the equations of motion for the auxiliary metric $\gamma_{ab}$ as manual constraints. Varying the action with respect to $\gamma^{ab}$ yields the worldsheet stress-energy tensor $T_{ab} = 0$, giving us the **Virasoro Constraints**:

$$
\dot{X} \cdot X' = 0 \quad \text{and} \quad \dot{X}^2 + X'^2 = 0
$$

---

## 4. Quantization and the Critical Dimension

Solving the wave equation with Neumann boundary conditions (for open strings) yields a Fourier mode expansion of harmonic oscillators:

$$
X^\mu(\tau, \sigma) = x_0^\mu + 2\alpha' p_0^\mu \tau + i\sqrt{2\alpha'} \sum_{n \neq 0} \frac{\alpha_n^\mu}{n} e^{-in\tau} \cos(n\sigma)
$$

When quantized, the zero-mode of the Hamiltonian (the $L_0$ Virasoro operator) becomes:

$$
L_0 = \frac{1}{2} \alpha_0^2 + \sum_{n=1}^\infty \alpha_{-n} \cdot \alpha_n + \epsilon_0
$$

Here, $\epsilon_0$ is the infinite zero-point vacuum energy of all oscillator modes across the $d-2$ transverse dimensions. Using Riemann zeta-function regularization ($\sum_{n=1}^\infty n = \zeta(-1) = -1/12$), we find:

$$
\epsilon_0 = \frac{d-2}{2} \sum_{n=1}^\infty n = -\frac{d-2}{24}
$$

To preserve quantum conformal symmetry without anomalies, the intercept parameter $a$ must equal 1 ($a = -\epsilon_0 = 1$). Therefore:

<div style="font-weight: bold; color: #d32f2f;">

$$
\frac{d-2}{24} = 1 \implies d = 26
$$

</div>

The mathematics strictly demands that Bosonic String Theory can only exist in a 26-dimensional spacetime!

### The Tachyon Problem

The mass-squared operator for physical states is $m^2 = \frac{1}{\alpha'}(N - 1)$. For the ground state ($N=0$), we find $m^2 < 0$. This imaginary mass particle is the **Tachyon**. Its existence indicates that the bosonic vacuum is unstable, providing the historical and mathematical motivation to introduce fermions and Supersymmetry (leading to 10D Superstring Theory).
