<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-first-brillouin-zone-construction-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Welcome to **Module 3: Free Electron Theory & Lattice Vibrations (Phonons)** . 

This module bridges microscopic quantum mechanics with macroscopic thermal and transport properties of solids. It is one of the highest-yield scoring sections in GATE Physics. 

## **1. Quantum Free Electron Theory (Sommerfeld Model)** 

While the classical Drude-Lorentz model treated electrons as a Maxwell-Boltzmann gas, Arnold Sommerfeld applied **quantum mechanics and Fermi-Dirac statistics** to conduction electrons trapped in a 3D potential box. 

**A. Fundamental Fermi Parameters (3D Bulk Metal)** At _T_ = 0 K, electrons fill energy levels up to a maximum cutoff energy called the **Fermi Energy (** _EF_ **)** : 

1. **Fermi Wavevector (** _kF_ **):** 



<!-- Start of picture text -->
kF = �3 π 2 n �1/3<br><!-- End of picture text -->

_(where n_ = _N_ / _V is the free electron concentration)._ 

2. **Fermi Energy (** _EF_ **):** 



<!-- Start of picture text -->
EF = h ¯2 k F 2 �3 π 2 n �2/3<br>2 m = 2 h ¯ m 2<br><!-- End of picture text -->

3. **Fermi Velocity (** _vF_ **) & Fermi Temperature (** _TF_ **):** 



<!-- Start of picture text -->
vF = hk ¯ F TF = EF<br>m , kB<br><!-- End of picture text -->

**B. Density of States** _D_ ( _E_ ) **& Dimensionality (Major GATE Trap!)** The **Density of States** _D_ ( _E_ ) is defined as the number of available quantum states per unit energy range per unit volume. Its functional form depends critically on the spatial dimension _d_ : 

Notes 

2 

|||Density of States|Scaling|Fermi Energy|
|---|---|---|---|---|
|Dimension (_d_)|Physical System|_D_(_E_)|Dependency|_EF_(_n_)|
|**3D**|Bulk Metal /<br>Crystal|_D_3_D_(_E_) =<br>1<br>2_π_<sup>2</sup><br>�<br>2_m_<br>¯_h_<sup>2</sup><br>�3/2 _~~√~~_<br>_E_|_D_(_E_)_∝E_<sup>1/2</sup>|_EF ∝n_<sup>2/3</sup>|
|**2D**|Quantum Well /<br>2DEG|_D_2_D_(_E_) =<br>_m_<br>_π_¯_h_<sup>2</sup>|_D_(_E_)_∝E_<sup>0</sup><br>**(Constant)**|_EF ∝n_<sup>1</sup><br>2_D_|
|**1D**|Quantum Wire /<br>Nanowire|_D_1_D_(_E_) =<br>_~~√~~_<br>2_m_<br>_π_¯_h_<br>_~~√~~_<br>_E_|_D_(_E_)_∝E_<sup>_−_1/2</sup><br>**(Diverges)**|_EF ∝n_<sup>2</sup><br>1_D_|



**C. Mean Energy & Electronic Specific Heat (** _Cel_ **)** 

- **Average Energy at** _T_ = 0 **K (3D):** 



<!-- Start of picture text -->
E ¯0 = 3 5 EF = ⇒ U 0 = 5 3 NEF<br><!-- End of picture text -->

- **Electronic Specific Heat (** _Cel_ **):** Classical theory incorrectly predicted _Cel_ = <u>32</u><sup>_R_.Quantummechanicsshowsthat</sup><sup>**onlyelectronswithin**</sup><sup>_kBT_</sup><sup>**oftheFermi**</sup> **surface** can be excited thermally: 



<!-- Start of picture text -->
B D ( EF )<br>Cel =  γT = T ∝ T<br>� π 2 k 2 3 �<br><!-- End of picture text -->

## **2. Lattice Vibrations & Phonons** 

Quantized elastic sound waves propagating through the crystal lattice are called **phonons** (bosons with zero chemical potential, _µ_ = 0). 

**A. 1D Monatomic Chain Dispersion Relation** For a line of identical atoms of mass _M_ separated by distance _a_ with spring constant _β_ : 



<!-- Start of picture text -->
4 β<br>ω ( k ) =<br>� M ����sin � ka 2 �����<br><!-- End of picture text -->

- **Maximum Frequency (Zone Boundary** _k_ = _±π_ / _a_ **):** _ω_ max = ~~�~~ 4 _Mβ_<sup>.</sup> _<u>β</u>_ 

- • **Long Wavelength Limit (** _k →_ 0 **):** _ω ≈_ � _a_ ~~�~~ _M_ <u>�</u> _k_ = _vsk_ (linear acoustic regime). • **Group Velocity (** _vg_ =<sup>_<u>dω</u>_</sup> _dk_<sup>**):**AttheBrillouinZoneboundary(</sup><sup>_k_=</sup><sup>_π_/</sup><sup>_a_),</sup><sup>_vg_= 0</sup><sup>_→_</sup> forms a **standing wave** . 

**B. 1D Diatomic Chain (Alternating Masses** _M_ 1 _< M_ 2 **)** When two different masses exist in the unit cell, the dispersion relation splits into **two branches** : 

1. **Acoustic Branch (Lower):** 

Notes 

3 

- At _k_ = 0 = _⇒ ω_ = 0. 



<!-- Start of picture text -->
• At k =  π / a = ⇒ ω ac = � M 2 β 2 (heavy mass vibrates, light mass rests).<br>2. Optical Branch (Upper):<br>• At k = 0 = ⇒ ω opt = 2 β � M 11 + M 12 � (adjacent atoms move out of phase).<br>�<br>• At k =  π / a = ⇒ ω opt = � M 2 β 1 (light mass vibrates, heavy mass rests).<br>3. Forbidden Band Gap: No elastic lattice waves can propagate in the frequency<br>gap between the branches:<br>2 β 2 β<br>< ω <<br>� M 2 � M 1<br><!-- End of picture text -->

**C. General Branch Counting Rule (3D Crystals)** For a 3D unit cell containing _p_ **atoms in the primitive basis** : 

- **Total Modes of Vibration:** 3 _p_ 

- **Acoustic Branches:** Always 3 (1 Longitudinal Acoustic + 2 Transverse Acoustic). 

- **Optical Branches:** Always 3 _p −_ 3. 

_(Example: For NaCl, p_ = 2 = _⇒_ 3 _Acoustic_ + 3 _Optical_ = 6 _total branches)._ 

## **3. Heat Capacity Models for Solids** 

**A. Einstein Model (Independent Oscillators)** Assumes all 3 _N_ lattice modes vibrate at a single fixed frequency _ωE_ : 



<!-- Start of picture text -->
e θE / T<br>CV = 3 R<br>T<br>� θE �2 ( e θE / T − 1) 2<br><!-- End of picture text -->

- **High** _T ≫ θE_ **:** _CV →_ 3 _R_ (Dulong-Petit Law). 

- **Low** _T ≪ θE_ **:** _CV ∝ e_<sup>_−θE_/</sup><sup>_T_</sup> _→_ 0. 

- **Failure:** It drops off **too rapidly** at low temperatures because it ignores longwavelength acoustic modes. 

**B. Debye Model (Elastic Continuum &** _T_<sup>3</sup> **Law)** Models the lattice as a continuous elastic medium with _D_ ( _ω_ ) = 2<sup><u>3</u></sup> _π_<sup>_<u>V ω</u>_2</sup> _v_<sup>2</sup> _s_<sup>3uptoacutofffrequency</sup><sup>_ωD_:</sup> 

• **Low Temperature Limit (** _T ≪ θD_ **):** 



<!-- Start of picture text -->
CV = 12 π 4 NkB = ⇒ Clat ∝ T 3<br>5 � θTD �3<br><!-- End of picture text -->

**C. Total Heat Capacity of Metals at Low Temperatures** In metals, total heat capacity is the sum of electronic and lattice (phonon) contributions: 

_C_ total = _Cel_ + _Clat_ = _γT_ + _AT_<sup>3</sup> 

Notes 

4 

To separate these experimentally, rewrite the equation as: 

_C T_<sup>=</sup><sup>_γ_+</sup><sup>_AT_2</sup> 

- A plot of<sup>_<u>C</u>_</sup> _T_<sup>**vs.**</sup><sup>_T_2yieldsastraightlinewhere:</sup> 

   - **Y-intercept =** _γ_ (Sommerfeld coefficient _∝ D_ ( _EF_ )). 

   - **Slope =** _A_ (Debye coefficient _∝ θ_ <u>1</u> _D_<sup>3).</sup> 

## **Crucial GATE Exam Traps to Watch For** 

1. **Dimensionality of** _D_ ( _E_ ) **:** Always read whether the problem specifies 3D bulk, 2D quantum well, or 1D quantum wire. 

2. **Debye** _T_<sup>3</sup> **vs.** _T_<sup>_d_</sup> **scaling:** In a _d_ -dimensional solid, the Debye heat capacity scales as _CV ∝ T_<sup>_d_</sup> . _(e.g., for a 2D sheet like graphene, Clat ∝ T_<sup>2</sup> _; for 1D, Clat ∝ T_<sup>1</sup> _)_ . 

3. **Phase vs. Group Velocity at** _k_ = _π_ / _a_ **:** Phase velocity _vp_ = _ω_ / _k̸_ = 0, but Group velocity _vg_ = _dω_ / _dk_ = 0. Transport and energy flow depend strictly on _vg_ . 

Next, shall we test your understanding with a couple of previous GATE numerical questions on **Fermi parameters** and **Debye heat capacity plots** , or move directly to **Module 4: Band Theory & Semiconductors** ? 

