<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-radial-probability-density-hydrogen-4.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**Yes, absolutely!** There are exact general formulas for any principal quantum number _n_ and orbital quantum number _l_ for a hydrogen-like atom with nuclear charge _Z_ . 

## **1. General Radial Wavefunction** _Rnl_ ( _r_ ) 

The exact normalized radial wavefunction for any state ( _n, l_ ) is: 



<!-- Start of picture text -->
Rnl ( r ) = ·  e − na0 Zr ·  L 2l n − + l 1 − 1<br>√(  2Zna0 ) 3 2n ( n [(  − nl  +  −  l1 )!])! 3 · ( 2Zrna0 ) l ( 2Zrna0 )<br><!-- End of picture text -->

where: 

- _a_ 0 =<sup><u>4</u></sup> _m_<sup>_<u>πϵ</u>_</sup> _e_<sup><u>0</u></sup> _e_<sup>_<u>h</u>_¯22</sup><sup>_≈_0</sup><sup>_._529Åisthe</sup><sup>**Bohrradius**.</sup> 

- _L_<sup>2</sup> _n_<sup>_l_</sup> _−_<sup>+1</sup> _l−_ 1<sup>(</sup><sup>_x_)isthe</sup><sup>**AssociatedLaguerrePolynomial**ofdegree</sup><sup>_Nr_=</sup><sup>_n−l−_1</sup> (which gives the number of radial nodes). 

## **2. General Radial Probability Density** _Pnl_ ( _r_ ) 

The radial probability density _Pnl_ ( _r_ ) represents the probability per unit length of finding the electron in a spherical shell at distance _r_ : 



<!-- Start of picture text -->
Pnl ( r ) =  r 2 | Rnl ( r ) | 2<br><!-- End of picture text -->

Substituting the general _Rnl_ ( _r_ ) yields: 



<!-- Start of picture text -->
Pnl ( r ) = · e − na 2 Zr 0 · L 2 n l − +1 l− 1<br>( 2 naZ 0 )3 2( nn [(  −n  + l − l )!]1)! 3 · r 2  · ( 2 naZr 0 )2 l [ ( 2 naZr 0 )]2<br><!-- End of picture text -->

## **3. General Formula for “Circular” / Maximal Orbits (** _l_ = _n −_ 1 **)** 

For states where orbital angular momentum is maximized ( _l_ = _n−_ 1, i.e., 1 _s,_ 2 _p,_ 3 _d,_ 4 _f, . . ._ ), there are **zero radial nodes** ( _n − l −_ 1 = 0). The Associated Laguerre polynomial simplifies to a constant, making the expressions much simpler: 

Notes 

2 

- **Radial Wavefunction:** 



<!-- Start of picture text -->
na 0<br>Rn,n− 1( r )  ∝ r n− 1 e − Zr<br><!-- End of picture text -->

- **Radial Probability Density:** 



<!-- Start of picture text -->
na 0<br>Pn,n− 1( r )  ∝ r 2 n e − 2 Zr<br><!-- End of picture text -->

Setting<sup>_<u>dP</u>_</sup> _dr_<sup>= 0givesthe</sup><sup>**MostProbableRadius**foranystatewith</sup><sup>_l_=</sup><sup>_n −_1:</sup> 



<!-- Start of picture text -->
r mp = n2a0<br>Z<br><!-- End of picture text -->

• **Examples (** _Z_ = 1 **): –** 1 _s_ ( _n_ = 1 _, l_ = 0) = _⇒ r_ mp = 1<sup>2</sup> _a_ 0 = _a_ 0 **–** 2 _p_ ( _n_ = 2 _, l_ = 1) = _⇒ r_ mp = 2<sup>2</sup> _a_ 0 = 4 _a_ 0 **–** 3 _d_ ( _n_ = 3 _, l_ = 2) = _⇒ r_ mp = 3<sup>2</sup> _a_ 0 = 9 _a_ 0 **–** 4 _f_ ( _n_ = 4 _, l_ = 3) = _⇒ r_ mp = 4<sup>2</sup> _a_ 0 = 16 _a_ 0 

## **4. General Formula for Expectation Values** _⟨r_<sup>_k_</sup> _⟩nl_ 

For **any** general quantum state ( _n, l_ ), the average radial distance and radial powers are given by exact closed-form expressions: 

|Quantity|General Formula for Any<br>(_n, l_)|Ground State (1_s_) Example|
|---|---|---|
|**Average Distance** _⟨r⟩_|_⟨_**r**_⟩_**nl** = <sup>**a0**</sup><br>**2Z**<br>[<br>**3n**<sup>**2**</sup> _−_**l**(**l**+**1**)<br>]<br>|3<br>2<sup>_a_0</sup>|
|**Reciprocal Distance**<br>⟨1<br>_r_<br>⟩|⟨**1**<br>**r**<br>⟩<br>**nl** <sup>=</sup><br>**Z**<br>**n**<sup>**2**</sup>**a0**<br>|1<br>_a_0|
|**Squared Reciprocal**<br>⟨1<br>_r_<sup>2</sup><br>⟩<br>**Mean Square Distance**<br>⟨<br>_r_<sup>2⟩</sup>|⟨**1**<br>**r**<sup>**2**</sup><br>⟩<br>**nl** <sup>=</sup><br>**Z**<sup>**2**</sup><br>**n**<sup>**3**</sup>(**l**+ <sup>**1**</sup><br>**2**<sup>)</sup><sup>**a2**</sup><br>**0**<br>⟨<br>**r**<sup>**2**⟩</sup><br>**nl** <sup>=</sup> <sup>**a2**</sup><br>**0**<sup>**n2**</sup><br>**2Z**<sup>**2**</sup><br>[<br>**5n**<sup>**2** </sup>+**1**_−_**3l**(**l**+|2<br>_a_<sup>2</sup><br>0<br> **1**)<br>]<br>3_a_<sup>2</sup><br>0|



**Follow-up suggestion:** Would you like to practice evaluating **spin-orbit interaction energy shifts** ∆ _E_ **SO** _∝_ ⟨ _r_ <u>1</u><sup>3</sup> ⟩ or calculating **radial probability integrals** using these general formulas? 

