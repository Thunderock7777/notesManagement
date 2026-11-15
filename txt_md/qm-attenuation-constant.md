<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-attenuation-constant.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Standard Formula & Direct Answer** 

1. **Attenuation Constant (Decay Constant** _α_ **):** 



<!-- Start of picture text -->
√ 2 m ( V 0  − E )<br>α  =<br>h ¯<br><!-- End of picture text -->

2. **Decay Length for Wavefunction Amplitude (** _x_ 0 = 1/ _α_ **):** 



<!-- Start of picture text -->
h ¯<br>x0 =<br>√ 2m ( V0  − E )<br><!-- End of picture text -->

3. **Decay Length for Probability Density (** _x_ 0 _,P_ = 1/2 _α_ **):** 



<!-- Start of picture text -->
h ¯<br>x0 , P =<br>2 √ 2m ( V0  − E )<br><!-- End of picture text -->

## **Detailed Step-by-Step Derivation** 

**1. Solve the Time-Independent Schrödinger Equation for** _x >_ 0 In region II ( _x >_ 0), the potential is constant with height _V_ ( _x_ ) = _V_ 0. Since the incident energy _E < V_ 0, this is a **classically forbidden region** . 

The Schrödinger equation in region II is: 



<!-- Start of picture text -->
− h ¯2 d 2 ψ<br>2 m dx 2 +  V 0 ψ ( x ) =  Eψ ( x )<br><!-- End of picture text -->

Rearranging terms: 



<!-- Start of picture text -->
d 2 ψ<br>ψ ( x )<br>dx 2 = 2 m ( V h ¯ 02  − E )<br><!-- End of picture text -->

Define the real positive decay constant _α_ : 



<!-- Start of picture text -->
α 2 = 2 m ( V 0  − E ) = ⇒ α  = √ 2m ( V0  − E )<br>h ¯ 2 h ¯<br><!-- End of picture text -->

The differential equation simplifies to: 



<!-- Start of picture text -->
d 2 ψ<br>dx 2 − α 2 ψ ( x ) = 0<br><!-- End of picture text -->

Notes 

2 

**2. Apply Boundary Conditions at Infinity** The general solution is a linear combination of exponential terms: 



<!-- Start of picture text -->
ψ ( x ) =  Ce −αx +  De + αx<br><!-- End of picture text -->

- As _x →_ + _∞_ , the term _e_<sup>+</sup><sup>_αx_</sup> _→∞_ , which violates the physical requirement that the wavefunction must remain finite and normalizable. 

- Therefore, we must set _D_ = 0. 

The physically acceptable wavefunction in _x >_ 0 is: 



<!-- Start of picture text -->
ψ ( x ) =  Ce −αx =  C  exp − √ 2 m ( V 0  − E ) x<br>h ¯<br>( )<br><!-- End of picture text -->

## **3. Calculate the Decay Lengths** 

**Case A: Wavefunction Decay Length (** _x_ 0 = 1/ _α_ **)** The spatial distance _x_ 0 at which the amplitude of the wavefunction _ψ_ ( _x_ ) drops to 1/ _e_ (or _≈_ 36 _._ 8%) of its value at the interface ( _x_ = 0): 



<!-- Start of picture text -->
|ψ ( x 0) |  =  |ψ (0) |e −αx 0 =  |ψ (0) |e − 1 = ⇒ αx 0 = 1<br><!-- End of picture text -->



<!-- Start of picture text -->
x0 = 1 h ¯<br>α =<br>√ 2m ( V0  − E )<br><!-- End of picture text -->

**Case B: Probability Density Decay Length (** _x_ 0 _,P_ = 1/2 _α_ **)** The probability density _P_ ( _x_ ) in region _x >_ 0 is given by: 



<!-- Start of picture text -->
P ( x ) =  |ψ ( x ) | 2 =  |C| 2 e − 2 αx<br><!-- End of picture text -->

The distance _x_ 0 _,P_ at which the probability density drops to 1/ _e_ of its value at _x_ = 0 satisfies: 



<!-- Start of picture text -->
e − 2 αx 0 ,P =  e − 1 = ⇒ 2 αx 0 ,P = 1<br><!-- End of picture text -->



<!-- Start of picture text -->
x0 , P = 1 h ¯<br>2 α = 2 √ 2m ( V0  − E )<br><!-- End of picture text -->

**Summary Table for Potential Step (** _E < V_ 0 **)** 

|Physical Quantity|Symbol|Formula|
|---|---|---|
|**Decay/Attenuation**<br>**Constant**|_α_|_~~√~~_<br>2_m_(_V_0_−E_)<br>¯_h_|



Notes 

3 

|Physical Quantity|Symbol|Formula|
|---|---|---|
|**Wavefunction**<br>**Penetration Depth**|_x_0 = <sup>1</sup><br>_α_|¯_h_<br>_~~√~~_<br>2_m_(_V_0_−E_)|
|**Probability Density**<br>**Penetration Depth**|1<br>2_α_|¯_h_<br>2<sup>_~~√~~_</sup><br>2_m_(_V_0_−E_)|
|**Reflection Coefficient**|_R_|1 _(100% total reflection)_|
|**Transmitted**<br>**Probability Current**|_J_trans|0|



**Follow-up suggestion:** Would you like to practice calculating the **phase shift of the reflected wave** at a potential step or solve a **quantum tunneling problem through a rectangular barrier of finite width** ? 

