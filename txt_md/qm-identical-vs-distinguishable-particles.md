<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-identical-vs-distinguishable-particles.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

It sounds like a paradox at first—how can particles be **identical** and **distinguishable** at the same time? 

In quantum mechanics and statistical mechanics, these two terms refer to two completely different properties: **intrinsic identity** vs. **spatial tracking/localization** . 

## **1. What “Identical” Means** 

Particles are **identical** if they 

share the exact same intrinsic physical properties. 

- They have the **same mass (** _m_ **)** , **same charge (** _q_ **)** , **same total spin (** _s_ **)** , and **same magnetic moment** . 

- You cannot tell particle #1 apart from particle #2 by looking at their fundamental nature. 

## **2. What “Distinguishable” Means** 

Particles are **distinguishable** if you can uniquely **label, track, or locate** each particle individually throughout time. 

- **How do quantum particles become distinguishable?** 

   - They become distinguishable when they are **spatially separated** or **localized at fixed positions in space** such that their wavefunctions **do not overlap** . 

- **Classic Physics Example:** Consider _N_ atoms fixed at specific lattice sites in a crystal lattice (like a paramagnetic solid or an array of quantum dots). 

      - Site #1 is at _⃗r_ 1, Site #2 is at _⃗r_ 2, …, Site #N is at _⃗rN_ . 

      - Even though the atoms are intrinsically identical, you can point to Site #1 and say _“This is Particle 1”_ , and point to Site #2 and say _“This is Particle 2”_ . 

Notes 

2 

## **3. Why This Gives** _D_ = (2 _s_ + 1)<sup>_N_</sup> 

For a single particle of spin _s_ , the number of allowed magnetic spin projections _ms ∈ {−s, −s_ + 1 _, . . . ,_ + _s}_ is: 

_g_ = 2 _s_ + 1 

Because the particles are **distinguishable** (labeled 1 _,_ 2 _, . . . , N_ by their distinct spatial locations): 

1. Particle #1 can choose any of the (2 _s_ + 1) spin states. 

2. Particle #2 can choose any of the (2 _s_ + 1) spin states. 

3. … 

4. Particle #N can choose any of the (2 _s_ + 1) spin states. 

Crucially, because they are distinguishable, swapping their spins produces a **physically distinct microstate** : 



<!-- Start of picture text -->
=<br>| ↑⟩ 1 | ↓⟩ 2 | ↓⟩ 1 | ↑⟩ 2<br><!-- End of picture text -->

Therefore, by the fundamental counting principle, the total dimension of the Hilbert space is simply the product of their individual state spaces: 



<!-- Start of picture text -->
D  = ( 2s  +  1 )  ×  ( 2s  +  1 )  × · · · ×  ( 2s  +  1 ) = ( 2s  +  1 ) N<br><!-- End of picture text -->

## **Summary Comparison for GATE Physics** 

|Particle<br>Classification|Physical Scenario|Can swapping particles<br>create a new state?|Total Hilbert Space /<br>Microstate Counting<br>(_D_)|
|---|---|---|---|
|**Identical &**|Localized spins at|**YES**|(**2s**+**1**)<sup>**N**</sup>|
|**Distinguishable**|fixed lattice sites in<br>a crystal solid.|(_| ↑⟩_1_| ↓⟩_2_̸_ =_| ↓⟩_1_| ↑⟩_2)||
|**Identical & In-**<br>**distinguishable**|Electrons free to<br>move in a 1D/3D|**NO** (Must form an<br>antisymmetric Slater|(**2s**+**1**<br>**N**<br>)<br>_(for N ≤_2_s_+ 1<br>_single-particle states)_|
|**Fermions**|box (overlapping<br>wavefunctions).|determinant)||
|**Identical & In-**<br>**distinguishable**<br>**Bosons**|Photons/Rubidium<br>atoms in an optical<br>trap (overlapping<br>wavefunctions).|**NO** (Must form a<br>symmetric<br>wavefunction)|(**N**+(**2s**+**1**)_−_**1**<br>**N**<br>)|



