<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-relative-global-phase.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

In quantum mechanics, phase refers to the complex angle _θ_ in a term _e_<sup>_iθ_</sup> . The distinction between **global phase** and **relative phase** is one of the most fundamental concepts in quantum state description: **a global phase is completely unobservable and physically meaningless, whereas a relative phase is physically measurable and dictates quantum interference.** 

## **1. Global Phase** 

**Definition** A **global phase** occurs when the _entire_ state vector _|ψ⟩_ of a quantum system is multiplied by a single complex phase factor _e_<sup>_iθ_</sup> (where _θ_ is a real number): 



<!-- Start of picture text -->
|ψ ′ ⟩ =  e iθ |ψ⟩<br><!-- End of picture text -->

**Why Global Phase Has NO Physical Effect** In quantum mechanics, all physically observable predictions—such as expectation values, probability distributions, and density matrices—remain completely identical whether you use _|ψ⟩_ or _e_<sup>_iθ_</sup> _|ψ⟩_ : 

1. **Expectation Values Are Unchanged:** For any physical observable represented by a Hermitian operator _A_<sup>ˆ</sup> , the expectation value in state _|ψ_<sup>_′_</sup> _⟩_ is: 

   - _⟨ψ_<sup>_′_</sup> _|A_<sup>ˆ</sup> _|ψ_<sup>_′_</sup> _⟩_ = ( _⟨ψ|e_<sup>_−iθ_)</sup> _A_<sup>ˆ</sup> ( _e_<sup>_iθ_</sup> _|ψ⟩_ ) = _e_<sup>_−iθ_</sup> _e_<sup>_iθ_</sup> _⟨ψ|A_<sup>ˆ</sup> _|ψ⟩_ = _⟨ψ|A_<sup>ˆ</sup> _|ψ⟩_ 

2. **Measurement Probabilities Are Unchanged:** The probability of measuring an eigenvalue corresponding to state _|ϕ⟩_ is: 



<!-- Start of picture text -->
P =  |⟨ϕ|ψ ′ ⟩| 2 =  |⟨ϕ|e iθ ψ⟩| 2 =  |e iθ | 2 |⟨ϕ|ψ⟩| 2 =  |⟨ϕ|ψ⟩| 2<br><!-- End of picture text -->

3. **Density Matrix Is Identical:** 



<!-- Start of picture text -->
ρ ˆ ′ =  |ψ ′ ⟩⟨ψ ′ |  =  e iθ |ψ⟩⟨ψ|e −iθ =  |ψ⟩⟨ψ|  = ρ ˆ<br><!-- End of picture text -->

Because multiplying by _e_<sup>_iθ_</sup> changes nothing physical, _|ψ⟩_ and _e_<sup>_iθ_</sup> _|ψ⟩_ represent the **exact same physical state** (a single “ray” in Hilbert space). 

Notes 

2 

## **2. Relative Phase** 

**Definition** A **relative phase** occurs when there is a phase difference between different orthogonal components in a **superposition state** . 

Consider a two-level state: 



<!-- Start of picture text -->
|ψ⟩ =  c 1 | 1 ⟩ +  c 2 | 2 ⟩<br><!-- End of picture text -->

Expressing the complex coefficients in polar form ( _c_ 1 = _|c_ 1 _|e_<sup>_iϕ_1</sup> and _c_ 2 = _|c_ 2 _|e_<sup>_iϕ_2</sup> ): 



<!-- Start of picture text -->
|ψ⟩ =  |c 1 |e iϕ 1 | 1 ⟩ +  |c 2 |e iϕ 2 | 2 ⟩ =  e iϕ 1 ( |c 1 || 1 ⟩ +  |c 2 |e i ( ϕ 2 −ϕ 1) | 2 ⟩ )<br><!-- End of picture text -->

- _e_<sup>_iϕ_1</sup> is a **global phase** factor for the whole state (can be ignored). 

- ∆ _ϕ_ = _ϕ_ 2 _− ϕ_ 1 is the **relative phase** between component _|_ 1 _⟩_ and component _|_ 2 _⟩_ . 

**Why Relative Phase IS Physically Observable** Changing the relative phase ∆ _ϕ_ transforms the state into a **physically distinct, non-identical quantum state** . 

**Concrete Example (Qubit System):** Compare two quantum states with the same component magnitudes but different relative phases (∆ _ϕ_ = 0 vs ∆ _ϕ_ = _π_ ): 



<!-- Start of picture text -->
|ψ + ⟩ = 1 (relative phase ∆ ϕ  = 0)<br>√ 2 | 0 ⟩ + √ 1 2 | 1 ⟩<br>|ψ−⟩ = 1 (relative phase ∆ ϕ  =  π )<br>√ 2 | 0 ⟩− √ 1 2 | 1 ⟩ = √ 1 2 | 0 ⟩ + √ eiπ 2 | 1 ⟩<br><!-- End of picture text -->

- **Measurement in** _{|_ 0 _⟩, |_ 1 _⟩}_ **Basis:** 



<!-- Start of picture text -->
Both states give a 50% chance of measuring | 0 ⟩ and a 50% chance of measuring | 1 ⟩ .<br>• Measurement in the Superposition Basis | + ⟩ = | 0 ⟩ √ + 2 | 1 ⟩ and |−⟩ = | 0 ⟩ √ − 2 | 1 ⟩ :<br><!-- End of picture text -->



<!-- Start of picture text -->
– For |ψ + ⟩ : P ( | + ⟩ ) =  |⟨ + |ψ + ⟩| 2 =  100 %<br>– For |ψ−⟩ : P ( | + ⟩ ) =  |⟨ + |ψ−⟩| 2 =  0 % (and P ( |−⟩ ) = 100%)<br><!-- End of picture text -->

The two states are **orthogonal** ( _⟨ψ_ + _|ψ−⟩_ = 0) and can be distinguished experimentally with 100% certainty! 

## **3. Role of Relative Phase in Time Evolution & Interference** 

As we explored in our discussion on stationary vs non-stationary states: If _|_ 1 _⟩_ and _|_ 2 _⟩_ are energy eigenstates with different energy eigenvalues _E_ 1 _̸_ = _E_ 2, the time evolution introduces a time-dependent relative phase: 



<!-- Start of picture text -->
i (∆ ϕ− ( E 2 − h ¯ E 1) t )<br>|ψ ( t ) ⟩ =  |c 1 || 1 ⟩ +  |c 2 |e | 2 ⟩<br><!-- End of picture text -->

This continuously changing relative phase causes the probability cloud _|_ Ψ( **r** _, t_ ) _|_<sup>2</sup> to oscillate in time at the Bohr frequency _ω_ =<sup>_<u>E</u>_</sup><sup><u>2</u></sup><sup>_−_</sup> _h_ ¯<sup>_<u>E</u>_</sup><sup><u>1</u></sup> , producing **quantum beats** and **constructive/destructive interference** . 

Notes 

3 

## **Summary Comparison** 

|Property|Global Phase (_e_<sup>_iθ_</sup>_|ψ⟩_)|Relative Phase<br>(_c_1_|_1_⟩_+_c_2_e_<sup>_i_∆</sup><sup>_ϕ_</sup>_|_2_⟩_)|
|---|---|---|
|**Applies To**|The **entire** state vector<br>equally.|The **difference** between<br>components in a<br>superposition.|
|**Physical Effect**|**None** (unobservable).|**Major** (creates distinct<br>quantum states).|
|**Probabilities**|Leaves all measurement<br>probabilities unchanged.|Alters measurement<br>probabilities in non-diagonal<br>bases.|
|**Interference**|Does not produce<br>interference.|Governs **constructive**<br>**vs. destructive**<br>**interference**.|



Would you like to see how relative phase shifts are generated in real physical experiments— such as via magnetic vector potentials ( **Aharonov-Bohm Effect** ), geometric paths ( **Berry’s Phase** ), or quantum computing logic gates? 

