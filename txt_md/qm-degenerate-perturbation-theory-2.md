<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-degenerate-perturbation-theory-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**Correct Answer** 

**Option (b): 0** 

## **Detailed Step-by-Step Solution** 

**1. Analyze the Unperturbed Hamiltonian (** _H_ 0 **)** The unperturbed Hamiltonian is given as: 



<!-- Start of picture text -->
H 0 = 10 02 00<br>0 0 2<br> <br><!-- End of picture text -->

Since _H_ 0 is already diagonal, its eigenvalues are the diagonal elements: 



<!-- Start of picture text -->
• Ground State Energy ( E 1 (0) ): E 1 (0) = 1 (Non-degenerate, g = 1)<br>• Excited State Energy ( E 2 (0) =  E 3 (0) ): E 2 (0) = 2 (2-fold degenerate, g = 2)<br><!-- End of picture text -->

The unperturbed ground state eigenstate is: 



<!-- Start of picture text -->
1<br>|ψ 1 (0) ⟩ = 0<br>0<br> <br><!-- End of picture text -->

## **2. Determine Which Perturbation Theory to Use** 

- The question asks specifically for the correction to the **ground state** ( _E_ 1<sup>(0)</sup> = 1). 

- Because the ground state is **non-degenerate** , we use **standard non-degenerate perturbation theory** . _(We do_ **_not_** _need degenerate perturbation theory here, even though the excited states are degenerate!)_ 

**3. Calculate the First-Order Energy Correction (** _E_ 1<sup>(1)</sup><sup>**)**</sup> According to first-order non-degenerate perturbation theory, the energy correction to state _n_ is the expectation value of the perturbation operator _H_<sup>_′_</sup> in the unperturbed state _|ψn_<sup>(0)</sup><sup>_⟩_:</sup> 

Notes 

2 



<!-- Start of picture text -->
E 1 (1) =  ⟨ψ 1 (0) |H ′|ψ 1 (0) ⟩ =  H 11 ′<br><!-- End of picture text -->

Given: 



<!-- Start of picture text -->
H ′ =  ϵ 01 10 00<br>0 0 1<br> <br><!-- End of picture text -->

The matrix element _H_ 11<sup>_′_issimplythetop-leftelementof</sup><sup>_H′_:</sup> 



<!-- Start of picture text -->
H 11 ′ = (1 0 0)  01 10 00 10<br>0 0 1 0<br> ϵ     =  ϵ ·  0 =  0<br><!-- End of picture text -->

Thus, the first-order energy correction to the ground state is 0. 

## **Bonus Concept Extension: What if GATE asked for the Excited States?** 

If the question had asked for the first-order corrections to the **excited state** ( _E_<sup>(0)</sup> = 2): 



<!-- Start of picture text -->
1. The excited state subspace is 2-fold degenerate, spanned by states | 2 ⟩ = 01<br>0<br>  and<br><!-- End of picture text -->



<!-- Start of picture text -->
0<br>| 3 ⟩ = 0<br>1<br> .<br>2. The 2 × 2 perturbation matrix W in this degenerate subspace is built from the<br>bottom-right 2  ×  2 block of H ′ :<br><!-- End of picture text -->



<!-- Start of picture text -->
0<br>W =  ϵ<br>0 1<br>(0 )<br><!-- End of picture text -->

3. The eigenvalues of _W_ give the first-order corrections: 



<!-- Start of picture text -->
E 2 (1) = 0 and E 3 (1) =  ϵ<br><!-- End of picture text -->

4. So the perturbed excited state energies would be 2 + 0 = 2 and 2 + _ϵ_ . 

## **Key Concepts & Formulae to Remember for GATE** 

**1. The First Rule of Perturbation Theory Problems** Always check the **degeneracy of the target state** first before setting up any matrices: 

- **Target state is Non-Degenerate:** Simply pick the corresponding diagonal matrix element _Hnn_<sup>_′_.</sup> 

   - _E_<sup>(1)</sup> = _H_<sup>_′_</sup> _n nn_ 

- **Target state is Degenerate:** Extract the sub-block of _H_<sup>_′_</sup> corresponding to those degenerate states and find its eigenvalues. 

Notes 

3 

**2. Matrix Element Shortcut for Matrix Hamiltonians** For a Hamiltonian in standard basis representation: 



<!-- Start of picture text -->
0<br> ... <br> <br>If |ψn (0) ⟩ =  en = 1 (1 at the n -th position)<br> <br> ... <br>0<br><!-- End of picture text -->

Then the expectation value _⟨ψn_<sup>(0)</sup><sup>_|H′|ψ_</sup> _n_<sup>(0)</sup><sup>_⟩_is</sup><sup>**alwaysthe**</sup><sup>_n_</sup><sup>**-thdiagonalelement**</sup><sup>_H_</sup> _nn_<sup>_′_</sup> of the perturbation matrix _H_<sup>_′_</sup> . 

