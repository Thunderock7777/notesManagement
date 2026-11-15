<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-pauli-exclusion-principle-fermions-4.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answers** 



<!-- Start of picture text -->
• Total Ground-State Energy ( E total): 24 (in units of 2 πmL 2 h ¯ 22 )<br><!-- End of picture text -->



<!-- Start of picture text -->
• Fermi Energy / Fermi Level ( EF ): 5 (in units of 2 πmL 2 h ¯ 22 )<br><!-- End of picture text -->

_(Note: Depending on the specific GATE key convention, if the prompt asks for total groundstate energy, the answer is_ **_24_** _; if it specifically asks for the highest filled single-particle energy level at_ 0 _K, the answer is_ **_5_** _)._ 

## **Detailed Step-by-Step Solution** 

**1. Single-Particle Energy Levels in a 2D Square Box** For a 2D infinite square well of length _L_ (0 _≤ x ≤ L,_ 0 _≤ y ≤ L_ ), the single-particle energy levels are: 



<!-- Start of picture text -->
E ( nx, ny ) = 2 π mL 2 h ¯22 ( n 2 x +  n 2 y ) where nx, ny ∈{ 1 ,  2 ,  3 , . . . }<br><!-- End of picture text -->

Letting _E_ 0 = 2<sup>_<u>π</u>_</sup> _mL_<sup>2</sup><sup>_<u>h</u>_¯22bethebaseunitofenergy:</sup> 



<!-- Start of picture text -->
E ( nx, ny ) = ( nx 2 +  n 2 y ) E 0<br><!-- End of picture text -->

**2. Energy Level Spectrum & Degeneracies** Let’s list the lowest single-particle energy levels in increasing order: 

|Quantum||||Spin|Cumulative|
|---|---|---|---|---|---|
|Numbers<br>(_nx, ny_)|_n_<sup>2</sup><br>_x_ <sup>+</sup><sup>_n_2</sup><br>_y_|Energy (_E_)|Spatial<br>Degeneracy|Capacity<br>(_gs_ = 2)|Electron<br>Capacity|
|(1_,_1)|1<sup>2 </sup>+ 1<sup>2 </sup>= 2|2_E_0|1|2 electrons|**2**|
|(1_,_2) **&** (2_,_1)|1<sup>2 </sup>+ 2<sup>2 </sup>= 5|5_E_0|2|4 electrons|**6**|
|(2_,_2)|2<sup>2 </sup>+ 2<sup>2 </sup>= 8|8_E_0|1|2 electrons|8|
|(1_,_3) **&** (3_,_1)|1<sup>2 </sup>+ 3<sup>2 </sup>= 10|10_E_0|2|4 electrons|12|



Notes 

2 

**3. Filling** _N_ = 6 **Electrons at** _T_ = 0 **K (Pauli Exclusion Principle)** Since electrons are **spin-1/2 fermions** , each spatial orbital ( _nx, ny_ ) can hold a maximum of **2 electrons** (one spin-up _ms_ = +1/2 and one spin-down _ms_ = _−_ 1/2). 

At 0 K, electrons fill the lowest available energy levels: 

   1. **First Level —** (1 _,_ 1) **State:** 

      - Energy = 2 _E_ 0 

      - Number of electrons placed = **2** 

      - Contribution to total energy = 2 _×_ 2 _E_ 0 = **4E0** 

   2. **Second Level —** (1 _,_ 2) **and** (2 _,_ 1) **States:** 

      - Energy = 5 _E_ 0 

      - Number of electrons needed to reach _N_ = 6: 6 _−_ 2 = **4** electrons. 

      - Place 2 electrons in (1 _,_ 2) and 2 electrons in (2 _,_ 1). 

      - Contribution to total energy = 4 _×_ 5 _E_ 0 = **20E0** 

**4. Total Ground-State Energy (** _E_ **total)** Summing the energies of all 6 electrons: _E_ total = 2(2 _E_ 0) + 2(5 _E_ 0) + 2(5 _E_ 0) = 4 _E_ 0 + 20 _E_ 0 = **24E0** 



<!-- Start of picture text -->
E total =  24<br>2mL 2<br>( π 2h ¯ 2 )<br><!-- End of picture text -->

**5. Fermi Level / Fermi Energy (** _EF_ **)** The **Fermi energy (** _EF_ **)** is defined as the energy of the **highest occupied single-particle state** at _T_ = 0 K. 

   - The highest occupied single-particle states are (1 _,_ 2) and (2 _,_ 1). 

   - Their energy is _EF_ = (1<sup>2</sup> + 2<sup>2</sup> ) _E_ 0 = 5 _E_ 0. 



<!-- Start of picture text -->
EF =  5<br>2mL 2<br>( π 2h ¯ 2 )<br><!-- End of picture text -->

## **Key Concepts & Summary for GATE Physics** 

## **1. Energy Expressions for Rigid Box Potentials** 

|Dimension|Energy Formula<br>_E_(**n**)|Ground State (_ni_ = 1)|Ground State<br>Degeneracy|
|---|---|---|---|
|**1D Box**<br>(0_≤x ≤L_)|_En_ = <sup>_n_2</sup><sup>_π_2¯</sup><sup>_h_2</sup><br>2_mL_<sup>2</sup>|1_· E_0|Non-degenerate|
|**2D Square Box**<br>(_L × L_)|_Enx,ny_ =<br>(_n_<sup>2</sup><br>_x_<sup>+</sup><sup>_n_2</sup><br>_y_<sup>)</sup><sup>_π_2¯</sup><sup>_h_2</sup><br>2_mL_<sup>2</sup>|2_· E_0|Non-degenerate|
|**3D Cubic Box**<br>(_L × L × L_)|_Enx,ny,nz_ =<br>(_n_<sup>2</sup><br>_x_<sup>+</sup><sup>_n_2</sup><br>_y_<sup>+</sup><sup>_n_2</sup><br>_z_<sup>)</sup><sup>_π_2¯</sup><sup>_h_2</sup><br>2_mL_<sup>2</sup>|3_· E_0|Non-degenerate|



Notes 

3 

**2. Quick Reference for Filling** _N_ **-Fermion 2D Box Systems** 

   - _N_ = 2 **electrons:** Fill (1 _,_ 1) = _⇒ E_ total = 2 _×_ 2 = 4 _E_ 0, _EF_ = 2 _E_ 0. 

   - _N_ = 4 **electrons:** Fill 2 in (1 _,_ 1) and 2 in (1 _,_ 2) = _⇒ E_ total = 4 + 10 = 14 _E_ 0, _EF_ = 5 _E_ 0. 

   - _N_ = 6 **electrons:** Fill 2 in (1 _,_ 1), 2 in (1 _,_ 2), 2 in (2 _,_ 1) = _⇒ E_ total = 4+20 = 24 _E_ 0, _EF_ = 5 _E_ 0. 

   - _N_ = 8 **electrons:** Fill 2 in (1 _,_ 1), 4 in level-5, 2 in (2 _,_ 2) = _⇒ E_ total = 4+20+16 = 40 _E_ 0, _EF_ = 8 _E_ 0. 

**Follow-up suggestion:** Would you like to solve a similar Fermi energy question for a **3D cubic box** or for **non-interacting spinless bosons** in a 2D box? 

