<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-pauli-exclusion-principle-fermions-3.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answer** 

**Option (b): L2** [sin ( _<u>π</u>_ **Lx1** ) sin ( **<u>2</u>** _<u>π</u>_ **Lx2** ) _−_ sin ( **<u>2</u>** _<u>π</u>_ **Lx1** ) sin ( _<u>π</u>_ **Lx2** )] _(Note: With full normalization, the overall prefactor is_ _~~<u>√</u>~~ L_ <u>2</u><sup>_, but option (b) uniquely specifies_</sup> _the correct antisymmetric spatial structure)._ 

## **Detailed Step-by-Step Solution** 

**1. The Pauli Exclusion Principle & Total Wavefunction** Electrons are **fermions** (spin-1/2 particles). According to the **Spin-Statistics Theorem** , the total wavefunction Ψ(1 _,_ 2) of a system of two identical fermions must be **completely antisymmetric** under the exchange of the two particles: 



<!-- Start of picture text -->
Ψ(1 ,  2) =  − Ψ(2 ,  1)<br><!-- End of picture text -->

The total wavefunction is the product of a **spatial wavefunction** _ψ_ ( _x_ 1 _, x_ 2) and a **spin wavefunction** _χ_ (1 _,_ 2): 



<!-- Start of picture text -->
Ψ(1 ,  2) =  ψ ( x 1 , x 2)  χ (1 ,  2)<br><!-- End of picture text -->

**2. Analyze the Spin Wavefunction** _χ_ (1 _,_ 2) The problem specifies that **both electrons are spin-up** ( _ms_ = +1/2): 



<!-- Start of picture text -->
χ (1 ,  2) =  | ↑ 1 ↑ 2 ⟩<br><!-- End of picture text -->

Exchanging particle 1 and particle 2 in this spin state gives: 



<!-- Start of picture text -->
χ (2 ,  1) =  | ↑ 2 ↑ 1 ⟩ =  | ↑ 1 ↑ 2 ⟩ = + χ (1 ,  2)<br><!-- End of picture text -->

Since the spin part _χ_ (1 _,_ 2) is **SYMMETRIC** under exchange, the spatial part _ψ_ ( _x_ 1 _, x_ 2) **MUST BE ANTISYMMETRIC** to keep the overall wavefunction antisymmetric: 

Total Ψ (Antisymmetric) = _ψ_ spatial (Antisymmetric) _× χ_ spin (Symmetric) 

_ψ_ ( **x2** _,_ **x1** ) = _−ψ_ ( **x1** _,_ **x2** ) 

Notes 

2 

**3. Determine Single-Particle Spatial Quantum Numbers** The single-particle wavefunctions for a 1D box of length _L_ are: 



<!-- Start of picture text -->
2<br>ϕn ( x ) = , n  = 1 ,  2 ,  3 , . . .<br>√ L sin ( nπxL )<br><!-- End of picture text -->

- **Can both electrons occupy** _n_ = 1 **?** 

If _n_ 1 = 1 and _n_ 2 = 1, an antisymmetric spatial state would be: 

_ψ_ ( _x_ 1 _, x_ 2) _∝ ϕ_ 1( _x_ 1) _ϕ_ 1( _x_ 2) _− ϕ_ 1( _x_ 2) _ϕ_ 1( _x_ 1) = 0 

Two electrons with identical spin-up orientations **cannot** occupy the same spatial state (Pauli Exclusion Principle). 

- **Lowest Energy Configuration (Ground State):** To get the lowest possible total energy while obeying Pauli exclusion, one electron must occupy _n_ 1 = 1 and the other must occupy _n_ 2 = 2. 

**4. Construct the Antisymmetric Spatial Wavefunction** Combining _n_ 1 = 1 and _n_ 2 = 2 into an antisymmetric linear combination: 



<!-- Start of picture text -->
ψ ( x 1 , x 2) = 1<br>√ 2 [ ϕ 1( x 1) ϕ 2( x 2)  − ϕ 2( x 1) ϕ 1( x 2)]<br><!-- End of picture text -->

<u>2 2</u> : Substitute _ϕ_ 1( _x_ ) = _L_<sup>sin</sup> ( _<u>πxL</u>_ ) and _ϕ_ 2( _x_ ) = _L_<sup>sin</sup> ( 2 _Lπx_ ) ~~√ √~~ 



<!-- Start of picture text -->
2 2<br>ψ ( x 1 , x 2) = √ 1 2 L L sin ( πxL 1 ) sin ( 2 πxL 2 ) − sin ( 2 πxL 1 ) sin ( πxL 2 ) ]<br>( √ ) ( √ ) [<br>√ 2<br>ψ ( x1 ,  x2 ) = sin sin − sin sin<br>L ( π Lx1 ) L L ( π Lx2<br>[ ( 2 π x2 ) ( 2 π x1 ) ) ]<br><!-- End of picture text -->

Matching the structure with a minus sign _−_ between the swapped product terms gives **Option (b)** . 

## **Evaluation of Options** 

- **Option (a):** Symmetric spatial wavefunction with _n_ 1 = 1 _, n_ 2 = 1 _→_ **Violates Pauli Exclusion Principle for same-spin electrons.** 

- **Option (b):** Antisymmetric spatial wavefunction with _n_ 1 = 1 _, n_ 2 = 2 _→_ **CORRECT!** 

- **Option (c):** Symmetric spatial wavefunction with _n_ 1 = 1 _, n_ 2 = 2 _→_ **Incorrect** (valid only if spin state was antisymmetric / singlet). 

- **Option (d):** Symmetric spatial wavefunction with _n_ 1 = 2 _, n_ 2 = 2 _→_ **Incorrect** (higher energy and violates Pauli principle). 

Notes 

3 

## **Key Concepts & Formulae to Remember for GATE** 

## **1. Spin States of Two Spin-1/2 Particles** 

|Total Spin _S_|_MS_ Values|State Configuration|Exchange Symmetry|
|---|---|---|---|
|**Triplet (**_S_ = 1**)**|+1_,_0_, −_1|_| ↑↑_<br>_⟩,_<br>_|↑↓⟩_+_|↓↑⟩_<br>_~~√~~_<br>2<br>_,_<br>_| ↓↓⟩_|**SYMMETRIC**<br>=_⇒_Spatial part<br>must be<br>**Antisymmetric**|
|**Singlet (**_S_ = 0**)**|0|_|↑↓⟩−|↓↑⟩_<br>_~~√~~_<br>2|**ANTISYMMETRIC**<br>=_⇒_Spatial part<br>must be **Symmetric**|



**2. Ground State Energy Comparison for Two Particles in a 1D Box** 

   - **Two Distinguishable Particles (or Opposite Spin Electrons in Singlet State):** Both particles can sit in _n_ = 1: 



<!-- Start of picture text -->
E ground =  E 1 +  E 1 = π 2 h ¯2<br>2 mL 2 (12 + 12) = π mL 2h ¯ 22<br><!-- End of picture text -->

- **Two Identical Same-Spin Electrons (Triplet State):** Particles must occupy _n_ 1 = 1 and _n_ 2 = 2: 



<!-- Start of picture text -->
E ground =  E 1 +  E 2 = π 2 h ¯2<br>2 mL 2 (12 + 22) = 5 2mL π 2h ¯ 22<br><!-- End of picture text -->

