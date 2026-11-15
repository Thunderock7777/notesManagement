<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-perturbation-theory-energy-correction-4.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**Correct Answer Option (a):** _<u>β</u>_ **2a** 

## **Method 1: The 10-Second Symmetry Shortcut** 

**1. Express** _E_<sup>(1)</sup> **as an Expectation Value** In first-order perturbation theory, the energy correction to state _n_ is the expectation value of the perturbation operator _W_ ( _x_ ) in the unperturbed state _|ψn_<sup>(0)</sup><sup>_⟩_:</sup> 



<!-- Start of picture text -->
E 1 (1) =  ⟨ψ 1 (0) |W ( x ) |ψ 1 (0) ⟩ =  ⟨ψ 1 (0) |βx|ψ 1 (0) ⟩ =  β⟨x⟩ 1<br><!-- End of picture text -->

**2. Exploit Midpoint Symmetry of the 1D Box** For any stationary state _ψn_ ( _x_ ) in an infinite potential box bounded between _x_ = 0 and _x_ = _a_ , the probability density _|ψn_ ( _x_ ) _|_<sup>2</sup> is **perfectly symmetric** about the midpoint _x_ =<sup>_<u>a</u>_</sup> 2<sup>.</sup> 

Therefore, the average position _⟨x⟩_ for **any** state _n_ is simply the geometric midpoint of the box: 



<!-- Start of picture text -->
⟨x⟩n = a<br>2<br><!-- End of picture text -->

**3. Calculate** _E_ 1<sup>(1)</sup> 



<!-- Start of picture text -->
E ( 1 1 ) =  β⟨ x ⟩ 1 =  β = β a<br>� 2a � 2<br><!-- End of picture text -->

_(Note: This result is independent of the quantum number n! The first-order correction for_ **_every_** _state in the box under a linear potential W_ ( _x_ ) = _βx is_<sup>_<u>β</u>_</sup> 2<sup>_a)._</sup> 

## **Method 2: Direct Integration (Full Proof)** 

**1. Unperturbed Ground State Wavefunction** 



<!-- Start of picture text -->
2<br>ψ 1( x ) =<br>� a sin � πxa �<br><!-- End of picture text -->

Notes 

2 

## **2. Evaluate the Integral** 



<!-- Start of picture text -->
E 1 (1) = �0 a |ψ 1( x ) | 2 ( βx )  dx  = 2 a β �0 a x  sin 2 � πx a � dx<br><!-- End of picture text -->

Using the trigonometric identity sin<sup>2</sup> _θ_ =<sup>1</sup><sup>_−_cos</sup> 2<sup><u>(2</u></sup><sup>_θ_</sup><sup><u>)</u></sup> : 



<!-- Start of picture text -->
E 1 (1) = β x 1  − cos dx  = β x dx − x  cos dx<br>a �0 a � � 2 πxa �� a ��0 a �0 a � 2 πxa � �<br>First Integral:<br>x dx  = = a 2<br>�0 a � x 22 � a 0 2<br><!-- End of picture text -->

1. **First Integral:** 

2. **Second Integral (Integration by Parts):** 



<!-- Start of picture text -->
x  cos dx  = x sin(2 πx / a ) − sin(2 πx / a ) dx  = 0  − 0 = 0<br>�0 a � 2 πxa � � 2 π / a � a 0 �0 a 2 π / a<br><!-- End of picture text -->

Substituting back: 



<!-- Start of picture text -->
E 1 (1) = β = β a<br>a 2 − 0 2<br>� a 2 �<br><!-- End of picture text -->

## **Key Concepts & Formulae to Remember for GATE** 

**1. Expectation Values in a 1D Box (** 0 _≤ x ≤ a_ **)** 

|Quantity|Expectation Value Formula|Notes / GATE Insight|
|---|---|---|
|**Position** _⟨x⟩_|_a_<br>2|Same for all _n_ (midpoint<br>symmetry)|
|**Position Squared** _⟨x_<sup>2</sup>_⟩_|_a_<sup>2 �1</sup><br>3 <sup>_−_</sup><br>1<br>2_n_<sup>2</sup>_π_<sup>2</sup><br>�|Increases as _n →∞_towards<br>classical limit <sup>_a_2</sup><br>3|
|**Momentum** _⟨px⟩_|0|Particle moves left and right<br>with equal probability|
|**Momentum Squared** _⟨p_<sup>2</sup><br>_x_<sup>_⟩_</sup>|_n_<sup>2</sup>_π_<sup>2</sup>¯_h_<sup>2</sup><br>_a_<sup>2</sup><br>= 2_mEn_|Proportional to energy level|



## **2. Common Perturbation Shortcuts in 1D Box** 

- **Linear Potential** _W_ ( _x_ ) = _βx_ **(** 0 _≤ x ≤ a_ **):** 



<!-- Start of picture text -->
E (1) = βa<br>n 2 (for all n )<br><!-- End of picture text -->

Notes 

3 



<!-- Start of picture text -->
• Constant Delta Function at Midpoint W ( x ) =  V 0  δ � x − a 2 � :<br><!-- End of picture text -->



<!-- Start of picture text -->
En (1) =  V 0 2 = 2 Va 0 for odd n  = 1 ,  3 ,  5 , . . .<br>��� ψn � a 2 ���� 0 for even n  = 2 ,  4 ,  6 , . . .<br>�<br><!-- End of picture text -->

_(Even states have a node at x_ = _a_ /2 _, so they experience zero shift!)_ 

• **Step Perturbation over Half the Box (** _W_ ( _x_ ) = _V_ 0 **for** 0 _≤ x ≤ a_ /2 **):** 



<!-- Start of picture text -->
E (1) = V 0<br>n 2 (for all n )<br><!-- End of picture text -->

**Follow-up suggestion:** Would you like to practice a problem involving **Delta Function Perturbations** or **Variational Method estimates** for ground state energy next? 

