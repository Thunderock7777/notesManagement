<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-eigenvalues-and-eigenstates-formalism-3.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**Correct Answer** 

**Option (b): a0** _−|_ **b** _|_ 

**Detailed Step-by-Step Solution** 

**1. Understand the Matrix Structure** The Hamiltonian is defined as: 



<!-- Start of picture text -->
H =  a 0 I +  b  · σ<br><!-- End of picture text -->

where: 



<!-- Start of picture text -->
0<br>• I = is the 2  ×  2 identity matrix.<br>0 1<br>�1 �<br>• b  = ( bx, by, bz ) is a real 3D vector.<br>• σ = ( σx, σy, σz ) are the standard Pauli spin matrices:<br><!-- End of picture text -->



<!-- Start of picture text -->
1 −i 0<br>σx = , σy = , σz =<br>1 0 i 0 0 − 1<br>�0 � �0 � �1 �<br><!-- End of picture text -->

Expanding **b** _· σ_ : 



<!-- Start of picture text -->
bz bx − iby<br>b  · σ =  bxσx  +  byσy  +  bzσz =<br>� bx  +  iby −bz �<br><!-- End of picture text -->

**2. Find the Eigenvalues of b** _· σ_ 

**Method A: Using the Operator Identity** ( **b** _· σ_ )<sup>2</sup> = _|_ **b** _|_<sup>2</sup> _I_ For any vector **b** , the Pauli matrix product satisfies the identity: 



<!-- Start of picture text -->
( b  · σ ) 2 = ( b  ·  b ) I +  i ( b  ×  b )  · σ =  | b | 2 I<br><!-- End of picture text -->

If _λ_ is an eigenvalue of **b** _· σ_ , then: 



<!-- Start of picture text -->
λ 2 =  | b | 2 = ⇒ λ  =  ±| b |<br><!-- End of picture text -->

Notes 

2 

## **Method B: Characteristic Equation** 



<!-- Start of picture text -->
det( b  · σ − λI ) = 0<br><!-- End of picture text -->



<!-- Start of picture text -->
bz − λ bx − iby<br>x +  b 2 y ) = 0<br>���� bx  +  iby −bz − λ ���� = ( bz − λ )( −bz − λ )  − ( b 2<br>λ 2 − b 2 z − ( b 2 x +  b 2 y ) = 0 = ⇒ λ 2 =  b x 2 +  b 2 y +  b z 2 =  | b | 2<br><!-- End of picture text -->



<!-- Start of picture text -->
λ  =  ±| b |<br><!-- End of picture text -->

**3. Calculate Total Energy Eigenvalues of** _H_ Since _H_ = _a_ 0 _I_ + **b** _· σ_ , adding a multiple of the identity matrix _a_ 0 _I_ shifts every eigenvalue of **b** _· σ_ by + _a_ 0: 



<!-- Start of picture text -->
E± =  a 0  ± | b |<br><!-- End of picture text -->

- **Excited State Energy:** _E_ + = _a_ 0 + _|_ **b** _|_ 

- **Ground State Energy (Lower Eigenvalue): E** _−_ = **a0** _−|_ **b** _|_ 

## **Evaluation of Options** 

- **Option (a):** _b →_ **Incorrect** 

- **Option (b): a0** _−|_ **b** _| →_ **CORRECT!** 

- **Option (c):** _a_ 0 + _|_ **b** _| →_ **Incorrect** (This is the excited state energy) 

- **Option (d):** _a_ 0 _→_ **Incorrect** 

## **Key Concepts & Summary for GATE Physics** 

## **1. Pauli Matrix Algebraic Identities** 

- **Hermiticity & Unitarity:** _σi_<sup>_†_=</sup><sup>_σi_and</sup><sup>_σ_</sup> _i_<sup>2=</sup><sup>_I_.</sup> 

- **Trace & Determinant:** Tr( _σi_ ) = 0 and det( _σi_ ) = _−_ 1. 

- **Fundamental Product Identity:** 



<!-- Start of picture text -->
( a  · σ )( b  · σ ) = ( a  ·  b ) I +  i ( a  ×  b )  · σ<br><!-- End of picture text -->

- **Commutator & Anti-commutator:** 



<!-- Start of picture text -->
[ σi, σj ] = 2 iϵijkσk, {σi, σj}  = 2 δijI<br><!-- End of picture text -->

Notes 

3 

**2. Physical Application: Spin-1/2 Particle in a Magnetic Field** This Hamiltonian _H_ = _a_ 0 _I_ + **b** _· σ_ represents a spin-1/2 particle in an external magnetic field **B** (where **b** = _−µ ·_ **B** = _−γ_<sup>_<u>h</u>_¯</sup> 2<sup>**B**):</sup> 

   - The energy gap / splitting between ground and excited states is **∆E** = **E** + _−_ **E** _−_ = **2** _|_ **b** _|_ (Zeeman splitting). 

**Follow-up suggestion:** Would you like to practice calculating the **corresponding normalized ground-state eigenvector** for this Hamiltonian, or solve a problem on **timeevolution of spin states** using exp( _−iHt_ / _h_ ¯)? 

