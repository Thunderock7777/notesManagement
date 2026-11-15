<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-parity-operator-algebraic-properties.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Here is a detailed, step-by-step breakdown of the algebraic proof using operator algebra. 

## **Step 1: Understanding the Parity Operator** Π<sup>ˆ</sup> 

The **Parity Operator** Π<sup>ˆ</sup> is defined by its action on spatial coordinates: 



<!-- Start of picture text -->
ˆΠ ψ ( x ) =  ψ ( −x )<br><!-- End of picture text -->

**Key Algebraic Properties of** Π<sup>ˆ</sup> **:** 

1. **Involution (** Π<sup>ˆ2</sup> = _I_<sup>ˆ</sup> **):** Reflecting space twice brings the particle back to its original position: 

      - ˆΠ<sup>2</sup> _ψ_ ( _x_ ) = ˆΠ _ψ_ ( _−x_ ) = _ψ_ ( _−_ ( _−x_ )) = _ψ_ ( _x_ ) 

2. **Hermitian & Unitary (** Π<sup>ˆ</sup><sup>_†_</sup> = Π<sup>ˆ</sup><sup>_−_1</sup> = Π<sup>ˆ</sup> **):** Parity is an observable with real eigenvalues _±_ 1. 

3. **Action on Position** _x_ ˆ **and Momentum** _p_ ˆ **:** 

   - Under spatial reflection _x →−x_ : 



<!-- Start of picture text -->
ˆΠˆ x ˆΠ † =  −x ˆ<br>• Since p ˆ =  −ih ¯ dx d and d ( −d x ) =  − dx d :<br>ˆΠˆ p ˆΠ † =  −p ˆ<br><!-- End of picture text -->

## **Step 2: Parity of the Ground State** _|_ 0 _⟩_ 

The ground state spatial eigenfunction is a Gaussian centered at the origin: 



<!-- Start of picture text -->
ψ 0( x ) = e − mω 2 h ¯ x 2<br>� mωπh ¯ �1/4<br><!-- End of picture text -->

Applying the parity operator: 



<!-- Start of picture text -->
ˆΠ ψ 0( x ) =  ψ 0( −x ) = e − mω 2 h ¯ ( −x )2 = e − mω 2 h ¯ x 2 = + ψ 0( x )<br>� mωπh ¯ �1/4 � mωπh ¯ �1/4<br><!-- End of picture text -->

In bra-ket notation: 



<!-- Start of picture text -->
Π ˆ | 0 ⟩ = +1  · | 0 ⟩ (Even Parity / Eigenvalue + 1 )<br><!-- End of picture text -->

Notes 

2 

**Step 3: Why the Creation Operator** _a_ ˆ<sup>_†_</sup> **is an “Odd Operator”** 

The creation (raising) operator expressed in terms of _x_ ˆ and _p_ ˆ is: 



<!-- Start of picture text -->
mω i<br>a ˆ † = � 2 h ¯ x ˆ  − √ 2 mhω ¯ p ˆ<br><!-- End of picture text -->

To find how _a_ ˆ<sup>_†_</sup> transforms under parity, we transform the operators inside: 



<!-- Start of picture text -->
mω i<br>ˆΠˆ a † ˆΠ † = � 2 h ¯ (ˆΠˆ x ˆΠ † )  − √ 2 mhω ¯ (Πˆ ˆ p Π ˆ † )<br><!-- End of picture text -->

Substitute Πˆ<sup>ˆ</sup> _x_ Π<sup>ˆ</sup><sup>_†_</sup> = _−x_ ˆ and Πˆ<sup>ˆ</sup> _p_ Π<sup>ˆ</sup><sup>_†_</sup> = _−p_ ˆ: 



<!-- Start of picture text -->
mω i mω i<br>ˆΠˆ a † ˆΠ † = � 2 h ¯ ( −x ˆ)  − √ 2 mhω ¯ ( −p ˆ) =  − � � 2 h ¯ x ˆ  − √ 2 mhω ¯ p ˆ� =  −a ˆ †<br><!-- End of picture text -->

Multiply by Π<sup>ˆ</sup> from the right (using Π<sup>ˆ</sup><sup>_†_ˆ</sup> Π = _I_<sup>ˆ</sup> ): 

**Π** ˆ **_a_** ˆ<sup>**_†_**</sup> **=** **_−a_** ˆ<sup>**_†_**</sup> **Π** ˆ 

**Crucial Anti-Commutation Relation:** The parity operator and creation operator **anti-commute** ( _{_ Π<sup>ˆ</sup> _,_ ˆ _a_<sup>_†_</sup> _}_ = 0). Passing Π<sup>ˆ</sup> past a single creation operator _a_ ˆ<sup>_†_</sup> produces a **minus sign** ! 

**Step 4: Rigorous Derivation of** Π<sup>ˆ</sup> _|n⟩_ = ( _−_ 1)<sup>_n_</sup> _|n⟩_ 

The _n_ -th excited state is built by applying _a_ ˆ<sup>_†_</sup> _n_ times to the ground state: 



<!-- Start of picture text -->
1 1<br>|n⟩ = √ n ! (ˆ a † ) n | 0 ⟩ = √ n ! � a ˆ † a ˆ † a ˆ �� † · · ·  ˆ a � † | 0 ⟩<br>n times<br><!-- End of picture text -->

Now apply the parity operator Π<sup>ˆ</sup> to state _|n⟩_ : 



<!-- Start of picture text -->
ˆΠ |n⟩ = ˆΠ a ˆ † a ˆ † · · ·  ˆ a † | 0 ⟩<br>� √ 1 n ! �<br><!-- End of picture text -->

Using the anti-commutation rule Πˆ<sup>ˆ</sup> _a_<sup>_†_</sup> = _−a_ ˆ<sup>_†_ˆ</sup> Π, move Π<sup>ˆ</sup> past each _a_ ˆ<sup>_†_</sup> operator one by one: 1. Move past the 1<sup>st</sup> operator: 



<!-- Start of picture text -->
ˆΠ(ˆ a † a ˆ † · · · | 0 ⟩ ) = ( −a ˆ † )ˆΠ(ˆ a † · · · | 0 ⟩ )<br><!-- End of picture text -->

2. Move past the 2<sup>nd</sup> operator: 



<!-- Start of picture text -->
( −a ˆ † )Π(ˆ ˆ a † · · · | 0 ⟩ ) = ( −a ˆ † )( −a ˆ † )Π( ˆ · · · | 0 ⟩ ) = ( −a ˆ † ) 2 ˆ Π( · · · | 0 ⟩ )<br><!-- End of picture text -->

3. Repeat this process for all _n_ operators: 



<!-- Start of picture text -->
ˆΠ(ˆ a † ) n | 0 ⟩ = ( −a ˆ † ) n ˆΠ | 0 ⟩<br><!-- End of picture text -->

Notes 

3 

Substitute ( _−a_ ˆ<sup>_†_</sup> )<sup>_n_</sup> = ( _−_ 1)<sup>_n_</sup> (ˆ _a_<sup>_†_</sup> )<sup>_n_</sup> and Π<sup>ˆ</sup> _|_ 0 _⟩_ = + _|_ 0 _⟩_ : 



<!-- Start of picture text -->
1<br>ˆΠ |n⟩ = ( − 1) n (ˆ a † ) n (+ | 0 ⟩ )<br>√ n !<br><!-- End of picture text -->

Rearranging terms: 



<!-- Start of picture text -->
ˆΠ |n⟩ = ( − 1) n | 0 ⟩ = ( − 1 ) n | n ⟩<br>� ( √ a ˆ †n )! n �<br><!-- End of picture text -->

## **Step 5: Physical Meaning (The Parity Ladder)** 

Each application of the raising operator _a_ ˆ<sup>_†_</sup> acts as a **parity-flipping quantum step** : 

State |0 _⟩_ ---> Even Parity (+1) [Gaussian bell curve] | (apply a _†_ ) State |1 _⟩_ ---> Odd Parity (-1) [Node at origin x = 0] | (apply a _†_ ) State |2 _⟩_ ---> Even Parity (+1) [Non-zero at x = 0] | (apply a _†_ ) State |3 _⟩_ ---> Odd Parity (-1) [Node at origin x = 0] • **Even** _n_ **(** _n_ = 0 _,_ 2 _,_ 4 _, . . ._ **):** ( _−_ 1)<sup>_n_</sup> = +1 = _⇒ ψn_ ( _−x_ ) = + _ψn_ ( _x_ ) ( **Even Parity** , _ψn_ (0) _̸_ = 0). • **Odd** _n_ **(** _n_ = 1 _,_ 3 _,_ 5 _, . . ._ **):** ( _−_ 1)<sup>_n_</sup> = _−_ 1 = _⇒ ψn_ ( _−x_ ) = _−ψn_ ( _x_ ) ( **Odd Parity** , _ψn_ (0) = 0). 

**Follow-up suggestion:** Would you like to see how this parity selection rule (∆ _n_ = _±_ 1 _, ±_ 3 _, . . ._ ) dictates electric dipole matrix elements _⟨m|x_ ˆ _|n⟩_ and radiative transitions in spectroscopy? 

