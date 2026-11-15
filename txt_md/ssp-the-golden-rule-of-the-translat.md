<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-the-golden-rule-of-the-translat.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

The second term _V_ ( _x_ + _a_ ) _ψ_ ( _x_ + _a_ ) comes directly from how the **Translation Operator (** _T_<sup>ˆ</sup> _a_ **)** works on a product of functions. 

Here is the step-by-step breakdown: 

## **1. The Golden Rule of the Translation Operator (** _T_<sup>ˆ</sup> _a_ **)** 

By definition, the translation operator _T_<sup>ˆ</sup> _a_ takes **any function of** _x_ , let’s call it _f_ ( _x_ ), and **replaces every single instance of** _x_ **with** ( _x_ + _a_ ): 



<!-- Start of picture text -->
T ˆ a � f ( x )� =  f ( x  +  a )<br><!-- End of picture text -->

**2. What is** _f_ ( _x_ ) **in our expression** _T_<sup>ˆ</sup> _a_ � _Hψ_ ˆ ( _x_ )� **?** 

First, let _H_<sup>ˆ</sup> act on _ψ_ ( _x_ ): 



<!-- Start of picture text -->
d 2 ψ ( x )<br>Hψ ˆ ( x ) =  − h ¯2 + V  ( x ) ψ ( x )<br>� 2 m �� dx 2 � Term � 2 �� (Potential) �<br>Term 1 (Kinetic)<br><!-- End of picture text -->

Look closely at **Term 2** : it is a product of two terms, both depending on _x_ : 

1. The potential function _V_ ( _x_ ) 

2. The wavefunction _ψ_ ( _x_ ) 

So, Term 2 as a single function of _x_ is: 

Term 2 = _V_ ( _x_ ) _· ψ_ ( _x_ ) 

**3. Applying** _T_<sup>ˆ</sup> _a_ **to Term 2** 

When _T_<sup>ˆ</sup> _a_ acts on _Hψ_<sup>ˆ</sup> ( _x_ ), it replaces **every** _x_ in Term 2 with ( _x_ + _a_ ): 

- _V_ ( _x_ ) _−→ V_ ( _x_ + _a_ ) 

- _ψ_ ( _x_ ) _−→ ψ_ ( _x_ + _a_ ) 

Notes 

2 

Multiplying them together gives: 



<!-- Start of picture text -->
T ˆ a � V  ( x ) ψ ( x )� =  V ( x  +  a ) ψ ( x  +  a )<br><!-- End of picture text -->

## **Comparing the Two Orders (Why this is so important)** 

To see the difference clearly, compare the two operations side-by-side: 

1. **In** _T_<sup>ˆ</sup> _a_ � _Hψ_ ˆ ( _x_ )� **(Translate** **_after_ applying** _H_ **):** 

   - _H_<sup>ˆ</sup> acts first to create the function _V_ ( _x_ ) _ψ_ ( _x_ ). 

   - Then _T_<sup>ˆ</sup> _a_ shifts **everything** , turning _V_ ( _x_ ) _ψ_ ( _x_ ) into _V_ ( _x_ + _a_ ) _ψ_ ( _x_ + _a_ ). 

2. **In** _H_<sup>ˆ</sup> � _T_ ˆ _aψ_ ( _x_ )� **(Translate** **_before_ applying** _H_ **):** 

   - _T_<sup>ˆ</sup> _a_ acts first on _ψ_ ( _x_ ) alone to create _ϕ_ ( _x_ ) = _ψ_ ( _x_ + _a_ ). 



<!-- Start of picture text -->
• Then H ˆ =  − h ¯ 2 d 2<br>2 m dx 2 +  V  ( x ) acts on ϕ ( x ).<br>• This gives − 2 h ¯ m 2 d 2 ψdx ( x 2 + a ) +  V ( x ) ψ ( x  +  a ).<br><!-- End of picture text -->

Notice that in (1) we get _V_ ( _x_ + _a_ ), whereas in (2) we get _V_ ( _x_ ). Subtracting the two gives [ _V_ ( _x_ ) _− V_ ( _x_ + _a_ )] _ψ_ ( _x_ + _a_ ), which equals 0 **only because the potential is periodic** ( _V_ ( _x_ + _a_ ) = _V_ ( _x_ ))! 

_Does this clear up how V_ ( _x_ + _a_ ) _ψ_ ( _x_ + _a_ ) _was generated?_ 

