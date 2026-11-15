<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-ladder-operators-harmonic-oscillator.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**Correct Answer** 

**Option (a):** _n_ ( _n −_ 1) 

## **Detailed Step-by-Step Solution** 

**Method 1: Step-by-Step Action of Ladder Operators** Recall the fundamental actions of the annihilation operator ( _a_ ) and creation operator ( _a_<sup>_†_</sup> ) on an energy eigenstate _|n⟩_ : 



<!-- Start of picture text -->
a|n⟩ = √ n |n − 1 ⟩<br>a † |n⟩ = √ n  + 1  |n  + 1 ⟩<br><!-- End of picture text -->

Applying the operator sequence _O_<sup>ˆ</sup> = _a_<sup>_†_</sup> _a_<sup>_†_</sup> _aa_ from right to left on state _|n⟩_ : 

1. **First annihilation operator (** _a_ **):** 



<!-- Start of picture text -->
a|n⟩ = √ n|n − 1 ⟩<br><!-- End of picture text -->

2. **Second annihilation operator (** _a_ **):** 



<!-- Start of picture text -->
a ( √ n|n − 1 ⟩ ) = √ n √ n − 1 |n − 2 ⟩ = √ n ( n − 1) |n − 2 ⟩<br><!-- End of picture text -->

3. **First creation operator (** _a_<sup>_†_</sup> **):** 



<!-- Start of picture text -->
=<br>a †  ( √ n ( n − 1) |n − 2 ⟩ ) √ n ( n − 1) √ ( n − 2) + 1 |n− 1 ⟩ = √ n ( n − 1) √ n − 1 |n− 1 ⟩<br><!-- End of picture text -->

4. **Second creation operator (** _a_<sup>_†_</sup> **):** 



<!-- Start of picture text -->
a †  ( √ n ( n − 1) √ n − 1 |n − 1 ⟩ ) = √ n ( n − 1) √ n − 1 √ ( n − 1) + 1 |n⟩ =  n ( n − 1) |n⟩<br><!-- End of picture text -->

Thus: 



<!-- Start of picture text -->
a † a † aa|n⟩ =  n ( n  − 1 ) | n ⟩<br><!-- End of picture text -->

Notes 

2 

**Method 2: Using the Number Operator Identity (Algebraic Method)** Define the number operator _N_<sup>ˆ</sup> = _a_<sup>_†_</sup> _a_ , which satisfies _N_<sup>ˆ</sup> _|n⟩_ = _n|n⟩_ . 

Using the fundamental commutator relation [ _a, a_<sup>_†_</sup> ] = _aa_<sup>_†_</sup> _− a_<sup>_†_</sup> _a_ = 1 = _⇒ aa_<sup>_†_</sup> = _a_<sup>_†_</sup> _a_ + 1 = _N_ ˆ + 1: 

Rewrite the operator _a_<sup>_†_</sup> _a_<sup>_†_</sup> _aa_ : 



<!-- Start of picture text -->
a † a † aa  =  a † ( a † a ) a  =  a † Na ˆ<br><!-- End of picture text -->

Using the operator commutation rule [ _N, a_<sup>ˆ</sup> ] = _−a_ = _⇒ Na_ ˆ = _a_ ( ˆ _N −_ 1): _a_<sup>_†_</sup> _Na_<sup>ˆ</sup> = _a_<sup>_†_</sup> _a_ ( _N_<sup>ˆ</sup> _−_ 1) = _N_<sup>ˆ</sup> ( _N_<sup>ˆ</sup> _−_ 1) 

Operating on state _|n⟩_ : 



<!-- Start of picture text -->
N ˆ ( ˆ N − 1) |n⟩ =  n ( n − 1) |n⟩<br><!-- End of picture text -->

## **Evaluation of Options** 

- **Option (a):** _n_ ( _n −_ 1) _→_ **CORRECT!** 

- **Option (b):** _n_<sup>2</sup> _→_ Incorrect. 

- **Option (c):** _n_ ( _n_ + 1) _→_ Incorrect (this corresponds to _aa_<sup>_†_</sup> _a_<sup>_†_</sup> _a_ ). 

- **Option (d):** ( _n_ + 1)<sup>2</sup> _→_ Incorrect (this corresponds to _aaa_<sup>_†_</sup> _a_<sup>_†_</sup> ). 

## **General Rule for Ladder Operator Products** 

For any power of creation and annihilation operators in normal-ordered form (all creation operators to the left of annihilation operators): 



<!-- Start of picture text -->
n !<br>( a † ) k a k |n⟩ = ( n − k )! |n⟩ =  n ( n − 1)( n − 2)  . . .  ( n − k  + 1) |n⟩<br><!-- End of picture text -->



<!-- Start of picture text -->
• For k = 1 : a † a|n⟩ =  n|n⟩<br>• For k = 2 : a † a † aa|n⟩ =  n ( n − 1) |n⟩<br><!-- End of picture text -->



<!-- Start of picture text -->
• For k = 3 : a † a † a † aaa|n⟩ =  n ( n − 1)( n − 2) |n⟩<br><!-- End of picture text -->

**Follow-up suggestion:** Would you like to practice evaluating expectation values of non-normal-ordered operator combinations like _⟨n|aa_<sup>_†_</sup> _aa_<sup>_†_</sup> _|n⟩_ or calculating **quadrature uncertainty products** ∆ _x ·_ ∆ _p_ using ladder operators next? 

