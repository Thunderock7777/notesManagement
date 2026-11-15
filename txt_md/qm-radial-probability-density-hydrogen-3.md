<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-radial-probability-density-hydrogen-3.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Quantum Spatial Architecture of the Hydrogen Atom: Ground and Excited States** 

**1. Mathematical Framework and Spatial Separation** The spatial behavior of the electron in a hydrogenic atom (atomic number _Z_ , reduced mass _µ ≈ me_ ) is governed by the time-independent Schrödinger equation with a central Coulomb potential: 



<!-- Start of picture text -->
H ˆ =  − h ¯2<br>2 µ ∇ 2 +  V  ( r ) =  − 2 h ¯ µ 2 ∇ 2  − 4 Ze πϵ 0 2 r<br><!-- End of picture text -->

In spherical polar coordinates ( _r, θ, ϕ_ ), the Laplacian operator separates into radial and angular components: 



<!-- Start of picture text -->
∇ 2 = 1 ∂ r 2 ∂ + 1 ∂ sin  θ ∂ + 1 ∂ 2<br>r 2 ∂r � ∂r � r 2 sin  θ ∂θ � ∂θ � r 2 sin 2 θ ∂ϕ 2<br><!-- End of picture text -->

Because the Coulomb potential _V_ ( _r_ ) = _−Ze_<sup>2</sup> /(4 _πϵ_ 0 _r_ ) is spherically symmetric, the total spatial wavefunction _ψnlm_ ( _r, θ, ϕ_ ) factorizes strictly into a radial wavefunction _Rnl_ ( _r_ ) and an angular wavefunction given by the spherical harmonics _Ylm_ ( _θ, ϕ_ ): 

_ψnlm_ ( _r, θ, ϕ_ ) = _Rnl_ ( _r_ ) _Ylm_ ( _θ, ϕ_ ) 

**1.1 Quantum Numbers and Spatial Constraints** The spatial structure is uniquely specified by three integral quantum numbers: 

- _<u>µZ</u>_<sup>2</sup> _e_<sup>4</sup> 

- • **Principal Quantum Number (** _n ≥_ 1 **):** Governs total energy _En_ = _−_ 32 _π_<sup>2</sup> _ϵ_<sup>2</sup> 0<sup>_h_¯2</sup><sup>_n_2=</sup> _−_ 13 _._ 6<sup>_<u>Z</u>_</sup> _n_<sup>22eV,totalnumberofspatialnodes(</sup><sup>_n−_1),andthespatialexponential</sup> decay scale factor _e_<sup>_−Zr_/</sup><sup>_na_0</sup> . 

- **Orbital Angular Momentum Quantum Number (** _l ∈{_ 0 _,_ 1 _<u>, . . . , n</u> −_ 1 _}_ **):** Quantizes total orbital angular momentum magnitude _|_ **L** _|_ = ~~�~~ _l_ ( _l_ + 1) _h_ ¯ and specifies angular node count _Na_ = _l_ . 

- **Magnetic Quantum Number (** _ml ∈{−l, −l_ + 1 _, . . . ,_ + _l}_ **):** Quantizes the _z_ - projection of angular momentum _Lz_ = _mlh_ ¯, governing the directional orientation of the probability density. 

Notes 

2 

**1.2 Spatial Degeneracy** For a pure 1/ _r_ Coulomb potential, energy depends exclusively on _n_ . The spatial degeneracy _gn_ (ignoring electron spin) is given by summing over all allowed _l_ subshells: 



<!-- Start of picture text -->
n− 1<br>gn = �(2 l  + 1) =  n 2<br>l =0<br><!-- End of picture text -->

Including the 2-fold spin degeneracy ( _ms_ = _±_ 1/2), the total state capacity of the _n_ -th shell is 2 _n_<sup>2</sup> . 

**2. Spatial Properties of the Ground State (** 1 _s_ **,** _n_ = 1 _, l_ = 0 _, ml_ = 0 **)** The ground state represents the lowest-energy bound configuration ( _E_ 1 = _−_ 13 _._ 6 eV for _Z_ = 1). 

**2.1 Wavefunction and Spatial Distribution** With _n_ = 1 _, l_ = 0 _, ml_ = 0, the angular factor is isotropic ( _Y_ 00 = 1/ _~~√~~_ 4 _π_ ), yielding a completely spherically symmetric wavefunction: 



<!-- Start of picture text -->
1<br>ψ 100( r ) = e −r / a 0<br>� πa 3 0<br><!-- End of picture text -->

where _a_ 0 =<sup><u>4</u></sup> _m_<sup>_<u>πϵ</u>_</sup> _e_<sup><u>0</u></sup> _e_<sup>_<u>h</u>_¯22</sup><sup>_≈_0</sup><sup>_._529177ÅistheBohrradius.</sup> Unlike states with _l >_ 0, the _s_ -wave radial wavefunction _R_ 10( _r_ ) = 2 _a_<sup>_−_</sup> 0<sup>3/2</sup> _e_<sup>_−r_/</sup><sup>_a_0</sup> attains its global maximum directly at the nucleus ( _r_ = 0): 



<!-- Start of picture text -->
2 1<br>R 10(0) = = ⇒|ψ 100(0) | 2 =<br>a 3/2 0 πa 3 0<br><!-- End of picture text -->

**2.2 Radial Probability Density and Most Probable Radius** The probability of finding the electron in a spherical shell of radius _r_ and thickness _dr_ is governed by the radial probability density function _P_ ( _r_ ): 



<!-- Start of picture text -->
P ( r ) =  r 2 |R 10( r ) | 2 = 4 r 2 e − 2 r / a 0<br>a 3 0<br><!-- End of picture text -->

To locate the most probable distance _r_ mp from the nucleus, set the first derivative of _P_ ( _r_ ) to zero: 



<!-- Start of picture text -->
dP ( r ) = 4 2 r − 2 r 2<br>e − 2 r / a 0 = 0 = ⇒ r mp =  a 0<br>dr a 3 0 � a 0 �<br><!-- End of picture text -->

Thus, the most probable radius in quantum mechanics coincides exactly with the radius of the first circular orbit in Bohr’s classical model. 

**2.3 Spatial Expectation Values and Spread** Due to the asymmetric, right-skewed tail of _P_ ( _r_ ), the average (expectation) distance _⟨r⟩_ is larger than the most probable distance _r_ mp: 



<!-- Start of picture text -->
• Mean Distance: ⟨r⟩ 1 s = �0 ∞ rP ( r ) dr = 2 3 a 0 = 1 . 5 a 0<br><!-- End of picture text -->

Notes 

3 

- **Mean Squared Distance:** _⟨r_<sup>2</sup> _⟩_ 1 _s_ = 3 _a_<sup>2</sup> 0 

- **Spatial Uncertainty (Spread):** ∆ _r_ = ~~�~~ _⟨r_<sup>2</sup> _⟩−⟨r⟩_<sup>2</sup> = ~~�~~ 3 _a_<sup>2</sup> 0<sup>_−_2</sup><sup>_._25</sup><sup>_a_2</sup> 0<sup>=</sup> _~~<u>√</u>~~_ 23<sup>_a_0</sup><sup>_≈_</sup> 0 _._ 866 _a_ 0 

- **Mean Reciprocal Distance:** � <u>1</u> _r_ �1 _s_<sup>=</sup> _a_ <u>10</u> 



<!-- Start of picture text -->
• Mean Reciprocal Squared Distance: � r 1 2 �1 s = a 2 2 0<br><!-- End of picture text -->

**3. Spatial Architecture of Excited States (** _n_ = 2 _,_ 3 _,_ 4 **)** As _n_ increases, the electron spatial probability cloud expands outward as _n_<sup>2</sup> , and the radial wavefunctions develop nodes where _Rnl_ ( _r_ ) = 0. 

- **3.1 The** _n_ = 2 **Excited Shell (4-fold Spatial Degeneracy)** The _n_ = 2 energy level ( _E_ 2 = _−_ 3 _._ 4 eV) contains four degenerate spatial states: 2 _s_ ( _l_ = 0) and three 2 _p_ orbitals ( _l_ = 1 _, ml ∈{_ 0 _, ±_ 1 _}_ ). 

_1. The_ 2 _s State (n_ = 2 _, l_ = 0 _)_ 

- **Normalized Radial Wavefunction:** 



<!-- Start of picture text -->
R 20( r ) = 1 1  − r e −r /2 a 0<br>2 √ 2 a 3/2 0 � 2 a 0 �<br><!-- End of picture text -->

- **Behavior at Nucleus:** Non-zero at origin, _R_ 20(0) = 



<!-- Start of picture text -->
1<br>2 √ 2 a 3/2 0 .<br><!-- End of picture text -->

- **Radial Node:** Exactly 1 radial node where 1 _− r_ /(2 _a_ 0) = 0 = _⇒ r_ = 2 _a_ 0. 

- **Radial Probability Peaks:** _P_ 2 _s_ ( _r_ ) exhibits two distinct maxima: a small inner sphere at _r ≈_ 0 _._ 76 _a_ 0 and a dominant outer spherical shell at _r ≈_ 5 _._ 24 _a_ 0. 



<!-- Start of picture text -->
• Expectation Values: ⟨r⟩ 2 s = 6 a 0, ⟨r 2 ⟩ 2 s = 42 a 2 0 , � 1 r �2 s = 4 a 10 .<br><!-- End of picture text -->

_2. The_ 2 _p States (n_ = 2 _, l_ = 1 _)_ 

   - **Normalized Radial Wavefunction:** 



<!-- Start of picture text -->
1<br>R 21( r ) = e −r /2 a 0<br>2 √ 6 a 3/2 0 � ar 0 �<br><!-- End of picture text -->

- **Behavior at Nucleus:** Vanishes at origin ( _R_ 21(0) = 0) due to the centrifugal barrier. 

- **Radial Nodes:** 0 radial nodes ( _n − l −_ 1 = 2 _−_ 1 _−_ 1 = 0). 

- **Most Probable Radius:** _r_ mp = 4 _a_ 0. 

- <u>1</u> 

- • **Expectation Values:** _⟨r⟩_ 2 _p_ = 5 _a_ 0, _⟨r_<sup>2</sup> _⟩_ 2 _p_ = 30 _a_ 0<sup>2,</sup> � <u>1</u> _r_ �2 _p_<sup>=</sup> 4 _a_ 0<sup>.</sup> 

Notes 

4 

**3.2 The** _n_ = 3 **Excited Shell (9-fold Spatial Degeneracy)** The _n_ = 3 level ( _E_ 3 = _−_ 1 _._ 51 eV) comprises 3 _s_ ( _l_ = 0), 3 _p_ ( _l_ = 1), and 3 _d_ ( _l_ = 2) orbitals. 

   - 3 _s_ **Orbital (** _n_ = 3 _, l_ = 0 **):** Has 2 radial nodes at _r_ = 23<sup>(3</sup><sup>_∓_</sup> _~~√~~_ 3) _a_ 0 _≈_ 1 _._ 90 _a_ 0 and 7 _._ 10 _a_ 0. _⟨r⟩_ 3 _s_ = 13 _._ 5 _a_ 0. 

   - 3 _p_ **Orbital (** _n_ = 3 _, l_ = 1 **):** Has 1 radial node at _r_ = 6 _a_ 0. _⟨r⟩_ 3 _p_ = 12 _._ 5 _a_ 0. 

   - 3 _d_ **Orbital (** _n_ = 3 _, l_ = 2 **):** Maximum angular momentum state ( _l_ = _n −_ 1), 0 radial nodes. _r_ mp = 9 _a_ 0, _⟨r⟩_ 3 _d_ = 10 _._ 5 _a_ 0. 

**4. Nodal Topology and Spatial Symmetry Rules** The spatial nodes are zeroprobability boundary surfaces dividing regions of opposite wavefunction phase. 

## **4.1 Categorization of Nodal Surfaces** 

1. **Radial Nodes (** _Nr_ **):** Spherical surfaces centered at the nucleus where _Rnl_ ( _r_ ) = 0. 



<!-- Start of picture text -->
Nr =  n − l − 1<br><!-- End of picture text -->

2. **Angular Nodes (** _Na_ **):** Planar or conical surfaces passing through the nucleus where _Ylm_ ( _θ, ϕ_ ) = 0. 



<!-- Start of picture text -->
Na =  l<br><!-- End of picture text -->

3. **Total Spatial Nodes (** _N_ **total):** 



<!-- Start of picture text -->
N total =  Nr  +  Na = ( n − l − 1) +  l =  n − 1<br><!-- End of picture text -->

**4.2 Spatial Parity and Inversion Symmetry** Under spatial reflection through the origin ( _⃗r →−⃗r_ , which corresponds in spherical coordinates to _r → r_ , _θ → π − θ_ , _ϕ → ϕ_ + _π_ ), the radial function is invariant ( _Rnl_ ( _r_ ) _→ Rnl_ ( _r_ )), while spherical harmonics transform according to: 



<!-- Start of picture text -->
PY ˆ lm ( θ, ϕ ) =  Ylm ( π − θ, ϕ  +  π ) = ( − 1) l Ylm ( θ, ϕ )<br><!-- End of picture text -->

Thus, spatial parity Π depends solely on the orbital quantum number _l_ : 



<!-- Start of picture text -->
Π = ( − 1) l<br><!-- End of picture text -->

- **Even Parity (** Π = +1 **):** _s_ -orbitals ( _l_ = 0), _d_ -orbitals ( _l_ = 2), _g_ -orbitals ( _l_ = 4). 

- **Odd Parity (** Π = _−_ 1 **):** _p_ -orbitals ( _l_ = 1), _f_ -orbitals ( _l_ = 3). 

Notes 

5 

**4.3 Centrifugal Barrier Near the Origin** Near _r →_ 0, the radial equation is dominated by the repulsive centrifugal potential term<sup>_l_</sup><sup><u>(</u></sup><sup>_l_</sup><sup><u>+1)</u></sup><sup>_h_¯2</sup> 2 _µr_<sup>2:</sup> 

_r_ lim _→_ 0<sup>_Rnl_(</sup><sup>_r_)</sup><sup>_∝rl_</sup> 

- For _l_ = 0 ( _s_ -states): _Rn_ 0(0) _̸_ = 0. Electron density at the nucleus is non-vanishing, enabling **Fermi contact hyperfine interaction** . 

- For _l >_ 0 ( _p, d, f_ states): _Rnl_ ( _r_ ) vanishes at _r_ = 0 as _r_<sup>1</sup> _, r_<sup>2</sup> _, r_<sup>3</sup> _, . . ._ , suppressing overlap with the nucleus. 

**5. Master Comparison Table of Spatial Properties** The table below synthesizes the spatial parameters for low-lying hydrogenic states ( _Z_ = 1): 

|State<br>(_n, l_)|Orbital<br>Nota-<br>tion|_Rnl_(_r_)<br>Analyt-<br>ical<br>Form<br>Radial<br>Nodes<br>(_n −_<br>_l −_1)<br>Angular<br>Nodes<br>(_l_)|Most<br>Proba-<br>ble<br>Radius<br>_r_mp|Mean<br>Radius<br>_⟨r⟩_/_a_0|Mean<br>_r_<sup>2</sup><br>_⟨r_<sup>2</sup>_⟩_/_a_<sup>2</sup><br>0|Mean<br>1/_r_<br>_⟨_1/_r⟩·_<br>_a_0|Parity<br>Π =<br>(_−_1)<sup>_l_</sup>|
|---|---|---|---|---|---|---|---|
|(1, 0)|1_s_|2_a_<sup>_−_3/2</sup><br>0<br>_e_<sup>_−r_/</sup><sup>_a_0</sup><br>0<br>0|_a_0|1.5|3.0|1.0|Even<br>(+1)|
|(2, 0)|2_s_|1<br>2<br>_~~√~~_<br>2<sup>_a−_3/2</sup><br>0<br>�<br>1_−_<br>_r_<br>2_a_0<br>�<br>_e_<sup>_−r_/2</sup><sup>_a_0</sup><br>1 (_r_ ~~=~~<br>2_a_0)<br>0|5_._24_a_0<br>(outer)|6.0|42.0|0.25|Even<br>(+1)|
|(2, 1)|2_p_|1<br>2<br>_~~√~~_<br>6<sup>_a−_3/2</sup><br>0<br>�<br>_r_<br>_a_0<br>�<br>_e_<sup>_−r_/2</sup><sup>_a_0</sup><br>0<br>1|4_a_0|5.0|30.0|0.25|Odd<br>(_−_1)|
|(3, 0)|3_s_|2<br>27<br>_~~√~~_<br>3<sup>_a−_3/2</sup><br>0<br>�<br>27_−_18 <sup>_r_</sup><br>_a_0 <sup>+ 2</sup> <sup>_r_2</sup><br>_a_<sup>2</sup><br>0<br>�<br>2<br>~~0~~|_e_<sup>_−r_/3</sup><sup>_a_0</sup><br>11_._6_a_0<br>(outer)|13.5|207.0|0.111|Even<br>(+1)|
|(3, 1)|3_p_|8<br>27<br>_~~√~~_<br>6<sup>_a−_3/2</sup><br>0<br>�<br>1_−_<br>_r_<br>6_a_0<br>��<br>_r_<br>_a_0<br>�<br>_e_<sup>_−_</sup><br>1 (_r_ ~~=~~<br>6_a_0)<br>1<br>|<sup>_r_/3</sup><sup>_a_0</sup><br>12_._0_a_0|12.5|180.0|0.111|Odd<br>(_−_1)|
|(3, 2)|3_d_|4<br>81<br>_~~√~~_<br>30<sup>_a−_3/2</sup><br>0<br>�<br>_r_<br>_a_0<br>�2<br>_e_<sup>_−r_/3</sup><sup>_a_0</sup><br>0<br>2|9_a_0|10.5|126.0|0.111|Even<br>(+1)|
|(_n, n −_<br>1)|Max _l_|_Nnr_<sup>_n−_1</sup>_e_<sup>_−r_/</sup><sup>_na_0</sup><br>0<br>_n −_1|_n_<sup>2</sup>_a_0|_n_<br>2 <sup>(</sup><sup>_n_ +</sup><br>2)_a_0|_n_<sup>3</sup><br>2 <sup>(2</sup><sup>_n_+</sup><br>1)_a_<sup>2</sup><br>0|1<br>_n_<sup>2</sup>_a_0|(_−_1)<sup>_n−_1</sup>|



**6. General Formulae for Radial Expectation Values** For an arbitrary hydrogenic state _|n, l, m⟩_ , radial expectation values obey closed-form expressions: 

## **6.1 Standard Closed-Form Moments** 

1. **Expectation Value of** _r_ **:** 



<!-- Start of picture text -->
⟨r⟩nl = a 0 �3 n 2 − l ( l  + 1)�<br>2 Z<br><!-- End of picture text -->

Notes 

6 

2. **Expectation Value of** _r_<sup>2</sup> **:** 



<!-- Start of picture text -->
0<br>⟨r 2 ⟩nl = n 2 a 2 �5 n 2 + 1  − 3 l ( l  + 1)�<br>2 Z 2<br><!-- End of picture text -->

3. **Expectation Value of** 1/ _r_ **(Inverse Radial Distance):** 



<!-- Start of picture text -->
Z<br>=<br>� 1 r � nl n 2 a 0<br><!-- End of picture text -->

_(Note: ⟨_ 1/ _r⟩ depends solely on n, reflecting the Virial Theorem ⟨V ⟩_ = 2 _En)._ 

4. **Expectation Value of** 1/ _r_<sup>2</sup> **:** 



<!-- Start of picture text -->
Z 2<br>=<br>� r 1 2 � nl n 3 a 2 0 � l  + 2 1 �<br><!-- End of picture text -->

5. **Expectation Value of** 1/ _r_<sup>3</sup> **(Valid for** _l >_ 0 **):** 



<!-- Start of picture text -->
Z 3<br>=<br>� r 1 3 � nl n 3 a 3 0 l � l  + 1 2 � ( l  + 1)<br><!-- End of picture text -->

**6.2 Kramers’ Recurrence Relation** All radial moments _⟨r_<sup>_k_</sup> _⟩_ satisfy Kramers’ recurrence relation ( _k > −_ 2 _l −_ 1): 



<!-- Start of picture text -->
k  + 1<br>�(2 l  + 1) 2 − k 2� a 2 0 ⟨rk− 2 ⟩ = 0<br>n 2 ⟨rk⟩− (2 k  + 1) a 0 ⟨rk− 1 ⟩ + k 4<br><!-- End of picture text -->

**7. Response to External Fields and Dipole Properties** 

**7.1 Permanent Electric Dipole Moment** The electric dipole moment operator is **d** = _−e_ **r** . For any isolated, unperturbed stationary state _|n, l, ml⟩_ , the expectation value vanishes identically: 



<!-- Start of picture text -->
⟨ d ⟩ =  −e |ψnlm ( ⃗r ) | 2 · r d 3 r = 0<br>� � �� � ����<br>EVEN ODD<br><!-- End of picture text -->

**Fundamental Physics Rule:** An isolated hydrogen atom in any energy eigenstate has zero permanent electric dipole moment due to definite spatial parity Π = ( _−_ 1)<sup>_l_</sup> . 

## **7.2 Linear vs. Quadratic Stark Effect** 

- **Ground State (** 1 _s_ **,** _n_ = 1 **):** Non-degenerate state of definite parity (Π = +1). First-order energy shift ∆ _E_<sup>(1)</sup> = _⟨_ 100 _|eEz|_ 100 _⟩_ = 0. Exhibits a **quadratic Stark shift** (∆ _E ∝E_<sup>2</sup> ). 

Notes 

7 

- **First Excited State (** _n_ = 2 **):** 4-fold degenerate space containing states of opposite parities (2 _s_ with Π = +1 and 2 _pz_ with Π = _−_ 1). The electric field breaks parity symmetry by mixing 2 _s_ and 2 _pz_ : 



<!-- Start of picture text -->
⟨ 200 |eEz| 210 ⟩ =  − 3 ea 0 E<br><!-- End of picture text -->

This non-zero off-diagonal matrix element yields a **linear Stark shift** (∆ _E_ = _±_ 3 _ea_ 0 _E,_ 0). “‘eof 

The errors have been resolved, and the content is completely reformatted using clean standard LaTeX syntax for the math block and proper | pipe syntax for the Master Comparison Table. If you need any further adjustments to equations or layout, let me know! 

