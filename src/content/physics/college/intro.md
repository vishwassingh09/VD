---
title: "Dynamics"
tab: "college"
sectionId: "college-intro"
sidebarLabel: "🎓 College"
isIntro: true
order: 0
---

## Dynamics

To simplify the study of dynamical systems we will divide it into six main parts depending on whether we are studying single/many body, at low/high speeds and if we are in the quantum/classical limits. For three out of four forces we have experimentally verified Quantum Theory. For the fourth force of Gravity we have a very beautiful classical theory by Einstein whose Quantum Part is yet to be discovered experimentally but still we have really a very strong candidate called String Theory which is mathematically consistent and brings all forces under one formalism. For now we will be exploring these experimentally verified regimes:

1. Single Body Non-Relativistic Classical Physics (CM)
2. Many Body Non-Relativistic Classical Physics (SM)
3. Single Body Non-Relativistic Quantum Physics (QM)
4. Many Body Non-Relativistic Quantum Physics (CMP)
5. Single Body Relativistic Classical Physics (STR+GR)
6. Many-Body Relativistic Quantum Physics (QFT)

In any kind of Dynamics, it's helpful to define the SYSTEM, the STATE and EVOLUTION. In Newtonian Mechanics, we defined the SYSTEM as the particle acted on by a Force whose STATE (Initial) was given by pair of position and velocity vectors and finally using Newtons Laws F=ma (solving this differential equation), we can get the position and velocity at later times (final state). We can extend this idea to our six divisions.

<div class="table-container" style="overflow-x: auto;">
    <table class="evolution-table">
        <thead>
            <tr>
                <th>System Framework</th>
                <th>1. CM</th>
                <th>2. SM</th>
                <th>3. QM</th>
                <th>4. CMP</th>
                <th>5. STR+GR</th>
                <th>6. QFT</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>The System</strong></td>
                <td>A low-speed particle</td>
                <td>A probability distribution (ensemble)</td>
                <td>A wavefunction</td>
                <td>An interacting many-body lattice</td>
                <td>A massive body in curved spacetime</td>
                <td>A quantized field</td>
            </tr>
            <tr>
                <td><strong>State Variables (State)</strong></td>
                <td>$$(\mathbf{x}, \mathbf{p})$$</td>
                <td>$$\rho(\mathbf{q}, \mathbf{p})$$</td>
                <td>$$|\psi\rangle$$</td>
                <td>$$|\Psi\rangle$$</td>
                <td>$$g_{\mu\nu}, x^\mu(\tau)$$</td>
                <td>$$\hat{\phi}(x), |0\rangle$$</td>
            </tr>
            <tr>
                <td><strong>Dynamical Equation (Evolution)</strong></td>
                <td>$$m\ddot{\mathbf{x}} = -\nabla V$$</td>
                <td>$$\frac{\partial \rho}{\partial t} = \{H, \rho\}$$</td>
                <td>$$i\hbar\frac{\partial}{\partial t}|\psi\rangle = \hat{H}|\psi\rangle$$</td>
                <td>$$\hat{H} = -t \sum_{\langle i,j \rangle, \sigma} (\hat{c}_{i\sigma}^\dagger \hat{c}_{j\sigma} + h.c.) + U \sum_i \hat{n}_{i\uparrow} \hat{n}_{i\downarrow}$$</td>
                <td>$$R_{\mu\nu} - \frac{1}{2}Rg_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$</td>
                <td>$$\mathcal{L} = \bar{\psi}(i\gamma^\mu\partial_\mu - m)\psi$$</td>
            </tr>
        </tbody>
    </table>
</div>
