<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-einstein-temperature-lattice-oscillations-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

The **Einstein Model of Heat Capacity** (1907) was a groundbreaking triumph because it was the first theory to apply quantum mechanics to lattice vibrations, explaining why classical physics (the Dulong-Petit Law) failed at low temperatures. 

Here is the complete physical breakdown, mathematical derivation, and explanation of why it fails at low temperatures. 

## **1. Historical Context: The Classical Failure** 

Before Einstein, classical statistical mechanics used the **Equipartition Theorem** , which stated that every 1D harmonic oscillator has an average thermal energy of _⟨E⟩_ = _kBT_ . 

For a 3D solid with _N_ atoms (3 _N_ independent vibrational degrees of freedom), the total internal energy was: 

_U_ = 3 _NkBT_ = 3 _RT_ 

Differentiating with respect to temperature gives the classical **Dulong-Petit Law** : 



<!-- Start of picture text -->
CV = = 3 R ≈ 24 . 9 J/mol  ·  K<br>( ∂U∂T ) V<br><!-- End of picture text -->

While Dulong-Petit works well near room temperature for most solids, experiments in the late 19th century revealed that as _T →_ 0 K, the specific heat _CV →_ 0. Classical physics had no way to explain why heat capacity disappears at low temperatures. 

## **2. The Key Assumptions of Einstein’s Model (1907)** 

Albert Einstein realized that the problem lay in assuming energy is continuous ( _kBT_ ). Applying Max Planck’s quantum hypothesis (1900), Einstein made three central assumptions: 

1. 3 _N_ **Independent Oscillators:** A solid of _N_ atoms behaves like 3 _N_ independent, 1D quantum harmonic oscillators. 

2. **Single Fixed Frequency (** _ωE_ **):** All 3 _N_ oscillators vibrate at the **exact same characteristic frequency** _ωE_ (the _Einstein frequency_ ). 

Notes 

2 

3. **Quantized Energy:** Oscillator energies are restricted to discrete quantum steps of _hω_ ¯ _E_ : 



<!-- Start of picture text -->
En = n  + 1 hω ¯ E, n  = 0 ,  1 ,  2 , . . .<br>2<br>( )<br><!-- End of picture text -->

## **3. Mathematical Derivation of** _CV_ 

**Step A: Average Energy per Oscillator** Using Planck/Bose-Einstein quantum statistics, the average thermal excitation number of phonons at temperature _T_ is given by the Planck distribution: 



<!-- Start of picture text -->
1<br>⟨n⟩ =<br>e hω ¯ E / kBT − 1<br><!-- End of picture text -->

Ignoring the temperature-independent ground-state zero-point energy (<sup><u>1</u></sup> 2<sup>_hω_¯</sup><sup>_E_),thether-</sup> mal energy of a single oscillator is: 



<!-- Start of picture text -->
hω ¯ E<br>⟨E⟩ =<br>e hω ¯ E / kBT − 1<br><!-- End of picture text -->

**Step B: Total Internal Energy (** _U_ **)** Multiplying by the 3 _N_ vibrational modes: 



<!-- Start of picture text -->
hω ¯ E<br>U = 3 N ⟨E⟩ = 3 N<br>e hω ¯ E / kBT − 1<br><!-- End of picture text -->

For 1 mole of a solid ( _N_ = _NA_ , where _NAkB_ = _R_ ). We define the **Einstein Temperature (** _θE_ **)** as the characteristic thermal energy threshold of the material: 



<!-- Start of picture text -->
θE ≡ hω ¯ E<br>kB<br><!-- End of picture text -->

Rewriting _U_ in terms of _θE_ : 



<!-- Start of picture text -->
1<br>U = 3 RθE<br>e θE / T − 1<br><!-- End of picture text -->

**Step C: Differentiating to find** _CV_ = ( _<u>∂U∂T</u>_ ) _V_ Using the chain rule: 



<!-- Start of picture text -->
3 RθE 1<br>− − θE<br>CV = ∂ = 3 RθE ·<br>∂T [ e θE / T − 1 ] [ ( e θE / T − 1) 2 · eθE / T · ( T 2 )]<br>e θE / T<br>CV = 3 R<br>T<br>( θE )2 ( e θE / T − 1) 2<br><!-- End of picture text -->

Notes 

3 

## **4. Analysis of the Two Temperature Regimes** 

**A. High-Temperature Limit (** _T ≫ θE_ = _⇒_ _<u>θTE</u>_<sup>_≪_1</sup><sup>**)**</sup> When the temperature is high, thermal energy _kBT_ is far larger than the quantum step ¯ _hωE_ . Using the Taylor expansion _e_<sup>_x_</sup> _≈_ 1 + _x_ (where _x_ = _θE_ / _T_ ): 



<!-- Start of picture text -->
e θE / T − 1  ≈ θE<br>T<br><!-- End of picture text -->

Substitute this back into the heat capacity equation: 



<!-- Start of picture text -->
1<br>CV ≈ 3 R (Dulong-Petit Law)<br>T<br>( θE )2<br>( θTE ) 2 =  3R<br><!-- End of picture text -->

- **Physics Insight:** At high temperatures, the discrete energy gap _hω_ ¯ _E_ is negligible compared to _kBT_ . Quantum effects wash out, recovering classical physics. 

**B. Low-Temperature Limit (** _T ≪ θE_ = _⇒_ _<u>θTE</u>_<sup>_≫_1</sup><sup>**)**</sup> At low temperatures, _e_<sup>_θE_/</sup><sup>_T_</sup> _≫_ 1, so ( _e_<sup>_θE_/</sup><sup>_T_</sup> _−_ 1)<sup>2</sup> _≈ e_<sup>2</sup><sup>_θE_/</sup><sup>_T_</sup> . 

Simplifying the equation: 



<!-- Start of picture text -->
CV ≈ 3 R e −θE / T<br>T e 2 θE / T = 3 R T<br>( θE )2 eθE / T ( θE )2<br><!-- End of picture text -->

Because the decaying exponential _e_<sup>_−θE_/</sup><sup>_T_</sup> decreases much faster than any power term ( _θE_ / _T_ )<sup>2</sup> grows, the exponential term dominates: 



<!-- Start of picture text -->
CV ∝ e −θ E / T → 0 as T  → 0 K<br><!-- End of picture text -->

- **Physics Insight (“Freezing Out” of Modes):** At low temperatures ( _kBT ≪ hω_ ¯ _E_ ), thermal collisions lack the energy needed to supply even a single quantum step _hω_ ¯ _E_ . The vibrational modes freeze in their ground state, making the lattice incapable of absorbing heat, so _CV →_ 0. 

## **5. Why Einstein’s Model Fails at Low Temperatures** 

Although Einstein correctly proved that quantum mechanics forces _CV →_ 0, **the rate at which** _CV_ **approaches zero was experimentally wrong** : 

- **Einstein Model Prediction:** _CV ∝ e_<sup>_−θE_/</sup><sup>_T_</sup> (Exponential decay) 

- **Experimental Measurements:** _CV ∝ T_<sup>3</sup> (Power-law decay, the Debye _T_<sup>3</sup> law) 

## **The Fundamental Flaw:** 

1. **The Single Frequency Assumption:** Einstein assumed _all_ 3 _N_ modes oscillate at a single fixed frequency _ωE_ . 

Notes 

4 

2. **Neglecting Long-Wavelength Sound Waves:** In a real solid, atoms are elastic networks. Waves propagating through the lattice (acoustic phonons) can have arbitrarily long wavelengths ( _λ →∞_ ), which means **arbitrarily low frequencies (** _ω →_ 0 **)** . 

3. **Why Low-Frequency Modes Matter:** No matter how cold the crystal gets ( _T →_ 0), there are **always** acoustic modes with small enough energy steps ¯ _hω < kBT_ that can still be excited thermally. 

4. Because Einstein imposed an artificial energy threshold _hω_ ¯ _E_ , his model made _CV_ drop off **much too rapidly** compared to real solids. 

## **6. Modern Application of the Einstein Model** 

The Einstein model is **not obsolete** ! While the **Debye model** (elastic continuum) correctly describes low-frequency **acoustic phonons** ( _CV ∝ T_<sup>3</sup> ), the **Einstein model is still used today to describe optical phonons** in complex crystals (e.g., optical branches in NaCl or GaAs), where the dispersion curve is nearly flat ( _ω ≈_ constant)! 

