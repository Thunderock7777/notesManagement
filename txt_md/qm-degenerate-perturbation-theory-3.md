<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-degenerate-perturbation-theory-3.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answer** 

**Option (b): 1** + **2** _δ,_ **1** 

## **Step-by-Step Solution** 

**Method 1: Degenerate Perturbation Theory** 

1. **Identify the Unperturbed Eigenvalues:** The unperturbed Hamiltonian is: 



<!-- Start of picture text -->
0<br>H 0 =<br>0 1<br>�1 �<br><!-- End of picture text -->

The eigenvalues of _H_ 0 are obtained from det� _H_ 0 _− E_<sup>(0)</sup> _I_ � = 0: (1 _− E_<sup>(0)</sup> )<sup>2</sup> = 0 = _⇒ E_ 1<sup>(0)</sup> = 1 _, E_ 2<sup>(0)</sup> = 1 

Since both eigenvalues are equal ( _E_ 1<sup>(0)</sup> = _E_ 2<sup>(0)</sup> = 1), the 2-state system is **2-fold degenerate** . 

2. **Set up the Perturbation Matrix (** _W_ **-matrix):** In the degenerate subspace, the first-order energy corrections _E_<sup>(1)</sup> are the eigenvalues of the perturbation matrix _W_ = _H_<sup>_′_</sup> : 



<!-- Start of picture text -->
δ<br>W =  H ′ =<br>δ δ<br>� δ �<br><!-- End of picture text -->

3. **Find the First-Order Energy Corrections (** _E_<sup>(1)</sup> **):** Solve the secular equation det� _W − E_<sup>(1)</sup> _I_ � = 0: 



<!-- Start of picture text -->
δ − E (1) δ<br>δ δ − E (1)<br>���� ���� = 0<br>( δ − E (1) ) 2 − δ 2 = 0<br><!-- End of picture text -->



<!-- Start of picture text -->
δ − E (1) =  ±δ<br><!-- End of picture text -->

- Taking the plus sign: _E_ 1<sup>(1)</sup> = _δ_ + _δ_ = **2** _δ_ 

- • Taking the minus sign: _E_ 2<sup>(1)</sup> = _δ − δ_ = **0** 

Notes 

2 

4. **Calculate First-Order Perturbed Energies (** _E_ = _E_<sup>(0)</sup> + _E_<sup>(1)</sup> **):** 



<!-- Start of picture text -->
E 1 =  E 1 (0) +  E 1 (1) = 1 + 2 δ<br>E 2 =  E 2 (0) +  E 2 (1) = 1 + 0 = 1<br><!-- End of picture text -->

Thus, the first-order perturbed energy eigenvalues are 1 + 2 _δ_ **and** 1. 

**Method 2: Exact Diagonalization (Shortcut)** Since _H_ 0 and _H_<sup>_′_</sup> are simple 2 _×_ 2 matrices, we can write the total Hamiltonian _H_ = _H_ 0 + _H_<sup>_′_</sup> explicitly: 



<!-- Start of picture text -->
0 δ δ<br>H = + =<br>0 1 δ δ δ 1 +  δ<br>�1 � � δ � �1 +  δ �<br><!-- End of picture text -->

Now, find the exact eigenvalues of _H_ using the trace and determinant properties of a 2 _×_ 2 matrix: 

- **Trace:** Tr( _H_ ) = _E_ 1 + _E_ 2 = (1 + _δ_ ) + (1 + _δ_ ) = 2 + 2 _δ_ 

- **Determinant:** det( _H_ ) = _E_ 1 _· E_ 2 = (1 + _δ_ )<sup>2</sup> _− δ_<sup>2</sup> = 1 + 2 _δ_ 

Solving _E_ 1 + _E_ 2 = 2 + 2 _δ_ and _E_ 1 _E_ 2 = 1 + 2 _δ_ yields: 



<!-- Start of picture text -->
E 1 = 1 + 2 δ, E 2 = 1<br><!-- End of picture text -->

## **Key Concepts & Formulas to Remember for GATE** 

**1. Why Standard Non-Degenerate Perturbation Theory Fails** In nondegenerate perturbation theory, the second-order energy correction is given by: 



<!-- Start of picture text -->
|⟨ψm (0) |H ′|ψ n (0) ⟩| 2<br>E (2) =<br>n �<br>m̸ = n En (0) − E m (0)<br><!-- End of picture text -->

If _En_<sup>(0)</sup> = _Em_<sup>(0)</sup> (degeneracy), the denominator vanishes ( _En_<sup>(0)</sup> _− Em_<sup>(0)</sup> = 0), causing the expression to explode to infinity. Therefore, **degenerate perturbation theory must be used** . 

## **2. Recipe for Degenerate Perturbation Theory** 

1. **Identify the Degenerate Subspace:** Group all states that share the same unperturbed energy _E_<sup>(0)</sup> . 

2. **Construct the** _W_ **-matrix:** Build the matrix elements of _H_<sup>_′_</sup> within the degenerate subspace: 

   - _Wij_ = _⟨ψi_<sup>(0)</sup><sup>_|H′|ψ_</sup> _j_<sup>(0)</sup><sup>_⟩_</sup> 

3. **Diagonalize** _W_ **:** Solve det� _W − E_<sup>(1)</sup> _I_ � = 0 to get the first-order corrections _E_<sup>(1)</sup> . 4. **Total First-Order Energy:** _Ei_ = _E_<sup>(0)</sup> + _Ei_<sup>(1).</sup> 

Notes 

3 

**3. Useful** 2 _×_ 2 **Matrix Tricks for GATE** For a 2 _×_ 2 perturbation matrix _W_ = _b_ : 

_c d_ 

� _a_ � 

1. **Trace Trick:** 



<!-- Start of picture text -->
E 1 (1) +  E 2 (1) = Tr( W ) =  a  +  d<br><!-- End of picture text -->

2. **Determinant Trick:** 



<!-- Start of picture text -->
E 1 (1) · E 2 (1) = det( W ) =  ad − bc<br><!-- End of picture text -->

3. **Eigenvalues Formula:** 



<!-- Start of picture text -->
E (1) = Tr( W )  ± � [Tr( W )] 2 − 4 det( W )<br>2<br><!-- End of picture text -->

_δ_ Applied directly to _W_ = : _δ δ_ � _δ_ � • Tr( _W_ ) = 2 _δ_ • det( _W_ ) = _δ_<sup>2</sup> _− δ_<sup>2</sup> = 0 • _E_<sup>(1)</sup> =<sup><u>2</u></sup><sup>_<u>δ±</u>_</sup> _~~<u>√</u>~~_ 24 _<u>δ</u>_<sup>2</sup> _−_ <u>0</u> =<sup><u>2</u></sup><sup>_<u>δ±</u>_</sup> 2<sup><u>2</u></sup><sup>_<u>δ</u>_</sup> = _⇒_ 2 _δ,_ 0 

