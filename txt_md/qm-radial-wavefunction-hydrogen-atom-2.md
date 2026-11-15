<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-radial-wavefunction-hydrogen-atom-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answer** 

**Option (a): Plot with 1 radial node** 

## **Detailed Step-by-Step Solution** 

**1. Quantum Numbers for the** 3 _p_ **Orbital** For a hydrogen atom state specified by the radial wavefunction _Rnl_ ( _r_ ): 

- **Principal Quantum Number (** _n_ **):** _n_ = 3 

- **Orbital Quantum Number (** _l_ **):** For a _p_ -orbital, _l_ = 1 (where _s → l_ = 0, _p → l_ = 1, _d → l_ = 2, _f → l_ = 3). 

**2. Formula for Nodal Surfaces in Hydrogen Wavefunctions** In three-dimensional central potentials, the complete spatial wavefunction is separated into radial and angular parts: 



<!-- Start of picture text -->
ψnlm ( r, θ, ϕ ) =  Rnl ( r ) Ylm ( θ, ϕ )<br><!-- End of picture text -->

The nodes (regions where the probability density vanishes) are categorized as: 

1. **Total Nodes:** _N_ total = _n −_ 1 

2. **Angular Nodes (Nodal Cones/Planes):** _Na_ = _l_ 

3. **Radial Nodes (Spherical Nodal Shells):** _Nr_ = _n − l −_ 1 

Applying the formula for the 3 _p_ **orbital** ( _n_ = 3 _, l_ = 1): 



<!-- Start of picture text -->
Nr = 3  − 1  − 1 =  1 radial node<br><!-- End of picture text -->

**3. Explicit Radial Wavefunction** _R_ 31( _r_ ) **Analysis** The normalized radial wavefunction for the 3 _p_ state of Hydrogen ( _Z_ = 1) is given by: 



<!-- Start of picture text -->
R 31( r ) = 8 1  − r e −r /3 a 0<br>27 √ 6 a 3/2 0 ( 6 a 0 ) ( ar 0 )<br><!-- End of picture text -->

Notes 

2 

where _a_ 0 is the Bohr radius. 

Analyzing the behavior of _R_ 31( _r_ ): 

- **At** _r_ = 0 **(Origin):** Since _Rnl_ ( _r_ ) _∝ r_<sup>_l_</sup> as _r →_ 0, for _l_ = 1, _R_ 31(0) = 0. 

- **Radial Node Location (** _R_ 31( _r_ ) = 0 **for** _r >_ 0 **):** 



<!-- Start of picture text -->
1  − r = 0 = ⇒ r  =  6a0<br>6 a 0<br><!-- End of picture text -->

This linear factor yields **exactly one real positive root** at _r_ = 6 _a_ 0. 



<!-- Start of picture text -->
• Asymptotic Behavior ( r →∞ ): R 31( r )  → 0 exponentially as e −r /3 a 0 .<br><!-- End of picture text -->

Therefore, a schematic plot of _R_ 31( _r_ ) versus _r_ starts at zero at the origin, rises to a positive peak, crosses the horizontal axis at _r_ = 6 _a_ 0 ( **1 radial node** ), reaches a negative minimum, and asymptotically approaches zero at infinity. 

## **Summary Table: Node Comparison for Low-Lying Hydrogen Orbitals** 

|State|_n_|_l_|Total<br>Nodes<br>(_n −_1)|Angular<br>Nodes (_l_)|Radial<br>Nodes<br>(_n −l −_1)|Behavior<br>at _r_ = 0|
|---|---|---|---|---|---|---|
|1_s_|1|0|0|0|0|Non-zero<br>(_R̸_= 0)|
|2_s_|2|0|1|0|1|Non-zero<br>(_R̸_= 0)|
|2_p_|2|1|1|1|0|Zero<br>(_R_= 0)|
|3_s_|3|0|2|0|2|Non-zero<br>(_R̸_= 0)|
|3_p_|3|1|2|1|**1**|Zero<br>(_R_= 0)|
|3_d_|3|2|2|2|0|Zero<br>(_R_= 0)|



## **Key Takeaways & Conceptual Guidelines for GATE Physics** 

1. **Origin Behavior (** _r_ = 0 **):** 

   - Only _s_ -orbitals ( _l_ = 0) have a non-zero radial wavefunction value at the nucleus ( _Rn_ 0(0) _̸_ = 0). 

   - All orbitals with orbital angular momentum _l ≥_ 1 ( _p, d, f, . . ._ ) vanish at the origin ( _Rnl_ (0) = 0) due to the centrifugal potential barrier<sup>_l_</sup><sup><u>(</u></sup> 2<sup>_l_</sup><sup><u>+</u></sup> _mr_<sup>1)2</sup><sup>_h_¯2.</sup> 

2. **Maximum Angular Momentum States (** _l_ = _n −_ 1 **):** 

   - States such as 1 _s,_ 2 _p,_ 3 _d,_ 4 _f_ have _n − l −_ 1 = 0 radial nodes. Their radial wavefunctions decay smoothly without crossing the zero axis. 

3. **Radial Probability Distribution** _P_ ( _r_ ) **:** 

Notes 

3 

- _P_ ( _r_ ) = _r_<sup>2</sup> _|Rnl_ ( _r_ ) _|_<sup>2</sup> represents the probability of finding the electron in a spherical shell between _r_ and _r_ + _dr_ . 

- The radial nodes of _Rnl_ ( _r_ ) correspond to radii where _P_ ( _r_ ) = 0. 

**Follow-up suggestion:** Would you like to practice calculating the **most probable radius** _r_ **mp** or **expectation values** _⟨r⟩_ **and** _⟨_ 1/ _r⟩_ for hydrogenic orbitals? 

