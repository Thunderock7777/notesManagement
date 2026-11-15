<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-radial-probability-density-hydrogen-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 



<!-- Start of picture text -->
Correct Answer<br>Option (a): P ( r ) = a4 3 0 r2e − 2r / a0<br><!-- End of picture text -->

## **Detailed Step-by-Step Solution** 

**1. Ground State Wavefunction of the Hydrogen Atom** The quantum state of the electron in the ground state of a Hydrogen atom is characterized by quantum numbers _n_ = 1 _, l_ = 0 _, m_ = 0. 

The spatial wavefunction _ψ_ 100( _r, θ, ϕ_ ) is spherically symmetric (independent of angles _θ_ and _ϕ_ ): 



<!-- Start of picture text -->
2 1 1<br>ψ 100( r ) =  R 10( r ) Y 00 = e −r / a 0 = e −r / a 0<br>( a 3/2 0 ) ( √ 4 π ) √ πa 3 0<br><!-- End of picture text -->

where: 



<!-- Start of picture text -->
• R 10( r ) = 2<br>a 3/2 0 e−r / a 0 is the radial wavefunction.<br>• a 0 = 4 πϵ me 02 h ¯ 2 ≈ 0 . 529 Å is the Bohr radius.<br><!-- End of picture text -->

**2. Probability Density vs. Radial Probability Density** There is a critical distinction in quantum mechanics between **volume probability density** and **radial probability density** : 

- **3D Volume Probability Density** _|ψ_ ( _r_ ) _|_<sup>2</sup> **:** Measures the probability per unit volume of finding the electron near a specific point ( _r, θ, ϕ_ ): 



<!-- Start of picture text -->
1<br>|ψ 100( r ) | 2 = e − 2 r / a 0<br>πa 3 0<br><!-- End of picture text -->

_(This is maximum at the origin r_ = 0 _)._ 

- **Radial Probability Density** _P_ ( _r_ ) **:** Measures the total probability per unit radial thickness of finding the electron in a spherical shell of radius _r_ and thickness _dr_ . 

Notes 

2 

The differential volume element in spherical polar coordinates is: 

_dV_ = _r_<sup>2</sup> sin _θ dr dθ dϕ_ 

Integrating over all angles _θ ∈_ [0 _, π_ ] and _ϕ ∈_ [0 _,_ 2 _π_ ] (since ∫ sin _θdθdϕ_ = 4 _π_ ): 



<!-- Start of picture text -->
dP = |ψ ( r ) | 2 dV = 4 πr 2 |ψ 100( r ) | 2 dr =  P ( r )  dr<br>∫angles<br><!-- End of picture text -->

**3. Calculate** _P_ ( _r_ ) Substitute _ψ_ 100( _r_ ) = <u>1</u> _~~√~~ πa_<sup>3</sup> 0<sup>_e−r_/</sup><sup>_a_0intothedefinition</sup><sup>_P_(</sup><sup>_r_)=</sup> 4 _πr_<sup>2</sup> _|ψ_ ( _r_ ) _|_<sup>2</sup> : 



<!-- Start of picture text -->
1<br>P ( r ) = 4 πr 2 e −r / a 0 = 4 πr 2 e − 2 r / a 0<br>( √ πa 3 0 )2 ( πa 1 3 0 )<br><!-- End of picture text -->



<!-- Start of picture text -->
P ( r ) = 4 r 2 e − 2r / a0<br>a 3<br>0<br><!-- End of picture text -->

Alternatively, using the normalized radial wavefunction _R_ 10( _r_ ): 



<!-- Start of picture text -->
P ( r ) =  r 2 |R 10( r ) | 2 =  r 2 2 e −r / a 0 = 4 r 2 e − 2r / a0<br>( a 3/2 0 )2 a 3 0<br><!-- End of picture text -->

**Key Concepts & Formulae to Remember for GATE** 

**1. Normalization Condition** The total probability of finding the electron anywhere in space is 1: 



<!-- Start of picture text -->
P ( r )  dr = 4 r 2 e − 2 r / a 0 dr = 1<br>∫0 ∞ a 3 0 ∫0 ∞<br>(Useful Gamma Integral identity for GATE: ∫0 ∞ xne−axdx  = a n n +1 ! ) .<br><!-- End of picture text -->

**2. Most Probable Radius (** _r_ **mp)** To find the radius at which the electron is most likely to be found, set<sup>_dP_</sup> _dr_<sup><u>(</u></sup><sup>_r_</sup><sup><u>)</u></sup> = 0: 



<!-- Start of picture text -->
d r 2 e − 2 r / a 0 = 4 2 re − 2 r / a 0 − 2 r 2 e − 2 r / a 0 = 0<br>dr ( a 4 3 0 ) a 3 0 ( a 0 )<br>2 r 1  − r e − 2 r / a 0 = 0 = ⇒ r mp =  a0<br>( a 0 )<br><!-- End of picture text -->

**GATE Insight:** Even though the 3D probability density _|ψ_ ( _r_ ) _|_<sup>2</sup> is maximum at the nucleus ( _r_ = 0), the **radial probability density** _P_ ( _r_ ) peaks at the Bohr radius _r_ = _a_ 0 because the volume element 4 _πr_<sup>2</sup> _dr_ vanishes at the origin. 

Notes 

3 

**3. Expectation Values in the Ground State (** _n_ = 1 _, l_ = 0 **)** Using _⟨r_<sup>_k_</sup> _⟩_ = ∫0 _∞_<sup>_rkP_(</sup><sup>_r_)</sup><sup>_dr_:</sup> 

- **Average Distance** _⟨r⟩_ **:** 



<!-- Start of picture text -->
⟨r⟩ = 4 r 3 e − 2 r / a 0 dr = 3<br>a 3 0 ∫0 ∞ 2 a0<br><!-- End of picture text -->

- **Mean Squared Distance** _⟨r_<sup>2</sup> _⟩_ **:** 



<!-- Start of picture text -->
⟨r 2 ⟩ = a 43 0 ∫0 ∞ r 4 e − 2 r / a 0 dr =  3a 2 0<br><!-- End of picture text -->

- **Uncertainty in Position** ∆ _r_ **:** 



<!-- Start of picture text -->
√ 3<br>∆ r = √ ⟨r 2 ⟩−⟨r⟩ 2 = 3 a 2 0 − 9 0 =<br>√ 4 a 2 2 a0 ≈ 0 . 866a0<br><!-- End of picture text -->



<!-- Start of picture text -->
• Expectation Value of Inverse Distance ⟨ 1 r ⟩ :<br>= 1<br>⟨ 1 r ⟩ a0<br><!-- End of picture text -->



<!-- Start of picture text -->
• Expectation Value of ⟨ r 1 2 ⟩ :<br>= 2<br>r 2 a 2<br>⟨ 1 ⟩ 0<br><!-- End of picture text -->

**4. Hydrogen-like Ions (Nuclear Charge** _Z_ **)** For a hydrogen-like system with atomic number _Z_ (e.g., He<sup>+</sup> _,_ Li<sup>2+</sup> ), substitute _a_ 0 _→_<sup>_<u>a</u>_</sup> _Z_<sup><u>0</u>:</sup> 



<!-- Start of picture text -->
PZ ( r ) = 4 Z 3 r 2 e − 2 Zr / a 0<br>a 3 0<br>r mp = a 0 ⟨r⟩ = 3 a 0<br>Z , 2 Z<br><!-- End of picture text -->

