<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-perturbation-theory-energy-correction.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answer** 

**Option (b): E**<sup>(</sup> **1**<sup>**0**)</sup> +<sup>**<u>V</u>**</sup> **2**<sup>**<u>0</u>**</sup> 

## **Detailed Step-by-Step Solution** 

## **Method 1: The Symmetry Shortcut (10-Second Method)** 

1. **First-Order Energy Correction Formula:** In first-order perturbation theory, the energy correction to state _n_ is: 



<!-- Start of picture text -->
En (1) =  ⟨ψn (0) |H ′|ψ n (0) ⟩ = |ψn (0)( x ) | 2 H ′ ( x )  dx<br>∫ −∞∞<br><!-- End of picture text -->

2. **Exploit Probability Density Symmetry:** The perturbation is a constant step potential _V_ 0 applied over half the box (0 _≤ x ≤ L_ /2): 



<!-- Start of picture text -->
V 0 for 0  ≤ x ≤ L /2<br>H ′ ( x ) =<br>{0 for L /2  < x ≤ L<br><!-- End of picture text -->

For any stationary state _ψn_ ( _x_ ) in an infinite potential box, the probability density _|ψn_ ( _x_ ) _|_<sup>2</sup> is **symmetric about the center of the box (** _x_ = _L_ /2 **)** . 

3. **Integrate Half the Box:** Because of this reflection symmetry, the probability of finding the particle in the left half of the box (0 _≤ x ≤ L_ /2) is exactly 1/2 for **all** quantum states _n_ : 



<!-- Start of picture text -->
|ψn (0)( x ) | 2 dx  = 1<br>∫0 L /2 2<br><!-- End of picture text -->

4. **Calculate** _E_ 1<sup>(1)</sup><sup>**:**</sup> 



<!-- Start of picture text -->
E 1 (1) =  V 0 |ψ 1 (0)( x ) | 2 dx  =  V 0 = V 0<br>∫0 L /2 ( 21 ) 2<br><!-- End of picture text -->

Therefore, the ground state energy including the first-order correction is: 



<!-- Start of picture text -->
E1 =  E ( 1 0 ) +  E ( 1 1 ) =  E ( 1 0 ) + V 2 0<br><!-- End of picture text -->

Notes 

2 

## **Method 2: Direct Integration (Full Proof)** 

## 1. **Ground State Wavefunction:** 



<!-- Start of picture text -->
2<br>ψ 1 (0)( x ) =<br>√ L sin ( πxL )<br><!-- End of picture text -->

2. **Evaluate the Expectation Value:** 



<!-- Start of picture text -->
2<br>E 1 (1) = V 0  dx  = 2 V 0 dx<br>∫0 L /2 L sin ( πxL L ∫0 L /2 sin 2 ( πx L )<br>( √ ) )2<br><!-- End of picture text -->

3. **Use Trigonometric Identity** sin<sup>2</sup> _θ_ =<sup>1</sup><sup>_−_cos</sup> 2<sup><u>(2</u></sup><sup>_θ_</sup><sup><u>)</u></sup> **:** 



<!-- Start of picture text -->
1  − cos<br>( 2 Lπx )<br>E 1 (1) = 2 L V 0 ∫0 L /2 2 dx  = V L 0 [ x − 2 L π sin ( 2 Lπx )] L 0 /2<br><!-- End of picture text -->

## 4. **Substitute Limits:** 



<!-- Start of picture text -->
• At x  =  L /2: sin 2 π ( LL /2) = sin( π ) = 0<br>( )<br>• At x  = 0: sin(0) = 0<br><!-- End of picture text -->



<!-- Start of picture text -->
E 1 (1) = V L 0 2 − 0 = V 2 0<br>( L )<br>Thus, total energy E 1 =  E 1 (0) + V 2 0 .<br><!-- End of picture text -->

## **Evaluation of Options** 

- **Option (a):** _E_ 1<sup>(0)</sup> + _V_ 0 _→_ **Incorrect** (This would be true if _V_ 0 was applied across the _entire_ box). 

- • **Option (b): E**<sup>(</sup> **1**<sup>**0**)</sup> +<sup>**<u>V</u>**</sup> **2**<sup>**<u>0</u>**</sup><sup>_→_</sup><sup>**CORRECT!**</sup> • **Option (c):** _E_ 1<sup>(0)</sup> +<sup>_<u>V</u>_</sup> 4<sup><u>0</u></sup><sup>_→_</sup><sup>**Incorrect**</sup> • **Option (d):** _E_ 1<sup>(0)</sup> _→_ **Incorrect** 

## **Key Concepts & Formulae to Remember for GATE** 

**1. High-Yield Step & Delta Perturbations in 1D Box (** 0 _≤ x ≤ L_ **)** 

|Perturbation Type|Expression _H_<sup>_′_</sup>(_x_)|First-Order Energy<br>Correction _E_<sup>(1)</sup><br>_n_|
|---|---|---|
|**Half-Box Step Potential**<br>**Full-Box Linear Potential**|_V_0 for 0_≤x ≤L_/2<br>_βx_ for 0_≤x ≤L_|_V_0<br>2 <sup>(for all</sup> <sup>_n_)</sup><br>_βL_<br>2 <sup>(for all</sup> <sup>_n_)</sup>|



Notes 

3 

|Perturbation Type|Expression _H_<sup>_′_</sup>(_x_)|First-Order Energy<br>Correction _E_<sup>(1)</sup><br>_n_|
|---|---|---|
|**Center Delta Function**|_V_0_δ_<br>(<br>_x −_<sup>_L_</sup><br>2<br>)|~~{~~<br>2_V_0<br>_L_<br>for odd _n_<br>0<br>for even _n_|
|**Full-Box Constant**<br>**Potential**|_V_0 for 0_≤x ≤L_|_V_0 (for all _n_)|



**Follow-up suggestion:** Would you like to practice a problem where the step potential covers a fraction other than half the box (e.g., 0 _≤ x ≤ L_ /4), or solve a **second-order perturbation theory** question next? 

