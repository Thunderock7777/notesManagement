<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-perturbation-theory-energy-correction-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**Correct Answer** 

**Option (c): 0** _, ϵ_ 

**Detailed Step-by-Step Solution** 

**1. Identify the Degenerate Subspace** From **Q.50** , the unperturbed Hamiltonian is: 



<!-- Start of picture text -->
H 0 = 10 02 00<br>0 0 2<br> <br><!-- End of picture text -->



<!-- Start of picture text -->
1<br>• The ground state E 1 (0) = 1 is non-degenerate (basis vector | 1 ⟩ = 0<br>0<br> ).<br><!-- End of picture text -->

- The excited level _E_<sup>(0)</sup> = 2 is **2-fold degenerate** , spanned by the states: 



<!-- Start of picture text -->
| 2 ⟩ = 01 and | 3 ⟩ = 00<br>0 1<br>   <br><!-- End of picture text -->

**2. Construct the Perturbation Matrix (** _W_ **-Matrix)** Because the excited state level is 2-fold degenerate, first-order perturbation theory requires constructing the 2 _×_ 2 matrix _W_ in the degenerate subspace spanned by _{|_ 2 _⟩, |_ 3 _⟩}_ : 



<!-- Start of picture text -->
⟨ 2 |H ′ | 3 ⟩<br>W =<br>� ⟨⟨ 32 ||HH ′ ′|| 22 ⟩⟩ ⟨ 3 |H ′ | 3 ⟩ �<br><!-- End of picture text -->

Given the perturbation matrix _H_<sup>_′_</sup> : 



<!-- Start of picture text -->
H ′ =  ϵ 01 10 00<br>0 0 1<br> <br><!-- End of picture text -->

Selecting rows **2 and 3** and columns **2 and 3** (the bottom-right 2 _×_ 2 block) gives: 



<!-- Start of picture text -->
0<br>W =  ϵ<br>0 1<br>�0 �<br><!-- End of picture text -->

Notes 

2 

**3. Calculate the Eigenvalues of** _W_ **(First-Order Corrections)** The first-order energy corrections _E_<sup>(1)</sup> to the degenerate excited level are the eigenvalues of _W_ , found by solving the secular equation: 

Yielding two roots: 



<!-- Start of picture text -->
det� W − E (1) I � = 0<br>0  − E (1) 0<br>0 ϵ − E (1)<br>���� ���� = 0<br>( −E (1) )( ϵ − E (1) ) = 0<br>E 2 (1) = 0 and E 3 (1) =  ϵ<br><!-- End of picture text -->

Thus, the first-order energy corrections to the degenerate excited level are 0 **and** _ϵ_ (Option c). 

_(The total perturbed energies for these excited states are therefore E_ 2 = 2 + 0 = 2 _and E_ 3 = 2 + _ϵ)._ 

## **Evaluation of Options** 

- **Option (a):** _ϵ, −ϵ →_ **Incorrect** 

- **Option (b):** _ϵ, ϵ →_ **Incorrect** 

- **Option (c): 0** _, ϵ →_ **CORRECT!** 

- **Option (d):** 0 _,_ 0 _→_ **Incorrect** 

## **Key Concepts & Formulae to Remember for GATE** 

**1. Quick Trace & Determinant Verification** For any diagonal perturbation matrix 0 

_W_ = _ϵ_ , the eigenvalues are directly the diagonal entries _aϵ_ and _bϵ_ : 0 _b_ 

� _a_ � 

   - Trace( _W_ ) = _E_ 2<sup>(1)</sup> + _E_ 3<sup>(1)</sup> = _ϵ_ 

   - • det( _W_ ) = _E_ 2<sup>(1)</sup> _· E_ 3<sup>(1)</sup> = 0 

**2. Summary of Full System Spectrum (Q.50 + Q.51)** 

|||||Total 1<sup>st</sup>-Order|
|---|---|---|---|---|
|State Level|Unperturbed<br>_E_<sup>(0)</sup>|Degeneracy|1<sup>st</sup>-Order<br>Correction _E_<sup>(1)</sup>|Energy<br>(_E_<sup>(0) </sup>+_E_<sup>(1)</sup>)|
|**Ground State**|1|Non-degenerate|0|1|



Notes 

3 

|State Level|Unperturbed<br>_E_<sup>(0)</sup>|Degeneracy|1<sup>st</sup>-Order<br>Correction _E_<sup>(1)</sup>|Total 1<sup>st</sup>-Order<br>Energy<br>(_E_<sup>(0) </sup>+_E_<sup>(1)</sup>)|
|---|---|---|---|---|
|**Excited State**|2|Degenerate|0|2|
|**1**|||||
|**Excited State**<br>**2**|2|Degenerate|_ϵ_|2 +_ϵ_|



**Next Step:** Would you like to tackle another quantum mechanics GATE problem (such as Variational Method or WKB Approximation)? 

