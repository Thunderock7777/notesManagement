<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-eigenvalues-and-eigenstates-formalism.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Here is the step-by-step mathematical derivation for finding the eigenvalues and eigenstates of the Pauli matrices, followed by the general spin state along an arbitrary direction _n_ ˆ. 

**1. Eigenstates of standard Pauli Matrices (** _σz_ **,** _σx_ **,** _σy_ **)** 

**A.** _σz_ **Matrix (Computational Basis)** 



<!-- Start of picture text -->
0<br>σz =<br>0 − 1<br>�1 �<br><!-- End of picture text -->

1. **Characteristic Equation:** 

det( _σz − λI_ ) = (1 _− λ_ )( _−_ 1 _− λ_ ) = _λ_<sup>2</sup> _−_ 1 = 0 = _⇒ λ_ = _±_ **1** 

2. **Eigenvector for** _λ_ = +1 **:** 



<!-- Start of picture text -->
0<br>= 1 = ⇒ = = ⇒ β = 0<br>�01 − 1�� αβ � � αβ � � −αβ � � αβ �<br><!-- End of picture text -->

Normalizing ( _α_ = 1): 



<!-- Start of picture text -->
|  +  z⟩ = =  | 0 ⟩<br>0<br>�1�<br><!-- End of picture text -->

3. **Eigenvector for** _λ_ = _−_ 1 **:** 



<!-- Start of picture text -->
0<br>=  − 1 = ⇒ = = ⇒ α  = 0<br>�01 − 1�� αβ � � αβ � � −αβ � � −−αβ �<br><!-- End of picture text -->

Normalizing ( _β_ = 1): 



<!-- Start of picture text -->
| − z⟩ = =  | 1 ⟩<br>1<br>�0�<br><!-- End of picture text -->

Notes 

2 

**B.** _σx_ **Matrix** 



<!-- Start of picture text -->
1<br>σx =<br>1 0<br>�0 �<br><!-- End of picture text -->

1. **Characteristic Equation:** 



<!-- Start of picture text -->
det( σx − λI ) =  λ 2 − 1 = 0 = ⇒ λ  =  ± 1<br><!-- End of picture text -->

2. **Eigenvector for** _λ_ = +1 **:** 



<!-- Start of picture text -->
1<br>= 1 = ⇒ β =  α<br>�10 0�� αβ � � αβ �<br>Normalizing ( α 2 +  β 2 = 2 α 2 = 1 = ⇒ α  = √ 12 ):<br><!-- End of picture text -->



<!-- Start of picture text -->
|  +  x⟩ = 1 = | 0 ⟩ + | 1 ⟩<br>√ 2 �11� √ 2<br><!-- End of picture text -->

3. **Eigenvector for** _λ_ = _−_ 1 **:** 



<!-- Start of picture text -->
1<br>=  − 1 = ⇒ β =  −α<br>�10 0�� αβ � � αβ �<br>| − x⟩ = 1 = | 0 ⟩ − | 1 ⟩<br>√ 2 � − 11� √ 2<br><!-- End of picture text -->

**C.** _σy_ **Matrix** 



<!-- Start of picture text -->
−i<br>σy =<br>i 0<br>�0 �<br><!-- End of picture text -->

1. **Characteristic Equation:** 

det( _σy − λI_ ) = _λ_<sup>2</sup> _−_ ( _−i_ )( _i_ ) = _λ_<sup>2</sup> _−_ 1 = 0 = _⇒ λ_ = _±_ **1** 

2. **Eigenvector for** _λ_ = +1 **:** 



<!-- Start of picture text -->
−i<br>= 1 = ⇒−iβ =  α = ⇒ β =  iα<br>�0 i 0 �� αβ � � αβ �<br><!-- End of picture text -->

Normalizing: 



<!-- Start of picture text -->
|  +  y⟩ = 1 = | 0 ⟩ +  i| 1 ⟩<br>√ 2 �1 i � √ 2<br><!-- End of picture text -->

3. **Eigenvector for** _λ_ = _−_ 1 **:** 



<!-- Start of picture text -->
−i<br>=  − 1 = ⇒−iβ =  −α = ⇒ β =  −iα<br>�0 i 0 �� αβ � � αβ �<br>| − y⟩ = 1 = | 0 ⟩ − i| 1 ⟩<br>√ 2 � − 1 i � √ 2<br><!-- End of picture text -->

Notes 

3 

## **2. Derivation of General Spin Projection** **_σ_** _·_ ˆ _n_ 

Let _n_ ˆ = (sin _θ_ cos _ϕ,_ sin _θ_ sin _ϕ,_ cos _θ_ ) be an arbitrary unit vector in 3D space. 

## **Step A: Construct the Matrix** 



<!-- Start of picture text -->
σ  ·  ˆ n  =  nxσx  +  nyσy  +  nzσz<br>1 −i 0<br>σ  ·  ˆ n  = sin  θ  cos  ϕ + sin  θ  sin  ϕ + cos  θ<br>1 0 i 0 0 − 1<br>�0 � �0 � �1 �<br>σ  ·  ˆ n  = cos  θ sin  θ (cos  ϕ − i  sin  ϕ ) = sin  θe −iϕ<br>�sin  θ (cos  ϕ  +  i  sin  ϕ ) − cos  θ � �sincos  θe θ iϕ − cos  θ �<br><!-- End of picture text -->

## **Step B: Find Eigenvalues** 



<!-- Start of picture text -->
cos  θ − λ sin  θe −iϕ<br>det( σ  ·  ˆ n − λI ) =<br>sin  θe iϕ − cos  θ − λ<br>���� ���� = 0<br><!-- End of picture text -->



<!-- Start of picture text -->
λ 2 − cos 2 θ − sin 2 θ = 0 = ⇒ λ 2 − 1 = 0 = ⇒ λ  =  ± 1<br><!-- End of picture text -->

Here is the explicit step-by-step derivation for the general spin state along _n_ ˆ. 

## **1. Matrix Construction** 



<!-- Start of picture text -->
σ  ·  ˆ n  =  nxσx  +  nyσy  +  nzσz<br><!-- End of picture text -->



<!-- Start of picture text -->
1 −i 0<br>σ  ·  ˆ n  = sin  θ  cos  ϕ + sin  θ  sin  ϕ + cos  θ<br>1 0 i 0 0 − 1<br>�0 � �0 � �1 �<br><!-- End of picture text -->

Combining terms using Euler’s formula (cos _ϕ ± i_ sin _ϕ_ = _e_<sup>_±iϕ_</sup> ): 



<!-- Start of picture text -->
sin  θe −iϕ<br>σ  ·  ˆ n  =<br>sin  θe iϕ − cos  θ<br>� cos  θ �<br><!-- End of picture text -->

## **2. Eigenvalues** 



<!-- Start of picture text -->
det( σ  ·  ˆ n − λI ) = (cos  θ − λ )( − cos  θ − λ )  − (sin  θe −iϕ )(sin  θe iϕ ) = 0<br><!-- End of picture text -->



<!-- Start of picture text -->
λ 2 − cos 2 θ − sin 2 θ = 0 = ⇒ λ 2 − 1 = 0 = ⇒ λ  =  ± 1<br><!-- End of picture text -->

Notes 

4 

**3. Eigenvector for** _λ_ = +1 



<!-- Start of picture text -->
sin  θe −iϕ<br>= 1<br>�sincos  θe θ iϕ − cos  θ �� αβ � � αβ �<br><!-- End of picture text -->

Expanding the first row: 

_α_ cos _θ_ + _β_ sin _θe_<sup>_−iϕ_</sup> = _α_ = _⇒ β_ sin _θe_<sup>_−iϕ_</sup> = _α_ (1 _−_ cos _θ_ ) 

Apply standard half-angle identities: 



<!-- Start of picture text -->
• 1  − cos  θ = 2 sin 2 � 2 θ �<br>• sin  θ = 2 sin cos<br>� 2 θ � � 2 θ �<br><!-- End of picture text -->

Substitute these into the equation: 



<!-- Start of picture text -->
β 2 sin cos e −iϕ =  α 2 sin 2<br>2 2 2<br>� � θ � � θ �� � � θ ��<br><!-- End of picture text -->

Divide both sides by 2 sin � 2 _<u>θ</u>_ �: 



<!-- Start of picture text -->
cos( θ /2)<br>β  cos e −iϕ =  α  sin = ⇒ α<br>� 2 θ � � 2 θ � β = sin( θ /2) e iϕ<br><!-- End of picture text -->

To satisfy this ratio while ensuring normalization ( _|α|_<sup>2</sup> + _|β|_<sup>2</sup> = 1): 



<!-- Start of picture text -->
α  = cos<br>2<br>� θ �<br>β =  e iϕ sin<br>2<br>� θ �<br><!-- End of picture text -->

## **Final Bloch State Result** 



<!-- Start of picture text -->
back into the state vector :<br>� αβ �<br>|χ +(ˆ n ) ⟩ = cos | 0 ⟩ +  e iϕ sin | 1 ⟩<br>2 2<br>� θ � � θ �<br><!-- End of picture text -->

Putting the components back into the state vector 

This confirms that the normalized eigenstate of **_σ_** _· n_ ˆ for eigenvalue +1 generates the exact standard Bloch sphere representation! 

