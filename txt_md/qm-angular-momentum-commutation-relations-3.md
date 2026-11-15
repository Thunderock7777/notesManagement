<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-angular-momentum-commutation-relations-3.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**Correct Answer** 

**Option (b):** _−_ **a**<sup>**2**</sup> **0** 

**Method 1: Symmetry & Expectation Values (The 15-Second GATE Shortcut)** 

**1. Exploit Spherical Symmetry** The ground state _|_ 1 _s⟩_ ( _n_ = 1 _, l_ = 0 _, m_ = 0) of the Hydrogen atom has zero orbital angular momentum ( _l_ = 0), making its probability distribution **100% spherically symmetric** . 

In any spherically symmetric state, spatial direction is completely unbiased: 



<!-- Start of picture text -->
⟨x 2 ⟩ =  ⟨y 2 ⟩ =  ⟨z 2 ⟩<br><!-- End of picture text -->

Since _r_<sup>2</sup> = _x_<sup>2</sup> + _y_<sup>2</sup> + _z_<sup>2</sup> , taking the expectation value gives: 



<!-- Start of picture text -->
⟨r 2 ⟩ =  ⟨x 2 ⟩ +  ⟨y 2 ⟩ +  ⟨z 2 ⟩ = 3 ⟨z 2 ⟩ = ⇒⟨ z 2 ⟩ = 1<br>3 ⟨ r2 ⟩<br><!-- End of picture text -->

**2. Substitute** _⟨z_<sup>2</sup> _⟩_ **into the Operator** _Q_<sup>ˆ</sup> We are asked to find the expectation value of _Q_<sup>ˆ</sup> = 2 _z_<sup>2</sup> _− r_<sup>2</sup> : 



<!-- Start of picture text -->
⟨Q ˆ ⟩ =  ⟨ 2 z 2 − r 2 ⟩ = 2 ⟨z 2 ⟩−⟨r 2 ⟩<br><!-- End of picture text -->

Substitute _⟨z_<sup>2</sup> _⟩_ =<sup><u>1</u></sup> 3<sup>_⟨r_2</sup><sup>_⟩_:</sup> 



<!-- Start of picture text -->
⟨Q ˆ ⟩ = 2 −⟨r 2 ⟩ = ⟨r 2 ⟩ =  − 1<br>( 31 ⟨r 2 ⟩ ) ( 32 − 1 ) 3 ⟨r 2 ⟩<br><!-- End of picture text -->

**3. Plug in** _⟨r_<sup>2</sup> _⟩_ **for the** _|_ 1 _s⟩_ **Ground State** For the Hydrogen ground state _|_ 1 _s⟩_ , the expectation value of _r_<sup>2</sup> is: 



<!-- Start of picture text -->
⟨r 2 ⟩ 1 s = 3 a 2 0<br><!-- End of picture text -->

Substituting this in: 



<!-- Start of picture text -->
⟨Q ˆ ⟩ =  − 1 (3 a 2 0) =  − a 2 0<br>3<br><!-- End of picture text -->

Notes 

2 

**Method 2: Direct Angular & Radial Integration (Full Proof)** 

**1. Convert** _Q_<sup>ˆ</sup> **to Spherical Coordinates** Using _z_ = _r_ cos _θ_ = _⇒ z_<sup>2</sup> = _r_<sup>2</sup> cos<sup>2</sup> _θ_ : 



<!-- Start of picture text -->
Q ˆ = 2( r 2 cos 2 θ )  − r 2 =  r 2 (2 cos 2 θ − 1)<br><!-- End of picture text -->

## **2. Ground State Wavefunction** 



<!-- Start of picture text -->
1<br>ψ 100( r ) = e −r / a 0<br>√ πa 3 0<br><!-- End of picture text -->

**3. Evaluate the Integral** 



<!-- Start of picture text -->
⟨Q ˆ ⟩ = ψ 100 ∗ [ r 2 (2 cos 2 θ − 1)] ψ 100  r 2 sin  θ dr dθ dϕ<br>∫0 ∞ ∫0 π ∫0 2 π<br><!-- End of picture text -->

Splitting into independent radial, angular _θ_ , and angular _ϕ_ integrals: 

1. **Radial Integral:** 



<!-- Start of picture text -->
1 1 4!<br>r 4 |ψ 100( r ) | 2 dr = r 4 e − 2 r / a 0 dr = · 0<br>∫0 ∞ πa 3 0 ∫0 ∞ πa 3 0 (2/ a 0) 5 = 3 4 a π 2<br><!-- End of picture text -->

2. _θ_ **Angular Integral:** 



<!-- Start of picture text -->
− 2 = − − 2 =  − 2<br>∫0 π (2 cos 2 θ − 1) sin  θ dθ = [ 3 cos3  θ  + cos  θ ] π 0 ( 23 − 1 ) ( 3 + 1 ) 3<br><!-- End of picture text -->

3. _ϕ_ **Angular Integral:** 



<!-- Start of picture text -->
dϕ  = 2 π<br>∫0 2 π<br><!-- End of picture text -->

Combining all three parts: 



<!-- Start of picture text -->
0 × − 2<br>⟨Q ˆ ⟩ = ( 34 aπ 2 ) ( 3 ) ×  (2 π ) =  − a 2 0<br><!-- End of picture text -->

**Key Concepts & Formulae to Remember for GATE** 

**1. Expectation Values in Hydrogen** _|_ 1 _s⟩_ **State** 



<!-- Start of picture text -->
• ⟨r⟩ = 3 2 a 0<br>• ⟨r 2 ⟩ = 3 a 2 0<br>• ⟨z 2 ⟩ =  ⟨x 2 ⟩ =  ⟨y 2 ⟩ =  a 2 0<br><!-- End of picture text -->

Notes 

3 

**2. Quadrupole Operator vs.** _Q_<sup>ˆ</sup> = 2 _z_<sup>2</sup> _− r_<sup>2</sup> Be careful not to confuse 2 _z_<sup>2</sup> _− r_<sup>2</sup> with the **electric quadrupole moment operator** (3 _z_<sup>2</sup> _− r_<sup>2</sup> ): 



<!-- Start of picture text -->
• For Q ˆ quad = 3 z 2 − r 2 :<br><!-- End of picture text -->



<!-- Start of picture text -->
⟨ 3 z 2 − r 2 ⟩ = 3 ⟨z 2 ⟩−⟨r 2 ⟩ = 3( a 2 0 )  − 3 a 2 0 =  0<br><!-- End of picture text -->

_(The electric quadrupole moment strictly vanishes for all spherically symmetric s- states!)_ 

• **For** _Q_<sup>ˆ</sup> = 2 _z_<sup>2</sup> _− r_<sup>2</sup> **:** 



<!-- Start of picture text -->
⟨ 2 z 2 − r 2 ⟩ = 2( a 2 0 )  − 3 a 2 0 =  − a 0 2<br><!-- End of picture text -->

