<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-truncated-half-harmonic-oscillator.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**Correct Answer** 

**Option (d):** **<u>72</u>**<sup>**h**¯</sup><sup>_ω_</sup> 

## **Detailed Step-by-Step Solution** 

**1. Understand the Truncated (Half) Harmonic Oscillator Potential** A truncated or half harmonic oscillator potential is defined as: 



<!-- Start of picture text -->
12 mω 2 x 2 for x >  0<br>V  ( x ) =<br>∞ for x ≤ 0<br>{<br><!-- End of picture text -->

Because _V_ ( _x_ ) = _∞_ for _x ≤_ 0, the particle cannot penetrate into the negative region. This imposes a strict **hard-wall boundary condition** at _x_ = 0: 

_ψ_ (0) = 0 

**2. Relate to the Full Harmonic Oscillator** For a standard full harmonic oscillator ( _−∞ < x < ∞_ ), the energy eigenvalues are: 



<!-- Start of picture text -->
En = n  + 1 hω ¯ where n  = 0 ,  1 ,  2 ,  3 , . . .<br>2<br>( )<br><!-- End of picture text -->

The wavefunctions _ψn_ ( _x_ ) of the full oscillator have definite parity under spatial reflection ( _x →−x_ ): 

- **Even** _n_ **(** _n_ = 0 _,_ 2 _,_ 4 _, . . ._ **):** Wavefunctions have **EVEN parity** ( _ψn_ ( _−x_ ) = _ψn_ ( _x_ )). Crucially, _ψn_ (0) _̸_ = 0. 

- **Odd** _n_ **(** _n_ = 1 _,_ 3 _,_ 5 _, . . ._ **):** Wavefunctions have **ODD parity** ( _ψn_ ( _−x_ ) = _−ψn_ ( _x_ )). Crucially, _ψn_ (0) = 0. 

Notes 

2 

**3. Apply the Boundary Condition** _ψ_ (0) = 0 Since the wavefunction for the truncated potential must satisfy _ψ_ (0) = 0, **only the odd parity states of the full harmonic oscillator survive** . 

Thus, the allowed energy levels for the truncated oscillator correspond to **odd quantum numbers** _n_ = 1 _,_ 3 _,_ 5 _,_ 7 _, . . ._ of the full harmonic oscillator: 

- **Ground State (** _k_ = 0 **):** Corresponds to _n_ = 1: 



<!-- Start of picture text -->
E ground =  E 1 = 1 + 1 hω ¯ = 3<br>2 2 h ¯ ω<br>( )<br><!-- End of picture text -->

_(Parity of the underlying spatial state is odd)_ 

- **First Excited State (** _k_ = 1 **):** Corresponds to _n_ = 3: 



<!-- Start of picture text -->
E 1st excited =  E 3 = 3 + 1 hω ¯ = 7<br>2 2 h ¯ ω<br>( )<br><!-- End of picture text -->

_(Parity of the underlying spatial state is odd)_ 

- **Second Excited State (** _k_ = 2 **):** Corresponds to _n_ = 5: 



<!-- Start of picture text -->
E 2nd excited =  E 5 = 5 + 1 hω ¯ = 11<br>2 2 hω ¯<br>( )<br><!-- End of picture text -->

## **Evaluation of Options** 

- **Option (a):** “The parity of the first excited state is even” _→_ **Incorrect** (corresponds to _n_ = 3, which has odd parity). 

- **Option (b):** “The parity of the ground state is even” _→_ **Incorrect** (corresponds to _n_ = 1, which has odd parity). 

- **Option (c):** “The ground state energy is<sup><u>1</u></sup> 2<sup>_hω_¯”</sup><sup>_→_</sup><sup>**Incorrect**(ground state energy</sup> is<sup><u>3</u></sup> 2<sup>_hω_¯).</sup> 

- • **Option (d):** “The first excited state energy is<sup><u>7</u></sup> 2<sup>_hω_¯”</sup><sup>_→_</sup><sup>**CORRECT!**</sup> 

## **Key Concepts & Formulae to Remember for GATE** 

## **1. Full vs. Half Harmonic Oscillator Comparison Table** 

||Full Harmonic Oscillator|Half/Truncated Oscillator|
|---|---|---|
|Property|(_−∞< x < ∞_)|(_x >_0)|
|**Potential** _V_(_x_)|1<br>2<sup>_mω_2</sup><sup>_x_2</sup>|1<br>2<sup>_mω_2</sup><sup>_x_2 for</sup> <sup>_x >_ 0;</sup> <sup>_∞_for</sup><br>_x ≤_0|



Notes 

3 

|Property|Full Harmonic Oscillator<br>(_−∞< x < ∞_)|Half/Truncated Oscillator<br>(_x >_0)|
|---|---|---|
|**Allowed States**|All _n_= 0_,_1_,_2_,_3_,_4_, . . ._|Odd _n_= 1_,_3_,_5_,_7_, . . ._ only|
|**Energy Formula**|_En_ =<br>(<br>_n_+ <sup>1</sup><br>2<br>)<br>¯_hω_|_Ek_ =<br>(<br>2_k_+ <sup>3</sup><br>2<br>)<br>¯_hω_<br>(_k_ =<br>0_,_1_,_2_, . . ._)|
|**Ground State Energy**|_E_0 = <sup>1</sup><br>2<sup>¯</sup><sup>_hω_</sup>|_E_0 = <sup>3</sup><br>2<sup>¯</sup><sup>_hω_</sup>|
|**Energy Level Spacing**|∆_E_ =¯_hω_|∆_E_ = 2¯_hω_|
|**Parity of States**|Alternates (Even, Odd, Even,<br>Odd…)|All allowed states are **Odd**<br>**Parity**|



**2. General Golden Rule for Infinite Barriers at** _x_ = 0 Whenever an infinite barrier _V_ = _∞_ is placed at _x_ = 0 across any symmetric 1D potential _V_ ( _−x_ ) = _V_ ( _x_ ): 

   1. The boundary condition _ψ_ (0) = 0 eliminates all even-parity solutions. 

   2. Only the odd-parity solutions of the full symmetric potential are physically allowed. 

   3. The ground state energy of the truncated potential is equal to the **first excited state energy** of the full symmetric potential. 

## **3. Expectation Values for the Half Harmonic Oscillator** 

- **Position** _⟨x⟩_ **:** _⟨x⟩ >_ 0 (unlike the full oscillator where _⟨x⟩_ = 0 by symmetry). 

- **Momentum** _⟨p⟩_ **:** _⟨p⟩_ = 0 (holds true for any bound stationary state). 

- **Virial Theorem:** For any power-law potential _V_ ( _x_ ) _∝ x_<sup>_k_</sup> , here _k_ = 2, so: 

_⟨T ⟩_ = _⟨V ⟩_ =<sup>1</sup> 2<sup>_E_</sup> 

