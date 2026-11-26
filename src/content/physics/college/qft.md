---
title: "6. Quantum Field Theory (QFT)"
tab: "college"
sectionId: "college-qft"
group: "Relativistic Limits"
order: 6
---

## Many-Body Relativistic Quantum Physics (QFT)

QFT is an attempt to unify the rules of the fast world with the rules of the small world. One of the first steps in these directions can be just to pick up the classical rules of energy conservation, apply the operator formalism and see if we can keep the conservation of probability intact while maintaining the Lorentz covariance.

<div style="background: var(--sidebar-border, #f8f9fa); padding: 15px; border-left: 4px solid var(--accent-color, #007bff); margin: 25px 0; border-radius: 4px;">

<h3 style="margin-top: 0; color: var(--accent-color, #007bff); font-size: 1.1em;">Deep Dive: Where do the operators come from?</h3>

Fundamentally, energy and momentum are the conserved quantities associated with time and space translation symmetries (Noether's Theorem). In quantum mechanics, the generator of time translation is the Hamiltonian, giving us the energy operator $E \to i\hbar \frac{\partial}{\partial t}$. The generator of space translation gives us the momentum operator $\mathbf{p} \to -i\hbar \nabla$. We plug these directly into classical energy equations to find our quantum equations of motion.

</div>

<hr style="margin: 40px 0; border: 0; border-top: 2px solid var(--accent-color, #007bff);">

### 1. The Non-Relativistic Case (Schrödinger Equation)

We start with the classical energy conservation for a free particle:

$$
E = \frac{p^2}{2m}
$$

Applying the operator formalism to a state $|\psi\rangle$ (represented by a complex wavefunction $\psi$), we get the standard Schrödinger equation:

$$
i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m} \nabla^2 \psi
$$

Doing the same for the "bra" vector (taking the complex conjugate of the equation) gives:

$$
-i\hbar \frac{\partial \psi^*}{\partial t} = -\frac{\hbar^2}{2m} \nabla^2 \psi^*
$$

To verify if probability is conserved, we calculate the time evolution of the probability density (the mod square, $\rho = \psi^*\psi$):

$$
\frac{\partial \rho}{\partial t} = \frac{\partial}{\partial t}(\psi^* \psi) = \psi^* \frac{\partial \psi}{\partial t} + \frac{\partial \psi^*}{\partial t} \psi
$$

Substituting the time derivatives from our two Schrödinger equations:

$$
\frac{\partial \rho}{\partial t} = \psi^* \left( \frac{i\hbar}{2m} \nabla^2 \psi \right) - \left( \frac{i\hbar}{2m} \nabla^2 \psi^* \right) \psi
$$

$$
\frac{\partial \rho}{\partial t} = \frac{i\hbar}{2m} \nabla \cdot (\psi^* \nabla \psi - \psi \nabla \psi^*)
$$

By defining the probability current $\mathbf{j} = \frac{-i\hbar}{2m} (\psi^* \nabla \psi - \psi \nabla \psi^*)$, we arrive at the continuity equation:

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{j} = 0
$$

Because $\rho = |\psi|^2 \geq 0$, probability is strictly positive and perfectly conserved. Non-relativistic QM works beautifully!

<hr style="margin: 40px 0; border: 0; border-top: 2px solid var(--accent-color, #007bff);">

### 2. The Relativistic Case (Klein-Gordon Equation)

Now, let's attempt the exact same procedure using the relativistic energy-momentum relation:

$$
E^2 = p^2c^2 + m^2c^4
$$

Applying the energy and momentum operators to a wavefunction $\phi$, we obtain the Klein-Gordon equation:

$$
-\hbar^2 \frac{\partial^2 \phi}{\partial t^2} = -\hbar^2 c^2 \nabla^2 \phi + m^2 c^4 \phi
$$

Taking the complex conjugate for the bra vector:

$$
-\hbar^2 \frac{\partial^2 \phi^*}{\partial t^2} = -\hbar^2 c^2 \nabla^2 \phi^* + m^2 c^4 \phi^*
$$

To check for probability conservation, we multiply the first equation by $\phi^*$, the second by $\phi$, and subtract them (effectively taking the dot product to find the conserved current):

$$
-\hbar^2 \left( \phi^* \frac{\partial^2 \phi}{\partial t^2} - \phi \frac{\partial^2 \phi^*}{\partial t^2} \right) = -\hbar^2 c^2 \left( \phi^* \nabla^2 \phi - \phi \nabla^2 \phi^* \right)
$$

This can be mathematically massaged into a continuity equation $\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{j} = 0$, but this time, the "probability density" $\rho$ evaluates to:

$$
\rho = \frac{i\hbar}{2mc^2} \left( \phi^* \frac{\partial \phi}{\partial t} - \phi \frac{\partial \phi^*}{\partial t} \right)
$$

<h4 style="color: #d32f2f; margin-top: 25px;">The Breakdown of Single-Particle Probability</h4>

Here lies the catastrophic failure of single-particle relativistic quantum mechanics. Because the Klein-Gordon equation is *second-order* in time, both the initial wavefunction $\phi$ and its time derivative $\partial_t \phi$ can be chosen completely independently.

As a direct result, **the density $\rho$ can be negative!**

A negative probability makes absolutely no physical sense. To resolve this paradox, we can no longer treat $\phi$ as a simple probability wavefunction. Instead, $\rho$ must be reinterpreted as a *charge density* (which is allowed to be positive or negative), and $\phi$ must be elevated from a state vector to a **Quantum Field Operator** capable of creating and annihilating particles. This mathematical necessity is the birthplace of Quantum Field Theory.

<hr style="margin: 40px 0; border: 0; border-top: 2px solid var(--accent-color, #007bff);">

### 3. Dirac's Brilliant Fix (The Dirac Equation)

In 1928, Paul Dirac sought to cure the negative probability disease of the Klein-Gordon equation. He realized that to guarantee a positive probability density (like the Schrödinger equation), the new equation had to be **first-order in time**. However, to satisfy special relativity, space and time must be treated on equal footing, meaning the equation also had to be **first-order in space**.

Dirac effectively tried to take the "square root" of the relativistic energy equation $E^2 = p^2c^2 + m^2c^4$. He proposed a linear equation of the form:

$$
E = c(\alpha_1 p_1 + \alpha_2 p_2 + \alpha_3 p_3) + \beta mc^2
$$

<div style="background: var(--sidebar-border, #f8f9fa); padding: 20px; border-left: 4px solid #28a745; margin: 25px 0; border-radius: 4px;">

<h4 style="margin-top: 0; color: #28a745; font-size: 1.1em;">The Algebraic Deduction: Why 4x4?</h4>

Dirac knew that if he squared his new linear equation, it had to perfectly reproduce the standard relativistic energy equation. Let's expand $E^2$:

$$
E^2 = c^2 \sum_{i=1}^3 \alpha_i^2 p_i^2 + c^2 \sum_{i < j} (\alpha_i \alpha_j + \alpha_j \alpha_i)p_i p_j + mc^3 \sum_{i=1}^3 (\alpha_i \beta + \beta \alpha_i)p_i + \beta^2 m^2c^4
$$

For this massive expansion to collapse neatly back into $E^2 = p^2c^2 + m^2c^4$, the coefficients $\alpha_i$ and $\beta$ must satisfy three strict mathematical rules:

1. **They must square to 1:** $\alpha_1^2 = \alpha_2^2 = \alpha_3^2 = \beta^2 = I$
2. **They must mutually anti-commute:** $\alpha_i \alpha_j + \alpha_j \alpha_i = 0$ (for $i \neq j$)
3. **$\beta$ must anti-commute with all $\alpha$'s:** $\alpha_i \beta + \beta \alpha_i = 0$

Clearly, ordinary numbers cannot anti-commute ($2 \times 3$ is always $3 \times 2$). Therefore, $\alpha_i$ and $\beta$ **must be matrices**. But what size?

- Because they square to $I$, their eigenvalues can only be $+1$ or $-1$.
- Because they anti-commute, one can prove mathematically that their *trace* (the sum of their diagonal elements) must be strictly zero.
- For the trace to be zero, there must be an equal number of $+1$ and $-1$ eigenvalues. This means the matrices **must have an even dimension** ($2 \times 2$, $4 \times 4$, $6 \times 6$, etc.).

Could they be $2 \times 2$? The physics world already knew of three mutually anti-commuting $2 \times 2$ matrices: the Pauli spin matrices ($\sigma_x, \sigma_y, \sigma_z$). However, Dirac needed **four** mutually anti-commuting matrices (three $\alpha$'s for spatial dimensions, and one $\beta$ for mass). Since there are only three such $2 \times 2$ matrices in existence, $2 \times 2$ is too small!

Dirac was therefore forced to move to the next smallest even dimension: **$4 \times 4$ matrices**.

</div>

Applying the quantum operator formalism ($E \to i\hbar \partial_t$ and $\mathbf{p} \to -i\hbar \nabla$) to Dirac's linear Hamiltonian yields the original **Dirac Equation**:

<div style="background-color: var(--sidebar-border, #f9f9f9); padding: 15px; border-radius: 8px; font-weight: bold;">

$$
i\hbar \frac{\partial \psi}{\partial t} = \left( -i\hbar c \boldsymbol{\alpha} \cdot \nabla + \beta mc^2 \right) \psi
$$

</div>

Because the operators are $4 \times 4$ matrices, the wavefunction $\psi$ can no longer be a simple scalar function. It is forced by the math to become a 4-component column vector called a **Dirac Spinor**. This mathematical inevitability accidentally predicted the existence of intrinsic *spin-1/2* (up and down states) and the existence of *antimatter* (the positron)!

<h4 style="margin-top: 25px;">The Covariant Form</h4>

To make the Lorentz symmetry obvious, we multiply the equation by $\beta / c$ and define new matrices called the Gamma matrices: $\gamma^0 = \beta$ and $\gamma^i = \beta \alpha_i$. In natural units ($\hbar = c = 1$), the Dirac equation takes its most famous, compact covariant form:

$$
(i\gamma^\mu \partial_\mu - m)\psi = 0
$$

---

### 4. Popular Bases for the Gamma Matrices

The algebra of the Gamma matrices ($\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}$) defines the physics, but the actual $4 \times 4$ matrices can be written in different ways (bases) depending on the physical regime being studied. Here are the three most common representations:

- **The Dirac (Standard) Basis:**
  Best suited for *non-relativistic limits*. In this basis, $\gamma^0$ is diagonal. It perfectly separates the spinor into a "large" upper component (representing the particle) and a "small" lower component (representing the antiparticle) at low energies.

  $$
  \gamma^0 = \begin{pmatrix} I & 0 \\ 0 & -I \end{pmatrix}, \quad \gamma^i = \begin{pmatrix} 0 & \sigma^i \\ -\sigma^i & 0 \end{pmatrix}
  $$

- **The Weyl (Chiral) Basis:**
  Best suited for *ultra-relativistic limits* or massless particles (like the historical view of neutrinos). Here, $\gamma^5$ is diagonal. It splits the Dirac spinor into left-handed and right-handed chiral Weyl spinors, which is essential for studying the Weak Interaction and parity violation.

  $$
  \gamma^0 = \begin{pmatrix} 0 & I \\ I & 0 \end{pmatrix}, \quad \gamma^i = \begin{pmatrix} 0 & \sigma^i \\ -\sigma^i & 0 \end{pmatrix}
  $$

- **The Majorana Basis:**
  Designed so that all Gamma matrices are purely imaginary. As a result, the Dirac equation becomes a purely real differential equation. This is used to describe Majorana fermions—particles that are their own antiparticles (a heavy area of research in modern condensed matter and neutrino physics).
