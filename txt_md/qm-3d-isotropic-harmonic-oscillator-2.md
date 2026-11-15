<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-3d-isotropic-harmonic-oscillator-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**Correct Answer** 

**Option (b): 10** 

## **Detailed Step-by-Step Solution** 

**1. Energy Eigenvalues of a 3D Isotropic Quantum Harmonic Oscillator** The potential energy for a 3D isotropic harmonic oscillator is given by: 



<!-- Start of picture text -->
V  ( x, y, z ) = 1<br>2 mω 2( x 2 +  y 2 +  z 2)<br><!-- End of picture text -->

Using separation of variables in Cartesian coordinates, the energy eigenvalues are: 



<!-- Start of picture text -->
Enx,ny,nz = nx  +  ny  +  nz  + 3 hω ¯ = n  + 3 hω ¯<br>2 2<br>( ) ( )<br><!-- End of picture text -->

where _nx, ny, nz ∈{_ 0 _,_ 1 _,_ 2 _,_ 3 _, . . . }_ are non-negative integer quantum numbers, and _n_ = _nx_ + _ny_ + _nz_ represents the total principal quantum number. 

**2. General Degeneracy Formula** The degeneracy _gn_ of the _n_ -th energy level is equal to the number of distinct ways to partition the non-negative integer _n_ into three non-negative integers ( _nx, ny, nz_ ): 



<!-- Start of picture text -->
gn = ( n  + 1)( n  + 2)<br>2<br><!-- End of picture text -->

## **3. Calculating Degeneracy for the 3rd Excited State** 

- **Ground State (** _n_ = 0 **):** _E_ 0 =<sup><u>3</u></sup> 2<sup>_hω_¯</sup> 

- • **1st Excited State (** _n_ = 1 **):** _E_ 1 = 2<sup><u>5</u></sup><sup>_hω_¯</sup> 

- **2nd Excited State (** _n_ = 2 **):** _E_ 2 =<sup><u>7</u></sup> 2<sup>_hω_¯</sup> 

- **3rd Excited State (** _n_ = 3 **):** _E_ 3 =<sup><u>9</u></sup> 2<sup>_hω_¯</sup> 

Notes 

2 

Substitute _n_ = 3 into the degeneracy formula: 



<!-- Start of picture text -->
g 3 = (3 + 1)(3 + 2) = 4  ×  5 =  10<br>2 2<br><!-- End of picture text -->

**4. Explicit Enumeration of the 10 Microstates** The 10 distinct quantum states ( _nx, ny, nz_ ) satisfying _nx_ + _ny_ + _nz_ = 3 are: 

   1. **Permutations of** (3 _,_ 0 _,_ 0) **:** (3 _,_ 0 _,_ 0) _,_ (0 _,_ 3 _,_ 0) _,_ (0 _,_ 0 _,_ 3) _→_ **3 states** 

   2. **Permutations of** (2 _,_ 1 _,_ 0) **:** (2 _,_ 1 _,_ 0) _,_ (2 _,_ 0 _,_ 1) _,_ (0 _,_ 2 _,_ 1) _,_ (1 _,_ 2 _,_ 0) _,_ (1 _,_ 0 _,_ 2) _,_ (0 _,_ 1 _,_ 2) _→_ **6 states** 

   3. **Permutations of** (1 _,_ 1 _,_ 1) **:** (1 _,_ 1 _,_ 1) _→_ **1 state** 

Total Degeneracy _g_ 3 = 3 + 6 + 1 = **10** 

## **Low-Lying Energy Levels & Degeneracy Summary Table** 

|Energy Level|Total Quantum<br>Number (_n_)|Energy (_E_)|Allowed States<br>(_nx, ny, nz_)<br>Degeneracy<br>_gn_ = <sup>(</sup><sup>_n_+1)(</sup><sup>_n_+2)</sup><br>2|
|---|---|---|---|
|**Ground**|_n_= 0|3<br>2<sup>¯</sup><sup>_hω_</sup>|(0_,_0_,_0)<br>**1**|
|**State**||||
|1<sup>**st **</sup>**Excited**|_n_= 1|5<br>2<sup>¯</sup><sup>_hω_</sup>|(1_,_0_,_0)_,_(0_,_1_,_0)_,_(0_,_0_,_1)<br>**3**|
|**State**||||
|2<sup>**nd **</sup>**Excited**|_n_= 2|7<br>2<sup>¯</sup><sup>_hω_</sup>|(2_,_0_,_0)_,_(0_,_2_,_0)_,_(0_,_0_,_2)_,_(1_,_1_,_0)_,_(1_,_0_,_1)_,_(0_,_1_,_1)<br>**6**|
|**State**||||
|3<sup>**rd **</sup>**Excited**|_n_= 3|9<br>2<sup>¯</sup><sup>_hω_</sup>|(3_,_0_,_0)_,_(0_,_3_,_0)_,_(0_,_0_,_3)_,_(2_,_1_,_0)_,_(2_,_0_,_1)_,_(0_,_2_,_1)_,_(1<br>**10**|
|**State**||||
|4<sup>**th **</sup>**Excited**|_n_= 4|11<br>2 <sup>¯</sup><sup>_hω_</sup>|Permutations<br>**15**|
|**State**|||of<br>(4_,_0_,_0)_,_(3_,_1_,_0)_,_(2_,_2_,_0)_,_(2_,_1_,_1)|



**Follow-up suggestion:** Would you like to practice calculating the **degeneracy of a 2D or 3D anisotropic harmonic oscillator** (e.g., _ωx_ = _ωy_ = _ω_ and _ωz_ = 2 _ω_ ), or explore how **first-order perturbation theory** lifts this 10-fold degeneracy when an anharmonic perturbation like _V_<sup>_′_</sup> = _λxyz_ is introduced? 

