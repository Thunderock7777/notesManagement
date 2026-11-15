<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-potential-wells-comparison-master-chart-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Welcome to **Module 4: Band Theory & Semiconductor Physics** ! 

This module explains why some solids are metals, some are insulators, and others are semiconductors, and provides the mathematical foundation for semiconductor devices in the GATE Physics exam. 

## **1. Band Theory of Solids & Bloch’s Theorem** 

**A. Periodic Potential & Bloch’s Theorem** When an electron moves through a 3D crystal lattice, it experiences a periodic potential _V_ ( _r_ + _R_ ) = _V_ ( _r_ ) imposed by the array of ion cores. 

According to **Bloch’s Theorem** , the wavefunctions governing such an electron take the form of plane waves modulated by a function _uk_ ( _r_ ) that shares the exact spatial periodicity of the lattice: 



<!-- Start of picture text -->
ψk ( r ) =  uk ( r ) e ik·r where uk ( r  +  R ) =  uk ( r )<br><!-- End of picture text -->

An equivalent statement is the translational phase-shift property: 



<!-- Start of picture text -->
ψk ( x  +  a ) =  ψk ( x ) e ika<br><!-- End of picture text -->

**B. The Kronig-Penney Model** To analytically solve the Schrödinger equation in a 1D periodic potential, the Kronig-Penney model replaces the atomic potential wells with an array of rectangular barriers modeled as Dirac delta functions of barrier strength _P_ : 



<!-- Start of picture text -->
P sin( αa ) + cos( αa ) = cos( ka ) where α  = √ 2 mE<br>αa h ¯<br><!-- End of picture text -->

   - _P_ = dimensionless barrier strength parameter (proportional to potential barrier height _V_ 0 and width _b_ ). 

   - _a_ = lattice spacing. 

   - _k_ = crystal wave vector. 

- **C. Key Physical Consequences & Limiting Cases** 

   1. **Formation of Energy Bands & Gaps:** Real _k_ values exist only when the lefthand transcendental function satisfies _|F_ ( _αa_ ) _| ≤_ 1. Regions where _|F_ ( _αa_ ) _| >_ 1 force 

Notes 

2 

_k_ to become complex, causing exponential decay of waves, which defines **forbidden energy band gaps (** _Eg_ **)** . 

2. **Limit** _P →_ 0 **(Free Electron Limit):** 



<!-- Start of picture text -->
cos( αa ) = cos( ka ) = ⇒ α  =  k = ⇒ E = h ¯2 k 2<br>2 m<br><!-- End of picture text -->

The forbidden gaps vanish completely, recovering the free-particle parabola. 

3. **Limit** _P →∞_ **(Isolated Atom Limit):** 



<!-- Start of picture text -->
sin( αa ) = 0 = ⇒ αa  =  nπ = ⇒ En = n 2 π 2 h ¯2<br>2 ma 2<br><!-- End of picture text -->

The allowed bands shrink into infinitely sharp, discrete atomic energy levels. 

4. **Energy Band Gap Behavior:** As energy _E_ increases (larger _αa_ ), the term _P_<sup>sin</sup> _αa_<sup><u>(</u></sup><sup>_αa_</sup><sup><u>)</u></sup> decays because _αa_ is in the denominator. Consequently, **higher energy allowed bands become wider, while forbidden band gaps become narrower** . 

**2. Effective Mass (** _m_<sup>_∗_</sup> **) & The Concept of Holes** 

**A. Semiclassical Equations of Motion & Group Velocity** An electron wave packet in a band moves with group velocity _vg_ : 



<!-- Start of picture text -->
vg = 1 dE<br>h ¯ dk<br><!-- End of picture text -->

Differentiating _vg_ with respect to time under an external force _F_ = _−eE_ ext = ¯ _h_<sup>_<u>dk</u>_</sup> _dt_<sup>gives:</sup> 



<!-- Start of picture text -->
d 2 E dk d 2 E<br>a  = dv dt g = h ¯ 1 dk 2 dt = ( h ¯1 2 dk 2 ) F<br><!-- End of picture text -->

**B. Effective Mass Definition** Comparing _a_ = _F_ / _m_<sup>_∗_</sup> to Newton’s second law yields the **curvature definition of effective mass** : 



<!-- Start of picture text -->
1 d 2 E = ⇒ m ∗ ( k ) = d h ¯2 E 2<br>m ∗ ≡ h ¯ 12 dk 2<br>dk 2<br><!-- End of picture text -->

- **Near the bottom of a band (** _k ≈_ 0 **):** Curve opens upward (<sup>_<u>d</u>_</sup> _dk_<sup>2</sup><sup>_<u>E</u>_2</sup><sup>_>_0),so</sup><sup>_m∗>_0</sup> (behaves like a normal electron). 

- **At the inflection point:** _<u>ddk</u>_<sup>2</sup> _<u>E</u>_<sup>2= 0,so</sup><sup>_m∗→∞_.</sup> 

- **Near the top of a band (** _k →±π_ / _a_ **):** Curve bends downward (<sup>_<u>d</u>_</sup> _dk_<sup>2</sup><sup>_<u>E</u>_2</sup><sup>_<_0),so</sup> _m_<sup>_∗_</sup> _<_ 0 (negative mass). 

**C. Concept of a Hole** An electron with negative effective mass at the top of a valence band accelerates in a direction **opposite** to an applied electric field. Physically, this state with one missing electron is modeled as a positively charged particle called a **hole** with positive charge + _e_ and positive effective mass _m_<sup>_∗_</sup> _h_<sup>=</sup><sup>_−m_</sup> _e_<sup>_∗_.</sup> 

Notes 

3 

**D. Density-of-States Mass vs. Conductivity Mass** For anisotropic semiconductors (e.g., Silicon with ellipsoidal constant-energy surfaces characterized by longitudinal mass _ml_ and transverse mass _mt_ ): 

- **Density-of-States Effective Mass (** _m_<sup>_∗_</sup> _dn_<sup>**):**Used for calculating total carrier pop-</sup> ulations ( _Nc, Nv_ ): 

   - _m_<sup>_∗_</sup> _dn_<sup>= 62/3(</sup><sup>_mlm_2</sup> _t_<sup>)1/3</sup> ( _≈_ 1 _._ 08 _m_ 0 for Si) 



<!-- Start of picture text -->
• Conductivity Effective Mass ( m ∗ cn ): Used for transport, drift, and mobility<br>( µ  =  eτ / m ∗ cn ):<br>1 = 1 + 2 = ⇒ m ∗ cn = 3 mlmt ( ≈ 0 . 26 m 0 for Si)<br>m ∗ cn 3 ( m 1 l mt ) mt  + 2 ml<br><!-- End of picture text -->

## **3. Semiconductor Carrier Statistics & Mass Action Law** 

**A. Equilibrium Carrier Concentrations** Under non-degenerate conditions (Fermi level _EF_ lies inside the band gap at least 3 _kBT_ away from band edges), the Fermi-Dirac distribution simplifies to Maxwell-Boltzmann statistics: 

- **Conduction Band Electrons (** _n_ 0 **):** 



<!-- Start of picture text -->
e kBT<br>n 0 =  Nce − ( Ec−EF  )/ kBT where Nc = 2<br>h 2<br>( 2 πm∗ )3/2<br><!-- End of picture text -->

- **Valence Band Holes (** _p_ 0 **):** 



<!-- Start of picture text -->
h kBT<br>p 0 =  Nve − ( EF −Ev )/ kBT where Nv = 2<br>h 2<br>( 2 πm∗ )3/2<br><!-- End of picture text -->

**B. Intrinsic Carrier Concentration (** _ni_ **) & Law of Mass Action** Multiplying _n_ 0 and _p_ 0 causes the _EF_ term to cancel completely, proving the **Law of Mass Action** : 



<!-- Start of picture text -->
n 0 p 0 =  n 2 i =  NcNve−Eg / kBT<br><!-- End of picture text -->



<!-- Start of picture text -->
ni ( T ) = √ NcNve − Eg / 2kBT =  2 ( m ∗ e m h ∗ ) 3 / 4e − Eg / 2kBT ∝ T3 / 2e − Eg / 2kBT<br>h 2<br>( 2 π kBT ) 3 / 2<br><!-- End of picture text -->

_(GATE Trap: Note the factor of 2 in e_<sup>_−Eg_/</sup><sup>**2**</sup><sup>_kBT_</sup> _for ni, whereas the product n_ 0 _p_ 0 = _n_<sup>2</sup> _i_<sup>_has_</sup> _e_<sup>_−Eg_/</sup><sup>_kBT_</sup> _)._ 

**C. Fermi Level Positioning (** _EF_ **)** 

1. **Intrinsic Semiconductor (** _n_ 0 = _p_ 0 = _ni_ **):** 



<!-- Start of picture text -->
h<br>EFi = Ec  +  Ev + 3<br>2 4 kBT ln ( mm∗ ∗ e )<br><!-- End of picture text -->

At _T_ = 0 K (or if _m_<sup>_∗_</sup> _e_<sup>=</sup><sup>_m∗_</sup> _h_<sup>),</sup><sup>_EFi_sits</sup><sup>**exactlyatthemid-bandgap**.</sup> 

Notes 

4 

2. **Extrinsic N-type Semiconductor (Donor Doping** _Nd ≫ ni_ **):** 



<!-- Start of picture text -->
n 0 ≈ Nd, p 0 ≈ n i 2<br>Nd<br>EF =  Ec − kBT ln = ⇒ EF − EFi =  kBT ln (shifts UP toward Ec )<br>( NNdc ) ( Nnid )<br><!-- End of picture text -->

3. **Extrinsic P-type Semiconductor (Acceptor Doping** _Na ≫ ni_ **):** 



<!-- Start of picture text -->
i<br>p 0 ≈ Na, n 0 ≈ n 2<br>Na<br>EF =  Ev + kBT ln = ⇒ EFi−EF =  kBT ln (shifts DOWN toward Ev )<br>( NNav ) ( Nnia )<br><!-- End of picture text -->

## **4. Carrier Transport & Hall Effect** 

**A. Drift & Diffusion Current Densities** Total current in a semiconductor consists of both drift (electric field driven) and diffusion (concentration gradient driven) components: 



<!-- Start of picture text -->
J total =  J drift +  J diff<br>dn<br>Jn =  enµeE  +  eDn (Electrons)<br>dx<br>dp<br>Jp =  epµhE − eDp (Holes)<br>dx<br><!-- End of picture text -->

**B. The Einstein Relation** At thermal equilibrium under a non-uniform doping field, drift and diffusion balance out, deriving the **Einstein Relation** : 



<!-- Start of picture text -->
Dn = Dp = kBT =  Vt ( ≈ 25 . 9 mV at 300 K)<br>µe µh e<br><!-- End of picture text -->

**C. Hall Effect** When a current _Ix_ flows along _x_ in a magnetic field _Bz_ along _z_ , a transverse voltage _VH_ develops along _y_ : 



<!-- Start of picture text -->
VH = IxBz and RH = Ey = 1<br>qndd JxBz qn<br>• N-type Semiconductor: RH =  − ne 1 (Negative VH ).<br>• P-type Semiconductor: RH = + pe 1 (Positive VH ).<br>• Two-Carrier System (Intrinsic / Mixed):<br><!-- End of picture text -->



<!-- Start of picture text -->
p − nb 2<br>RH = 1 where b  = µe<br>e ( p  +  nb ) 2 µh<br><!-- End of picture text -->

_(Notice that if p_ = _nb_<sup>2</sup> _, RH_ = 0 _!)_ 

Notes 

5 

## **Summary Table of Crucial GATE Formulas** 

|Topic|Primary Formula|Key Notes / Traps|
|---|---|---|
|**Effective Mass**|_m_<sup>_∗_</sup>=¯_h_<sup>2</sup>/<br>~~(~~<br>_d_<sup>2</sup>_E_<br>_dk_<sup>2</sup><br>~~)~~|_m_<sup>_∗_</sup>_<_0 at top of band (hole).|
|**Mass Action Law**|_n_0_p_0 =_n_<sup>2</sup><br>_i_ <sup>=</sup><sup>_NcNve−Eg_/</sup><sup>_kBT_</sup>|Product _n_0_p_0 is independent<br>of doping.|
|**Intrinsic Density**|_ni ∝T_ <sup>3/2</sup>_e_<sup>_−Eg_/2</sup><sup>_kBT_</sup>|Don’t forget 2_kBT_ in the<br>exponent!|
|**Einstein Relation**|_D_/_µ_=_kBT_/_e ≈_25_._9 mV|Relates diffusion constant to<br>mobility.|
|**Single-Carrier** _RH_|_RH_ =<br>1<br>_qn_|Sign of _RH_ gives charge<br>carrier type.|



Shall we finish our roadmap with **Module 5: Dielectrics, Magnetism & Superconductivity** (covering polarizability, Clausius-Mossotti, Dia/Para/Ferromagnetism, London equations, and BCS theory)? 

