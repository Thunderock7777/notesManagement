<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-zeeman-effect-formulaes3.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Here is the complete, step-by-step quantum mechanical derivation of the **Anomalous Zeeman energy shift** ∆ _E_ = _gJ µBBmj_ . 

## **Step 1: The Interaction Hamiltonian (** _H_<sup>ˆ</sup> **mag)** 

When an atom is placed in a weak external static magnetic field along the _z_ -axis ( _⃗B_ = _Bz_ ˆ), both the orbital angular momentum ( _⃗L_ ) and the spin angular momentum ( _⃗S_ ) generate magnetic dipole moments: 

- **Orbital Magnetic Moment (** _⃗µL_ **):** 



<!-- Start of picture text -->
µL =  −gL L  =  − µB (since gL = 1)<br>( µh ¯ B ) h⃗ ¯ L<br><!-- End of picture text -->

- **Spin Magnetic Moment (** _⃗µS_ **):** 



<!-- Start of picture text -->
µS =  −gS S ≈− 2 µB (since gS ≈ 2)<br>( µh ¯ B ) h⃗ ¯ S<br><!-- End of picture text -->

where _µB_ = 2 _<u>emh</u>_ ¯ _e_<sup>isthe</sup><sup>**BohrMagneton**.</sup> 

The total magnetic moment operator _⃗µJ_ is the sum of both components: 



<!-- Start of picture text -->
µJ = ⃗µL  + ⃗µS =  − µB<br>h ¯ ( ⃗L  + 2 ⃗S )<br><!-- End of picture text -->

The magnetic interaction Hamiltonian _H_<sup>ˆ</sup> mag is the potential energy of this dipole in the field _⃗B_ = _Bz_ ˆ: 



<!-- Start of picture text -->
− µB<br>H ˆ mag =  −⃗µJ ·⃗B =  − [ h ¯ ( ⃗L  + 2 ⃗S ) ] ·  ( Bz ˆ)<br>H ˆ mag = µBB ( Lz  + 2 Sz )<br>h ¯<br><!-- End of picture text -->

Using _Lz_ + _Sz_ = _Jz_ , we can rewrite this as: 



<!-- Start of picture text -->
H ˆ mag = µBB ( Jz  +  Sz )<br>h ¯<br><!-- End of picture text -->

Notes 

2 

## **Step 2: First-Order Perturbation Theory** 

Under a weak magnetic field (∆ _E_ Zeeman _≪_ ∆ _E_ spin-orbit), the coupled basis states _|j, mj, l, s⟩_ remain good unperturbed eigenstates. 

By first-order perturbation theory, the energy shift ∆ _E_ is the expectation value of _H_<sup>ˆ</sup> mag in the unperturbed state: 



<!-- Start of picture text -->
∆ E =  ⟨j, mj|H ˆ mag |j, mj⟩ = µBB ( ⟨j, mj|Jz|j, mj⟩ +  ⟨j, mj|Sz|j, mj⟩ )<br>h ¯<br>j⟩⟩ is an eigenstate of Jzz with eigenvalue mjhjhh ¯::<br>⟨j, mj|Jz|j, mj⟩ =  mjh ¯<br><!-- End of picture text -->

Since _|j, mj⟩⟩_ is an eigenstate of _Jzz_ with eigenvalue _mjhjhh_ ¯:: 

This gives: 



<!-- Start of picture text -->
∆ E =  µBBmj + µBB ⟨Sz⟩ — (Equation 1)<br>h ¯<br><!-- End of picture text -->

Now, we need to evaluate _⟨Sz⟩_ . 

## **Step 3: Vector Model & Wigner-Eckart Projection Theorem** 

Because of the internal spin-orbit interaction, _⃗L_ and _⃗S_ precess rapidly around the total angular momentum vector _⃗J_ = _⃗L_ + _⃗S_ . 

The components of _⃗S_ perpendicular to _⃗J_ average out to zero over time. Only the projection of _⃗S_ along _⃗J_ has a non-zero time average. 

By the **Wigner-Eckart Projection Theorem** for a vector operator: 



<!-- Start of picture text -->
⟨⃗S ·⃗J⟩<br>⟨⃗S⟩ = h ¯ 2 j ( j  + 1) ⃗ J<br><!-- End of picture text -->

Taking the _z_ -component: 



<!-- Start of picture text -->
⟨⃗S ·⃗J⟩ ⟨⃗S ·⃗J⟩<br>⟨Sz⟩ = h ¯ 2 j ( j  + 1) ⟨Jz⟩ = h ¯ 2 j ( j  + 1) ( mjh ¯) — (Equation 2)<br><!-- End of picture text -->

**Step 4: Evaluating the Operator Dot Product (** _⃗S ·⃗J_ **)** 

To find _⃗S ·⃗J_ , express _⃗L_ in terms of _⃗J_ and _⃗S_ : 



<!-- Start of picture text -->
L  = ⃗J −⃗S<br><!-- End of picture text -->

Square both sides: 



<!-- Start of picture text -->
L 2 = ( ⃗J −⃗S )  ·  ( ⃗J −⃗S ) = ⃗J 2 + ⃗S 2 − 2 ⃗S ·⃗J<br><!-- End of picture text -->

Rearranging for 2 _⃗S ·⃗J_ : 



<!-- Start of picture text -->
2 ⃗S ·⃗J = ⃗J 2 + ⃗S 2 −⃗L 2<br><!-- End of picture text -->

Notes 

3 



<!-- Start of picture text -->
⃗S ·⃗J = 1<br>2 ( ⃗J 2 + ⃗S 2  −⃗L 2)<br><!-- End of picture text -->

Replacing the operators with their quantum mechanical eigenvalues ( _⃗J_<sup>2</sup> _→ j_ ( _j_ + 1) _h_ ¯<sup>2</sup> , _S_<sup>2</sup> _→ s_ ( _s_ + 1) _h_ ¯<sup>2</sup> , _⃗L_<sup>2</sup> _→ l_ ( _l_ + 1) _h_ ¯<sup>2</sup> ): 



<!-- Start of picture text -->
⟨⃗S ·⃗J⟩ = h ¯2<br>2 [ j ( j  + 1) +  s ( s  + 1)  − l ( l  + 1)]<br><!-- End of picture text -->

**Step 5: Substitute Back into** _⟨Sz⟩_ 

Substitute _⟨⃗S ·⃗J⟩_ into Equation 2: 



<!-- Start of picture text -->
h ¯2 2 [ j ( j  + 1) +  s ( s  + 1)  − l ( l  + 1)]<br>⟨Sz⟩ = ( mjh ¯)<br>h ¯ 2 j ( j  + 1)<br>⟨Sz⟩ = mjh ¯ — (Equation 3)<br>[ j ( j  + 1) +2  sj (( sj  + 1 + 1))  − l ( l  + 1) ]<br><!-- End of picture text -->

**Step 6: Combine Terms to Obtain the Landé** _g_ **-Factor (** _gJ_ **)** 

Substitute Equation 3 back into Equation 1: 



<!-- Start of picture text -->
∆ E =  µBBmj + µBB mjh ¯<br>h ¯ ([ j ( j  + 1) +2  sj (( sj  + 1 + 1))  − l ( l  + 1) ] )<br><!-- End of picture text -->

Factor out _µBBmj_ : 



<!-- Start of picture text -->
∆ E = 1 + j ( j  + 1) +  s ( s  + 1)  − l ( l  + 1) µBBmj<br>( 2 j ( j  + 1) )<br><!-- End of picture text -->



<!-- Start of picture text -->
We define the dimensionless quantity inside the parenthesis as the Landé g -factor ( gJ ) :<br>gJ ≡ 1  + j ( j  +  1 ) +  s ( s  +  1 )  − l ( l  +  1 )<br>2j ( j  +  1 )<br><!-- End of picture text -->

Thus, the total energy shift simplifies to: 



<!-- Start of picture text -->
￿E  =  gJ µ BBmj<br><!-- End of picture text -->

## **Summary of the Derivation** 

1. **Hamiltonian:** _H_<sup>ˆ</sup> mag =<sup>_<u>µB</u>_</sup> _h_ ¯<sup>_B_(</sup><sup>_Jz_+</sup><sup>_Sz_).</sup> 2. **Expectation Value:** ∆ _E_ = _µBBmj_ +<sup>_<u>µB</u>_</sup> _h_ ¯<sup>_B⟨Sz⟩_.</sup> 3. **Projection Theorem:** Projects _Sz_ onto _Jz_ , yielding _⟨Sz⟩_ = _h_ ¯<sup>2</sup> _<u>⟨j⃗S</u>_ ( _·j⃗J_ +1) _<u>⟩</u>_<sup>_mjh_¯.</sup> 4. **Dot Product Expansion:** _⃗S ·⃗J_ =<sup><u>1</u></sup> 2<sup>(</sup><sup>_⃗J_2 +</sup><sup>_⃗S_2</sup><sup>_−⃗L_2).</sup> 5. **Final Result:** Grouping terms yields **￿E** = **gJ** _µ_ **BBmj** . 

Would you like to evaluate _gJ_ for a specific atomic level (like<sup>2</sup> P3/2 or<sup>3</sup> D2), or work through a line-counting example for transitions between two terms? 

