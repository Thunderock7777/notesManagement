<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-bloch-wavefunction-and-theorem-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **1. What is** _uk_ ( _r_ ) **?** 

The function _uk_ ( _r_ ) (or _uk_ ( _x_ ) in 1D) is called the **cell-periodic function** or **Bloch amplitude function** . 

- **Physical Meaning:** It represents the **modulation of the electron wave caused by the periodic atomic potential** of the crystal lattice. 

   - If an electron were completely free (no potential barriers or ion cores), its wavefunction would be a pure plane wave _ψ_ ( _r_ ) = _Ae_<sup>_ik·r_</sup> , where the probability density _|ψ_ ( _r_ ) _|_<sup>2</sup> = _|A|_<sup>2</sup> is a flat constant everywhere. 

   - In a real crystal, the electron feels the strong electrostatic potential of positively charged ion cores at every lattice site. _uk_ ( _r_ ) modulates the wave so that the electron density adapts its spatial shape near each atomic nucleus inside the unit cell. 

- **Strict Periodicity:** It satisfies the exact lattice translation condition _uk_ ( _r_ + _R_ ) = _uk_ ( _r_ ) (or _uk_ ( _x_ + _a_ ) = _uk_ ( _x_ ) in 1D). This means _uk_ ( _r_ ) repeats **identically in every single unit cell** throughout the crystal lattice. 

- **Dependence on Wavevector** _k_ **:** The subscript _k_ indicates that the internal shape of _uk_ ( _r_ ) inside the unit cell depends on the electron’s crystal momentum wavevector _k_ (and energy band). Near _k_ = 0, _u_ 0( _r_ ) closely resembles atomic orbitals centered around the ion cores. 

## **2. What does the Translational Phase-Shift Property tell us in detail?** 

The relation _ψk_ ( _x_ + _a_ ) = _ψk_ ( _x_ ) _e_<sup>_ika_</sup> (or in 3D, _ψk_ ( _r_ + _R_ ) = _ψk_ ( _r_ ) _e_<sup>_ik·R_</sup> ) is an equivalent mathematical statement of Bloch’s Theorem. 

It is derived by evaluating the Bloch wavefunction _ψk_ ( _x_ ) = _uk_ ( _x_ ) _e_<sup>_ikx_</sup> at _x_ + _a_ : 



<!-- Start of picture text -->
ψk ( x  +  a ) =  uk ( x  +  a ) e ik ( x + a ) = � uk ( x ) e ikx � e ika =  ψk ( x ) e ika<br>� �� �<br>= uk ( x )<br><!-- End of picture text -->

This property reveals **three fundamental physical principles** : 

Notes 

2 

**A. Electron Probability Density is Strictly Periodic Across Unit Cells** Calculating the probability of finding the electron at position _x_ + _a_ : 



<!-- Start of picture text -->
|ψk ( x  +  a ) | 2 = �� ψk ( x ) eika ��2 =  |ψk ( x ) | 2  · |eika| 2 =  |ψk ( x ) | 2<br>� �� �<br>=1<br><!-- End of picture text -->

- **Physical Meaning:** The **electron probability density** _|ψk_ ( _x_ ) _|_<sup>2</sup> **is 100% identical at equivalent positions in every unit cell** across the entire crystal. The electron is not trapped at a single atomic site; it is **delocalized** equally throughout the entire crystal volume. 

**B. Constant Phase Gradient & Unhindered Wave Propagation** While the _probability amplitude |ψk_ ( _x_ ) _|_<sup>2</sup> is identical from cell to cell, the _complex wave function_ acquires a **spatial phase shift of** ∆ _ϕ_ = _ka_ (or _k · R_ in 3D) when moving to the adjacent unit cell. 

- This constant phase shift across unit cells gives the Bloch state the character of a **propagating traveling wave** . 

- It explains why electrons can glide through a perfect periodic lattice for large distances **without scattering** off the ion cores (explaining the high conductivity of pure metals and semiconductors). 

**C. Eigenvalue of the Lattice Translation Operator** In quantum mechanics, shifting a wavefunction spatially by one lattice vector _a_ is represented by the **translation operator** _T_<sup>ˆ</sup> _a_ , defined as _T_<sup>ˆ</sup> _aψ_ ( _x_ ) = _ψ_ ( _x_ + _a_ ). 

- Because the crystal Hamiltonian _H_<sup>ˆ</sup> possesses periodic lattice symmetry ( _V_ ( _x_ + _a_ ) = _V_ ( _x_ )), it commutes with the translation operator: [ _H,_<sup>ˆ</sup> _T_<sup>ˆ</sup> _a_ ] = 0. 

- Consequently, energy eigenfunctions _ψk_ ( _x_ ) are simultaneous **eigenstates of the translation operator** : 

   - _T_ ˆ _aψk_ ( _x_ ) = _Cψk_ ( _x_ ) 

- Since _T_<sup>ˆ</sup> _a_ is a unitary operator (preserving probability norm), its eigenvalue _C_ must have a magnitude of 1, taking the form _C_ = _e_<sup>_ika_</sup> . 

- Thus, _ψk_ ( _x_ + _a_ ) = _e_<sup>_ika_</sup> _ψk_ ( _x_ ) **is simply the eigenvalue equation for crystal translation symmetry** . 

Would you like to cover **Module 5: Dielectrics, Magnetism & Superconductivity** next to complete your Solid State Physics syllabus, or work through a GATE problem on the Kronig-Penney dispersion relation? 

