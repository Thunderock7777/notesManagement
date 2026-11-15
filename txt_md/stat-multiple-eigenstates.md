<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: stat-multiple-eigenstates.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

In quantum mechanics, **multiple eigenstates** appear in two distinct physical situations: 

**Case 1: Degeneracy (Multiple Eigenstates Sharing the** **_Same_ Energy)** 

**When does it happen?** When a system has spatial symmetry (like the spherical symmetry of an atom), multiple **physically different wavefunctions** end up having the **exact same energy eigenvalue** _E_ . 

- **Example in Hydrogen (** _n_ = 2 **):** 

The baseline energy formula gives _E_ 2 = _−_ 3 _._ 4 eV. However, there are **4 distinct quantum states** (eigenstates) sitting at this exact same energy: 

   - _|_ 2 _,_ 0 _,_ 0 _⟩_ (2 _s_ orbital) 

   - _|_ 2 _,_ 1 _,_ +1 _⟩_ (2 _p_ orbital) 

   - _|_ 2 _,_ 1 _,_ 0 _⟩_ (2 _p_ orbital) 

   - _|_ 2 _,_ 1 _, −_ 1 _⟩_ (2 _p_ orbital) 

- **Physical Effect:** Because they share the exact same energy _E_ 2, combining them still produces a **stationary state** with a single, sharp energy _E_ 2. Applying an external field (like a magnetic field in the Zeeman effect) breaks the symmetry and splits these degenerate states into distinct energy levels. 

**Case 2: Superposition States (Multiple Eigenstates with** **_Different_ Energies) When does it happen?** Whenever a physical system is in a **dynamic, time-evolving state** that isn’t locked into a single energy level. 

Here are the primary real-world situations where a system exists across multiple energy eigenstates ( _E_ 1 _̸_ = _E_ 2 _̸_ = _E_ 3): 

**A. During Quantum Transitions (Light Emission / Absorption)** When an electron drops from an excited state ( _E_ 2) to a lower state ( _E_ 1) by emitting a photon, the transition doesn’t happen instantaneously. During the process, the electron is briefly in a **time-dependent superposition state** : 

Ψ( **r** _, t_ ) = _c_ 1( _t_ ) _ψ_ 1( **r** ) _e_<sup>_−iE_1</sup><sup>_t_/</sup><sup>_h_¯</sup> + _c_ 2( _t_ ) _ψ_ 2( **r** ) _e_<sup>_−iE_2</sup><sup>_t_/</sup><sup>_h_¯</sup> 

It is this interference between _E_ 1 and _E_ 2 that causes the electron cloud to oscillate back and forth, radiating an electromagnetic wave (light). 

Notes 

2 

**B. Moving Wave Packets (Localized Particles)** A free electron moving through space isn’t a single plane wave of fixed energy—it is a **wave packet** . Mathematically, a wave packet is built by adding together a continuous range of different energy eigenstates: 



<!-- Start of picture text -->
Ψ( x, t ) = c ( E ) ψE ( x ) e −iEt / h ¯ dE<br>∫<br><!-- End of picture text -->

**C. Sudden Perturbations / Quantum Kicks** If an atom sitting in its ground state _|E_ 1 _⟩_ experiences a sudden force (like a fast laser pulse or a collision with another particle), it gets “kicked” into a combination of several energy eigenstates ( _|E_ 1 _⟩, |E_ 2 _⟩, |E_ 3 _⟩, . . ._ ). 

**D. Quantum Computing & Laser State Preparation** In quantum information, lasers or microwave pulses are used intentionally to place a qubit into a superposition of its ground state _|_ 0 _⟩_ and excited state _|_ 1 _⟩_ : 



<!-- Start of picture text -->
|ψ⟩ = √ 1 2 | 0 ⟩ + √ 1 2 | 1 ⟩<br><!-- End of picture text -->

## **Summary Comparison** 

|Context|Energy Eigenvalues|Is it a Stationary<br>State?|Physical<br>Manifestation|
|---|---|---|---|
|**Degeneracy**|**One shared value**<br>(_E_1 =_E_2)|**Yes**|Orbitals sharing the<br>same energy<br>(e.g. 2_s,_2_px,_2_py,_2_pz_).|
|**Superposition**|**Multiple different**<br>**values** (_E_1_̸_ =_E_2)|**No**<br>(Time-dependent)|Oscillating electron<br>clouds, light emission,<br>moving wave packets,<br>qubits.|



Would you like to see how the oscillation frequency _ω_ =<sup>_<u>E</u>_</sup><sup><u>2</u></sup><sup>_−_</sup> _h_ ¯<sup>_<u>E</u>_</sup><sup><u>1</u></sup> in a two-state superposition leads directly to the frequency of emitted light ( _E_ = _hν_ )? 

