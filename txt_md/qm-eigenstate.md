<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-eigenstate.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

In quantum mechanics, the difference between an **eigenstate** and **any state (a general quantum state)** is the difference between a **specific, definite baseline state** and a **general combination (superposition)** of those states. 

## **1. The Core Definitions** 

- **Eigenstate (Eigenvector / Eigenket):** An **eigenstate** of an observable operator _A_<sup>ˆ</sup> (like energy, momentum, or spin) is a special quantum state _|ψn⟩_ that, when acted upon by _A_<sup>ˆ</sup> , returns the exact same state multiplied by a single real number _an_ (the eigenvalue): 



<!-- Start of picture text -->
A ˆ |ψn⟩ =  an|ψn⟩<br><!-- End of picture text -->

   - **Physical meaning:** If a system is in an eigenstate of _A_<sup>ˆ</sup> , measuring _A_<sup>ˆ</sup> gives the outcome _an_ with **100% certainty** (zero uncertainty/variance). 

- **Any State (General Quantum State / Superposition State):** An **arbitrary state** _|_ Ψ _⟩_ of a quantum system is any valid state vector residing in Hilbert space. By the **principle of linear superposition** , any state can be expressed as a linear combination of the complete set of eigenstates _{|ψn⟩}_ : 



<!-- Start of picture text -->
| Ψ ⟩ =  c 1 |ψ 1 ⟩ +  c 2 |ψ 2 ⟩ +  c 3 |ψ 3 ⟩ +  · · ·  = ∑ cn|ψn⟩<br>n<br><!-- End of picture text -->

**– Physical meaning:** If a system is in a general state _|_ Ψ _⟩_ , measuring _A_<sup>ˆ</sup> does **not** give a single deterministic result. Instead, it yields one of the eigenvalues _an_ with probability _P_ ( _an_ ) = _|cn|_<sup>2</sup> . 

## **2. Main Differences At a Glance** 

|Feature|**Eigenstate** (of an operator<br>ˆ_A_)|**Any General State**|
|---|---|---|
|**Mathematical Form**|A single basis vector _|ψn⟩_.|A superposition|
|||_|_Ψ_⟩_= <sup>∑</sup><br>_n _<sup>_cn|ψn⟩_.</sup>|



Notes 

2 

|Feature|**Eigenstate** (of an operator<br>ˆ_A_)|**Any General State**|
|---|---|---|
|**Measurement Outcome**|**Deterministic:** Always<br>yields the eigenvalue _an_ with<br>100% certainty.|**Probabilistic:** Yields _an_<br>with probability _|cn|_<sup>2</sup>.|
|**Uncertainty (**_σA_**)**|**Zero:** _σA_ = 0.|**Non-zero:** _σA >_0 (unless it<br>happens to be an eigenstate).|
|**Expectation Value** _⟨_<sup>ˆ</sup>_A⟩_|Equal to the single eigenvalue<br>_an_.|Weighted average:<br>_⟨_<sup>ˆ</sup>_A⟩_= <sup>∑</sup><br>_n _<sup>_|cn|_2</sup><sup>_an_.</sup>|
|**Time Evolution** _(for_<br>_Energy Eigenstates)_|**Stationary State:**<br>Probability density<br>_|_Ψ(**r**_, t_)_|_<sup>2 </sup>=_|ψn_(**r**)_|_<sup>2 </sup>is<br>**constant in time**.|**Non-stationary State:**<br>Probability density<br>**oscillates/evolves in time**.|



## **3. A Simple Visual Analogy** 

Think of an ordinary 3D vector space: 

- **The Eigenstates** are like the main coordinate axes—the<sup>ˆ</sup> _i_ ( _x_ -axis),<sup>ˆ</sup> _j_ ( _y_ -axis), and _k_ ˆ ( _z_ -axis) direction vectors. 

- **Any State** is any arrow pointing in any arbitrary direction in that 3D space: _⃗V_ = _vx_<sup>ˆ</sup> _i_ + _vy_<sup>ˆ</sup> _j_ + _vzk_<sup>ˆ</sup> . 

In quantum mechanics, eigenstates form the **orthogonal coordinate axes (basis)** of Hilbert space, and **any general state** is a vector pointing in some direction built from a mixture of those basis axes. 

_Would you like to explore how a measurement forces “any state” to collapse into a single “eigenstate”, or see how this applies to a 2-level spin system?_ 

