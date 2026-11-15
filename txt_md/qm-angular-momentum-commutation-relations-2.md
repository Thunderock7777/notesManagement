<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-angular-momentum-commutation-relations-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **1. What is “Small** _l_ **”? (Orbital Angular Momentum Quantum Number)** 

In classical physics, a rotating object has continuous angular momentum. In quantum mechanics, however, an electron orbiting an atomic nucleus cannot have just any value of angular momentum—its magnitude and direction are strictly quantized. 

- _l_ **(Small** _l_ **):** Known as the **orbital angular momentum quantum number** (or azimuthal quantum number). 

- **Magnitude of Angular Momentum:** The total length/magnitude of the angular momentum vector **L** is fixed by _l_ : 

      - _|_ **L** _|_ = ~~√~~ _l_ ( _l_ + 1) _h_ ¯ 

- **Allowed Values:** _l_ takes non-negative integer values: _l_ = 0 _,_ 1 _,_ 2 _,_ 3 _, . . ._ . In atomic spectroscopy, these correspond to subshells: 

   - _l_ = 0 _→ s_ -orbital 

   - _l_ = 1 _→ p_ -orbital 

   - _l_ = 2 _→ d_ -orbital 

**What does** _l_ = 1 **mean?** When _l_ = 1 (a _p_ -state): 

1. **Magnitude:** _|_ **L** _|_ = ~~√~~ 1(1 + 1) _h_ ¯ = _~~√~~_ 2 _h_ ¯ _≈_ 1 _._ 414 _h_ ¯. 2. **Space Quantization (** _ml_ **or** _m_ **):** The projection of angular momentum along a chosen axis (the _z_ -axis, _Lz_ ) is given by: 



<!-- Start of picture text -->
Lz =  mh ¯<br><!-- End of picture text -->

where _m_ takes 2 _l_ + 1 possible integer values ranging from _−l_ to + _l_ : 



<!-- Start of picture text -->
m ∈{ +1 , 0 , − 1 }<br><!-- End of picture text -->

So for _l_ = 1, there are **3 distinct sub-states** corresponding to _m_ = +1, _m_ = 0, and _m_ = _−_ 1. 

## **2. What are “Vectors” and “Kets” (** _|l, m⟩_ **) in Quantum Mechanics?** 

In quantum mechanics (specifically Dirac notation and Heisenberg’s matrix mechanics), physical states are represented as **vectors in a state space** . 

Notes 

2 

**A. The Ket Notation** _|l, m⟩_ Instead of writing a complex spatial differential function, we represent a state by a bracket symbol called a **ket** : _|l, m⟩_ . 

- Inside _|l, m⟩_ , the first number is _l_ and the second is _m_ . 

- For _l_ = 1, our system has 3 basis states: 

   1. _|_ 1 _,_ +1 _⟩_ **:** State with _Lz_ = +1 _h_ ¯ 

   2. _|_ 1 _,_ 0 _⟩_ **:** State with _Lz_ = 0 _h_ ¯ 

   3. _|_ 1 _, −_ 1 _⟩_ **:** State with _Lz_ = _−_ 1 _h_ ¯ 



<!-- Start of picture text -->
B. Writing Kets as Column Vectors Just like a 3D physical vector  v  can be written<br>x<br> <br>as a column of 3 numbers y<br>z<br> , our 3 quantum states for  l = 1 are written as  3D column<br><!-- End of picture text -->

**vectors** . 

By convention, we order the rows by **descending value of** _m_ (top row is _m_ = +1, middle is _m_ = 0, bottom is _m_ = _−_ 1): 



<!-- Start of picture text -->
| 1 ,  +1 ⟩ = 10 | 1 ,  0 ⟩ = 01 | 1 , − 1 ⟩ = 00<br>0 0 1<br>  ,   ,  <br><!-- End of picture text -->

**C. Writing Bras as Row Vectors** A **bra** _⟨l, m|_ is the conjugate transpose (row vector) of a ket: 



<!-- Start of picture text -->
⟨ 1 ,  +1 |  = (1 0 0) , ⟨ 1 ,  0 |  = (0 1 0) , ⟨ 1 , − 1 |  = (0 0 1)<br><!-- End of picture text -->

## **3. What is Matrix Representation & How Do We Build It?** 

Physical observables (like operators _Lz_ or _L_ +) act on these column vectors to transform them. In a 3-dimensional basis (like _l_ = 1), operators are represented by 3 _×_ 3 **square matrices** . 

**A. Constructing the** _Lz_ **Matrix** Since _Lz|_ 1 _, m⟩_ = _mh_ ¯ _|_ 1 _, m⟩_ : 



<!-- Start of picture text -->
1 1 + h ¯<br>• Acting on | 1 ,  +1 ⟩ : Lz 0 0 0<br>0 0 0<br>  = (+1 h ¯)   =  <br>• Acting on | 1 ,  0 ⟩ : Lz 01 01 00<br>0 0 0<br>  = (0 h ¯)   =  <br>0 0  0 <br>• Acting on | 1 , − 1 ⟩ : Lz 0 0 0<br>1 1 −h ¯<br>  = ( − 1 h ¯)   =  <br><!-- End of picture text -->

Putting these 3 column outputs together side by side gives the matrix: 



<!-- Start of picture text -->
1 0 0 <br>Lz = ¯ h 0 0 0<br>0 0 − 1<br> <br><!-- End of picture text -->

Notes 

3 

**B. Constructing the Ladder Operator** _L_ + **Matrix** The raising operator _L_ + = _Lx_ + _iLy_ raises the quantum number _m_ by +1: 



<!-- Start of picture text -->
L + |l, m⟩ = ¯ h √ l ( l  + 1)  − m ( m  + 1)  |l, m  + 1 ⟩<br><!-- End of picture text -->

Let’s test what _L_ + does to each of our 3 basis vectors for _l_ = 1: 

1. **Acting on** _|_ 1 _, −_ 1 _⟩_ **(bottom state,** _m_ = _−_ 1 **):** 



<!-- Start of picture text -->
L + | 1 , − 1 ⟩ = ¯ h √ 1(2)  − ( − 1)(0)  | 1 ,  0 ⟩ = √ 2h ¯ | 1 ,  0 ⟩<br><!-- End of picture text -->

In column vector form: 



<!-- Start of picture text -->
L + 00 √ 2 h ¯ 01  √ 02 h ¯<br>1 0 0<br>  =   =  <br><!-- End of picture text -->

2. **Acting on** _|_ 1 _,_ 0 _⟩_ **(middle state,** _m_ = 0 **):** 



<!-- Start of picture text -->
L + | 1 ,  0 ⟩ = ¯ h √ 1(2)  − 0(1)  | 1 ,  +1 ⟩ = √ 2h ¯ | 1 ,  + 1 ⟩<br><!-- End of picture text -->

In column vector form: 



<!-- Start of picture text -->
L + 01 √ 2 h ¯ 10  √ 02 h ¯<br>0 0 0<br>  =   =  <br><!-- End of picture text -->

3. **Acting on** _|_ 1 _,_ +1 _⟩_ **(top state,** _m_ = +1 **):** 



<!-- Start of picture text -->
L + | 1 ,  +1 ⟩ = ¯ h √ 1(2)  − 1(2)  | 1 ,  +2 ⟩ =  0<br><!-- End of picture text -->

_(You cannot raise beyond the maximum state m_ = + _l)_ . 

Assembling these 3 outputs into the columns of a 3 _×_ 3 matrix gives: 



<!-- Start of picture text -->
0 √ 2 0 <br>L + = ¯ h 0 0 √ 2<br>0 0 0<br> <br><!-- End of picture text -->

**C. How the Matrix Multiplication Solves Question Q.50** The problem asked for the matrix element _⟨_ 1 _,_ 0 _|_ ( _Lx_ + _iLy_ ) _|_ 1 _, −_ 1 _⟩_ , which is _⟨_ 1 _,_ 0 _|L_ + _|_ 1 _, −_ 1 _⟩_ : 

1. **Step 1:** Act with matrix _L_ + on column vector _|_ 1 _, −_ 1 _⟩_ : 



<!-- Start of picture text -->
0 √ 2 0  0  0 <br>L + | 1 , − 1 ⟩ = ¯ h 0 0 √ 2 0 √ 2 h ¯<br>0 0 0 1 0<br>    =  <br><!-- End of picture text -->

Notes 

4 



<!-- Start of picture text -->
2. Step 2: Multiply by row vector ⟨ 1 ,  0 |  = (0 1 0) on the left:<br><!-- End of picture text -->



<!-- Start of picture text -->
⟨ 1 ,  0 |L + | 1 , − 1 ⟩ = (0 1 0)  √ 02 h ¯ √ 2 h ¯) + (0  ·  0) = √ 2h ¯<br>0<br>  = (0  ·  0) + (1  ·<br><!-- End of picture text -->

**Does this step-by-step breakdown make the concept of quantum basis vectors and matrices clear? Feel free to ask about any specific step!** 

