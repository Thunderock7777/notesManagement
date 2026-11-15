<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-degenerate-perturbation-theory.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Here is the step-by-step mathematical breakdown of **why and how** the 2 _×_ 2 perturbation matrix _W_ is constructed from the bottom-right block of _H_<sup>_′_</sup> . 

## **1. Identify the Degenerate Subspace Basis States** 

The unperturbed Hamiltonian _H_ 0 is: 



<!-- Start of picture text -->
H 0 = 10 02 00<br>0 0 2<br> <br><!-- End of picture text -->

Its 3 basis eigenstates (written as standard column vectors) are: 



<!-- Start of picture text -->
1<br>| 1 ⟩ = 0 (Energy E 1 (0) = 1)<br>0<br> <br>01<br>| 2 ⟩ = (Energy E 2 (0) = 2)<br>0<br> <br>0<br>| 3 ⟩ = 0 (Energy E 3 (0) = 3)<br>1<br> <br><!-- End of picture text -->

Notice that _|_ 2 _⟩_ **and** _|_ 3 _⟩_ **share the exact same energy (** _E_<sup>(0)</sup> = 2 **)** . Therefore, the degenerate subspace is 2-dimensional, spanned by _{|_ 2 _⟩, |_ 3 _⟩}_ . 

## **2. Definition of the Matrix Elements of** _W_ 

In degenerate perturbation theory, the matrix elements of _W_ are defined by taking inner products using only the degenerate basis states _{|_ 2 _⟩, |_ 3 _⟩}_ : 



<!-- Start of picture text -->
⟨ 2 |H ′ | 3 ⟩<br>W =<br>( ⟨⟨ 32 ||HH ′ ′|| 22 ⟩⟩ ⟨ 3 |H ′ | 3 ⟩ )<br><!-- End of picture text -->

Notes 

2 

## **3. Explicit Matrix Multiplication for Each Element** 



<!-- Start of picture text -->
Given H ′ =  ϵ 01 10 00<br>0 0 1<br> :<br><!-- End of picture text -->

1. **Top-Left Element (** _W_ 11 = _⟨_ 2 _|H_<sup>_′_</sup> _|_ 2 _⟩_ **):** 



<!-- Start of picture text -->
H ′ | 2 ⟩ =  ϵ 01 10 00 01 10<br>0 0 1 0 0<br>    =  ϵ  <br>⟨ 2 |H ′ | 2 ⟩ = (0 1 0)  10<br>0<br> ϵ   =  0<br><!-- End of picture text -->

2. **Top-Right Element (** _W_ 12 = _⟨_ 2 _|H_<sup>_′_</sup> _|_ 3 _⟩_ **):** 



<!-- Start of picture text -->
H ′ | 3 ⟩ =  ϵ 01 10 00 00 00<br>0 0 1 1 1<br>    =  ϵ  <br>⟨ 2 |H ′ | 3 ⟩ = (0 1 0)  00<br>1<br> ϵ   =  0<br><!-- End of picture text -->

3. **Bottom-Left Element (** _W_ 21 = _⟨_ 3 _|H_<sup>_′_</sup> _|_ 2 _⟩_ **):** 



<!-- Start of picture text -->
⟨ 3 |H ′ | 2 ⟩ = (0 0 1)  10<br>0<br> ϵ   =  0<br><!-- End of picture text -->

4. **Bottom-Right Element (** _W_ 22 = _⟨_ 3 _|H_<sup>_′_</sup> _|_ 3 _⟩_ **):** 



<!-- Start of picture text -->
⟨ 3 |H ′ | 3 ⟩ = (0 0 1)  00<br>1<br> ϵ   =  ϵ<br><!-- End of picture text -->

## **4. Summary Shortcut** 

Because the basis is standard, _⟨i|H_<sup>_′_</sup> _|j⟩_ is simply the element _Hij_<sup>_′_at</sup><sup>**row**</sup><sup>_i_</sup><sup>**,column**</sup><sup>_j_of</sup> the 3 _×_ 3 matrix _H_<sup>_′_</sup> : 



<!-- Start of picture text -->
H 11 ′ H 12 ′ H 13 ′ 0 1 0<br>H ′ =  ϵ  H 21 ′ H ′ 22 H ′ 23  1 0 0 <br> H 31 ′ H ′ 32 H ′ 33  =  ϵ 0 0 1 <br><!-- End of picture text -->

Since state 1 corresponds to row/col 1, state 2 to row/col 2, and state 3 to row/col 3: • The degenerate states are 2 and 3. 

Notes 

3 

• Selecting **rows 2 & 3** and **columns 2 & 3** extracts the **bottom-right** 2 _×_ 2 **block** : 



<!-- Start of picture text -->
22 H 23 ′ 0<br>W = =  ϵ<br>( HH 32 ′ ′ H 33 ′ ) (00 1)<br><!-- End of picture text -->

Would you like to try another matrix perturbation problem where the degenerate states are not adjacent (e.g., states 1 and 3)? 

