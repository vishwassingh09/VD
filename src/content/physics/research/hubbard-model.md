---
title: "1. Hubbard Model"
tab: "research"
sectionId: "research-hubbard"
group: "Active Topics"
order: 1
---

<div class="report-container" style="max-width: 900px; margin: 0 auto; line-height: 1.6; text-align: justify;">

<h1 style="text-align: center; margin-bottom: 30px;">Simulating Hubbard Model using Exact Diagonalization and Quantum Computation</h1>

## Second Quantization

In formulating quantum mechanics from classical mechanics, we elevate the dynamical variables $q_i$ and $p_i$ to operators and define a commutation relation between them as $[q_i,p_i]=i\hbar$. This is called First Quantization.

When we elevate the wavefunction $\psi(r)$ itself to operator also known as Field Operator $\vu{\psi}(r)$, this formulation is called Second Quantization. Similar to how a $q_i$ has a canonical conjugate as $p_i$, the field operator $\vu{\psi}(r)$ has $\vu{\psi}^{\dagger}(r)$ and they have a commutation relation between them given as $[\vu{\psi}(r_1),\vu{\psi}^{\dagger}(r_2)]=\delta(r_1 - r_2)$ for Bosons and Anti-commutation relation for Fermions i.e. $\{\vu{\psi}(r_1),\vu{\psi^{\dagger}}(r_2)\}=\delta(r_1 - r_2)$.

This field operator which is function of space and time in one dimension in general is defined as :

$$
\vu{\psi}(r)=\sum_n c_n \phi_n(r)
$$

where, $\phi_n(x)$ is the usual first quantization wavefunction and $c_n$ is the annihilation operator. Similarly its canonical conjugate is defined as :

$$
\vu{\psi}^{\dagger}(r)=\sum_n c_n^{\dagger} \phi_n^*(r)
$$

where, $\phi_n^*(x)$ is the complex conjugate of the wave function and $c_n^{\dagger}$ is the creation operator.

These creation and annhilation operators will act on the STATE of the system which is called the "Fock Space". which we will denote by :

$$
\ket{n_1, n_2, n_3, ..., n_i, ... , n_N}
$$

where, $n_i$ tells us the number of particles present at the ith state (first quantization wavefunction).

A "Vaccum State", where physically there are no particles present in our space is $\ket{0, 0, ..., 0}$. So as an example if we act $c_1^{\dagger}$ on the vaccum state, we get $\sqrt{2} \ket{1, 0, ..., 0}$ and $c_1$ acting on vacuum state will give us zero.

<div style="background: var(--sidebar-border, #f8f9fa); padding: 15px; border-left: 4px solid var(--accent-color, #d32f2f); margin: 25px 0; border-radius: 4px;">

<h4 style="margin-top: 0; color: var(--accent-color, #d32f2f);">Disclaimer</h4>

We have borrowed the action of ladder operators from first quantization from the harmonic oscillator but physically these are two different operators. In first quantization the creation ladder operator will change the $\ket{n}$ to $\ket{n+1}$ by and factor of $\sqrt{n+1}$ and annihilation operator will change $\ket{n}$ to $\ket{n-1}$ by a factor of $\sqrt{n}$.

</div>

<hr style="margin: 40px 0; border: 0; border-top: 1px solid var(--sidebar-border, #e2e8f0);">

### System

If we look at atoms whose outermost shell is the s orbital then their wave function is not localized i.e. of the form $\psi = e^{i(k\cdot r)}$ (The probability of finding the particle is equally like everywhere). But if we take a look at the atoms whose outermost electrons lie in the d orbital. These wavefunctions are bound to the atom and they have localization around the ion. But the localization is not strong enough for them so as to stop them from tunneling the neighbouring atoms and occupy and empty state present. Now given the fixed number of such electrons and fixed number of sites, the system will choose a state such that the total energy of the system is minimized. The dynamics of such materials can be modelled by what is called the Hubbard Model whose Hamiltonian can be written as:

$$
H = -t \sum_{i,\sigma} c_{i,\sigma}^\dagger c_{i+1,\sigma} + h.c + U \sum_{i}^n {n_{i\uparrow}} {n_{i\downarrow}}
$$

where:

- $c_{i,\sigma}^\dagger$: The creation operator for an electron with spin $\sigma$ ($\uparrow$ or $\downarrow$) at site i.
- $c_{i,\sigma}$: The annihilation operator for an electron with spin $\sigma$ at site i.
- $t$: The hopping amplitude, representing the kinetic energy of an electron hopping between nearest-neighbor sites.
- $n_{i\sigma} = c_{i,\sigma}^\dagger c_{i,\sigma}$: The number operator for electrons with spin $\sigma$ at site i.
- $U$: The on-site Coulomb interaction energy between two electrons of opposite spins ($\uparrow$ and $\downarrow$) at the same site.

It is an extension of the Tight Binding Approximation for single band and inclusion of electron-electron repulsion. Hubbard Model was introduced in order to explain the insulating behaviour of partially filled Transition Metal Oxide like TiO. Not only that in the limiting behaviour where the repulsion between electrons is more than the tunneling term, the electrons tends to localize on sites having same spin and hence show ferromagnetism.

---

### State

We are going to choose our basis state as what is called Wernier Wave Functions (they are fourier transforms of conventional Bloch States) which will give us the state of ONE electron localized on ONE particular site labelled by index i.

$$
W_\gamma(\vec{r}-\vec{R_i}) = \frac{1}{\sqrt{N}} \sum_{k} e^{-i \vec{k}\cdot\vec{R_i}} \phi_{k,\gamma}(\vec{r})
$$

Here, $\gamma$ is the band index, $\vec{R}$ is the ionic position vector, $\phi(\vec{r})$ is the Bloch wave function. We can then also define a ortho normality between states of different sites.

$$
\bra{W_n(\vec{r}-\vec{R_i})}\ket{W_n(\vec{r}-\vec{R_j})} = \delta_{R_i,R_j}
$$

Since this is a fermionic system, each site can have either one up spin or one down spin or both one up and one down spin. In order to denote the state of the system i.e. all sites at once we will use the notation as follows:

$$
\ket{\uparrow} \quad \ket{\downarrow} \quad \ket{\uparrow\downarrow}
$$

---

## Exact Diagonalization

### 2 Sites 2 Electrons

All possible states for 2 sites and 2 electrons will look like:

$$
\ket{\uparrow,\uparrow} \quad \ket{0,\uparrow\downarrow} \quad \ket{\uparrow, \downarrow} \quad \ket{\downarrow,\uparrow} \quad \ket{\uparrow\downarrow, 0} \quad \ket{\downarrow,\downarrow}
$$

The Hamiltonian for this system is:

$$
\begin{aligned} H = &-t ( c_{1\uparrow}^\dagger c_{2\uparrow} + c_{2\uparrow}^\dagger c_{1\uparrow} + c_{1\downarrow}^\dagger c_{2\downarrow} + c_{2\downarrow}^\dagger c_{1\downarrow} ) \\ &+ U ( n_{1\uparrow} n_{1\downarrow} + n_{2\uparrow} n_{2\downarrow} ) \end{aligned}
$$

When we operate this Hamiltonian operator on all the six states we get:

<div style="background: var(--sidebar-border, #f9f9f9); padding: 15px; border-radius: 5px; font-size: 1.1em; text-align: center;">

$H \ket{\uparrow,\uparrow} = 0$

$H \ket{0,\uparrow\downarrow} = -t ( \ket{\uparrow, \downarrow} + \ket{\downarrow,\uparrow} ) + U (\ket{0,\uparrow\downarrow})$

$H \ket{\downarrow, \uparrow} = -t ( \ket{0,\uparrow\downarrow} + \ket{\uparrow\downarrow, 0} )$

$H \ket{\downarrow\uparrow, 0} = -t ( \ket{\downarrow,\uparrow} + \ket{\uparrow, \downarrow}) + U \ket{\uparrow\downarrow, 0}$

$H \ket{\downarrow,\downarrow} = 0$

</div>

From this we can easily get the matrix element. For t = 1, U = 1:

$$
\begin{bmatrix} 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 1 & -1 & -1 & 0 & 0 \\ 0 & -1 & 0 & 0 & -1 & 0 \\ 0 & -1 & 0 & 0 & -1 & 0 \\ 0 & 0 & -1 & -1 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}
$$

On Diagonalizing this matrix numerically using LAPACK library function, we get Eigenvalues : 2.56, -1.56, 1, 0, 0, 0. The Ground State Energy as -1.56.

---

### Nagaoka's Theorem

**Statement:** In Hubbard Model, the relative ground state in the sector with one unoccupied site is maximally FERROMAGNETIC for large U.

<div style="text-align: center; margin: 30px 0;">
    <img src="/images/Nagaoka.png" alt="Nagaoka's Theorem Graph" style="max-width: 100%; height: auto; border: 1px solid #ccc; border-radius: 4px;">
    <p style="color: #666; font-size: 0.9em; margin-top: 8px;"><em>For 4 sites and 3 electrons we have plotted U v/s Ground State Energies</em></p>
</div>

In operational sense it means that if we take one less than half filled sites, then for large value of U (interaction between electrons on same site), the ground state of the system will be Ferromagnetic and spins will try to allow themselves in one direction. The Hubbard model can become equivalent to the Heisenberg model in the limit of strong electron-electron interactions (U) compared to the kinetic energy (t), particularly in the limit of large U and at half-filling of the electron density (one electron per lattice site). In this regime, virtual hopping processes are suppressed due to the high energy cost of double occupancy, leading to an effective spin-spin interaction between localized electrons. Under these conditions, the Hubbard model effectively reduces to the Heisenberg model, where the kinetic energy terms are neglected, and the dominant interactions are described by spin operators.

<hr style="margin: 40px 0; border: 0; border-top: 1px solid var(--sidebar-border, #e2e8f0);">

## Quantum Simulation

### Qubit

In quantum computing, the fundamental unit of information is the qubit, which can exist in a superposition of two basis states $|0\rangle$ and $|1\rangle$. The state of a single qubit is generally represented as:

$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle
$$

where:

- $|0\rangle$ and $|1\rangle$ are the computational basis states, analogous to the classical binary states.
- $\alpha$ and $\beta$ are complex numbers representing the probability amplitudes of the respective basis states.
- The coefficients satisfy the normalization condition $|\alpha|^2 + |\beta|^2 = 1$, ensuring the total probability is conserved.

<div style="text-align: center; margin: 30px 0;">
    <img src="/images/Bloch.png" alt="Bloch Sphere" style="max-width: 50%; height: auto; border: 1px solid #ccc; border-radius: 4px;">
    <p style="color: #666; font-size: 0.9em; margin-top: 8px;"><em>Bloch Sphere</em></p>
</div>

A general qubit in this 3 dimensional space can then be written as:

$$
|\psi\rangle = \cos\left(\frac{\theta}{2}\right) |0\rangle + e^{i\phi} \sin\left(\frac{\theta}{2}\right) |1\rangle
$$

where:

- $\theta$ is the polar angle ($0 \leq \theta \leq \pi$).
- $\phi$ is the azimuthal angle ($0 \leq \phi < 2\pi$).
- The coefficients $\alpha$ and $\beta$ are parameterized as: $\alpha = \cos\left(\frac{\theta}{2}\right)$ and $\beta = e^{i\phi} \sin\left(\frac{\theta}{2}\right)$.

In the context of quantum computing, the $|0\rangle$ and $|1\rangle$ states of a qubit can be mapped to the physical occupation states of a fermionic site:

- $|0\rangle$: Represents the absence of a particle (no occupation) at the site.
- $|1\rangle$: Represents the presence of a particle (occupied) at the site.

For the Hubbard Model, which includes both spin-up ($\uparrow$) and spin-down ($\downarrow$) fermions at each site, the Hilbert space of a single site is expanded to account for four possible states:

- $|00\rangle$: No particles at the site.
- $|01\rangle$: A spin-down ($\downarrow$) particle occupies the site.
- $|10\rangle$: A spin-up ($\uparrow$) particle occupies the site.
- $|11\rangle$: Both spin-up ($\uparrow$) and spin-down ($\downarrow$) particles occupy the site.

---

### Jordan Wigner Transformation

The Jordan-Wigner Transformation allows fermionic creation and annihilation operators to be represented as spin operators. Specifically, the creation and annihilation operators at site $j$ are expressed as:

$$
\begin{aligned} c_{j}^\dagger &= \frac{1}{2} \left( \prod_{k=1}^{j-1} Z_k \right) (X_j - i Y_j) \\ c_{j} &= \frac{1}{2} \left( \prod_{k=1}^{j-1} Z_k \right) (X_j + i Y_j) \end{aligned}
$$

---

### Variational Quantum Eigensolver

The ground state energy of a quantum system can be expressed as the expectation value of the Hamiltonian $H$ with respect to a trial wavefunction $|\psi(\theta)\rangle$, parameterized by $\theta$. Mathematically, this is given by:

$$
E(\theta) = \langle \psi(\theta) | H | \psi(\theta) \rangle
$$

where $E(\theta)$ represents the energy for a given parameter set $\theta$. The Variational Quantum Eigensolver aims to minimize this energy by optimizing the parameters $\theta$ such that:

$$
E_{\text{ground}} = \min_{\theta} \langle \psi(\theta) | H | \psi(\theta) \rangle
$$

<div style="text-align: center; margin: 30px 0;">
    <img src="/images/VQE.png" alt="Variational Quantum Eigensolver" style="max-width: 100%; height: auto; border: 1px solid #ccc; border-radius: 4px;">
    <p style="color: #666; font-size: 0.9em; margin-top: 8px;"><em>Variational Quantum Algorithm Eigensolver</em></p>
</div>

The *Variational Quantum Eigensolver* (VQE) is a hybrid quantum-classical algorithm designed to find the ground state energy of quantum systems. The algorithm minimizes the expectation value of the Hamiltonian $H$, which represents the system's energy operator, to identify the lowest possible energy state.

</div>
