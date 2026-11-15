<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-3d-isotropic-harmonic-oscillator-3.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

The full wavefunction for a **1D Quantum Simple Harmonic Oscillator** consists of a spatial part (the stationary state eigenfunction _ψn_ ( _x_ )) and a time-evolution phase factor. 

## **1. Time-Independent Wavefunction (Stationary States** _ψn_ ( _x_ ) **)** 

The spatial eigenfunction for the _n_ -th quantum level is given by: 



<!-- Start of picture text -->
1<br>ψn ( x ) = Hn ( ξ )  e −ξ 2/2<br>( mωπh ¯ )1/4 √ 2 n n !<br><!-- End of picture text -->

where: 

- **Dimensionless position variable (** _ξ_ **):** 



<!-- Start of picture text -->
mω<br>ξ =<br>√ h ¯ x  = x x 0<br><!-- End of picture text -->

_(where x_ 0 = ~~√~~ _mωh_ ¯<sup>_isthecharacteristicquantumlengthscaleoftheoscillator)_.</sup> 

• _Hn_ ( _ξ_ ) **:** The _n_ -th **Hermite Polynomial** ( _n_ = 0 _,_ 1 _,_ 2 _,_ 3 _, . . ._ ). • **Normalization Factor:** ( _<u>mωπh</u>_ ¯ )1/4 _~~√~~_ 21<sup>_n_</sup> _n_ !<sup>ensures</sup> ∫ _−∞∞_<sup>_|ψn_(</sup><sup>_x_)</sup><sup>_|_2</sup><sup>_dx_= 1.</sup> 

## **2. Hermite Polynomials** _Hn_ ( _ξ_ ) 

The Hermite polynomials can be generated using **Rodrigues’ Formula** : 



<!-- Start of picture text -->
Hn ( ξ ) = ( − 1) n e ξ 2 dξ dnn ( e −ξ 2)<br><!-- End of picture text -->

The first few Hermite polynomials are: 

- _H_ 0( _ξ_ ) = 1 

- _H_ 1( _ξ_ ) = 2 _ξ_ 

- _H_ 2( _ξ_ ) = 4 _ξ_<sup>2</sup> _−_ 2 

- _H_ 3( _ξ_ ) = 8 _ξ_<sup>3</sup> _−_ 12 _ξ_ 

Notes 

2 

## **3. Full Time-Dependent Wavefunction** Ψ _n_ ( _x, t_ ) 

For a system in a single stationary state with energy _En_ = ( _n_ + 2<sup><u>1</u></sup> ) _hω_ ¯ , the complete time-dependent wavefunction is: 



<!-- Start of picture text -->
1 mω<br>Ψ n ( x, t ) =  ψn ( x )  e −iEnt / h ¯ = ( mωπh ¯ )1/4 √ 2 n n ! Hn ( √ h ¯ x ) e − mωx 2 h ¯ 2 e −i ( n + 2 1 ) ωt<br><!-- End of picture text -->

## **4. General Arbitrary State (Superposition)** 

For any arbitrary or non-stationary state, the general wavefunction is expressed as a linear combination of all stationary states: 



<!-- Start of picture text -->
∞ ∞ 1 mω<br>Ψ( x, t ) = ∑ n =0 cnψn ( x )  e −iEnt / h ¯ = ∑ n =0 cn ( mωπh ¯ )1/4 √ 2 n n ! Hn ( √ h ¯ x ) e − mωx 2 h ¯ 2 e −i ( n + 2 1 ) ωt<br><!-- End of picture text -->

where the expansion coefficients _cn_ are determined from the initial condition Ψ( _x,_ 0) by: 



<!-- Start of picture text -->
cn = ψn ∗ ( x ) Ψ( x,  0)  dx<br>∫ −∞∞<br><!-- End of picture text -->

## **5. First Few Explicit Wavefunctions** 



<!-- Start of picture text -->
• Ground State ( n  = 0 , E 0 = 1 2 hω ¯ ):<br><!-- End of picture text -->



<!-- Start of picture text -->
ψ 0( x ) = e − mωx 2 h ¯ 2<br>( mωπh ¯ )1/4<br>• First Excited State ( n  = 1 , E 1 = 3 2 hω ¯ ):<br>mω<br>ψ 1( x ) = 2 e − mωx 2 h ¯ 2<br>( mωπh ¯ )1/4 √ h ¯ x<br>( √ )<br><!-- End of picture text -->



<!-- Start of picture text -->
• Second Excited State ( n  = 2 , E 2 = 5 2 hω ¯ ):<br><!-- End of picture text -->



<!-- Start of picture text -->
ψ 2( x ) = x 2 − 1 e − mωx 2 h ¯ 2<br>( mωπh ¯ )1/4 √ 12 ( 2 mωh ¯ )<br><!-- End of picture text -->

## **6. 3D Isotropic Harmonic Oscillator** 

In three dimensions with isotropic frequency _ω_ , the wavefunction separates in Cartesian coordinates as: 



<!-- Start of picture text -->
ψnx,ny,nz ( x, y, z ) =  ψnx ( x )  ψny ( y )  ψnz ( z )<br><!-- End of picture text -->

with total energy: 



<!-- Start of picture text -->
hω ¯<br>Enx,ny,nz = nx  +  ny  +  nz  + 3<br>2<br>( )<br><!-- End of picture text -->

Notes 

3 

The definite parity of the 1D Quantum Harmonic Oscillator wavefunctions _ψn_ ( _x_ ) and their behavior at the origin ( _x_ = 0) can be understood through **three complementary perspectives** : 

## **1. Mathematical Proof via Hermite Polynomials** 

The spatial wavefunction of the harmonic oscillator is expressed as: 



<!-- Start of picture text -->
1 mω<br>ψn ( x ) = ( mωπh ¯ )1/4 √ 2 n n ! Hn ( ξ )  e −ξ 2/2 , where ξ = √ h ¯ x<br><!-- End of picture text -->

1. **The Gaussian Factor (** _e_<sup>_−ξ_2/2</sup> **):** Since ( _−ξ_ )<sup>2</sup> = _ξ_<sup>2</sup> , the exponential term is **strictly even** under reflection ( _ξ →−ξ_ ). 

2. **The Hermite Polynomials (** _Hn_ ( _ξ_ ) **):** From the Rodrigues formula _Hn_ ( _ξ_ ) = ( _−_ 1)<sup>_n_</sup> _e_<sup>_ξ_2</sup> _dξ_<sup>_<u>dnn</u>_</sup> ( _e_<sup>_−ξ_2)</sup> , Hermite polynomials satisfy the parity relation: 



<!-- Start of picture text -->
Hn ( −ξ ) = ( − 1) n Hn ( ξ )<br><!-- End of picture text -->

- **For Even** _n_ **(** _n_ = 0 _,_ 2 _,_ 4 _, . . ._ **):** _Hn_ ( _−ξ_ ) = ( _−_ 1)<sup>even</sup> _Hn_ ( _ξ_ ) = + _Hn_ ( _ξ_ ) = _⇒ ψ_ **n** ( _−_ **x** ) = + _ψ_ **n** ( **x** ) (EVEN Parity) 

- **For Odd** _n_ **(** _n_ = 1 _,_ 3 _,_ 5 _, . . ._ **):** 

   - _Hn_ ( _−ξ_ ) = ( _−_ 1)<sup>odd</sup> _Hn_ ( _ξ_ ) = _−Hn_ ( _ξ_ ) = _⇒ ψ_ **n** ( _−_ **x** ) = _−ψ_ **n** ( **x** ) (ODD Parity) 

**2. Why** _ψn_ (0) = 0 **for Odd** _n_ **and** _ψn_ (0) _̸_ = 0 **for Even** _n_ 

**For Odd** _n_ **(Odd Parity):** By definition, any function _f_ ( _x_ ) with odd parity satisfies _f_ ( _−x_ ) = _−f_ ( _x_ ). Evaluating this relation at the origin _x_ = 0: 



<!-- Start of picture text -->
f (0) =  −f (0) = ⇒ 2 f (0) = 0 = ⇒ f ( 0 ) =  0<br><!-- End of picture text -->

**Every odd-parity function MUST vanish at** _x_ = 0 **.** 

_In terms of Hermite polynomials:_ Odd Hermite polynomials consist strictly of odd powers of _ξ_ (e.g., _H_ 1( _ξ_ ) = 2 _ξ_ , _H_ 3( _ξ_ ) = 8 _ξ_<sup>3</sup> _−_ 12 _ξ_ ). Setting _ξ_ = 0 makes every term zero, so _Hn_ (0) = 0. 

**For Even** _n_ **(Even Parity):** Even Hermite polynomials contain a non-zero constant term (e.g., _H_ 0(0) = 1, _H_ 2(0) = _−_ 2, _H_ 4(0) = 12): 



<!-- Start of picture text -->
H 2 k (0) = ( − 1) k  (2 k )!<br>k !<br><!-- End of picture text -->

Since the Gaussian term _e_<sup>0</sup> = 1 is also non-zero, _ψn_ (0) _̸_ = 0 **for all even** _n_ . 

Notes 

4 

## **3. Algebraic Proof via Creation/Annihilation Operators** 

The ground state _ψ_ 0( _x_ ) = ( _<u>mωπh</u>_ ¯ )1/4 _e−mωx_ 2/2 _h_ ¯ is a Gaussian centered at _x_ = 0, which is **even** (Π<sup>ˆ</sup> _|_ 0 _⟩_ = + _|_ 0 _⟩_ ). 

The raising (creation) operator is: 



<!-- Start of picture text -->
mω d<br>a ˆ † = x − h ¯<br>√ 2 h ¯ ( mω dx )<br><!-- End of picture text -->



<!-- Start of picture text -->
Under spatial reflection ( x →−x and dxd →− dx d ):<br>ˆΠ ˆ a † ˆΠ † =  −a ˆ † = ⇒ ^a † is an ODD operator<br><!-- End of picture text -->

Any _n_ -th excited state is generated by applying _a_ ˆ<sup>_†_</sup> _n_ times to the ground state: 



<!-- Start of picture text -->
|n⟩ = ( a ˆ † ) n | 0 ⟩<br>√ n !<br><!-- End of picture text -->

Applying the parity operator Π<sup>ˆ</sup> : 



<!-- Start of picture text -->
ˆΠ |n⟩ = ( −a ˆ † ) n ˆΠ | 0 ⟩ = ( − 1) n ( a ˆ † ) n (+ | 0 ⟩ ) = ( − 1 ) n | n ⟩<br>√ n ! √ n !<br><!-- End of picture text -->

- Applying an odd operator _n_ times to an even state flips the parity _n_ times, yielding a parity eigenvalue of ( _−_ 1)<sup>_n_</sup> . 

## **Summary Table** 

|Quantum<br>Number _n_|State Type|Hermite<br>Polynomial<br>_Hn_(_ξ_)|Parity<br>_ψn_(_−x_)|Value at<br>Origin _ψn_(0)|Number of<br>Nodes|
|---|---|---|---|---|---|
|_n_= 0|Ground State|1|**Even (**+_ψ_0**)**|= 0<br>(Maximum)|0|
|_n_= 1|1<sup>st </sup>Excited<br>State|2_ξ_|**Odd (**_−ψ_1**)**|= 0 (Node at<br>origin)|1|
|_n_= 2|2<sup>nd </sup>Excited<br>State|4_ξ_<sup>2</sup> _−_2|**Even (**+_ψ_2**)**|= 0|2|
|_n_= 3|3<sup>rd </sup>Excited<br>State|8_ξ_<sup>3</sup> _−_12_ξ_|**Odd (**_−ψ_3**)**|= 0 (Node at<br>origin)|3|



**Follow-up suggestion:** This odd/even parity distinction is the exact mathematical key behind solving **half-harmonic oscillator problems** ( _V_ ( _x_ ) =<sup><u>1</u></sup> 2<sup>_mω_2</sup><sup>_x_2for</sup><sup>_x>_0and</sup> _V_ ( _x_ ) = _∞_ for _x ≤_ 0). Would you like to see how the half-oscillator spectrum is derived using these boundary conditions? 

