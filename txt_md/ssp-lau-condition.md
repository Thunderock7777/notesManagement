<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-lau-condition.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Here is the step-by-step mathematical breakdown of how we get from the **Laue condition** to 2 _⃗k ·⃗G_ = _G_<sup>2</sup> , and why it is physically identical to **Bragg’s Law** . 

## **Step 1: Understand Elastic Scattering** 

When an X-ray or electron wave scatters **elastically** from a crystal: 

- _⃗ki_ = incident wavevector 

- _⃗kf_ = diffracted (final) wavevector 

- **Elastic** means energy is conserved, so the wavelength does not change ( _λf_ = _λi_ ). 

- • Therefore, the **magnitudes** (lengths) of both wavevectors are identical: 



<!-- Start of picture text -->
|⃗kf |  =  |⃗ki|  =  k = 2 π<br>λ<br><!-- End of picture text -->

## **Step 2: The Laue Condition** 

The Laue diffraction condition states that the wavevector shift (momentum transfer) must equal a reciprocal lattice vector _⃗G_ : 



<!-- Start of picture text -->
kf −⃗ki = ⃗G = ⇒⃗kf = ⃗ki  + ⃗G<br><!-- End of picture text -->

## **Step 3: Squaring Both Sides (Dot Product)** 

To eliminate vector directions and work with magnitudes, take the dot product of each side with itself: 



<!-- Start of picture text -->
kf ·⃗kf = ( ⃗ki  + ⃗G )  ·  ( ⃗ki  + ⃗G )<br><!-- End of picture text -->

1. **Left-Hand Side (LHS):** 



<!-- Start of picture text -->
kf ·⃗kf =  |⃗kf | 2 =  k 2<br><!-- End of picture text -->

2. **Right-Hand Side (RHS):** Expand using vector FOIL/dot product rules: 



<!-- Start of picture text -->
( ⃗ki  + ⃗G )  ·  ( ⃗ki  + ⃗G ) = ( ⃗ki ·⃗ki ) + 2( ⃗ki ·⃗G ) + ( ⃗G ·⃗G )<br><!-- End of picture text -->

Notes 

2 



<!-- Start of picture text -->
=  |⃗ki| 2 + 2( ⃗ki ·⃗G ) +  |⃗G| 2 =  k 2 + 2( ⃗ki ·⃗G ) +  G 2<br><!-- End of picture text -->

3. **Equate LHS and RHS:** 



<!-- Start of picture text -->
k 2 =  k 2 + 2( ⃗ki ·⃗G ) +  G 2<br><!-- End of picture text -->

4. **Subtract** _k_<sup>2</sup> **from both sides:** 



<!-- Start of picture text -->
2( ⃗ki ·⃗G ) +  G 2 = 0 = ⇒ 2( ⃗ki ·⃗G ) =  −G 2<br><!-- End of picture text -->

**Step 4: Why is it written as** 2 _⃗k ·⃗G_ = _G_<sup>2</sup> **?** 

Since _−⃗G_ is also a valid reciprocal lattice vector in the lattice (reciprocal space is symmetric), or if we define the incident vector as pointing _towards_ the origin ( _⃗k_ = _−⃗ki_ ), the minus sign disappears: 



<!-- Start of picture text -->
2k ~  · G ~  =  G 2<br><!-- End of picture text -->

**Step 5: How This Is Literally Bragg’s Law (** 2 _d_ sin _θ_ = _λ_ **)** 

Let’s prove that 2 _⃗k ·⃗G_ = _G_<sup>2</sup> is just Bragg’s Law written in vector notation: 

1. **Dot Product Definition:** 



<!-- Start of picture text -->
k ·⃗G  =  kG  cos  ϕ<br><!-- End of picture text -->

where _ϕ_ is the angle between _⃗k_ and _⃗G_ . Since _⃗G_ is perpendicular to the atomic planes, _ϕ_ = (90<sup>_◦_</sup> _− θ_ ), where _θ_ is the Bragg glancing angle. Therefore: 



<!-- Start of picture text -->
cos(90 ◦ − θ ) = sin  θ = ⇒⃗k ·⃗G  =  kG  sin  θ<br><!-- End of picture text -->

2. **Substitute back into** 2 _⃗k ·⃗G_ = _G_<sup>2</sup> **:** 



<!-- Start of picture text -->
2( kG  sin  θ ) =  G 2<br><!-- End of picture text -->

Divide both sides by _G_ : 



<!-- Start of picture text -->
2 k  sin  θ =  G<br><!-- End of picture text -->



<!-- Start of picture text -->
3. Plug in k = 2 λ π and G  = 2 d π :<br>2 sin  θ = 2 π<br>λ d<br>( 2 π )<br><!-- End of picture text -->



<!-- Start of picture text -->
4. Cancel 2 π from both sides:<br><!-- End of picture text -->



<!-- Start of picture text -->
2 sin  θ = 1<br>λ d = ⇒ 2d  sin  θ =  λ<br><!-- End of picture text -->

Notes 

3 

## **Summary** 

- 2 _d_ sin _θ_ = _λ −→_ Bragg’s Law in **real space** . 

- 2 _⃗k ·⃗G_ = _G_<sup>2</sup> _−→_ Bragg’s Law in **reciprocal space (vector form)** . 

They are 100% mathematically equivalent! 

