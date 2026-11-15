<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: nuc-liquid-drop-model-mass-formula.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Welcome to **Section 10: Nuclear and Particle Physics** for GATE! 

Just as we mastered Solid State Physics, we will break down Nuclear and Particle Physics into **5 high-yield modules** , focusing on core physical intuition, exact mathematical frameworks, GATE examiner traps, and step-by-step solved numerical problems. 

### **Master Roadmap: Nuclear & Particle Physics** 

┌─────────────────────────────────────────────────────────────────────────┐ │Module 1: Nuclear Properties, Liquid Drop Model & SEMF │ ├─────────────────────────────────────────────────────────────────────────┤ │Module 2: Nuclear Models (Shell Model) & Electromagnetic Moments │ ├─────────────────────────────────────────────────────────────────────────┤ │Module 3: Nuclear Forces & Radioactive Decays ( _α_ , _β_ , _γ_ Selection Rules) │ ├─────────────────────────────────────────────────────────────────────────┤ │Module 4: Nuclear Reactions, Scattering, Fission/Fusion & Detectors │ ├─────────────────────────────────────────────────────────────────────────┤ │Module 5: Particle Physics, Quark Model & Discrete Symmetries (C,P,T,G) │ └─────────────────────────────────────────────────────────────────────────┘ 

## **Module 1: Nuclear Properties, Liquid Drop Model & SEMF** 

**1. Core Theory & Physical Intuition** 

   1. **Nuclear Scale & Density Saturation:** 

      - Nuclei are bound states of _Z_ protons and _N_ = _A − Z_ neutrons. 

      - The nuclear charge and matter radius scale as: 

_R_ = _R_ 0 _A_<sup>1/3</sup> ( _R_ 0 _≈_ 1 _._ 2 to 1 _._ 25 fm) 

- Because nuclear volume scales as _V ∝ R_<sup>3</sup> _∝ A_ , the central nuclear matter density _ρ_ 0 _≈_ 0 _._ 17 nucleons/fm<sup>3</sup> _≈_ 2 _._ 3 _×_ 10<sup>17</sup> kg/m<sup>3</sup> is **constant for almost** 

Notes 

2 

**all nuclei** . This constant density is the primary physical evidence that nuclear forces **saturate** (each nucleon interacts only with its immediate neighbors). 2. **Mass Defect & Binding Energy (** _B_ **):** 

- The rest mass of a bound nucleus _M_ ( _A, Z_ ) is always less than the sum of its free constituent nucleons. This missing mass equivalent is the **Binding Energy (** _B_ **)** : 



<!-- Start of picture text -->
B ( A, Z ) = [ Zmp  + ( A − Z ) mn − M nucleus( A, Z )]  c 2<br><!-- End of picture text -->

- Expressed using neutral atomic masses _M_ atom( _A, Z_ ) and hydrogen atom mass _M_ (<sup>1</sup> H) (where electron rest masses _Zme_ cancel out): 



<!-- Start of picture text -->
B ( A ,  Z ) = [ ZM ( 1 H) + ( A  − Z ) mn  − M atom( A ,  Z )] c 2<br><!-- End of picture text -->

### **2. Mathematical Framework: The Semi-Empirical Mass Formula (SEMF)** 

The **Weizsäcker Liquid Drop Model** treats the nucleus as an incompressible, charged fluid droplet, leading to five distinct energy terms: 



<!-- Start of picture text -->
Z ( Z − 1) ( A − 2 Z ) 2<br>B ( A, Z ) =  avA − asA 2/3 − ac − a sym +  δ ( A, Z )<br>A 1/3 A<br>B/A (MeV/nucleon)<br>8.8 | ^ 56Fe (Peak ~ 8.8 MeV)<br>| / \____________________ Heavy Nuclei (Fission)<br>8.0 | /<br>| /<br>6.0 | /<br>| / Light Nuclei (Fusion)<br>0.0 +----+-----------------------------------------> A<br>20 56 100 200<br><!-- End of picture text -->

### **Detailed Breakdown of SEMF Terms:** 

|Term|Algebraic Form|Physical Origin|Typical Value|
|---|---|---|---|
|**1. Volume Term**|+_avA_|Nearest-neighbor<br>attractive strong<br>force (saturation).|_av ≈_15_._5 MeV|
|**2. Surface Term**|_−asA_<sup>2/3</sup>|Nucleons on the<br>surface have fewer<br>neighbors (surface<br>tension).|_as ≈_16_._8 MeV|
|**3. Coulomb Term**|_−ac_<br>_Z_(_Z−_1)<br>_A_<sup>1/3</sup>|Electrostatic<br>repulsion between<br>_Z_(_Z −_1)/2 proton<br>pairs.|_ac ≈_0_._72 MeV|



Notes 

3 

|Term|Algebraic Form|Physical Origin|Typical Value|
|---|---|---|---|
|**4. Asymmetry**<br>**Term**|_−a_sym<br>(_A−_2_Z_)<sup>2</sup><br>_A_|Pauli exclusion<br>principle forces excess<br>neutrons into higher<br>energy states.|_a_sym _≈_23_._0 MeV|
|**5. Pairing Term**|+_δ_(_A, Z_)|Quantum<br>spin-pairing of<br>identical nucleons<br>into _J_ = 0<sup>+ </sup>pairs.|_ap ≈_34 MeV|





<!-- Start of picture text -->
+ apA − 3/4 for Even- Z, Even- N (Even- A , Most Stable)<br>δ ( A, Z ) = 0 for Odd- A (Even- Z /Odd- N or Odd- Z /Even- N )<br><br> −apA − 3/4 for Odd- Z, Odd- N (Even- A , Least Stable)<br><!-- End of picture text -->

### **3. Derivation Milestones & Applications** 

**A. Parabola of Stable Isobars (** _Z_ 0 **)** For a fixed mass number _A_ , atomic mass _M_ ( _A, Z_ ) plotted against _Z_ forms a parabola. To find the **most stable isobar** ( _Z_ 0) that minimizes mass _M_ ( _A, Z_ ) (or maximizes _B_ ( _A, Z_ )): 



<!-- Start of picture text -->
∂M ( A, Z )<br>= 0 = ⇒ ∂B ( A, Z ) = 0<br>∂Z ∂Z<br><!-- End of picture text -->

Differentiating the Coulomb and Asymmetry terms with respect to _Z_ : 



<!-- Start of picture text -->
∂ Z 2 ( A − 2 Z ) 2<br>∂Z [ −ac A 1/3 − a sym A ] = 0<br>− 2 acZ<br>= 0<br>A 1/3 + 4 a sym( A A  − 2 Z )<br><!-- End of picture text -->

Solving for _Z_ 0 gives: 



<!-- Start of picture text -->
A A<br>Z0 =<br>ac 2  +  0 . 015A 2 / 3<br>2  + A 2 / 3 ≈<br>( 2a sym )<br><!-- End of picture text -->

- **Light Nuclei (** _A ≪_ 40 **):** _Z_ 0 _≈ A_ /2 ( _N_ = _Z_ ). 

- **Heavy Nuclei (** _A >_ 100 **):** _Z_ 0 _< A_ /2 ( _N > Z_ ), as extra neutrons are needed to dilute Coulomb repulsion without adding electrostatic energy. 

**B. Spontaneous Fission Condition** Deforming a spherical nucleus into a prolate ellipsoid ( _a_ = _R_ (1 + _ϵ_ ), _b_ = _R_ (1 _− ϵ_ /2)) changes the surface area ( _S ∝_ 1 + 5<sup><u>2</u></sup><sup>_ϵ_2)and</sup> Coulomb self-energy ( _Ec ∝_ 1 _−_<sup><u>1</u></sup> 5<sup>_ϵ_2).</sup> 

Notes 

4 

The net energy change is: 



<!-- Start of picture text -->
Z 2<br>∆ E = ∆ Es  + ∆ Ec = ϵ 2<br>( 25 asA 2/3  − 1 5 ac A 1/3 )<br><!-- End of picture text -->

Spontaneous fission becomes energetically favorable (∆ _E <_ 0) when: 



<!-- Start of picture text -->
1 Z 2<br>≈ 45 to 50<br>5 ac A 1/3 ≥ 2 5 asA 2/3 = ⇒ Z A 2 ≥ 2a ac s<br><!-- End of picture text -->

### **4. GATE Exam Traps & Crucial Pitfalls** 

1. **Mass Defect Unit Trap:** In GATE questions, atomic masses are given in atomic mass units (u). Always use _c_<sup>2</sup> = 931 _._ 5 MeV/u directly. Do not convert u to kg first! 

2. **Atomic vs. Nuclear Mass Inconsistency:** When calculating _B_ , if you use _M_ (<sup>1</sup> H) = 1 _._ 007825 u, you **must** use the neutral atomic mass _M_ atom( _A, Z_ ). If you use _mp_ = 1 _._ 007276 u, you must use the bare nuclear mass _M_ nucleus( _A, Z_ ). Mixing them introduces a systematic error of _Zme_ . 

3. **Coulomb Term Approximation:** Check whether the question writes the Coulomb term as _Z_ ( _Z −_ 1)/ _A_<sup>1/3</sup> or _Z_<sup>2</sup> / _A_<sup>1/3</sup> . For heavy nuclei ( _Z ≫_ 1), _Z_ ( _Z −_ 1) _≈ Z_<sup>2</sup> , but for light nuclei, _Z_ ( _Z −_ 1) must be evaluated strictly. 

4. **Sign Errors in Pairing Term (** _δ_ **):** 

   - **Even-Even (** _Z_ **even,** _N_ **even):** _δ_ is **Positive** (+ _apA_<sup>_−_3/4</sup> ) = _⇒_ increases _B_ , lowers mass. 

   - **Odd-Odd (** _Z_ **odd,** _N_ **odd):** _δ_ is **Negative** ( _−apA_<sup>_−_3/4</sup> ) = _⇒_ decreases _B_ , raises mass. 

   - **Odd-** _A_ **:** _δ_ = 0. 

### **5. Classic Solved GATE Numerical Problem** 

**Problem:** Consider an isobaric chain of mass number _A_ = 125. Given the SEMF coefficients _ac_ = 0 _._ 72 MeV and _a_ sym = 23 _._ 0 MeV: 

1. Calculate the atomic number _Z_ 0 of the most stable isobar. 

2. Determine whether<sup>125</sup> 52<sup>Teisstableagainst</sup><sup>_β_-decay.</sup> 

### **Step-by-Step Solution:** 

1. **Calculate** _Z_ 0 **using the derived formula:** 



<!-- Start of picture text -->
A<br>Z 0 =<br>2 + ac A 2/3<br>( 2 a sym )<br><!-- End of picture text -->

- _A_<sup>2/3</sup> = (125)<sup>2/3</sup> = 25 

- _<u>ac</u>_ <u>0</u> _<u>.</u>_ <u>72</u> 

- 2 _a_ sym<sup>=</sup> 2 _×_ 23 _._ 0<sup>=</sup><sup><u>0</u></sup> 46<sup>_<u>.</u>_</sup><sup><u>72</u></sup> _._ 0<sup>_≈_0</sup><sup>_._01565</sup> 

- Denominator: 2 + (0 _._ 01565 _×_ 25) = 2 + 0 _._ 3913 = 2 _._ 3913 

Notes 

5 



<!-- Start of picture text -->
125<br>Z 0 = 2 . 3913 ≈ 52 . 27<br><!-- End of picture text -->

2. **Rounding to the nearest integer:** 



<!-- Start of picture text -->
Z0 =  52<br><!-- End of picture text -->

3. **Conclusion:** The most stable isobar for _A_ = 125 is _Z_ = 52, which corresponds to Tellurium (<sup>125</sup> 52<sup>Te).Therefore,125</sup> 52<sup>Tesitsatthebottomofthemassparabolaandis</sup> **completely stable against** _β_ **-decay** . 

### **Next Steps** 

Shall we move on to **Module 2: Nuclear Shell Model, Spin-Orbit Coupling,** _J_<sup>Π</sup> **Assignments, and Schmidt Magnetic Limits** , or would you like a Python script to visualize the **Isobaric Mass Parabolas for Even-** _A_ **vs. Odd-** _A_ **nuclei** first? 

