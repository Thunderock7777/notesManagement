<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-ladder-operators-harmonic-oscillator-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**Correct Answer Option (b):** _~~√~~_ **2h** ¯ 

## **Detailed Step-by-Step Solution** 

**1. Identify the Ladder Operator** The given operator is the **angular momentum raising operator** _L_ +: 



<!-- Start of picture text -->
L + =  Lx  +  iLy<br><!-- End of picture text -->

We need to calculate the matrix element: 



<!-- Start of picture text -->
⟨ 1 ,  0 |L + | 1 , − 1 ⟩<br><!-- End of picture text -->

**2. Apply the Ladder Operator Formula** The general action of the raising operator _L_ + on an angular momentum eigenstate _|l, m⟩_ is given by: 



<!-- Start of picture text -->
L + |l, m⟩ = ¯ h √ l ( l  + 1)  − m ( m  + 1)  |l, m  + 1 ⟩<br><!-- End of picture text -->

Alternatively, expressed using factors: 

_L_ + _|l, m⟩_ = ¯ _h_ ~~√~~ ( _l − m_ )( _l_ + _m_ + 1) _|l, m_ + 1 _⟩_ 

**3. Calculate** _L_ + _|_ 1 _, −_ 1 _⟩_ Substitute _l_ = 1 and _m_ = _−_ 1 into the raising operator formula: 



<!-- Start of picture text -->
L + | 1 , − 1 ⟩ = ¯ h √ 1(1 + 1)  − ( − 1)( − 1 + 1)  | 1 , − 1 + 1 ⟩<br><!-- End of picture text -->



<!-- Start of picture text -->
= ¯ h √ 2  − 0  | 1 ,  0 ⟩ = √ 2h ¯ | 1 ,  0 ⟩<br><!-- End of picture text -->

Notes 

2 

**4. Take the Inner Product** Substitute _L_ + _|_ 1 _, −_ 1 _⟩_ = _~~√~~_ 2 _h_ ¯ _|_ 1 _,_ 0 _⟩_ back into the matrix element: 



<!-- Start of picture text -->
⟨ 1 ,  0 |L + | 1 , − 1 ⟩ =  ⟨ 1 ,  0 | 2 h ¯ | 1 ,  0 ⟩<br>( √ )<br><!-- End of picture text -->

Since _~~√~~_ 2 _h_ ¯ is a constant scalar, pull it out of the bra-ket: 



<!-- Start of picture text -->
= √ 2 h ¯  ⟨ 1 ,  0 | 1 ,  0 ⟩<br><!-- End of picture text -->

= Since angular momentum eigenstates are orthonormal ( _⟨l_<sup>_′_</sup> _, m_<sup>_′_</sup> _|l, m⟩ δl,l′δm,m′_ ), _⟨_ 1 _,_ 0 _|_ 1 _,_ 0 _⟩_ = 1: 



<!-- Start of picture text -->
⟨ 1 ,  0 | L + | 1 , − 1 ⟩ = √ 2h ¯<br><!-- End of picture text -->

**Alternative Method: Matrix Representation for** _l_ = 1 

Using the standard basis states for _l_ = 1 ordered as _{|_ 1 _,_ 1 _⟩, |_ 1 _,_ 0 _⟩, |_ 1 _, −_ 1 _⟩}_ : 

1. **State Vector Representations:** 



<!-- Start of picture text -->
| 1 ,  1 ⟩ = 10 | 1 ,  0 ⟩ = 01 | 1 , − 1 ⟩ = 00<br>0 0 1<br>  ,   ,  <br><!-- End of picture text -->

2. **Matrix Form of** _L_ + **for** _l_ = 1 **:** 



<!-- Start of picture text -->
0 √ 2 0 <br>L + = ¯ h 0 0 √ 2<br>0 0 0<br> <br><!-- End of picture text -->

3. **Matrix Multiplication:** 



<!-- Start of picture text -->
0 √ 2 0  0  0 <br>L + | 1 , − 1 ⟩ = ¯ h 0 0 √ 2 0 √ 2 √ 2 h ¯ | 1 ,  0 ⟩<br>0 0 0 1 0<br>    = ¯ h   =<br><!-- End of picture text -->

4. **Compute** _⟨_ 1 _,_ 0 _|L_ + _|_ 1 _, −_ 1 _⟩_ **:** 



<!-- Start of picture text -->
(0 1 0)   √ 02 √ 2h ¯<br>0<br> h ¯    =<br><!-- End of picture text -->

Notes 

3 

## **Evaluation of Options** 

- **Option (a):** _h_ ¯ _→_ **Incorrect** 

- • **Option (b):** _~~√~~_ **2h** ¯ _→_ **CORRECT!** 

- **Option (c):** 2 _h_ ¯ _→_ **Incorrect** 

- **Option (d):** 0 _→_ **Incorrect** 

## **Key Concepts & Formulae to Remember for GATE Physics** 

**1. Angular Momentum Ladder Operators** 

   - **Definitions:** 



<!-- Start of picture text -->
L + =  Lx  +  iLy, L− =  Lx − iLy<br><!-- End of picture text -->

- **Action on Basis States:** 



<!-- Start of picture text -->
L±|l, m⟩ = ¯ h √ l ( l  + 1)  − m ( m ±  1)  |l, m ±  1 ⟩<br><!-- End of picture text -->

- **Adjoint Property:** 



<!-- Start of picture text -->
( L +) † =  L−, ( L− ) † =  L +<br>Lyy :<br>Lx = L + +  L− , Ly = L +  − L−<br>2 2 i<br><!-- End of picture text -->

   - **Reconstructing** _Lx_ **and** _Lyy_ **:** 

**2. Commutation Relations for Ladder Operators** 

   - [ _Lz, L_ +] = + _hL_ ¯ + 

   - [ _Lz, L−_ ] = _−hL_ ¯ _−_ 

   - [ _L_ + _, L−_ ] = 2 _hL_ ¯ _z_ 

   - • [ _L_<sup>2</sup> _, L±_ ] = 0 

**3. Matrix Representations for** _l_ = 1 **(Basis:** _|_ 1 _,_ 1 _⟩, |_ 1 _,_ 0 _⟩, |_ 1 _, −_ 1 _⟩_ **)** 



<!-- Start of picture text -->
Lx = h ¯ 01 10 01 Ly = h ¯ 0 i − 0 i − 0 i  Lz = ¯ h 10 00 00 <br>√ 2 √ 2<br>0 1 0 0 i 0 0 0 − 1<br>  ,   ,  <br>L + = ¯ h 00 √ 02 √ 02 L− = ¯ h  √ 02 00 00<br>0 0 0  ,  0 √ 2 0<br><!-- End of picture text -->

**Summary Table: Matrix Elements of** _L_ + **and** _L−_ **for** _l_ = 1 

Notes 

4 

|Matrix Element|Operator Expression|Value|
|---|---|---|
|_⟨_1_,_1_∥L_+_∥_1_,_0_⟩_|¯_h_<br>~~√~~<br>1(2)_−_0(1)|_~~√~~_<br>2¯_h_|
|_⟨_1_,_0_∥L_+_∥_1_, −_1_⟩_|¯_h_<br>~~√~~<br>1(2)_−_(_−_1)(0)|_~~√~~_<br>2¯_h_|
|_⟨_1_,_0_∥L−∥_1_,_1_⟩_|¯_h_<br>~~√~~<br>1(2)_−_1(0)|_~~√~~_<br>2¯_h_|
|_⟨_1_, −_1_∥L−∥_1_,_0_⟩_|¯_h_<br>~~√~~<br>1(2)_−_0(_−_1)|_~~√~~_<br>2¯_h_|
|_⟨_1_,_1_∥L_+_∥_1_,_1_⟩_|Exceeds maximum _m_= 1|0|



**Follow-up suggestion:** Would you like to practice calculating matrix elements for _L_<sup>2</sup> _x_ **or** _L_<sup>2</sup> _y_<sup>inthe</sup><sup>_|l, m⟩_basis,ortacklea</sup><sup>**spin-1Clebsch-Gordanaddition**problemnext?</sup> 

