<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-set-up-the-wavefunction.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Here is the step-by-step mathematical proof showing that the probability of finding a particle in the left half of the box is **always**<sup><u>1</u></sup> 2<sup>**foranyquantumstate**</sup><sup>_n_.</sup> 

## **1. Set Up the Wavefunction & Integral** 

For a 1D box of length _L_ (0 _≤ x ≤ L_ ), the normalized eigenfunction for any state _n_ = 1 _,_ 2 _,_ 3 _, . . ._ is: 



<!-- Start of picture text -->
2<br>ψn (0)( x ) =<br>� L sin � nπxL �<br><!-- End of picture text -->

The probability of finding the particle in the interval 0 _≤ x ≤ L_ /2 is given by: 



<!-- Start of picture text -->
2<br>P �0  ≤ x ≤ L 2 � = �0 L /2 �� ψn (0) ( x ) ��2  dx  = �0 L /2 L sin � nπxL dx<br>� � � �2<br>P = 2 dx<br>L �0 L /2 sin 2 � nπx L �<br><!-- End of picture text -->

## **2. Apply the Trigonometric Identity** 

Using sin<sup>2</sup> _θ_ =<sup>1</sup><sup>_−_cos</sup> 2<sup><u>(2</u></sup><sup>_θ_</sup><sup><u>)</u></sup> with _θ_ =<sup>_<u>nπx</u>_</sup> _L_<sup>:</sup> 



<!-- Start of picture text -->
1  − cos<br>P = 2 � 2 nπxL � dx<br>L �0 L /2 2<br>� �<br><!-- End of picture text -->

The factor of 2 cancels out: 



<!-- Start of picture text -->
P = 1 1  − cos dx<br>L �0 L /2 � � 2 nπxL ��<br><!-- End of picture text -->

Notes 

2 

## **3. Perform the Integration** 

Integrating term-by-term: 



<!-- Start of picture text -->
P = 1 x − L<br>L 2 nπ sin L<br>� � 2 nπx �� L 0 /2<br><!-- End of picture text -->

Now, substitute the upper limit _x_ = _L_ /2 and lower limit _x_ = 0: 

1. **At Upper Limit (** _x_ = _L_ /2 **):** 



<!-- Start of picture text -->
x → L<br>2<br>sin = sin( nπ )<br>L<br>� 2 nπ ( L /2) �<br><!-- End of picture text -->

Since _n_ is an integer ( _n_ = 1 _,_ 2 _,_ 3 _, . . ._ ), sin( _nπ_ ) = 0 **for all** _n_ . 

2. **At Lower Limit (** _x_ = 0 **):** 



<!-- Start of picture text -->
x → 0<br><!-- End of picture text -->



<!-- Start of picture text -->
sin(0) = 0<br><!-- End of picture text -->

## **4. Combine Results** 

Substituting these evaluated limits back into the expression: 



<!-- Start of picture text -->
P = 1 L − (0  − 0)<br>L 2 − 2 nπ (0)<br>�� L � �<br>P = 1 = 1<br>L 2 2<br>� L �<br><!-- End of picture text -->



<!-- Start of picture text -->
|ψ n ( 0 )( x ) | 2dx  = 1 for all n  =  1 ,  2 ,  3 , . . .<br>� 0L / 2 2<br><!-- End of picture text -->

## **Geometric / Physical Intuition** 

1. **Total Normalization:** The probability across the whole box is 1: 



<!-- Start of picture text -->
|ψn (0)( x ) | 2 dx  = 1<br>�0 L<br><!-- End of picture text -->

2. **Reflection Symmetry:** The probability density _Pn_ ( _x_ ) = _|ψn_<sup>(0)(</sup><sup>_x_)</sup><sup>_|_2=</sup> _L_<sup><u>2</u>sin2 �</sup><sup>_<u>nπx</u>_</sup> _L_ � is completely symmetric about the center _x_ = _L_ /2. 

3. Because the left half (0 _≤ x ≤ L_ /2) and right half ( _L_ /2 _≤ x ≤ L_ ) are exact mirror images, the total area under _Pn_ ( _x_ ) splits equally into two halves of **1** / **2** each. 

**Would you like to see how this probability changes if the perturbation is localized over a smaller region, like** 0 _≤ x ≤ L_ /4 **?** 

