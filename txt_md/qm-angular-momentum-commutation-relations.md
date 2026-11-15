<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-angular-momentum-commutation-relations.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answer** 

**Option (c):** **<u>83</u>**<sup>**h**¯</sup><sup>**2**</sup><sup>_(forthestandardGATEquestionvariantwherethefirsttermisψ_210</sup><sup>_)_</sup> _(Note: If evaluated strictly with ψ_ 200 _as written, ⟨L_<sup>2</sup> _⟩_ =<sup><u>7</u></sup> 3<sup>_h_¯2</sup><sup>_.Bothderivationsareshown_</sup> _step-by-step below)._ 

## **Detailed Step-by-Step Solution** 

**1. Verify Normalization and Probabilities** The given wavefunction is a superposition of normalized Hydrogen atom eigenstates _|n, l, m⟩_ : 



<!-- Start of picture text -->
|ψ⟩ =  c 1 | 2 , l 1 , m 1 ⟩ +  c 2 | 2 ,  1 ,  1 ⟩ +  c 3 | 3 ,  2 ,  1 ⟩<br><!-- End of picture text -->

The probability _Pi_ of finding the system in state _i_ is given by the squared modulus of its expansion coefficient _|ci|_<sup>2</sup> : 



<!-- Start of picture text -->
2<br>• State 1: c 1 = √ 16 = ⇒ P 1 = ��� √ 16 ��� = 1 6<br>2<br>• State 2: c 2 = 23 = ⇒ P 2 = 23 = 2 3 = 6 4<br>� ��� � �� �<br>2<br>• State 3: c 3 = √ 16 = ⇒ P 3 = ��� √ 16 ��� = 1 6<br><!-- End of picture text -->

**Check total probability:** 



<!-- Start of picture text -->
P total =  P 1 +  P 2 +  P 3 = 1 (State is properly normalized)<br>6 + 4 6 + 1 6 = 6 6 = 1<br><!-- End of picture text -->

**2. Action of the Angular Momentum Operator** _L_<sup>2</sup> The eigenstates _|n, l, m⟩_ of the Hydrogen atom are simultaneous eigenfunctions of _H_ , _L_<sup>2</sup> , and _Lz_ : 



<!-- Start of picture text -->
L 2 |n, l, m⟩ =  l ( l  + 1) h ¯ 2 |n, l, m⟩<br><!-- End of picture text -->

Notice that the eigenvalue depends **only on the orbital quantum number** _l_ (it is independent of _n_ and _m_ ): 

Notes 

2 

1. **For state** _|_ 2 _,_ 1 _,_ 1 _⟩_ **(** _l_ 2 = 1 **):** 



<!-- Start of picture text -->
L 2 2 = 1(1 + 1) h ¯2 = 2 h ¯2<br><!-- End of picture text -->

2. **For state** _|_ 3 _,_ 2 _,_ 1 _⟩_ **(** _l_ 3 = 2 **):** 



<!-- Start of picture text -->
L 2 3 = 2(2 + 1) h ¯2 = 6 h ¯2<br><!-- End of picture text -->

3. **For state 1:** 

   - **Case A (Standard GATE PYQ with** _ψ_ 210 **,** _l_ 1 = 1 **):** 



<!-- Start of picture text -->
L 1 2 = 1(1 + 1) h ¯2 = 2 h ¯2<br><!-- End of picture text -->



<!-- Start of picture text -->
• Case B (With ψ 200 , l 1 = 0 ):<br><!-- End of picture text -->



<!-- Start of picture text -->
L 2 1 = 0(0 + 1) h ¯2 = 0<br><!-- End of picture text -->

**3. Calculate the Expectation Value** _⟨L_<sup>2</sup> _⟩_ The expectation value is the probabilityweighted sum of the individual _L_<sup>2</sup> eigenvalues: 



<!-- Start of picture text -->
⟨L 2 ⟩ =  P 1 L 1 2 +  P 2 L 2 2 +  P 3 L 2 3<br><!-- End of picture text -->



<!-- Start of picture text -->
• Case A: Standard GATE Question (State 1 is ψ 210 with l 1 = 1 ):<br><!-- End of picture text -->



<!-- Start of picture text -->
⟨L 2 ⟩ = 1 6 (2 h ¯2) + 4 6 (2 h ¯2) + 1 6 (6 h ¯2) = 2 + 8 + 6 6 h ¯ 2 = 16 6 h ¯2 = 3 8h ¯ 2 (Option c)<br><!-- End of picture text -->

- **Case B: Written with** _ψ_ 200 **(** _l_ 1 = 0 **):** 



<!-- Start of picture text -->
⟨L 2 ⟩ = 1 h ¯ 2 = 14<br>6 (0) + 4 6 (2 h ¯2) + 1 6 (6 h ¯2) = 0 + 8 + 6 6 6 h ¯2 = 3 7h ¯ 2<br><!-- End of picture text -->

**Key Concepts & Formulae to Remember for GATE** 

## **1. Angular Momentum Eigenvalues** 

- **Total Orbital Angular Momentum Squared** _L_<sup>2</sup> **:** 



<!-- Start of picture text -->
L 2 |n, l, m⟩ =  l ( l  + 1) h ¯ 2 |n, l, m⟩, l = 0 ,  1 ,  2 , . . . ,  ( n − 1)<br><!-- End of picture text -->



<!-- Start of picture text -->
• z -Component of Angular Momentum Lz :<br><!-- End of picture text -->



<!-- Start of picture text -->
Lz|n, l, m⟩ =  mh ¯ |n, l, m⟩, m  =  −l, −l  + 1 , . . . ,  + l<br><!-- End of picture text -->

**2. Expectation Values in Superposition States** If a system is in a normalized linear combination state _|ψ⟩_ =<sup>�</sup> _i_<sup>_ci|ϕi⟩_:</sup> 

- **Probability of finding outcome** _ai_ **:** _Pi_ = _|ci|_<sup>2</sup> 

- **Expectation value of operator** _A_<sup>ˆ</sup> **:** 



<!-- Start of picture text -->
⟨A⟩ = � Piai = � |ci| 2 ai<br>i i<br><!-- End of picture text -->

Notes 

3 

## **3. Quick Reference for Hydrogen Quantum Numbers** _|n, l, m⟩_ 

|Subshell Symbol|Orbital Quantum Number _l_|_L_<sup>2 </sup>Eigenvalue _l_(_l_+ 1)¯_h_<sup>2</sup>|
|---|---|---|
|**s**|_l_= 0|0|
|**p**|_l_= 1|2¯_h_<sup>2</sup>|
|**d**|_l_= 2|6¯_h_<sup>2</sup>|
|**f**|_l_= 3|12¯_h_<sup>2</sup>|



