<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-parity-operator-algebraic-properties-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answer** 

**Option (c): P**<sup>**2**</sup> = _−_ **I** _(This identity is NOT valid)_ 

**Detailed Step-by-Step Proof for Each Option** 

The **Parity Operator** _P_<sup>ˆ</sup> (also written as Π<sup>ˆ</sup> ) performs a spatial reflection about the origin: 

_Pψ_ ˆ ( _x_ ) = _ψ_ ( _−x_ ) 

**1. Proof of Option (b): P**<sup>**2**</sup> = **I (VALID)** Apply the parity operator twice to an arbitrary wavefunction _ψ_ ( _x_ ): 



<!-- Start of picture text -->
P ˆ 2 ψ ( x ) = P ˆ ( Pψ ˆ ( x )) = Pψ ˆ ( −x ) =  ψ ( − ( −x )) =  ψ ( x )<br><!-- End of picture text -->

Since applying parity twice returns the original wavefunction unchanged: 



<!-- Start of picture text -->
P 2 =  I<br><!-- End of picture text -->

Since _P_<sup>2</sup> = _I_ , the option **(c)** _P_<sup>2</sup> = _−I_ **is strictly INCORRECT/NOT VALID** . 

**2. Proof of Option (a): P**<sup>_†_</sup> = **P (VALID)** To check Hermiticity, evaluate the inner product: 



<!-- Start of picture text -->
⟨ϕ|Pψ⟩ = ϕ ∗ ( x ) ψ ( −x )  dx<br>∫ −∞∞<br><!-- End of picture text -->

Substitute _y_ = _−x_ = _⇒ dx_ = _−dy_ : 



<!-- Start of picture text -->
⟨ϕ|Pψ⟩ = ϕ ∗ ( −y ) ψ ( y )( −dy ) = ϕ ∗ ( −y ) ψ ( y )  dy<br>∫ ∞−∞ ∫ −∞∞<br><!-- End of picture text -->

Notes 

2 

Rewriting using the parity definition _ϕ_<sup>_∗_</sup> ( _−y_ ) = ( _Pϕ_ ( _y_ ))<sup>_∗_</sup> : 



<!-- Start of picture text -->
⟨ϕ|Pψ⟩ = [ Pϕ ( y )] ∗ ψ ( y )  dy =  ⟨Pϕ|ψ⟩<br>∫ −∞∞<br><!-- End of picture text -->

Therefore, the parity operator equals its adjoint: 

**P**<sup>_†_</sup> = **P** (Hermitian) 

_(Note: Since P_<sup>_†_</sup> = _P and P_<sup>2</sup> = _I_ = _⇒ P_<sup>_−_1</sup> = _P , parity is both_ **_Hermitian_** _and_ **_Unitary_** _)._ 

**3. Proof of Option (d): PxP** = _−_ **x (VALID)** Let the operator sequence _PxP_ act on a wavefunction _ψ_ ( _x_ ): 



<!-- Start of picture text -->
( PxP ) ψ ( x ) =  P [ x ( Pψ ( x ))] =  P [ xψ ( −x )]<br><!-- End of picture text -->

Applying parity _P_ reflects every occurrence of _x →−x_ : 

_P_ [ _xψ_ ( _−x_ )] = ( _−x_ ) _ψ_ ( _−_ ( _−x_ )) = _−xψ_ ( _x_ ) 

Cancelling _ψ_ ( _x_ ) from both sides: 

**PxP** = _−_ **x** 

_(Equivalently, using P_<sup>_−_1</sup> = _P : PxP_<sup>_−_1</sup> = _−x, which shows x is an odd operator under parity)._ 

## **Evaluation Summary** 

- **Option (a):** _P_<sup>_†_</sup> = _P →_ **Valid** (Parity is Hermitian) 

- **Option (b):** _P_<sup>2</sup> = _I →_ **Valid** (Involution property) 

- **Option (c): P**<sup>**2**</sup> = _−_ **I** _→_ **NOT VALID! (Correct answer to the query)** 

- **Option (d):** _PxP_ = _−x →_ **Valid** (Position transforms as an odd vector) 

## **Key Concepts & Summary for GATE Physics** 

**1. Fundamental Properties of the Parity Operator** _P_<sup>ˆ</sup> 

- **Eigenvalues:** Since _P_<sup>2</sup> = _I_ , the eigenvalues _λ_ satisfy _λ_<sup>2</sup> = 1 = _⇒ λ_ = _±_ **1** . **–** _λ_ = +1 = _⇒_ **Even Parity** state ( _ψ_ ( _−x_ ) = + _ψ_ ( _x_ )) **–** _λ_ = _−_ 1 = _⇒_ **Odd Parity** state ( _ψ_ ( _−x_ ) = _−ψ_ ( _x_ )) 

- **Hermiticity & Unitarity: P**<sup>_†_</sup> = **P** = **P**<sup>_−_</sup><sup>**1**</sup> 

Notes 

3 

**2. Action of Parity on Quantum Observables** 

   - **Position:** _PxP_<sup>_†_</sup> = _−x_ (Odd) 

   - **Momentum:** _PpP_<sup>_†_</sup> = _−p_ (Odd) 

   - **Orbital Angular Momentum:** _P_ **L** _P_<sup>_†_</sup> = _P_ ( **r** _×_ **p** ) _P_<sup>_†_</sup> = ( _−_ **r** ) _×_ ( _−_ **p** ) = + **L** ( **Even / Axial Vector** ) 

   - **Spin Angular Momentum:** _P_ **S** _P_<sup>_†_</sup> = + **S** ( **Even** ) 

**Follow-up suggestion:** Would you like to explore **selection rules for dipole transitions under parity conservation** or solve a question on **parity of spherical harmonics** _Yl_<sup>_m_(</sup><sup>_θ, ϕ_)next?</sup> 

