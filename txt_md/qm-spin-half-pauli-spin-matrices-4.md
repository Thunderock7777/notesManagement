<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-spin-half-pauli-spin-matrices-4.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Here is the step-by-step mathematical proof explaining **why and how** finding _E_<sup>2</sup> allows us to determine the eigenvalues _E_ = _±λB_ . 

## **1. The General Operator Eigenvalue Theorem** 

Suppose _|ψ⟩_ is an eigenstate (eigenvector) of the operator _A_<sup>ˆ</sup> with eigenvalue _E_ . By definition: 



<!-- Start of picture text -->
A ˆ |ψ⟩ =  E|ψ⟩<br><!-- End of picture text -->

Now, apply the operator _A_<sup>ˆ</sup> a second time to both sides: 



<!-- Start of picture text -->
A ˆ 2 |ψ⟩ = A ˆ ( A ˆ |ψ⟩ ) = A ˆ  ( E|ψ⟩ )<br><!-- End of picture text -->

Since _E_ is just a scalar number (constant), we can pull it out in front: 



<!-- Start of picture text -->
A ˆ ( E|ψ⟩ ) =  E ( A ˆ |ψ⟩ )<br><!-- End of picture text -->

Now substitute _A_<sup>ˆ</sup> _|ψ⟩_ = _E|ψ⟩_ once more: 



<!-- Start of picture text -->
E  ( E|ψ⟩ ) =  E 2 |ψ⟩<br><!-- End of picture text -->

**Key Rule:** If an operator _A_<sup>ˆ</sup> has an eigenvalue _E_ , then the squared operator _A_ ˆ<sup>2</sup> **MUST have the eigenvalue** _E_<sup>2</sup> for the exact same eigenvector _|ψ⟩_ . 

## **2. Applying This Rule to Our Specific Operator** _A_<sup>ˆ2</sup> 

From the Pauli matrix vector identity, we already derived that: 



<!-- Start of picture text -->
A ˆ 2 =  λ 2 B 2 I<br><!-- End of picture text -->



<!-- Start of picture text -->
0<br>(where I = is the 2  ×  2 Identity Matrix).<br>0 1<br>(1 )<br><!-- End of picture text -->

Notes 

2 

Now, let’s act with _A_<sup>ˆ2</sup> on an eigenvector _|ψ⟩_ using **both** expressions: 

1. **Using the general property from Section 1:** 



<!-- Start of picture text -->
A ˆ 2 |ψ⟩ =  E 2 |ψ⟩<br><!-- End of picture text -->

2. **Using the explicit form of** _A_<sup>ˆ2</sup> = _λ_<sup>2</sup> _B_<sup>2</sup> _I_ **:** 



<!-- Start of picture text -->
A ˆ 2 |ψ⟩ = ( λ 2 B 2 I ) |ψ⟩ =  λ 2 B 2 ( I|ψ⟩ ) =  λ 2 B 2 |ψ⟩<br><!-- End of picture text -->

## **3. Equating the Two Results** 

Equating the right-hand sides of both expressions: 



<!-- Start of picture text -->
E 2 |ψ⟩ =  λ 2 B 2 |ψ⟩<br><!-- End of picture text -->

Since an eigenvector _|ψ⟩_ is non-zero by definition, we can cancel _|ψ⟩_ from both sides: 



<!-- Start of picture text -->
E 2 =  λ 2 B 2<br><!-- End of picture text -->

Taking the square root gives two possible algebraic solutions: 



<!-- Start of picture text -->
E  =  ± √ λ 2 B 2 =  ±λ B<br><!-- End of picture text -->

**4. Why Are BOTH** + _bmsλB_ **and** _−_ 

_bmsλB_ **Present?** 

Since _A_<sup>ˆ</sup> = _λ_ ( _σ ·_ **B** ) is a 2 _×_ 2 **matrix** for a spin-1/2 particle, it **must have exactly 2 eigenvalues** : 

1. The trace of any Pauli vector is zero: Tr( _A_<sup>ˆ</sup> ) = _E_ 1 + _E_ 2 = 0. 

2. For the sum of the two eigenvalues to equal 0 while both satisfy _E_<sup>2</sup> = _λ_<sup>2</sup> _B_<sup>2</sup> , one eigenvalue **must be positive** and the other **must be negative** : 



<!-- Start of picture text -->
E1 = + λ B and E2 =  −λ B<br><!-- End of picture text -->

**Would you like to try another matrix problem where taking operator powers (like** _A_<sup>ˆ3</sup> **or** _eA_<sup>ˆ</sup> **) helps solve the question quickly?** 

