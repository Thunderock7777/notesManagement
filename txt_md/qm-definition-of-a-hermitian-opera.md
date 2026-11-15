<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-definition-of-a-hermitian-opera.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answer** 

**Option (b): dxd**<sup>**22**</sup> 

## **Detailed Step-by-Step Solution** 

**1. Definition of a Hermitian Operator** An operator _A_<sup>ˆ</sup> acting on square-integrable wavefunctions _ψ_ ( _x_ ) and _ϕ_ ( _x_ ) (which vanish at boundary infinity, _x →±∞_ ) is **Hermitian** if it equals its Hermitian conjugate (adjoint): 

_A_ ˆ<sup>_†_</sup> = _A_ ˆ = _⇒⟨ϕ|_ ˆ _Aψ⟩_ = _⟨Aϕ_ ˆ _|ψ⟩_ 



<!-- Start of picture text -->
ϕ ∗ ( x ) Aψ ˆ ( x ) dx  = Aϕ ˆ ( x ) ψ ( x )  dx<br>� −∞∞ � � � −∞∞ � � ∗<br><!-- End of picture text -->

**2. Adjoint of the** _n_ **-th Spatial Derivative** _dxd_<sup>_nn_</sup> Let’s test the derivative operator _D_ ˆ = _<u>d</u> dx_<sup>usingintegrationbyparts:</sup> 



<!-- Start of picture text -->
− dϕ ∗<br>⟨ϕ| d ϕ ∗ ( x ) dψ [ ϕ ∗ ( x ) ψ ( x )] ∞ −∞<br>dx ψ⟩ = � −∞∞ dx dx  = � �� � � −∞∞ dx ψ ( x )  dx<br>= 0 (Boundary condition)<br>⟨ϕ| d − dϕ ψ ( x )  dx  =  ⟨− d<br>dx ψ⟩ = � −∞∞ � dx � ∗ dx ϕ|ψ⟩<br><!-- End of picture text -->

Thus, the adjoint of a single spatial derivative is **anti-Hermitian** : 



<!-- Start of picture text -->
=  − d<br>dx dx<br>� d � †<br><!-- End of picture text -->

Extending this to the _n_ -th derivative by applying integration by parts _n_ times: 



<!-- Start of picture text -->
= ( − 1 ) n dn<br>dx n dx n<br>� dn � †<br><!-- End of picture text -->

Notes 

2 

## **3. Test Each Option** 



<!-- Start of picture text -->
• Option (a): A ˆ  = dxd<br>A ˆ † = ( − 1) 1 d (Anti-Hermitian)<br>dx =  − dx d =  −A ˆ<br><!-- End of picture text -->



<!-- Start of picture text -->
• Option (b): B ˆ = dxd 22<br>B ˆ † = ( − 1) 2 d 2 (HERMITIAN!)<br>dx 2 = + dx d 22 = + ˆ B<br><!-- End of picture text -->

• **Option (c):** _C_<sup>ˆ</sup> = _idxd_<sup>22=</sup><sup>_−i_</sup> _dx_<sup>_<u>d</u>_22Takingtheadjoint(complexconjugateofconstant</sup> + adjoint of operator): 



<!-- Start of picture text -->
C ˆ † = ( −i ) ∗ = (+ i ) =  − −i d 2 =  −C ˆ (Anti-Hermitian)<br>dx 2 dx 2 dx 2<br>� d 2 � † � d 2 � � �<br><!-- End of picture text -->



<!-- Start of picture text -->
• Option (d): D ˆ = dxd 33<br><!-- End of picture text -->



<!-- Start of picture text -->
D ˆ † = ( − 1) 3 d 3 (Anti-Hermitian)<br>dx 3 =  − dx d 33 =  −D ˆ<br><!-- End of picture text -->

## **Evaluation of Options** 

- **Option (a):** _dxd_<sup>_→_</sup><sup>**Anti-Hermitian**</sup> 

- • **Option (b): dxd**<sup>**22**</sup><sup>_→_</sup><sup>**CORRECT!(Hermitian)**</sup> • **Option (c):** _idxd_<sup>22</sup><sup>_→_</sup><sup>**Anti-Hermitian**</sup> • **Option (d):** _dxd_<sup>33</sup><sup>_→_</sup><sup>**Anti-Hermitian**</sup> 

**Key Concepts & Formulae to Remember for GATE 1. General Rule for Differential Operators** _c dx_<sup>_<u>dnn</u>_</sup> For any complex scalar constant _c_ : 



<!-- Start of picture text -->
c dn =  c ∗ ( − 1) n dn<br>dx n dx n<br>� � †<br><!-- End of picture text -->

An operator is Hermitian if _c_<sup>_∗_</sup> ( _−_ 1)<sup>_n_</sup> = _c_ : 

- **Odd derivatives (** _n_ = 1 _,_ 3 _,_ 5 _, . . ._ **):** Require an **imaginary factor** _i_ to be Hermitian (e.g., _p_ ˆ _x_ = _−ih_ ¯ _dx_<sup>_<u>d</u>_or</sup><sup>_i_</sup> _dx_<sup>_<u>d</u>_33).</sup> 

- **Even derivatives (** _n_ = 2 _,_ 4 _,_ 6 _, . . ._ **):** Require a **real factor** to be Hermitian (e.g., _T_ ˆ = _−_<sup>_<u>h</u>_¯2</sup> _<u>d</u>_<sup>2</sup> 2 _m dx_<sup>2).</sup> 

Notes 

3 

## **2. High-Yield Examples in Quantum Mechanics** 

|Operator|Formula|Hermitian or<br>Anti-Hermitian?|Physical Meaning|
|---|---|---|---|
|**Momentum** ˆ_px_|_−i_¯_h_ <sup>_d_</sup><br>_dx_|**Hermitian**|Real physical<br>observable|
|**Kinetic Energy** <sup>ˆ</sup>_T_|_−_<sup>¯</sup><sup>_h_2</sup><br>2_m_<br>_d_<sup>2</sup><br>_dx_<sup>2</sup>|**Hermitian**|Real physical<br>observable|
|**Spatial**<br>**Derivative**<br>_d_<br>_dx_|_d_<br>_dx_<br>|**Anti-Hermitian**|—|
|**Third Derivative**<br>_i_ <sup>_d_3</sup><br>_dx_<sup>3</sup>|_i_ <sup>_d_3</sup><br>_dx_<sup>3</sup>|**Hermitian**|—|



**Follow-up suggestion:** Would you like to practice a question on **commutators of Hermitian operators** (e.g., [ˆ _x,_ ˆ _px_ ]) or checking the **parity and Hermiticity** of composite operators next? 

