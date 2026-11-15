<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-evaluate-the-inner-commutator.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**Correct Answer** 

**Option (a):** _−_<sup>_<u>h</u>_¯</sup> _m_<sup>2</sup> 

**Detailed Step-by-Step Solution** 

**1. Evaluate the Inner Commutator** [ _x, H_ ] Given the Hamiltonian of a free particle: 



<!-- Start of picture text -->
H = p 2<br>2 m<br><!-- End of picture text -->

Evaluate [ _x, H_ ]: 



<!-- Start of picture text -->
1<br>=<br>[ x, H ] = x, p 2<br>2 m 2 m [ x, p 2]<br>[ ]<br><!-- End of picture text -->

Using the standard commutator product identity [ _A, BC_ ] = [ _A, B_ ] _C_ + _B_ [ _A, C_ ]: 



<!-- Start of picture text -->
[ x, p 2 ] = [ x, p ] p  +  p [ x, p ]<br><!-- End of picture text -->

Substituting the canonical commutation relation [ _x, p_ ] = _ih_ ¯: 



<!-- Start of picture text -->
[ x, p 2 ] = ( ih ¯) p  +  p ( ih ¯) = 2 ihp ¯<br><!-- End of picture text -->

Therefore, the inner commutator becomes: 



<!-- Start of picture text -->
1<br>[ x, H ] =<br>2 m (2 ihp ¯ ) = m ih ¯ p<br><!-- End of picture text -->

_(Note: This expression is directly related to velocity, since v_ = _m_<sup>_<u>p</u>_=</sup> _i_<sup><u>1</u></sup> _h_ ¯<sup>[</sup><sup>_x, H_]</sup><sup>_)._</sup> 

Notes 

2 

**2. Evaluate the Outer Commutator** [ _x,_ [ _x, H_ ]] Now substitute [ _x, H_ ] =<sup>_<u>i</u>_</sup> _m_<sup>_<u>h</u>_¯</sup><sup>_p_into the</sup> double commutator: 



<!-- Start of picture text -->
[ x,  [ x, H ]] = x, ih ¯<br>m p<br>[ ]<br><!-- End of picture text -->

Since<sup>_<u>i</u>_</sup> _m_<sup>_<u>h</u>_¯isascalarconstant,factoritoutsidethecommutator:</sup> 



<!-- Start of picture text -->
[ x,  [ x, H ]] = ih ¯<br>m [ x, p ]<br><!-- End of picture text -->

Substitute [ _x, p_ ] = _ih_ ¯: 



<!-- Start of picture text -->
[ x,  [ x, H ]] = ih ¯<br>m ( ih ¯) = i 2 m h ¯2 =  − h ¯ m 2<br><!-- End of picture text -->

## **Evaluation of Options** 

- **Option (a):** _−_<sup>_<u>h</u>_¯</sup> _m_<sup>2</sup><sup>_→_</sup><sup>**CORRECT!**</sup> 

- • **Option (b):** _<u>h</u>_ ¯ _m_<sup>2</sup><sup>_→_Incorrect(thiscorrespondsto[</sup><sup>_x,_[</sup><sup>_H, x_]]).</sup> 

- **Option (c):** 0 _→_ Incorrect. 

- **Option (d):** _<u>imh</u>_ ¯<sup>_→_Incorrect(thisisthevalueof[</sup><sup>_x, H_]beforetakingthesecond</sup> commutator with _x_ ). 

## **Key Concepts & Summary for GATE Physics** 

**1. Connection to the Thomas-Reiche-Kuhn (TRK) Sum Rule** In quantum mechanics, the double commutator of position with a standard kinetic-plus-potential Hamiltonian _H_ =<sup>_<u>p</u>_2</sup> 2 _m_<sup>+</sup><sup>_V_(</sup><sup>_x_)yieldsaconstantidentityscalar(since[</sup><sup>_x, V_(</sup><sup>_x_)] = 0):</sup> 



<!-- Start of picture text -->
[ x,  [ H, x ]] = h ¯2 = ⇒ [ x,  [ x, H ]] =  − h ¯2<br>m m<br><!-- End of picture text -->

Taking the expectation value of [ _x,_ [ _H, x_ ]] in an energy eigenstate _|n⟩_ leads directly to the **TRK Oscillator Strength Sum Rule** : 



<!-- Start of picture text -->
∑( Ek − En ) |⟨k|x|n⟩| 2 = 2 h ¯ m 2<br>k<br><!-- End of picture text -->

**2. Summary of High-Yield Commutators Involving** _H_ 

|Commutator Expression|Result|Physical Context|
|---|---|---|
|[_x, H_]|_i_¯_h_<br>_m_<sup>_p_</sup>|Velocity operator<br>_v_ = <sup>1</sup><br>_i_¯_h_<sup>[</sup><sup>_x, H_]</sup>|



Notes 

3 

|Commutator Expression|Result|Physical Context|
|---|---|---|
|[_p, H_]|_−i_¯_h_ <sup>_dV_</sup><br>_dx_ <sup>=</sup><sup>_i_¯</sup><sup>_hF_</sup>|Ehrenfest’s theorem for<br>force _F_|
|[_x,_[_x, H_]]|_−_<sup>¯</sup><sup>_h_2</sup><br>_m_|Double spatial commutator|
|[_x,_[_H, x_]]|+ <sup>¯</sup><sup>_h_2</sup><br>_m_|Operator form of TRK sum<br>rule basis|



**Follow-up suggestion:** Would you like to practice applying this double commutator identity to derive the **Thomas-Reiche-Kuhn sum rule** , or solve an **Ehrenfest’s theorem equation of motion** problem next? 

