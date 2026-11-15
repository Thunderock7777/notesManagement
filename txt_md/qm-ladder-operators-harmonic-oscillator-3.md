<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-ladder-operators-harmonic-oscillator-3.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answer** 

**Option (a): Only** _βx_<sup>4</sup> 

## **Detailed Step-by-Step Solution** 

**1. First-Order Perturbation Theory Formula** In time-independent perturbation theory, the first-order correction to the energy level _En_<sup>(0)</sup> of an unperturbed state _|n⟩_ is given by the expectation value of the perturbation Hamiltonian _H_<sup>_′_</sup> : 



<!-- Start of picture text -->
En (1) =  ⟨n|H ′ |n⟩<br><!-- End of picture text -->

Substituting the given perturbation _H_<sup>_′_</sup> = _αx_<sup>3</sup> + _βx_<sup>4</sup> + _γx_ : 



<!-- Start of picture text -->
En (1) =  α⟨n|x 3 |n⟩ +  β⟨n|x 4 |n⟩ +  γ⟨n|x|n⟩<br><!-- End of picture text -->

**2. Parity Argument (Symmetry Rule)** The 1D quantum harmonic oscillator potential _V_ ( _x_ ) =<sup><u>1</u></sup> 2<sup>_mω_2</sup><sup>_x_2issymmetricunderspatialreflection(</sup><sup>_x →−x_).Consequently:</sup> 

   - Each stationary state eigenfunction _ψn_ ( _x_ ) has **definite parity** : 

      - Even _n_ : _ψn_ ( _−x_ ) = + _ψn_ ( _x_ ) 

      - Odd _n_ : _ψn_ ( _−x_ ) = _−ψn_ ( _x_ ) 

   - In either case, the probability density _|ψn_ ( _x_ ) _|_<sup>2</sup> = _ψn_<sup>_∗_(</sup><sup>_x_)</sup><sup>_ψn_(</sup><sup>_x_) is</sup><sup>**strictlyanEVEN**</sup> **function** under _x →−x_ . 

Evaluating the expectation value of any power _x_<sup>_k_</sup> : 



<!-- Start of picture text -->
⟨n|x k |n⟩ = |ψn ( x ) | 2 · x k dx<br>� −∞∞ � EVEN �� � Parity depends���� on k<br><!-- End of picture text -->

1. **For Odd Powers (** _k_ = 1 _,_ 3 _,_ 5 _, . . ._ **):** 

   - _x_<sup>_k_</sup> is an **ODD function** . 

   - Integrand = EVEN _×_ ODD = ODD. 

Notes 

2 

   - The integral of an odd function over the symmetric interval ( _−∞, ∞_ ) is **identically zero** : 

      - _⟨_ **n** _|_ **x** _|_ **n** _⟩_ = **0** and _⟨_ **n** _|_ **x**<sup>**3**</sup> _|_ **n** _⟩_ = **0** 

2. **For Even Powers (** _k_ = 2 _,_ 4 _,_ 6 _, . . ._ **):** 

   - _x_<sup>_k_</sup> is an **EVEN function** . 

   - Integrand = EVEN _×_ EVEN = EVEN. 

   - The integral over ( _−∞, ∞_ ) is non-zero: 



<!-- Start of picture text -->
⟨ n | x 4 | n ⟩̸  =  0<br><!-- End of picture text -->



<!-- Start of picture text -->
3. Explicit Calculation of ⟨n|x 4 |n⟩ Using ladder operators x  = � 2 mωh ¯ ( a  +  a† ):<br><!-- End of picture text -->



<!-- Start of picture text -->
h ¯<br>⟨n|x 4 |n⟩ = 2 mω 4 (6 n 2 + 6 n  + 3) ̸  = 0<br>� �2 3<br><!-- End of picture text -->

Therefore, the first-order energy shift simplifies to: 



<!-- Start of picture text -->
E ( n 1 ) =  β⟨ n | x 4 | n ⟩ = 3 β h ¯ 2<br>4m 2 ω 2 ( 2n2  +  2n  +  1 )<br><!-- End of picture text -->

Only the _βx_<sup>4</sup> term produces a non-vanishing contribution to the first-order energy shift. 

## **Evaluation of Options** 

- **Option (a): Only** _βx_<sup>4</sup> _→_ **CORRECT!** 

- **Option (b):** _αx_<sup>3</sup> **and** _γx →_ Incorrect (their first-order expectation values vanish identically). 

- **Option (c): All terms** _→_ Incorrect. 

- **Option (d): None of the terms** _→_ Incorrect. 

## **Key Takeaways & Summary for GATE Physics** 

|Power of<br>Perturbation (_x_<sup>_k_</sup>)|Parity of _x_<sup>_k_</sup>|1st-Order Energy Shift<br>_E_<sup>(1)</sup><br>_n_|2nd-Order Energy<br>Shift _E_<sup>(2)</sup><br>_n_|
|---|---|---|---|
|**Odd Powers**|**Odd**|**Zero (**0**)**|**Non-zero**|
|**(**_x, x_<sup>3</sup>_, x_<sup>5</sup>**)**|||**(Non-vanishing)**|
|**Even Powers**<br>**(**_x_<sup>2</sup>_, x_<sup>4</sup>_, x_<sup>6</sup>**)**|**Even**|**Non-zero**|**Non-zero**|



Notes 

3 

**What happens to the odd terms (** _αx_<sup>3</sup> **and** _γx_ **)?** While odd power perturbations give zero contribution at first order, they do contribute at **second order** in perturbation theory: 



<!-- Start of picture text -->
|⟨m|H ′ |n⟩| 2<br>E (2) =<br>n �<br>m̸ = n En (0) − E m (0)<br><!-- End of picture text -->

because matrix elements like _⟨n ±_ 1 _|x|n⟩_ and _⟨n ±_ 1 _, n ±_ 3 _|x_<sup>3</sup> _|n⟩_ between states of _opposite_ parity are non-zero. 

**Follow-up suggestion:** Would you like to practice calculating the **second-order energy shift** _En_<sup>(2)</sup> for the linear perturbation _H_<sup>_′_</sup> = _γx_ (stark effect on oscillator) or solve a problem on **first-order shifts in anharmonic oscillators** next? 

