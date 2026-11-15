<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-made-option-detailed.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **Correct Answer** 

**Option (a):** **<u>76</u>**<sup>**h**¯</sup><sup>_ω_</sup> 

## **Detailed Step-by-Step Solution** 

**1. Check Normalization of the State** The given wavefunction at _t_ = 0 is a superposition of the stationary energy eigenstates _|n⟩_ : 



<!-- Start of picture text -->
|ψ (0) ⟩ =  c 0 | 0 ⟩ +  c 1 | 1 ⟩ +  c 2 | 2 ⟩ = √ 1 2 | 0 ⟩ + √ 1 3 | 1 ⟩ + √ 1 6 | 2 ⟩<br><!-- End of picture text -->

The probability _Pn_ of finding the oscillator in state _|n⟩_ is given by _|cn|_<sup>2</sup> : 



<!-- Start of picture text -->
2<br>• Ground State ( n  = 0 ): P 0 =  |c 0 | 2 = ��� √ 12 ��� = 1 2<br>2<br>• First Excited State ( n  = 1 ): P 1 =  |c 1 | 2 = ��� √ 13 ��� = 1 3<br>2<br>• Second Excited State ( n  = 2 ): P 2 =  |c 2 | 2 = ��� √ 16 ��� = 1 6<br><!-- End of picture text -->

**Check total probability:** 



<!-- Start of picture text -->
P total =  P 0 +  P 1 +  P 2 = 2 1 + 1 3 + 1 6 = 3 + 2 + 1 6 = 6 6 = 1<br><!-- End of picture text -->

_(The state vector is properly normalized)_ . 

**2. Energy Eigenvalues of a 1D Harmonic Oscillator** The energy eigenvalues of a 1D harmonic oscillator are given by: 



<!-- Start of picture text -->
En = n  + 1 hω, ¯ n  = 0 ,  1 ,  2 ,  3 , . . .<br>2<br>� �<br><!-- End of picture text -->

- _E_ 0 **(for** _n_ = 0 **):** _E_ 0 =<sup><u>1</u></sup> 2<sup>_hω_¯</sup> 

- • _E_ 1 **(for** _n_ = 1 **):** _E_ 1 =<sup><u>3</u></sup> 2<sup>_hω_¯</sup> • _E_ 2 **(for** _n_ = 2 **):** _E_ 2 =<sup><u>5</u></sup> 2<sup>_hω_¯</sup> 

Notes 

2 

**3. Calculate the Average Energy** _⟨E⟩_ The expectation value (average energy) is the probability-weighted sum of the energy eigenvalues: 



<!-- Start of picture text -->
⟨E⟩ = � PnEn =  P 0 E 0 +  P 1 E 1 +  P 2 E 2<br>n<br>⟨E⟩ = + +<br>� 12 �� 21 hω ¯ � � 13 �� 23 hω ¯ � � 61 �� 25 hω ¯ �<br>⟨E⟩ = ¯ hω<br>4 + 1 2 + 12 5<br>� 1 �<br><!-- End of picture text -->

Convert to a common denominator of 12: 



<!-- Start of picture text -->
⟨E⟩ = ¯ hω = 3 + 6 + 5 hω ¯ = 14<br>12 + 12 6 + 12 5 12 12 hω ¯ = 7 6 h ¯ ω<br>� 3 �<br><!-- End of picture text -->

## **Evaluation of Options** 

- **Option (a):** **<u>76</u>**<sup>**h**¯</sup><sup>_ω→_</sup><sup>**CORRECT!**</sup> 

- • **Option (b):** <u>43</u><sup>_hω_¯</sup><sup>_→_</sup><sup>**Incorrect**</sup> • **Option (c):** <u>32</u><sup>_hω_¯</sup><sup>_→_</sup><sup>**Incorrect**</sup> • **Option (d):** <u>53</u><sup>_hω_¯</sup><sup>_→_</sup><sup>**Incorrect**</sup> 

## **Key Concepts & Formulae to Remember for GATE** 

**1. Time Independence of** _⟨E⟩_ Because the Hamiltonian _H_<sup>ˆ</sup> is time-independent, the energy expectation value **is constant in time** : 



<!-- Start of picture text -->
d⟨E⟩ = 0 = ⇒⟨E ( t ) ⟩ =  ⟨E (0) ⟩ = 7<br>dt 6 hω ¯<br><!-- End of picture text -->

Even though the wavefunction evolves as _|ψ_ ( _t_ ) _⟩_ =<sup>�</sup> _cne_<sup>_−iEnt_/</sup><sup>_h_¯</sup> _|n⟩_ , the probabilities _Pn_ = _|cne_<sup>_−iEnt_/</sup><sup>_h_¯</sup> _|_<sup>2</sup> = _|cn|_<sup>2</sup> do not change with time. 

**2. Quick Check for Harmonic Oscillator Superposition States** When given _|ψ⟩_ =<sup>�</sup> _cn|n⟩_ : 

   1. Always confirm<sup>�</sup> _|cn|_<sup>2</sup> = 1. If not, divide by ~~��~~ _|cn|_ 2. 

   2. Compute _⟨n⟩_ =<sup>�</sup> _nPn_ . 

   3. Use the shortcut: 



<!-- Start of picture text -->
⟨E⟩ = ⟨n⟩ + 1 hω ¯<br>2<br>� �<br>• For this problem: ⟨n⟩ = 0 � 21 � + 1 � 13 � + 2 � 16 � = 0 + 1 3 + 2 6 = 2 3 .<br>• Therefore: ⟨E⟩ = � 23 + 2 1 � hω ¯ = 7 6 h ¯ ω .<br><!-- End of picture text -->

Notes 

3 

**Follow-up suggestion:** Would you like to practice calculating the **uncertainty in energy** ∆ _E_ = ~~�~~ _⟨E_<sup>2</sup> _⟩−⟨E⟩_<sup>2</sup> for this state, or tackle a problem on **ladder operators (** _a, a_<sup>_†_</sup> **)** next? 

