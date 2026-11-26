---
title: "Electrostatics"
tab: "school"
sectionId: "phys-electrostatics"
group: "Electricity"
order: 13
---

## Electrostatics

Electrostatics deals with the study of forces, fields, and potentials arising from static charges. This forms the foundation for electromagnetism.

---

### 1. Coulomb's Law

Coulomb's law states that the electrostatic force between two point charges is directly proportional to the product of the magnitudes of charges and inversely proportional to the square of the distance between them.

$$
F = \frac{1}{4\pi\epsilon_0} \frac{q_1 q_2}{r^2}
$$

**Vector Form:** The force on charge $q_2$ due to $q_1$ is given by:

$$
\vec{F}_{12} = \frac{1}{4\pi\epsilon_0} \frac{q_1 q_2}{r^2} \hat{r}_{12}
$$

Where $\epsilon_0$ is the permittivity of free space ($\approx 8.854 \times 10^{-12} \text{ C}^2\text{N}^{-1}\text{m}^{-2}$).

---

### 2. Electric Field and Potential

**Electric Field (E):** The electrostatic force experienced per unit positive test charge. For a point charge $q$ at a distance $r$:

$$
\vec{E} = \frac{\vec{F}}{q_0} = \frac{1}{4\pi\epsilon_0} \frac{q}{r^2} \hat{r}
$$

**Electric Potential (V):** The work done by an external force in bringing a unit positive charge from infinity to a point. For a point charge $q$:

$$
V = \frac{1}{4\pi\epsilon_0} \frac{q}{r}
$$

**Relation between E and V:** The electric field is the negative gradient of the electric potential.

$$
\vec{E} = -\nabla V = -\left( \frac{\partial V}{\partial x}\hat{i} + \frac{\partial V}{\partial y}\hat{j} + \frac{\partial V}{\partial z}\hat{k} \right)
$$

---

### 3. Electric Dipole

A system of two equal and opposite charges ($+q$ and $-q$) separated by a small distance ($2a$). The dipole moment $\vec{p}$ is a vector directed from $-q$ to $+q$ with magnitude $p = q(2a)$.

**Torque in a Uniform Electric Field:** When placed in a uniform field $\vec{E}$, the net force is zero, but the charges experience equal and opposite forces creating a couple. The torque ($\tau$) is the cross product of dipole moment and electric field:

$$
\vec{\tau} = \vec{p} \times \vec{E} \implies \tau = pE \sin\theta
$$

**Potential Energy of a Dipole:** The work done in rotating a dipole from an angle $\theta_1$ to $\theta_2$ is stored as potential energy ($U$). Taking standard reference at $90^\circ$:

$$
U = -\vec{p} \cdot \vec{E} = -pE \cos\theta
$$

---

### 4. Gauss's Law

**Electric Flux ($\Phi_E$):** The measure of electric field lines crossing a given surface area. For a uniform electric field and a planar area vector $\vec{A}$:

$$
\Phi_E = \int \vec{E} \cdot d\vec{A}
$$

**Gauss's Theorem:** The total electric flux through any closed surface is equal to $1/\epsilon_0$ times the net charge enclosed by the surface.

$$
\oint \vec{E} \cdot d\vec{A} = \frac{q_{\text{enclosed}}}{\epsilon_0}
$$

*Exam Note:* Gauss's Law is primarily useful for finding electric fields for highly symmetric charge distributions (e.g., infinite line charge, infinite plane sheet, spherical shells).
