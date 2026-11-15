<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-pauli-exclusion-principle-fermions.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answer** 

**Option (b): 2h** ¯ _ω_ 

## **Detailed Step-by-Step Solution** 

**1. The Pauli Exclusion Principle & Total Wavefunction** Since the particles are **spin-1/2 fermions** , the total wavefunction Ψ(1 _,_ 2) must be **completely antisymmetric** under the exchange of the two particles: 



<!-- Start of picture text -->
Ψ(1 ,  2) =  − Ψ(2 ,  1)<br><!-- End of picture text -->

The total wavefunction is a product of a **spatial part** _ψ_ ( _x_ 1 _, x_ 2) and a **spin part** _χ_ (1 _,_ 2): 

Ψ(1 _,_ 2) = _ψ_ ( _x_ 1 _, x_ 2) _χ_ (1 _,_ 2) 

**2. Spin Symmetry for the Triplet State (** _S_ = 1 **)** A system of two spin-1/2 particles can form two total spin configurations: 

- **Triplet State (** _S_ = 1 **): Symmetric** under particle exchange. 

- **Singlet State (** _S_ = 0 **): Antisymmetric** under particle exchange. 

Because the system is specified to be in a **spin-triplet state** ( _χ_ spin is **symmetric** ), the spatial wavefunction _ψ_ ( _x_ 1 _, x_ 2) **MUST BE ANTISYMMETRIC** to satisfy the overall Fermi-Dirac statistics: 

Total Ψ (Antisymmetric) = _ψ_ spatial (Antisymmetric) _× χ_ spin (Symmetric) 

_ψ_ ( **x2** _,_ **x1** ) = _−ψ_ ( **x1** _,_ **x2** ) 

Notes 

2 

**3. Determine Single-Particle Energy Levels** The single-particle energy eigenvalues for a 1D harmonic oscillator are: 



<!-- Start of picture text -->
En = n  + 1 hω, ¯ n  = 0 ,  1 ,  2 ,  3 , . . .<br>2<br>( )<br><!-- End of picture text -->

   - Ground state ( _n_ = 0): _E_ 0 =<sup><u>1</u></sup> 2<sup>_hω_¯</sup> 

   - • First excited state ( _n_ = 1): _E_ 1 =<sup><u>3</u></sup> 2<sup>_hω_¯</sup> • Second excited state ( _n_ = 2): _E_ 2 =<sup><u>5</u></sup> 2<sup>_hω_¯</sup> 

**4. Apply Pauli Exclusion to Find Ground State Quantum Numbers** 

   - **Can both particles occupy** _n_ 1 = 0 **and** _n_ 2 = 0 **?** If _n_ 1 = 0 and _n_ 2 = 0, an antisymmetric spatial state would be: 



<!-- Start of picture text -->
ψ ( x 1 , x 2)  ∝ ϕ 0( x 1) ϕ 0( x 2)  − ϕ 0( x 2) ϕ 0( x 1) = 0<br><!-- End of picture text -->

This state vanishes! Two same-spin/triplet fermions **cannot** occupy the same spatial state. 

- **Lowest Energy State Configuration:** 

   - To minimize energy while maintaining spatial antisymmetry ( _n_ 1 _̸_ = _n_ 2), one particle must occupy _n_ 1 = 0 and the other must occupy _n_ 2 = 1. 

## **5. Calculate Total Ground State Energy** 



<!-- Start of picture text -->
E ground =  En 1=0 +  En 2=1<br><!-- End of picture text -->



<!-- Start of picture text -->
E ground = 0 + 1 hω ¯  + 1 + 1 hω ¯ = 1<br>2 2 2 hω ¯  + 2 3 hω ¯ =  2h ¯ ω<br>( ) ( )<br><!-- End of picture text -->

## **Comparison for GATE: Triplet vs. Singlet vs. Bosons** 

|System / Spin<br>Configuration|Spatial Symmetry|Single-Particle States<br>(_n_1_, n_2)|Total Ground State<br>Energy (_E_)|
|---|---|---|---|
|**Spin-Triplet**|**Antisymmetric**|(0_,_1)|**2**¯**h**_ω_|
|**(**_S_ = 1**) Fermions**||||
|**Spin-Singlet**<br>**(**_S_ = 0**) Fermions**|**Symmetric**|(0_,_0)|¯**h**_ω_|
|**Distinguishable**|No requirement|(0_,_0)|¯**h**_ω_|
|**Particles**||||
|**Spin-0 Bosons**|**Symmetric**|(0_,_0)|¯**h**_ω_|



Notes 

3 

## **Key Concepts & Formulae to Remember for GATE** 

**1.** _N_ **-Fermion Ground State Energy in 1D Harmonic Potential** For _N_ spin-1/2 non-interacting fermions in a 1D harmonic oscillator: 

   - Due to spin degeneracy ( _gs_ = 2), **at most 2 electrons** (one spin-up, one spin-down) can occupy each spatial level _n_ . 

   - The ground state energy is obtained by filling levels from _n_ = 0 _,_ 1 _,_ 2 _, . . ._ upward. 

**2. Quick Symmetry Rules for 2-Particle Systems** 

   - **Triplet Spin State (** _S_ = 1 **):** 

_χ_ (1 _,_ 2) = Symmetric = _⇒ ψ_ ( _x_ 1 _, x_ 2) = Antisymmetric 

- **Singlet Spin State (** _S_ = 0 **):** 



<!-- Start of picture text -->
χ (1 ,  2) = Antisymmetric = ⇒ ψ ( x 1 , x 2) = Symmetric<br><!-- End of picture text -->

