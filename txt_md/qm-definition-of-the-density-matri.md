<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-definition-of-the-density-matri.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**Correct Answer** 

**Option (b):** 2/3 

## **Detailed Step-by-Step Solution** 

**1. Definition of the Density Matrix for a Mixed State** For a statistical mixture (an incoherent ensemble) of pure quantum states _{|ψi⟩}_ , where each state occurs with classical probability _pi_ (such that<sup>�</sup> _i_<sup>_pi_= 1),thedensityoperator</sup><sup>_ρ_ˆisdefinedas:</sup> 



<!-- Start of picture text -->
ρ ˆ = � pi|ψi⟩⟨ψi|<br>i<br><!-- End of picture text -->

**2. Construction of the Density Matrix** Given: 

- State _|ψ_ 1 _⟩_ = _|_ 1 _⟩_ with probability _p_ 1 =<sup><u>1</u></sup> 3 

- • State _|ψ_ 2 _⟩_ = _|_ 2 _⟩_ with probability _p_ 2 =<sup><u>2</u></sup> 3 

Assuming _{|_ 1 _⟩, |_ 2 _⟩}_ forms an orthonormal basis ( _⟨i|j⟩_ = _δij_ ), the density operator is: 



<!-- Start of picture text -->
ρ ˆ = 3 1 | 1 ⟩⟨ 1 |  + 2 3 | 2 ⟩⟨ 2 |<br><!-- End of picture text -->

In matrix representation using the basis _{|_ 1 _⟩, |_ 2 _⟩}_ : 



<!-- Start of picture text -->
ρ  = ⟨ 1 |ρ ˆ | 2 ⟩ = 0<br>� ⟨⟨ 21 ||ρρ ˆˆ || 11 ⟩⟩ ⟨ 2 |ρ ˆ | 2 ⟩ � �1/30 2/3�<br><!-- End of picture text -->

**3. Evaluating the Diagonal Element** _ρ_ 22 The matrix element _ρ_ 22 is given by: 



<!-- Start of picture text -->
ρ 22 =  ⟨ 2 |ρ ˆ | 2 ⟩ = 1 + 2 = 2<br>3 � ⟨ 2 | 1 �� ⟩⟨ 1 | 2 � ⟩ 3 � ⟨ 2 | 2 �� ⟩⟨ 2 | 2 � ⟩ 3<br>0 1<br><!-- End of picture text -->

Notes 

2 

## **Evaluation of Options** 

- **Option (a):** 1/3 _→_ Incorrect (this is the diagonal element _ρ_ 11, representing the population of state _|_ 1 _⟩_ ). 

- **Option (b):** 2/3 _→_ **CORRECT!** 

- **Option (c):** 1/2 _→_ Incorrect. 

- **Option (d):** 1 _→_ Incorrect (this would be the total trace Tr( _ρ_ ) = _ρ_ 11 + _ρ_ 22). 

## **Key Takeaways & Density Matrix Essentials** 

1. **Populations vs. Coherences:** 

   - **Diagonal Elements (** _ρii_ **):** Represent the **populations** (the probability of finding the system in state _|i⟩_ ). Here, _ρ_ 11 = 1/3 and _ρ_ 22 = 2/3. 

   - **Off-Diagonal Elements (** _ρij_ **for** _i̸_ = _j_ **):** Represent **quantum coherences** (phase relationships between states). For a statistical mixture of basis states, _ρ_ 12 = _ρ_ 21 = 0. 

2. **Normalization (Trace Condition):** 

- The sum of diagonal elements must equal 1: Tr( _ρ_ ) = _ρ_ 11 + _ρ_ 22 =<sup><u>1</u></sup> 3<sup>+</sup><sup><u>2</u></sup> 3<sup>= 1.</sup> 

- 3. **Purity Test:** 

   - For a pure state: Tr( _ρ_<sup>2</sup> ) = 1. 

   - For this mixed state: Tr( _ρ_<sup>2</sup> ) = (1/3)<sup>2</sup> + (2/3)<sup>2</sup> =<sup><u>1</u></sup> 9<sup>+</sup><sup><u>4</u></sup> 9<sup>=</sup> **9**<sup>**<u>5</u>**</sup><sup>_<_</sup><sup>**1**,confirmingit</sup> is a mixed state. 

Would you like to practice calculating the **purity Tr** ( _ρ_<sup>2</sup> ) or **von Neumann entropy** _S_ = _−_ **Tr** ( _ρ_ ln _ρ_ ) for mixed density matrices next? 

