<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-2d-isotropic-harmonic-oscillator.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

For a **2D Isotropic Quantum Harmonic Oscillator** , the potential is _V_ ( _x, y_ ) = <u>12</u><sup>_mω_2(</sup><sup>_x_2 +</sup><sup>_y_2).</sup> 

## **1. Energy Eigenvalues in 2D** 

Separating variables in Cartesian coordinates, the single-particle energy eigenvalues are: 



<!-- Start of picture text -->
Enx,ny = ( nx  +  ny  + 1) ¯ hω = ( n  + 1) hω ¯<br><!-- End of picture text -->

where: 

- _nx, ny ∈{_ 0 _,_ 1 _,_ 2 _,_ 3 _, . . . }_ are non-negative integer quantum numbers. 

- _n_ = _nx_ + _ny_ is the total principal quantum number ( _n_ = 0 _,_ 1 _,_ 2 _,_ 3 _, . . ._ ). 

## **2. General Degeneracy Formula for 2D** 

The degeneracy _gn_ of the _n_ -th energy level is the number of distinct ways to partition the non-negative integer _n_ into **two** non-negative integers ( _nx, ny_ ): 



<!-- Start of picture text -->
nx  +  ny =  n<br><!-- End of picture text -->

Since _nx_ can take any integer value from 0 up to _n_ (and _ny_ = _n − nx_ is uniquely fixed for each choice), there are _n_ + 1 total choices. 



<!-- Start of picture text -->
gn =  n  +  1<br><!-- End of picture text -->

## **3. Low-Lying Energy Levels & Enumeration** 

Notes 

2 

|Energy Level|Total Quantum<br>Number (_n_)|Energy (_En_)|Allowed<br>Microstates<br>(_nx, ny_)<br>Degeneracy<br>(_gn_ =_n_+ 1)|
|---|---|---|---|
|**Ground**|_n_= 0|1¯_hω_|(0_,_0)<br>**1**|
|**State**||||
|1<sup>**st **</sup>**Excited**|_n_= 1|2¯_hω_|(1_,_0)_,_(0_,_1)<br>**2**|
|**State**||||
|2<sup>**nd **</sup>**Excited**|_n_= 2|3¯_hω_|(2_,_0)_,_(1_,_1)_,_(0_,_2)<br>**3**|
|**State**||||
|3<sup>**rd **</sup>**Excited**<br>**State**|_n_= 3|4¯_hω_|(3_,_0)_,_(2_,_1)_,_(1_,_2)_,_(0_,_3)<br>**4**|
|4<sup>**th **</sup>**Excited**<br>**State**|_n_= 4|5¯_hω_|(4_,_0)_,_(3_,_1)_,_(2_,_2)_,_(1_,_3)_,_(0_,_4)<br>**5**|



## **4. Master Comparison:** _d_ **-Dimensional Isotropic Harmonic Oscillator** 

Using the stars-and-bars combinatorics formula ( _n_ + _d−d−_ 1 1), the degeneracy of an isotropic quantum harmonic oscillator in _d_ dimensions is: 

|Dimension (_d_)|Zero-Point Energy|Energy Level _En_|Degeneracy Formula<br>(_gn_)|
|---|---|---|---|
|**1D**|1<br>2<sup>¯</sup><sup>_hω_</sup>|(<br>_n_+ <sup>1</sup><br>2<br>)<br>¯_hω_|**gn** =**1**<br>_(Non-degenerate)_|
|**2D**|1¯_hω_|(_n_+ 1)¯_hω_|**gn** =**n**+**1**|
|**3D**|3<br>2<sup>¯</sup><sup>_hω_</sup>|(<br>_n_+ <sup>3</sup><br>2<br>)<br>¯_hω_|**gn** = <sup>(</sup><sup>**n**+</sup><sup>**1**)(</sup><sup>**n**+</sup><sup>**2**)</sup><br>**2**<br>|
|_d_**-D**|_d_<br>2<sup>¯</sup><sup>_hω_</sup>|(<br>_n_+ <sup>_d_</sup><br>2<br>)<br>¯_hω_|**gn** =<br>(**n**+**d**_−_**1**<br>**d**_−_**1**<br>)|



Would you like to practice a question on an **anisotropic 2D oscillator** (where _ωx̸_ = _ωy_ ) to see how degeneracy breaks? 

