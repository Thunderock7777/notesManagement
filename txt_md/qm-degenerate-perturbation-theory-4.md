<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-degenerate-perturbation-theory-4.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

That is a very perceptive question! The short answer is: **Finding the eigenvalues of a matrix IS diagonalizing the matrix.** 

Here is the step-by-step breakdown of why this method is called **Exact Diagonalization** , why it works as a shortcut, and what is happening under the hood mathematically. 

## **1. What does “Diagonalizing” a Hamiltonian actually mean?** 

In Quantum Mechanics, “diagonalizing” a Hamiltonian matrix _H_ means finding a change of basis (a unitary matrix _P_ ) such that _H_ transforms into a pure diagonal matrix _D_ : 



<!-- Start of picture text -->
0<br>P − 1 HP =  D =<br>( E 01 E 2)<br><!-- End of picture text -->

Notice what sits on the diagonal of _D_ : **the energy eigenvalues** _E_ 1 **and** _E_ 2 **!** 

- **If you know the eigenvalues (** _E_ 1 _, E_ 2 **), you already know the diagonal matrix** _D_ **!** 

- The characteristic equation det( _H − λI_ ) = 0 (or the Trace/Determinant trick) is simply the direct mathematical formula to find those diagonal values **without having to explicitly write out the full matrix** _P_ . 

## **2. Why is it called “EXACT”?** 

In the problem, we were given _H_ = _H_ 0 + _H_<sup>_′_</sup> where _H_<sup>_′_</sup> was a small perturbation ( _δ ≪_ 1). 

- **Perturbative approach:** Approximates the energy in powers of _δ_ : _E_ = _E_<sup>(0)</sup> + _δE_<sup>(1)</sup> + _δ_<sup>2</sup> _E_<sup>(2)</sup> + _. . ._ 

This is only an _approximation_ that holds when _δ_ is very small. 

- _δ_ 

- • **Exact Diagonalization approach:** Solves the full matrix _H_ = _δ_ 1 + _δ_ 

- (1 + _δ_ ) 

- directly without making any “small _δ_ ” approximations. The eigenvalues _E_ 1 = 1+2 _δ_ and _E_ 2 = 1 are **100% exact for ANY value of** _δ_ (whether _δ_ = 0 _._ 001 or _δ_ = 100). 

Notes 

2 

## **3. Why is it called a “SHORTCUT”?** 

In GATE exam problems, when students see _δ ≪_ 1 and a degenerate _H_ 0, they are trained to follow the formal **Degenerate Perturbation Theory** recipe: 

1. Identify degenerate states. 

2. Set up the sub-space perturbation matrix _Wij_ = _⟨ψi_<sup>(0)</sup><sup>_|H′|ψ_</sup> _j_<sup>(0)</sup><sup>_⟩_.</sup> 3. Solve det( _W − E_<sup>(1)</sup> _I_ ) = 0 to find _E_<sup>(1)</sup> . 

4. Add _E_<sup>(1)</sup> back to _E_<sup>(0)</sup> . 

The **“shortcut”** is realizing that you don’t need to do perturbation theory at all! Because _H_ is a simple 2 _×_ 2 matrix, you can skip the perturbation machinery entirely and solve for the diagonal values of _H_ directly in 10 seconds. 

## **4. What Explicit Diagonalization looks like if we write out** _P_ 

To see the actual “diagonalization” explicitly: 



<!-- Start of picture text -->
δ<br>1. Normalized Eigenvectors of H = :<br>δ 1 +  δ<br>(1 +  δ )<br>|ψ 1 ⟩ = 1 and |ψ 2 ⟩ = 1<br>√ 2 (11) √ 2 ( − 11)<br><!-- End of picture text -->

2. **Construct the Transformation Matrix** _P_ **(columns are eigenvectors):** 



<!-- Start of picture text -->
P = 1 1<br>√ 2 (11 − 1)<br><!-- End of picture text -->

3. **Perform the Diagonalization Transformation** _P_<sup>_†_</sup> _HP_ **:** 



<!-- Start of picture text -->
1 δ 1 0<br>P † HP = 1 =<br>2 1 − 1 δ 1 +  δ 1 − 1 0 1<br>(1 ) (1 +  δ ) (1 ) (1 + 2 δ )<br><!-- End of picture text -->

There is the diagonal matrix! 

Because we only needed the numbers on that diagonal (1 + 2 _δ_ and 1), calculating the eigenvalues directly gave us those exact diagonal elements without wasting time carrying out the matrix multiplication above! 

