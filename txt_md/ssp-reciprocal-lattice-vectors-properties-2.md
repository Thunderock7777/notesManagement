<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-reciprocal-lattice-vectors-properties-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Welcome to **Module 2: Reciprocal Lattice & Wave Diffraction** ! 

In real space, crystal lattices can be complex to visualize when studying wave propagation, X-ray scattering, or electron bands. The **Reciprocal Lattice** transforms these real-space periodicities into **momentum space (** _k_ **-space)** , where every set of parallel planes in the direct lattice maps onto a **single point** . 

## **1. Reciprocal Lattice Vectors & Properties** 

**Definition of Primitive Reciprocal Vectors** Given direct lattice primitive vectors _a_ 1 _,⃗a_ 2 _,⃗a_ 3, the primitive vectors of the reciprocal lattice _⃗b_ 1 _,⃗b_ 2 _,⃗b_ 3 are defined in solid-state physics using the 2 _π_ **convention** : 



<!-- Start of picture text -->
a 2  ×⃗a 3 a 3  ×⃗a 1 a 1  ×⃗a 2<br>b 1 = 2 π⃗⃗a 1  ·  ( ⃗a 2  ×⃗a 3) ,⃗ b 2 = 2 π⃗⃗a 1  ·  ( ⃗a 2  ×⃗a 3) ,⃗ b 3 = 2 π⃗⃗a 1  ·  ( ⃗a 2  ×⃗a 3)<br><!-- End of picture text -->

This definition enforces the fundamental orthonormality relation: 



<!-- Start of picture text -->
ai ·⃗bj = 2 πδij<br><!-- End of picture text -->

**General Reciprocal Lattice Vector (** _⃗Ghkl_ **)** A general translation vector in the reciprocal lattice is specified by the integers ( _h, k, l_ ) corresponding to the Miller indices: 



<!-- Start of picture text -->
Ghkl =  h⃗b 1 +  k⃗b 2 +  l⃗b 3<br><!-- End of picture text -->

## **Fundamental Physical Relations** 

1. **Orthogonality:** The reciprocal vector _⃗Ghkl_ is strictly **perpendicular** to the realspace crystal plane ( _hkl_ ). 

2. **Interplanar Spacing:** The magnitude _|⃗Ghkl|_ is inversely proportional to the interplanar spacing _dhkl_ : 



<!-- Start of picture text -->
2 π<br>dhkl =<br>|⃗Ghkl|<br><!-- End of picture text -->

3. **Unit Cell Volume Relationship:** If _Vc_ = _|⃗a_ 1 _·_ ( _⃗a_ 2 _×⃗a_ 3) _|_ is the volume of the direct primitive cell, the volume of the reciprocal primitive cell _Vr_ is: 



<!-- Start of picture text -->
Vr =  |⃗b 1  ·  ( ⃗b 2  ×⃗b 3) |  = (2 π )3<br>Vc<br><!-- End of picture text -->

Notes 

2 

## **Reciprocal Transformations of Common Lattices** 

- **Simple Cubic (SC):** Self-reciprocal (a SC lattice of side _a_ transforms to a SC lattice of side<sup><u>2</u></sup> _a_<sup>_<u>π</u>_).</sup> 

- • **Body-Centered Cubic (BCC):** The reciprocal lattice of a BCC lattice is a **FaceCentered Cubic (FCC)** lattice. 

- **Face-Centered Cubic (FCC):** The reciprocal lattice of an FCC lattice is a **BodyCentered Cubic (BCC)** lattice. 

## **2. Equivalence of Diffraction Conditions** 

X-ray, neutron, or electron diffraction from a crystal can be formulated in three mathematically equivalent ways: 



<!-- Start of picture text -->
[Real Space] [Momentum Space]<br>Bragg's Law Laue Condition<br>2d sin( θ ) = n λ <=============> ∆k = k_f - k_i = G<br><!-- End of picture text -->

**A. Bragg’s Law (Real Space)** Reflections from parallel atomic planes spaced _dhkl_ apart constructively interfere when the optical path difference is an integer number of wavelengths: 



<!-- Start of picture text -->
2 dhkl  sin  θ =  nλ<br><!-- End of picture text -->

_(In modern notation, absorbing n into the indices yields_ 2 _d_ sin _θ_ = _λ)._ 

**B. Laue Condition (Vector Form)** Diffraction occurs when the scattering vector ∆ _⃗k_ = _⃗kf −⃗ki_ (the momentum transfer) equals a reciprocal lattice vector _⃗G_ : 



<!-- Start of picture text -->
∆ ⃗k = ⃗G<br><!-- End of picture text -->

**C. Vector / Elastic Scattering Condition** For elastic scattering ( _|⃗kf |_ = _|⃗ki|_ = _k_ = <u>2</u> _λπ_<sup>),squaringtheLauecondition</sup><sup>_⃗kf_=</sup><sup>_⃗ki_+</sup><sup>_⃗G_yields:</sup> 



<!-- Start of picture text -->
2 ⃗k ·⃗G  +  G 2 = 0 or 2 ⃗k ·⃗G  =  G 2<br><!-- End of picture text -->

## **3. Ewald Sphere & Brillouin Zones** 

**Ewald Sphere Construction** The **Ewald Sphere** provides a geometric visualization of the diffraction condition in reciprocal space: 

1. Draw the incident wavevector _⃗k_ (length<sup><u>2</u></sup> _λ_<sup>_<u>π</u>_)terminatingattheoriginofreciprocal</sup> space. 

2. Construct a sphere of radius _k_ =<sup><u>2</u></sup> _λ_<sup>_<u>π</u>_centeredatthestartof</sup><sup>_⃗k_.</sup> 

3. **Diffraction condition:** A diffracted beam is generated **only if the sphere intersects another reciprocal lattice point** . 

Notes 

3 

**First Brillouin Zone (1st BZ)** Dividing the vector diffraction condition 2 _⃗k ·⃗G_ = _G_<sup>2</sup> by 4 gives: 



<!-- Start of picture text -->
2<br>1<br>k · 2 ⃗ G = 2 ⃗ G<br>� 1 � ���� ����<br><!-- End of picture text -->

- **Definition:** This is the equation of a plane that **perpendicularly bisects** the reciprocal lattice vector _⃗G_ . 

- The **First Brillouin Zone** is defined as the **Wigner-Seitz primitive cell of the reciprocal lattice** . 

- **Physical Significance:** Electron or photon waves whose wavevectors _⃗k_ touch the boundary of the 1st BZ undergo Bragg reflection, creating **standing waves** and opening up **energy band gaps** . 

## **4. Structure Factor (** _Shkl_ **) & Systematic Extinctions** 

While the geometry of the Bravais lattice determines the _directions_ of allowed diffracted beams, the distribution of atoms inside the unit cell (the **basis** ) determines the _intensity_ . 

**Structure Factor Formula** For a unit cell containing _N_ atoms at fractional coordinates ( _xj, yj, zj_ ) with atomic form factors _fj_ : 



<!-- Start of picture text -->
N<br>Shkl = � fj  exp [ − 2 πi ( hxj +  kyj +  lzj )]<br>j =1<br><!-- End of picture text -->

The diffracted intensity is proportional to the square of the magnitude: _Ihkl ∝|Shkl|_<sup>2</sup> . When _Shkl_ = 0, that specific reflection is **systematically extinguished (forbidden)** . 

**Selection Rules for Cubic Lattices (Crucial for GATE)** 

|Crystal<br>Structure|Basis Atom<br>Positions<br>(_xj, yj, zj_)|Structure Factor<br>_Shkl_|Allowed<br>Reflections<br>(_Shkl̸_ = 0)|Forbidden<br>Reflections<br>(_Shkl_ = 0)|
|---|---|---|---|---|
|**Simple Cubic**<br>**(SC)**|(0_,_0_,_0)|_f_|**All** (_hkl_)<br>**allowed**|None|
|**Body-**<br>**Centered**|(0_,_0_,_0)_,_( <sup>1</sup><br>2<sup>_,_</sup> <sup>1</sup><br>2<sup>_,_</sup> <sup>1</sup><br>2<sup>)</sup>|_f_<br>�<br>1 +_e_<sup>_−πi_(</sup><sup>_h_+</sup><sup>_k_+</sup><sup>_l_)�</sup>|_h_+_k_+_l_=**even**|_h_+_k_+_l_=odd<br>(e.g. 100, 111,|
|**Cubic (BCC)**||||221)|
|**Face-Centered**<br>**Cubic (FCC)**|(0_,_0_,_0)_,_( <sup>1</sup><br>2<sup>_,_</sup> <sup>1</sup><br>2<sup>_,_ 0)</sup><sup>_,_ (</sup>|<sup>1</sup><br>2<sup>_,_ 0</sup><sup>_,_</sup> <sup>1</sup><br>2<sup>)</sup><sup>_,_ (0</sup><sup>_,_</sup> <sup>1</sup><br>2<sup>_,_</sup> <sup>1</sup><br>2<sup>)</sup><br>_f_<br>�<br>~~1~~+_e_<sup>_−πi_(</sup><sup>_h_+</sup><sup>_k_) </sup>+|_e_<sup>_−πi_(</sup><sup>_k_+</sup><sup>_l_) </sup>+_e_<sup>_−πi_(</sup><sup>_l_+</sup><sup>_h_)</sup><br>**Unmixed** _h, k, l_<br>(all even or all<br>odd)|<sup>�</sup><br>Mixed indices<br>(e.g. 110, 210,<br>100)|
|**Diamond**<br>**Cubic (DC)**|FCC positions +<br>4 tetrahedrally<br>displaced atoms|_f_<br>�<br>1 +_e_<sup>_−iπ_</sup><br>2 <sup>(</sup><sup>_h_+</sup><sup>_k_+</sup><sup>_l_)�</sup><br>_S_FCC|_×_<br>**All odd OR all**<br>**even with**<br>_h_+_k_+_l_= 4_n_|All mixed OR<br>all even with<br>_h_+_k_+_l̸_= 4_n_<br>(e.g. 200)|



Notes 

4 

## **Crucial GATE Traps to Avoid** 

1. **The** 2 _π_ **Factor in Reciprocal Lattices:** Solid-state physics textbooks (like Kittel) include 2 _π_ in _⃗bi_ , making _⃗ai ·⃗bj_ = 2 _πδij_ and _d_ = _|_<sup><u>2</u></sup> _⃗G_<sup>_<u>π</u>_</sup> _|_<sup>.Crystallographytextsomit2</sup><sup>_π_.</sup> **Always use the** 2 _π_ **convention for GATE Physics** . 

2. **Bragg Angle (** _θ_ **):** _θ_ in 2 _d_ sin _θ_ = _λ_ is the **glancing angle** measured relative to the crystal plane surface, **not** the angle relative to the surface normal. 

3. **BCC vs. FCC Selection Rule Confusion:** In BCC, (110) is allowed (1+1+0 = 2, even). In FCC, (110) is forbidden because 1 _,_ 1 _,_ 0 are mixed. 

Would you like to try a classic GATE numerical problem on determining allowed X- ray diffraction peaks and lattice parameters, or shall we proceed to **Module 3: Free Electron Theory & Lattice Vibrations (Phonons)** ? 

