<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-perturbation-theory-energy-correction-5.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answer** 

**Option (a):** _⟨_ **200** _|_ **z** _|_ **210** _⟩_ 

## **Detailed Step-by-Step Solution** 

**1. Matrix Element Operator in Spherical Coordinates** The perturbation operator for an electric field _E_ applied along the _z_ -axis is _H_<sup>_′_</sup> = _eEz_ . In spherical polar coordinates, _z_ = _r_ cos _θ_ , which is proportional to the spherical harmonic _Y_ 1 _,_ 0( _θ, ϕ_ ). 

The general matrix element between two hydrogenic states _|nlm⟩_ and _|n_<sup>_′_</sup> _l_<sup>_′_</sup> _m_<sup>_′_</sup> _⟩_ is given by: 



<!-- Start of picture text -->
⟨nlm|z|n ′ l ′ m ′ ⟩ = Rnl ( r )  r Rn′l′ ( r )  r 2 dr × Ylm ∗ ( θ, ϕ ) cos  θ Yl′m′ ( θ, ϕ ) sin  θ dθ dϕ<br>�0 ∞ �0 π �0 2 π<br>� �� � � �� �<br>Radial Integral Angular Integral<br><!-- End of picture text -->

**2. Selection Rules for the** _z_ **Matrix Element** To determine which matrix elements are non-zero, we apply two strict quantum mechanical selection rules: 

   1. **Parity Selection Rule (** ∆ _l_ = _±_ 1 **):** 

      - The operator _z_ is **odd under spatial parity** ( _z →−z_ ). 

      - For the integrand to be an **even function** (so the integral does not vanish over symmetric space), the initial and final states must have **opposite parities** . 

      - • Since parity is given by Π = ( _−_ 1)<sup>_l_</sup> , we require: 

**∆l** = **l**<sup>_′_</sup> _−_ **l** = _±_ **1** 

   - Diagonal matrix elements (∆ _l_ = 0) vanish identically because Even _×_ Odd _×_ Even = Odd. 

2. **Azimuthal Selection Rule (** ∆ _m_ = 0 **):** 

   - The operator _z_ = _r_ cos _θ_ has **no** _ϕ_ **-dependence** . 

   - The integral over _ϕ_ takes the form: 



<!-- Start of picture text -->
e −imϕ · e im′ϕ dϕ  = e i ( m′−m ) ϕ dϕ  = 2 πδm,m′<br>�0 2 π �0 2 π<br><!-- End of picture text -->

Notes 

2 

- Therefore, the matrix element vanishes unless: 

**∆m** = **m**<sup>_′_</sup> _−_ **m** = **0** 

## **3. Evaluation of Options** 

- **Option (a):** _⟨_ 200 _|z|_ 210 _⟩_ 

   - States: _|_ 2 _s⟩_ = _|_ 2 _,_ 0 _,_ 0 _⟩_ and _|_ 2 _pz⟩_ = _|_ 2 _,_ 1 _,_ 0 _⟩_ . 

   - Check ∆ _l_ : _l_<sup>_′_</sup> _− l_ = 1 _−_ 0 = +1 = _⇒_ **Satisfied (** ∆ _l_ = _±_ 1 **)** . 

   - Check ∆ _m_ : _m_<sup>_′_</sup> _− m_ = 0 _−_ 0 = 0 = _⇒_ **Satisfied (** ∆ _m_ = 0 **)** . 

   - **Result: NON-ZERO!** (Explicit calculation yields _⟨_ 200 _|z|_ 210 _⟩_ = _−_ 3 _a_ 0). 

- **Option (b):** _⟨_ 200 _|z|_ 200 _⟩_ 

   - States: _|_ 2 _s⟩_ and _|_ 2 _s⟩_ . 

   - Check ∆ _l_ : 0 _−_ 0 = 0 = _⇒_ **Violates parity selection rule** (integrand is odd, integral vanishes). 

- **Option (c):** _⟨_ 211 _|z|_ 210 _⟩_ 

   - States: _|_ 2 _,_ 1 _,_ 1 _⟩_ and _|_ 2 _,_ 1 _,_ 0 _⟩_ . 

   - Check ∆ _m_ : 0 _−_ 1 = _−_ 1 _̸_ = 0 = _⇒_ **Violates azimuthal selection rule** ( _ϕ_ -integral vanishes). Also violates ∆ _l_ = _±_ 1. 

- **Option (d):** _⟨_ 211 _|z|_ 211 _⟩_ 

   - States: _|_ 2 _,_ 1 _,_ 1 _⟩_ and _|_ 2 _,_ 1 _,_ 1 _⟩_ . 

   - Check ∆ _l_ : 1 _−_ 1 = 0 _̸_ = _±_ 1 = _⇒_ **Violates parity selection rule** . 

## **Physical Context: The Linear Stark Effect** 

The non-vanishing matrix element _⟨_ 200 _|z|_ 210 _⟩_ = _−_ 3 _a_ 0 is precisely the term responsible for mixing the degenerate _|_ 2 _s⟩_ and _|_ 2 _pz⟩_ states in first-order perturbation theory, leading to the **Linear Stark Effect** in the _n_ = 2 level of hydrogen with first-order energy shifts ∆ _E_<sup>(1)</sup> = _±_ 3 _ea_ 0 _E_ . 

Would you like to practice calculating the **energy level splitting diagram** for the _n_ = 2 state in an electric field, or solve a problem on the **Quadratic Stark Effect** for the _n_ = 1 ground state? 

