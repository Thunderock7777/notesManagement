<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-definitions-of-the-two-operator.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

To see why the crystal Hamiltonian _H_<sup>ˆ</sup> commutes with the lattice translation operator _T_<sup>ˆ</sup> _a_ , we test their commutator [ _H,_<sup>ˆ</sup> _T_<sup>ˆ</sup> _a_ ] = _H_<sup>ˆ</sup> _T_<sup>ˆ</sup> _a−T_<sup>ˆ</sup> _aH_<sup>ˆ</sup> by acting on an arbitrary test wavefunction _ψ_ ( _x_ ). 

## **1. Definitions of the Two Operators** 

1. **Translation Operator (** _T_<sup>ˆ</sup> _a_ **):** Shifts any function of _x_ forward by one lattice constant _a_ : _T_ ˆ _aψ_ ( _x_ ) = _ψ_ ( _x_ + _a_ ) 

2. **1D Crystal Hamiltonian (** _H_<sup>ˆ</sup> **):** Sum of kinetic and potential energy operators: 



<!-- Start of picture text -->
H ˆ =  − h ¯2 d 2<br>2 m dx 2 +  V  ( x )<br><!-- End of picture text -->

## **2. Step-by-Step Proof** 

**Step A: Evaluate** _H_<sup>ˆ</sup> ( _T_ ˆ _aψ_ ( _x_ )) First, apply _T_<sup>ˆ</sup> _a_ to _ψ_ ( _x_ ), then act with _H_<sup>ˆ</sup> on the result: _T_ ˆ _aψ_ ( _x_ ) = _ψ_ ( _x_ + _a_ ) 



<!-- Start of picture text -->
d 2<br>H ˆ =  − h ¯2<br>ψ ( x  +  a )<br>[ ] 2 m dx 2 ψ ( x  +  a ) +  V ( x ) ψ ( x  +  a )<br><!-- End of picture text -->

_(Notice that V_ ( _x_ ) _is evaluated at x because H_<sup>ˆ</sup> _acts on the shifted wavefunction at position x.)_ 

**Step B: Evaluate** _T_<sup>ˆ</sup> _a_ ( _Hψ_ ˆ ( _x_ )) First, act with _H_<sup>ˆ</sup> on _ψ_ ( _x_ ), then apply _T_<sup>ˆ</sup> _a_ to shift every _x_ in the entire expression to ( _x_ + _a_ ): 



<!-- Start of picture text -->
Hψ ˆ ( x ) =  − h ¯2 d 2 ψ ( x ) +  V  ( x ) ψ ( x )<br>2 m dx 2<br><!-- End of picture text -->

Notes 

2 



<!-- Start of picture text -->
T ˆ a Hψ ˆ ( x ) =  − h ¯2 d 2 ψ ( x  +  a ) +  V ( x  +  a ) ψ ( x  +  a )<br>[ ] 2 m dx 2<br><!-- End of picture text -->

**Step C: Compute the Commutator** [ _H,_<sup>ˆ</sup> _T_<sup>ˆ</sup> _a_ ] _ψ_ ( _x_ ) Subtract Step B from Step A: 



<!-- Start of picture text -->
− h ¯2 d 2 ψ ( x  +  a ) − − h ¯2 d 2 ψ ( x  +  a )<br>(  H ˆ T ˆ a−T ˆ aH ˆ ) ψ ( x ) = +  V  ( x ) ψ ( x  +  a ) +  V  ( x  +  a ) ψ ( x  +  a )<br>2 m dx 2 2 m dx 2<br>[ ] [ ]<br><!-- End of picture text -->

The kinetic energy derivative terms cancel out completely: 



<!-- Start of picture text -->
[  H, ˆ T ˆ a ] ψ ( x ) = V ( x )  − V ( x  +  a ) ψ ( x  +  a )<br>[ ]<br><!-- End of picture text -->

## **3. The Role of Lattice Periodicity** 

Because the crystal lattice is strictly periodic ( _V_ ( _x_ + _a_ ) = _V_ ( _x_ )), the potential term difference is identically zero: 



<!-- Start of picture text -->
V  ( x )  − V  ( x  +  a ) = 0<br><!-- End of picture text -->

Therefore: 



<!-- Start of picture text -->
[  H, ˆ T ˆ a ] ψ ( x ) = 0 = ⇒ [ H ^ , T ^ a ] =  0<br><!-- End of picture text -->

## **Physical Meaning** 

1. **Kinetic Energy** depends only on spatial derivatives ( _dx_<sup>_<u>d</u>_22),whichmeasurelocal</sup> wave curvature. Shifting space by a constant _a_ doesn’t alter derivatives, so the kinetic energy operator _always_ commutes with translation. 

2. **Potential Energy** _V_ ( _x_ ) depends explicitly on position _x_ . Translating through space only leaves the potential energy operator unchanged if the atomic potential landscape at _x_ + _a_ is **100% identical** to _x_ . 

Because the Hamiltonian commutes with _T_<sup>ˆ</sup> _a_ , quantum mechanics guarantees that energy stationary states can be chosen as **simultaneous eigenfunctions of** _T_<sup>ˆ</sup> _a_ , directly giving birth to **Bloch’s Theorem** ( _ψ_ ( _x_ + _a_ ) = _e_<sup>_ika_</sup> _ψ_ ( _x_ )). 

_Would you like to move on to_ **_Module 5: Dielectrics, Magnetism & Superconductivity_** _to complete the solid-state syllabus?_ 

