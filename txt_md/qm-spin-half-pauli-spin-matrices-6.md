<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-spin-half-pauli-spin-matrices-6.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Yes, you are completely right to raise this! The overall requirement for symmetry depends strictly on whether the particle is a **fermion** or a **boson** . 

To eliminate any confusion, we must separate **spin symmetry** (pure math of spin combination) from **total wavefunction symmetry** (dictated by particle type). 

## **1. Spin Part Symmetry (Pure Spin Addition Algebra)** 

When you combine two spin-1/2 states, the resulting spin states have fixed exchange symmetry **regardless of whether the particle is a fermion or boson** : 



<!-- Start of picture text -->
• Triplet State ( S = 1 ):<br>1 ↔ 2<br>– | ↑ 1 ↑ 2 ⟩ −−→| ↑ 2 ↑ 1 ⟩ = + | ↑ 1 ↑ 2 ⟩<br>– 1 1 ↔ 2<br>√ 2 ( | ↑ 1 ↓ 2 ⟩ +  | ↓ 1 ↑ 2 ⟩ ) −−→ + √ 1 2 ( | ↑ 1 ↓ 2 ⟩ +  | ↓ 1 ↑ 2 ⟩ )<br>1 ↔ 2<br>– | ↓ 1 ↓ 2 ⟩ −−→ + | ↓ 1 ↓ 2 ⟩<br><!-- End of picture text -->



<!-- Start of picture text -->
χ spin is ALWAYS SYMMETRIC for Triplet<br>• Singlet State ( S = 0 ):<br>– 1 1 ↔ 2<br>√ 2 ( | ↑ 1 ↓ 2 ⟩−| ↓ 1 ↑ 2 ⟩ ) −−→− √ 1 2 ( | ↑ 1 ↓ 2 ⟩−| ↓ 1 ↑ 2 ⟩ )<br>χ spin is ALWAYS ANTISYMMETRIC for Singlet<br><!-- End of picture text -->

## **2. Total Wavefunction Requirement (Spin-Statistics Theorem)** 

Here is where **Fermion vs. Boson** enters: 

Ψtotal(1 _,_ 2) = _ψ_ spatial( _x_ 1 _, x_ 2) _× χ_ spin(1 _,_ 2) 

|Particle Type|Total Wavefunction Requirement (Ψtotal)|
|---|---|
|**Fermions** (Half-integer spin: electrons,<br>protons, spin-1/2)|**MUST be ANTISYMMETRIC** under<br>exchange|



Notes 

2 

Particle Type Total Wavefunction Requirement (Ψtotal) **Bosons** (Integer spin: photons, alpha **MUST be SYMMETRIC** under exchange particles, spin-1) 

**3. How Spatial Symmetry (** _ψ_ **spatial) is Dictated** 

Because **electrons are Fermions** , the total product Ψtotal = _ψ_ spatial _× χ_ spin **must equal Antisymmetric (-)** : 

**Case A: For Fermions (Spin-1/2 Electrons)** 

- **Triplet Spin (Symmetric** (+) **):** 



<!-- Start of picture text -->
Total ( − ) =  ψ spatial ( − )  × χ spin (+)<br><!-- End of picture text -->



<!-- Start of picture text -->
= ⇒ ψ spatial MUST BE ANTISYMMETRIC<br><!-- End of picture text -->

- **Singlet Spin (Antisymmetric** ( _−_ ) **):** 



<!-- Start of picture text -->
Total ( − ) =  ψ spatial (+)  × χ spin ( − )<br><!-- End of picture text -->



<!-- Start of picture text -->
= ⇒ ψ spatial MUST BE SYMMETRIC<br><!-- End of picture text -->

**Case B: What if they were Bosons?** If hypothetical spin-1/2 particles were **Bosons** , total Ψtotal would have to be **Symmetric (+)** : 

- **Triplet Spin (Symmetric** (+) **):** 



<!-- Start of picture text -->
Total (+) =  ψ spatial (+)  × χ spin (+)<br>= ⇒ ψ spatial would be SYMMETRIC<br><!-- End of picture text -->

## **Summary Rule for GATE** 

1. **Spin state alone:** Triplet is always **(+) Symmetric** , Singlet is always **(-) Antisymmetric** . 

2. **Particle identity:** Fermions require overall **(-) Antisymmetric** , Bosons require overall **(+) Symmetric** . 

3. **Spatial state:** Adjusted to ensure the product ( _ψ_ spatial _× χ_ spin) matches the particle’s overall requirement. 

