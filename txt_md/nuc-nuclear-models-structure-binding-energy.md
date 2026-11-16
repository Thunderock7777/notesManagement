<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: nuc-nuclear-models-structure-binding-energy.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

GATE PHYSICS 

NUCLEAR PHYSICS & MODELS 

# **GATE PHYSICS STUDY NOTES Nuclear Physics, Models, and Structure** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**|**Nuclear Binding Energy and the Liquid Drop Model**|**2**|
|---|---|---|
|**2**|**Nuclear Electric and Magnetic Moments**|**6**|
|**3**|**The Nuclear Shell Model**|**9**|



1 

GATE PHYSICS 

NUCLEAR PHYSICS & MODELS 

## **1 Nuclear Binding Energy and the Liquid Drop Model** 

### **1. Core Theory** 

**Nuclear Binding Energy** is the energy required to disassemble a atomic nucleus completely into its constituent free, isolated protons and neutrons. Physically, it is the energy equivalent of the **mass defect**, which is the difference between the sum of the individual rest masses of the nucleons and the actual rest mass of the bound nucleus. The nuclear force holding nucleons together is an extremely strong, short-range, saturating interaction. 

The **Liquid Drop Model (LDM)** is a phenomenological model proposed by George Gamow and developed by Carl Friedrich von Weizs¨acker. It treats the atomic nucleus as a droplet of an incompressible, homogeneous, high-density quantum fluid. The nucleons are analogous to molecules in a liquid, experiencing short-range attractive forces that lead to a constant density inside the nucleus and a well-defined surface boundary. 

This model successfully explains the macroscopic bulk properties of nuclei, such as the constant binding energy per nucleon ( _B/A ≈_ 8 MeV) across most of the periodic table, the spherical shape of ground-state nuclei, and the physics of nuclear fission. 

### **2. Mathematical Framework** 

- **Mass Defect (** ∆ _m_ **) and Binding Energy (** _B_ **):** 



<!-- Start of picture text -->
∆ m  =  Zmp  + ( A − Z ) mn − M ( A, Z ) (1)<br><!-- End of picture text -->



<!-- Start of picture text -->
B ( A, Z ) = ∆ m · c 2 = [ Zmp  + ( A − Z ) mn − M ( A, Z )]  c 2 (2)<br><!-- End of picture text -->

where: 

-  _Z_ is the atomic number (number of protons). 

-  _A_ is the mass number (total number of nucleons). 

-  _mp ≈_ 1 _._ 007276 u is the proton rest mass. 

-  _mn ≈_ 1 _._ 008665 u is the neutron rest mass. 

-  _M_ ( _A, Z_ ) is the rest mass of the bound nucleus. 

-  _c_<sup>2</sup> _≈_ 931 _._ 5 MeV/u is the mass-to-energy conversion factor. 

- **The Semi-Empirical Mass Formula (SEMF - Weizs¨acker Formula):** 



<!-- Start of picture text -->
Z ( Z − 1) ( A − 2 Z ) 2<br>B ( A, Z ) =  avA − asA 2 / 3 − ac − a sym +  δ ( A, Z ) (3)<br>A 1 / 3 A<br><!-- End of picture text -->

where each term represents a distinct physical contribution: 

1. **Volume Term (** _avA_ **):** Represents the dominant attractive, short-range strong nuclear force. Since each nucleon only interacts with its nearest neighbors (saturation), the energy is directly proportional to the volume, and hence to _A_ . ( _av ≈_ 15 _._ 5 _−_ 15 _._ 8 MeV). 

2. **Surface Term (** _−asA_<sup>2</sup><sup>_/_3</sup> **):** Corrects the volume term for nucleons located at the surface, which have fewer neighbors to bind with (analogous to surface tension in a liquid drop). Since surface area scales as _R_<sup>2</sup> _∝ A_<sup>2</sup><sup>_/_3</sup> , this term reduces the binding energy. ( _as ≈_ 16 _._ 8 _−_ 18 _._ 3 MeV). 

2 

GATE PHYSICS 

NUCLEAR PHYSICS & MODELS 

- _Z_ <u>(</u> _Z−_ 1) 

- 3. **Coulomb Term (** _−ac A_<sup>1</sup><sup>_/_3</sup><sup>**):**Representstheelectrostaticrepulsionbetweenprotons.It</sup> is proportional to the number of proton pairs _Z_ ( _Z −_ 1) _/_ 2 and inversely proportional to the radius _R ∝ A_<sup>1</sup><sup>_/_3</sup> . ( _ac ≈_ 0 _._ 71 _−_ 0 _._ 72 MeV). 

- <u>(</u> _A−_ 2 _Z_ <u>)</u><sup>2</sup> 

- 4. **Asymmetry Term (** _−a_ **sym** _A_ **):** Accounts for the Pauli exclusion principle. When _N̸_ = _Z_ , neutrons are forced to occupy higher-energy quantum states, which reduces the overall binding energy of the system. ( _a_ sym _≈_ 23 MeV). 

5. **Pairing Term (** _δ_ ( _A, Z_ ) **):** Reflects the quantum mechanical spin-pairing effect, where identical nucleons form stable pairs with zero total angular momentum: 



<!-- Start of picture text -->
+ apA − 3 / 4 for even-even nuclei (Z even, N even)<br>δ ( A, Z ) = 0 for odd-A nuclei (A odd) (4)<br><br> −apA − 3 / 4 for odd-odd nuclei (Z odd, N odd)<br><!-- End of picture text -->

where _ap ≈_ 33 _−_ 34 MeV (or written as _apA_<sup>_−_1</sup><sup>_/_2</sup> with _ap ≈_ 12 MeV). 

* **Nuclear Fission Energy Criterion:** The energetic allowedness of spontaneous fission is determined by comparing the surface and Coulomb terms. Fission is energetically favorable when: 



<!-- Start of picture text -->
Z 2<br>≈ 45  − 50 (5)<br>A ≥ 2 a a c s<br><!-- End of picture text -->

### **3. Conservation Laws & Symmetries** 

* **Governing Forces:** The LDM and SEMF are governed by the interplay of the **Strong Nuclear Force** (Volume and Surface terms) and the **Electromagnetic Force** (Coulomb term). * **Conserved Quantities:** 

-  **Baryon Number (** _A_ **):** The total number of nucleons remains strictly conserved in all stable and decaying systems. 

-  **Electric Charge (** _Z_ **):** Total charge is strictly conserved. 

-  **Parity (** Π **):** Strong and electromagnetic interactions strictly preserve spatial parity. 

-  **Isospin (** _I_ **):** Strong nuclear interactions possess approximate isospin symmetry (charge independence of the nuclear force), which is explicitly broken by the electromagnetic Coulomb term. 

### **4. Derivation Milestones** 

1. **Coulomb Self-Energy of a Spherical Charge:** Model the nucleus as a sphere of radius _R_ = _r_ 0 _A_<sup>1</sup><sup>_/_3</sup> with a uniform charge density _Q_ = _Ze_ . The classical electrostatic potential energy is: 



<!-- Start of picture text -->
Ec = 3 1 Q 2 3 e 2 Z 2 (6)<br>5 4 πϵ 0 R = 20 πϵ 0 r 0 A 1 / 3<br><!-- End of picture text -->

Replacing _Z_<sup>2</sup> with _Z_ ( _Z −_ 1) to exclude the self-interaction of a single proton yields the Coulomb <u>3</u> _<u>e</u>_<sup>2</sup> coefficient _ac_ = 20 _πϵ_ 0 _r_ 0<sup>_≈_0</sup><sup>_._72MeV.2.**PauliAsymmetryEnergy:**Modelthenucleusastwo</sup> independent Fermi gases (protons and neutrons) in a potential well. The Fermi energy of a species scales as _EF ∝_ ( _N/V_ )<sup>2</sup><sup>_/_3</sup> . Integrating the total kinetic energy of _Z_ protons and _N_ neutrons up to 

3 

GATE PHYSICS 

NUCLEAR PHYSICS & MODELS 

their respective Fermi levels and performing a Taylor series expansion about the symmetric point _N_ = _Z_ = _A/_ 2 yields: 



<!-- Start of picture text -->
E kin ≈ EF 0 A  + 5 ( N − Z ) 2 (7)<br>� 9 A �<br><!-- End of picture text -->

<u>(</u> _A−_ 2 _Z_ <u>)</u><sup>2</sup> This mathematically derives the _A_ -dependence of the asymmetry term: _E_ asym _∝ A_ . 3. **Parabola of Stable Isobars:** Express the atomic mass _M_ ( _A, Z_ ) in terms of binding energy using the SEMF. For a constant _A_ , _M_ ( _A, Z_ ) is a quadratic function of _Z_ : 



<!-- Start of picture text -->
M ( A, Z ) =  ZM ( 1 H) + ( A − Z ) mn − B ( A, Z ) /c 2 ≡ αZ 2 +  βZ  +  γ (8)<br><!-- End of picture text -->

Differentiating with respect to _Z_ and setting _∂M/∂Z_ = 0 yields the **most stable isobar** ( _Z_ 0) for a given mass number _A_ : 



<!-- Start of picture text -->
A<br>Z 0 = 2 + 2 aa sym c A 2 / 3 (9)<br><!-- End of picture text -->

### **5. Problem-Solving Algorithm** 

#### **Finding the Most Stable Isobar and Binding Energies** 

1. **Calculate** _Z_ 0 **for a Given** _A_ **:** Use the derived formula: 



<!-- Start of picture text -->
A<br>Z 0 = (10)<br>2 + 0 . 015 A 2 / 3<br><!-- End of picture text -->

where we have substituted the standard parameters _ac ≈_ 0 _._ 72 MeV and _a_ sym _≈_ 23 MeV. Round _Z_ 0 to the nearest integer to find the most stable element. 

2. **Calculate Binding Energy per Nucleon (** _B/A_ **):** Substitute _A_ , _Z_ , and the provided SEMF coefficients directly into Weizs¨acker’s equation. Remember to check the pairing term _δ_ : 

   -  If _A_ is odd, _δ_ = 0. 

   -  If _A_ is even, check if _Z_ is even (even-even: add _δ_ ) or odd (odd-odd: subtract _δ_ ). 

3. **Calculate Fission Energy Release (Q-value):** For a symmetric fission reaction _A →_<sup>_<u>A</u>_</sup> 2<sup>+</sup><sup>_<u>A</u>_</sup> 2<sup>:</sup> _Q_ = 2 _B_ ( _A/_ 2 _, Z/_ 2) _− B_ ( _A, Z_ ) (11) 

4 

GATE PHYSICS 

NUCLEAR PHYSICS & MODELS 

### **6. Crucial Pitfalls** 

#### **Liquid Drop and SEMF Traps to Avoid** 

-  **Pairing Term Sign Errors:** The pairing term _δ_ is **positive** (increases binding energy) for even-even nuclei because they are highly stable, and **negative** (decreases binding energy) for odd-odd nuclei. A common mistake is flipping these signs or applying a non-zero _δ_ to odd-A nuclei. 

-  **The** _Z_ ( _Z −_ 1) **vs.** _Z_<sup>2</sup> **Coulomb Approximation:** Some GATE questions approximate the Coulomb term as _Z_<sup>2</sup> _/A_<sup>1</sup><sup>_/_3</sup> instead of _Z_ ( _Z −_ 1) _/A_<sup>1</sup><sup>_/_3</sup> . Carefully inspect the coefficients and form provided in the question. 

-  **Mass Defect Atom vs. Nucleus Mismatch:** When calculating mass defects, ensuring you are consistent. If you use the mass of neutral Hydrogen _M_ (<sup>1</sup> H) instead of the bare proton mass _mp_ , you must use the neutral atomic mass _M_ atom( _A, Z_ ) instead of the nuclear mass _M_ ( _A, Z_ ) to cancel out the electron masses: 



<!-- Start of picture text -->
B ( A, Z ) = � ZM ( 1 H) + ( A − Z ) mn − M atom( A, Z )� c 2 (12)<br><!-- End of picture text -->

### **7. Standard Textbook Systems** 

* **The** _A_ = 125 **Isobaric Chain:** Used to illustrate the stable isobar parabola. Since _A_ is odd, there is a single parabola, and the minimum identifies<sup>125</sup> Te ( _Z_ = 52) as the only stable nucleus, while neighboring<sup>125</sup> Sb ( _Z_ = 51) and<sup>125</sup> I ( _Z_ = 53) are unstable to beta decay. * **The** _A_ = 140 **Isobaric Chain:** Since _A_ is even, the pairing term splits the system into two curves (even-even and odd-odd). This allows for multiple stable isobars (e.g.,<sup>140</sup> Ce and<sup>140</sup> Ba) because transitions must occur in steps of ∆ _Z_ = _±_ 1, forcing the odd-odd intermediates to have higher energy. 

5 

GATE PHYSICS 

NUCLEAR PHYSICS & MODELS 

## **2 Nuclear Electric and Magnetic Moments** 

### **1. Core Theory** 

Nuclear moments describe the electromagnetic spatial charge and current distributions of a nucleus, providing direct physical insight into its shape and internal shell configurations. * **Magnetic Dipole Moment (** **_µ_ ):** Arises from the combined effects of the intrinsic spin magnetic moments of the individual nucleons and the orbital motion of charged protons. The physical origin is the relativistic spin-orbit coupling of the nucleons. * **Electric Quadrupole Moment (** _Q_ **):** Measures the deviation of the nuclear charge distribution from spherical symmetry. * ** _Q_ = 0:** Perfectly spherical charge distribution. * ** _Q >_ 0:** Prolate shape (elongated along the spin axis, like a rugby ball). * ** _Q <_ 0:** Oblate shape (flattened like a pumpkin). 

The existence of large quadrupole moments in heavy nuclei provides strong evidence for collective deformations, showing that the single-particle spherical model is an approximation. 

### **2. Mathematical Framework** 

* **Magnetic Moment Operator (** **_µ_** ˆ **):** 



<!-- Start of picture text -->
A<br>µ ˆ  = � � gl ( i )ˆ l i  +  g s ( i )ˆ s i � µN (13)<br>i =1<br><!-- End of picture text -->

where the **Nuclear Magneton** is defined as _µN_ = 2 _<u>em</u>_ <u>ℏ</u> _p_<sup>_≈_3</sup><sup>_._152</sup><sup>_×_10</sup><sup>_−_8eV/T,andthegyromag-</sup> netic ratios are: 

 For a Proton: _gl_ = 1, _gs ≈_ 5 _._ 5857. 



<!-- Start of picture text -->
 For a Neutron: gl = 0, gs ≈− 3 . 8263.<br><!-- End of picture text -->

* **The Schmidt Limits (Single-Particle Magnetic Moments):** For an odd-A nucleus where the spin is dictated by a single unpaired nucleon with total angular momentum _j_ = _l ±_ 1 _/_ 2: * **For _j_ = _l_ + 1 _/_ 2:** 



<!-- Start of picture text -->
µ  =  jgl  + 1 2 ( gs − gl ) nuclear magnetons (14)<br><!-- End of picture text -->



<!-- Start of picture text -->
* **For j =  l − 1 / 2:**<br><!-- End of picture text -->



<!-- Start of picture text -->
j<br>µ  =  jgl − 2( j  + 1) ( gs − gl ) nuclear magnetons (15)<br><!-- End of picture text -->

* **Electric Quadrupole Moment (** _Q_ **):** The quadrupole moment of a single odd proton in a state _j_ is: 



<!-- Start of picture text -->
Q sp =  − 2 j − 1 (16)<br>2( j  + 1) ⟨r 2 ⟩<br><!-- End of picture text -->

where _⟨r_<sup>2</sup> _⟩≈_ <u>35</u><sup>_R_2isthemean-squarenuclearradius.</sup> For an odd neutron, the single-particle quadrupole moment is theoretically _Q ≈_ 0 (with a tiny correction due to the center-of-mass recoil motion). 

6 

GATE PHYSICS 

NUCLEAR PHYSICS & MODELS 

### **3. Conservation Laws & Symmetries** 

* **Parity Symmetries and Electric Moments:** Under spatial inversion, the electric multipole moments _El_ are non-zero only for even _l_ (e.g., monopole _E_ 0, quadrupole _E_ 2). Thus, all oddorder electric moments (e.g., **electric dipole moment _E_ 1**) are strictly zero for nuclear states of definite parity. * **Time Reversal Symmetries and Magnetic Moments:** Under time reversal, magnetic multipole moments _Ml_ are non-zero only for odd _l_ (e.g., dipole _M_ 1, octupole _M_ 3). Thus, even-order magnetic moments (e.g., **magnetic quadrupole moment _M_ 2**) are strictly zero. * **Spin Restrictions on Moments:** For a nucleus of spin _J_ , multipole moments of order _L_ can exist only if: 



<!-- Start of picture text -->
L ≤ 2 J (17)<br><!-- End of picture text -->

* Consequently, any nucleus with **spin _J_ = 0 is completely spherical** and has no electromagnetic moments ( _Q_ = 0 _, µ_ = 0). * Any nucleus with **spin _J_ = 1 _/_ 2 cannot possess an electric quadrupole moment ( _Q_ = 0)**, though it can have a non-zero magnetic moment. 

### **4. Derivation Milestones** 

1. **Classical Multipole Expansion:** Expand the electrostatic potential _V_ ( **r** ) of a localized charge distribution _ρ_ ( **r**<sup>_′_</sup> ) in Legendre polynomials: 



<!-- Start of picture text -->
1 ρ ( r ′ ) 1 ∞ 1<br>V  ( r ) = 4 πϵ 0 � | r  − r ′ | d 3 r′ = 4 πϵ 0 � r L +1 � ρ ( r ′ )( r ′ ) L PL (cos  θ ′ ) d 3 r ′ (18)<br>L =0<br><!-- End of picture text -->

2. **Isolating the Quadrupole Term ( _L_ = 2):** Define the quadrupole moment along the _z_ -axis as: 



<!-- Start of picture text -->
eQ ≡ ρ ( r ′ )(3 z ′ 2 − ( r ′ ) 2 ) d 3 r ′ (19)<br>�<br><!-- End of picture text -->

3. **Evaluating the Expectation Value:** In quantum mechanics, the nuclear charge density is replaced by the wave function: _ρ_ ( **r** ) = _e|ψJJ_ ( **r** ) _|_<sup>2</sup> . The quadrupole moment is the expectation value of the operator in the state with maximum projection _mJ_ = _J_ : 



<!-- Start of picture text -->
Q  =  ⟨J, mJ =  J| �(3 zi 2 − r i 2) |J, mJ =  J⟩ (20)<br>i<br><!-- End of picture text -->

4. **Wigner-Eckart Projection:** Apply the projection theorem to the magnetic operator **_µ_** ˆ = _gl_<sup>ˆ</sup> **l** + _gs_ ˆ **s** within the subspace of total angular momentum<sup>ˆ</sup> **j** =<sup>ˆ</sup> **l** + ˆ **s** : 



<!-- Start of picture text -->
⟨ µ ˆ  · ˆ j ⟩<br>⟨ µ ˆ ⟩ = j ( j  + 1)ℏ 2 ⟨ ˆ j ⟩ (21)<br><!-- End of picture text -->

Evaluating the dot product<sup>ˆ</sup> **l** _·_<sup>ˆ</sup> **j** and ˆ **s** _·_<sup>ˆ</sup> **j** algebraically using ˆ **s**<sup>2</sup> = (<sup>ˆ</sup> **j** _−_<sup>ˆ</sup> **l** )<sup>2</sup> yields the Schmidt limit equations. 

7 

GATE PHYSICS 

NUCLEAR PHYSICS & MODELS 

### **5. Problem-Solving Algorithm** 

#### **Calculating Single-Particle Magnetic Moments (Schmidt Limits)** 

1. **Identify the Unpaired Nucleon:** Use the shell model to find the orbital ( _l_ ) and total ( _j_ ) angular momentum of the unpaired proton or neutron. 

2. **Select the Gyromagnetic Constants:** 

   -  For a Proton: _gl_ = 1, _gs_ = 5 _._ 586. 

   -  For a Neutron: _gl_ = 0, _gs_ = _−_ 3 _._ 826. 

3. **Apply the Schmidt Equation:** 



<!-- Start of picture text -->
 If j =  l  + 1 / 2:<br>µ  =  jgl  + 2 1 ( gs − gl ) (22)<br><!-- End of picture text -->

-  If _j_ = _l −_ 1 _/_ 2: 



<!-- Start of picture text -->
j<br>µ  =  jgl − 2( j  + 1) ( gs − gl ) (23)<br><!-- End of picture text -->

4. **Compare with Experimental Values:** Note that real nuclear magnetic moments are typically shifted inward toward the center of the Schmidt lines (quenched) due to nuclear polarization and meson exchange currents. 

### **6. Crucial Pitfalls** 

#### **Electromagnetic Moments Traps to Avoid** 

-  **The** _J_ = 1 _/_ 2 **Quadrupole Trap:** Expecting quadrupole splitting for spin-1/2 nuclei. Remember that _Q_ = 0 is strictly required for _J ≤_ 1 _/_ 2. A common exam trap is asking for the quadrupole moment of<sup>1</sup> H or<sup>3</sup> He ( _J_ = 1 _/_ 2); the answer is exactly zero. 

-  **The** _gl_ **values for neutrons:** Forgetting that the neutron is uncharged and thus has _gl_ = 0. Using _gl_ = 1 for a neutron will invalidate the Schmidt calculations. 

-  **Schmidt Formula Indexing:** Accidentally using the formula for _j_ = _l_ + 1 _/_ 2 when the state is _j_ = _l −_ 1 _/_ 2 (e.g., 1 _p_ 1 _/_ 2). 

### **7. Standard Textbook Systems** 

* **The Deuteron (**<sup>2</sup> **H) Ground State:** Has spin _J_ = 1 and parity _π_ = +. It possesses a small, positive quadrupole moment ( _Q_ = +0 _._ 00286 b), which proves that the nuclear force is non-central (possesses a tensor component), mixing a small fraction of the _D_ -wave ( _l_ = 2) into the dominant _S_ -wave ( _l_ = 0) ground state. * **The**<sup>17</sup> **O Nucleus:** Consists of a closed shell plus an odd neutron in the 1 _d_ 5 _/_ 2 state ( _j_ = 5 _/_ 2 _, l_ = 2). The Schmidt limit predicts _µ_ = _−_ 1 _._ 913 _µN_ , which is very close to the experimental value of _−_ 1 _._ 89 _µN_ , making it a classic single-particle system. 

8 

GATE PHYSICS 

NUCLEAR PHYSICS & MODELS 

## **3 The Nuclear Shell Model** 

### **1. Core Theory** 

The **Nuclear Shell Model** is a quantum mechanical model based on the concept that nucleons move independently in a common, spherically symmetric potential well, analogous to the electronic shells of atoms. 

The physical origin of the model is the **mean-field approximation**, where the short-range, highly attractive nucleon-nucleon interactions are averaged into a single central potential _V_ ( _r_ ). However, a simple harmonic oscillator or Woods-Saxon potential fails to reproduce the experimental **Magic Numbers** (2 _,_ 8 _,_ 20 _,_ 28 _,_ 50 _,_ 82 _,_ 126), which are the nuclear analogs of inert gas configurations. 

In 1949, Maria Goeppert Mayer and J. Hans D. Jensen resolved this by proposing a strong, attractive **spin-orbit coupling term** ( **l** _·_ **s** ) of relativistic origin. This coupling splits the states of different total angular momentum _j_ = _l ±_ 1 _/_ 2, pushing the higher- _j_ state down in energy. For large _l_ , this splitting is so large that it shifts states across the principal oscillator shells, naturally generating the magic number gaps. 

### **2. Mathematical Framework** 

* **The Mean-Field Hamiltonian (** _H_<sup>ˆ</sup> **):** 



<!-- Start of picture text -->
H ˆ = � i =1 A � − 2 ℏ m 2 ∇ i 2 +  V  ( ri ) +  V so( ri )(ˆ l i ·  ˆ s i ) � (24)<br><!-- End of picture text -->

where _V_ ( _r_ ) is typically modeled as a **Woods-Saxon Potential**: 



<!-- Start of picture text -->
V 0<br>V  ( r ) =  − (25)<br>1 +  e ( r−R ) /a<br><!-- End of picture text -->

* **Spin-Orbit Energy Splitting (** ∆ _E_ **so):** The eigenvalue of the spin-orbit operator is: 



<!-- Start of picture text -->
⟨ ˆ l  ·  ˆ s ⟩ = 1 (26)<br>2 [ j ( j  + 1)  − l ( l  + 1)  − s ( s  + 1)]<br><!-- End of picture text -->

Since _s_ = 1 _/_ 2, the states are _j_ = _l_ + 1 _/_ 2 and _j_ = _l −_ 1 _/_ 2. The eigenvalues are: 



<!-- Start of picture text -->
⟨ ˆ l  ·  ˆ s ⟩ = 2 l for j =  l  + 1 / 2 (27)<br>� − l +1 2 for j =  l − 1 / 2<br><!-- End of picture text -->

The energy splitting between these two levels is: 



<!-- Start of picture text -->
∆ E so =  E ( l − 1 / 2)  − E ( l  + 1 / 2) =  C l  + 1 (28)<br>� 2 �<br><!-- End of picture text -->

Since _C_ is strictly positive for the nuclear spin-orbit force, the **state with the larger _j_ ( _j_ = _l_ +1 _/_ 2) is pushed lower in energy**. 

- **Standard Shell Ordering (from lowest to highest):** 

1. [1 _s_ 1 _/_ 2] (capacity 2) _→_ **Magic 2** 

2. [1 _p_ 3 _/_ 2 _,_ 1 _p_ 1 _/_ 2] (capacities 4, 2) _→_ **Magic 8** 

9 

GATE PHYSICS 

NUCLEAR PHYSICS & MODELS 

3. [1 _d_ 5 _/_ 2 _,_ 2 _s_ 1 _/_ 2 _,_ 1 _d_ 3 _/_ 2] (capacities 6, 2, 4) _→_ **Magic 20** 

4. [1 _f_ 7 _/_ 2] (capacity 8) _→_ **Magic 28** 

5. [2 _p_ 3 _/_ 2 _,_ 1 _f_ 5 _/_ 2 _,_ 2 _p_ 1 _/_ 2 _,_ 1 _g_ 9 _/_ 2] (capacities 4, 6, 2, 10) _→_ **Magic 50** 

6. [1 _g_ 7 _/_ 2 _,_ 2 _d_ 5 _/_ 2 _,_ 2 _d_ 3 _/_ 2 _,_ 3 _s_ 1 _/_ 2 _,_ 1 _h_ 11 _/_ 2] (capacities 8, 6, 4, 2, 12) _→_ **Magic 82** 

7. [1 _h_ 9 _/_ 2 _,_ 2 _f_ 7 _/_ 2 _,_ 2 _f_ 5 _/_ 2 _,_ 3 _p_ 3 _/_ 2 _,_ 3 _p_ 1 _/_ 2 _,_ 1 _i_ 13 _/_ 2] (capacities 10, 8, 6, 4, 2, 14) _→_ **Magic 126** 

### **3. Conservation Laws & Symmetries** 

- **Conserved Quantities:** 

   -  **Total Angular Momentum (** _J_ **):** Conserved in spherical potentials. 

   -  **Parity (** Π **):** A conserved quantum number, defined by the orbital angular momentum _l_ of the occupied state: 



<!-- Start of picture text -->
Π = ( − 1) l (29)<br><!-- End of picture text -->

* **The Pairing Force Rule:** Protons and neutrons independently form pairs with opposing angular momenta, coupling to _J_ = 0<sup>+</sup> to minimize energy. This means that: * **All even-even nuclei have ground state spin and parity _J_<sup>Π</sup> = 0<sup>+</sup> .** 

### **4. Derivation Milestones** 

1. **The Spin-Orbit Operator Square:** Express the total angular momentum<sup>ˆ</sup> **j** =<sup>ˆ</sup> **l** +ˆ **s** and square it: 



<!-- Start of picture text -->
ˆ j 2 = ˆ l 2 + ˆ s 2 + 2ˆ l  ·  ˆ s = ⇒ ˆ l  ·  ˆ s  = 1 (30)<br>2 �ˆ j 2 − ˆ l 2 − ˆ s 2�<br><!-- End of picture text -->

2. **Eigenvalue Substitution:** Substitute the angular momentum quantum numbers to yield the split eigenvalues, showing that the spin-orbit splitting scales linearly with _l_ . 3. **Calculating Level Capacities:** The occupancy capacity of any given shell with total angular momentum _j_ is (2 _j_ +1) due to magnetic degeneracy. 4. **Generating Magic Gaps:** Show that for the _N_ = 4 oscillator shell, the 1 _g_ 9 _/_ 2 state ( _j_ = 9 _/_ 2 _, l_ = 4) is pushed down so strongly that it merges with the _N_ = 3 shell, creating a massive gap of 10 nucleons after the 40th state, which defines the magic number 50. 

10 

GATE PHYSICS 

NUCLEAR PHYSICS & MODELS 

### **5. Problem-Solving Algorithm** 

#### **Predicting Spin and Parity (** _J_<sup>Π</sup> **) of Odd-A Nuclei** 

1. **Identify the Odd Nucleon Species:** Find the number of protons _Z_ and neutrons _N_ . 

   -  If _Z_ is even and _N_ is even, stop: the ground state is always _J_<sup>Π</sup> = 0<sup>+</sup> . 

   -  If _A_ is odd, the spin and parity are determined entirely by the single unpaired species (proton or neutron). 

2. **Fill the Shells for the Unpaired Species:** Distribute the nucleons of the odd species sequentially into the shell model levels: 

   - 1 _s_ 1 _/_ 2(2) _→_ 1 _p_ 3 _/_ 2(4) _→_ 1 _p_ 1 _/_ 2(2) _→_ 1 _d_ 5 _/_ 2(6) _→_ 2 _s_ 1 _/_ 2(2) _→_ 1 _d_ 3 _/_ 2(4) _→_ 1 _f_ 7 _/_ 2(8) _→ . . ._ 

3. **Identify the Active Shell:** Note the last shell occupied by the unpaired nucleon. The total angular momentum of this shell is _j_ , and its orbital angular momentum is _l_ . 

4. **Assign Spin and Parity:** 

   -  Spin is _J_ = _j_ . 

   -  Parity is Π = ( _−_ 1)<sup>_l_</sup> . 

   -  *Note:* s-states ( _l_ = 0 _,_ Π = +), p-states ( _l_ = 1 _,_ Π = _−_ ), d-states ( _l_ = 2 _,_ Π = +), f-states ( _l_ = 3 _,_ Π = _−_ ), g-states ( _l_ = 4 _,_ Π = +), h-states ( _l_ = 5 _,_ Π = _−_ ). 

### **6. Crucial Pitfalls** 

#### **Shell Model Traps to Avoid** 

-  **Odd-Odd Coupling Errors:** Do not try to apply the single-particle rule to oddodd nuclei (where both _Z_ and _N_ are odd). For odd-odd nuclei, you must couple the unpaired proton and unpaired neutron using **Nordheim’s Rules**: 

   - Calculate the Nordheim number: _N_ Nord = ( _jp − lp_ ) + ( _jn − ln_ ). 

   - If _N_ Nord = 0, the spins couple to _J_ = _|jp − jn|_ . 

   - If _N_ Nord = _±_ 1, the spins couple to _J_ = _jp_ + _jn_ . 

   - The parity is Π = ( _−_ 1)<sup>_lp_+</sup><sup>_ln_</sup> . 

-  **Energy Level Inversions in Heavy Nuclei:** Be careful when filling the 2 _s_ 1 _/_ 2 and 1 _d_ 3 _/_ 2 shells. In some nuclei, the 2 _s_ 1 _/_ 2 state is lower in energy than the 1 _d_ 3 _/_ 2 state, while in others they invert. For example,<sup>13</sup> C (7 neutrons) has the odd neutron in the 1 _p_ 1 _/_ 2 state ( _J_<sup>Π</sup> = 1 _/_ 2<sup>_−_</sup> ), whereas<sup>17</sup> O (9 neutrons) has the odd neutron in the 1 _d_ 5 _/_ 2 state ( _J_<sup>Π</sup> = 5 _/_ 2<sup>+</sup> ). 

11 

GATE PHYSICS 

NUCLEAR PHYSICS & MODELS 

### **7. Standard Textbook Systems** 

* **Oxygen-17 (**<sup>17</sup> **O):** Has 8 protons (closed magic shell) and 9 neutrons. The 9th neutron sits in the 1 _d_ 5 _/_ 2 state ( _j_ = 5 _/_ 2 _, l_ = 2). The shell model correctly predicts _J_<sup>Π</sup> = 5 _/_ 2<sup>+</sup> . * **Carbon-13 (**<sup>13</sup> **C):** Has 6 protons and 7 neutrons. The 7th neutron occupies the 1 _p_ 1 _/_ 2 state ( _j_ = 1 _/_ 2 _, l_ = 1). The shell model correctly predicts _J_<sup>Π</sup> = 1 _/_ 2<sup>_−_</sup> . * **Scandium-41 (**<sup>41</sup> **Sc):** Has 21 protons and 20 neutrons (closed magic shell). The 21st proton sits in the 1 _f_ 7 _/_ 2 state ( _j_ = 7 _/_ 2 _, l_ = 3). The shell model correctly predicts _J_<sup>Π</sup> = 7 _/_ 2<sup>_−_</sup> . 

12 

GATE PHYSICS 

NUCLEAR PHYSICS & MODELS 

## **References** 

1. Krane, Kenneth S. _Introductory Nuclear Physics_ . Wiley, 1988. 

2. Beiser, Arthur. _Concepts of Modern Physics_ . McGraw-Hill, 2003. 

3. Rajkumar. _Atomic and Molecular Spectra: Laser_ . Kedar Nath Ram Nath, 2015. 

13 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 

# **GATE PHYSICS STUDY NOTES Nuclear Dynamics: S-Wave Forces, Alpha, Beta, & Gamma Decays** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**|**The Nature of the Nuclear Force & The Two-Nucleon Problem (The Deuteron)**<br>**2**|
|---|---|
|**2**|**Alpha Decay & Gamow’s Theory of Tunneling**<br>**6**|
|**3**|**Beta Decay & Fermi’s Theory**<br>**9**|
|**4**|**Electromagnetic Transitions & Gamma Decay Selection Rules**<br>**13**|



1 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 

- **1 The Nature of the Nuclear Force & The Two-Nucleon Problem (The Deuteron)** 

### **1. Core Theory** 

The **nuclear force** is the extremely powerful, short-range interaction that binds protons and neutrons together inside atomic nuclei, overcoming the long-range electrostatic Coulomb repulsion of the protons. 

-  **Physical Origin:** Classically modeled by Hideki Yukawa in 1935 as an exchange of virtual **pi-mesons** ( _π_<sup>0</sup> _, π_<sup>+</sup> _, π_<sup>_−_</sup> ) of mass _mπ ≈_ 140 MeV _/c_<sup>2</sup> . In modern physics, it is a residual color force leaking out from the fundamental strong interaction between quarks, mediated by gluons under quantum chromodynamics (QCD). 

-  **Unique Characteristics:** 

   - **Short Range:** Active only up to _≈_ 2 fm, with a strongly repulsive core at _≤_ 0 _._ 5 fm preventing nuclear collapse. 

   - **Charge Independence:** The strong nuclear force between _p_ - _p_ , _p_ - _n_ , and _n_ - _n_ is identical (excluding Coulomb forces). 

   - **Saturation:** A nucleon interacts only with its immediate neighbors. 

   - **Spin Dependence:** The force is stronger in parallel spin configurations than in antiparallel configurations. 

   - **Tensor (Non-Central) Character:** The force is not purely central, meaning it depends on the spatial orientation of the spins relative to the inter-nucleon axis. 

-  **The Deuteron (**<sup>2</sup> **H):** The simplest bound nuclear system, consisting of a single proton and a single neutron. It represents the crucial two-nucleon testbed for analyzing the strong force. 

   - **Properties:** It is exceptionally weakly bound (binding energy _EB ≈_ 2 _._ 224 MeV). It has no excited bound states; any excitation breaks it. It exists only in the spin-triplet ground state ( _J_ = 1) with positive parity ( _π_ = +). 

### **2. Mathematical Framework** 

The Deuteron ground state is modeled as an _l_ = 0 ( _s_ -wave) state in a 3D finite spherical square well potential: 



<!-- Start of picture text -->
−V 0 for r ≤ R<br>V  ( r ) = (1)<br>0 for r > R<br>�<br><!-- End of picture text -->

where _V_ 0 is the well depth and _R_ is the effective nuclear radius. The radial Schr¨odinger equation for _u_ ( _r_ ) = _rψ_ ( _r_ ) is: 



<!-- Start of picture text -->
d 2 u<br>dr 2 +  K 2 u  = 0 ( r ≤ R ) (2)<br><!-- End of picture text -->



<!-- Start of picture text -->
d 2 u<br>dr 2 − α 2 u  = 0 ( r > R ) (3)<br><!-- End of picture text -->

where: 



<!-- Start of picture text -->
mpmn<br> µ  = mp + mn ≈ m 2 p is the reduced mass of the nucleon system.<br><!-- End of picture text -->

2 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 



<!-- Start of picture text -->
mp ( V 0 −|E| )<br> K = � ℏ 2 is the wave number inside the well (since 2 µ  =  mp ).<br>mp|E|<br> α  = � ℏ 2 is the decay constant outside the well ( |E|  = 2 . 224 MeV).<br><!-- End of picture text -->

The boundary matching condition at _r_ = _R_ (continuity of logarithmic derivatives) yields the transcendental equation: 



<!-- Start of picture text -->
K  cot( KR ) =  −α (4)<br><!-- End of picture text -->

The spin-parity of the Deuteron is _J_<sup>Π</sup> = 1<sup>+</sup> . Due to the non-central **tensor force** , the true ground state is an admixture of the orbital states: 



<!-- Start of picture text -->
|ψ deuteron ⟩ =  aS| 3 S 1 ⟩ +  aD| 3 D 1 ⟩ (5)<br><!-- End of picture text -->

where _|aS|_<sup>2</sup> _≈_ 96% ( _l_ = 0) and _|aD|_<sup>2</sup> _≈_ 4% ( _l_ = 2). This _l_ = 2 component accounts for the deuteron’s small, positive electric quadrupole moment: 



<!-- Start of picture text -->
Q ≈ +0 . 00286 b = +2 . 86  ×  10 − 31 m 2 (6)<br><!-- End of picture text -->

### **3. Conservation Laws & Symmetries** 

-  **Governing Force:** The **Strong Force** governs the nuclear binding, while the **Electromagnetic Force** introduces Coulomb corrections. 

-  **Conserved Quantities:** 

   - **Baryon Number (** _A_ = 2 **):** Strictly conserved. 

   - **Electric Charge (** _Z_ = 1 **):** Strictly conserved. 

   - **Total Angular Momentum (** _J_ = 1 **):** Conserved. 

   - **Parity (** Π = + **):** Conserved. The deuteron is symmetric under spatial inversion. 

   - **Isospin (** _I_ = 0 **):** In the _np_ system, the ground state is antisymmetric in isospin space (singlet, _I_ = 0) to satisfy the generalized Pauli principle, since it is symmetric in spin ( _S_ = 1) and orbital space ( _l_ = 0). 

### **4. Derivation Milestones** 

The calculation of the minimum potential well depth _V_ 0 of the deuteron follows these mathematical stages: 

1. **Piecewise Solutions:** Write the general normalizable solutions for the radial wave function _u_ ( _r_ ): 



<!-- Start of picture text -->
A  sin( Kr ) ( r ≤ R )<br>u ( r ) = (7)<br>� Ce −αr ( r > R )<br><!-- End of picture text -->

2. **Logarithmic Matching:** Equating the value and first derivative at _r_ = _R_ : 



<!-- Start of picture text -->
u ′ ( R − ) = u′ ( R +) = ⇒ K  cot( KR ) =  −α (8)<br>u ( R ) u ( R )<br><!-- End of picture text -->

3. **The Weakly Bound Approximation (** _|E| →_ 0 **):** Since _|E|_ = 2 _._ 224 MeV _≪ V_ 0, the parameter _α_ is very small. In the limit _α ≈_ 0, the boundary condition reduces to: 



<!-- Start of picture text -->
K  cot( KR )  ≈ 0 = ⇒ KR ≈ π (9)<br>2<br><!-- End of picture text -->

3 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 

4. **Extracting the Well Depth:** Substitute the wave number expression: 



<!-- Start of picture text -->
K 2 = mpV 0 ≈ π 2 π 2 ℏ 2 (10)<br>ℏ 2 4 R 2 = ⇒ V 0 ≈ 4 mpR 2<br><!-- End of picture text -->

Substituting _R ≈_ 2 _._ 1 fm and _mpc_<sup>2</sup> _≈_ 938 MeV yields a minimum depth of _V_ 0 _≈_ 36 MeV. 

### **5. Problem-Solving Algorithm** 

#### **Algorithm for Deuteron Finite Well Calculations** 

1. **Verify Mass Definition:** Ensure you are using the correct reduced mass ( _µ ≈ mp/_ 2). In the radial equations, always use the conversion: 



<!-- Start of picture text -->
m ℏ 2 p = 2 ℏ µ 2 ≈ 41 . 47 MeV  ·  fm2 (11)<br><!-- End of picture text -->

2. **Solve for inside wave number** _K_ **:** Given _V_ 0 and _E_ , calculate: 



<!-- Start of picture text -->
mp ( V 0  − |E| )<br>K = (12)<br>� ℏ 2<br><!-- End of picture text -->

3. **Check Transcendental Alignment:** Check if _K_ cot( _KR_ ) = _−α_ , where _α_ = ~~�~~ _mp|E|/_ ℏ<sup>2</sup> . 

4. **Calculate S-D Mixing Moments:** For quadrupole and magnetic moment questions, use: 

_µ_ deuteron = _a_<sup>2</sup> _S_<sup>_µ_(</sup><sup>_S_) +</sup><sup>_a_2</sup> _D_<sup>_µ_(</sup><sup>_D_)</sup><sup>_≈_(0</sup><sup>_._96)[</sup><sup>_µp_+</sup><sup>_µn_] + (0</sup><sup>_._04)[</sup><sup>_µp_+</sup><sup>_µn−_1</sup><sup>_._5]</sup> (13) 

### **6. Crucial Pitfalls** 

#### **Deuteron Traps to Avoid** 

-  **The Reduced Mass Error:** Using the full proton mass _mp_ in the Schr¨odinger equation rather than the reduced mass _µ ≈ mp/_ 2. This leads to a potential well depth _V_ 0 that is off by exactly a factor of 2. 

-  **Assuming Excitation Existence:** Attempting to calculate the energy of the “first excited state” of the deuteron. The deuteron is so weakly bound that it has **no excited bound states** . Any attempt to excite it results in dissociation into a free proton and neutron. 

-  **The Spherical Symmetry Fallacy:** Assuming that because _l_ = 0 is the dominant component (96%), the deuteron is perfectly spherical. The non-zero electric quadrupole moment _Q >_ 0 strictly proves the presence of a non-central (tensor) component that mixes the _D_ -wave ( _l_ = 2) state. 

4 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 

### **7. Standard Textbook Systems** 

-  **The Deuteron Ground State (**<sup>2</sup> **H):** The benchmark bound _np_ configuration with spinparity 1<sup>+</sup> used to derive potential parameters and the tensor character of the nuclear force. 

-  **Low-Energy Neutron-Proton Scattering:** Probes the spin-triplet ( _S_ = 1) and spinsinglet ( _S_ = 0) configurations of the nuclear force, demonstrating that the singlet state is too weak to support a bound state (there is no “singlet deuteron”). 

5 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 

## **2 Alpha Decay & Gamow’s Theory of Tunneling** 

### **1. Core Theory** 

**Alpha decay** is a nuclear de-excitation process in which an unstable heavy parent nucleus spontaneously emits a tightly bound helium-4 (<sup>4</sup> He) nucleus ( _α_ particle) to transition into a more stable daughter nucleus. 

-  **Physical Origin:** A direct consequence of the competition between the short-range, attractive strong force and the long-range, repulsive electrostatic Coulomb force. In heavy nuclei ( _A >_ 200), Coulomb repulsion scales as _Z_<sup>2</sup> , destabilizing the system. 

-  **The Gamow Tunneling Paradox:** The _Q_ -value of alpha decay for heavy nuclei typically ranges between 4 and 9 MeV, which is significantly lower than the peak of the electrostatic Coulomb potential barrier ( _V_ max _≈_ 25 _−_ 30 MeV at the nuclear surface _R_ ). Classically, the _α_ particle is trapped in the potential well and can never escape. 

-  **The Quantum Solution:** George Gamow, Ronald Gurney, and Edward Condon resolved this in 1928. They modeled the pre-formed _α_ particle as a quantum mechanical wave packet that has a non-zero probability of **tunneling through the classically forbidden Coulomb barrier** . 

### **2. Mathematical Framework** 

* **Decay Q-Value (Kinematics):** 



<!-- Start of picture text -->
Q  = � M ( A, Z )  − M ( A − 4 , Z − 2)  − M ( 4 He)� c 2 (14)<br><!-- End of picture text -->

where _M_ represents atomic masses. The kinetic energy of the emitted _α_ particle is: 



<!-- Start of picture text -->
Eα =  Q (15)<br>� A −A 4 �<br>Penetration: The decay constant λ is written as:<br>λ  =  f · P (16)<br><!-- End of picture text -->

* **Gamow Factors and Barrier Penetration:** The decay constant _λ_ is written as: 

where: 

 _f_ = 2 _<u>vR</u>_<sup>isthecollisionfrequency(</sup><sup>_≈_1021s</sup><sup>_−_1)ofthe</sup><sup>_α_particleagainstthebarrier,with</sup> internal velocity _v_ . 

-  _P_ is the quantum tunneling transmission coefficient from the WKB approximation: 



<!-- Start of picture text -->
P =  e − 2 G (17)<br><!-- End of picture text -->

 _G_ is the dimensionless **Gamow Factor** : 



<!-- Start of picture text -->
2 m<br>G  = � Rrc � ℏ 2 ( V  ( r )  − Q ) dr (18)<br><!-- End of picture text -->

is the electrostatic where _m ≈_ 4 _mp_ is the mass of the alpha particle, and _V_ ( _r_ ) =<sup>2(</sup> 4<sup>_Z_</sup> _πϵ_<sup>_−_</sup> 0<sup>2</sup> _r_<sup><u>)</u></sup><sup>_e_2</sup> potential. 

6 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 



<!-- Start of picture text -->
 rc is the classical turning point where V  ( rc ) =  Q :<br>rc = 2( Z − 2) e 2 (19)<br>4 πϵ 0 Q<br><!-- End of picture text -->

* **Geiger-Nuttall Law:** Evaluating the integral yields: 



<!-- Start of picture text -->
Z<br>log10  λ  =  C 1  − C 2 (20)<br>√ Q<br><!-- End of picture text -->

where _C_ 1 and _C_ 2 are constants, showing that tiny changes in _Q_ lead to exponential variations in half-life. 

### **3. Conservation Laws & Symmetries** 

-  **Governing Forces:** The **Strong Force** and **Electromagnetic Force** govern the barrier formation and emission. 

-  **Conserved Quantities:** 

   - **Baryon Number (** _A_ **):** Conserved. 

   - **Lepton Number (** _L_ = 0 **):** Strictly conserved. 

   - **Total Angular Momentum (J** _i_ = **J** _f_ + **L):** Conserved. The orbital angular momentum _L_ carried by the _α_ particle must satisfy _|Ji − Jf | ≤ L ≤ Ji_ + _Jf_ . 

   - **Parity (** Π _i_ = Π _f_ ( _−_ 1)<sup>_L_</sup> **):** Strictly conserved. Since the _α_ particle has intrinsic parity Π _α_ = +, the spatial parity change is governed entirely by ( _−_ 1)<sup>_L_</sup> . 

### **4. Derivation Milestones** 

The analytical derivation of the Gamow Factor is achieved through these mathematical steps: 

1. **The WKB Integrand Setup:** Substitute the Coulomb potential _V_ ( _r_ ) = _Q_<sup>_<u>r</u>_</sup> _r_<sup>_<u>c</u>_intothe</sup> Gamow integral: 



<!-- Start of picture text -->
2 mQ rc<br>G  = (21)<br>� ℏ 2 � Rrc � r − 1 dr<br><!-- End of picture text -->

2. **Trigonometric Integration:** Use the substitution _r_ = _rc_ cos<sup>2</sup> _θ_ , with limits _r_ = _R → θ_ 0 = arccos ~~�~~ _R/rc_ and _r_ = _rc → θ_ = 0: 



<!-- Start of picture text -->
rc R R<br>� � r − 1 dr =  rc �arccos � rc − � rc �1  − r R c � � (22)<br><!-- End of picture text -->

3. **The Thick Barrier Approximation (** _R ≪ rc_ **):** Since the barrier is thick, ~~�~~ _R/rc ≪_ 1. Taylor expand the terms: 



<!-- Start of picture text -->
arccos R ≈ π R = ⇒ G ≈ 2 mQ π R (23)<br>� rc 2 − � rc � ℏ 2 rc � 2 − 2 � rc �<br><!-- End of picture text -->

4. **The Velocity-Dependent Result:** Substitute _rc_ back and express in terms of the alpha velocity _v_ = ~~�~~ 2 _Q/m_ : 



<!-- Start of picture text -->
m ( Z − 2) R<br>G  = πe 2( Z − 2) − 4 e (24)<br>ϵ 0ℏ v � πϵ 0ℏ 2<br><!-- End of picture text -->

This derives the 2 _G ∝_ 1 _/_<sup>_~~√~~_</sup> _Q_ dependency which yields the Geiger-Nuttall law. 

7 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 

### **5. Problem-Solving Algorithm** 

#### **Algorithm for Alpha Decay Kinematics & Selection Rules** 

1. **Compute Decay Q-Value:** Given atomic masses of Parent ( _MP_ ), Daughter ( _MD_ ), and Helium-4 ( _Mα_ ), calculate: 

      - _Q_ = ( _MP − MD − Mα_ ) _×_ 931 _._ 5 MeV (25) 

2. **Calculate Alpha Kinetic Energy:** Apply the conservation of momentum mass-ratio factor: 

      - _Eα_ = _Q_ (where _AD_ = _AP −_ 4) (26) � _AADP_ � 

3. **Evaluate Spin-Parity Allowedness:** For transitions _Ji_<sup>Π</sup><sup>_i_</sup> _→ Jf_<sup>Π</sup><sup>_f_:</sup> 

   -  Find the allowed orbital angular momentum values: _|Ji − Jf | ≤ L ≤ Ji_ + _Jf_ . 

   -  Test parity conservation: check if Π _i/_ Π _f_ = ( _−_ 1)<sup>_L_</sup> . 

   -  If no value of _L_ in the allowed range satisfies this parity relation, the transition is **forbidden by parity conservation** . 

### **6. Crucial Pitfalls** 

#### **Alpha Decay Traps to Avoid** 

-  **Neglecting Daughter Recoil:** Calculating the emitted alpha particle’s kinetic energy as being exactly equal to the _Q_ -value ( _Eα_ = _Q_ ). Because the daughter nucleus must conserve momentum by recoiling, the alpha particle carries off only a fraction of the energy: _Eα_ = _Q_ ( _A −_ 4) _/A_ . Forgetting this factor introduces systematic errors. 

-  **The Parity Conservation Fallacy:** Assuming a transition such as 1<sup>_−_</sup> _→_ 0<sup>+</sup> can occur with _L_ = 0 because of spin. If _L_ = 0, then ( _−_ 1)<sup>0</sup> = +, which violates the parity change from _−_ to +. The transition must occur with _L_ = 1, which satisfies the conservation rule since ( _−_ 1)<sup>1</sup> = _−_ . 

### **7. Standard Textbook Systems** 

-  **Polonium-212 (**<sup>212</sup> **Po) Decay:** Decays to Lead-208 (<sup>208</sup> Pb) with a very high _Q_ -value of 8 _._ 95 MeV, yielding an exceptionally short half-life of _t_ 1 _/_ 2 _≈_ 3 _×_ 10<sup>_−_7</sup> s, illustrating the extreme sensitivity of the Gamow exponent. 

-  **Uranium-238 (**<sup>238</sup> **U) Decay:** Decays to Thorium-234 (<sup>234</sup> Th) with a low _Q_ -value of 4 _._ 27 MeV, resulting in a massive half-life of 4 _._ 47 _×_ 10<sup>9</sup> years, providing the classical baseline for geothermal and geochronological models. 

8 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 

## **3 Beta Decay & Fermi’s Theory** 

### **1. Core Theory** 

**Beta decay** is a weak-interaction radioactive process in which a nucleon inside an unstable nucleus is transformed into another nucleon type, accompanied by the emission of a beta particle (an electron or positron) and a lepton partner (an antineutrino or neutrino). 

-  **Beta-Minus (** _β_<sup>_−_</sup> **) Decay:** A neutron transforms into a proton, emitting an electron and an electron antineutrino: 



<!-- Start of picture text -->
n → p  +  e − + ¯ νe (27)<br><!-- End of picture text -->

-  **Beta-Plus (** _β_<sup>+</sup> **) Decay:** A proton transforms into a neutron, emitting a positron and an electron neutrino: 

   - _p → n_ + _e_<sup>+</sup> + _νe_ (28) 

-  **Electron Capture (EC):** A core atomic orbital electron is captured by a proton, emitting a neutrino: _p_ + _e_<sup>_−_</sup> _→ n_ + _νe_ (29) 

-  **The Three-Body Problem & Continuous Spectrum:** Because beta decay is a threebody decay, the available energy ( _Q_ -value) is shared continuously between the recoil daughter, the beta particle, and the neutrino. This results in the characteristic **continuous beta spectrum** , which historically led Wolfgang Pauli to postulate the existence of the neutrino. 

-  **Fermi’s Theory of Beta Decay:** Models the transition probability using First-Order Perturbation Theory ( **Fermi’s Golden Rule** ) and a point-like contact weak interaction Hamiltonian, explaining the shape of the momentum spectrum and providing the foundation for **Kurie Plots** . 

### **2. Mathematical Framework** 

* **Kinematic Q-Values (expressed in Atomic Masses):** 



<!-- Start of picture text -->
Qβ− = [ M ( A, Z )  − M ( A, Z  + 1)]  c 2 (30)<br><!-- End of picture text -->



<!-- Start of picture text -->
Qβ + = [ M ( A, Z )  − M ( A, Z − 1)  − 2 me ]  c 2 (31)<br><!-- End of picture text -->



<!-- Start of picture text -->
Q EC = [ M ( A, Z )  − M ( A, Z − 1)]  c 2 − EB (32)<br><!-- End of picture text -->

where _me_ is the electron rest mass ( _≈_ 0 _._ 511 MeV) and _EB_ is the atomic binding energy of the captured shell. * **Fermi’s Golden Rule:** The transition rate is: 



<!-- Start of picture text -->
dλ  = 2 π 2 dρf (33)<br>ℏ ��� ⟨ψf |H  ˆweak |ψi⟩ ���<br><!-- End of picture text -->

Assuming a contact interaction of strength _GF_ (the Fermi coupling constant, _GF ≈_ 1 _._ 43 _×_ 10<sup>_−_62</sup> J _·_ m<sup>3</sup> ), the momentum spectrum of the emitted beta particle is: 



<!-- Start of picture text -->
N ( p ) dp  =  C · F ( Z, p )  · p 2 ( E 0  − Ee ) 2 dp (34)<br><!-- End of picture text -->

where: 

9 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 

-  _F_ ( _Z, p_ ) is the **Fermi Function** , correcting for Coulomb distortion of the beta wave function by the nuclear charge. 

-  _E_ 0 is the maximum endpoint energy of the beta particle. 

-  _p_ and _Ee_ are the beta momentum and relativistic energy. 

* **The Kurie Plot:** Linearizing the momentum spectrum equation: 



<!-- Start of picture text -->
N ( p )<br>� p 2 F ( Z, p ) ∝ ( E 0  − Ee ) (35)<br><!-- End of picture text -->

Plotting this quantity against _Ee_ yields a straight line with an _x_ -intercept at the endpoint energy _E_ 0, allowing precise measurement of _E_ 0 and any deviation near the limit due to non-zero neutrino mass. 

### **3. Conservation Laws & Symmetries** 

-  **Governing Force:** The **Weak Force** is the sole driver of beta transitions. 

-  **Conserved Quantities:** 

   - **Baryon Number (** _A_ **):** Strictly conserved. 

   - **Lepton Number (** _Le_ = _Ne− − Ne_ + + _Nνe − Nν_ ¯ _e_ **):** Conserved. 

   - **Total Angular Momentum (J** _i_ = **J** _f_ + **J** _β_ + **J** _ν_ + **Lorbital):** Conserved. 

-  **Violated Symmetries:** 

   - **Parity (** Π **):** Maximally violated in weak interactions (electrons are emitted with negative helicity). 

   - **Charge Conjugation (** _C_ **):** Violated. 

   - **Isospin (** _I_ **):** Violated. 

### **4. Derivation Milestones** 

1. **Transition Matrix Element:** Write the weak interaction matrix element using the Fermi constant _GF_ : 



<!-- Start of picture text -->
Vfi =  GF Mfi e −i k e· r e −i k ν · r d 3 r (36)<br>�<br><!-- End of picture text -->

2. **The Allowed Approximation:** Since the wavelengths of the electron and neutrino are large compared to the nuclear radius, we Taylor expand the exponentials: _e_<sup>_−i_</sup><sup>**k**</sup><sup>_·_</sup><sup>**r**</sup> _≈_ 1. This reduces the matrix element to the unretarded nuclear matrix element: 



<!-- Start of picture text -->
Vfi ≈ GF Mfi (37)<br><!-- End of picture text -->

3. **Phase Space Integration:** The density of final states _dρf_ is a product of electron and neutrino states: 



<!-- Start of picture text -->
dρf = V 2 d 3 ped 3 pν (38)<br>(2 π ℏ) 6 dEf<br><!-- End of picture text -->

10 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 

Integrating over the neutrino phase space subject to the energy conservation delta function _δ_ ( _E_ 0 _− Ee − Eν_ ) yields the momentum spectrum: 



<!-- Start of picture text -->
dN<br>∝ p 2 e p ν 2 =  p 2 e (39)<br>dpe � E 0  −c Ee �2<br><!-- End of picture text -->

4. **Fermi Coulomb Correction:** Multiplying by the relativistic electrostatic boundary factor _F_ ( _Z, pe_ ) yields the final allowed beta spectrum. 

### **5. Problem-Solving Algorithm** 

#### **Algorithm for Beta Decay Classifications & Q-Values** 

1. **Calculate Q-Value (Mind the Positron mass!):** 

   -  For _β_<sup>_−_</sup> : _Q_ = [ _MP − MD_ ] _c_<sup>2</sup> . 

   -  For _β_<sup>+</sup> : _Q_ = [ _MP − MD −_ 2 _me_ ] _c_<sup>2</sup> . (Subtract 1 _._ 022 MeV). 

2. **Classify the Spin-Coupling (Fermi vs. Gamow-Teller):** 

   -  **Fermi Transition:** Spins of electron and neutrino couple antiparallel to _S_ = 0. Selection rule: ∆ _J_ = 0, no parity change. 

   -  **Gamow-Teller Transition:** Spins of electron and neutrino couple parallel to _S_ = 1. Selection rule: ∆ _J_ = 0 _, ±_ 1 (excluding 0 _→_ 0), no parity change. 

3. **Classify Forbiddenness by Parity:** 

   -  If parity does not change: transition is **Allowed** ( _L_ = 0). 

   -  If parity changes: transition is **First-Forbidden** ( _L_ = 1). 

### **6. Crucial Pitfalls** 

#### **Beta Decay Kinematic & Classification Traps** 

-  **The Positron mass subtraction error:** Forgetting the factor of 2 _mec_<sup>2</sup> when calculating _Qβ_ + using neutral atomic masses. Since the daughter atom has one less electron, we must subtract the positron mass plus the mass of the newly ejected atomic shell electron, totaling 1 _._ 022 MeV. 

-  **The** 0 _→_ 0 **Gamow-Teller Trap:** Assuming a transition such as 0<sup>+</sup> _→_ 0<sup>+</sup> can be a Gamow-Teller transition. Since _S_ = 1 for Gamow-Teller, a 0 _→_ 0 transition is strictly forbidden. It must occur via a pure **Fermi transition** . 

### **7. Standard Textbook Systems** 

-  **Tritium Beta Decay (**<sup>3</sup> **H** _→_<sup>3</sup> **He** + _e_<sup>_−_</sup> + ¯ _νe_ **):** The standard system for analyzing Kurie plot endpoints because of its exceptionally low endpoint energy ( _E_ 0 _≈_ 18 _._ 6 keV), which minimizes systematic errors when placing upper limits on the neutrino mass. 

11 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 

-  **Cobalt-60 Beta Decay (**<sup>60</sup> **Co** _→_<sup>60</sup> **Ni**<sup>_∗_</sup> **):** The experiment conducted by Chien-Shiung Wu in 1956 that confirmed parity violation in weak interactions by aligning the spins of<sup>60</sup> Co nuclei and observing an asymmetric, backward emission profile of electrons. 

12 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 

## **4 Electromagnetic Transitions & Gamma Decay Selection Rules** 

### **1. Core Theory** 

**Gamma decay** is an electromagnetic de-excitation process in which a nucleus in an excited state transitions to a lower energy state by emitting a highly energetic photon (a _γ_ ray). 

-  **Physical Origin:** Occurs when the spatial charge and current distributions within the nucleus rearrange. Unlike atoms (where transitions involve single valence electrons), nuclear gamma decays represent collective or single-particle rearrangement of protons and neutrons. 

-  **Multipole Radiation Fields:** Gamma-ray photons carry off a discrete angular momentum _L_ . The transitions are classified based on the nature of the oscillating source: 

   - **Electric Multipole (** _EL_ **):** Driven by oscillations in the nuclear charge distribution (e.g., dipole _E_ 1, quadrupole _E_ 2). 

   - **Magnetic Multipole (** _ML_ **):** Driven by oscillations in the nuclear current loop and spin magnetization distributions (e.g., dipole _M_ 1, quadrupole _M_ 2). 

-  **Internal Conversion (IC):** A competing de-excitation mechanism where the excitation energy of the nucleus is transferred electromagnetically to a core orbital electron (typically from the _K_ or _L_ shell), ejecting it from the atom. IC dominates in heavy nuclei with low excitation energies. 

### **2. Mathematical Framework** 

* **Energy Conservation & Recoil:** 



<!-- Start of picture text -->
E 2<br>Eγ ≈ Ei − Ef − ER with ER = γ (40)<br>2 Mc 2<br><!-- End of picture text -->

Since the nuclear mass _M_ is massive, the recoil energy _ER_ is extremely small ( _∼_ 10<sup>_−_5</sup> eV), making _Eγ ≈ Ei − Ef_ to a high degree of precision. * **Multipole Parity Relations:** The spatial parity of the emitted multipole radiation is: 



<!-- Start of picture text -->
Π( EL ) = ( − 1) L (41)<br><!-- End of picture text -->



<!-- Start of picture text -->
Π( ML ) = ( − 1) L +1 (42)<br><!-- End of picture text -->

* **Weisskopf Transition Probability Estimates:** The transition rate _λ_ scales with energy and mass number: 



<!-- Start of picture text -->
λ ( EL )  ∝ Eγ 2 L +1 A 2 L/ 3 (43)<br><!-- End of picture text -->



<!-- Start of picture text -->
λ ( ML )  ∝ Eγ 2 L +1 A (2 L− 2) / 3 (44)<br><!-- End of picture text -->

*Rule of thumb:* 

-  Lower multipole orders _L_ are faster and highly dominant: _λ_ ( _L_ = 1) _≫ λ_ ( _L_ = 2) _≫ λ_ ( _L_ = 3). 

-  For a given _L_ , electric transitions are faster: _λ_ ( _EL_ ) _> λ_ ( _ML_ ). 

13 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 

### **3. Conservation Laws & Symmetries** 

-  **Governing Force:** The **Electromagnetic Force** governs gamma transitions. 

-  **Conserved Quantities:** 

   - **Baryon Number (** _A_ **):** Conserved. 

   - **Electric Charge (** _Z_ **):** Conserved. 

   - **Angular Momentum (J** _i_ = **J** _f_ + **L):** Conserved. The photon angular momentum _L_ must satisfy: 



<!-- Start of picture text -->
|Ji − Jf | ≤ L ≤ Ji  +  Jf (with L ≥ 1) (45)<br><!-- End of picture text -->

*Note:* **Monopole ( _L_ = 0) transitions are strictly forbidden** because a photon is a transverse wave and cannot carry zero spin. 

**– Parity (** Π _i_ = Π _f ·_ Π **rad):** Conserved. 

### **4. Derivation Milestones** 

1. **The Vector Potential Expansion:** Express the electromagnetic vector potential in terms of spherical vector waves: 



<!-- Start of picture text -->
A ( r ) = � aLM A LM ( r ) (46)<br>LM<br><!-- End of picture text -->

2. **The Interaction Hamiltonian:** Set up the perturbation Hamiltonian using the nuclear current density **J** ( **r** ): 



<!-- Start of picture text -->
H ˆint =  − J ( r )  ·  A ( r ) d 3 r (47)<br>�<br><!-- End of picture text -->

3. **Applying First-Order Reflection Theory:** The transition rate is given by Fermi’s Golden Rule: 



<!-- Start of picture text -->
λ  = 2 π 2 ρf (48)<br>ℏ ��� ⟨ψf |H  ˆint |ψi⟩ ���<br><!-- End of picture text -->

4. **Weisskopf Unit Calculations:** Simplify the spatial matrix elements by modeling the transition as a single proton moving within a spherical box of radius _R_ = _r_ 0 _A_<sup>1</sup><sup>_/_3</sup> , yielding the power-law Weisskopf estimates. 

14 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 

### **5. Problem-Solving Algorithm** 

#### **Algorithm for Gamma Decay Selection Rules** 

1. **Determine the Allowed Multipolarity Range (** _L_ **):** Given initial spin _Ji_ and final spin _Jf_ , calculate: _L_ min = _|Ji − Jf |, L_ max = _Ji_ + _Jf_ (49) 

Ensure _L ≥_ 1. If _Ji_ = _Jf_ = 0, no gamma emission can occur (transition is via Internal Conversion). 

2. **Determine the Required Parity Change (** ∆Π **):** Compare initial parity Π _i_ and final parity Π _f_ : 

      - ∆Π = Π _i ·_ Π _f_ (50) 

3. **Test Parity Rules for each allowed** _L_ **:** 

   -  If ∆Π = + (no parity change): allowed multipoles are ** _M_ odd, _E_ even** (e.g., _M_ 1 _, E_ 2 _, M_ 3 _, E_ 4). 

   -  If ∆Π = _−_ (parity change): allowed multipoles are ** _E_ odd, _M_ even** (e.g., _E_ 1 _, M_ 2 _, E_ 3 _, M_ 4). 

4. **Identify the Dominant Transition:** The lowest allowed _L_ is highly dominant. Identify the lowest allowed electric ( _EL_ ) or magnetic ( _ML_ ) multipoles. The transition rate of _E_ ( _L_ ) is typically 10<sup>2</sup> to 10<sup>4</sup> times faster than _M_ ( _L_ ), so _E_ ( _L_ ) dominates over _M_ ( _L_ ), and _M_ ( _L_ ) dominates over _E_ ( _L_ + 1). 

### **6. Crucial Pitfalls** 

#### **Gamma Decay Selection Rule Traps** 

-  **The** 0 _→_ 0 **Gamma Fallout:** Attempting to calculate the multipolarity of a 0<sup>+</sup> _→_ 0<sup>+</sup> transition. This transition is strictly forbidden for gamma emission because _L ≥_ 1 is required. The de-excitation must occur via **Internal Conversion** (ejecting a shell electron). 

-  **Flipping the Parity Exponents:** Confusing the exponents in the parity relations. Remember that _EL_ parity is ( _−_ 1)<sup>_L_</sup> and _ML_ parity is ( _−_ 1)<sup>_L_+1</sup> . Mixing these up will cause you to misclassify magnetic and electric multipoles in exams. 

### **7. Standard Textbook Systems** 

-  **Barium-137 Isomer Decay (**<sup>137</sup> **Ba**<sup>_∗_</sup> _→_<sup>137</sup> **Ba):** A highly notable transition from the 11 _/_ 2<sup>_−_</sup> excited state to the 3 _/_ 2<sup>+</sup> ground state. The allowed angular momentum range is 4 _≤ L ≤_ 7, and the parity changes. The transition is classified as a pure **M4 transition** , resulting in an exceptionally long half-life of 2 _._ 55 minutes. 

-  **Lead-208 Transition (**<sup>208</sup> **Pb**<sup>_∗_</sup> _→_<sup>208</sup> **Pb):** The transition from the 3<sup>_−_</sup> first excited state to the 0<sup>+</sup> ground state. The allowed _L_ is strictly _L_ = 3, and the parity changes. The transition is a pure **E3 transition**. 

15 

GATE PHYSICS 

NUCLEAR FORCE & RADIOACTIVE DECAYS 

## **References** 

1. Krane, Kenneth S. _Introductory Nuclear Physics_ . John Wiley & Sons, 1988. 

2. Griffiths, David. _Introduction to Elementary Particles_ . Wiley-VCH, 2008. 

3. Zettili, Nouredine. _Quantum Mechanics: Concepts and Applications_ . Wiley, 2009. 

16 

GATE PHYSICS 

NUCLEAR REACTIONS & DETECTORS 

# **GATE PHYSICS STUDY NOTES Nuclear Reactions, Scattering, Fission, Fusion, and Instrumentation** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

|**Contents**||
|---|---|
|**1**<br>**Rutherford Scattering Kinematics**|**2**|
|**2**<br>**Nuclear Reactions, Q-Values, and Threshold Energies**|**6**|
|**3**<br>**The Physics of Nuclear Fission and Fusion**|**9**|
|**4**<br>**Operating Principles of Particle Accelerators and Detectors**|**12**|



1 

GATE PHYSICS 

NUCLEAR REACTIONS & DETECTORS 

## **1 Rutherford Scattering Kinematics** 

### **1. Core Theory** 

**Rutherford Scattering** represents the elastic scattering of charged particles (typically alpha particles,<sup>4</sup> He<sup>2+</sup> ) by the electrostatic Coulomb potential of a heavy, positively charged atomic nucleus. 

The physical origin of this phenomenon is the long-range, repulsive Coulomb force between the projectile charge _q_ = _ze_ and the target nucleus charge _Q_ = _Ze_ . Under the assumption that the target nucleus is infinitely massive and remains stationary during the collision, the trajectory of the projectile is a classical Keplerian hyperbola with the target nucleus located at its external focus. 

The physical significance of Rutherford scattering is that it experimentally demonstrated the existence of the atomic nucleus, showing that almost all the mass and positive charge of an atom are concentrated in an extremely small central volume ( _R ≈_ 10<sup>_−_14</sup> m) rather than distributed uniformly throughout the atom as suggested by the Thomson ”plum pudding” model. At very high energies, deviations from classical Rutherford scattering map out the physical boundaries where the short-range strong nuclear force overrides the electromagnetic repulsion, allowing for the precise measurement of nuclear radii. 

### **2. Mathematical Framework** 

The classical scattering is governed by the following equations: 

-  **Impact Parameter (** _b_ **):** The perpendicular distance from the initial velocity vector of the projectile to the center of the target nucleus: 



<!-- Start of picture text -->
zZe 2<br>b  = d 2 0 cot � 2 θ � = 4 πϵ 0  ·  2 E cot � 2 θ � (1)<br><!-- End of picture text -->

where _θ_ is the scattering angle, _E_ is the kinetic energy of the incident projectile, and _d_ 0 is the distance of closest approach in a head-on collision. 

-  **Distance of Closest Approach for a Head-on Collision (** _d_ 0 **):** Occurs when the impact parameter _b_ = 0, causing the particle to stop momentarily and reverse its direction ( _θ_ = 180<sup>_◦_</sup> ): 



<!-- Start of picture text -->
d 0 = zZe 2 (expressed in meters) (2)<br>4 πϵ 0 E<br><!-- End of picture text -->

-  **Distance of Closest Approach for Arbitrary** _b_ **(** _d_ **min):** 



<!-- Start of picture text -->
d min = d 0 1 + csc (3)<br>2 � � 2 θ ��<br><!-- End of picture text -->

-  **Rutherford Differential Scattering Cross-Section (** _dσ/d_ Ω **):** Represents the probability of a projectile being scattered into a unit solid angle _d_ Ω= 2 _π_ sin _θdθ_ : 



<!-- Start of picture text -->
dσ zZe 2 1<br>csc 4 (expressed in m 2 / sr) (4)<br>d Ω = � 4 πϵ 0  ·  4 E �2 sin 4 � 2 θ � = � d 40 �2 � 2 θ �<br><!-- End of picture text -->

### **3. Conservation Laws & Symmetries** 

-  **Governing Force:** The interaction is mediated strictly by the classical **Electromagnetic Force** . 

-  **Conserved Quantities:** 

2 

GATE PHYSICS 

NUCLEAR REACTIONS & DETECTORS 

- **Total Energy (** _E_ **):** Since the scattering is completely elastic and the target is assumed stationary, the kinetic energy of the projectile is conserved before and after scattering. 

- **Total Angular Momentum (L):** The Coulomb force is a central force ( **F** _∝_ ˆ **r** ), yielding zero net torque ( **_τ_** = **r** _×_ **F** = 0). The angular momentum of the projectile about the target is conserved, restricting the motion to a single plane: 

_L_ = _mv_ 0 _b_ = constant (5) 

- **Linear Momentum (P):** The momentum of the individual projectile is rotated by the scattering angle _θ_ , but the total momentum of the projectile-target system is strictly conserved. 

- **Parity (** Π **):** The electromagnetic potential is symmetric under spatial inversion ( _V_ ( **r** ) = _V_ ( _−_ **r** )), strictly conserving parity. 

### **4. Derivation Milestones** 

The Rutherford cross-section is derived via these critical physical steps: 

1. **Conservation of Angular Momentum and Energy:** Establish the orbital parameters of the hyperbolic trajectory. At infinite distance, the velocity is _v_ 0 and the impact parameter is _b_ , giving _L_ = _mv_ 0 _b_ . At the point of closest approach _d_ min, the velocity is _v_ min, which must be perpendicular to the radial vector, giving _L_ = _mv_ min _d_ min. Apply conservation of energy: 



<!-- Start of picture text -->
E = 1 0 = 1 min + zZe 2 (6)<br>2 mv 2 2 mv 2 4 πϵ 0 d min<br><!-- End of picture text -->

2. **Hyperbolic Orbit Angle Relation:** Solve the classical central-force orbital equation _r_ ( _ϕ_ ) = 1+ _ϵ_ cos _<u>p</u> ϕ_<sup>,where</sup><sup>_ϵ_istheeccentricityofthehyperbola.</sup> The scattering angle _θ_ is related to the asymptotic angles of the hyperbola, which directly yields the relation between eccentricity and the impact parameter: 



<!-- Start of picture text -->
2 Eb<br>ϵ  = 1 + = csc (7)<br>� � zZe 2 / 4 πϵ 0 �2 � 2 θ �<br><!-- End of picture text -->

3. **Relating** _b_ **to** _θ_ **:** Rearranging this eccentricity relation directly isolates the impact parameter: 



<!-- Start of picture text -->
zZe 2<br>b  = (8)<br>4 πϵ 0  ·  2 E cot � 2 θ �<br><!-- End of picture text -->

4. **Transforming Cross-Section Area:** Projectiles passing through an annular ring of radius _b_ and width _db_ must scatter into a solid angle _d_ Ω= 2 _π_ sin _θdθ_ . By conservation of particle number, equate the areas: 



<!-- Start of picture text -->
db<br>dσ = 2 πb|db|  = 2 πb (9)<br>���� dθ ���� dθ<br><!-- End of picture text -->

Substitute _b_ ( _θ_ ) and its derivative _dθ_<sup>_<u>db</u>_=</sup><sup>_−_</sup><sup>_<u>d</u>_</sup> 4<sup><u>0</u>csc2(</sup><sup>_θ/_2)intotheareabalance:</sup> 



<!-- Start of picture text -->
0 cos( θ/ 2)<br>dσ = 2 π � d 20 cot � 2 θ ��� d 40 csc2 � 2 θ �� dθ =  π d 4 2 sin 3 ( θ/ 2) dθ (10)<br><!-- End of picture text -->

Dividing by _d_ Ω= 2 _π_ sin _θdθ_ = 4 _π_ sin( _θ/_ 2) cos( _θ/_ 2) _dθ_ yields the Rutherford differential cross-section. 

3 

GATE PHYSICS 

NUCLEAR REACTIONS & DETECTORS 

### **5. Problem-Solving Algorithm** 

#### **Rutherford Scattering Calculations** 

1. **Identify the System Constants:** Write out the charge of the projectile ( _z_ ), target atomic number ( _Z_ ), and the incident kinetic energy _E_ (often given in MeV). 

2. **Evaluate the Head-on Distance of Closest Approach (** _d_ 0 **):** To simplify cal- _<u>e</u>_<sup>2</sup> 

culations, express _d_ 0 using the constant 4 _πϵ_ 0<sup>_≈_1</sup><sup>_._44MeV</sup><sup>_·_fm:</sup> 



<!-- Start of picture text -->
1 . 44  · zZ<br>d 0 = (expressed in femtometers, 1 fm = 10 − 15 m) (11)<br>E (in MeV)<br><!-- End of picture text -->

3. **Calculate the Impact Parameter (** _b_ **) for a Given** _θ_ **:** 



<!-- Start of picture text -->
b  = d 2 0 cot � 2 θ � (12)<br><!-- End of picture text -->



<!-- Start of picture text -->
4. Calculate the Minimum Distance of Closest Approach ( d min):<br>d min = d 0 1 + csc (13)<br>2 � � 2 θ ��<br><!-- End of picture text -->

### **6. Crucial Pitfalls** 

#### **Rutherford Scattering Traps to Avoid** 

-  **The Target Recoil Kinetic Energy Trap:** Assuming the target nucleus is infinitely heavy and completely stationary at extremely high projectile energies. If the projectile mass _m_ is not negligible compared to the target mass _M_ , you must transform the equations to the center-of-mass (CM) frame, replacing _m_ with the reduced mass _µ_ = _mmM_ + _M_<sup>andtheincidentenergy</sup><sup>_E_withtheCMenergy</sup><sup>_E_cm=</sup> _E_ _<u>M</u> m_ + _M_<sup>.</sup> 

-  **Angle Halving in** csc<sup>4</sup> ( _θ/_ 2) **:** Forgetting the factor of 2 in the argument of the cosecant term. If the scattering angle is _θ_ = 60<sup>_◦_</sup> , you must evaluate csc<sup>4</sup> (30<sup>_◦_</sup> ) = 2<sup>4</sup> = 16, not csc<sup>4</sup> (60<sup>_◦_</sup> ). 

-  **The Strong Force Threshold Limit:** Applying classical Rutherford formulas when the alpha particle penetrates the nucleus. When _d_ min _≤ R_ nucleus = _R_ 0 _A_<sup>1</sup><sup>_/_3</sup> , the alpha particle experiences the highly attractive strong nuclear force, causing the experimental cross-section to drop sharply below the Coulomb-predicted Rutherford value. 

### **7. Standard Textbook Systems** 

-  **Geiger-Marsden Gold Foil Experiment (** _Z_ = 79 **,** _z_ = 2 **):** A historical system where 5 _._ 5 MeV alpha particles are scattered by a gold target. The head-on distance of closest approach is calculated to be _d_ 0 _≈_ 41 _._ 3 fm, which is larger than the gold nuclear radius ( _R ≈_ 7 _._ 3 fm), explaining why classical Rutherford scattering is highly accurate for this setup. 

-  **Alpha Scattering off Aluminum (** _Z_ = 13 **,** _z_ = 2 **):** At _E_ = 7 _._ 7 MeV, the distance of 

4 

GATE PHYSICS 

NUCLEAR REACTIONS & DETECTORS 

closest approach is _d_ 0 _≈_ 4 _._ 85 fm. Since this is comparable to the aluminum nuclear radius ( _R ≈_ 3 _._ 6 fm), this system is used to illustrate the breakdown of Rutherford scattering due to strong nuclear force interference. 

5 

GATE PHYSICS 

NUCLEAR REACTIONS & DETECTORS 

## **2 Nuclear Reactions, Q-Values, and Threshold Energies** 

### **1. Core Theory** 

A **Nuclear Reaction** occurs when a projectile particle _a_ collides with a target nucleus _X_ , initiating a nuclear transformation that produces a new outgoing particle _b_ and a residual recoil nucleus _Y_ : 



<!-- Start of picture text -->
a  +  X → Y +  b or in compact notation: X ( a, b ) Y (14)<br><!-- End of picture text -->

* **The Q-Value:** The net energy released or absorbed during a nuclear reaction, representing the difference between the rest masses of the reactants and products. * If _Q >_ 0, the reaction is **exothermic** (exoergic), releasing energy as kinetic energy of the products. This can occur spontaneously. * If _Q <_ 0, the reaction is **endothermic** (endoergic), requiring a net input of energy. * **Threshold Energy ( _E_ th):** For an endothermic reaction ( _Q <_ 0), the incident projectile _a_ must possess a minimum kinetic energy in the laboratory frame to initiate the reaction. This threshold energy is strictly greater than _|Q|_ because a portion of the projectile’s momentum must be conserved as kinetic energy of the moving center of mass of the system. 

### **2. Mathematical Framework** 

* **The Q-Value Equation:** 



<!-- Start of picture text -->
Q  = [( Ma  +  MX )  − ( Mb  +  MY  )]  c 2 =  Eb  +  EY − Ea (15)<br><!-- End of picture text -->

where _Mi_ are the rest masses of the individual species, and _Ei_ are their respective laboratory kinetic energies (assuming the target _X_ is initially at rest, _EX_ = 0). * **The Reaction Kinematics Equation (The Q-Equation):** Relating the Q-value to the projectile kinetic energy _Ea_ , the emitted particle kinetic energy _Eb_ , and the scattering angle _θ_ in the laboratory frame: 



<!-- Start of picture text -->
2<br>Q  =  Eb 1 + Mb − Ea 1  − Ma − � MaMbEaEb  cos  θ (16)<br>� MY � � MY � MY<br><!-- End of picture text -->

* **Threshold Energy for Endothermic Reactions ( _E_ th):** 



<!-- Start of picture text -->
E th =  −Q 1 + Ma (17)<br>� MX �<br><!-- End of picture text -->

where _Ma_ is the mass of the projectile and _MX_ is the mass of the stationary target. 

### **3. Conservation Laws & Symmetries** 

-  **Governing Forces:** Nuclear reactions can be mediated by the **Strong Force** (fast transitions, _∼_ 10<sup>_−_23</sup> s), the **Electromagnetic Force** (radiative captures, _∼_ 10<sup>_−_16</sup> s), or the **Weak Force** (beta-mediated captures, _∼_ 10<sup>_−_2</sup> s). 

-  **Conserved Quantities:** 

   - **Baryon Number (** _A_ **):** The total number of nucleons must be equal before and after the reaction. 

   - **Electric Charge (** _Z_ **):** Sum of atomic numbers is conserved. 

   - **Total Angular Momentum (J):** The vector sum of spin and orbital angular momenta is conserved: **J** _a_ + **J** _X_ + **L** _i_ = **J** _b_ + **J** _Y_ + **L** _f_ . 

   - **Spatial Parity (** Π **):** Conserved in strong and electromagnetic reactions: Π _a ·_ Π _X ·_ ( _−_ 1)<sup>_li_</sup> = Π _b ·_ Π _Y ·_ ( _−_ 1)<sup>_lf_</sup> . Violating parity is restricted strictly to weak-interactionmediated reactions. 

   - **Isospin (** _I_ **):** Strictly conserved in strong nuclear reactions; violated in electromagnetic and weak reactions. 

6 

GATE PHYSICS 

NUCLEAR REACTIONS & DETECTORS 

### **4. Derivation Milestones** 

The threshold energy _E_ th is derived via these critical center-of-mass kinematic steps: 

1. **Center-of-Mass Frame Formulation:** In the center-of-mass (CM) frame, the total momentum of the system is by definition zero. The total available energy in the CM frame is the sum of the Q-value and the kinetic energies of the reactants: 



<!-- Start of picture text -->
E available, CM =  Ea, cm +  EX, cm +  Q (18)<br><!-- End of picture text -->

At the threshold limit, the products _b_ and _Y_ must be created completely at rest in the CM frame (possessing zero relative kinetic energy, _Eb,_ cm = _EY,_ cm = 0). Thus, the threshold condition in the CM frame is: 



<!-- Start of picture text -->
Ea, cm +  EX, cm +  Q  = 0 = ⇒ E kin, cm =  −Q (19)<br><!-- End of picture text -->

2. **Relating CM Kinetic Energy to Lab Kinetic Energy:** Relate the total kinetic energy in the CM frame to the incident kinetic energy in the laboratory frame _Ea_ using the reduced mass relation: 



<!-- Start of picture text -->
MX<br>E kin, cm =  Ea (20)<br>� Ma  +  MX �<br><!-- End of picture text -->

3. **Equating Threshold Terms:** Equate the minimum required CM kinetic energy to _−Q_ : 



<!-- Start of picture text -->
MX<br>E th =  −Q (21)<br>� Ma  +  MX �<br><!-- End of picture text -->

4. **Isolating** _E_ **th:** Solve for the laboratory threshold energy _E_ th: 



<!-- Start of picture text -->
E th =  −Q =  −Q 1 + Ma (22)<br>� MaM  + X MX � � MX �<br><!-- End of picture text -->

### **5. Problem-Solving Algorithm** 

#### **Nuclear Reaction Kinematics** 

1. **Calculate the Q-Value:** Given the rest masses of the reactants and products in atomic mass units (u): 



<!-- Start of picture text -->
Q  = [( Ma  +  MX )  − ( Mb  +  MY  )]  ×  931 . 5 MeV (23)<br><!-- End of picture text -->

2. **Classify the Reaction:** 



<!-- Start of picture text -->
 If Q >  0: The reaction is exothermic. The threshold energy is E th = 0.<br><!-- End of picture text -->



<!-- Start of picture text -->
 If Q <  0: The reaction is endothermic. Proceed to step 3.<br><!-- End of picture text -->

3. **Calculate the Threshold Energy (** _E_ **th):** 



<!-- Start of picture text -->
E th =  −Q 1 + Ma (24)<br>� MX �<br><!-- End of picture text -->

*Ensure you use the mass of the projectile _Ma_ and the mass of the stationary target _MX_ in the ratio.* 

7 

GATE PHYSICS 

NUCLEAR REACTIONS & DETECTORS 

### **6. Crucial Pitfalls** 

#### **Reaction Kinematics Traps to Avoid** 

-  **Mass Ratio Inversion:** Confusing the mass ratio in the threshold equation. The ratio is strictly **<sup>_M_</sup> _M_<sup><u>pro</u></sup> target<sup><u>jectile</u>**,i.e.,</sup> _MMXa_<sup>.Invertingthisto</sup><sup>_M_</sup> _M_<sup>_<u>X</u>_</sup> _a_<sup>isahighlycommon</sup> calculation error, especially when the projectile is heavier than the target. 

-  **Confusing Atomic and Nuclear Masses:** When calculating the Q-value from atomic tables, ensure you do not double-count electron binding energies. As long as the number of protons is conserved, the electron masses cancel out. However, for positron decay ( _β_<sup>+</sup> ), you must manually subtract 2 _mec_<sup>2</sup> if using atomic masses. 

-  **Threshold and Potential Barrier Separation:** Forgetting that the threshold energy is a kinematic minimum. Even if _Ea ≥ E_ th, the reaction cross-section may remain zero if the projectile lacks the energy to overcome the repulsive electrostatic _<u>zZe</u>_<sup>2</sup> 

- Coulomb barrier _Vc_ = 4 _πϵ_ 0( _Ra_ + _RX_ )<sup>.Theprojectilemusttypicallyovercomethe</sup> larger of the two barriers: _Ea ≥ E_ th and _Ea ≥ Vc_ . 

#### **Standard Textbook System:** 

The endothermic reaction<sup>14</sup> N( _α, p_ )<sup>17</sup> O: 



<!-- Start of picture text -->
α  + 14 N  → 17 O +  p<br><!-- End of picture text -->

Using mass data ( _Mα ≈_ 4 _._ 0026 u, _M_ (<sup>14</sup> N) _≈_ 14 _._ 0031 u, _M_ (<sup>17</sup> O) _≈_ 16 _._ 9991 u, _Mp ≈_ 1 _._ 0078 u), the Q-value is calculated to be _Q ≈−_ 1 _._ 19 MeV. The kinematic threshold is: 



<!-- Start of picture text -->
E th = 1 . 19 1 + 4 ≈ 1 . 53 MeV<br>� 14 �<br><!-- End of picture text -->

### **7. Standard Textbook Systems** 

-  **The**<sup>10</sup> **B** ( _n, α_ )<sup>7</sup> **Li Reaction:** A classic exothermic neutron absorption reaction used in nuclear engineering for control rods and neutron detectors. It has a high cross-section for thermal neutrons, releasing _Q ≈_ 2 _._ 79 MeV. 

-  **The**<sup>3</sup> **H** ( _d, n_ )<sup>4</sup> **He Fusion Reaction:** The premier D-T fusion reaction, releasing a massive _Q ≈_ 17 _._ 6 MeV. The energy is shared as kinetic energy of the neutron (14 _._ 1 MeV) and the alpha particle (3 _._ 5 MeV). 

8 

GATE PHYSICS 

NUCLEAR REACTIONS & DETECTORS 

## **3 The Physics of Nuclear Fission and Fusion** 

### **1. Core Theory** 

* **Nuclear Fission:** The splitting of a heavy, unstable nucleus into two medium-mass fragment nuclei, accompanied by the release of several neutrons and a large quantity of energy. * **Physical Origin:** The competing balance between the attractive, short-range strong nuclear force (Surface Energy) and the repulsive, long-range electrostatic force (Coulomb Energy). For heavy nuclei, the Coulomb repulsion scales quadratically with charge ( _Z_<sup>2</sup> ), outstripping the linear scaling of the strong volume term. Deforming the nucleus increases its surface area (penalizing surface energy) but increases the average proton separation (reducing Coulomb repulsion). If the deformation exceeds an activation barrier, the nucleus undergoes fission. * **Nuclear Fusion:** The combining of two light nuclei to form a single, more tightly bound, heavier nucleus. * **Physical Origin:** Light nuclei have a very small binding energy per nucleon ( _B/A_ ) due to their large surface-to-volume ratio. Combining them increases the volume-to-surface ratio, drastically increasing the binding energy. However, the nuclei must first overcome the massive electrostatic Coulomb repulsion barrier (the **Gamow Peak**) to bring them within range of the attractive strong nuclear force ( _r ≤_ 1 fm). 

### **2. Mathematical Framework** 

* **Fission Activation Energy (Bohr-Wheeler Condition):** Using the liquid drop model, deform a spherical nucleus into a prolate spheroid with semi-major axis _a_ = _R_ (1 + _ϵ_ ) and semiminor axis _b_ = _R_ (1 _− ϵ/_ 2). The change in energy is: 



<!-- Start of picture text -->
Z 2<br>∆ E = ∆ Es  + ∆ Ec = ϵ 2 (25)<br>� 52 asA 2 / 3  − 5 1 ac A 1 / 3 �<br><!-- End of picture text -->

The activation barrier vanishes entirely, allowing spontaneous fission, when the Coulomb term exceeds the surface term: 



<!-- Start of picture text -->
Z 2<br>≈ 47  − 50 (26)<br>A ≥ 2 a a c s<br><!-- End of picture text -->

* **Neutron Economy Multiplication Factor ( _k_ ):** Governs the chain reaction rate in a nuclear reactor: 



<!-- Start of picture text -->
Number of neutrons in one generation<br>k = (27)<br>Number of neutrons in the preceding generation<br><!-- End of picture text -->

* _k <_ 1: Subcritical (chain reaction dies out). * _k_ = 1: Critical (steady-state power generation). * _k >_ 1: Supercritical (exponential power surge). * **Lawson Criterion for Fusion:** The condition required for a fusion reactor to achieve net power gain (breakeven), where the fusion power released exceeds the thermal conduction and radiation losses: 



<!-- Start of picture text -->
12 kBT<br>nτE ≥ = ⇒ nτE ≥ 10 20 s/m 3 (for D-T fusion at T ≈ 10 8 K) (28)<br>⟨σv⟩Q fusion<br><!-- End of picture text -->

where _n_ is the ion plasma density, _τE_ is the energy confinement time, and _⟨σv⟩_ is the Maxwellianaveraged fusion cross-section. 

### **3. Conservation Laws & Symmetries** 

* **Governing Forces:** Both fission and fusion processes are mediated by the **Strong Nuclear Force** (energy release and binding) and the **Electromagnetic Force** (Coulomb barrier and repulsion). * **Conserved Quantities:** * **Baryon Number ( _A_ ):** Conserved strictly. * **Lepton Number ( _L_ ):** Conserved strictly. * **Electric Charge ( _Z_ ):** Conserved strictly. * **Total Angular Momentum ( _J_ ) and Parity (Π):** Conserved in both processes. * **Isospin ( _I_ ):** Violated in fission due to the large Coulomb contribution of the heavy reactants; approximately conserved in light fusion reactions. 

9 

GATE PHYSICS 

NUCLEAR REACTIONS & DETECTORS 

### **4. Derivation Milestones** 

The Bohr-Wheeler condition is derived via these critical geometric steps: 

1. **Spheroid Deformation Volume Preservation:** Deform a sphere of radius _R_ into an ellipsoid with axes _R_ 1 = _R_ (1 + _ϵ_ ) and _R_ 2 = _R_ 3 = _R_ (1 + _ϵ_ )<sup>_−_1</sup><sup>_/_2</sup> to preserve volume: 



<!-- Start of picture text -->
V = 4 (29)<br>3 πR 1 R 2 R 3 = 4 3 πR 3 = constant<br><!-- End of picture text -->

2. **Surface Area Expansion:** Calculate the surface area of the spheroid as a power series in the deformation parameter _ϵ_ : 



<!-- Start of picture text -->
S ( ϵ )  ≈ 4 πR 2 1 + 2 = ⇒ Es ( ϵ ) =  Es 0 1 + 2 (30)<br>� 5 ϵ 2 � � 5 ϵ 2 �<br><!-- End of picture text -->

3. **Coulomb Energy Reduction:** Calculate the electrostatic energy of the spheroidal charge distribution: 



<!-- Start of picture text -->
Ec ( ϵ )  ≈ Ec 0 1  − 1 (31)<br>� 5 ϵ 2 �<br><!-- End of picture text -->

4. **Determining Spontaneous Fission Limits:** Sum the terms to find the net change in energy: 



<!-- Start of picture text -->
∆ E =  Es ( ϵ ) +  Ec ( ϵ )  − ( Es 0 +  E c 0) =  ϵ 2 � 52 E s 0 − 5 1 E c 0 � (32)<br><!-- End of picture text -->

For the system to be unstable to spontaneous deformation, the net energy change must be negative (∆ _E <_ 0): 



<!-- Start of picture text -->
1 c > 2 s = ⇒ E c 0 >  2 (33)<br>5 E 0 5 E 0 Es 0<br>Substituting Ec 0 = acZ 2 /A 1 / 3 and E s 0 = asA 2 / 3 yields the spontaneous fission parameter<br>limit:<br>Z 2<br>≈ 47  − 50 (34)<br>A ≥ 2 a a c s<br><!-- End of picture text -->

### **5. Problem-Solving Algorithm** 

- **Fission and Fusion Energy Calculations** 1. **Determine the Mass Defect of Fission/Fusion:** Calculate the difference in masses: 



<!-- Start of picture text -->
∆ m  =  M initial  − M final (35)<br><!-- End of picture text -->

2. **Calculate Energy Release (Q-value):** 



<!-- Start of picture text -->
Q  = ∆ m ×  931 . 5 MeV (36)<br><!-- End of picture text -->



<!-- Start of picture text -->
3. Evaluate Coulomb Barrier for Fusion: To estimate the temperature required<br>to initiate fusion, calculate the Coulomb potential at the contact radius R  =  R 1 +<br>R 2 =  r 0( A 1 1 / 3 +  A 1 2 / 3 ):<br>1 . 44  · Z 1 Z 2<br>Vc = MeV (using r 0 ≈ 1 . 2 fm) (37)<br>r 0( A 1 1 / 3 +  A 1 2 / 3 )<br><!-- End of picture text -->

The average thermal kinetic energy required is _kBT ≈ Vc_ . (Typically, quantum tunneling reduces this requirement by a factor of 10). 

10 

GATE PHYSICS 

NUCLEAR REACTIONS & DETECTORS 

### **6. Crucial Pitfalls** 

#### **Fission and Fusion Traps to Avoid** 

-  **The Spontaneous vs. Induced Fission Limit Confusion:** Confusing _Z_<sup>2</sup> _/A ≥_ 47 with the threshold for induced fission. Nuclei like 235U and 239Pu have _Z_<sup>2</sup> _/A ≈_ 36, meaning their activation barrier is small ( _∼_ 5 _−_ 6 MeV) but non-zero. They require the absorption of a slow neutron to supply the excitation energy (via pairing stability) to overcome the barrier, whereas nuclei with _Z_<sup>2</sup> _/A ≥_ 47 undergo spontaneous fission instantly. 

-  **Fission Product Asymmetry Assumption:** Assuming fission split is always symmetric ( _A/_ 2 + _A/_ 2). Due to shell structure stabilization, heavy nuclei split asymmetricly, peaking near magic numbers _N_ = 82 ( _A ≈_ 140) and _Z_ = 50 ( _A ≈_ 95). 

-  **Lawson Confinement Density Units:** Confusing the units of _nτE_ . It is expressed in s _·_ cm<sup>_−_3</sup> in older texts (10<sup>14</sup> s _·_ cm<sup>_−_3</sup> ) but must be converted to s _·_ m<sup>_−_3</sup> (10<sup>20</sup> s _·_ m<sup>_−_3</sup> ) for SI calculations. 

### **7. Standard Textbook Systems** 

-  **Thermal Fission of Uranium-235 (**<sup>235</sup> **U** + _n →_<sup>141</sup> **Ba** +<sup>92</sup> **Kr** +3 _n_ **):** A classic induced fission system, releasing an average of 200 MeV per fission event, primarily distributed as kinetic energy of the fission fragments. 

-  **The Solar Proton-Proton (p-p) Chain:** The primary fusion process in main-sequence stars: 

   - 4 _p →_<sup>4</sup> He + 2 _e_<sup>+</sup> + 2 _νe_ + 2 _γ_ ( _Q ≈_ 26 _._ 7 MeV) (38) 

Demonstrates how slow, weak interactions ( _p_ + _p → d_ + _e_<sup>+</sup> + _νe_ ) act as the bottleneck rate-limiting step in stellar lifespans. 

11 

GATE PHYSICS 

NUCLEAR REACTIONS & DETECTORS 

## **4 Operating Principles of Particle Accelerators and Detectors** 

### **1. Core Theory** 

* **Cyclotrons:** Electromagnetic accelerators that utilize a static, uniform magnetic field to bend charged particles into circular orbits while an alternating electric field applied across two ”Dee”-shaped electrodes accelerates them twice per orbit. * **Relativistic Limitation:** As the particle accelerates to relativistic velocities, its inertial mass increases ( _m_ = _γm_ 0). This decreases the orbital frequency, causing the particle to desynchronize from the fixed RF electric field. This limitation is resolved by **Synchrocyclotrons** (which modulate the RF frequency) or **Synchrotrons** (which modulate both the magnetic field and the frequency to maintain a constant orbital radius). * **Detectors:** Instrumentation used to measure the energy, momentum, and position of ionizing radiation. * **Gas-Filled Detectors:** Utilize an electric field to collect the electron-ion pairs generated when radiation ionizes gas molecules. * *Ionization Chamber:* Low voltage; collects only primary ionizations (no gas multiplication). * *Proportional Counter:* Intermediate voltage; electrons gain enough kinetic energy to cause secondary ionizations, resulting in an output pulse proportional to the incident energy. * *Geiger-M¨uller (GM) Counter:* High voltage; secondary ionizations trigger a runaway Townsend avalanche across the entire anode wire, producing a massive, uniform pulse regardless of the initial ionizing energy (no energy resolution). * **Semiconductor Detectors:** Function as reverse-biased p-n junction diodes, where ionizing radiation generates electron-hole pairs. Because the energy required to create an electron-hole pair in a semiconductor is exceptionally low ( _≈_ 3 eV in Ge/Si) compared to gas ionization energy ( _≈_ 30 eV), they yield 10 times more charge carriers per unit of energy, resulting in superior energy resolution. 

### **2. Mathematical Framework** 

* **Cyclotron Resonance Condition:** Balancing the centrifugal force with the magnetic Lorentz force: 



<!-- Start of picture text -->
mv 2 =  qvB = ⇒ v = qBr (39)<br>r m<br><!-- End of picture text -->

The orbital frequency (Larmor frequency) is completely independent of the radius _r_ : 



<!-- Start of picture text -->
v<br>fc = (expressed in Hz) (40)<br>2 πr = 2 q πm B<br><!-- End of picture text -->

* **Maximum Kinetic Energy in a Cyclotron ( _E_ max):** Occurs at the outer radius _R_ of the Dee electrodes: 



<!-- Start of picture text -->
E max = 1 max = q 2 B 2 R 2 (expressed in Joules) (41)<br>2 mv 2 2 m<br><!-- End of picture text -->

* **Relativistic Cyclotron Frequency:** 



<!-- Start of picture text -->
qB<br>f relativistic = =  f 0 1  − (42)<br>2 πγm 0 � � vc �2<br><!-- End of picture text -->

* **Detector Charge Carrier Yield ( _N_ ):** The number of primary charge carriers generated by an incident radiation particle of energy _E_ 0: 



<!-- Start of picture text -->
N = E 0 (43)<br>w<br><!-- End of picture text -->

where _w_ is the average energy required to create a single electron-ion (or electron-hole) pair. The statistical energy resolution is limited by Fano fluctuations: 



<!-- Start of picture text -->
F · w<br>R Fano ≡ ∆ E ∝ (44)<br>E 0 � E 0<br><!-- End of picture text -->

where _F_ is the dimensionless Fano factor ( _F ≈_ 0 _._ 1 for semiconductors). 

12 

GATE PHYSICS 

NUCLEAR REACTIONS & DETECTORS 

### **3. Conservation Laws & Symmetries** 

* **Governing Forces:** Particle acceleration and detection are mediated strictly by the **Electromagnetic Force** (Lorentz forces, gas ionization, and electronic carrier generation). * **Conserved Quantities:** Total energy, momentum, charge, and angular momentum are strictly conserved during the detection and acceleration processes. 

### **4. Derivation Milestones** 

The maximum cyclotron energy is derived via these critical steps: 

1. **Lorentz Centripetal Balance:** Equate the centripetal force to the magnetic Lorentz force acting on a particle of charge _q_ moving perpendicular to a magnetic field _B_ : 



<!-- Start of picture text -->
mv 2<br>=  qvB = ⇒ p  =  mv =  qBr (45)<br>r<br><!-- End of picture text -->

where _p_ is the linear momentum of the particle. 

2. **Radius-Velocity Proportionality:** Show that the velocity scales linearly with orbit radius: _v_ = _<u>qmB</u> r_ . This proves that the orbital period remains constant: � � 



<!-- Start of picture text -->
T = 2 πr = 2 πm (46)<br>v qB<br><!-- End of picture text -->

3. **Asserting Maximum Boundary Conditions:** The maximum energy is reached when the orbital radius matches the outer boundary _R_ of the pole pieces, giving _v_ max =<sup>_<u>qBR</u>_</sup> _m_<sup>.</sup> 

4. **Constructing Energy Formulation:** Substitute _v_ max into the classical kinetic energy expression: 



<!-- Start of picture text -->
E max = 1 max = 1 = q 2 B 2 R 2 (47)<br>2 mv 2 2 m � qBRm �2 2 m<br><!-- End of picture text -->

### **5. Problem-Solving Algorithm** 

#### **Cyclotron and Detector Calculations** 

1. **Calculate Cyclotron Frequency:** Given magnetic field _B_ , particle mass _m_ , and charge _q_ : 



<!-- Start of picture text -->
fc = qB (48)<br>2 πm<br><!-- End of picture text -->

   - *Ensure you use _q_ = 1 _._ 6 _×_ 10<sup>_−_19</sup> C for protons/electrons and exact isotopic masses (e.g., _mp ≈_ 1 _._ 67 _×_ 10<sup>_−_27</sup> kg).* 

2. **Calculate Max Kinetic Energy (** _E_ **max):** 



<!-- Start of picture text -->
E max = q 2 B 2 R 2 (in Joules) (49)<br>2 m<br><!-- End of picture text -->

To convert to MeV, divide by 1 _._ 602 _×_ 10<sup>_−_13</sup> J/MeV. 

3. **Calculate Detector Resolution Yield (** _N_ **):** Given incident particle energy _E_ 0 and mean ionization energy _w_ : 



<!-- Start of picture text -->
N = E 0 (50)<br>w<br>Use this to calculate the statistical limit of resolution: ∆ E = √ F · N · w .<br><!-- End of picture text -->

13 

GATE PHYSICS 

NUCLEAR REACTIONS & DETECTORS 

### **6. Crucial Pitfalls** 

#### **Accelerator and Detector Traps to Avoid** 

-  **Using Relativistic Energy Formula Classically:** Attempting to apply the classical maximum energy formula _E_ max =<sup>_<u>q</u>_2</sup><sup>_B_</sup> 2 _m_<sup>2</sup><sup>_R_2</sup> to electrons at high energies. Because electron mass is small ( _me ≈_ 0 _._ 511 MeV _/c_<sup>2</sup> ), they become relativistic almost instantly (at _E ≥_ 100 keV). You must use relativistic dynamics: 

   - _E_ total = ~~�~~ _p_<sup>2</sup> _c_<sup>2</sup> + _m_<sup>2</sup> 0<sup>_c_4=</sup> ~~�~~ _q_<sup>2</sup> _B_<sup>2</sup> _R_<sup>2</sup> _c_<sup>2</sup> + _m_<sup>2</sup> 0<sup>_c_4</sup> (51) 

-  **The GM Gas Multiplication Error:** Assuming a Geiger-M¨uller counter can be used to measure different radiation energies. Because the Townsend avalanche saturates the gas volume, the output pulse amplitude is identical for a 10 keV X-ray and a 5 MeV alpha particle. It is strictly a counter, not a spectrometer. 

-  **Deuteron vs. Proton Mass Ratios:** Forgetting that a deuteron (<sup>2</sup> H<sup>+</sup> ) has twice the mass of a proton ( _md ≈_ 2 _mp_ ) but the same charge. In the same cyclotron setup ( _B, R_ ), a deuteron will have **half** the maximum kinetic energy and **half** the resonance frequency of a proton. 

### **7. Standard Textbook Systems** 

-  **Standard Proton Cyclotron (** _B_ = 1 _._ 5 **T,** _R_ = 0 _._ 5 **m):** A classic textbook system. The cyclotron frequency is calculated to be _fc ≈_ 22 _._ 9 MHz, and the maximum proton energy is _E_ max _≈_ 27 MeV, illustrating the limits where relativistic corrections begin to become necessary. 

-  **Silicon Lithium-Drifted [Si(Li)] Semiconductor Detector:** A standard high-resolution detector system used for X-ray spectroscopy. Because the average ionization energy is _w ≈_ 3 _._ 81 eV at liquid nitrogen temperatures, it achieves exceptional resolution, allowing for the separation of adjacent characteristic transition lines. 

14 

GATE PHYSICS 

NUCLEAR REACTIONS & DETECTORS 

## **References** 

1. Krane, Kenneth S. _Introductory Nuclear Physics_ . Wiley, 1987. 

2. Beiser, Arthur. _Concepts of Modern Physics_ . McGraw-Hill, 2003. 

3. Griffiths, David. _Introduction to Elementary Particles_ . Wiley, 1987. 

15 

GATE PHYSICS 

ELEMENTARY PARTICLES & SYMMETRIES 

# **GATE PHYSICS STUDY NOTES Elementary Particle Physics & Discrete Symmetries** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

|**Contents**||
|---|---|
|**1**<br>**Classification of Elementary Particles & The Quark Model**|**2**|
|**2**<br>**Fundamental Conservation Laws & Isospin Symmetry**|**5**|
|**3**<br>**Discrete Symmetries: C, P, T Invariance & The CPT Theorem**|**8**|



1 

GATE PHYSICS 

ELEMENTARY PARTICLES & SYMMETRIES 

## **1 Classification of Elementary Particles & The Quark Model** 

### **1. Core Theory** 

At the fundamental level, particles are classified according to their spin statistics, internal quantum numbers, and the specific fundamental interactions they experience: 

-  **Leptons (Spin-1/2 Fermions):** Fundamental, point-like particles that do not experience the strong nuclear force. There are six lepton flavors grouped into three generations: the electron ( _e_<sup>_−_</sup> ), muon ( _µ_<sup>_−_</sup> ), and tau ( _τ_<sup>_−_</sup> ), each accompanied by its corresponding neutrino ( _νe, νµ, ντ_ ). 

-  **Hadrons:** Composite particles possessing a finite spatial size ( _∼_ 1 fm) that experience the strong interaction. Hadrons are sub-divided into: 

   - **Baryons (Spin-1/2 or 3/2 Fermions):** Composed of three quarks ( _qqq_ ), carrying a baryon number of _B_ = 1. Examples include the proton, neutron, and hyperons. 

   - **Mesons (Integer Spin Bosons):** Composed of a quark-antiquark pair ( _qq_ ¯), carrying a baryon number of _B_ = 0. Examples include pions, kaons, and rho mesons. 

-  **Photons (Spin-1 Gauge Bosons):** The massless quantum mediators of the electromagnetic force, representing vector fields. 

-  **The Quark Model:** Postulates that all hadrons are formed from fundamental spin-1/2 constituent fields called **quarks**. Quarks carry fractional electric charge (+2 _/_ 3 _e_ or _−_ 1 _/_ 3 _e_ ), a baryon number of _B_ = 1 _/_ 3, and an additional internal charge called **color** (Red, Green, Blue) that mediates the strong color-force via gluon exchange. The six quark flavors are divided into three generations: Up ( _u_ ), Down ( _d_ ); Charm ( _c_ ), Strange ( _s_ ); Top ( _t_ ), Bottom ( _b_ ). 

### **2. Mathematical Framework** 

* **Fractional Quark Charges:** 



<!-- Start of picture text -->
Q ( u, c, t ) = + 2 Q ( d, s, b ) =  − 1 (1)<br>3 e, 3 e<br><!-- End of picture text -->

* **The Gell-Mann–Nishijima Formula:** Relates the electric charge ( _Q_ ) of any hadron to its isospin _z_ -projection ( _I_ 3), baryon number ( _B_ ), and flavor quantum numbers: 



<!-- Start of picture text -->
Q  =  I 3 + B  +  S  +  C′  +  B∗ +  T ′ =  I 3 + Y (2)<br>2 2<br><!-- End of picture text -->

where: 

 _S_ is **Strangeness** ( _S_ = _−_ 1 for the _s_ quark, _S_ = +1 for the _s_ ¯ antiquark). 



<!-- Start of picture text -->
 C ′ is **Charm** ( C ′ = +1 for the c quark).<br><!-- End of picture text -->



<!-- Start of picture text -->
 B ∗ is **Bottomness** ( B ∗ =  − 1 for the b quark).<br> T ′ is **Topness** ( T ′ = +1 for the t quark).<br><!-- End of picture text -->

-  _Y ≡ B_ + _S_ + _C_<sup>_′_</sup> + _B_<sup>_∗_</sup> + _T_<sup>_′_</sup> is the **Hypercharge**. 

2 

GATE PHYSICS 

ELEMENTARY PARTICLES & SYMMETRIES 

* **Baryon Color Singlet Constraint:** Because of color confinement, all physical hadrons must be colorless (”color singlets”). The color wave function of a baryon must be completely antisymmetric: 



<!-- Start of picture text -->
1<br>ξ color = √ 6 ( |RGB⟩−|RBG⟩ +  |GBR⟩−|GRB⟩ +  |BRG⟩−|BGR⟩ ) (3)<br><!-- End of picture text -->

* **Total Hadron Wave Function:** For a baryon (which is a fermion), the total wave function under the exchange of any two identical quarks must be completely antisymmetric: 

Ψtotal = _ψ_ space _ϕ_ flavor _χ_ spin _ξ_ color = Antisymmetric (4) 

Since _ξ_ color is antisymmetric, the remaining product _ψ_ space _ϕ_ flavor _χ_ spin must be **completely symmetric** under any quark exchange. 

### **3. Conservation Laws & Symmetries** 

* **Governing Forces:** Hadronic compositions and configurations are bound by the **Strong Force** (Quantum Chromodynamics, QCD), while leptons and hadrons undergo electro-weak decays. * **Conserved Quantities in Strong and Electromagnetic Interactions:** 

-  **Baryon Number ( _B_ ):** Conserved absolutely. Quarks have _B_ = 1 _/_ 3; antiquarks have _B_ = _−_ 1 _/_ 3. 

-  **Lepton Flavor Numbers ( _Le, µµ, Lτ_ ):** Conserved individually in all interactions. 

-  **Quark Flavors ( _S, C_<sup>_′_</sup> _, B_<sup>_∗_</sup> _, T_<sup>_′_</sup> ):** Conserved in Strong and EM interactions. 

* **Weak Interaction Flavor Violation:** The weak force violates flavor numbers (∆ _S_ = _±_ 1 _,_ ∆ _C_<sup>_′_</sup> = _±_ 1). Weak decay is the only mechanism that allows a quark to change its flavor (e.g., _s → u_ + _W_<sup>_−_</sup> ). 

### **4. Derivation Milestones** 

The quark model relies on Group Theory representations under the Lie Groups _SU_ (2) and _SU_ (3): 

1. **Meson** _SU_ (3) **Multiplets:** Combine a fundamental quark triplet **3** and an antiquark antitriplet<sup>**¯**</sup> **3** : 

**3** _⊗_<sup>**¯**</sup> **3** = **8** _⊕_ **1** (5) 

This mathematically derives the **Meson Nonet**, which consists of an octet (eight states) and a singlet. 

2. **Baryon** _SU_ (3) **Multiplets:** Combine three quark triplets: 



<!-- Start of picture text -->
3  ⊗ 3  ⊗ 3  =  10  ⊕ 8 M ⊕ 8 M ⊕ 1 (6)<br><!-- End of picture text -->

This derives the **Baryon Decuplet** (10 completely symmetric flavor states), two **Baryon Octets** (mixed symmetry), and a **Baryon Singlet** (completely antisymmetric). 

3. **Introduction of Color:** Consider the ∆<sup>++</sup> baryon ( _uuu_ ) with spin _J_ = 3 _/_ 2 ( _Sz_ = +3 _/_ 2, all three spins aligned parallel _↑↑↑_ ). In the ground state ( _l_ = 0), the spatial, flavor, and spin wave functions are all completely symmetric. Without color, the total wave function would be completely symmetric, violating the spin-statistics theorem (Pauli exclusion principle) for fermions. Introducing the completely antisymmetric color singlet state _ξ_ color resolves this paradox. 

3 

GATE PHYSICS 

ELEMENTARY PARTICLES & SYMMETRIES 

### **5. Problem-Solving Algorithm** 

#### **Predicting Hadron Composition from Quantum Numbers** 

1. **Identify Given Hadron Properties:** Note the electric charge _Q_ , baryon number _B_ , isospin _z_ -projection _I_ 3, and strangeness _S_ . 

2. **Formulate Linear Equations:** Write equations for the number of Up ( _Nu_ ), Down ( _Nd_ ), and Strange ( _Ns_ ) quarks in the hadron (assuming only _u, d, s_ flavors are present): 



<!-- Start of picture text -->
B = 1 (7)<br>3 ( Nu  +  Nd  +  Ns )  − 1 3 ( Nu ¯ +  Nd  ¯ +  Ns ¯)<br>S =  −Ns  +  Ns ¯ (8)<br><!-- End of picture text -->



<!-- Start of picture text -->
Q  = 2 (9)<br>3 ( Nu − Nu ¯)  − 1 3 ( Nd − Nd  ¯)  − 1 3 ( Ns − Ns ¯)<br><!-- End of picture text -->

3. **Solve for Quark Counts:** Use the fact that for a baryon, _Nu_ + _Nd_ + _Ns_ = 3 (and anti-quark counts are zero). For a meson, _Nq_ = 1 _, Nq_ ¯ = 1. 

4. **Verify with Isospin:** Check that _I_ 3 = 2<sup><u>1</u>(</sup><sup>_Nu −Nu_¯)</sup><sup>_−_</sup><sup><u>1</u></sup> 2<sup>(</sup><sup>_Nd −Nd_¯)matchesthegiven</sup> isospin. 

### **6. Crucial Pitfalls** 

#### **Quark Model Traps to Avoid** 

-  **The Strangeness Sign Trap:** Forgetting that the strange quark has a **negative** strangeness ( _S_ = _−_ 1) despite its fractional charge of _Q_ = _−_ 1 _/_ 3. The _s_ ¯ antiquark has positive strangeness ( _S_ = +1). 

-  **Meson Baryon Number Error:** Assigning a baryon number of _B_ = 1 _/_ 3 to a meson because it contains a quark. Remember that a meson has _B_ = 0 because the quark ( _B_ = 1 _/_ 3) and antiquark ( _B_ = _−_ 1 _/_ 3) cancel each other out. 

### **7. Standard Textbook Systems** 

-  **The Baryon Decuplet (** ∆<sup>++</sup> _,_ ∆<sup>+</sup> _,_ ∆<sup>0</sup> _,_ ∆<sup>_−_</sup> **):** Illustrates completely symmetric spin-flavor states under _SU_ (3) where color plays a mandatory role. The ∆<sup>++</sup> is composed of _uuu_ with spin 3 _/_ 2. 

-  **The Light Pseudo-scalar Meson Octet (** _π_<sup>+</sup> _, π_<sup>0</sup> _, π_<sup>_−_</sup> _, K_<sup>+</sup> _, K_<sup>0</sup> _, K_<sup>¯0</sup> _, K_<sup>_−_</sup> _, η_ **):** Composed of _u, d, s_ quarks and antiquarks with orbital angular momentum _l_ = 0 and antiparallel spins ( _S_ = 0), yielding spin-parity _J_<sup>Π</sup> = 0<sup>_−_</sup> . 

4 

GATE PHYSICS 

ELEMENTARY PARTICLES & SYMMETRIES 

## **2 Fundamental Conservation Laws & Isospin Symmetry** 

### **1. Core Theory** 

* **Conservation Laws:** In particle physics, reactions are governed by strict symmetries. According to **Noether’s Theorem**, every continuous physical symmetry corresponds to a conserved conservation law: 

-  **Space-time Translation Symmetries:** Lead to the exact conservation of energy and momentum. 

-  **Rotational Invariance:** Leads to the conservation of angular momentum. 

-  **Gauge Invariance:** Leads to the exact conservation of electric charge. 

* **Isospin Symmetry (** _I_ **):** An approximate symmetry of the strong nuclear force under the exchange of up ( _u_ ) and down ( _d_ ) quarks (or protons and neutrons). Because the strong interaction is completely blind to electric charge, it treats up and down quarks identically. * **Origin:** Mathematically modeled using the _SU_ (2) Lie group, completely analogous to quantum spin. Protons and neutrons are grouped as a single **isospin doublet** (nucleon, _I_ = 1 _/_ 2), while pions form an **isospin triplet** ( _I_ = 1). 

### **2. Mathematical Framework** 

* **Isospin Algebra:** The isospin operators _I_<sup>ˆ</sup> _x, I_<sup>ˆ</sup> _y, I_<sup>ˆ</sup> _z_ satisfy the angular momentum commutation relations: 



<!-- Start of picture text -->
[ I ˆ i, I ˆ j ] =  iϵijkI ˆ k (10)<br><!-- End of picture text -->



<!-- Start of picture text -->
* Isospin Doublet (Nucleons, I = 1 / 2 ):<br><!-- End of picture text -->



<!-- Start of picture text -->
|p⟩ =  | 1 / 2 ,  +1 / 2 ⟩, |n⟩ =  | 1 / 2 , − 1 / 2 ⟩ (11)<br><!-- End of picture text -->

* **Isospin Triplet (Pions,** _I_ = 1 **):** 



<!-- Start of picture text -->
|π + ⟩ =  | 1 ,  +1 ⟩, |π 0 ⟩ =  | 1 ,  0 ⟩, |π − ⟩ =  | 1 , − 1 ⟩ (12)<br><!-- End of picture text -->

* **Isospin Amplitude Decomposition:** For a reaction such as pion-nucleon scattering ( _π_ + _N → π_ + _N_ ), the initial and final states are coupled isospin states _|Iπ, IN_ ; _I, I_ 3 _⟩_ where _I_ can be 3 _/_ 2 or 1 _/_ 2. The transition amplitudes are determined by Clebsch-Gordan expansions: 



<!-- Start of picture text -->
M =  ⟨ Ψ f |H ˆ strong | Ψ i⟩ = � Cf ( I ) C i ( I ) AI (13)<br>I<br><!-- End of picture text -->

where _A_ 3 _/_ 2 and _A_ 1 _/_ 2 are the transition amplitudes for the pure isospin channels _I_ = 3 _/_ 2 and _I_ = 1 _/_ 2, and _C_<sup>(</sup><sup>_I_)</sup> are the Clebsch-Gordan coefficients. 

### **3. Conservation Laws & Symmetries** 

- **Interaction Dependency of Isospin Conservation:** 

   -  **Strong Interaction:** Strictly conserves both total isospin _I_ and its _z_ -projection _I_ 3 (∆ _I_ = 0 _,_ ∆ _I_ 3 = 0). 

5 

GATE PHYSICS 

ELEMENTARY PARTICLES & SYMMETRIES 

-  **Electromagnetic Interaction:** Conserves _I_ 3 (∆ _I_ 3 = 0), but violates total isospin _I_ (∆ _I̸_ = 0) because the EM force distinguishes between different charges (e.g., protons and neutrons have different charges). 

-  **Weak Interaction:** Violates both total isospin _I_ and _I_ 3 (∆ _I̸_ = 0 _,_ ∆ _I_ 3 _̸_ = 0). 

### **4. Derivation Milestones** 

Let us derive the relative cross-sections for pion-nucleon scattering channels at the ∆(1232) resonance ( _I_ = 3 _/_ 2 dominant channel, _A_ 3 _/_ 2 _≫ A_ 1 _/_ 2): 

1. **Construct Coupled States using Clebsch-Gordan Expansion:** 



<!-- Start of picture text -->
|π + p⟩ =  | 1 ,  1 ⟩| 1 / 2 ,  1 / 2 ⟩ =  | 3 / 2 ,  3 / 2 ⟩ (14)<br><!-- End of picture text -->



<!-- Start of picture text -->
1 2<br>|π − p⟩ =  | 1 , − 1 ⟩| 1 / 2 ,  1 / 2 ⟩ = √ 3 | 3 / 2 , − 1 / 2 ⟩− � 3 | 1 / 2 , − 1 / 2 ⟩ (15)<br><!-- End of picture text -->



<!-- Start of picture text -->
2<br>|π 0 n⟩ =  | 1 ,  0 ⟩| 1 / 2 , − 1 / 2 ⟩ = (16)<br>� 3 | 3 / 2 , − 1 / 2 ⟩ + √ 1 3 | 1 / 2 , − 1 / 2 ⟩<br><!-- End of picture text -->

2. **Formulate the Scattering Amplitudes (** _M_ **):** 



<!-- Start of picture text -->
M ( π + p → π + p ) =  ⟨ 3 / 2 |H ˆ | 3 / 2 ⟩ =  A 3 / 2 (17)<br><!-- End of picture text -->



<!-- Start of picture text -->
M ( π − p → π − p ) = 1 (18)<br>3 A 3 / 2 + 2 3 A 1 / 2<br><!-- End of picture text -->



<!-- Start of picture text -->
√ 2 √ 2<br>M ( π − p → π 0 n ) = 3 A 3 / 2  − 3 A 1 / 2 (19)<br><!-- End of picture text -->

3. **Apply the resonance condition (** _A_ 3 _/_ 2 _≫ A_ 1 _/_ 2 **):** Set _A_ 1 _/_ 2 _≈_ 0: 



<!-- Start of picture text -->
M ( π + p → π + p )  ≈ A 3 / 2 , M ( π − p → π − p )  ≈ 3 1 A 3 / 2 , M ( π − p → π 0 n )  ≈ √ 32 A 3 / 2 (20)<br><!-- End of picture text -->

4. **Square the Amplitudes to find Cross-Section Ratios (** _σ ∝|M |_<sup>2</sup> **):** 



<!-- Start of picture text -->
σ ( π + p → π + p ) :  σ ( π − p → π − p ) :  σ ( π − p → π 0 n ) = 1 : 1 (21)<br>9 : 9 2 = 9 : 1 : 2<br><!-- End of picture text -->

6 

GATE PHYSICS 

ELEMENTARY PARTICLES & SYMMETRIES 

### **5. Problem-Solving Algorithm** 

#### **Verifying Allowed Particle Reactions** 

1. **Verify Exact Conservation Laws:** Check that energy, momentum, angular momentum, and electric charge ( _Q_ ) are strictly conserved. 

2. **Check Baryon (** _B_ **) and Lepton (** _Li_ **) Numbers:** Ensure<sup>�</sup> _B_ initial =<sup>�</sup> _B_ final and � _Li,_ initial = � _Li,_ final. 

3. **Evaluate Strangeness and Flavor changes:** * If strangeness is conserved (∆ _S_ = 0), the reaction can occur via the **Strong** or **EM** force. * If strangeness is violated by ∆ _S_ = _±_ 1, the reaction can only occur via the **Weak** force. * If ∆ _S >_ 1, the reaction is strictly forbidden. 

4. **Apply Isospin Conservation rules (for Strong Force):** Verify that the total initial isospin vector **I** initial = **I** 1 + **I** 2 can couple to the final isospin vector **I** final = **I** 3 + **I** 4 using the triangle inequality: 

_|I_ 1 _− I_ 2 _| ≤ I ≤ I_ 1 + _I_ 2 (22) 

### **6. Crucial Pitfalls** 

#### **Isospin Traps to Avoid** 

-  **Confusing Isospin of Pions and Nucleons:** Forgetting that pions are a triplet ( _I_ = 1) while nucleons are a doublet ( _I_ = 1 _/_ 2). 

-  **Attempting to conserve Isospin in Weak Decays:** Applying isospin conservation to weak decays like Λ<sup>0</sup> _→ p_ + _π_<sup>_−_</sup> . Since this is a weak decay (∆ _S_ = 1), isospin is **not conserved**. 

### **7. Standard Textbook Systems** 

-  **The Deuteron (**<sup>2</sup> **H):** The bound state of a proton and neutron. Since the spatial-spin state of the deuteron is symmetric (<sup>3</sup> _S_ 1 state), the generalized Pauli principle requires the isospin wave function to be completely antisymmetric, forcing the deuteron to be an **isospin singlet ( _I_ = 0)**. 

-  **Pion-Nucleon (** _π_ + _N_ **) Scattering:** Used to illustrate how approximate isospin symmetry dictates the branching ratios of strong reactions in the laboratory. 

7 

GATE PHYSICS 

ELEMENTARY PARTICLES & SYMMETRIES 

## **3 Discrete Symmetries: C, P, T Invariance & The CPT Theorem** 

### **1. Core Theory** 

Discrete symmetries describe the behavior of quantum states under non-continuous coordinate transformations: 

-  **Parity (Spatial Inversion,** _P_<sup>ˆ</sup> **):** Reflects all spatial coordinates through the origin: **r** _→−_ **r** . Under Parity, true vectors (position, momentum) reverse sign, while axial vectors (angular momentum, spin, magnetic field) remain invariant. 

-  **Charge Conjugation (Particle-Antiparticle Conjugation,** _C_<sup>ˆ</sup> **):** Converts every particle into its corresponding antiparticle, reversing all internal charges (electric charge, baryon number, lepton number, strangeness) while preserving mass, spin, and momentum. 

-  **Time Reversal (Time Inversion,** _T_<sup>ˆ</sup> **):** Reverses the direction of time flow: _t →−t_ . Under T, velocity, linear momentum, and spin reverse sign, while position and electric field do not. 

-  **The CPT Theorem:** A fundamental theorem of quantum field theory stating that any local, Lorentz-invariant, Hermitian quantum field theory is strictly invariant under the combined operation of _C_<sup>ˆ</sup> , _P_<sup>ˆ</sup> , and _T_<sup>ˆ</sup> in any order ( _C_<sup>ˆ</sup> _P_<sup>ˆ</sup> _T_<sup>ˆ</sup> = 1). This guarantees that a particle and its antiparticle have exactly identical masses, lifetimes, and opposite magnetic moments. 

### **2. Mathematical Framework** 

* **Parity Eigenvalues (** Π **):** 

_P_ ˆ<sup>2</sup> = 1 = _⇒_ Π = _±_ 1 (23) 

* For orbital states, the spatial parity is Π = ( _−_ 1)<sup>_l_</sup> . * For a composite **meson** ( _qq_ ¯): Since antiquarks have opposite intrinsic parity to quarks ( _Pq_ ¯ = _−Pq_ ), the total parity is: 

_P_ meson = _PqPq_ ¯( _−_ 1)<sup>_l_</sup> = (+1)( _−_ 1)( _−_ 1)<sup>_l_</sup> = ( _−_ 1)<sup>_l_+1</sup> (24) 

* For a composite **baryon** ( _qqq_ ): Since quarks all have positive intrinsic parity, the total parity is: 



<!-- Start of picture text -->
P baryon = ( Pq ) 3 ( − 1) L = ( − 1) L (25)<br><!-- End of picture text -->

* **Charge Conjugation Eigenvalues (** _C_ **):** Only completely neutral bosons can be eigenstates of _C_ ˆ: * For a neutral meson with orbital angular momentum _l_ and total spin _S_ : 

_C_ = ( _−_ 1)<sup>_l_+</sup><sup>_S_</sup> (26) 

* For a photon ( _γ_ ): Since the electromagnetic vector potential **A** changes sign under charge conjugation (reversing charges reverses currents and fields), the photon is _C_ -odd: 



<!-- Start of picture text -->
Cγ =  − 1 = ⇒ C ( nγ ) = ( − 1) n (27)<br><!-- End of picture text -->

* **G-Parity:** Because charge conjugation only applies to neutral states, **G-Parity** is defined as a combination of charge conjugation and a 180<sup>_◦_</sup> isospin rotation about the _y_ -axis, allowing it to describe charged states of pions: 



<!-- Start of picture text -->
G ≡ Ce ˆ iπI 2 = ( − 1) I C neutral (28)<br><!-- End of picture text -->

For pions ( _I_ = 1 _, C_ neutral = +1), G-parity is strictly: 



<!-- Start of picture text -->
Gπ =  − 1 (29)<br><!-- End of picture text -->

8 

GATE PHYSICS 

ELEMENTARY PARTICLES & SYMMETRIES 

### **3. Conservation Laws & Symmetries** 

- **Symmetry Violations by Fundamental Forces:** 

   -  **Strong Interaction:** Strictly conserves _C_ , _P_ , _T_ , _CP_ , and _G_ -parity. 

   -  **Electromagnetic Interaction:** Strictly conserves _C_ , _P_ , _T_ , and _CP_ , but violates _G_ -parity. 

   -  **Weak Interaction:** Maximally violates _P_ and _C_ individually. It also violates _CP_ (and thus _T_ , by the CPT theorem) at a very small level ( _≈_ 10<sup>_−_3</sup> ). 

   -  **CPT Invariance:** Conserved absolutely by all fundamental interactions. 

### **4. Derivation Milestones** 

Let us derive why the G-parity of an _n_ -pion state is _G_ = ( _−_ 1)<sup>_n_</sup> , which restricts strong hadronic decays: 

1. **Establish G-Parity of a Single Pion:** The neutral pion _π_<sup>0</sup> is an eigenstate of _C_ with _C_ = +1 (since it decays to 2 _γ_ ). Its isospin is _I_ = 1. The G-parity is: 



<!-- Start of picture text -->
Gπ =  Ce iπI 2 = ( − 1) I C neutral = ( − 1) 1 (+1) =  − 1 (30)<br><!-- End of picture text -->

Because G-parity is a multiplicative quantum number and isospin rotations are symmetric for the entire triplet, all three pions ( _π_<sup>+</sup> _, π_<sup>0</sup> _, π_<sup>_−_</sup> ) have _G_ = _−_ 1. 

2. **Formulate Multi-Pion G-Parity:** For a state of _n_ pions, G-parity is multiplicative: 

   - _G_ ( _nπ_ ) = ( _Gπ_ )<sup>_n_</sup> = ( _−_ 1)<sup>_n_</sup> (31) 

3. **Strong Decay Restriction:** Since the strong interaction strictly conserves G-parity, any strong decay of a meson into pions must conserve this G-parity factor: 



<!-- Start of picture text -->
G parent = ( − 1) n pions (32)<br><!-- End of picture text -->

This explains why the _ρ_ meson ( _G_ = +1) can only decay into an even number of pions ( _ρ →_ 2 _π_ ), while the _ω_ meson ( _G_ = _−_ 1) decays into an odd number of pions ( _ω →_ 3 _π_ ). 

9 

GATE PHYSICS 

ELEMENTARY PARTICLES & SYMMETRIES 

### **5. Problem-Solving Algorithm** 

#### **Verifying Selection Rules for Electromagnetic and Strong Decays** 

1. **Check the Mediating Force:** Identify if the decay is Strong (no photons or leptons, short lifetime _∼_ 10<sup>_−_23</sup> s) or Electromagnetic (photons are emitted). 

2. **Apply Parity Conservation:** Verify that Π _i_ = Π _f_ (incorporating spatial parities ( _−_ 1)<sup>_l_</sup> ). 

3. **Apply Charge Conjugation (for EM and neutral states):** Ensure the initial and final states have matching _C_ -parity: 

_C_ initial = _C_ final 

(33) 

For _n_ photons in the final state, _C_ final = ( _−_ 1)<sup>_n_</sup> . 

4. **Apply G-Parity (for Strong decays involving pions):** Verify that _G_ initial = ( _−_ 1)<sup>_n_pions</sup> . 

### **6. Crucial Pitfalls** 

#### **Discrete Symmetry Traps to Avoid** 

-  **Applying C-Parity to Charged Particles:** Attempting to assign a _C_ -parity eigenvalue to charged particles like _π_<sup>+</sup> or electrons. Charged particles are **not eigenstates of C** because _C_<sup>ˆ</sup> _|π_<sup>+</sup> _⟩_ = _|π_<sup>_−_</sup> _⟩_ , which is a completely different physical state. Only completely neutral states can have a defined _C_ -parity. 

-  **Weak Decay Symmetry Conservation:** Attempting to enforce parity or charge conjugation conservation on weak decays. Remember that weak decays maximally violate both _P_ and _C_ . 

### **7. Standard Textbook Systems** 

-  **Neutral Pion Decay (** _π_<sup>0</sup> _→_ 2 _γ_ **vs.** _π_<sup>0</sup> _→_ 3 _γ_ **):** The neutral pion is a pseudo-scalar meson with _J_<sup>Π</sup> = 0<sup>_−_</sup> and _Cπ_ 0 = +1. * For a 2 _γ_ final state, _C_ 2 _γ_ = ( _−_ 1)<sup>2</sup> = +1. (Allowed, highly dominant decay mode). * For a 3 _γ_ final state, _C_ 3 _γ_ = ( _−_ 1)<sup>3</sup> = _−_ 1. (Strictly forbidden by _C_ -conservation). 

-  **The Wu**<sup>60</sup> **Co Beta Decay Experiment (1956):** Demonstrated **maximal parity violation in the weak interaction** by aligning the spins of<sup>60</sup> Co nuclei at low temperatures and observing a spatial asymmetry in the direction of emitted beta electrons relative to the spin axis. 

10 

GATE PHYSICS 

ELEMENTARY PARTICLES & SYMMETRIES 

## **References** 

1. Griffiths, David. _Introduction to Elementary Particles_ . Wiley, 1987. 

2. Krane, Kenneth S. _Introductory Nuclear Physics_ . Wiley, 1988. 

3. Beiser, Arthur. _Concepts of Modern Physics_ . McGraw-Hill, 2003. 

11 

