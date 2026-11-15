<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-made-option-detailed-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answer** 

**Option (d): 2ih** ¯ ( **xp** + **px** ) 

**Detailed Step-by-Step Solution** 

**Method 1: Operator Identity Expansion (Step-by-Step)** 

1. **Recall the Fundamental Commutation Relation:** 



<!-- Start of picture text -->
[ x, p ] =  xp − px  =  ih ¯<br><!-- End of picture text -->

2. **Use the Commutator Product Identity:** For any three operators _A_<sup>ˆ</sup> , _B_<sup>ˆ</sup> , and _C_<sup>ˆ</sup> : [ _A, BC_ ] = [ _A, B_ ] _C_ + _B_ [ _A, C_ ] 

Let _A_<sup>ˆ</sup> = _x_<sup>2</sup> , _B_<sup>ˆ</sup> = _p_ , and _C_<sup>ˆ</sup> = _p_ . Then: 



<!-- Start of picture text -->
[ x 2 , p 2 ] = [ x 2 , p · p ] = [ x 2 , p ] p  +  p [ x 2 , p ]<br><!-- End of picture text -->

3. **Evaluate the Inner Commutator** [ _x_<sup>2</sup> _, p_ ] **:** Applying the identity [ _AB, C_ ] = _A_ [ _B, C_ ] + [ _A, C_ ] _B_ with _A_ = _x_ , _B_ = _x_ , and _C_ = _p_ : 



<!-- Start of picture text -->
[ x 2 , p ] =  x [ x, p ] + [ x, p ] x<br><!-- End of picture text -->

Substitute [ _x, p_ ] = _ih_ ¯: 



<!-- Start of picture text -->
[ x 2 , p ] =  x ( ih ¯) + ( ih ¯) x  =  ihx ¯  +  ihx ¯  = 2 ihx ¯<br><!-- End of picture text -->

4. **Substitute** [ _x_<sup>2</sup> _, p_ ] = 2 _ihx_ ¯ **back into** [ _x_<sup>2</sup> _, p_<sup>2</sup> ] **:** 



<!-- Start of picture text -->
[ x 2 , p 2 ] = (2 ihx ¯ ) p  +  p (2 ihx ¯ )<br><!-- End of picture text -->

Since 2 _ih_ ¯ is a scalar constant, pull it out in front: 



<!-- Start of picture text -->
[ x 2 ,  p 2 ] =  2ihxp ¯  +  2ihpx ¯  =  2ih ¯ ( xp  +  px )<br><!-- End of picture text -->

Notes 

2 

**Method 2: Dual Expansion via** [ _x, p_<sup>2</sup> ] Alternatively, expand using [ _AB, C_ ] = _A_ [ _B, C_ ] + [ _A, C_ ] _B_ with _A_ = _x_ , _B_ = _x_ , _C_ = _p_<sup>2</sup> : 

1. **Expand** [ _x_<sup>2</sup> _, p_<sup>2</sup> ] **:** 



<!-- Start of picture text -->
[ x 2 , p 2 ] =  x [ x, p 2 ] + [ x, p 2 ] x<br><!-- End of picture text -->



<!-- Start of picture text -->
2. Evaluate [ x, p 2 ] :<br><!-- End of picture text -->



<!-- Start of picture text -->
[ x, p 2 ] = [ x, p ] p  +  p [ x, p ] = ( ih ¯) p  +  p ( ih ¯) = 2 ihp ¯<br><!-- End of picture text -->

3. **Substitute back:** 



<!-- Start of picture text -->
[ x 2 , p 2 ] =  x (2 ihp ¯ ) + (2 ihp ¯ ) x  =  2ih ¯ ( xp  +  px )<br><!-- End of picture text -->

## **Evaluation of Options** 

- **Option (a):** _ih_ ¯( _xp − px_ ) _→_ **Incorrect** 

- **Option (b):** 2 _ih_ ¯( _xp − px_ ) _→_ **Incorrect** (Note: _xp − px_ = _ih_ ¯, so this equals 2 _ih_ ¯( _ih_ ¯) = _−_ 2 _h_ ¯<sup>2</sup> , which is a constant, whereas [ _x_<sup>2</sup> _, p_<sup>2</sup> ] is an operator). 

- **Option (c):** _ih_ ¯( _xp_ + _px_ ) _→_ **Incorrect** (Missing a factor of 2). 

- **Option (d): 2ih** ¯ ( **xp** + **px** ) _→_ **CORRECT!** 

## **Key Concepts & Formulae to Remember for GATE Physics** 

## **1. Core Commutator Identities** 

- **Linearly Distributive:** [ _A, B_ + _C_ ] = [ _A, B_ ] + [ _A, C_ ] 

- **Antisymmetry:** [ _A, B_ ] = _−_ [ _B, A_ ] 

- **Right Product Rule:** [ _A, BC_ ] = [ _A, B_ ] _C_ + _B_ [ _A, C_ ] 

- **Left Product Rule:** [ _AB, C_ ] = _A_ [ _B, C_ ] + [ _A, C_ ] _B_ 

- **Jacobi Identity:** [ _A,_ [ _B, C_ ]] + [ _B,_ [ _C, A_ ]] + [ _C,_ [ _A, B_ ]] = 0 

**2. Derivative Shortcuts for Powers of Operators** For any well-behaved function _f_ ( _x_ ) or _g_ ( _p_ ): 

- [ _f_ ( _x_ ) _, p_ ] = _ih_ ¯ _dx_<sup>_df_</sup> 

- • [ _x, g_ ( _p_ )] = _ih_ ¯<sup>_d_</sup> _dp_<sup>_<u>g</u>_</sup> • [ _x_<sup>_n_</sup> _, p_ ] = _nihx_ ¯<sup>_n−_1</sup> • [ _x, p_<sup>_n_</sup> ] = _nihp_ ¯<sup>_n−_1</sup> 

_Example:_ [ _x_<sup>3</sup> _, p_ ] = 3 _ihx_ ¯<sup>2</sup> and [ _x, p_<sup>4</sup> ] = 4 _ihp_ ¯<sup>3</sup> . 

## **3. High-Yield Commutator Master Table** 

Notes 

3 

|Commutator|Simplified Expression|Notes / Physical<br>Significance|
|---|---|---|
|[_x, p_]|_i_¯_h_|Canonical commutation<br>relation|
|[_x_<sup>2</sup>_, p_]|2_i_¯_hx_|Linear in _x_|
|[_x, p_<sup>2</sup>]|2_i_¯_hp_|Linear in _p_|
|[_x_<sup>2</sup>_, p_<sup>2</sup>]|**2i**¯**h**(**xp**+**px**)|Symmetrized product of _x_<br>and _p_|
|[_x, H_]|_i_¯_h_ <sup>_p_</sup><br>_m_|Velocity operator _v_ = <sup>_p_</sup><br>_m_<br>(for _H_ = <sup>_p_2</sup><br>2_m_ <sup>+</sup><sup>_V_ (</sup><sup>_x_))</sup>|
|[_p, H_]|_−i_¯_h_ <sup>_dV_</sup><br>_dx_ <sup>=</sup><sup>_i_¯</sup><sup>_hF_</sup>|Ehrenfest theorem for force|



**Follow-up suggestion:** Would you like to practice evaluating commutators involving **angular momentum components** (e.g., [ _L_<sup>2</sup> _x_<sup>_, Ly_])orsolvingan</sup><sup>**Ehrenfesttheorem**</sup> rate of change problem next? 

