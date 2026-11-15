<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-spin-half-pauli-spin-matrices-3.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **1. Quantum Coupling of Two Spin-1/2 Particles** 

When two spin-<sup><u>1</u></sup> 2<sup>particles (such as two electrons,</sup><sup>_s_1=</sup><sup><u>1</u></sup> 2<sup>and</sup><sup>_s_2=</sup> 2<sup><u>1</u>) combine, their total</sup> spin operator is: 



<!-- Start of picture text -->
S  =  s 1 +  s 2<br><!-- End of picture text -->

According to the rules of addition of angular momentum: 

- The total spin quantum number _S_ ranges from _|s_ 1 _− s_ 2 _|_ to _s_ 1 + _s_ 2 in integer steps: 



<!-- Start of picture text -->
1<br>S = and S  =  1<br>2 − 1 2 2 + 1 2 = ⇒ S  =  0<br>���� ���� , 1<br><!-- End of picture text -->

- For each total spin _S_ , the magnetic spin quantum number _MS_ takes 2 _S_ +1 possible values: 



<!-- Start of picture text -->
MS ∈{−S, −S  + 1 , . . . ,  + S}<br><!-- End of picture text -->

**2. Detailed Breakdown of the Singlet State (** _S_ = 0 **)** 

**A. Definition & Wavefunction** Setting _S_ = 0 yields a single combined state ( _MS_ = 0). Constructed from the uncoupled basis _{| ↑↑⟩, | ↑↓⟩, | ↓↑⟩, | ↓↓⟩}_ , the singlet spin wavefunction is: 



<!-- Start of picture text -->
χ singlet =  | S  =  0 ,  MS =  0 ⟩ = 1 ( | ↑↓⟩−| ↓↑⟩ )<br>√ 2<br><!-- End of picture text -->

**B. Exchange Symmetry** Under the permutation operator _P_<sup>ˆ</sup> 12 (interchanging particle 1 _↔_ 2): 



<!-- Start of picture text -->
P ˆ12 χ singlet = √ 1 2 ( | ↓↑⟩−| ↑↓⟩ ) =  − √ 1 2 ( | ↑↓⟩−| ↓↑⟩ ) =  −χ singlet<br><!-- End of picture text -->

- **The Singlet spin state is strictly ANTISYMMETRIC (-) under particle exchange.** 

Notes 

2 

## **C. Degeneracy of the Singlet State** 

- **Spin Multiplicity Formula:** _gS_ = 2 _S_ + 1 

- For _S_ = 0: 

_g_ 0 = 2(0) + 1 = **1** (Non-degenerate / Single state) 

**3. Detailed Breakdown of the Triplet States (** _S_ = 1 **)** 

**A. Definition & Wavefunctions** Setting _S_ = 1 yields three distinct projection states ( _MS_ = +1 _,_ 0 _, −_ 1): 

1. **Top State (** _MS_ = +1 **):** 



<!-- Start of picture text -->
|S = 1 , MS = +1 ⟩ =  | ↑↑⟩<br><!-- End of picture text -->



<!-- Start of picture text -->
2. Middle State ( MS = 0 ):<br><!-- End of picture text -->



<!-- Start of picture text -->
|S = 1 , MS = 0 ⟩ = 1<br>√ 2 ( | ↑↓⟩ +  | ↓↑⟩ )<br><!-- End of picture text -->

3. **Bottom State (** _MS_ = _−_ 1 **):** 



<!-- Start of picture text -->
|S = 1 , MS =  − 1 ⟩ =  | ↓↓⟩<br><!-- End of picture text -->

**B. Exchange Symmetry** Applying the permutation operator _P_<sup>ˆ</sup> 12 to each of the three states: 



<!-- Start of picture text -->
• P ˆ 12 | ↑↑⟩ = + | ↑↑⟩<br>• P ˆ 12 � √ 12 ( | ↑↓⟩ +  | ↓↑⟩ ) � = + √ 1 2 ( | ↑↓⟩ +  | ↓↑⟩ )<br><!-- End of picture text -->

- _P_<sup>ˆ</sup> 12 _| ↓↓⟩_ = + _| ↓↓⟩_ 

- **All three Triplet spin states are strictly SYMMETRIC (+) under particle exchange.** 

## **C. Degeneracy of the Triplet State** 

- For _S_ = 1: 

_g_ 1 = 2(1) + 1 = **3** (Threefold / 3-fold degenerate) 

- In the absence of an external magnetic field ( **B** = 0) or internal spin-orbit coupling, all three states share the **exact same energy** . 

## **4. What is Degeneracy & How is it Lifted?** 

**What is Degeneracy? Degeneracy** ( _g_ ) represents the existence of **two or more linearly independent quantum states that share the exact same energy eigenvalue** ( _H|ψk⟩_ = _E|ψk⟩_ ). 

- The total spin Hilbert space dimension for two spin-1/2 particles is: 



<!-- Start of picture text -->
2  ×  2 = 4 states = ⇒ 1 (Singlet) + 3 (Triplet) = 4 states<br>� �� � � �� �<br>S =0 S =1<br><!-- End of picture text -->

Notes 

3 

## **Lifting Spin Degeneracy** 

1. **In Zero Magnetic Field (B** = 0 **):** The triplet level remains 3-fold degenerate because spatial rotations do not prefer any _z_ -axis ( _MS_ = +1 _,_ 0 _, −_ 1 are energyequivalent). 

2. **In an External Magnetic Field (B** _̸_ = 0 **- Zeeman Effect):** The magnetic interaction Hamiltonian _H_<sup>ˆ</sup> _Z_ = _−µ ·_ **B** = _gsµBBzS_<sup>ˆ</sup> _z_ / _h_ ¯ splits the 3-fold degenerate triplet into **three distinct energy sublevels** separated by ∆ _E_ = _gsµBBz_ : 

   - _E_ ( _MS_ = +1) = _E_ 0 + _gsµBB_ 

   - _E_ ( _MS_ = 0) = _E_ 0 

   - _E_ ( _MS_ = _−_ 1) = _E_ 0 _− gsµBB_ 

## **5. Pauli Exclusion Principle & Total Wavefunction Symmetry** 

For two identical **fermions** (electrons), the total wavefunction Ψ(1 _,_ 2) must be **completely antisymmetric** under coordinate exchange: 



<!-- Start of picture text -->
Ψ total (1 ,  2) =  ψ spatial ( r 1 , r 2)  × χ spin (1 ,  2) =  Antisymmetric (-)<br><!-- End of picture text -->

This imposes a direct constraint between spatial symmetry and spin state: 

|Spin State|Spin Symmetry|Required Spatial<br>Wavefunction<br>Symmetry (_ψ_spatial)|Resulting Combination|
|---|---|---|---|
|**Singlet (**_S_ = 0**)**|**Antisymmetric (-)**|**Symmetric (+)**|_ψ_symmetric_×_<br>_χ_antisymmetric =<br>Antisymmetric (-)|
|**Triplet (**_S_ = 1**)**|**Symmetric (+)**|**Antisymmetric (-)**|_ψ_antisymmetric_×_<br>_χ_symmetric =<br>Antisymmetric (-)|



## **6. Physical Origin of Exchange Energy Splitting (** 2 _J_ **)** 

Even though the Coulomb potential _V_ ( _r_ 12) = 4 _πϵ_ 0 _|er_<sup>2</sup> 1 _−r_ 2 _|_<sup>doesnotcontainanyspinoper-</sup> ators, the **spin alignment dictates spatial distribution** , which drastically alters the electrostatic repulsion! 

1. **Triplet State (Spatially Antisymmetric** _ψA_ **):** 



<!-- Start of picture text -->
ψA ( r 1 , r 2) = 1<br>√ 2 [ ψa ( r 1) ψb ( r 2)  − ψa ( r 2) ψb ( r 1)]<br><!-- End of picture text -->

- As _r_ 1 _→ r_ 2, _ψA_ ( _r_ 1 _, r_ 1) = 0. 

- The probability of finding two parallel-spin electrons at the same position vanishes ( **“Fermi Hole”** ). 

- Electrons stay further apart on average, **reducing Coulomb repulsion** . 

Notes 

4 

2. **Singlet State (Spatially Symmetric** _ψS_ **):** 



<!-- Start of picture text -->
ψS ( r 1 , r 2) = 1<br>√ 2 [ ψa ( r 1) ψb ( r 2) +  ψa ( r 2) ψb ( r 1)]<br><!-- End of picture text -->

- As _r_ 1 _→ r_ 2, _ψS_ ( _r_ 1 _, r_ 1) _̸_ = 0. 

- Electrons have an enhanced probability of being close together ( **“Fermi Heap”** ). 

- Electrostatic repulsion is significantly higher. 



<!-- Start of picture text -->
e 2<br>First-Order Perturbation Energy Shift: Evaluating ⟨ 4 πϵ 0 r 12 ⟩ yields:<br><!-- End of picture text -->



<!-- Start of picture text -->
∆ E singlet =  I +  J<br>∆ E triplet =  I − J<br><!-- End of picture text -->

- **Direct Coulomb Integral (** _I >_ 0 **):** Classical electrostatic repulsion between charge clouds. 

- **Exchange Integral (** _J >_ 0 **):** Purely quantum mechanical overlap integral: 



<!-- Start of picture text -->
e 2<br>J = d 3 r 1 d 3 r 2  ψa ∗ ( r 1) ψ b ∗ ( r 2) ψa ( r 2) ψb ( r 1)  >  0<br>� � 4 πϵ 0 r 12 �<br><!-- End of picture text -->



<!-- Start of picture text -->
E singlet  − E triplet =  2J<br><!-- End of picture text -->

Thus, **the Triplet state lies lower in energy than the corresponding Singlet state by** 2 _J_ (Hund’s First Rule: Maximum multiplicity gives the lowest energy state). 

## **7. Application: Helium Atom Spectrum (Parahelium vs. Orthohelium)** 

In a Helium atom ( _Z_ = 2): 

1. **Ground State Configuration** (1 _s_ )<sup>2</sup> **:** 

   - Both electrons occupy the 1 _s_ orbital ( _a_ = _b_ = 1 _s_ ). 

   - The spatial wavefunction is strictly symmetric: _ψ_ spatial = _ψ_ 1 _s_ ( _r_ 1) _ψ_ 1 _s_ ( _r_ 2). 

   - Therefore, by Pauli Exclusion, the spin state **must be a Singlet (** _S_ = 0 **)** . 

   - **The** 1<sup>3</sup> _S_ 1 **Triplet ground state is physically impossible/missing!** 

2. **Excited Configurations** (1 _s_ )( _ns_ ) **or** (1 _s_ )( _np_ ) **:** 

   - **Parahelium (** _S_ = 0 **, Singlet terms):** Antiparallel spins. 

   - **Orthohelium (** _S_ = 1 **, Triplet terms):** Parallel spins. 

   - Since ∆ _S_ = 0 for electric dipole transitions ( _E_ 1), transitions between Parahelium and Orthohelium are strictly forbidden (“Intersystem Crossing Prohibition”). 

## **Summary Table for Quick Revision** 

Notes 

5 

|Property|Spin Singlet State|Spin Triplet States|
|---|---|---|
|**Total Spin Quantum**<br>**Number (**_S_**)**|_S_ = 0|_S_ = 1|
|**Magnetic Substates**<br>**(**_MS_**)**|_MS_ = 0|_MS_ = +1_,_0_, −_1|
|**Degeneracy**<br>**(**_g_ = 2_S_+ 1**)**|_g_ = 1 (Non-degenerate)|_g_ = 3 (3-fold degenerate)|
|**Spin Exchange**|**Antisymmetric (-)**|**Symmetric (+)**|
|**Symmetry**|||
|**Spatial Exchange**<br>**Symmetry**|**Symmetric (+)**|**Antisymmetric (-)**|
|**Electron Spatial**<br>**Distribution**|Clustered (“Fermi Heap”)|Avoid each other (“Fermi Hole”)|
|**Relative Energy Level**|Higher energy (_E_0+_I_ +_J_)|**Lower energy (**_E_0+_I −J_**)**|
|**Helium Classification**|Parahelium|Orthohelium|



**Follow-up suggestion:** Would you like to practice calculating **spectroscopic term symbols (**<sup>2</sup><sup>_S_+1</sup> _LJ_ **)** for two-electron configurations (like 2 _p_<sup>2</sup> or 4 _p_ 4 _d_ ) or explore how an external magnetic field breaks this 3-fold triplet degeneracy via the **Zeeman effect** ? 

