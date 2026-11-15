<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-zeeman-effect-energy-level-splitting.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answer** 

**Option (a):** _±λ_ **B** 

## **Detailed Step-by-Step Solution** 

**Method 1: Pauli Vector Identity (Direct Operator Method)** 

1. **Square the Operator** _A_<sup>ˆ</sup> **:** The Hamiltonian operator is _A_<sup>ˆ</sup> = _λ_ ( _σ·_ **B** ). Let’s evaluate _A_ ˆ<sup>2</sup> : _A_ ˆ<sup>2</sup> = _λ_<sup>2</sup> ( _σ ·_ **B** )( _σ ·_ **B** ) 

2. **Apply the Fundamental Pauli Identity:** For any three-dimensional vector **a** , the inner product with Pauli vector satisfies: 



<!-- Start of picture text -->
( σ ·  a )( σ ·  b ) = ( a  ·  b ) I +  iσ ·  ( a  ×  b )<br><!-- End of picture text -->

Setting **a** = **b** = **B** : 



<!-- Start of picture text -->
( σ ·  B ) 2 = ( B  ·  B ) I +  iσ ·  ( B  ×  B ) =  B 2 I + 0 =  B 2 I<br><!-- End of picture text -->

_(where B_ = _|_ **B** _|_ =<sup>~~√~~</sup> _Bx_<sup>2+</sup><sup>_B_</sup> _y_<sup>2+</sup><sup>_B_</sup> _z_<sup>2</sup><sup>_isthemagnitudeofthemagneticfield)._</sup> 3. **Find the Eigenvalues:** Substituting this back into _A_<sup>ˆ2</sup> : 



<!-- Start of picture text -->
A ˆ 2 =  λ 2 B 2 I<br><!-- End of picture text -->

If _E_ represents an eigenvalue of _A_<sup>ˆ</sup> , then _E_<sup>2</sup> must be an eigenvalue of _A_<sup>ˆ2</sup> : 



<!-- Start of picture text -->
E 2 =  λ 2 B 2 = ⇒ E  =  ±λ B<br><!-- End of picture text -->

4. **Verify via Trace:** Since Tr( _σx_ ) = Tr( _σy_ ) = Tr( _σz_ ) = 0, the trace of _A_<sup>ˆ</sup> is zero (Tr( _A_<sup>ˆ</sup> ) = _E_ 1 + _E_ 2 = 0). Thus, the two eigenvalues must be equal in magnitude and opposite in sign: + _λB_ **and** _−λB_ . 

Notes 

2 

**Method 2: Coordinate Alignment Shortcut** Since quantum mechanics is invariant under spatial rotations, we can choose our coordinate system such that the magnetic field **B** points along the _z_ -axis without loss of generality: 



<!-- Start of picture text -->
B  = (0 ,  0 , B )<br><!-- End of picture text -->

Then the operator simplifies to: 



<!-- Start of picture text -->
0 0<br>=<br>A ˆ =  λ ( σ ·  B ) =  λσzB =  λB<br>0 − 1 0 −λB<br>(1 ) ( λB )<br><!-- End of picture text -->

Since this matrix is already diagonal, its eigenvalues are directly read off from the main diagonal: **E1** = + _λ_ **B** and **E2** = _−λ_ **B** 

## **Evaluation of Options** 

- **Option (a):** _±λ_ **B** _→_ **CORRECT!** 

- **Option (b):** _±_ 2 _λB →_ **Incorrect** 

- **Option (c):** 0 _, λB →_ **Incorrect** 

- **Option (d):** 0 _, −λB →_ **Incorrect** 

**Key Concepts & Formulae to Remember for GATE** 

**1. Crucial Pauli Matrix Vector Identities** For any vectors **a** and **b** : 

   - ( _σ ·_ **a** )<sup>2</sup> = _|_ **a** _|_<sup>2</sup> _I_ = ( _a_<sup>2</sup> _x_<sup>+</sup><sup>_a_2</sup> _y_<sup>+</sup><sup>_a_</sup> _z_<sup>2)</sup><sup>_I_</sup> 

   - det( _σ ·_ **a** ) = _−|_ **a** _|_<sup>2</sup> 

   - **Tr** ( _σ ·_ **a** ) = 0 

   - ( _σ ·_ **a** )( _σ ·_ **b** ) = ( **a** _·_ **b** ) _I_ + _iσ ·_ ( **a** _×_ **b** ) 

**2. Physical Application: Zeeman Effect & Energy Splitting** The interaction Hamiltonian of a magnetic dipole moment _µ_ = _γ_ **S** =<sup>_<u>gq</u>_</sup> 4 _m_<sup>_h_¯</sup><sup>_σ_inamagneticfield</sup><sup>**B**is:</sup> 



<!-- Start of picture text -->
H =  −µ ·  B  =  − gqh ¯<br>4 m ( σ ·  B )<br>• Ground state energy: E− =  − 1 2 gµBB (spin aligned parallel to B )<br>• Excited state energy: E + = + 1 2 gµBB (spin anti-parallel to B )<br>• Zeeman Energy Splitting ( ∆ E ):<br><!-- End of picture text -->



<!-- Start of picture text -->
∆ E =  E +  − E− =  gµBB = 2 λB<br><!-- End of picture text -->

**Follow-up suggestion:** Would you like to solve a problem involving **spin precession frequency (Larmor frequency)** or calculate **time-dependent state transition probabilities** in a magnetic field next? 

