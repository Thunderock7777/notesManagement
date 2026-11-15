<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-two-state-time-evolved-wavefunction.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answer** 

**1** (or **100%** ) 

## **Detailed Step-by-Step Solution** 

**1. Write the Time-Evolved Wavefunction** In quantum mechanics, a stationary state _|ψn⟩_ with energy eigenvalue _En_ evolves in time according to: 



<!-- Start of picture text -->
|ψn ( t ) ⟩ =  e −iEnt / h ¯ |ψn (0) ⟩<br><!-- End of picture text -->

For the given two-state system: 



<!-- Start of picture text -->
• E + = + ϵ = ⇒|ψ +( t ) ⟩ =  e −iϵt / h ¯ |ψ + ⟩<br>• E− =  −ϵ = ⇒|ψ− ( t ) ⟩ =  e + iϵt / h ¯ |ψ−⟩<br><!-- End of picture text -->

Given the initial state at _t_ = 0: 



<!-- Start of picture text -->
| Ψ(0) ⟩ = 1<br>√ 2 ( |ψ + ⟩ +  |ψ−⟩ )<br><!-- End of picture text -->

The state at time _t_ is: 



<!-- Start of picture text -->
| Ψ( t ) ⟩ = 1 ( e −iϵt / h ¯ |ψ + ⟩ +  e + iϵt / h ¯ |ψ−⟩ )<br>√ 2<br><!-- End of picture text -->

**2. Calculate the Transition Amplitude** _⟨_ Ψ(0) _|_ Ψ( _t_ ) _⟩_ Using the orthonormality of the energy eigenstates ( _⟨ψ_ + _|ψ_ + _⟩_ = _⟨ψ−|ψ−⟩_ = 1 and _⟨ψ_ + _|ψ−⟩_ = 0): 



<!-- Start of picture text -->
⟨ Ψ(0) | Ψ( t ) ⟩ = 1 ( e −iϵt / h ¯ +  e + iϵt / h ¯)<br>2<br><!-- End of picture text -->

: Using the Euler identity cos( _θ_ ) =<sup>_<u>eiθ</u>_</sup><sup><u>+</u></sup> 2<sup>_<u>e−iθ</u>_</sup> 

_⟨_ Ψ(0) _|_ Ψ( _t_ ) _⟩_ = cos _h_ ¯ <u>(</u> _ϵt_ <u>)</u> 

Notes 

2 

**3. Compute the Survival Probability** _P_ ( _t_ ) The probability of finding the system in its initial state _|_ Ψ(0) _⟩_ at time _t_ is: 



<!-- Start of picture text -->
P ( t ) =  |⟨ Ψ(0) | Ψ( t ) ⟩| 2 = cos 2<br>h ¯<br>( ϵt )<br><!-- End of picture text -->

**4. Substitute** _t_ = <u>6</u> _ϵh_ Recall the relationship between Planck’s constant _h_ and the reduced Planck constant _h_ ¯: 



<!-- Start of picture text -->
h  = 2 πh ¯<br><!-- End of picture text -->

Substitute _t_ =<sup>6(2</sup> _ϵ_<sup>_πh_¯)</sup> =<sup><u>12</u></sup> _ϵ_<sup>_<u>πh</u>_¯</sup> into the angle argument: 



<!-- Start of picture text -->
ϵt<br>= 12 π<br>h ¯ = h ¯ ϵ ϵ<br>( 12 πh ¯ )<br><!-- End of picture text -->

Now calculate the probability: 



<!-- Start of picture text -->
P t  = 6 h = cos 2 (12 π ) = (1) 2 =  1<br>ϵ<br>( )<br><!-- End of picture text -->

## **Physical Insight & Oscillation Period** 

1. **Oscillation Frequency (** _ω_ 12 **):** The energy difference between the two states is ∆ _E_ = _E_ + _− E−_ = 2 _ϵ_ . The transition oscillation frequency is: 



<!-- Start of picture text -->
ω = ∆ E = 2 ϵ<br>h ¯ h ¯<br><!-- End of picture text -->

2. **Time Period of Complete Revival (** _T_ **):** 



<!-- Start of picture text -->
T = 2 ω π = 2 2 π ϵ h ¯ = 2 h ϵ<br><!-- End of picture text -->

3. **Given Time:** 



<!-- Start of picture text -->
t  = 6 h = 12 T<br>ϵ = 12 2 ϵ<br>(  h )<br><!-- End of picture text -->

Since _t_ is an exact integer multiple (12) of the fundamental oscillation period _T_ , the quantum state undergoes **12 full cycles** and returns perfectly to its initial state with **100% probability** . 

**Follow-up suggestion:** Would you like to solve a problem on **time-dependent spin precession in a magnetic field (Rabi oscillations)** or practice **matrix calculation of state transition probabilities** next? 

