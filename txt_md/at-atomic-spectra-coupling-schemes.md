<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: at-atomic-spectra-coupling-schemes.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

GATE PHYSICS 

ATOMIC SPECTRA & COUPLING SCHEMES 

# **GATE PHYSICS STUDY NOTES Atomic Spectra, Coupling Schemes & Fine-Hyperfine Structure** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**<br>**Spectra of One- and Many-Electron Atoms**|**2**|
|---|---|
|**2**<br>**The Physics of the Spin-Orbit Interaction**|**5**|
|**3**<br>**L-S and j-j Coupling Schemes**|**8**|
|**4**<br>**Fine and Hyperfine Structures**|**11**|



1 

GATE PHYSICS 

ATOMIC SPECTRA & COUPLING SCHEMES 

## **1 Spectra of One- and Many-Electron Atoms** 

### **1. Core Theory** 

The study of **one-electron spectra** (e.g., Hydrogen, singly ionized Helium He<sup>+</sup> , doubly ionized Lithium Li<sup>2+</sup> ) and **many-electron spectra** (e.g., Helium, Alkali metals like Sodium) reveals the quantum structure of atomic shells. 

-  **One-Electron Atoms:** The spectral lines originate from transitions of a single valence electron orbiting a nucleus of charge _Ze_ . Because the electrostatic potential is purely Coulombic ( _V_ ( _r_ ) _∝_ 1 _/r_ ), states with different orbital angular momentum _l_ but the same principal quantum number _n_ are degenerate in unperturbed non-relativistic wave mechanics. This degeneracy is broken only by relativistic corrections (fine structure). 

-  **Many-Electron Atoms (Alkali Spectra):** In many-electron atoms, the inner closed shells of electrons screen the nuclear charge. The outer single valence electron experiences a nonCoulombic, centrally symmetric **effective potential** _V_ eff( _r_ ) that deviates from 1 _/r_ . Close to the nucleus, the electron experiences the bare nuclear charge _Z_ , whereas far away it experiences a shielded charge _Z_ eff _≈_ 1. Highly penetrating orbits (low _l_ , s- and p-states) penetrate the core and are more tightly bound than non-penetrating orbits (high _l_ , d- and f-states). This lifts the _l_ -degeneracy, splitting the unperturbed energy levels into distinct _s, p, d, f_ terms. 

### **2. Energy Level Framework** 

The mathematical energy eigenvalues are governed by the following formulations: 

-  **One-Electron (Hydrogenic) Energy Levels:** 



<!-- Start of picture text -->
µZ 2 e 4<br>En =  − (1)<br>32 π 2 ϵ 2 0 ℏ2 n 2 =  −R∞hc � Zn 2 2 � � mµe �<br><!-- End of picture text -->

where _n ∈{_ 1 _,_ 2 _,_ 3 _, . . . }_ is the principal quantum number, _µ_ = _mmee_ + _<u>MM</u>_<sup>isthereducedmassof</sup> _<u>mee</u>_<sup>4</sup> the electron-nucleus system, and _R∞_ = 8 _ϵ_<sup>2</sup> 0<sup>_h_3</sup><sup>_c≈_109737</sup><sup>_._3cm</sup><sup>_−_1istheRydbergconstant.</sup> 

-  **Alkali Metal (Many-Electron) Energy Levels:** To account for nuclear shielding, the energy terms are modeled using the **Rydberg-Ritz formula** containing the **quantum defect** _µl_ (or _σl_ ): 



<!-- Start of picture text -->
RAhc<br>Enl =  − (2)<br>( n − µl ) 2 =  − R ( n A∗hc ) 2<br><!-- End of picture text -->

where _n_<sup>_∗_</sup> = _n − µl_ is the **effective principal quantum number** . The quantum defect _µl_ is a constant for a given spectral series (fixed _l_ ) and decreases rapidly as _l_ increases: 



<!-- Start of picture text -->
µs > µp > µd > µf ≈ 0 (3)<br><!-- End of picture text -->

because high- _l_ states are non-penetrating, making their effective potential almost purely Coulombic. 

2 

GATE PHYSICS 

ATOMIC SPECTRA & COUPLING SCHEMES 

### **3. Selection Rules & Transitions** 

Electric dipole transitions (E1) are governed by rigorous quantum-mechanical selection rules: 

 **Principal Quantum Number:** ∆ _n_ is arbitrary (no restriction). 



<!-- Start of picture text -->
 Orbital Angular Momentum:<br><!-- End of picture text -->



<!-- Start of picture text -->
∆ l  =  ± 1 (4)<br><!-- End of picture text -->

This is a strict conservation law reflecting the parity of the photon (parity of state must change: ( _−_ 1)<sup>_l_</sup> _→−_ ( _−_ 1)<sup>_l_</sup> ). 

 **Magnetic Quantum Number:** 



<!-- Start of picture text -->
∆ ml = 0 , ± 1 (5)<br><!-- End of picture text -->

where ∆ _ml_ = 0 corresponds to linearly polarized light ( _π_ -transitions) and ∆ _ml_ = _±_ 1 corresponds to circularly polarized light ( _σ_ -transitions). 

### **4. Derivation Milestones** 

The lifted _l_ -degeneracy in alkali atoms is derived via the following mathematical steps: 

1. **Effective Central Potential Expansion:** Write the shielding potential as a perturbation to the Coulomb potential: _V_ ( _r_ ) = _−_ 4 _πϵe_<sup>2</sup> 0 _r_<sup>_−_</sup><sup>_<u>be</u>_</sup> _r_<sup>22.</sup> 

2. **Radial Schr¨odinger Modification:** Substitute _V_ ( _r_ ) into the radial wave equation, which shifts the centrifugal term: 



<!-- Start of picture text -->
l ( l  + 1)ℏ 2 − e 2<br>+  V  ( r )  → l∗ ( l∗ + 1)ℏ2 (6)<br>2 mr 2 2 mr 2 4 πϵ 0 r<br><!-- End of picture text -->

where the effective orbital quantum number _l_<sup>_∗_</sup> is solved from _l_<sup>_∗_</sup> ( _l_<sup>_∗_</sup> + 1) = _l_ ( _l_ + 1) _−_<sup><u>8</u></sup><sup>_<u>πϵ</u>_</sup><sup><u>0</u></sup> ℏ<sup>_<u>mbe</u>_22</sup> . 

3. **Solving for Effective Quantum Numbers:** Writing _l_<sup>_∗_</sup> = _l − δl_ . Substituting this into the hydrogenic radial solutions shifts the radial node termination conditions, giving an effective principal quantum number _n_<sup>_∗_</sup> = _n − δl_ . 

3 

GATE PHYSICS 

ATOMIC SPECTRA & COUPLING SCHEMES 

### **5. Problem-Solving Algorithm** 

#### **Analyzing Alkali Spectral Series and Transition Energies** 

1. **Identify the Spectral Series:** Know the standard terminology for alkali transitions: 

   -  **Sharp Series:** Transitions from upper _ns_ states to the lowest _p_ state ( _ns →_ 3 _p_ for Sodium). 

   -  **Principal Series:** Transitions from upper _np_ states to the lowest _s_ ground state ( _np →_ 3 _s_ for Sodium). 

   -  **Diffuse Series:** Transitions from upper _nd_ states to the lowest _p_ state ( _nd →_ 3 _p_ ). 

   -  **Fundamental Series:** Transitions from upper _nf_ states to the lowest _d_ state ( _nf →_ 3 _d_ ). 

2. **Calculate Effective Principal Quantum Numbers:** Use the unperturbed energies to find _n_<sup>_∗_</sup> : 



<!-- Start of picture text -->
RA<br>n ∗ = � |E obs |/hc = ⇒ µl =  n − n∗ (7)<br>Transition Wavenumbers: Subtract the term values ( T =  −E/hcE/hc ):<br>1 1<br>ν ¯ =  T upper  − T lower =  RA (8)<br>� ( n ∗ lower )2 − ( n ∗ upper) 2 �<br><!-- End of picture text -->

3. **Determine Transition Wavenumbers:** Subtract the term values ( _T_ = _−E/hcE/hc_ ): 

### **6. Crucial Pitfalls** 

#### **Common Errors in Single/Many Electron Spectra** 

-  **Reduced Mass Neglect:** Forgetting to use the reduced mass _µ_ instead of the bare electron mass _me_ . In hydrogenic systems like positronium or muonic atoms, this leads to massive errors (e.g., positronium’s Rydberg constant is exactly half of _R∞_ ). 

-  **Misapplying Degeneracy to Alkali Atoms:** Confusing Hydrogen with Sodium and assuming that 3 _s_ , 3 _p_ , and 3 _d_ states have the same energy. In Sodium, _E_ 3 _s < E_ 3 _p < E_ 3 _d_ due to core penetration. 

### **7. Standard Textbook Systems** 

-  **Positronium (** _e_<sup>+</sup> _e_<sup>_−_</sup> **):** An unstable system consisting of an electron and its antiparticle (positron) orbiting each other. The energy levels are hydrogenic, but with _µ_ = _me/_ 2, shifting all spectral lines by a factor of 2 compared to Hydrogen. 

-  **Lithium Atom (** _Z_ = 3 **):** The three electrons arrange as 1 _s_<sup>2</sup> 2 _s_<sup>1</sup> . The valence electron experiences the shielded nuclear charge _Z_ eff _≈_ 1 _._ 26 in the 2 _s_ state and _Z_ eff _≈_ 1 _._ 00 in nonpenetrating excited _d_ -states. 

4 

GATE PHYSICS 

ATOMIC SPECTRA & COUPLING SCHEMES 

## **2 The Physics of the Spin-Orbit Interaction** 

### **1. Core Theory** 

The **spin-orbit interaction** is a relativistic quantum correction resulting from the electromagnetic coupling between the electron’s spin magnetic dipole moment **_µ_** _s_ and the magnetic field **B** it experiences in its rest frame as it orbits the charged nucleus. Physically, from the perspective of the moving electron, the nucleus orbits the electron, creating an effective current loop that generates a magnetic field. The interaction of the electron’s spin magnetic moment with this induced field is modeled as **H** so = _−_ **_µ_** _s ·_ **B** . This relativistic coupling breaks the unperturbed spatial rotational symmetry, lifting the spin degeneracy and splitting spectral terms into fine-structure multiplets. 

### **2. Energy Level Framework** 

The relativistic spin-orbit Hamiltonian is: 



<!-- Start of picture text -->
1 dV ( r )<br>H ˆso =  ξ ( r ) L  ·  S  = L  ·  S (9)<br>2 m 2 ec 2 � 1 r dr �<br><!-- End of picture text -->

where **L** is the orbital angular momentum operator, **S** is the spin angular momentum operator, and _V_ ( _r_ ) is the central potential. 

For a hydrogenic Coulomb potential _V_ ( _r_ ) = _−_ 4<sup>_<u>Ze</u>_</sup> _πϵ_ 0<sup>2</sup> _r_<sup>,the spin-orbit parameter</sup><sup>_ξ_(</sup><sup>_r_) simplifies to:</sup> 



<!-- Start of picture text -->
Ze 2<br>ξ ( r ) = (10)<br>8 πϵ 0 m 2 ec 2 r 3<br><!-- End of picture text -->

The expectation value of 1 _/r_<sup>3</sup> in a state _|n, l⟩_ is: 



<!-- Start of picture text -->
Z 3<br>⟨r − 3 ⟩ = (11)<br>a 3 0 n 3 l ( l  + 1 / 2)( l  + 1)<br><!-- End of picture text -->

which is defined for _l >_ 0. The resulting first-order spin-orbit energy shift is: 



<!-- Start of picture text -->
∆ E so = a 2 nl [ j ( j  + 1)  − l ( l  + 1)  − s ( s  + 1)] (12)<br><!-- End of picture text -->

where the spin-orbit coupling constant _anl_ is: 



<!-- Start of picture text -->
Z 4 e 2 ℏ 2<br>anl = (13)<br>8 πϵ 0 m 2 ec 2 a 3 0 n 3 l ( l  + 1 / 2)( l  + 1) ∝ Z n 34<br><!-- End of picture text -->

The quantum numbers are: 



<!-- Start of picture text -->
 l : Orbital angular momentum quantum number.<br><!-- End of picture text -->



<!-- Start of picture text -->
 s  = 1 / 2: Spin quantum number.<br><!-- End of picture text -->



<!-- Start of picture text -->
 j ∈{l − 1 / 2 , l  + 1 / 2 } : Total angular momentum quantum number.<br><!-- End of picture text -->

### **3. Selection Rules & Transitions** 

Transitions between spin-orbit split states are governed by: 



<!-- Start of picture text -->
∆ l  =  ± 1 , ∆ j = 0 , ± 1 (but j = 0  → j = 0 is forbidden) (14)<br><!-- End of picture text -->



<!-- Start of picture text -->
∆ mj = 0 , ± 1 (15)<br><!-- End of picture text -->

5 

GATE PHYSICS 

ATOMIC SPECTRA & COUPLING SCHEMES 

### **4. Derivation Milestones** 

The derivation of the spin-orbit shift involves these critical mathematical steps: 

1. **Lorentz Boost and Relativistic Fields:** Transform the Coulomb electric field **E** = _−∇V_ in the lab frame to the moving frame of the electron, yielding the relativistic magnetic field: 



<!-- Start of picture text -->
1 dV<br>B  =  − v  ×  E = L (16)<br>c 2 meec 2 � 1 r dr �<br><!-- End of picture text -->

2. **Thomas Precession Correction:** The electron’s rest frame is undergoing accelerated, curved motion. Relativistic kinematics dictates a coordinate rotation rate called Thomas Precession, which reduces the effective field by exactly a factor of 2 (the Thomas factor): 



<!-- Start of picture text -->
B eff = 1 (17)<br>2 B<br><!-- End of picture text -->

3. **Formulating the Spin Coupling:** Multiply by the spin magnetic moment **_µ_** _s_ = _−gs_ 2 _me e_<sup>**S**</sup><sup>_≈_</sup> _− m_<sup>_<u>e</u>_</sup> _e_<sup>**S**(since</sup><sup>_gs≈_2),giving:</sup> 



<!-- Start of picture text -->
1 dV<br>H ˆso =  − µ s ·  B eff = L  ·  S (18)<br>2 m 2 ec 2 � 1 r dr �<br><!-- End of picture text -->

4. **Diagonalizing the L** _·_ **S Operator:** Introduce the total angular momentum **J** = **L** + **S** . Squaring both sides gives **J**<sup>2</sup> = **L**<sup>2</sup> + **S**<sup>2</sup> + 2 **L** _·_ **S** , which diagonalizes the coupling: 



<!-- Start of picture text -->
L  ·  S  = 1 � J 2 − L 2 − S 2� = ⇒⟨ L  ·  S ⟩ = ℏ2 (19)<br>2 2 [ j ( j  + 1)  − l ( l  + 1)  − s ( s  + 1)]<br><!-- End of picture text -->

### **5. Problem-Solving Algorithm** 

#### **Calculating Spin-Orbit Splittings and Term Spacings** 

1. **Determine the Allowed** _j_ **States:** For a given orbital term _L_ and spin _S_ , write down all possible total angular momentum states: _j_ = _|l − s|, . . . , l_ + _s_ . 

2. **Evaluate the Energy Shift for Each** _j_ **:** Compute ∆ _E_ so( _j_ ) =<sup>_<u>a</u>_</sup> 2<sup>_<u>nl</u>_[</sup><sup>_j_(</sup><sup>_j_+ 1)</sup><sup>_−l_(</sup><sup>_l_+</sup> 1) _− s_ ( _s_ + 1)]. 

3. **Calculate Multiplet Interval Spacings:** To find the energy separation between two adjacent states _j_ and _j −_ 1 in a multiplet: 



<!-- Start of picture text -->
∆ E ( j )  − ∆ E ( j − 1) = a 2 nl [ j ( j  + 1)  − ( j − 1) j ] =  anlj (20)<br><!-- End of picture text -->

This is **Land´e’s Interval Rule** : The energy spacing between adjacent fine-structure levels in a term is proportional to the larger _j_ value of the pair. 

6 

GATE PHYSICS 

ATOMIC SPECTRA & COUPLING SCHEMES 

### **6. Crucial Pitfalls** 

#### **Spin-Orbit Pitfalls** 

-  **Ignoring the Thomas Factor of 2:** Forgetting to divide the Lorentz-boosted magnetic interaction by 2, which leads to a factor-of-two overestimate of the fine-structure splitting. 

-  **Applying Spin-Orbit to s-States (** _l_ = 0 **):** Attempting to compute spin-orbit shifts for _l_ = 0 states. Since s-states have no orbital angular momentum ( **L** = 0), the expectation value of **L** _·_ **S** is zero. The fine structure of s-states is shaped solely by relativistic kinetic energy corrections and the Darwin term, not spin-orbit. 

### **7. Standard Textbook Systems** 

-  **The Sodium D-line Doublet (** 3 _p →_ 3 _s_ **):** The 3 _p_ state of Sodium is split by the spin-orbit interaction into 3 _p_ 3 _/_ 2 and 3 _p_ 1 _/_ 2. Transitions from these levels to the unsplit 3 _s_ 1 _/_ 2 ground state produce the famous yellow doublet lines: _D_ 2 (5890<sup>˚</sup> A) and _D_ 1 (5896<sup>˚</sup> A). 

7 

GATE PHYSICS 

ATOMIC SPECTRA & COUPLING SCHEMES 

## **3 L-S and j-j Coupling Schemes** 

### **1. Core Theory** 

In **many-electron atoms** , the total Hamiltonian contains electrostatic repulsions between electrons and relativistic spin-orbit couplings. The order in which these angular momenta are coupled defines two limiting angular momentum coupling schemes: 

-  **L-S (Russell-Saunders) Coupling:** Valid for **light atoms** ( _Z ≪_ 30), where the electrostatic repulsion between electrons is much stronger than the relativistic spin-orbit interaction. Here, individual orbital angular momenta **l** _i_ couple strongly to form a total orbital angular momentum **L** =<sup>�</sup> **l** _i_ , and individual spins **s** _i_ couple to form a total spin **S** =<sup>�</sup> **s** _i_ . Finally, the weaker spin-orbit interaction couples **L** and **S** to form the total angular momentum **J** = **L** + **S** . 

-  **j-j Coupling:** Valid for **heavy atoms** ( _Z ≫_ 30), where the relativistic spin-orbit interaction is extremely strong and dominates over the electrostatic repulsions. Here, the orbital and spin angular momenta of each individual electron couple first to form a single-electron total angular momentum **j** _i_ = **l** _i_ + **s** _i_ . Finally, the weaker electrostatic repulsions couple the individual **j** _i_ vectors to form the total angular momentum of the atom: **J** =<sup>�</sup> **j** _i_ . 

### **2. Energy Level Framework** 

The quantum numbers and states in both schemes are characterized as follows: 

-  **L-S Coupling Terms:** Represented in spectroscopic term notation: 



<!-- Start of picture text -->
2 S +1 LJ (21)<br><!-- End of picture text -->

where 2 _S_ + 1 is the spin multiplicity, _L_ is the spectroscopic symbol for total orbital angular momentum ( _S, P, D, F, . . ._ ), and _J_ is the total angular momentum quantum number: 



<!-- Start of picture text -->
|L − S| ≤ J ≤ L  +  S (22)<br><!-- End of picture text -->

-  **j-j Coupling Terms:** Denoted by listing individual electronic _j_ -values: 



<!-- Start of picture text -->
( j 1 , j 2) J (23)<br><!-- End of picture text -->

where the total angular momentum is bounded by: 



<!-- Start of picture text -->
|j 1  − j 2 | ≤ J ≤ j 1 +  j 2 (24)<br><!-- End of picture text -->

### **3. Selection Rules & Transitions** 

The E1 selection rules differ dramatically between the two coupling regimes: 

-  **Selection Rules in L-S Coupling:** 



<!-- Start of picture text -->
∆ S = 0 , ∆ L  = 0 , ± 1 , ∆ J = 0 , ± 1 ( J = 0  → J = 0 forbidden) (25)<br><!-- End of picture text -->

The strict rule ∆ _S_ = 0 (intersystem crossing prohibition) means transitions between states of different multiplicities (e.g., singlet-triplet) are highly forbidden. 

-  **Selection Rules in j-j Coupling:** 



<!-- Start of picture text -->
∆ ji = 0 , ± 1 (for the transitioning electron) , ∆ J = 0 , ± 1 (26)<br><!-- End of picture text -->

Here, total spin _S_ and total orbital momentum _L_ are no longer good quantum numbers, so rules on ∆ _S_ and ∆ _L_ do not apply. 

8 

GATE PHYSICS 

ATOMIC SPECTRA & COUPLING SCHEMES 

### **4. Derivation Milestones** 

The mathematical formulation of both schemes is derived through these vector addition stages: 

1. **Formulating the Non-Relativistic Perturbation:** Write the unperturbed many-electron Hamiltonian as: 

   - _H_ ˆ = _H_ ˆ0 + _H_ ˆelec + _H_ ˆso (27) 

where _H_<sup>ˆ</sup> 0 is the independent particle Coulomb core, _H_<sup>ˆ</sup> elec =<sup>�</sup> _i<j_ 4 _πϵe_ 0<sup>2</sup> _rij_<sup>istheelectrostatic</sup> repulsion, and _H_<sup>ˆ</sup> so =<sup>�</sup> _i_<sup>_ξ_(</sup><sup>_ri_)</sup><sup>**l**</sup><sup>_i ·_</sup><sup>**s**</sup><sup>_i_isthespin-orbitterm.</sup> 

2. **L-S Limit Approximation:** For _Z ≪_ 30, _H_<sup>ˆ</sup> elec _≫ H_<sup>ˆ</sup> so. We diagonalize _H_<sup>ˆ</sup> elec first using the basis _|L, S, ML, mS⟩_ . This breaks the degeneracy, grouping states into electrostatic term multiplets. Finally, we treat _H_<sup>ˆ</sup> so _∝_ **L** _·_ **S** as a perturbation to split the terms into fine-structure levels _J_ . 

3. **j-j Limit Approximation:** For _Z ≫_ 30, _H_<sup>ˆ</sup> so _≫ H_<sup>ˆ</sup> elec. We diagonalize _H_<sup>ˆ</sup> so first for each electron using the basis _|ji, mji⟩_ . This splits levels into single-particle fine structure. Finally, we treat _H_<sup>ˆ</sup> elec as a weak perturbation to couple the **j** _i_ values into the final total _J_ states. 

### **5. Problem-Solving Algorithm** 

#### **Determining Term Symbols and Fine-Structure States** 

1. **Identify Electronic Configurations:** Note if the electrons are equivalent (same shell, e.g., _np_<sup>2</sup> ) or non-equivalent (different shells, e.g., _np_ 1 _d_ ). 

2. **Calculate Non-Equivalent Terms (L-S Scheme):** 

   -  Find total _L_ = _|l_ 1 _− l_ 2 _|, . . . , l_ 1 + _l_ 2. 

   -  Find total _S_ = _|s_ 1 _− s_ 2 _|, . . . , s_ 1 + _s_ 2. 

   -  Form all possible combinations of _L_ and _S_ . For each pair, write down the terms and calculate the possible _J_ values. 

3. **Apply Hund’s Rules to Find the Ground State (for Equivalent Configurations):** 

   -  **Rule 1:** The term with the maximum multiplicity (maximum _S_ ) lies lowest in energy. 

   -  **Rule 2:** For a given multiplicity, the state with the largest _L_ lies lowest. 

   -  **Rule 3:** If the outermost shell is less than half-filled, the state with the minimum _J_ is lowest. If the shell is more than half-filled, the state with the maximum _J_ lies lowest. 

9 

GATE PHYSICS 

ATOMIC SPECTRA & COUPLING SCHEMES 

### **6. Crucial Pitfalls** 

#### **Coupling Scheme Pitfalls** 

-  **Equivalent vs. Non-Equivalent Confusion:** Applying simple vector addition to equivalent electrons ( _np_<sup>2</sup> ) without enforcing the Pauli exclusion principle. For non-equivalent 2 _p_ 3 _p_ , vector addition yields singlet/triplet _S, P, D_ terms: 1 _S,_ 1 _P,_ 1 _D,_ 3 _S,_ 3 _P,_ 3 _D_ . However, for equivalent 2 _p_ 2 configurations, the Pauli principle excludes<sup>3</sup> _D_ ,<sup>3</sup> _S_ , and<sup>1</sup> _P_ , leaving only<sup>1</sup> _S,_<sup>3</sup> _P,_<sup>1</sup> _D_ . 

-  **Mixing up Hund’s Rule 3:** Applying the shell-filling rule to non-equivalent configurations. Hund’s rules for ground states are defined strictly for equivalent configurations. 

### **7. Standard Textbook Systems** 

-  **Carbon Atom Ground State (** 1 _s_<sup>2</sup> 2 _s_<sup>2</sup> 2 _p_<sup>2</sup> **):** Features equivalent electrons. The Pauli principle restricts terms to<sup>1</sup> _D,_<sup>3</sup> _P,_<sup>1</sup> _S_ . Applying Hund’s rules, the maximum spin multiplicity is the triplet state ( _S_ = 1), making<sup>3</sup> _P_ the lowest term. The 2 _p_ shell is less than half-filled (2 _/_ 6), so the lowest _J_ level is lowest: the ground state is exactly<sup>3</sup> _P_ 0. 

10 

GATE PHYSICS 

ATOMIC SPECTRA & COUPLING SCHEMES 

## **4 Fine and Hyperfine Structures** 

### **1. Core Theory** 

Spectral lines are split into nested tiers of multiplet structures under different relativistic and nuclear interactions: 

-  **Fine Structure:** The splitting of unperturbed atomic energy levels of a given principal quantum number _n_ due to relativistic corrections. Physically, it is caused by three distinct relativistic phenomena: the relativistic correction to the electron’s kinetic energy, the spinorbit interaction, and the Darwin term (a relativistic correction to the electrostatic potential experienced by s-electrons due to zitterbewegung). 

-  **Hyperfine Structure:** A much smaller splitting of the fine-structure levels (typically 10<sup>3</sup> to 10<sup>6</sup> times smaller than fine structure). Physically, it is caused by the electromagnetic coupling between the total angular momentum **J** of the atomic electrons and the nuclear spin angular momentum **I** . This coupling has two primary components: the magnetic dipole interaction (nuclear magnetic dipole interacting with the magnetic field generated by the electrons) and the electric quadrupole interaction (nuclear electric quadrupole moment interacting with the electric field gradient of the electron cloud). 

### **2. Energy Level Framework** 

The energy eigenvalues and shifts are governed by: 

-  **Fine-Structure Relativistic Shift (Dirac Equation for Hydrogenic Atoms):** 



<!-- Start of picture text -->
E fine =  En (0) 1 + α 2 Z 2 1 (28)<br>� n � j  + 1 / 2 − 4 3 n ��<br><!-- End of picture text -->

where _En_<sup>(0)</sup> is the non-relativistic hydrogenic energy, and _α_ = 4 _πϵe_<sup>2</sup> 0ℏ _c_<sup>_≈_</sup> 1371 _._ 036<sup>isthe</sup><sup>**fine-**</sup> **structure constant** . Note that the unperturbed _l_ -degeneracy is only partially broken: states with different _l_ but the same _j_ (e.g., 2 _s_ 1 _/_ 2 and 2 _p_ 1 _/_ 2) remain degenerate under Dirac finestructure formulation. 

-  **Hyperfine Structure Energy Shift:** The interaction Hamiltonian is modeled as _H_<sup>ˆ</sup> hfs = _A_ **I** _·_ **J** . The first-order shift is: 



<!-- Start of picture text -->
∆ E hfs = A 2 [ F ( F + 1)  − I ( I + 1)  − J ( J + 1)] (29)<br><!-- End of picture text -->

where _A_ is the magnetic dipole hyperfine coupling constant, and **F** = **I** + **J** is the **total angular momentum of the atom** (electrons + nucleus). The quantum numbers are: 

- _I_ : Nuclear spin angular momentum quantum number. 

- _J_ : Electronic total angular momentum quantum number. 

- _F ∈{|I − J|, . . . , I_ + _J}_ : Total atomic angular momentum quantum number. 

11 

GATE PHYSICS 

ATOMIC SPECTRA & COUPLING SCHEMES 

### **3. Selection Rules & Transitions** 

The transitions are governed by: 

-  **Fine Structure Transitions (E1):** 



<!-- Start of picture text -->
∆ j = 0 , ± 1 , ∆ l  =  ± 1 (30)<br><!-- End of picture text -->

 **Hyperfine Structure Transitions (magnetic dipole M1 or E1):** 



<!-- Start of picture text -->
∆ F = 0 , ± 1 (but F = 0  → F = 0 is forbidden) (31)<br><!-- End of picture text -->

### **4. Derivation Milestones** 

The fine and hyperfine splittings are derived through these stages: 

1. **Fine-Structure Relativistic Expansions:** Expand the relativistic Hamiltonian: 

_H_ ˆrelativistic = _H_ ˆkinetic + _H_ ˆso + _H_ ˆDarwin (32) where the kinetic correction is _H_<sup>ˆ</sup> kinetic = _−_ 8 _mp_ ˆ<sup>3</sup> _e_<sup>4</sup> _c_<sup>2, and the Darwin term is</sup><sup>_H_ˆDarwin=</sup><sup>_<u>π</u>_</sup> 2<sup><u>ℏ</u></sup> _m_<sup>2</sup><sup>_<u>Ze</u>_2</sup> _ec_<sup>22</sup><sup>_δ_3(</sup><sup>**r**).</sup> 

2. **First-Order Perturbative Solutions:** Apply unperturbed hydrogenic states to calculate the expectations of each relativistic perturbation term. Summing the three terms yields the Dirac energy correction. 

3. **Hyperfine Magnetic Dipole Coupling:** Model the magnetic field **B** elec generated by the orbiting electrons at the nucleus. The nuclear spin possesses a magnetic dipole moment **_µ_** _I_ = _gI_ 2 _Me p_<sup>**I**.Thisgivestheinteraction:</sup> 



<!-- Start of picture text -->
H ˆhfs =  − µ I ·  B elec =  A I  ·  J (33)<br><!-- End of picture text -->

4. **Diagonalizing I** _·_ **J:** Expressing **I** _·_ **J** =<sup><u>1</u></sup> 2<sup>(</sup><sup>**F**2</sup><sup>_−_</sup><sup>**I**2</sup><sup>_−_</sup><sup>**J**2),whichdiagonalizesthehyperfine</sup> Hamiltonian in the coupled _|I, J, F, MF ⟩_ representation. 

### **5. Problem-Solving Algorithm** 

#### **Calculating Hyperfine Splittings and Term Spacings** 

1. **Identify Nuclear Spin** _I_ **and Electronic State** _J_ **:** Locate the quantum numbers for the system. 

2. **Determine the Allowed** _F_ **Values:** Write down the complete range of total atomic states: _F_ = _|I − J|, . . . , I_ + _J_ . 

3. **Calculate Hyperfine Spacings:** To find the energy spacing between adjacent hyperfine levels _F_ and _F −_ 1: 

   - ∆ _E_ hfs( _F_ ) _−_ ∆ _E_ hfs( _F −_ 1) = _AF_ (34) 

The interval spacing between adjacent hyperfine levels is directly proportional to the larger _F_ value of the pair. 

4. **Solve for the Hyperfine Constant** _A_ **:** If the energy spacing between levels _F_ and _F −_ 1 is known experimentally, find the coupling constant: _A_ =<sup><u>∆</u></sup> _F_<sup>_<u>E</u>_.</sup> 

12 

GATE PHYSICS 

ATOMIC SPECTRA & COUPLING SCHEMES 

### **6. Crucial Pitfalls** 

#### **Fine and Hyperfine Pitfalls** 

-  **Assuming s-States Have No Hyperfine Splitting:** Falsely assuming _A_ = 0 for s- states because orbital magnetic fields vanish ( _l_ = 0). Although S-waves have no orbital magnetic contribution, they exhibit an extremely strong **Fermi contact interaction** due to the non-zero electron density at the nucleus ( _ψ_ (0) _̸_ = 0), yielding exceptionally large hyperfine splittings. 

-  **Confusing Fine-Structure Constant with Coupling Strengths:** Confusing the dimensionless fine-structure constant _α ≈_ 1 _/_ 137 with the coupling constants _anl_ or _A_ . 

### **7. Standard Textbook Systems** 

-  **The 21-cm Hydrogen Hyperfine Transition:** The ground state of Hydrogen (1 _s_ 1 _/_ 2, _J_ = 1 _/_ 2) coupled with the proton nuclear spin ( _I_ = 1 _/_ 2) yields two hyperfine levels: _F_ = 1 (parallel spins, triplet state) and _F_ = 0 (antiparallel spins, singlet state). The radiative transition _F_ = 1 _→ F_ = 0 releases a photon of frequency _ν ≈_ 1420 MHz, corresponding to a wavelength of exactly 21 cm. This is the most crucial spectral marker in observational radio astronomy. 

13 

GATE PHYSICS 

ATOMIC SPECTRA & COUPLING SCHEMES 

## **References** 

1. Rajkumar. _Atomic and Molecular Spectra: Laser_ . Kedar Nath Ram Nath, 2015. 

2. Banwell, Colin N. _Fundamentals of Molecular Spectroscopy_ . McGraw-Hill, 1994. 

3. Beiser, Arthur. _Concepts of Modern Physics_ . McGraw-Hill, 2003. 

14 

GATE PHYSICS 

ZEEMAN, PASCHEN-BACK, & STARK EFFECTS 

# **GATE PHYSICS STUDY NOTES Zeeman, Paschen-Back, Stark Effects, and Selection Rules** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**<br>**The Zeeman Effects (Normal and Anomalous)**|**2**|
|---|---|
|**2**<br>**The Paschen-Back Effect**|**5**|
|**3**<br>**The Stark Effect (Linear and Quadratic)**|**8**|
|**4**<br>**Quantum Mechanics of Electric Dipole Transitions and Selection Rules**|**11**|



1 

GATE PHYSICS 

ZEEMAN, PASCHEN-BACK, & STARK EFFECTS 

## **1 The Zeeman Effects (Normal and Anomalous)** 

### **1. Core Theory** 

The **Zeeman effect** refers to the splitting of atomic spectral lines when the atom is placed in a weak, static, external magnetic field **B** . 

-  **Normal Zeeman Effect (NZE):** This occurs in systems with zero total net spin ( _S_ = 0), such as singlet states of alkaline earth metals. Physically, it is a purely orbital phenomenon where the orbital magnetic dipole moment **_µ_** _l_ precesses around the external magnetic field. Since spin is absent, the orbital states split into 2 _l_ +1 equally spaced levels, yielding a symmetric three-line emission pattern (known as the Lorentz triplet) when observed perpendicular to the field. 

-  **Anomalous Zeeman Effect (AZE):** This occurs in systems with non-zero total spin ( _S̸_ = 0), such as alkali or hydrogen-like atoms. Physically, the spin **S** and orbital **L** angular momenta couple to form a total angular momentum **J** = **L** + **S** , which precesses around the magnetic field. Because the gyromagnetic ratios for spin and orbit differ ( _gs ≈_ 2 vs. _gl_ = 1), the magnetic moment **_µ_** _J_ is not collinear with **J** , resulting in unequal energy level splittings and complex multi-line patterns that cannot be explained classically. 

### **2. Energy Level Framework** 

The Hamiltonian in the presence of a weak external magnetic field _Bz_ along the _z_ -axis is: 



<!-- Start of picture text -->
H ˆ = H ˆ0 + H ˆmag , H ˆmag =  − µ  ·  B  = µ ℏ B (ˆ Lz  + 2 ˆ Sz ) (1)<br><!-- End of picture text -->

Applying first-order perturbation theory in the coupled _|j, mj⟩_ basis (Russell-Saunders scheme) yields the energy shift ∆ _EZ_ : 



<!-- Start of picture text -->
∆ EZ =  ⟨j, mj|H ˆ mag |j, mj⟩ =  gJ µBBzmj (2)<br><!-- End of picture text -->

where: 



<!-- Start of picture text -->
e ℏ<br> µB = 2 me ≈ 5 . 788  ×  10 − 5 eV/T is the Bohr magneton.<br><!-- End of picture text -->

 _mj ∈{−j, −j_ + 1 _, . . . , j}_ is the magnetic quantum number for total angular momentum. 

 _gJ_ is the dimensionless **Land´e g-factor** : 



<!-- Start of picture text -->
gJ = 1 + j ( j  + 1) +  s ( s  + 1)  − l ( l  + 1) (3)<br>2 j ( j  + 1)<br><!-- End of picture text -->

In the **Normal Zeeman Effect** ( _S_ = 0 = _⇒ j_ = _l_ , _gJ_ = 1), the energy shift is: 



<!-- Start of picture text -->
∆ E Normal =  µBBzml ( ml ∈{−l, . . . , l} ) (4)<br><!-- End of picture text -->

This yields equally spaced levels separated by exactly ∆ _E_ = _µBBz_ , which is independent of the orbital state _l_ . 

2 

GATE PHYSICS 

ZEEMAN, PASCHEN-BACK, & STARK EFFECTS 

### **3. Selection Rules & Transitions** 

For electric dipole (E1) transitions between split Zeeman levels, the selection rules are: 

∆ _l_ = _±_ 1 _,_ ∆ _j_ = 0 _, ±_ 1 (excluding _j_ = 0 _→ j_ = 0) _,_ ∆ _mj_ = 0 _, ±_ 1 (5) 

The polarization of the emitted light depends on ∆ _mj_ : 

-  _π_ **-components (** ∆ _mj_ = 0 **):** Linearly polarized parallel to the magnetic field **B** . When observed along the field axis (longitudinal view), these components vanish. 

-  _σ_ **-components (** ∆ _mj_ = _±_ 1 **):** Circularly polarized when viewed along the field axis (longitudinal view, LCP/RCP) and linearly polarized perpendicular to the field when viewed perpendicular to it (transverse view). 

### **4. Derivation Milestones** 

The quantum mechanical derivation of the Zeeman shift relies on these structural milestones: 

1. **Magnetic Interaction Hamiltonian:** Defining the interaction Hamiltonian _H_<sup>ˆ</sup> mag =<sup>_<u>µ</u>_</sup> ℏ<sup>_<u>B</u>_(ˆ</sup><sup>**L**+</sup> 2 **S**<sup>ˆ</sup> ) _·_ **B** using the gyromagnetic factors _gl_ = 1 and _gs_ = 2. 

2. **Vector Model Projection:** Projecting the total magnetic moment vector **_µ_** = **_µ_** _l_ + **_µ_** _s_ along the total angular momentum vector **J** because the rapid precession of **L** and **S** about **J** averages the perpendicular components of **_µ_** to zero over time. Mathematically, this corresponds to: 

   - _⟨L_<sup>ˆ</sup> _z_ + 2 _S_<sup>ˆ</sup> _z⟩_ =<sup>_<u>⟨</u>_</sup><sup><u>(</u></sup><sup>**L**ˆ + 2ˆ</sup><sup>**S**</sup><sup><u>)</u></sup><sup>_·_ˆ</sup><sup>**J**</sup><sup>_<u>⟩</u>_</sup> _Jz_ =<sup>_<u>⟨</u>_</sup><sup>**J**ˆ2 + ˆ</sup><sup>**S**2</sup><sup>_−_</sup><sup>**L**ˆ2</sup><sup>_<u>⟩</u>_</sup> _Jz_ + _Jz_ (6) **J**<sup>2</sup> 2 **J**<sup>2</sup> 

3. **Isolating the Land´e g-Factor:** Substituting the eigenvalue relations **J**<sup>2</sup> _→ j_ ( _j_ + 1)ℏ<sup>2</sup> , **L**<sup>2</sup> _→ l_ ( _l_ + 1)ℏ<sup>2</sup> , and **S**<sup>2</sup> _→ s_ ( _s_ + 1)ℏ<sup>2</sup> into the expectation value to extract the standard Land´e formula. 

### **5. Problem-Solving Algorithm** 

#### **Algorithm for Zeeman Effect Calculations** 

1. **Identify the Terms:** Convert spectroscopic terms (e.g.,<sup>2</sup> _D_ 3 _/_ 2) into quantum numbers ( _s_ = 1 _/_ 2 _, l_ = 2 _, j_ = 3 _/_ 2). 

2. **Calculate the Land´e g-Factors:** Compute _gJ_ for both the initial and final states of the transition. 

3. **Map the Splitting:** List all allowed _mj_ values for each state, and calculate the shifted energies _E_ = _E_ 0 + _gJ µBBzmj_ . 

4. **Find Allowed Transitions:** Apply the selection rule ∆ _mj_ = 0 _, ±_ 1 to find all allowed lines. 



<!-- Start of picture text -->
5. Compute Line Spacings: Express the transition wavenumbers ∆¯ ν or frequencies<br>∆ ν :<br>ν =  ν 0 + µB h Bz � gJ initial m initial j − gJ final m final j � (7)<br><!-- End of picture text -->

3 

GATE PHYSICS 

ZEEMAN, PASCHEN-BACK, & STARK EFFECTS 

### **6. Crucial Pitfalls** 

#### **Zeeman Effect Traps to Avoid** 

-  **Applying AZE Formulas to Singlets (** _S_ = 0 **):** If _S_ = 0, _gJ_ is identically 1. Attempting to compute complex fractional splits for _S_ = 0 states is a common error. All singlet-to-singlet transitions under magnetic fields yield a standard 3-line normal Zeeman triplet. 

-  **Ignoring the Weak Field Constraint:** Assuming these formulas apply in strong fields. This theory requires ∆ _E_ mag _≪_ ∆ _E_ so (fine structure). If the magnetic field is strong enough that magnetic energy exceeds spin-orbit coupling, the unperturbed coupled basis breaks down, and you must use the **Paschen-Back** formulation instead. 

-  **Sign and Scale Errors in Wavenumber Calculations:** Forgetting that the splitting of spectral lines ∆¯ _ν_ is often measured in cm<sup>_−_1</sup> , requiring division by _hc_ ( _E/hc_ ). 

### **7. Standard Textbook Systems** 

1. **Singlet-Singlet Normal Zeeman Triplet:** The transition<sup>1</sup> _D_ 2 _→_<sup>1</sup> _P_ 1 in Calcium ( _Z_ = 20). Because _S_ = 0 for both terms, the upper level splits into 5 equally spaced states and the lower into 3, yielding exactly 9 allowed transitions that collapse into a clean 3-line Lorentz triplet. 

2. **Sodium D-Line Splitting:** The transitions 3<sup>2</sup> _P_ 3 _/_ 2 _→_ 3<sup>2</sup> _S_ 1 _/_ 2 ( _D_ 2 line) and 3<sup>2</sup> _P_ 1 _/_ 2 _→_ 3<sup>2</sup> _S_ 1 _/_ 2 ( _D_ 1 line) in Sodium ( _Z_ = 11). The _D_ 1 line splits into a 6-line anomalous pattern because _g_ ( _P_ 1 _/_ 2) = 2 _/_ 3 and _g_ ( _S_ 1 _/_ 2) = 2, while the _D_ 2 line splits into a 10-line anomalous pattern because _g_ ( _P_ 3 _/_ 2) = 4 _/_ 3. 

4 

GATE PHYSICS 

ZEEMAN, PASCHEN-BACK, & STARK EFFECTS 

## **2 The Paschen-Back Effect** 

### **1. Core Theory** 

The **Paschen-Back effect** refers to the splitting of atomic spectral lines in the presence of a **strong** external magnetic field. Physically, it marks the transition from the coupled coupled-basis regime ( _l − s_ coupling) to the uncoupled regime. 

When the external magnetic field is strong enough, the torque exerted by the field on **L** and **S** individually exceeds the mutual internal spin-orbit coupling torque. Consequently, the coupling between **L** and **S** is broken, and they decouple, precessing **independently** around the external magnetic field axis. This simplifies the splitting pattern at extremely high fields, causing the complex anomalous Zeeman pattern to collapse back into a symmetric triplet resembling the normal Zeeman effect but with fine-structure offsets. 

### **2. Energy Level Framework** 

Under strong-field conditions (∆ _E_ mag _≫_ ∆ _E_ so), the unperturbed basis is the uncoupled basis _|l, s, ml, ms⟩_ . The total perturbation Hamiltonian is: 



<!-- Start of picture text -->
H ˆpert = H ˆmag + H ˆso (8)<br><!-- End of picture text -->

The unperturbed energy states split according to the diagonal expectation values of this perturbation: 



<!-- Start of picture text -->
∆ E PB =  ⟨l, s, ml, ms|H ˆ mag + H ˆ so |l, s, ml, ms⟩ (9)<br><!-- End of picture text -->

This yields the fundamental Paschen-Back energy equation: 



<!-- Start of picture text -->
∆ E PB =  µBBz ( ml  + 2 ms ) +  anlmlms (10)<br><!-- End of picture text -->

where: 

-  _ml ∈{−l, . . . , l}_ is the orbital magnetic quantum number. 

-  _ms ∈{−s, . . . , s}_ = _{−_ 1 _/_ 2 _,_ 1 _/_ 2 _}_ (for a single electron) is the spin magnetic quantum number. 

-  _anl_ is the unperturbed spin-orbit coupling constant. 

-  The term _µBBz_ ( _ml_ + 2 _ms_ ) represents the dominant strong magnetic splitting. 

-  The term _anlmlms_ represents the small, first-order diagonal spin-orbit correction. 

### **3. Selection Rules & Transitions** 

In the uncoupled strong-field representation, the electromagnetic wave interacts directly with the orbital state of the electron, while the spin is decoupled. The selection rules are: 



<!-- Start of picture text -->
∆ l  =  ± 1 , ∆ ms = 0 , ∆ ml = 0 , ± 1 (11)<br><!-- End of picture text -->

Because the spin does not flip during the E1 transition (∆ _ms_ = 0), the transitions split into three main groups of lines corresponding to ∆ _ml_ = 0 _, ±_ 1 (similar to the Normal Zeeman triplet), with each group containing sub-components split by the spin-orbit correction. 

5 

GATE PHYSICS 

ZEEMAN, PASCHEN-BACK, & STARK EFFECTS 

### **4. Derivation Milestones** 

The derivation of the Paschen-Back energy levels involves these critical milestones: 

1. **Selecting the Basis:** Recognizing that because _H_<sup>ˆ</sup> mag =<sup>_<u>µ</u>_</sup> ℏ<sup>_<u>B</u>_(ˆ</sup><sup>_Lz_+ 2 ˆ</sup><sup>_Sz_)</sup><sup>_Bz_commuteswith</sup> both _L_<sup>ˆ</sup> _z_ and _S_<sup>ˆ</sup> _z_ ([ _H_<sup>ˆ</sup> mag _, L_<sup>ˆ</sup> _z_ ] = [ _H_<sup>ˆ</sup> mag _, S_<sup>ˆ</sup> _z_ ] = 0), the uncoupled basis _|l, s, ml, ms⟩_ diagonalizes the dominant magnetic interaction. 

2. **Diagonalizing the Magnetic Term:** Evaluating the magnetic energy shift: 



<!-- Start of picture text -->
⟨l, s, ml, ms| µ ℏ B (ˆ Lz  + 2 ˆ Sz ) Bz|l, s, ml, ms⟩ =  µBBz ( ml  + 2 ms ) (12)<br><!-- End of picture text -->

3. **First-Order Spin-Orbit Expectation Value:** Treating the spin-orbit Hamiltonian _H_<sup>ˆ</sup> so = _<u>a</u>_ ℏ _<u>nl</u>_<sup>2</sup><sup>**L**ˆ</sup><sup>_·_ˆ</sup><sup>**S**asasmallperturbationonthemagneticlevels.Expandingthedotproduct:</sup> 



<!-- Start of picture text -->
L ˆ  ·  ˆ S  = L ˆ x  ˆ Sx  + L ˆ y  ˆ Sy  + L ˆ z  ˆ Sz = 1 (13)<br>2 (ˆ L + ˆ S− + L ˆ −S ˆ+) + L ˆ z  ˆ Sz<br><!-- End of picture text -->

Because the uncoupled basis elements are eigenstates of _L_<sup>ˆ</sup> _z_ and _S_<sup>ˆ</sup> _z_ , and the ladder operators change _ml_ and _ms_ (shifting states outside the diagonal), the off-diagonal terms average to zero in first-order perturbation, leaving: 



<!-- Start of picture text -->
⟨l, s, ml, ms| L ˆ  · S ˆ |l, s, ml, ms⟩ = ℏ 2 mlms (14)<br><!-- End of picture text -->

### **5. Problem-Solving Algorithm** 

#### **Algorithm for Paschen-Back Splitting** 

1. **Identify States:** Determine _l_ and _s_ for both the initial and final states. 

2. **List Uncoupled Configurations:** Write down all allowed ( _ml, ms_ ) combinations for each state. 

3. **Compute Energy Levels:** Calculate the energy for each combination using: _E_ ( _ml, ms_ ) = _E_ 0 + _µBBz_ ( _ml_ + 2 _ms_ ) + _anlmlms_ (15) 

4. **Apply Transition Rules:** Draw transition lines matching ∆ _ml_ = 0 _, ±_ 1 and ∆ _ms_ = 0. 

5. **Determine Line Frequencies:** Group transitions by ∆ _ml_ to analyze the finestructure splitting of the triplet. 

6 

GATE PHYSICS 

ZEEMAN, PASCHEN-BACK, & STARK EFFECTS 

### **6. Crucial Pitfalls** 

#### **Paschen-Back Traps to Avoid** 

-  **Using** _j_ **and** _mj_ **:** In a strong field, **J** is no longer conserved because the individual vectors **L** and **S** couple independently to the external field. Using coupled formulas or coupled quantum numbers ( _j_ ) is a conceptual error. 

-  **Neglecting the Spin-Orbit Correction:** Forgetting the _anlmlms_ term. While the magnetic term dominates, the spin-orbit correction is what splits the degenerate triplet components, and omitting it leads to incorrect transition frequencies. 

-  **Confusing the Magnetic Coupling Coefficient:** Assuming the spin term has a _g_ - factor of 1. Remember that the magnetic moment has a factor of 2 for spin: ( _ml_ +2 _ms_ ), not ( _ml_ + _ms_ ). 

### **7. Standard Textbook Systems** 

1. **Paschen-Back Effect in Hydrogen** 3 _d →_ 2 _p_ **(H-** _α_ **line):** In a strong field, the 3 _d_ ( _l_ = 2 _, s_ = 1 _/_ 2) and 2 _p_ ( _l_ = 1 _, s_ = 1 _/_ 2) levels split into uncoupled states. The transitions with ∆ _ms_ = 0 group into three sets of lines, illustrating the transition from a complex anomalous pattern to a highly structured triplet. 

2. **Lithium Doublet in a Strong Field:** The 2<sup>2</sup> _P_ 3 _/_ 2 _,_ 1 _/_ 2 _→_ 2<sup>2</sup> _S_ 1 _/_ 2 doublet of Lithium ( _Z_ = 3). Because Lithium is light, its spin-orbit coupling is weak ( _∼_ 0 _._ 34 cm<sup>_−_1</sup> ), allowing relatively modest laboratory magnetic fields ( _∼_ 1 Tesla) to fully decouple the states and demonstrate the Paschen-Back effect. 

7 

GATE PHYSICS 

ZEEMAN, PASCHEN-BACK, & STARK EFFECTS 

## **3 The Stark Effect (Linear and Quadratic)** 

### **1. Core Theory** 

The **Stark effect** is the splitting and shifting of atomic energy levels and spectral lines in the presence of a static, external **electric field E** ext. Physically, it arises from the interaction between the atom’s electric dipole moment **d** and the external electric field. 

-  **Linear Stark Effect:** The energy shift is directly proportional to the electric field strength ( _|_ **E** ext _|_ ). This occurs only in systems with permanent electric dipole moments. In atoms, this is restricted to states with **accidental degeneracy** of opposite parities, such as the excited states of Hydrogen ( _n ≥_ 2), where states of different _l_ (and thus different parities) share the same energy. 

-  **Quadratic Stark Effect:** The energy shift is proportional to the square of the electric field ( _|_ **E** ext _|_<sup>2</sup> ). This occurs in all atoms in non-degenerate ground states (e.g., ground-state Hydrogen _n_ = 1, Helium). Because the ground state has a definite parity, its permanent electric dipole moment is zero. The external electric field must first polarize the atom, inducing a dipole moment **d** ind = _α_ **E** ext, which then interacts with the field to produce a second-order energy shift. 

### **2. Energy Level Framework** 

The perturbation Hamiltonian for an electric field _E_ along the _z_ -axis is: 



<!-- Start of picture text -->
H ˆStark =  − d  ·  E ext =  eEz =  eEr  cos  θ (16)<br><!-- End of picture text -->

-  **Linear Stark Shift (for degenerate** _n_ = 2 **Hydrogen, neglecting spin):** First-order degenerate perturbation theory splits the _n_ = 2 level into three values: 



<!-- Start of picture text -->
∆ E linear = 0 , ± 3 ea 0 E (17)<br><!-- End of picture text -->

where _a_ 0 _≈_ 0 _._ 529<sup>˚</sup> A is the Bohr radius. 

-  **Quadratic Stark Shift (for non-degenerate ground states):** Second-order perturbation theory yields the energy shift: 



<!-- Start of picture text -->
∆ E quadratic =  e 2 E 2 � |⟨k (0) |z|n (0) ⟩| 2 =  − 2 1 α pol E 2 (18)<br>k̸ = n En (0) − Ek (0)<br><!-- End of picture text -->

where _α_ pol is the **electric polarizability** of the atom. 

### **3. Selection Rules & Transitions** 

Under an external electric field along the _z_ -axis, the azimuthal symmetry is preserved (spherical symmetry is broken to cylindrical symmetry), conserving _mj_ or _ml_ . The selection rules are: 



<!-- Start of picture text -->
∆ mj = 0 ( π -components) , ∆ mj =  ± 1 ( σ -components) (19)<br><!-- End of picture text -->

Parity conservation is broken by the external field, allowing transitions between states that would otherwise be forbidden in a symmetric central potential. 

8 

GATE PHYSICS 

ZEEMAN, PASCHEN-BACK, & STARK EFFECTS 

### **4. Derivation Milestones** 

The derivation of the Stark shifts involves these critical mathematical steps: 

1. **Parity Argument for Permanent Dipole Moment:** Proving that the expectation value of the dipole operator _⟨_ **d**<sup>ˆ</sup> _⟩_ vanishes for any state of definite parity. Since unperturbed nondegenerate states _|n_<sup>(0)</sup> _⟩_ have definite parity under spatial inversion ( **r** _→−_ **r** ), their diagonal matrix elements vanish: 



<!-- Start of picture text -->
⟨n (0) |ez|n (0) ⟩ =  e |ψn ( r ) | 2 zd 3 r = 0 (20)<br>�<br><!-- End of picture text -->

This proves that the first-order Stark shift is identically zero for all non-degenerate states. 

2. **Degenerate Subspace Formulation (** _n_ = 2 **Hydrogen):** For the _n_ = 2 level of Hydrogen, there are four degenerate states (excluding spin): _|_ 2 _,_ 0 _,_ 0 _⟩_ (2 _s_ ), _|_ 2 _,_ 1 _,_ 0 _⟩_ (2 _pz_ ), _|_ 2 _,_ 1 _,_ 1 _⟩_ (2 _px_ + _ipy_ ), and _|_ 2 _,_ 1 _, −_ 1 _⟩_ . The perturbation _H_<sup>ˆ</sup> Stark = _eEz_ is odd under parity, so only off-diagonal matrix elements between states of different parities (specifically 2 _s_ and 2 _pz_ , which share the same _m_ = 0) can be non-zero: 



<!-- Start of picture text -->
⟨ 2 ,  0 ,  0 |eEz| 2 ,  1 ,  0 ⟩ =  − 3 ea 0 E (21)<br><!-- End of picture text -->

3. **Solving the Secular Matrix:** Solving the 4 _×_ 4 secular equation inside the _n_ = 2 subspace: 



<!-- Start of picture text -->
−E (1) − 3 ea 0 E 0 0<br>− 3 ea 0 E −E (1) 0 0<br>= 0 (22)<br>0 0 −E (1) 0<br>�������� 0 0 0 −E (1) ��������<br><!-- End of picture text -->

This yields the roots _E_<sup>(1)</sup> = 0 (doublet) and _E_<sup>(1)</sup> = _±_ 3 _ea_ 0 _E_ . 

### **5. Problem-Solving Algorithm** 

#### **Algorithm for Stark Effect Problems** 

1. **Check for Degeneracy:** Determine if the state of interest is degenerate. 

   -  If it is the ground state or a non-degenerate level, the first-order shift is 0, and you must calculate the quadratic shift ∆ _E ∝E_<sup>2</sup> . 

   -  If it is an excited state of Hydrogen ( _n ≥_ 2), set up the linear Stark effect. 

2. **Identify Non-Zero Matrix Elements:** Apply parity and angular momentum selection rules to find non-zero integrals: _⟨l_ 1 _, m_ 1 _|z|l_ 2 _, m_ 2 _⟩_ is non-zero only if ∆ _l_ = _±_ 1 and ∆ _m_ = 0. 

3. **Solve the Linear Shift:** For the _n_ = 2 level of Hydrogen, the split energies are: 



<!-- Start of picture text -->
E =  E (0) , E =  E (0) ±  3 ea 0 E (23)<br><!-- End of picture text -->

4. **Evaluate the Quadratic Shift:** Use second-order perturbation or polarizability relations: ∆ _E_ = _−_ 2<sup><u>1</u></sup><sup>_α_pol</sup><sup>_E_2.</sup> 

9 

GATE PHYSICS 

ZEEMAN, PASCHEN-BACK, & STARK EFFECTS 

### **6. Crucial Pitfalls** 

#### **Stark Effect Traps to Avoid** 

-  **Assuming Ground State Hydrogen has a Linear Stark Shift:** Hydrogenic excited states have a linear Stark shift due to _l_ -degeneracy, but the _n_ = 1 ground state is non-degenerate (1 _s_ ). Thus, ground-state Hydrogen exhibits **only** a quadratic Stark shift. 

-  **Neglecting Spin-Orbit Coupling in Weak Fields:** In real Hydrogen, spin-orbit coupling lifts the _l_ -degeneracy (2 _s_ 1 _/_ 2 and 2 _p_ 1 _/_ 2 are slightly split, and 2 _p_ 3 _/_ 2 is further split). For the linear Stark effect formulas to be valid, the electric field must be strong enough that the Stark energy dominates over the fine-structure splitting: _eEa_ 0 _≫_ ∆ _E_ so. If the field is weak, the Stark effect is quadratic even for Hydrogen excited states. 

-  **Sign of Quadratic Shift:** The quadratic Stark shift of the ground state is always **negative** because the denominator _E_ 0<sup>(0)</sup> _− Ek_<sup>(0)</sup> in the second-order perturbation sum is strictly negative. 

### **7. Standard Textbook Systems** 

1. **Linear Stark Effect in** _n_ = 2 **Hydrogen:** The splitting of the _n_ = 2 level into three components under a strong electric field, which physically mixes the 2 _s_ and 2 _pz_ states to produce asymmetric, polarized electron distributions. 

2. **Quadratic Stark Effect in Ground-State Hydrogen (** 1 _s_ **):** Polarizing ground-state Hydrogen with an external field, where second-order perturbation yields a negative energy shift ∆ _E_ = _−_<sup><u>9</u></sup> 4<sup>_a_</sup> 0<sup>3</sup><sup>_E_2,correspondingtoanelectricpolarizabilityof</sup><sup>_α_pol=</sup><sup><u>9</u></sup> 2<sup>_a_</sup> 0<sup>3.</sup> 

10 

GATE PHYSICS 

ZEEMAN, PASCHEN-BACK, & STARK EFFECTS 

## **4 Quantum Mechanics of Electric Dipole Transitions and Selection Rules** 

### **1. Core Theory** 

In semi-classical radiation theory, the interaction between an atom and electromagnetic radiation is modeled by treating the atom quantum mechanically and the electromagnetic field classically. The dominant mechanism for the absorption and emission of photons is the **Electric Dipole (E1) transition** . 

Physically, the oscillating electric field of the light wave exerts an oscillating force on the atom’s electron cloud, driving spatial oscillations. If the transition matrix element of the electric dipole operator **d**<sup>ˆ</sup> = _−e_ **r** between the initial _|ψi⟩_ and final _|ψf ⟩_ states is non-zero, the transition is **allowed** to first order, occurring at a rate proportional to the square of the transition dipole moment. If the E1 matrix element vanishes, the transition is **forbidden** to first order, and must occur via much weaker, higher-order processes such as magnetic dipole (M1) or electric quadrupole (E2) radiation. 

### **2. Energy Level Framework & Matrix Elements** 

The transition rate _Ri→f_ for stimulated E1 transitions is governed by **Fermi’s Golden Rule** : 



<!-- Start of picture text -->
Ri→f = 2 π (24)<br>ℏ |⟨ψf |H  ˆ ′|ψi⟩| 2 ρ ( Ef )<br><!-- End of picture text -->

where: 

 _H_<sup>ˆ</sup><sup>_′_</sup> = _−_ **d**<sup>ˆ</sup> _·_ **E** 0 cos( _ωt_ ) is the time-dependent light-matter interaction Hamiltonian. 

-  **d** = _−e_<sup>�</sup> **r** _i_ is the total electric dipole operator. 

 **D** _fi_ = _⟨ψf |_ **r** _|ψi⟩_ is the **transition dipole moment matrix element** . 

 _ρ_ ( _Ef_ ) is the density of final states. 

The probability of spontaneous emission is governed by the Einstein _A_ -coefficient: 



<!-- Start of picture text -->
Aif = 4 ω 3 e 2 (25)<br>3ℏ c 3 |⟨ψf | r |ψi⟩| 2<br><!-- End of picture text -->

### **3. Selection Rules & Transitions** 

For single-electron atoms, the rigorous selection rules for Electric Dipole (E1) transitions are: 

1. **Parity Change (Laporte’s Rule):** The initial and final states must have different parities: 



<!-- Start of picture text -->
∆ π = yes = ⇒ ∆ l  =  ± 1 (26)<br><!-- End of picture text -->

Since the dipole operator **r** is odd under parity, the integral vanishes if the initial and final states have the same parity. 

2. **Orbital Angular Momentum Rule:** 



<!-- Start of picture text -->
∆ l  =  ± 1 , ∆ ml = 0 , ± 1 (27)<br><!-- End of picture text -->

11 

GATE PHYSICS 

ZEEMAN, PASCHEN-BACK, & STARK EFFECTS 

3. **Spin Conservation Rule:** The photon does not interact with the electron’s spin to first order: 



<!-- Start of picture text -->
∆ s  = 0 , ∆ ms = 0 (28)<br><!-- End of picture text -->

4. **Total Angular Momentum Rule (in the coupled representation):** 



<!-- Start of picture text -->
∆ j = 0 , ± 1 (excluding j = 0  → j = 0) , ∆ mj = 0 , ± 1 (29)<br><!-- End of picture text -->

### **4. Derivation Milestones** 

The derivation of the selection rules relies on these mathematical milestones: 

1. **Laporte’s Parity Proof:** Evaluating the spatial inversion ( **r** _→−_ **r** ) of the transition matrix element: 



<!-- Start of picture text -->
⟨ψf | r |ψi⟩ = ψf ∗ ( r ) r ψi ( r ) d 3 r (30)<br>�<br><!-- End of picture text -->

Under spatial inversion, the integral changes by a factor of ( _−_ 1)<sup>_lf_+1+</sup><sup>_li_</sup> . For the integral to be non-zero, this factor must be +1, requiring _lf_ + _li_ to be an odd integer, which means the parities must differ: ∆ _l_ = _±_ 1 _, ±_ 3 _, . . ._ . 

2. **Angular Integration via Spherical Harmonics:** Expressing the components of **r** ( _x, y, z_ ) in spherical coordinates using Spherical Harmonics _Y_ 1 _q_ ( _θ, ϕ_ ) ( _q_ = 0 _, ±_ 1). The angular integration is: 



<!-- Start of picture text -->
⟨ψf |rq|ψi⟩∝ dϕ Yl ∗ f mf ( θ, ϕ ) Y 1 q ( θ, ϕ ) Yl i m i ( θ, ϕ ) sin  θdθ (31)<br>�02 π �0 π<br><!-- End of picture text -->

3. **Applying the Wigner-Eckart Theorem:** Resolving the angular integral into ClebschGordan coefficients, which vanish unless: 



<!-- Start of picture text -->
|li − 1 | ≤ lf ≤ li  + 1 = ⇒ ∆ l  = 0 , ± 1 (32)<br><!-- End of picture text -->

Combining this with the parity requirement ∆ _l̸_ = 0 yields the selection rule ∆ _l_ = _±_ 1. 

### **5. Problem-Solving Algorithm** 

#### **Algorithm for Transition Allowedness** 

1. **Identify States:** Determine the quantum numbers ( _n, l, s, j, mj_ or _ml, ms_ ) of the initial and final states. 

2. **Check Parity/Laporte’s Rule:** Check if _l_ changes by exactly _±_ 1: ∆ _l_ = _±_ 1. If not (e.g., 2 _s →_ 1 _s_ , where ∆ _l_ = 0), the E1 transition is forbidden. 

3. **Check Spin Conservation:** Check if the total spin changes: ∆ _S_ = 0. If _S_ changes (e.g., singlet to triplet<sup>1</sup> _P_ 1 _→_<sup>3</sup> _S_ 1), the transition is spin-forbidden. 

4. **Check Total Angular Momentum:** Ensure ∆ _j_ = 0 _, ±_ 1 (excluding 0 _→_ 0). 

5. **Determine Component Polarizations:** Map allowed transitions to ∆ _m_ = 0 ( _π_ - polarization) or ∆ _m_ = _±_ 1 ( _σ_ -polarization). 

12 

GATE PHYSICS 

ZEEMAN, PASCHEN-BACK, & STARK EFFECTS 

### **6. Crucial Pitfalls** 

#### **Selection Rule Traps to Avoid** 

-  **Forgetting that** ∆ _l_ = 0 **is Forbidden for Single Electrons:** In many-electron atoms, transitions with ∆ _L_ = 0 (e.g.,<sup>2</sup> _P_ 3 _/_ 2 _→_<sup>2</sup> _P_ 1 _/_ 2) are allowed because other electrons can conserve parity, but for a single-electron atom, ∆ _l_ = 0 is strictly forbidden because it violates Laporte’s parity rule. 

-  **Confusing Allowedness with Absolute Impossibility:** Assuming ”forbidden” transitions never occur. A forbidden transition simply means its electric dipole rate is zero. It can still occur via much slower electric quadrupole (E2) or magnetic dipole (M1) processes (e.g., the 21-cm hydrogen line is a highly forbidden M1 transition that occurs spontaneously once in _∼_ 10<sup>7</sup> years). 

-  **Spin-Forbidden Leakage:** Assuming that ∆ _S_ = 0 is absolute. In heavy atoms, strong spin-orbit coupling mixes singlet and triplet states, breaking spin conservation and allowing ”forbidden” transitions (intersystem crossing, such as the 253 _._ 7 nm line in Mercury). 

### **7. Standard Textbook Systems** 

1. **The Lyman-Alpha Transition in Hydrogen:** The 2 _p →_ 1 _s_ transition. This is a highly allowed E1 transition because ∆ _l_ = 1 and the parity changes from odd (2 _p_ ) to even (1 _s_ ). 

2. **The Metastable** 2 _s_ **State of Hydrogen:** The 2 _s →_ 1 _s_ transition. This is strictly E1forbidden because ∆ _l_ = 0 (no parity change). The 2 _s_ state is highly metastable, decaying primarily via the slow emission of two simultaneous photons to conserve parity and angular momentum, with a long lifetime of _∼_ 0 _._ 12 seconds. 

13 

GATE PHYSICS 

ZEEMAN, PASCHEN-BACK, & STARK EFFECTS 

## **References** 

1. Rajkumar. _Atomic and Molecular Spectra: Laser_ . Kedar Nath Ram Nath, 2015. 

2. Beiser, Arthur. _Concepts of Modern Physics_ . McGraw-Hill, 2003. 

3. Griffiths, David J. _Introduction to Electrodynamics_ . Prentice Hall, 1999. 

4. Zettili, Nouredine. _Quantum Mechanics: Concepts and Applications_ . Wiley, 2009. 

14 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

# **GATE PHYSICS STUDY NOTES Diatomic Molecular Spectroscopy & Franck-Condon Principle** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**|**Rotational **|**Spectra of Diatomic Molecules (Rigid & Non-Rigid Rotors)**|**2**|
|---|---|---|---|
|**2**|**Vibrational**<br>**tors)**|**Spectra of Diatomic Molecules (Harmonic & Anharmonic **|**Oscilla-**<br>**7**|
|**3**|**Electronic **|**Transitions & The Franck-Condon Principle**|**12**|



1 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

## **1 Rotational Spectra of Diatomic Molecules (Rigid & Non-Rigid Rotors)** 

### **1. Core Theory** 

Pure rotational spectra arise from transitions between quantized rotational energy levels of a molecule. The physical origin of this phenomenon is the classical interaction of electromagnetic radiation with the molecule’s permanent electric dipole moment **_µ_** _e_ . 

When a polar molecule rotates, its permanent dipole moment rotates in space, creating an oscillating electric field that can couple with the transverse electric field of incident electromagnetic radiation (usually in the microwave region, 1 cm<sup>_−_1</sup> to 100 cm<sup>_−_1</sup> ). 

-  **The Rigid Rotor Model:** This model assumes that the chemical bond acts as a completely rigid, unstretchable link of length _r_ 0 connecting two point masses _m_ 1 and _m_ 2. The moment of inertia is constant regardless of how fast the molecule rotates. 

-  **The Non-Rigid Rotor Model:** In a real molecule, the chemical bond is elastic. As the rotation speed increases (higher rotational quantum states _J_ ), the centrifugal force stretches the bond, increasing the internuclear distance _r_ beyond its equilibrium value _re_ . This increase in _r_ raises the moment of inertia _I_ , which systematically lowers the rotational constant _B_ and compresses the spacing between higher energy levels. 

**Microwave Activity Condition:** A molecule must possess a non-zero permanent dipole moment ( **_µ_** _e̸_ = 0) to show pure rotational absorption or emission. Consequently, heteronuclear diatomic molecules (e.g., CO, HCl, NO) are _microwave-active_ , whereas homonuclear diatomic molecules (e.g., H2, O2, N2) are _microwave-inactive_ . 

### **2. Energy Level Framework** 

The quantum mechanical energy levels (expressed as Term Values _F_ ( _J_ ) in units of cm<sup>_−_1</sup> ) are governed by the following mathematical equations: 

#### **A. The Rigid Rotor** 



<!-- Start of picture text -->
F ( J ) =  BJ ( J + 1) (for J = 0 ,  1 ,  2 , . . .  ) (1)<br><!-- End of picture text -->

where: 

 _J_ is the rotational quantum number, taking non-negative integer values. 

-  _B_ is the **rotational constant** defined as: 



<!-- Start of picture text -->
ℏ h<br>B = [cm − 1 ] (2)<br>4 πIc = 8 π 2 Ic<br><!-- End of picture text -->

-  _I_ is the moment of inertia: _I_ = _µr_ 0<sup>2</sup> 

0<sup>.</sup> 

-  _µ_ is the **reduced mass** of the diatomic molecule: 



<!-- Start of picture text -->
m 1 m 2<br>µ  = (3)<br>m 1 +  m 2<br><!-- End of picture text -->

-  _r_ 0 is the constant internuclear distance (bond length). 

-  _c_ is the speed of light in vacuum (must be in cm/s if _B_ is in cm<sup>_−_1</sup> ). 

2 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

#### **B. The Non-Rigid Rotor** 



<!-- Start of picture text -->
F ( J ) =  BJ ( J + 1)  − DJ 2 ( J + 1) 2 (for J = 0 ,  1 ,  2 , . . .  ) (4)<br><!-- End of picture text -->

where: 

 _D_ is the **centrifugal distortion constant** (always a positive quantity): 



<!-- Start of picture text -->
D = 4 B 3 [cm − 1 ] (5)<br>ω ¯ e 2<br><!-- End of picture text -->

 _ω_ ¯ _e_ is the equilibrium vibrational wavenumber of the chemical bond (in cm<sup>_−_1</sup> ). 

### **3. Selection Rules & Transitions** 

For pure rotational transitions to occur: 

1. **Gross Selection Rule:** The molecule must have a permanent electric dipole moment ( **_µ_** _e̸_ = 0). 

2. **Specific Selection Rule:** The change in the rotational quantum number during absorption or emission is restricted to: 



<!-- Start of picture text -->
∆ J =  ± 1 (6)<br><!-- End of picture text -->

For an absorption transition from _J → J_ + 1, the transition wavenumber _ν_ ¯ is: 

#### **A. Rigid Rotor Transitions** 



<!-- Start of picture text -->
ν ¯ R ( J → J + 1) =  F ( J + 1)  − F ( J ) = 2 B ( J + 1) [cm − 1 ] (7)<br><!-- End of picture text -->

This yields a series of spectral lines at wavenumbers 2 _B,_ 4 _B,_ 6 _B,_ 8 _B, . . ._ with a constant adjacent line spacing of: 



<!-- Start of picture text -->
∆¯ ν = ν ¯( J + 1  → J + 2)  − ν ¯( J → J + 1) = 2 B (8)<br><!-- End of picture text -->

#### **B. Non-Rigid Rotor Transitions** 



<!-- Start of picture text -->
ν ¯ NR ( J → J + 1) =  F ( J + 1)  − F ( J ) = 2 B ( J + 1)  − 4 D ( J + 1) 3 [cm − 1 ] (9)<br><!-- End of picture text -->

This yields adjacent line spacings that contract as _J_ increases: 



<!-- Start of picture text -->
∆¯ ν = 2 B − 12 D ( J + 1) 2 (10)<br><!-- End of picture text -->

### **4. Derivation Milestones** 

The derivation of these rotational equations is marked by these physical milestones: 

1. **Schr¨odinger Formulation:** Writing the Time-Independent Schr¨odinger Equation (TISE) in spherical coordinates for two masses _m_ 1 _, m_ 2 at a fixed distance _r_ 0 with zero potential energy _V_ = 0: 



<!-- Start of picture text -->
− ℏ2 1 ∂ sin  θ ∂ + 1 ∂ 2 ψ =  Eψ (11)<br>2 µ ∇ 2 ψ ( θ, ϕ ) =  Eψ ( θ, ϕ ) = ⇒− 2 µr ℏ2 0 2 � sin  θ ∂θ � ∂θ � sin 2 θ ∂ϕ 2 �<br><!-- End of picture text -->

3 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

2. **Spherical Harmonics and Eigenvalues:** Recognizing that the differential operator in brackets is proportional to the square of the orbital angular momentum operator _L_<sup>ˆ2</sup> . The solutions are the Spherical Harmonics _YJM_ ( _θ, ϕ_ ) with eigenvalues: 



<!-- Start of picture text -->
L ˆ 2 YJM ( θ, ϕ ) =  J ( J + 1)ℏ 2 YJM ( θ, ϕ ) (12)<br><!-- End of picture text -->

Since the kinetic energy of pure rotation is _E_ =<sup>_<u>L</u>_</sup> 2 _I_<sup>2,substitutingtheseeigenvaluesyields</sup> _<u>h</u>_<sup>2</sup> _EJ_ = 8 _π_<sup>2</sup> _I_<sup>_J_(</sup><sup>_J_+ 1).</sup> 

3. **Centrifugal Force Balancing:** For the non-rigid rotor, we equate the centrifugal stretching force to the elastic restoring force (Hooke’s Law) of the bond: 



<!-- Start of picture text -->
Fc =  µrω 2 = µr L 23 =  k ( r − re ) (13)<br><!-- End of picture text -->

Approximating _r ≈ re_ in the centrifugal term yields the stretched bond length: 



<!-- Start of picture text -->
L 2<br>r ≈ re 1 + (14)<br>� kµre 4 �<br><!-- End of picture text -->

4. **Effective Hamiltonian Perturbation:** Substituting the stretched bond length _r_ back into the moment of inertia _I_ = _µr_<sup>2</sup> and the potential energy _V_ ( _r_ ) =<sup><u>1</u></sup> 2<sup>_k_(</sup><sup>_r−re_)2yields the effective</sup> Hamiltonian: 



<!-- Start of picture text -->
L ˆ 2 L ˆ 4<br>H ˆ = − (15)<br>2 µre 2 2 kµ 2 re 6<br><!-- End of picture text -->

- Taking the expectation value of this operator yields the centrifugal correction term _−DJ_<sup>2</sup> ( _J_ + 1)<sup>2</sup> . 

4 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

### **5. Problem-Solving Algorithm** 

#### **Algorithm for Rotational Spectra & Bond Length Calculations** 

1. **Determine** _B_ **from Line Spacings:** 

   -  For a rigid rotor, find the constant spacing between adjacent lines: ∆¯ _ν_ = 2 _B_ . Thus, _B_ = ∆¯ _ν/_ 2. 

   -  For a non-rigid rotor, use two different low-J transition frequencies to set up a system of equations: _ν_ ¯( _J_ ) = 2 _B_ ( _J_ + 1) _−_ 4 _D_ ( _J_ + 1)<sup>3</sup> and solve for both _B_ and _D_ . 

2. **Calculate the Moment of Inertia** _I_ **:** Convert _B_ to SI units (m<sup>_−_1</sup> or Joules) or use the direct formula: 



<!-- Start of picture text -->
h<br>I = where c  = 2 . 99792  ×  10 10 cm/s and B in cm − 1 (16)<br>8 π 2 Bc<br><!-- End of picture text -->

3. **Compute the Isotopic Reduced Mass** _µ_ **:** Convert individual atomic masses _m_ 1 _, m_ 2 from atomic mass units (amu) to kilograms: 



<!-- Start of picture text -->
µ  = ×  1 . 66054  ×  10 − 27 kg (17)<br>� mm 1 +1 m m 2 2 �<br>Length r 0 :<br>I<br>r 0 = [meters] (18)<br>� µ<br><!-- End of picture text -->

4. **Extract the Bond Length** _r_ 0 **:** 

5. **Determine the Vibrational Frequency from** _D_ **(if non-rigid):** Solve for the bond force constant and vibrational wavenumber: 



<!-- Start of picture text -->
4 B 3<br>ω ¯ e = [cm − 1 ] (19)<br>� D<br><!-- End of picture text -->

5 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

### **6. Crucial Pitfalls** 

#### **Common Rotational Spectroscopy Traps** 

-  **Speed of Light Unit Mismatch:** Using _c_ = 3 _×_ 10<sup>8</sup> m/s in the formula _I_ = 8 _π_<sup>2</sup> _<u>hBc</u>_ when _B_ is in cm<sup>_−_1</sup> . This is a massive mistake. You **must** write _c_ = 3 _×_ 10<sup>10</sup> cm/s to match the units, or convert _B_ to m<sup>_−_1</sup> first. 

-  **Incorrect Reduced Mass Calculation:** Calculating reduced mass using standard molar masses (e.g., 35 _._ 5 g/mol for Chlorine) instead of using the exact mass of the specific isotope under study (e.g.,<sup>35</sup> Cl or<sup>37</sup> Cl). Pure rotational spectra easily resolve individual isotopes; failing to specify the isotope yields incorrect transition frequencies. 

-  **Microwave Activity Confusion:** Assuming homonuclear molecules like N2 or O2 can show pure rotational spectra. They cannot, because their permanent dipole moment is strictly zero. Only heteronuclear polar molecules exhibit pure rotational spectra. 

### **7. Standard Textbook Systems** 

-  **The Carbon Monoxide (CO) Rigid Rotor:** Spacing between adjacent lines in its microwave spectrum is observed to be 3 _._ 842 cm<sup>_−_1</sup> . Solving this system yields a bond length of 1 _._ 13<sup>˚</sup> A. 

-  **The Hydrogen Chloride (HCl) Non-Rigid Rotor:** Serves as the classic system to study centrifugal distortion. The rotational constant _B ≈_ 10 _._ 59 cm<sup>_−_1</sup> and the centrifugal constant _D ≈_ 0 _._ 00053 cm<sup>_−_1</sup> illustrate the extremely small but measurable bond stretching at higher _J_ levels. 

-  **Isotopic Splitting in CO:** Comparing the microwave spectra of<sup>12</sup> C<sup>16</sup> O and<sup>13</sup> C<sup>16</sup> O. Since the bond length remains unchanged but the reduced mass increases, the rotational lines of 13C16O are shifted systematically to lower frequencies. 

6 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

## **2 Vibrational Spectra of Diatomic Molecules (Harmonic & Anharmonic Oscillators)** 

### **1. Core Theory** 

Vibrational spectra arise from transitions between quantized vibrational energy levels of a molecule. The physical origin is the coupling of electromagnetic radiation (typically in the infrared region, 100 cm<sup>_−_1</sup> to 4000 cm<sup>_−_1</sup> ) with the fluctuating electric dipole moment of a molecule during its mechanical vibrations. 

-  **The Harmonic Oscillator Model:** This model approximates the molecular potential energy curve near its minimum as a symmetric parabola: _V_ ( _r_ ) =<sup><u>1</u></sup> 2<sup>_k_(</sup><sup>_r −re_)2.Physically,it</sup> assumes that the restoring force is strictly proportional to the displacement from equilibrium (Hooke’s Law). 

-  **The Anharmonic Oscillator Model:** In reality, as a bond stretches, the restoring force weakens, and the bond eventually dissociates at large separations. At very short separations, strong electrostatic repulsions between the nuclei cause the potential to rise much more sharply than a parabola. This asymmetric behavior is modeled mathematically by the **Morse Potential** . 

**Infrared Activity Condition:** For a molecule to absorb or emit infrared radiation during a vibration, its electric dipole moment must change during the vibration: 



<!-- Start of picture text -->
= 0 (20)<br>� ddrµ � r = re<br><!-- End of picture text -->

Homonuclear diatomic molecules (O2 _,_ N2 _,_ H2) do not have a dipole moment at any bond length, so _dµ/dr_ = 0; they are strictly _IR-inactive_ . Heteronuclear diatomics (HCl _,_ CO _,_ NO) have changing dipoles during stretching and are _IR-active_ . 

### **2. Energy Level Framework** 

The quantized energy levels (expressed as Term Values _G_ ( _v_ ) in units of cm<sup>_−_1</sup> ) are governed by the following mathematical equations: 

#### **A. The Harmonic Oscillator** 



<!-- Start of picture text -->
G ( v ) = ω ¯ e v  + 1 (for v = 0 ,  1 ,  2 , . . .  ) (21)<br>� 2 �<br><!-- End of picture text -->

where: 

-  _v_ is the vibrational quantum number, taking non-negative integer values. 

-  _ω_ ¯ _e_ is the equilibrium vibrational wavenumber: 



<!-- Start of picture text -->
1 k<br>ω ¯ e = [cm − 1 ] (22)<br>2 πc � µ<br><!-- End of picture text -->

-  _k_ is the bond force constant (representing bond stiffness, in N/m). 

-  _µ_ is the reduced mass of the molecule (in kg). 

-  _G_ (0) = 2<sup><u>1</u></sup><sup>_ω_¯</sup><sup>_e_isthe</sup><sup>**zero-pointenergy**,representingtheminimumpossibleenergythevi-</sup> brating molecule can have, satisfying the uncertainty principle. 

7 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

#### **B. The Anharmonic Oscillator (Morse Potential)** 

The Morse Potential is defined as: 



<!-- Start of picture text -->
V  ( r ) =  De (23)<br>�1  − e −a ( r−re )�2<br><!-- End of picture text -->

Solving the Schr¨odinger equation with this potential yields the vibrational term values: 



<!-- Start of picture text -->
G ( v ) = ω ¯ e v  + 1 − ω ¯ exe v  + 1 (for v = 0 ,  1 ,  2 , . . .  ) (24)<br>� 2 � � 2 �2<br><!-- End of picture text -->

where: 

 _xe_ is the dimensionless **anharmonicity constant** (typically small and positive, _xe ≈_ 0 _._ 01). 

 The subtraction term causes the energy level spacing to contract as _v_ increases. 

 _De_ is the **classical dissociation energy** (measured from the potential minimum): 



<!-- Start of picture text -->
De = ω ¯ e [cm − 1 ] (25)<br>4 xe<br><!-- End of picture text -->

 _D_ 0 is the **experimental dissociation energy** (measured from the ground state _v_ = 0): 



<!-- Start of picture text -->
D 0 =  De − G (0) =  De − (26)<br>� 21 ω ¯ e − 4 1 ω ¯ exe �<br><!-- End of picture text -->

### **3. Selection Rules & Transitions** 

The rigorous quantum mechanical selection rules are: 

#### **A. The Harmonic Oscillator** 



<!-- Start of picture text -->
∆ v =  ± 1 (27)<br><!-- End of picture text -->

The transition wavenumber for absorption from _v → v_ + 1 is constant: 



<!-- Start of picture text -->
ν ¯ H =  G ( v  + 1)  − G ( v ) = ω ¯ e [cm − 1 ] (28)<br><!-- End of picture text -->

Thus, a harmonic oscillator shows only a single spectral line at _ω_ ¯ _e_ . 

#### **B. The Anharmonic Oscillator** 

The breaking of quadratic symmetry relaxes the selection rules, allowing overtones to appear: 



<!-- Start of picture text -->
∆ v =  ± 1 , ± 2 , ± 3 , . . . (29)<br><!-- End of picture text -->

For transitions starting from the ground state ( _v_ = 0): 

 **Fundamental Transition (** _v_ = 0 _→_ 1 **):** 



<!-- Start of picture text -->
ν ¯fundamental = ω ¯ e (1  − 2 xe ) [cm − 1 ] (30)<br><!-- End of picture text -->



<!-- Start of picture text -->
 First Overtone ( v = 0  → 2 ):<br>ν ¯1st overtone = 2¯ ωe (1  − 3 xe ) [cm − 1 ] (31)<br><!-- End of picture text -->

 **Second Overtone (** _v_ = 0 _→_ 3 **):** 



<!-- Start of picture text -->
ν ¯2nd overtone = 3¯ ωe (1  − 4 xe ) [cm − 1 ] (32)<br><!-- End of picture text -->

8 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

### **4. Derivation Milestones** 

The exact solution for vibrational states involves these key mathematical steps: 

1. **The Schr¨odinger Equation Setup:** Substituting the potential energy _V_ ( _r_ ) into the 1D radial equation (with orbital angular momentum _l_ = 0): 



<!-- Start of picture text -->
− ℏ2 d 2 ψ ( r )<br>+  V  ( r ) ψ ( r ) =  Eψ ( r ) (33)<br>2 µ dr 2<br><!-- End of picture text -->

2. **Coordinate Transformation for Morse Potential:** For the Morse Potential, we introduce a dimensionless variable: 



<!-- Start of picture text -->
z = 2 √ 2 µDe e −a ( r−re ) (34)<br>a ℏ<br><!-- End of picture text -->

This coordinate transform maps the radial equation onto a confluent hypergeometric differential equation. 

3. **Hypergeometric Series Solution:** The regular solution of the confluent hypergeometric equation is written as a power series: 



<!-- Start of picture text -->
∞ k − v<br>w ( z ) = � ckz k with ck +1 = (35)<br>( k  + 1)( k  + 2 α ) ck<br>k =0<br><!-- End of picture text -->

4. **Series Termination and Quantization:** For the wave function to decay at infinity rather than diverge, the infinite series must terminate at a finite index _k_ max = _v_ , forcing _v_ to be a non-negative integer. This termination condition directly yields the energy eigenvalues: 



<!-- Start of picture text -->
Ev = ℏ ωe v  + 1 − ℏ2 ω e 2 v  + 1 (36)<br>� 2 � 4 De � 2 �2<br><!-- End of picture text -->

9 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

### **5. Problem-Solving Algorithm** 

#### **Algorithm for Anharmonic Vibrational Calculations** 

1. **Solve for** _ω_ ¯ _e_ **and** _xe_ **from Transitions:** Given the fundamental transition frequency (¯ _ν_ 1) and the first overtone (¯ _ν_ 2): 



<!-- Start of picture text -->
ν ¯1 = ω ¯ e (1  − 2 xe ) (37)<br><!-- End of picture text -->



<!-- Start of picture text -->
ν ¯2 = 2¯ ωe (1  − 3 xe ) (38)<br><!-- End of picture text -->

Solve this system of linear equations. Divide the second by the first to isolate _xe_ : 



<!-- Start of picture text -->
xe = 2¯ ν 1  − ν ¯2 (39)<br>6¯ ν 1  − 2¯ ν 2<br><!-- End of picture text -->

Substitute _xe_ back to find the equilibrium frequency _ω_ ¯ _e_ = _ν_ ¯1 _/_ (1 _−_ 2 _xe_ ). 

2. **Calculate the Bond Force Constant** _k_ **:** 



<!-- Start of picture text -->
k = 4 π 2 c 2 µω ¯ e 2 where c  = 2 . 99792  ×  10 10 cm/s and µ in kg (40)<br><!-- End of picture text -->

3. **Evaluate Dissociation Energies** _De_ **and** _D_ 0 **:** 



<!-- Start of picture text -->
De = ω ¯ e [cm − 1 ] (41)<br>4 xe<br>D 0 =  De − [cm − 1 ] (42)<br>� 21 ω ¯ e − 1 4 ω ¯ exe �<br><!-- End of picture text -->

To convert dissociation energy to Joules or eV, multiply by _hc_ or use standard conversion factors. 

### **6. Crucial Pitfalls** 

#### **Common Vibrational Spectroscopy Traps** 

-  **Ignoring the Zero-Point Energy in** _D_ 0 **:** Conflating the dissociation energy measured from the potential minimum ( _De_ ) with the physical dissociation energy measured from the ground state ( _D_ 0). Diatomic molecules in their ground state ( _v_ = 0) still possess zero-point energy, so less energy is required to dissociate the bond: _D_ 0 = _De − E_ ZPE. 

-  **Anharmonic Level Spacing Direction:** Assuming the spacing between adjacent levels is constant in anharmonic wells. Spacing decreases as _v_ increases: ∆ _G_ = _G_ ( _v_ + 1) _− G_ ( _v_ ) = _ω_ ¯ _e_ [1 _−_ 2 _xe_ ( _v_ + 1)]. Levels crowd closer together as they approach dissociation. 

-  **Force Constant Velocity Constant Mismatch:** When calculating _k_ = 4 _π_<sup>2</sup> _c_<sup>2</sup> _µω_ ¯ _e_<sup>2,</sup> if _ω_ ¯ _e_ is in cm<sup>_−_1</sup> , _c_ must be in cm/s (3 _×_ 10<sup>10</sup> cm/s). Using _c_ = 3 _×_ 10<sup>8</sup> m/s will result in a value that is out by four orders of magnitude. 

10 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

### **7. Standard Textbook Systems** 

-  **The Carbon Monoxide (CO) Vibrational Spectrum:** Displays a highly intense fundamental absorption at 2143 cm<sup>_−_1</sup> , with a first overtone at 4260 cm<sup>_−_1</sup> . Solving this system yields _ω_ ¯ _e_ = 2170 cm<sup>_−_1</sup> and _xe_ = 0 _._ 0062. 

-  **The Vibration-Rotation Spectrum of HCl:** Shows coupled vibrational and rotational transitions. Because ∆ _J_ = _±_ 1, the spectrum splits into a lower-frequency **P-branch** (∆ _J_ = _−_ 1) and a higher-frequency **R-branch** (∆ _J_ = +1). The **Q-branch** (∆ _J_ = 0) is forbidden and missing, creating a central gap. 

-  **The Deuterium Substitution Effect in HCl vs. DCl:** Replacing Hydrogen with Deuterium increases the reduced mass _µ_ by a factor of nearly two. Since _ω_ ¯ _e ∝_ 1 _/_<sup>_~~√~~_</sup> _<u>µ</u>_ <u>,</u> the vibrational frequency of DCl shifts downward by a factor of approximately _~~√~~_ 2. 

11 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

## **3 Electronic Transitions & The Franck-Condon Principle** 

### **1. Core Theory** 

Electronic transitions in diatomic molecules involve the excitation of an electron from one molecular orbital to another, causing a transition between different electronic states (e.g., singlet-tosinglet or triplet-to-triplet states). Because the energy spacing between electronic states is large (10 _,_ 000 cm<sup>_−_1</sup> to 100 _,_ 000 cm<sup>_−_1</sup> ), electronic transitions are accompanied by simultaneous vibrational and rotational transitions, creating rich, complex bands known as **vibronic spectra** . 

The relative intensities of the vibrational lines within an electronic transition band are governed 

by the **Franck-Condon Principle** . 

-  **Physical Statement:** An electronic transition occurs extremely rapidly ( _∼_ 10<sup>_−_15</sup> s) compared to the typical period of nuclear vibrations ( _∼_ 10<sup>_−_13</sup> s). Therefore, during the electronic transition, the nuclei do not change their spatial positions or momenta. 

-  **Graphical Representation:** On a Morse potential energy diagram, electronic transitions are represented by strictly **vertical lines** . The molecule effectively undergoes an instantaneous transition from the lower electronic potential curve to the upper electronic potential curve without any change in the internuclear distance _r_ . 

### **2. Energy Level Framework** 

The intensity of an electronic-vibrational transition between a ground state vibrational level _v_<sup>_′′_</sup> and an excited state vibrational level _v_<sup>_′_</sup> is proportional to the square of the transition dipole moment **M** _f →i_ : 



<!-- Start of picture text -->
Iv′→v′′ ∝| M f →i| 2 (43)<br><!-- End of picture text -->

Under the **Born-Oppenheimer Approximation** , we separate the total molecular wave function into electronic, vibrational, and rotational components: 



<!-- Start of picture text -->
ψ total =  ψel ( r ;  R ) ψvib ( R ) ψ rot( θ, ϕ ) (44)<br><!-- End of picture text -->

The transition dipole operator is **_µ_** ˆ = **_µ_** ˆ _el_ + **_µ_** ˆ _N_ . The matrix element is: 



<!-- Start of picture text -->
M f →i = ψel ′∗ ( r ;  R ) ψ vib ′∗ ( R ) [ˆ µ el + µ ˆ N ]  ψ el ′′ ( r ;  R ) ψ vib ′′ ( R ) drdR (45)<br>�<br><!-- End of picture text -->

Because the electronic wave functions for different electronic states are orthogonal ( _⟨ψel_<sup>_′|ψ_</sup> _el_<sup>_′′⟩_= 0),</sup> the nuclear dipole term **_µ_** ˆ _N_ integrates to zero. This leaves: 



<!-- Start of picture text -->
M f →i = ψvib ′∗ ( R ) ψel ′∗ ( r ;  R )ˆ µ el ψ el ′′ ( r ;  R ) dr ψvib ′′ ( R ) dR (46)<br>� �� �<br><!-- End of picture text -->

Defining the electronic transition moment as **M** _el_ ( _R_ ) _≡_ � _ψel_<sup>_′∗_</sup><sup>**_µ_**ˆ</sup> _el_<sup>_ψ_</sup> _el_<sup>_′′dr_,and assuming</sup><sup>**M**</sup><sup>_el_(</sup><sup>_R_) varies</sup> slowly with _R_ (the **Franck-Condon Approximation** ), we can pull it out of the integral: 



<!-- Start of picture text -->
M f →i ≈ M el ψvib ′∗ ( R ) ψ vib ′′ ( R ) dR (47)<br>�<br><!-- End of picture text -->

The transition intensity is therefore proportional to the **Franck-Condon Factor (FCF)** : 



<!-- Start of picture text -->
2<br>Iv′→v′′ ∝| M el| 2 ψvib ′∗ ( R ) ψ vib ′′ ( R ) dR =  | M el| 2 |⟨v ′ |v ′′ ⟩| 2 (48)<br>����� ����<br><!-- End of picture text -->

The term _|⟨v_<sup>_′_</sup> _|v_<sup>_′′_</sup> _⟩|_<sup>2</sup> is the Franck-Condon Factor, which represents the square of the **overlap integral** of the vibrational wave functions of the two electronic states. 

12 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

### **3. Selection Rules & Transitions** 

The rigorous selection rules governing electronic transitions in diatomic molecules are: 

1. **Spin Selection Rule:** Transitions can only occur between states of the same spin multiplicity: 

   - ∆ _S_ = 0 (49) 

Thus, Singlet-to-Singlet (<sup>1</sup> Σ _→_<sup>1</sup> Σ) and Triplet-to-Triplet (<sup>3</sup> Π _→_<sup>3</sup> Π) transitions are highly allowed, whereas Singlet-to-Triplet (<sup>1</sup> Σ _→_<sup>3</sup> Σ) transitions are spin-forbidden. 

2. **Orbital Selection Rule:** The change in the projection of the electronic orbital angular momentum along the internuclear axis must satisfy: 



<!-- Start of picture text -->
∆Λ = 0 , ± 1 (50)<br><!-- End of picture text -->

This allows Σ _→_ Σ _,_ Σ _→_ Π _,_ Π _→_ ∆transitions, but forbids Σ _→_ ∆. 

3. **Parity (Laporte) Selection Rule (for homonuclear diatomics):** Transitions must occur between states of different inversion symmetry: 



<!-- Start of picture text -->
g ↔ u (51)<br><!-- End of picture text -->

Thus, _g → u_ and _u → g_ transitions are allowed, whereas _g → g_ and _u → u_ are forbidden. 

4. **Vibrational Selection Rules:** There are **no strict selection rules** for the change in the vibrational quantum number during an electronic transition: 

   - ∆ _v_ = any integer ( _v_<sup>_′_</sup> _− v_<sup>_′′_</sup> = 0 _, ±_ 1 _, ±_ 2 _, . . ._ ) (52) 

The probability of any specific vibronic transition is governed entirely by the magnitude of the Franck-Condon overlap integral _|⟨v_<sup>_′_</sup> _|v_<sup>_′′_</sup> _⟩|_<sup>2</sup> . 

### **4. Derivation Milestones** 

The mathematical formulation of the Franck-Condon Principle is marked by these milestones: 

1. **Born-Oppenheimer Separation:** Asserting that because the electron mass is much smaller than the nuclear mass ( _me/MN ∼_ 10<sup>_−_4</sup> ), electronic motion is instantaneous relative to nuclear motion. This allows the total wave function to be factored as _ψelψvibψrot_ . 

2. **Orthogonality Reduction:** Setting up the transition dipole matrix element and using the orthogonality of the electronic states to prove that the nuclear dipole operator does not contribute to electronic transitions. 

3. **FC Approximation:** Treating the electronic transition moment **M** _el_ ( _R_ ) as a constant independent of the internuclear coordinate _R_ near the equilibrium region. This allows us to separate the electronic transition probability from the nuclear overlap. 

4. **Wave Function Overlap Integration:** Resolving the vibrational wave functions of the ground and excited states (modeled as Hermite-Gauss functions for the ground state or Airy functions near turning points) to compute the spatial overlap integral: 



<!-- Start of picture text -->
⟨v ′ |v ′′ ⟩ = ψv ∗′ ( R ) ψv′′ ( R ) dR (53)<br>� −∞∞<br><!-- End of picture text -->

13 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

### **5. Problem-Solving Algorithm** 

The Franck-Condon Principle allows us to predict the intensity distribution of a vibrational progression based on the change in equilibrium bond length ∆ _r_ = _re_<sup>_′−r_</sup> _e_<sup>_′′_betweenthegroundand</sup> excited electronic states: 

1. **Case A: No Change in Bond Length (** ∆ _r ≈_ 0 **):** 

   -  The minimum of the excited-state potential curve lies directly above the ground-state minimum. 

   -  The vibrational wave function of the ground state _v_<sup>_′′_</sup> = 0 overlaps maximally with the excited state _v_<sup>_′_</sup> = 0 wave function. 

   -  **Intensity Profile:** The (0 _,_ 0) transition is the strongest line in the progression. Transitions to higher _v_<sup>_′_</sup> (such as (1 _,_ 0) _,_ (2 _,_ 0)) drop off rapidly in intensity. 

2. **Case B: Moderate Bond Length Increase (** ∆ _r >_ 0 **):** 

   -  The excited-state potential curve is shifted to larger internuclear distances. 

   -  A vertical line drawn from the center of the _v_<sup>_′′_</sup> = 0 ground state hits the side of the excited-state potential curve, where the excited-state wave functions have high amplitude near their turning points. 

   -  **Intensity Profile:** The (0 _,_ 0) transition is weak. The intensity of the progression increases with _v_<sup>_′_</sup> , peaking at a specific excited vibrational state _v_<sup>_′_</sup> _>_ 0 where the vertical overlap is maximized, before decreasing again. 

3. **Case C: Large Bond Length Increase (** ∆ _r ≫_ 0 **):** 

   -  The excited-state potential curve is shifted significantly to the right. 

   -  A vertical line from the ground state _v_<sup>_′′_</sup> = 0 passes above the dissociation limit of the excited-state potential curve into the continuum. 

   -  **Intensity Profile:** The spectrum shows a few weak, closely-spaced vibrational lines at low _v_<sup>_′_</sup> , followed by a continuous absorption spectrum (the dissociation continuum) representing the dissociation of the molecule into free atoms. 

14 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

### **6. Crucial Pitfalls** 

#### **Common Franck-Condon & Electronic Transition Traps** 

-  **Assuming Homonuclear Molecules are inactive in Electronic Transitions:** Believing that because N2 or O2 are IR and microwave-inactive, they cannot show electronic spectra. This is false. Electronic transitions rearrange the entire electron cloud, which can create a strong transient transition dipole moment. Homonuclear molecules have rich electronic spectra (e.g., the second positive system of N2). 

-  **Treating Franck-Condon as a Selection Rule:** Mistaking the Franck-Condon factor as a rigid selection rule like ∆ _J_ = _±_ 1. It is not a selection rule, but a probability modulator. Any vibrational transition ∆ _v_ is quantum mechanically allowed; the FCF simply determines how bright or dark that specific transition line will be. 

-  **Vibrational Wave Function Nodes:** Forgetting that vibrational wave functions for _v >_ 0 have nodes where the probability density drops to zero. As a result, the intensity of a progression does not always increase smoothly; it can exhibit local minimum ”dips” corresponding to regions where the ground-state wave function aligns with a node of the excited-state wave function. 

### **7. Standard Textbook Systems** 

-  **The Iodine Vapor (I** 2 **) Absorption Spectrum:** Shows a transition from the ground state _X_<sup>1</sup> Σ<sup>+</sup> _g_<sup>totheexcitedstate</sup><sup>_B_3Π</sup> 0<sup>+</sup> _u_<sup>.Becausetheexcited-statebondlengthissignificantly</sup> larger than the ground-state bond length, the spectrum shows a weak (0 _,_ 0) transition, a long progression peaking at _v_<sup>_′_</sup> _≈_ 25, and a clear dissociation continuum starting at 499 _._ 5 nm. 

-  **The Nitrogen (N** 2 **) Second Positive System:** A classic transition between the excited _C_<sup>3</sup> Π _u_ and _B_<sup>3</sup> Π _g_ states, exhibiting rich band heads and sequences that illustrate FranckCondon profiles in homonuclear molecules. 

15 

GATE PHYSICS 

MOLECULAR SPECTROSCOPY OF DIATOMIC MOLECULES 

## **References** 

1. Banwell, C. N., and McCash, E. M. _Fundamentals of Molecular Spectroscopy_ . McGraw-Hill, 1994. 

2. Rajkumar. _Atomic and Molecular Spectra: Laser_ . Kedar Nath Ram Nath, 2015. 

3. Beiser, Arthur. _Concepts of Modern Physics_ . McGraw-Hill, 2003. 

16 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

# **GATE PHYSICS STUDY NOTES Raman and Modern Spectroscopies** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**<br>**The Raman Effect & Raman Spectroscopy**|**2**|
|---|---|
|**2**<br>**Nuclear Magnetic Resonance (NMR) Spectroscopy**|**6**|
|**3**<br>**Electron Spin Resonance (ESR) Spectroscopy**|**9**|
|**4**<br>**X-Ray Spectroscopy**|**13**|
|**5**<br>**M¨ossbauer Spectroscopy**|**16**|



1 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

## **1 The Raman Effect & Raman Spectroscopy** 

### **1. Core Theory** 

The **Raman effect** is the inelastic scattering of monochromatic light by molecules, characterized by a shift in frequency of the scattered photons relative to the incident radiation. 

-  **Classical Explanation:** When a molecule is placed in an external electric field **E** , its electron cloud is deformed, inducing an electric dipole moment **p** = **_α_ E** , where **_α_** is the **polarizability tensor** . If the molecule rotates or vibrates, its shape or orientation changes, modulating the polarizability at the rotational or vibrational frequency. This periodic modulation mixes with the oscillating incident light frequency, generating sidebands corresponding to Stokes and Anti-Stokes lines. The physical origin is thus the **dynamic modulation of the molecular polarizability ellipsoid** . The gross selection rule is: _the polarizability must change during rotation or vibration_ . 

-  **Quantum Mechanical Explanation:** An incident photon of energy _hν_ 0 collides with a molecule, exciting it momentarily to a short-lived, non-resonant **virtual state** . 

   - If the photon scatters elastically, returning the molecule to its original state, the outgoing photon has energy _hν_ 0 ( **Rayleigh scattering** ). 

   - If the photon transfers energy to the molecule (exciting it to a higher vibrational/rotational state), the scattered photon emerges with lower energy _h_ ( _ν_ 0 _−_ ∆ _ν_ ) ( **Stokes scattering** ). 

   - If the molecule transfers energy to the photon (decaying from a pre-excited state to a lower state), the scattered photon emerges with higher energy _h_ ( _ν_ 0 +∆ _ν_ ) ( **Anti-Stokes scattering** ). 

### **2. Energy Level Framework** 

The shift in wavenumber (∆¯ _ν_ ) represents the quantized energy levels of molecular rotation or vibration: 

-  **Rotational Raman Shift:** For a rigid diatomic molecule with rotational constant _B_ , the rotational term values are _F_ ( _J_ ) = _BJ_ ( _J_ + 1). The Raman shifts are: 



<!-- Start of picture text -->
∆¯ ν rot =  ±B (4 J + 6) for J = 0 ,  1 ,  2 , . . . (1)<br><!-- End of picture text -->

where _J_ is the rotational quantum number of the initial state. This places the Stokes and Anti-Stokes lines at: 

   - _ν_ ¯ = _ν_ ¯0 _∓ B_ (4 _J_ + 6) (2) 

-  **Vibrational Raman Shift:** For a diatomic molecule modeled as an anharmonic oscillator with equilibrium frequency _ω_ ¯ _e_ and anharmonicity constant _xe_ , the shift for the fundamental transition ( _v_ = 0 _↔_ 1) is: 



<!-- Start of picture text -->
∆¯ ν vib =  ±ω ¯ e (1  − 2 xe ) (3)<br><!-- End of picture text -->

### **3. Selection Rules & Transitions** 

Under the quantum mechanical formulation of Raman scattering: 

2 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

####  **Pure Rotational Raman Selection Rule:** 



<!-- Start of picture text -->
∆ J = 0 , ± 2 (4)<br><!-- End of picture text -->

- ∆ _J_ = 0 corresponds to Rayleigh scattering. 

- ∆ _J_ = +2 corresponds to Stokes rotational Raman lines ( _J → J_ + 2). 

**–** ∆ _J_ = _−_ 2 corresponds to Anti-Stokes rotational Raman lines ( _J → J −_ 2, initial _J ≥_ 2). 

The first Stokes rotational Raman line ( _J_ = 0 _→_ 2) appears at a shift of 6 _B_ from the Rayleigh line, and all subsequent lines are spaced by 4 _B_ . 

-  **Pure Vibrational Raman Selection Rule:** 



<!-- Start of picture text -->
∆ v =  ± 1 , ± 2 , . . . (5)<br><!-- End of picture text -->

Similar to IR, the fundamental transition ∆ _v_ = _±_ 1 is overwhelmingly dominant. 

-  **Mutual Exclusion Principle:** For molecules with a **center of inversion** (e.g., CO2), transitions that are infrared-active (dipole-allowed) are Raman-inactive (polarizability-forbidden), and vice versa. 

### **4. Derivation Milestones** 

The classical derivation of the Raman frequency components involves these mathematical stages: 

1. **Induced Dipole Form:** Write the time-dependent electric field of the incident wave as **E** ( _t_ ) = **E** 0 cos(2 _πν_ 0 _t_ ) and the induced dipole moment as: 



<!-- Start of picture text -->
p ( t ) =  α ( t ) E 0 cos(2 πν 0 t ) (6)<br><!-- End of picture text -->

2. **Polarizability Modulation:** Expand the polarizability _α_ ( _t_ ) about the equilibrium coordinate _q_ = 0 as a Taylor series with respect to the molecular vibration coordinate _q_ ( _t_ ) = _q_ 0 cos(2 _πν_ vib _t_ ): 



<!-- Start of picture text -->
α ( t )  ≈ α 0 + q 0 cos(2 πν vib t ) (7)<br>� ∂α∂q �0<br><!-- End of picture text -->

3. **Trigonometric Expansion:** Substitute _α_ ( _t_ ) back into **p** ( _t_ ): 



<!-- Start of picture text -->
p ( t ) =  α 0 E 0 cos(2 πν 0 t ) + q 0 E 0 cos(2 πν vib t ) cos(2 πν 0 t ) (8)<br>� ∂α∂q �0<br><!-- End of picture text -->

Using the product identity cos( _A_ ) cos( _B_ ) =<sup><u>1</u></sup> 2<sup>[cos(</sup><sup>_A_+</sup><sup>_B_) + cos(</sup><sup>_A −B_)]yields:</sup> 



<!-- Start of picture text -->
p ( t ) =  α 0 E 0 cos(2 πν 0 t ) + 1 q 0 E 0 [cos(2 π ( ν 0 +  ν vib) t ) + cos(2 π ( ν 0  − ν vib) t )] (9)<br>2 � ∂α∂q �0<br><!-- End of picture text -->

This mathematically isolates the Rayleigh ( _ν_ 0), Stokes ( _ν_ 0 _− ν_ vib), and Anti-Stokes ( _ν_ 0 + _ν_ vib) radiating components. 

3 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

### **5. Problem-Solving Algorithm** 

#### **Analyzing Rotational Raman Spectra** 

1. **Determine the Line Spacing:** For a rotational Raman spectrum, identify the Rayleigh line _ν_ ¯0 and the Stokes lines. Set the constant spacing between adjacent Stokes lines equal to 4 _B_ : ∆¯ _ν_ = 4 _B_ = _⇒ B_ =<sup>∆¯</sup><sup>_ν_</sup> (10) 4 

2. **Identify the First Raman Line:** Verify that the first rotational Raman line (Stokes or Anti-Stokes) is separated from the unshifted Rayleigh line by exactly: 

   - _ν_ ¯0 _− ν_ ¯ _J_ =0 _→_ 2 = 6 _B_ (11) 

3. **Calculate Molecular Parameters:** Convert the rotational constant _B_ to SI units and compute the moment of inertia _I_ = _µr_ 0<sup>2andthebondlength</sup><sup>_r_0,followingthe</sup> standard rigid rotor conversions. 

4. **Stokes vs. Anti-Stokes Intensity:** Use Boltzmann statistics to evaluate the relative intensity of Stokes vs. Anti-Stokes lines: 

_I_ Anti-Stokes = _e_<sup>_−h_∆</sup><sup>_ν/kBT_</sup> (12) _I_ Stokes 

### **6. Crucial Pitfalls** 

#### **Raman Spectroscopy Traps to Avoid** 

-  **Confusing Raman and IR Selection Rules:** Forgetting that homonuclear diatomics (like N2 _,_ O2 _,_ H2), which are completely IR-inactive, are **Raman-active** because their polarizability ellipsoid deforms during stretching. 

-  **The** 6 _B_ **vs.** 4 _B_ **Misalignment:** Confusing the first line shift (6 _B_ ) with the subsequent line-to-line spacing (4 _B_ ) in pure rotational Raman spectra. For a rigid rotor: 

Rayleigh to 1st Stokes Line: ∆¯ _ν_ = 6 _B_ 1st Stokes to 2nd Stokes Line: ∆¯ _ν_ = 4 _B_ 

-  **Anti-Stokes Intensity Error:** Incorrectly assuming Stokes and Anti-Stokes lines have equal intensities. Because fewer molecules reside in pre-excited excited states at thermal equilibrium, Anti-Stokes lines are always significantly weaker than Stokes lines under normal conditions. 

### **7. Standard Textbook Systems** 

-  **The Rotational Raman Spectrum of Nitrogen (N** 2 **):** A classic system where pure rotational lines show an alternating intensity pattern of 2:1 due to nuclear spin statistics ( _I_ = 1 for<sup>14</sup> N), with adjacent line spacings of exactly 4 _B ≈_ 7 _._ 99 cm<sup>_−_1</sup> . 

4 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

-  **The Vibrational Raman Spectrum of Carbon Dioxide (CO** 2 **):** Demonstrates the mutual exclusion principle. The symmetric stretch Σ<sup>+</sup> _g_<sup>(1388cm</sup><sup>_−_1)isRaman-activebutIR-</sup> inactive, while the asymmetric stretch Σ<sup>+</sup> _u_<sup>(2349cm</sup><sup>_−_1)andbendingmodeΠ</sup><sup>_u_(667cm</sup><sup>_−_1)</sup> are IR-active but Raman-inactive. 

5 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

## **2 Nuclear Magnetic Resonance (NMR) Spectroscopy** 

### **1. Core Theory** 

**Nuclear Magnetic Resonance (NMR)** is a resonance spectroscopy based on the transitions of nuclear spins in a strong external magnetic field. 

The physical origin of this phenomenon is that nuclei with a non-zero nuclear spin quantum number _I̸_ = 0 possess an intrinsic nuclear magnetic dipole moment **_µ_** . When placed in a static magnetic field **B** 0, the spherical orientation degeneracy is lifted, splitting the nuclear spin states into distinct Zeeman levels. 

By applying an oscillating radiofrequency (RF) electromagnetic field perpendicular to **B** 0, transitions can be induced when the RF matches the **Larmor precession frequency** of the spins. Physically, NMR probes the local electronic environments of nuclei, as nearby electron clouds partially shield the external field, producing tiny, characteristic shifts in the resonance frequency ( **chemical shift** ) and spin-spin couplings. 

### **2. Energy Level Framework** 

The magnetic properties of a nucleus are defined by its nuclear spin vector **I** and magnetic moment: 



<!-- Start of picture text -->
µ  =  γ I  =  gN µN I / ℏ (13)<br><!-- End of picture text -->

where: 

-  _γ_ is the **gyromagnetic ratio** of the nucleus. 



<!-- Start of picture text -->
 gN is the nuclear g-factor.<br><!-- End of picture text -->



<!-- Start of picture text -->
e ℏ<br> µN = 2 mp is the nuclear magneton .<br><!-- End of picture text -->

In a static magnetic field **B** 0 = _B_ 0 **z** ˆ, the interaction Hamiltonian is: 



<!-- Start of picture text -->
H ˆ =  − µ  ·  B 0 =  −γB 0 ˆ Iz (14)<br><!-- End of picture text -->

The eigenvalues (Zeeman energy levels) are: 



<!-- Start of picture text -->
E ( mI ) =  −γB 0ℏ mI =  −gN µN B 0 mI for mI ∈{−I, −I + 1 , . . . , I} (15)<br><!-- End of picture text -->

For a spin-1/2 nucleus (such as<sup>1</sup> H or<sup>13</sup> C), there are exactly two energy levels: 



<!-- Start of picture text -->
E− 1 / 2 = + 1 (spin down, β ) , E +1 / 2 =  − 1 (spin up, α ) (16)<br>2 γ ℏ B 0 2 γ ℏ B 0<br><!-- End of picture text -->

The energy splitting is: 



<!-- Start of picture text -->
∆ E =  γ ℏ B 0 =  gN µN B 0 (17)<br><!-- End of picture text -->

### **3. Selection Rules & Transitions** 

For magnetic dipole transitions in NMR: 



<!-- Start of picture text -->
∆ mI =  ± 1 (18)<br><!-- End of picture text -->

The resonance condition is: 



<!-- Start of picture text -->
hν 0 = ∆ E = ⇒ ν 0 = γB 0 (Larmor precession frequency) (19)<br>2 π<br><!-- End of picture text -->

6 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

* **Chemical Shift (** _δ_ **):** The local field _B_ local = _B_ 0(1 _− σ_ ) is shielded by the electron screening constant _σ_ , shifting the resonance frequency: 



<!-- Start of picture text -->
δ ≡ ν sample  − ν ref ×  10 6 ppm (20)<br>ν ref<br><!-- End of picture text -->

* **Spin-Spin Coupling (** _J_ **-coupling):** Indirect dipole-dipole coupling mediated by bonding electrons between neighboring spins _I_ 1 and _I_ 2. It splits the resonance lines into multiplets. For a spin-1/2 nucleus coupled to _n_ equivalent neighboring spin-1/2 nuclei, the line splits into: 



<!-- Start of picture text -->
N =  n  + 1 lines (with intensities following Pascal’s triangle) (21)<br><!-- End of picture text -->

If coupled to _n_ nuclei of arbitrary spin _I_ : 



<!-- Start of picture text -->
N = 2 nI + 1 lines (22)<br><!-- End of picture text -->

### **4. Derivation Milestones** 

The derivation of the NMR resonance and precession condition follows these steps: 

1. **Torque Equation:** Relate the rate of change of spin angular momentum **I** to the magnetic torque: 



<!-- Start of picture text -->
d I<br>(23)<br>dt =  µ  ×  B 0 = ⇒ d dt µ =  γ µ  ×  B 0<br><!-- End of picture text -->

2. **Precession Solution:** Substitute **B** 0 = _B_ 0 **z** ˆ into the differential system. The components satisfy: 



<!-- Start of picture text -->
dµx dµy dµz<br>dt =  γµyB 0 , dt =  −γµxB 0 , dt = 0 (24)<br><!-- End of picture text -->

Differentiating again decoupling the variables yields<sup>_d_</sup> _dt_<sup>2</sup><sup>_<u>µ</u>_2</sup><sup>_<u>x</u>_+ (</sup><sup>_γB_0)2</sup><sup>_µx_=0,representingpre-</sup> cession about **z** ˆ at angular frequency _ω_ 0 = _γB_ 0. 

3. **Zeeman Projection:** Apply first-order perturbation theory to project the magnetic moment operator eigenvalues, demonstrating the linear dependency of Zeeman splitting on external field strength _B_ 0. 

7 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

### **5. Problem-Solving Algorithm** 

#### **Algorithm for NMR Multiplet Analysis** 

1. **Compute Resonance Frequency:** Given _γ_ or _gN_ and _B_ 0, calculate the baseline resonance Larmor frequency: _ν_ 0 =<sup>_<u>γB</u>_0</sup> (25) 2 _π_ 

2. **Calculate Chemical Shift Displacements:** Find sample shifts: 

   - ∆ _ν_ shift = _δ_ (ppm) _×_ 10<sup>_−_6</sup> _× ν_ operating (26) 

3. **Analyze Neighboring Spin Multiplets (** _J_ **-coupling):** Locate chemically nonequivalent spin groups. For a targeted group, count the number of neighboring equivalent spins _n_ and their spin value _I_ . The number of split peaks is: 

      - _N_ = 2 _nI_ + 1 (27) 

4. **Establish Multiplicity Intensities:** For spin-1/2 neighbors, expand (1 + _x_ )<sup>_n_</sup> or use Pascal’s triangle (e.g., _n_ = 1 _→_ 1 : 1 doublet, _n_ = 2 _→_ 1 : 2 : 1 triplet, _n_ = 3 _→_ 1 : 3 : 3 : 1 quartet). 

### **6. Crucial Pitfalls** 

#### **NMR Spectroscopy Traps to Avoid** 

-  **Using Gyromagnetic Ratio in Wrong Units:** Forgetting whether _γ_ is given in rad _·_ T<sup>_−_1</sup> _·_ s<sup>_−_1</sup> or Hz _·_ T<sup>_−_1</sup> . If in rad, you must divide by 2 _π_ to obtain the frequency in Hz. 

-  **Confusing operating frequency and coupling constant:** Assuming _J_ -coupling constants scale with the external magnetic field _B_ 0. _J_ **-coupling is field-independent** (remains in Hz regardless of spectrometer strength), whereas chemical shifts (in Hz) are strictly proportional to _B_ 0 (though their ppm values are field-independent). 

-  **Neglecting** _I_ = 0 **Nuclei:** Forgetting that isotopes with even numbers of protons and neutrons (like<sup>12</sup> C and<sup>16</sup> O) have _I_ = 0 and are completely NMR-silent. 

### **7. Standard Textbook Systems** 

-  **The**<sup>1</sup> **H NMR Spectrum of Ethanol (CH** 3 **CH** 2 **OH):** Shows three distinct resonance groups reflecting three chemical environments: a triplet for the _−_ CH3 protons (coupled to 2 _−_ CH2 _−_ protons), a quartet for the _−_ CH2 _−_ protons (coupled to 3 _−_ CH3 protons), and a singlet for the _−_ OH proton (due to rapid chemical exchange). 

-  **The**<sup>1</sup> **H NMR Spectrum of 2-Bromopropane (** ( **CH** 3)2 **CHBr):** Demonstrates spinspin coupling with high degeneracy. The six equivalent methyl _−_ CH3 protons are split by the single central _−_ CH _−_ proton into a 1 : 1 doublet, while the central proton is split by the six methyl protons into a septet (1 : 6 : 15 : 20 : 15 : 6 : 1 multiplet). 

8 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

## **3 Electron Spin Resonance (ESR) Spectroscopy** 

### **1. Core Theory** 

**Electron Spin Resonance (ESR)** , also known as Electron Paramagnetic Resonance (EPR), is the study of transitions between magnetic energy levels of unpaired electrons in a static magnetic field. 

The physical origin of this phenomenon is the Zeeman interaction of the electron’s spin magnetic dipole moment **_µ_** _s_ . Because the electron’s magnetic moment is roughly 658 times larger than the proton’s nuclear magnetic moment, ESR transitions occur in the microwave region (9 _−_ 35 GHz) rather than the radiofrequency region. 

ESR serves as the premier probe to identify and characterize unpaired electrons in free radicals, transition metal complexes, and lattice defects. The local fields of nearby magnetic nuclei couple with the electron spin, producing a highly characteristic **hyperfine splitting** that acts as an atomic fingerprint of the molecular coordinate distribution. 

### **2. Energy Level Framework** 

The magnetic moment of an electron is governed by its spin angular momentum **S** : 



<!-- Start of picture text -->
µ s =  −geµB S / ℏ (28)<br><!-- End of picture text -->

where: 

 _ge ≈_ 2 _._ 0023 is the Land´e g-factor of a free electron. 



<!-- Start of picture text -->
e ℏ<br> µB = 2 me is the Bohr magneton .<br><!-- End of picture text -->

In an external magnetic field **B** 0 = _B_ 0 **z** ˆ, the spin-Zeeman Hamiltonian is: 



<!-- Start of picture text -->
H ˆ =  − µ s ·  B 0 =  geµBB 0 ˆ Sz/ ℏ (29)<br><!-- End of picture text -->

The eigenvalues are: 



<!-- Start of picture text -->
E ( ms ) =  gµBB 0 ms for ms =  ± 1 / 2 (30)<br><!-- End of picture text -->

For a single unpaired electron, this yields two levels: 



<!-- Start of picture text -->
E +1 / 2 = + 1 E− 1 / 2 =  − 1 (31)<br>2 gµBB 0 , 2 gµBB 0<br><!-- End of picture text -->

The energy splitting is: 



<!-- Start of picture text -->
∆ E =  gµBB 0 (32)<br><!-- End of picture text -->

In material media, the spin-orbit coupling modifies the local g-factor, making _g_ anisotropic and characteristic of the chemical environment: 



<!-- Start of picture text -->
∆ E =  g eff µBB 0 (33)<br><!-- End of picture text -->

9 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

### **3. Selection Rules & Transitions** 

For magnetic dipole transitions in ESR: 



<!-- Start of picture text -->
∆ ms =  ± 1 , ∆ mI = 0 (34)<br><!-- End of picture text -->

The resonance condition is: 



<!-- Start of picture text -->
hν =  gµBB 0 (35)<br><!-- End of picture text -->

* **Hyperfine Splitting:** The electron spin interacts with nearby nuclear spins **I** _i_ via the isotropic Fermi contact interaction and anisotropic dipolar coupling, splitting the ESR resonance into multiple components. For an electron coupled to a nucleus of spin _I_ , the resonance splits into: 



<!-- Start of picture text -->
N = 2 I + 1 lines (of equal intensity) (36)<br><!-- End of picture text -->

If coupled to _n_ equivalent magnetic nuclei of spin _I_ : 



<!-- Start of picture text -->
N = 2 nI + 1 lines (37)<br><!-- End of picture text -->

If coupled to multiple non-equivalent sets of nuclei ( _n_ of spin _Ia_ , _m_ of spin _Ib_ ): 



<!-- Start of picture text -->
N = (2 nIa  + 1)(2 mIb  + 1) lines (38)<br><!-- End of picture text -->

### **4. Derivation Milestones** 

The derivation of ESR energy shifts under hyperfine interactions follows these stages: 

1. **Total Hamiltonian Formulation:** Write the Hamiltonian containing both electronic Zeeman and nuclear hyperfine terms: 



<!-- Start of picture text -->
H ˆ =  gµBB 0 ˆ Sz  +  A ˆ I  ·  ˆ S (39)<br><!-- End of picture text -->

where _A_ is the isotropic hyperfine coupling constant. 

2. **First-Order Perturbation Approximation:** For strong magnetic fields, the Zeeman term dominates ( _gµBB_ 0 _≫ A_ ). The hyperfine term can be approximated by its diagonal component along the field axis: 



<!-- Start of picture text -->
ˆ I  ·  ˆ S  ≈ I ˆ z  ˆ Sz (40)<br><!-- End of picture text -->

3. **Eigenvalue Resolution:** The energy eigenvalues of the coupled system are: 



<!-- Start of picture text -->
E ( ms, mI ) =  gµBB 0 ms  +  AmsmI (41)<br><!-- End of picture text -->

Evaluating the transitions under the selection rules ∆ _ms_ = _±_ 1 _,_ ∆ _mI_ = 0 yields the transition energies: 



<!-- Start of picture text -->
hν =  E (1 / 2 , mI )  − E ( − 1 / 2 , mI ) =  gµBB 0 +  AmI (42)<br><!-- End of picture text -->

This mathematically shows that the resonance line splits into (2 _I_ + 1) components spaced by _A_ (in units of magnetic field or frequency). 

10 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

### **5. Problem-Solving Algorithm** 

#### **Deciphering ESR Hyperfine Spectra** 

1. **Find the Land´e g-factor:** Given the operating microwave frequency _ν_ and the center of the magnetic field resonance _B_ 0, calculate _g_ : 

_hν g_ = (43) _µBB_ 0 

_Note: Keep track of constants: µB ≈_ 9 _._ 274 _×_ 10<sup>_−_24</sup> _J/T, h ≈_ 6 _._ 626 _×_ 10<sup>_−_34</sup> _J · s._ 

2. **Count the Lines of Equivalent Sets:** If the spectrum exhibits _N_ symmetric lines of equal spacing, determine the nuclear spin configuration. For _n_ equivalent protons ( _I_ = 1 _/_ 2): 

      - _N_ = _n_ + 1 lines (intensities follow Pascal’s triangle) (44) 

   - For equivalent deuterium nuclei ( _I_ = 1): 

_N_ = 2 _n_ + 1 lines (intensities follow trinomial coefficients) (45) 

3. **Decompose Non-Equivalent Splittings:** For nested splittings, multiply multiplicities. Work from the largest coupling constant (outermost coarse split) to the smallest (innermost fine split). 

### **6. Crucial Pitfalls** 

#### **ESR Spectroscopy Traps to Avoid** 

-  **Bohr vs. Nuclear Magneton Units:** Mistakenly using the nuclear magneton _µN_ instead of the Bohr magneton _µB_ in the ESR resonance equation. Since _me ≪ mp_ , _µB_ is about 1836 times larger than _µN_ . Using _µN_ will cause your calculated resonant field or frequency to be off by orders of magnitude. 

-  **First-Derivative Presentation Confusion:** Forgetting that ESR spectra are conventionally presented as the **first derivative of the absorption curve** ( _dχ_<sup>_′′_</sup> _/dB_ ). When counting lines, count the number of zero-crossings or peak pairs, not just positivegoing absorption envelopes. 

-  **Neglecting Hyperfine Selection Rules:** Assuming transitions can occur between different nuclear states. The selection rule ∆ _mI_ = 0 is strict; the nuclear spin does not flip during electronic transitions. 

### **7. Standard Textbook Systems** 

-  **The Methyl Radical (** _·_ **CH** 3 **):** A planar radical where the unpaired electron couples equivalently with the three protons ( _I_ = 1 _/_ 2). The ESR spectrum consists of exactly _N_ = 3+1 = 4 lines (a quartet) with relative intensity ratios of 1 : 3 : 3 : 1. 

-  **The Hydrogen Atom (Free H):** A single electron coupled to a single proton ( _I_ = 1 _/_ 2). 

11 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

The ESR spectrum consists of _N_ = 2(1)(1 _/_ 2)+1 = 2 symmetric lines of equal intensity (1 : 1 doublet) split by a massive isotropic hyperfine coupling of _A ≈_ 50 _._ 7 mT (or 1420 MHz). 

12 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

## **4 X-Ray Spectroscopy** 

### **1. Core Theory** 

**X-ray spectroscopy** analyzes the characteristic high-energy radiation emitted or absorbed when inner-shell electrons of heavy atoms undergo transitions, providing a direct diagnostic of core electronic binding energies and atomic numbers. 

The physical origin of characteristic X-rays is the ionization of a tightly bound core electron (typically from the _n_ = 1 or _n_ = 2 shells) by high-energy electron bombardment or synchrotron radiation. This leaves a highly unstable core hole. A outer-shell electron (from _n_ = 2 _,_ 3, etc.) undergoes a rapid radiative decay to fill the hole, emitting a high-energy photon in the X-ray region (0 _._ 01 _−_ 10 nm). 

Because the inner-shell electrons are close to the nucleus, they are minimally shielded by outer valence electrons, making their transition energies highly sensitive to the bare nuclear charge _Z_ , as formulated by **Moseley’s Law** . 

### **2. Energy Level Framework** 

The core electronic energy levels are designated by spectroscopic shell notation: _K_ ( _n_ = 1), _L_ ( _n_ = 2), _M_ ( _n_ = 3), _N_ ( _n_ = 4), etc. * **Transitions:** * ** _Kα_ line:** Transition of an electron from the _L_ shell ( _n_ = 2) to the _K_ shell ( _n_ = 1). * ** _Kβ_ line:** Transition of an electron from the _M_ shell ( _n_ = 3) to the _K_ shell ( _n_ = 1). * ** _Lα_ line:** Transition of an electron from the _M_ shell ( _n_ = 3) to the _L_ shell ( _n_ = 2). 

The frequency _ν_ of the characteristic X-rays is governed by **Moseley’s Law**: 



<!-- Start of picture text -->
√ ν =  a ( Z − σ ) (46)<br><!-- End of picture text -->

where: 

-  _Z_ is the atomic number of the element. 

-  _a_ is a constant related to the Rydberg frequency _νR ≈_ 3 _._ 29 _×_ 10<sup>15</sup> Hz: 



<!-- Start of picture text -->
a  = νR − 1 (47)<br>� � n 1 2 1 n 2 2 �<br><!-- End of picture text -->

-  _σ_ is the **screening constant** (shielding factor) representing the electrostatic shielding of the nucleus by remaining electrons inside the core. 

   - For _Kα_ transitions ( _n_ 2 = 2 _→ n_ 1 = 1), the single remaining electron in the _K_ -shell shields the nucleus, yielding: 



<!-- Start of picture text -->
σ ≈ 1 = ⇒ νKα =  νR ( Z − 1) 2 1  − 1 = 3 (48)<br>� 4 � 4 νR ( Z − 1)2<br><!-- End of picture text -->

- For _Lα_ transitions ( _n_ 2 = 3 _→ n_ 1 = 2), the shielding is much larger: 



<!-- Start of picture text -->
σ ≈ 7 . 4 (49)<br><!-- End of picture text -->

13 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

### **3. Selection Rules & Transitions** 

Because X-ray emission is driven by electric dipole (E1) transitions, they must obey the standard atomic selection rules in the coupled fine-structure basis: 



<!-- Start of picture text -->
∆ l  =  ± 1 , ∆ j = 0 , ± 1 (excluding j = 0  → j = 0) (50)<br><!-- End of picture text -->

Due to spin-orbit splitting of the _L_ shell (2 _s_ 1 _/_ 2 _,_ 2 _p_ 1 _/_ 2 _,_ 2 _p_ 3 _/_ 2), the _Kα_ line splits into a fine-structure doublet: 

-  ** _Kα_ 1 line:** Transition from 2 _p_ 3 _/_ 2 _→_ 1 _s_ 1 _/_ 2 (highly allowed). 

-  ** _Kα_ 2 line:** Transition from 2 _p_ 1 _/_ 2 _→_ 1 _s_ 1 _/_ 2 (allowed). 

-  The transition 2 _s_ 1 _/_ 2 _→_ 1 _s_ 1 _/_ 2 is strictly forbidden because ∆ _l_ = 0. 

### **4. Derivation Milestones** 

The derivation of Moseley’s Law and transition frequencies utilizes Bohr’s model modified by electrostatic shielding: 

1. **Shielded Potential Formulation:** Write the effective electrostatic potential experienced by an electron in an outer shell as: 



<!-- Start of picture text -->
V eff( r ) =  − ( Z − σ ) e 2 (51)<br>4 πϵ 0 r<br><!-- End of picture text -->

2. **Energy Level Assignment:** Solve the radial wave equation using this effective charge. The energy eigenvalues are: 



<!-- Start of picture text -->
mee 4 ( Z − σ ) 2 ( Z − σ ) 2<br>En =  − =  −hνR (52)<br>32 π 2 ϵ 2 0 ℏ2 n 2 n 2<br><!-- End of picture text -->

3. **Difference Evaluation:** Calculate the energy difference between the destination shell _n_ 1 and the starting shell _n_ 2: 



<!-- Start of picture text -->
− 1<br>hν =  En 2 − En 1 =  hνR ( Z − σ ) 2 (53)<br>� n 1 2 1 n 2 2 �<br><!-- End of picture text -->

Taking the square root of both sides directly yields Moseley’s law:<sup>_~~√~~_</sup> _<u>ν</u>_ = _σ_ ). 

~~�~~ _νR_ <u>�</u> _n_<sup>_−_</sup> 1<sup>2</sup> _− n_<sup>_−_</sup> 2<sup>2</sup> <u>�(</u> _Z−_ 

14 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

### **5. Problem-Solving Algorithm** 

#### **Analyzing Characteristic X-Ray Transitions** 

1. **Identify the Transition Line:** Convert designations to quantum numbers (e.g., _Kα → n_ 2 = 2 _, n_ 1 = 1, screening constant _σ_ = 1). 

2. **Formulate the Wavelength Relation:** Express the wavelength _λ_ using Moseley’s law: 



<!-- Start of picture text -->
1 1  − 1 = 3 (54)<br>λ =  R∞ ( Z − 1)2 � 4 � 4 R∞ ( Z − 1)2<br><!-- End of picture text -->

where _R∞_ = _νR/c ≈_ 1 _._ 097 _×_ 10<sup>7</sup> m<sup>_−_1</sup> is the Rydberg constant. 

3. **Solve for the Atomic Number** _Z_ **:** Given _λ_ , calculate: 



<!-- Start of picture text -->
4 4<br>( Z − 1) 2 = = ⇒ Z = 1 + (55)<br>3 λR∞ � 3 λR∞<br>Ratios: For comparative problems between elements Z 1<br>ν 1 = λ 2 = ( Z 1  − 1)2 λ 2 = Z 1  − 1 (56)<br>ν 2 λ 1 ( Z 2  − 1) 2 = ⇒ � λ 1 Z 2  − 1<br><!-- End of picture text -->

4. **Apply to Multi-Element Ratios:** For comparative problems between elements _Z_ 1 and _Z_ 2: 

### **6. Crucial Pitfalls** 

#### **X-Ray Spectroscopy Traps to Avoid** 

-  **Using** _Z_ **Instead of** ( _Z −_ 1) **for** _Kα_ **Lines:** Forgetting to include the screening constant ( _σ_ = 1) in the frequency formula. Using _ν ∝ Z_<sup>2</sup> instead of _ν ∝_ ( _Z −_ 1)<sup>2</sup> introduces substantial errors, especially for lighter elements. 

-  **Confusing Characteristic X-Rays with Bremsstrahlung:** Confusing the sharp, quantized characteristic peaks with the continuous background spectrum of X-rays ( **Bremsstrahlung** or ”braking radiation”). Bremsstrahlung has a sharp shortwavelength cutoff _λ_ min = _eVhc_ 0<sup>governedbytheDuane-Huntlimit,whichdependsonly</sup> on the accelerating voltage _V_ 0, whereas characteristic lines depend strictly on the target element _Z_ . 

### **7. Standard Textbook Systems** 

-  **The Copper Target X-Ray Tube (** _Z_ = 29 **):** A ubiquitous laboratory source where highenergy electron excitation produces extremely intense _Kα_ lines at _λ ≈_ 1 _._ 54<sup>˚</sup> A, used as the standard wavelength for X-ray diffraction (XRD) experiments. 

-  **Moseley’s Original Demonstration:** The systematic analysis of _Kα_ wavelengths across elements from Calcium ( _Z_ = 20) to Zinc ( _Z_ = 30), which provided the first physical proof that the periodic table is ordered by nuclear charge (atomic number) rather than atomic weight. 

15 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

## **5 M¨ossbauer Spectroscopy** 

### **1. Core Theory** 

**M¨ossbauer spectroscopy** is a high-resolution nuclear resonance spectroscopy based on the recoilless emission and absorption of gamma-ray photons by nuclei bound in a solid lattice. 

The physical origin of this phenomenon is that when a free nucleus in a gas emits a gamma-ray photon of energy _Eγ_ , it must conserve momentum by recoiling. This recoil removes a small portion of the transition energy: 



<!-- Start of picture text -->
E 2<br>ER = γ (57)<br>2 Mc 2<br><!-- End of picture text -->

This recoil energy shift is many orders of magnitude larger than the natural linewidth of the nuclear transition (Γ _∼_ 10<sup>_−_9</sup> eV), completely preventing resonant absorption by another free nucleus. 

Rudolf M¨ossbauer discovered that if the emitting and absorbing nuclei are locked within a cold, rigid crystal lattice, the momentum of the recoil is absorbed by the entire macro-crystal mass ( _M_ crystal _→∞_ ). Under these conditions, the recoil energy shifts vanish ( _ER →_ 0), enabling **recoilless resonance**. 

Because the natural linewidth Γ is extremely narrow, M¨ossbauer spectroscopy is sensitive to tiny perturbations in the nuclear energy levels caused by local electronic environments. By moving the source relative to the absorber, the gamma-ray energy can be finely modulated via the **Doppler shift** ( _v ∼_ mm/s) to map these shifts. 

### **2. Energy Level Framework** 

The resonance energy changes are mapped to three main hyperfine parameters: 

-  **Isomer Shift (** _δ_ **isomer):** A shift in the center of the resonance spectrum caused by the electrostatic interaction between the nuclear charge distribution and the non-zero s-electron density _|ψ_ (0) _|_<sup>2</sup> at the nucleus: 



<!-- Start of picture text -->
δ isomer = 4 5 π Ze 2 R 2 � ∆ RR �� |ψ (0) | 2 absorber −|ψ (0) | source 2 � (58)<br><!-- End of picture text -->

where ∆ _R_ = _R_ excited _− R_ ground is the difference in nuclear radii. 

-  **Quadrupole Splitting (** ∆ _EQ_ **):** If the nucleus has a non-spherical charge distribution (nuclear spin _I >_ 1 _/_ 2, possessing a electric quadrupole moment _Q_ ) and is placed in an asymmetric electronic environment (possessing a non-zero **Electric Field Gradient (EFG)** _q ∝ Vzz_ ), the interaction splits the nuclear states: 



<!-- Start of picture text -->
eQVzz<br>EQ ( mI ) = �3 m 2 I − I ( I + 1) � (59)<br>4 I (2 I − 1)<br><!-- End of picture text -->

For<sup>57</sup> Fe, the excited state ( _I_<sup>_∗_</sup> = 3 _/_ 2) splits into two sublevels ( _mI_ = _±_ 3 _/_ 2 _, ±_ 1 _/_ 2), while the ground state ( _I_ = 1 _/_ 2) remains unsplit, splitting the single resonance line into a symmetric doublet. 

-  **Magnetic Hyperfine Splitting (Zeeman Splitting):** Interaction between the nuclear magnetic moment and a local magnetic field _B_ int (internal or external), splitting the levels into 2 _I_ + 1 Zeeman states: 



<!-- Start of picture text -->
EM ( mI ) =  −gN µN B int mI (60)<br><!-- End of picture text -->

16 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

### **3. Selection Rules & Transitions** 

Transitions between nuclear states must satisfy selection rules for magnetic dipole (M1) or electric quadrupole (E2) radiation. For<sup>57</sup> Fe ( _I_<sup>_∗_</sup> = 3 _/_ 2 _→ I_ = 1 _/_ 2 transition): 



<!-- Start of picture text -->
∆ I = 1 = ⇒ ∆ mI = 0 , ± 1 (61)<br><!-- End of picture text -->

* Under **Isomer Shift** alone: Single unsplit line. * Under **Quadrupole Splitting** alone: Two transitions (∆ _mI_ = _±_ 1 and ∆ _mI_ = 0), producing a **doublet**. * Under **Magnetic Hyperfine Splitting** alone: Six allowed transitions out of the eight possible combinations, producing a characteristic **sextet** with intensity ratios of 3 : 4 : 1 : 1 : 4 : 3 for powder samples. 

### **4. Derivation Milestones** 

The derivation of M¨ossbauer recoil-free fractions and line shifts involves: 

1. **Recoil Energy Formulation:** Conserve momentum between the photon and the free emitting nucleus: 



<!-- Start of picture text -->
pγ =  p nucleus = ⇒ E c γ =  Mv = ⇒ v = Mc Eγ (62)<br><!-- End of picture text -->

The kinetic energy of recoil is: 



<!-- Start of picture text -->
E 2<br>γ<br>ER = 1 2 Mv 2 = 2 Mc 2 (63)<br><!-- End of picture text -->

2. **Lattice Quantization:** Treat the crystal lattice as a quantum harmonic oscillator with phonon frequencies _ω_ . The probability of recoilless emission (the **Lamb-M¨ossbauer factor** _f_ ) is: 



<!-- Start of picture text -->
f =  e −⟨x 2 ⟩/λ 2 (64)<br><!-- End of picture text -->

where _⟨x_<sup>2</sup> _⟩_ is the mean square displacement of the emitting atom and _λ_ = ℏ _/pγ_ is the reduced wavelength of the gamma ray. Resonant emission requires _⟨x_<sup>2</sup> _⟩≪ λ_<sup>2</sup> , which is satisfied at low temperatures and high Debye temperatures. 

3. **Doppler Tuning:** Relate the velocity _v_ of the source to the shifted energy change: 



<!-- Start of picture text -->
v<br>∆ E Doppler =  Eγ (65)<br>c<br><!-- End of picture text -->

17 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

### **5. Problem-Solving Algorithm** 

#### **Interpreting M¨ossbauer Spectra** 

1. **Convert Doppler Velocity to Energy:** Given a resonance velocity peak _v_ in mm/s, calculate the corresponding energy shift: 



<!-- Start of picture text -->
v<br>∆ E =  Eγ (66)<br>c<br><!-- End of picture text -->

_Example: For_<sup>57</sup> _Fe, Eγ_ = 14 _._ 4 _keV ≈_ 2 _._ 3 _×_ 10<sup>_−_15</sup> _J. A velocity of_ 1 _mm/s corresponds to a tiny shift of_ ∆ _E ≈_ 4 _._ 8 _×_ 10<sup>_−_8</sup> _eV._ 

2. **Identify Quadrupole Doublet Spacings:** For quadrupole doublets, the splitting value ∆ _EQ_ is the velocity separation between the two peaks: 

   - ∆ _EQ_ = _|v_ 1 _− v_ 2 _|_ mm/s (67) 

3. **Decompose Magnetic Sextets:** For<sup>57</sup> Fe sextets, check the symmetry. The spacing between outer peaks yields the total splitting of the nuclear ground and excited states, allowing calculation of the internal magnetic field _B_ int. 

### **6. Crucial Pitfalls** 

#### **M¨ossbauer Spectroscopy Traps to Avoid** 

-  **Units Conversion Errors:** Forgetting that M¨ossbauer spectra coordinates are plotted in units of **velocity (mm/s)** rather than frequency or wavelength. You must utilize the relation ∆ _E_ = _Eγ_<sup>_<u>v</u>_</sup> _c_<sup>totransformvelocitybacktoenergy.</sup> 

-  **Incorrect Quadrupole Assignment for** _I_ = 1 _/_ 2 **:** Expecting quadrupole splitting in nuclei with ground states _I ≤_ 1 _/_ 2. A nucleus with spin 1 _/_ 2 is spherical and has no electric quadrupole moment ( _Q_ = 0), so it cannot undergo quadrupole splitting. Splitting only occurs if the excited state has _I >_ 1 _/_ 2 (as in<sup>57</sup> Fe, where _I_<sup>_∗_</sup> = 3 _/_ 2). 

-  **Assuming All Materials exhibit M¨ossbauer Spectra:** Forgetting that the M¨ossbauer effect is strictly restricted to solid state lattices at low temperatures to ensure the Lamb-M¨ossbauer factor is non-zero ( _f →_ 1). 

#### **Classic Exam System (**<sup>57</sup> **Fe decay scheme):** 

The<sup>57</sup> Fe isotope is the premier M¨ossbauer probe. It is formed via the electron capture decay of<sup>57</sup> Co (half-life 270 days), which populates the 14 _._ 4 keV excited state ( _I_<sup>_∗_</sup> = 3 _/_ 2) of<sup>57</sup> Fe. The transition from this state to the ground state ( _I_ = 1 _/_ 2) emits the 14 _._ 4 keV gamma ray. 

### **7. Standard Textbook Systems** 

-  **The**<sup>57</sup> **Fe Sextet in Ferromagnetic Iron (** _α_ **-Fe):** Demonstrates nuclear magnetic Zeeman splitting. Due to the intense internal magnetic field ( _B_ int _≈_ 33 T at room temperature), the 14 _._ 4 keV transition splits into six distinct symmetric peaks, with intensity ratios of 3 : 4 : 1 : 

18 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

1 : 4 : 3. 

-  **The Nitroprusside Isomer Reference:** Sodium nitroprusside (Na2[Fe(CN)5NO] _·_ 2H2O) exhibits a large, highly temperature-independent quadrupole doublet (∆ _EQ ≈_ 1 _._ 7 mm/s), serving as the standard reference compound for calibrating M¨ossbauer spectrometers. 

19 

GATE PHYSICS 

RAMAN & MODERN SPECTROSCOPIES 

## **References** 

1. Banwell, C. N., and McCash, Elaine M. _Fundamentals of Molecular Spectroscopy_ . McGrawHill, 1994. 

2. Rajkumar. _Atomic and Molecular Spectra: Laser_ . Kedar Nath Ram Nath, 2015. 

3. Beiser, Arthur. _Concepts of Modern Physics_ . McGraw-Hill, 2003. 

20 

