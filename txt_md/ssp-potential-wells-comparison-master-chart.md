<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-potential-wells-comparison-master-chart.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

The **Kronig-Penney Model** (1931) is the quintessential 1D quantum model used in solid-state physics to prove analytically how a periodic lattice potential forces continuous free-electron energy states to split into **allowed energy bands** and **forbidden energy gaps** . 

## **1. Physical Motivation & Setup** 

In a real 3D crystal, an electron moves through a periodic potential _V_ ( _r_ + _R_ ) = _V_ ( _r_ ) created by positively charged ion cores. Solving the 3D Schrödinger equation for realistic atomic potentials is mathematically cumbersome. Kronig and Penney simplified this by replacing the continuous atomic potential wells with an array of 1D rectangular potential barriers of height _V_ 0 and width _b_ , separated by well regions of width _a_ . 

To make the equation cleaner and solvable in terms of elementary trigonometric functions, we take the **delta-function limit** : The barrier height _V_ 0 _→∞_ and barrier width _b →_ 0 such that the product _V_ 0 _b_ (the area/strength of the barrier) remains finite. This transforms the lattice into a periodic comb of Dirac delta functions separated by spacing _a_ . 

## **2. Breakdown of the Transcendental Equation** 

Applying **Bloch’s Theorem** ( _ψ_ ( _x_ + _a_ ) = _e_<sup>_ika_</sup> _ψ_ ( _x_ )) and matching wavefunctions and their derivatives at the potential boundaries yields the famous **Kronig-Penney dispersion relation** : 



<!-- Start of picture text -->
P  sin( α a )<br>+ cos( α a ) = cos( ka )<br>α a<br><!-- End of picture text -->

## **Meaning of Every Parameter:** 

- _~~<u>√</u>~~_ <u>2</u> _<u>mE</u>_ 

- 1. _α_ = **:** _h_ ¯ 

   - The wave number of the electron in the potential well region ( _V_ = 0). 

   - Since _α_<sup>2</sup> =<sup><u>2</u></sup><sup>_<u>mE</u>_</sup> _h_ ¯<sup>2, the variable</sup><sup>_α_directly encodes the</sup><sup>**electronkineticenergy**</sup> _E_ . 

Notes 

2 

2. _a_ **:** The **lattice constant** (spatial periodicity of the potential comb, _V_ ( _x_ + _a_ ) = _V_ ( _x_ )). 

3. _k_ **:** The **crystal wave vector** (Bloch index) that labels the collective traveling wave state of the electron across the crystal ( _k ∈_ [ _−π_ / _a, π_ / _a_ ] in the 1D first Brillouin zone). 

4. _P_ **(Dimensionless Barrier Strength / Binding Parameter):** 



<!-- Start of picture text -->
mV 0 ba<br>P ≡ lim<br>b→ 0 ,V 0 →∞ h ¯ 2<br><!-- End of picture text -->

- _P_ measures the area of the potential barrier ( _V_ 0 _b_ ). 

- **Physical significance:** A larger _P_ means a stronger barrier, binding the electron more tightly to an individual potential well. A smaller _P_ means electrons can easily tunnel between wells. 

## **3. Origin of Allowed Bands & Forbidden Gaps** 

Let us define the left-hand side function as _F_ ( _αa_ ) _≡_<sup>_P_sin</sup> _αa_<sup><u>(</u></sup><sup>_αa_</sup><sup><u>)</u></sup> + cos( _αa_ ). 

Since the right-hand side is cos( _ka_ ), and the cosine of a real wave vector _k_ is strictly bounded between _−_ 1 and +1: 



<!-- Start of picture text -->
− 1  ≤ P  sin( α a ) + cos( α a )  ≤ + 1<br>α a<br>F( α a) ^<br>| /\<br>+1 +------/--\------+-------------------- Upper Boundary<br>| / \ | /\<br>|----/------\----|------/--\---------- Lower Boundary<br>-1 +---/--------\---+-----/----\---------<br>| / \ | / \<br>+-------------------------------------> α a<br>Allowed |Gap| Allowed<br>Band Band<br><!-- End of picture text -->

1. **Allowed Energy Bands (** _|F_ ( _αa_ ) _| ≤_ 1 **):** 

   - For ranges of _αa_ (and hence energy _E_ ) where _F_ ( _αa_ ) falls between _−_ 1 and +1, _k_ is **real** . 

   - The wavefunctions are unattenuated propagating Bloch traveling waves that can travel across the entire crystal without scattering. 

2. **Forbidden Energy Band Gaps (** _|F_ ( _αa_ ) _| >_ 1 **):** 

   - When _F_ ( _αa_ ) exceeds +1 or drops below _−_ 1, no real wave vector _k_ can satisfy the equation. 

   - _k_ becomes complex ( _k_ = _kr_ + _iκ_ ), causing the wavefunction to decay exponentially ( _ψ ∝ e_<sup>_−κx_</sup> ). No stationary traveling electron states exist in these energy zones. 

Notes 

3 

## **4. Two Extreme Physical Limits** 

**Limit A:** _P →_ 0 **(Free Electron Limit)** When _P →_ 0, the potential barriers disappear ( _V_ 0 _→_ 0), leaving a completely free space: 



<!-- Start of picture text -->
0  ·  sin( αa )<br>+ cos( αa ) = cos( ka ) = ⇒ cos( αa ) = cos( ka )<br>αa<br><!-- End of picture text -->



<!-- Start of picture text -->
√ 2 mE<br>α  =  k = ⇒ =  k = ⇒ E  = h ¯ 2k2<br>h ¯ 2m<br><!-- End of picture text -->

- **Result:** The forbidden band gaps vanish completely, recovering the continuous parabolic energy spectrum of a free particle. 

**Limit B:** _P →∞_ **(Particle in a Box / Isolated Atom Limit)** When _P →∞_ , the potential barriers become infinitely impenetrable. 

- For the term _P_<sup>sin</sup> _αa_<sup><u>(</u></sup><sup>_αa_</sup><sup><u>)</u></sup> to remain finite, sin( _αa_ ) must equal zero: 



<!-- Start of picture text -->
sin( αa ) = 0 = ⇒ αa  =  nπ ( n  = 1 ,  2 ,  3 , . . .  )<br>√ 2 mEn<br>α  = nπ = ⇒ = nπ = ⇒ En = n2 π 2h ¯ 2<br>a h ¯ a 2ma 2<br><!-- End of picture text -->

   - **Result:** The allowed energy bands collapse into **infinitely sharp, discrete energy levels** —the exact energy spectrum of an electron trapped in a 1D rigid potential box of length _a_ . 

**5. Key Properties to Remember for GATE Exam** 

   1. **Band Gap Trend with Energy (Crucial Trap!):** 

      - As energy _E_ increases (larger _αa_ ), the term<sup>_P_sin</sup> _αa_<sup><u>(</u></sup><sup>_αa_</sup><sup><u>)</u></sup> decays toward zero because _αa_ appears in the denominator. 

      - Consequently, at higher energies, **allowed energy bands become wider** , and **forbidden band gaps become narrower** . 

   2. **Zone Boundary Discontinuities:** 

      - Band gaps occur precisely when _F_ ( _αa_ ) = _±_ 1, which corresponds to: 

cos( _ka_ ) = _±_ 1 = _⇒ ka_ = _±nπ_ = _⇒_ **k** = _±_<sup>**n**</sup><sup>_π_</sup> 

**a** 

- These correspond to the **Brillouin Zone boundaries** , where electron waves undergo destructive Bragg reflection, forming standing waves rather than traveling waves. 

Would you like to try a numerical GATE problem calculating the **lowest allowed energy band** or **band gap width** using this Kronig-Penney equation? 

