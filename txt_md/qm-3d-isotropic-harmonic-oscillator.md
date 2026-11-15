<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-3d-isotropic-harmonic-oscillator.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answer** 

The degeneracy of the **5th excited state** is **6** . 

## **Step-by-Step Derivation** 

**1. Energy Formula for a 3D Cubic Box** The energy of a particle of mass _m_ in a 3D cubic box of side _L_ is given by: 



<!-- Start of picture text -->
E = π 2 h ¯2 ( n 2 x +  n 2 y +  n z 2 )<br>2 mL 2<br><!-- End of picture text -->

where _nx, ny, nz ∈{_ 1 _,_ 2 _,_ 3 _, . . . }_ are **strictly positive integers** . Let _S_ = _n_<sup>2</sup> _x_<sup>+</sup><sup>_n_2</sup> _y_<sup>+</sup><sup>_n_</sup> _z_<sup>2.Theenergyofalevelisdirectlyproportionalto</sup><sup>_S_.</sup> 

**2. Order of Energy Levels (Increasing** _S_ **)** Listing the states in order of increasing energy: 

|State|Sum of Squares (_S_)|Quantum Number<br>Combinations<br>(_nx, ny, nz_)|Degeneracy (_g_)|
|---|---|---|---|
|**Ground State**|1<sup>2 </sup>+ 1<sup>2 </sup>+ 1<sup>2 </sup>=**3**|(1_,_1_,_1)|**1**|
|**1st Excited**|2<sup>2 </sup>+ 1<sup>2 </sup>+ 1<sup>2 </sup>=**6**|(2_,_1_,_1)_,_(1_,_2_,_1)_,_(1_,_1_,_2)|**3**|
|**State**||||
|**2nd Excited**<br>**State**|2<sup>2 </sup>+ 2<sup>2 </sup>+ 1<sup>2 </sup>=**9**|(2_,_2_,_1)_,_(2_,_1_,_2)_,_(1_,_2_,_2)|**3**|
|**3rd Excited**<br>**State**|3<sup>2 </sup>+ 1<sup>2 </sup>+ 1<sup>2 </sup>=**11**|(3_,_1_,_1)_,_(1_,_3_,_1)_,_(1_,_1_,_3)|**3**|
|**4th Excited**|2<sup>2 </sup>+ 2<sup>2 </sup>+ 2<sup>2 </sup>=**12**|(2_,_2_,_2)|**1**|
|**State**||||
|**5th Excited**|3<sup>2 </sup>+ 2<sup>2 </sup>+ 1<sup>2 </sup>=**14**|All 3!|**6**|
|**State**||permutations of<br>(3_,_2_,_1)||



Notes 

2 

The 6 distinct permutations for the 5th excited state ( _S_ = 14) are: 

(3 _,_ 2 _,_ 1) _,_ (3 _,_ 1 _,_ 2) _,_ (2 _,_ 3 _,_ 1) _,_ (2 _,_ 1 _,_ 3) _,_ (1 _,_ 3 _,_ 2) _,_ (1 _,_ 2 _,_ 3) 

Thus, **Degeneracy = 6** . 

**Why NOT** _gn_ =<sup><u>(</u></sup><sup>_n_</sup><sup><u>+1)(</u></sup> 2<sup>_n_</sup><sup><u>+2)</u></sup> **?** The formula _gn_ =<sup><u>(</u></sup><sup>_n_</sup><sup><u>+1)(</u></sup> 2<sup>_n_</sup><sup><u>+2)</u></sup> **does not apply** to a 3D box because: 

1. **Different Physics Systems:** 

   - _gn_ =<sup><u>(</u></sup><sup>_n_</sup><sup><u>+1)(</u></sup> 2<sup>_n_</sup><sup><u>+2)</u></sup> is strictly for a **3D Isotropic Quantum Harmonic Oscillator** , where quantum numbers start at zero ( _ni ≥_ 0). 

   - For a **3D Box** , quantum numbers start at one ( _ni ≥_ 1). 

2. **Energy Dependence on Quantum Numbers:** 

   - **Harmonic Oscillator:** _E ∝_ ( _nx_ + _ny_ + _nz_ ) _→_ Energy depends **linearly** on the sum. 

   - **3D Box:** _E ∝_ ( _n_<sup>2</sup> _x_<sup>+</sup><sup>_n_2</sup> _y_<sup>+</sup><sup>_n_</sup> _z_<sup>2)</sup><sup>_→_Energydependsonthe</sup><sup>**sumofsquares**.</sup> 

Because of the sum-of-squares dependence (<sup>∑</sup> _n_<sup>2</sup> _i_<sup>), there is</sup><sup>**nosingleclosed-formpoly-**</sup> **nomial formula** for the degeneracy of a 3D box. Degeneracy must be calculated by counting valid integer partitions that sum to the same value of _S_ . 

**Follow-up suggestion:** Would you like to practice a question on **accidental degeneracy** (such as states like (4 _,_ 1 _,_ 1) vs (3 _,_ 3 _,_ 0)) or explore **symmetric vs. asymmetric 3D boxes (** _Lx̸_ = _Ly̸_ = _Lz_ **)** next? 

