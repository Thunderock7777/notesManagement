<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: stat-thermodynamics-and-statistical-mechanics.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

GATE PHYSICS 

THERMODYNAMICS & PHASE TRANSITIONS 

# **GATE PHYSICS STUDY NOTES Thermodynamics, Potentials, Phase Transitions & Critical Phenomena** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

### **Contents** 

|**1**<br>**Laws of Thermodynamics & Thermodynamic Potentials**|**2**|
|---|---|
|**2**<br>**Maxwell’s Relations & Thermodynamic Coefficients**|**6**|
|**3**<br>**Phase Transitions & Phase Equilibria**|**9**|
|**4**<br>**Critical Phenomena, Scaling Laws & Landau Theory**|**12**|



1 

GATE PHYSICS 

THERMODYNAMICS & PHASE TRANSITIONS 

### **1 Laws of Thermodynamics & Thermodynamic Potentials** 

#### **1. Core Theory** 

Thermodynamics is a phenomenological theory describing the macroscopic properties of systems in thermal equilibrium. 

-  **Zeroth Law (Thermal Equilibrium):** If system _A_ is in thermal equilibrium with system _B_ , and _B_ is in thermal equilibrium with system _C_ , then _A_ is in thermal equilibrium with _C_ . This establishes the existence of a unique state function called **temperature** ( _T_ ). 

-  **First Law (Conservation of Energy):** Energy cannot be created or destroyed, only transformed. For a closed system, the change in internal energy ( _dU_ ) is the sum of the heat added ( _dQ_ ) and the work done on the system ( _dW_ ): 

_dU_ = _dQ_ + _dW_ = _TdS − PdV_ + _µdN_ (1) 

where _S_ is entropy, _V_ is volume, _P_ is pressure, _µ_ is chemical potential, and _N_ is particle number. 

-  **Second Law (Entropy and Direction of Heat Flow):** Entropy ( _S_ ) is a state function. In any spontaneous process, the total entropy of an isolated system must increase or remain constant: 



<!-- Start of picture text -->
dS ≥ dQ (2)<br>T<br><!-- End of picture text -->

This dictates that heat cannot spontaneously flow from a colder to a hotter body without external work. 

-  **Third Law (Nernst’s Theorem):** As the absolute temperature of a system approaches zero ( _T →_ 0), the entropy of a pure crystalline substance in its ground state approaches a universal constant (which can be defined as zero): 



<!-- Start of picture text -->
T lim → 0 S = 0 (3)<br><!-- End of picture text -->

This implies that it is physically impossible to reduce the temperature of any system to absolute zero in a finite number of steps. 

-  **Thermodynamic Potentials:** Macroscopic state functions that characterize the energy state of a system under specific boundary conditions. They represent the maximum amount of work extractable from the system under different constraints. 

#### **2. Mathematical Framework** 

The four primary thermodynamic potentials are related to each other via **Legendre Transformations** , which systematically switch independent variables between conjugate pairs ( _S ↔ T_ and _V ↔ P_ ): 

-  **Internal Energy (** _U_ ( _S, V, N_ ) **):** Represents the total energy of the system. 



<!-- Start of picture text -->
dU =  TdS − PdV +  µdN = ⇒ T = , P =  − , µ  = (4)<br>� ∂U∂S � V,N � ∂V∂U � S,N � ∂N∂U � S,V<br><!-- End of picture text -->

2 

GATE PHYSICS 

THERMODYNAMICS & PHASE TRANSITIONS 

-  **Enthalpy (** _H_ ( _S, P, N_ ) **):** Legendre transform of _U_ with respect to volume ( _V → P_ ): 



<!-- Start of picture text -->
H =  U  +  PV = ⇒ dH =  TdS  +  V dP +  µdN = ⇒ T = , V = (5)<br>� ∂H∂S � P,N � ∂H∂P � S,N<br><!-- End of picture text -->

-  **Helmholtz Free Energy (** _F_ ( _T, V, N_ ) **or** _A_ **):** Legendre transform of _U_ with respect to entropy ( _S → T_ ): 



<!-- Start of picture text -->
F =  U −TS = ⇒ dF =  −SdT −PdV  + µdN = ⇒ S =  − , P =  − (6)<br>� ∂F∂T � V,N � ∂V∂F � T,N<br><!-- End of picture text -->

-  **Gibbs Free Energy (** _G_ ( _T, P, N_ ) **):** Double Legendre transform of _U_ with respect to entropy and volume ( _S → T_ and _V → P_ ): 



<!-- Start of picture text -->
G  =  H −TS =  F  + PV = ⇒ dG  =  −SdT  + V dP  + µdN = ⇒ S =  − , V =<br>� ∂G∂T � P,N � ∂G∂P � T,N<br>(7)<br><!-- End of picture text -->

-  **Grand Potential (** Φ _G_ ( _T, V, µ_ ) **):** Legendre transform of _F_ with respect to particle number ( _N → µ_ ): 



<!-- Start of picture text -->
Φ G =  F − µN =  −PV = ⇒ d Φ G =  −SdT − PdV − Ndµ (8)<br><!-- End of picture text -->

#### **3. Derivation Milestones** 

Let us trace the Legendre transformation deriving Helmholtz Free Energy ( _F_ ) from Internal Energy ( _U_ ): 

1. **Define the Target Variable Change:** We wish to change the independent variable from Entropy ( _S_ ) to Temperature ( _T_ = _∂U/∂S_ ). 

2. **Formulate the Legendre Transform:** Define _F ≡ U − TS_ . 

3. **Differentiate the Transform:** Compute the total differential: 



<!-- Start of picture text -->
dF =  dU − d ( TS ) =  dU − TdS − SdT (9)<br><!-- End of picture text -->

4. **Substitute the First Law:** Substitute _dU_ = _TdS − PdV_ + _µdN_ into the equation: _dF_ = ( _TdS − PdV_ + _µdN_ ) _− TdS − SdT_ = _−SdT − PdV_ + _µdN_ (10) 

This proves that the natural variables of _F_ are indeed _T_ , _V_ , and _N_ . 

3 

GATE PHYSICS 

THERMODYNAMICS & PHASE TRANSITIONS 

#### **4. Problem-Solving Algorithm** 

##### **Using Potentials to Evaluate Equilibrium States** 

1. **Identify the Constraints:** Note which macroscopic variables are held constant: 

   -  Constant _S, V, N_ = _⇒_ Minimize Internal Energy _U_ .  Constant _S, P, N_ = _⇒_ Minimize Enthalpy _H_ .  Constant _T, V, N_ = _⇒_ Minimize Helmholtz Free Energy _F_ .  Constant _T, P, N_ = _⇒_ Minimize Gibbs Free Energy _G_ . 

2. **Write Down Potential Relations:** Use the partial derivatives of the minimized potential to express the target quantities (such as _P, S, V_ ). 



<!-- Start of picture text -->
3. Check Stability Conditions: Ensure the secondary derivatives satisfy thermody-<br>namic stability:<br>≥ 0 = ⇒ κT =  − 1 ≥ 0 (Isothermal compressibility is positive)<br>� ∂V∂ 2 F 2 � T V � ∂V∂P � T<br>(11)<br><!-- End of picture text -->



<!-- Start of picture text -->
≤ 0 = ⇒ CP =  −T ≥ 0 (Constant-pressure heat capacity is positive)<br>� ∂∂T 2 G 2 � P � ∂∂T 2 G 2 � P<br>(12)<br><!-- End of picture text -->

#### **5. Connections to Observables** 



<!-- Start of picture text -->
 Entropy ( S ): Expressed as S =  − � ∂F∂T � V,N =  − � ∂G∂T � P,N .<br> Pressure ( P ): Expressed as P =  − � ∂V∂F � T,N =  − � ∂V∂U � S,N .<br><!-- End of picture text -->

-  **Specific Heat at Constant Volume (** _CV_ **):** 



<!-- Start of picture text -->
CV =  T =  −T (13)<br>� ∂T∂S � V,N � ∂∂T 2 F 2 � V,N<br><!-- End of picture text -->

-  **Specific Heat at Constant Pressure (** _CP_ **):** 



<!-- Start of picture text -->
CP =  T =  −T (14)<br>� ∂T∂S � P,N � ∂∂T 2 G 2 � P,N<br><!-- End of picture text -->

4 

GATE PHYSICS 

THERMODYNAMICS & PHASE TRANSITIONS 

#### **6. Crucial Pitfalls** 

##### **Thermodynamic Potentials Mistakes to Avoid** 

-  **Incorrect Natural Variable Differentiation:** Taking derivatives of potentials with respect to variables that are not their natural variables without keeping other parameters constant. For instance, � _<u>∂U∂T</u>_ � is not equal to _S_ ; you must first express _U_ as a function of its natural variables _S, V, N_ . 

-  **Gibbs-Duhem Relation Violation:** Forgetting that Gibbs Free Energy is a homogeneous function of degree 1 in particle number ( _N_ ): _G_ ( _T, P, N_ ) = _µ_ ( _T, P_ ) _N_ . Thus, the chemical potential is simply the Gibbs free energy per particle: _µ_ = _G/N_ . 

#### **7. Standard Textbook Systems** 

-  **The Classical Ideal Gas:** Characterized by the equation of state _PV_ = _NkBT_ . Its Helmholtz free energy is: 



<!-- Start of picture text -->
F ( T, V, N ) =  −NkBT ln + 1 (15)<br>� � NλV 3 � �<br><!-- End of picture text -->

where _λ_ = ~~�~~ 2 _πmkh_<sup>2</sup> _BT_<sup>isthethermaldeBrogliewavelength.</sup> 

-  **The Ideal Paramagnet (Two-Level System):** A system of _N_ non-interacting magnetic dipoles _µB_ in an external magnetic field _B_ . The potential is minimized using the magnetic free energy. 

5 

GATE PHYSICS 

THERMODYNAMICS & PHASE TRANSITIONS 

### **2 Maxwell’s Relations & Thermodynamic Coefficients** 

#### **1. Core Theory** 

* **Maxwell’s Relations:** A set of equations relating the partial derivatives of the fundamental thermodynamic variables ( _P, V, T, S_ ). * **Physical Significance:** They allow us to replace difficultto-measure macroscopic partial derivatives (such as the change of entropy with volume, _∂S/∂V_ ) with easily measurable quantities in the laboratory (such as the change of pressure with temperature, _∂P/∂T_ ). * **Mathematical Origin:** They are a direct consequence of the exactness of the differentials of thermodynamic potentials, which means the mixed second partial derivatives of these state functions are completely independent of the order of differentiation. 

#### **2. Mathematical Framework** 

For any analytic thermodynamic potential Ψ( _x, y_ ) with an exact differential _d_ Ψ = _Mdx_ + _Ndy_ : 



<!-- Start of picture text -->
∂ 2 Ψ<br>=<br>(16)<br>∂y∂x = ∂x∂y ∂ 2Ψ = ⇒ � ∂M∂y � x � ∂N∂x � y<br><!-- End of picture text -->

The four primary Maxwell relations derived from the four potentials are: 

1. **From** _dU_ = _TdS − PdV_ **:** 



<!-- Start of picture text -->
=  − (17)<br>� ∂V∂T � S � ∂P∂S � V<br><!-- End of picture text -->

2. **From** _dF_ = _−SdT − PdV_ **:** 



<!-- Start of picture text -->
=<br>(18)<br>� ∂V∂S � T � ∂P∂T � V<br><!-- End of picture text -->

3. **From** _dH_ = _TdS_ + _V dP_ **:** 



<!-- Start of picture text -->
=<br>(19)<br>� ∂P∂T � S � ∂V∂S � P<br><!-- End of picture text -->

4. **From** _dG_ = _−SdT_ + _V dP_ **:** 



<!-- Start of picture text -->
=  − (20)<br>� ∂P∂S � T � ∂V∂T � P<br><!-- End of picture text -->

#### **3. Derivation Milestones** 

Let us derive the second Maxwell relation from the Helmholtz free energy differential: 

1. **Establish the Differential Form:** Write _dF_ ( _T, V_ ) = _−SdT − PdV_ . 

2. **Identify the Coefficients:** Express the coefficients as first derivatives of _F_ : 



<!-- Start of picture text -->
S =  − , P =  − (21)<br>� ∂F∂T � V � ∂V∂F � T<br><!-- End of picture text -->

6 

GATE PHYSICS 

THERMODYNAMICS & PHASE TRANSITIONS 

3. **Apply Clairaut’s Theorem (Mixed Partials Equality):** Since _F_ is a state function with an exact differential: 



<!-- Start of picture text -->
∂ 2 F ∂ 2 F<br>(22)<br>∂V ∂T = ∂T∂V<br><!-- End of picture text -->

4. **Substitute Derivative Terms:** Substitute the coefficients into the equality: 



<!-- Start of picture text -->
∂<br>− = ∂ − = ⇒ = (23)<br>∂V � � ∂F∂T � V � T ∂T � � ∂V∂F � T � V � ∂V∂S � T � ∂P∂T � V<br><!-- End of picture text -->

#### **4. Problem-Solving Algorithm** 

**Calculating** _CP − CV_ **for Any Substance** 

To derive the general relationship between constant-pressure ( _CP_ ) and constant-volume ( _CV_ ) specific heats: 

1. **Write Down the Fundamental** _dS_ **Equation:** Let _S_ = _S_ ( _T, V_ ). Then: 



<!-- Start of picture text -->
dS = dT + dV (24)<br>� ∂T∂S � V � ∂V∂S � T<br><!-- End of picture text -->

Multiply by _T_ : 



<!-- Start of picture text -->
TdS =  CV dT +  T dV (25)<br>� ∂V∂S � T<br><!-- End of picture text -->

2. **Apply the Second Maxwell Relation:** Replace the difficult entropy derivative: 



<!-- Start of picture text -->
= = ⇒ TdS =  CV dT +  T dV (26)<br>� ∂V∂S � T � ∂P∂T � V � ∂P∂T � V<br><!-- End of picture text -->

3. **Incorporate Pressure-Volume Constraints:** Under constant pressure ( _dP_ = 0), write _dV_ = � _<u>∂V∂T</u>_ � _P_<sup>_dT_:</sup> 



<!-- Start of picture text -->
TdSP =  CP dT =  CV dT +  T dT (27)<br>� ∂P∂T � V � ∂V∂T � P<br><!-- End of picture text -->

Divide by _dT_ : 



<!-- Start of picture text -->
CP − CV =  T (28)<br>� ∂P∂T � V � ∂V∂T � P<br><!-- End of picture text -->

4. **Substitute Standard Coefficients:** Use the coefficient of thermal expansion _α ≡ V_ <u>1</u> � _<u>∂V∂T</u>_ <u>�</u> _P_<sup>andisothermalcompressibility</sup><sup>_κT≡−_</sup> _V_<sup><u>1</u></sup> � _<u>∂V∂P</u>_ � _T_<sup>.Usingthetripleproduct</sup> rule � _<u>∂P∂T</u>_ � _V_ � _∂V∂T_ � _P_ � _<u>∂V∂P</u>_ � _T_<sup>=</sup><sup>_−_1:</sup> 



<!-- Start of picture text -->
CP − CV = TV α 2 (29)<br>κT<br><!-- End of picture text -->

7 

GATE PHYSICS 

THERMODYNAMICS & PHASE TRANSITIONS 

#### **5. Connections to Observables** 

-  **Thermal Expansion Coefficient (** _α_ **):** _α_ = _V_<sup><u>1</u></sup> � _<u>∂V∂T</u>_ � _P_<sup>.(Measurablechangeinvolumewith</sup> temperature). 

-  **Isothermal Compressibility (** _κT_ **):** _κT_ = _− V_<sup><u>1</u></sup> � _<u>∂V∂P</u>_ � _T_<sup>.(Measurablechangeinvolumewith</sup> pressure). 

-  **Adiabatic Compressibility (** _κS_ **):** _κS_ = _− V_<sup><u>1</u></sup> � _<u>∂V∂P</u>_ � _S_<sup>.</sup> 

-  **Specific Heat Ratio (** _γ_ **):** 



<!-- Start of picture text -->
γ ≡ CP = κT<br>CV κS<br><!-- End of picture text -->

(30) 

#### **6. Crucial Pitfalls** 

##### **Maxwell’s Relations & Coefficients Traps** 

-  **The Sign Error in Cross-Differentiation:** Forgetting the negative signs in Maxwell’s relations. The relations derived from potentials involving _−PdV_ (which are _U_ and _F_ ) have a negative sign when switching variables, such as: 



<!-- Start of picture text -->
=  − (31)<br>� ∂V∂T � S � ∂P∂S � V<br> Triple Product Rule Sign Error: Misapplying the cyclic triple product rule:<br>=  − 1 (NOT + 1) (32)<br>� ∂x∂y � z � ∂∂zy � x � ∂x∂z � y<br><!-- End of picture text -->

#### **7. Standard Textbook Systems** 

-  **The Van der Waals Gas:** Governed by the equation of state: 



<!-- Start of picture text -->
P + aN 2 ( V − Nb ) =  NkBT (33)<br>� V 2 �<br><!-- End of picture text -->

Used to illustrate how _CP − CV_ deviates from the ideal gas constant _NkB_ due to molecular interactions. 

8 

GATE PHYSICS 

THERMODYNAMICS & PHASE TRANSITIONS 

### **3 Phase Transitions & Phase Equilibria** 

#### **1. Core Theory** 

A **phase transition** is a physical process where a thermodynamic system transforms from one state of matter (phase) to another (e.g., solid to liquid, paramagnetic to ferromagnetic). 

-  **First-Order Phase Transitions:** Characterized by a discontinuity in the first-order derivatives of the Gibbs free energy ( _G_ ). This implies a discontinuous change in entropy ( _S_ = _−∂G/∂T_ ) and volume ( _V_ = _∂G/∂P_ ), requiring a absorption or release of **latent heat** ( _L_ = _T_ ∆ _S_ ). 

-  **Second-Order (Continuous) Phase Transitions:** The first-order derivatives of _G_ are continuous (no latent heat, continuous entropy and volume), but the second-order derivatives (such as specific heat _CP_ , thermal expansion _α_ , and isothermal compressibility _κT_ ) are discontinuous or diverge at the transition temperature ( _Tc_ ). 

-  **Phase Equilibria:** Two or more distinct phases coexist stably in thermodynamic contact. This requires thermal ( _T_ 1 = _T_ 2), mechanical ( _P_ 1 = _P_ 2), and chemical ( _µ_ 1 = _µ_ 2) equilibrium. 

#### **2. Mathematical Framework** 

* **The Clausius-Clapeyron Equation:** Governs the boundary curve of phase coexistence in the _P_ - _T_ plane for first-order transitions: 



<!-- Start of picture text -->
dP L L<br>(34)<br>dT = T ∆ V =<br>T ( V final  − V initial)<br><!-- End of picture text -->

where _L_ is the latent heat of the transition, _T_ is the absolute transition temperature, and ∆ _V_ is the change in volume during the phase change. * **For Liquid-Gas Coexistence (with approximations):** If we assume the gas phase behaves ideally ( _Vg ≫ Vl_ = _⇒_ ∆ _V ≈ Vg_ = _RT/P_ ) and the latent heat of vaporization _L_ is constant: 



<!-- Start of picture text -->
dP<br>(35)<br>dT ≈ RT LP 2 = ⇒ P ( T ) =  P 0 e−L/RT<br><!-- End of picture text -->

* **Ehrenfest Equations for Second-Order Transitions:** Since ∆ _S_ = 0 and ∆ _V_ = 0 at the transition point, the slope of the _P_ - _T_ curve is governed by the changes in second-order coefficients: 



<!-- Start of picture text -->
dP<br>(36)<br>dT = V T ∆ C ∆ P α = ∆ ∆ κ α T<br><!-- End of picture text -->

where ∆ _CP_ , ∆ _α_ , and ∆ _κT_ are the jumps in specific heat, thermal expansion, and isothermal compressibility across the transition. 

#### **3. Derivation Milestones** 

Let us derive the Clausius-Clapeyron equation from the condition of phase equilibria: 

1. **Assert Chemical Equilibrium:** At any point on the phase boundary, the chemical potentials of Phase 1 and Phase 2 must be equal: 



<!-- Start of picture text -->
µ 1( T, P ) =  µ 2( T, P ) (37)<br><!-- End of picture text -->

9 

GATE PHYSICS 

THERMODYNAMICS & PHASE TRANSITIONS 

2. **Differentiate Along the Boundary Curve:** If we move along the coexistence curve by _dT_ and _dP_ , the chemical potentials must remain equal: 



<!-- Start of picture text -->
dµ 1 =  dµ 2 (38)<br><!-- End of picture text -->

3. **Apply the Gibbs-Duhem Relation:** For a single component, the change in chemical potential is _dµ_ = _−sdT_ + _vdP_ , where _s_ = _S/N_ and _v_ = _V/N_ are the specific entropy and volume: 



<!-- Start of picture text -->
−s 1 dT +  v 1 dP =  −s 2 dT +  v 2 dP (39)<br><!-- End of picture text -->

4. **Isolate the Coexistence Slope (** _dP/dT_ **):** Rearrange the terms: 



<!-- Start of picture text -->
( v 2  − v 1) dP = ( s 2  − s 1) dT = ⇒ dP = ∆ S (40)<br>dT = v s 2 2  −  − v s 1 1 ∆ V<br><!-- End of picture text -->

Substituting latent heat _L_ = _T_ ∆ _S_ yields the Clausius-Clapeyron equation. 

#### **4. Problem-Solving Algorithm** 

##### **Solving Clausius-Clapeyron Coexistence Relations** 

To calculate the change in boiling/melting points or vapor pressure changes: 

1. **Identify the Transition Type and Phases:** State whether the transition is melting (solid-liquid) or vaporization (liquid-gas). 

2. **Calculate the Volume Difference (** ∆ _V_ **):** 

   -  For melting: ∆ _V_ = _V_ liquid _− V_ solid. Be careful with the sign (e.g., for water, ice is less dense than liquid water, so ∆ _V <_ 0, which means the melting point decreases with pressure). 

   -  For vaporization: ∆ _V ≈ V_ gas _≈_<sup>_<u>RT</u>_</sup> _P_ (using the ideal gas approximation). 

3. **Substitute into the Clausius-Clapeyron Equation:** 



<!-- Start of picture text -->
∆ T ≈ T ∆ V ∆ P (41)<br>L<br><!-- End of picture text -->

4. **Evaluate the Vapor Pressure Integration (for Liquid-Gas):** If calculating pressure as a function of temperature: 



<!-- Start of picture text -->
ln =  − L − 1 (42)<br>� PP 12 � R � T 12 T 1 �<br><!-- End of picture text -->

#### **5. Connections to Observables** 

-  **Latent Heat (** _L_ **):** Directly measurable thermal energy required to change the phase of a unit mass. 

-  **Discontinuity in Heat Capacity (** _CP_ **):** Signifies a continuous second-order transition (such as the superconducting transition in metals at zero magnetic field). 

10 

GATE PHYSICS 

THERMODYNAMICS & PHASE TRANSITIONS 

#### **6. Crucial Pitfalls** 

##### **Phase Transitions Traps to Avoid** 

-  **The Water Melting Slope Sign Error:** Assuming the melting curve _dP/dT_ of all solids is positive. For water, because ice is less dense than liquid water (∆ _V <_ 0), the slope is negative: _dP/dT <_ 0. This means increasing pressure lowers the melting point of ice. 

-  **Applying Ideal Gas Approximation to Liquids/Solids:** Approximating ∆ _V ≈ Vg_ for solid-liquid transitions. Solid-liquid volume changes are extremely tiny and cannot be modeled using gas laws; you must use the given solid/liquid densities. 

#### **7. Standard Textbook Systems** 

-  **Liquid-Vapor Coexistence of Water:** Illustrates the classical liquid-gas first-order transition ending at a critical point. 

-  **The Superconducting Transition in Zero Field:** A classic second-order phase transition where specific heat _Cv_ drops discontinuously at _Tc_ without any latent heat. 

11 

GATE PHYSICS 

THERMODYNAMICS & PHASE TRANSITIONS 

### **4 Critical Phenomena, Scaling Laws & Landau Theory** 

#### **1. Core Theory** 

* **Critical Point:** The endpoint of a phase coexistence curve (e.g., the liquid-gas coexistence curve), beyond which the distinction between the two phases vanishes entirely. * **Critical Phenomena:** The unique physical behaviors that manifest near a continuous (second-order) phase transition or critical point. These behaviors are characterized by the divergence of thermodynamic quantities (like susceptibility and correlation length) and are dominated by long-range fluctuations. * **Universality:** The remarkable physical observation that completely different physical systems (such as ferromagnets, liquid-gas systems, and binary alloys) exhibit identical critical exponents near their transitions, depending only on spatial dimensionality ( _d_ ) and the symmetry of the order parameter. * **Landau Theory of Phase Transitions:** A phenomenological mean-field theory that models phase transitions by expanding the thermodynamic potential (Gibbs free energy) as a power series in a macroscopic **order parameter** ( _η_ ) near the transition temperature ( _Tc_ ). 

#### **2. Mathematical Framework** 

* **Critical Exponents:** Describe the power-law behavior of thermodynamic variables as a function of the reduced temperature _t ≡_<sup>_<u>T</u>−_</sup> _Tc_<sup>_<u>Tc</u>_:</sup> 

-  **Specific Heat:** _CV ∼|t|_<sup>_−α_</sup> 

-  **Order Parameter (e.g., Magnetization** _M_ **):** _M ∼_ ( _−t_ )<sup>_β_</sup> (for _t <_ 0)  **Susceptibility (e.g., Magnetic Susceptibility** _χ_ **):** _χ ∼|t|_<sup>_−γ_</sup> 

-  **Critical Isotherm (** _t_ = 0 **):** _M ∼|H|_<sup>1</sup><sup>_/δ_</sup> 

-  **Correlation Length (** _ξ_ **):** _ξ ∼|t|_<sup>_−ν_</sup> 

-  **Correlation Function at** _t_ = 0 **:** _G_ ( _r_ ) _∼ r_<sup>_d−_</sup> <u>1</u><sup>2+</sup><sup>_η_</sup> 

* **Scaling Relations (Exactly Conserved):** 

   -  **Widom Scaling:** _γ_ = _β_ ( _δ −_ 1) 

   -  **Rushbrooke Equality:** _α_ + 2 _β_ + _γ_ = 2 

   -  **Fisher Relation:** _γ_ = _ν_ (2 _− η_ ) 

-  **Josephson (Hyper-scaling) Relation:** 2 _− α_ = _dν_ (where _d_ is spatial dimension) 

- * **Landau Free Energy Expansion (Symmetric under** _η →−η_ **):** _G_ ( _T, η_ ) = _G_ 0( _T_ ) + _a_ ( _T_ ) _η_<sup>2</sup> + _b_ ( _T_ ) _η_<sup>4</sup> _− ηH_ (43) 

where _b_ ( _T_ ) _>_ 0 for stability, _H_ is the external conjugate field, and the quadratic coefficient changes sign at _Tc_ : 



<!-- Start of picture text -->
a ( T ) =  a 0( T − Tc ) ( a 0 >  0) (44)<br><!-- End of picture text -->

12 

GATE PHYSICS 

THERMODYNAMICS & PHASE TRANSITIONS 

#### **3. Derivation Milestones** 

Let us derive the Mean-Field critical exponent _β_ = 1 _/_ 2 from Landau Theory under zero external field ( _H_ = 0): 

1. **Write the Equilibrium Free Energy Expansion:** 



<!-- Start of picture text -->
G ( T, η ) =  G 0( T ) +  a 0( T − Tc ) η 2 +  bη 4 (45)<br><!-- End of picture text -->

2. **Apply the Equilibrium Minimization Condition:** 



<!-- Start of picture text -->
∂G<br>∂η = 2 a 0( T − Tc ) η  + 4 bη 3 = 0 (46)<br><!-- End of picture text -->

3. **Isolate the Roots of the Equation:** 



<!-- Start of picture text -->
η �2 a 0( T − Tc ) + 4 bη 2� = 0 (47)<br><!-- End of picture text -->

* If _T > Tc_ : The only real root is _η_ 0 = 0 (symmetric, disordered phase). * If _T < Tc_ : The non-zero roots are: 



<!-- Start of picture text -->
η 0 2 = a 0( Tc − T ) = ⇒ η 0 =  ± a 0 (48)<br>2 b � 2 b ( Tc − T )1 / 2<br><!-- End of picture text -->

4. **Extract the Critical Exponent** _β_ **:** Comparing this result to the power law definition _η_ 0 _∼_ ( _−t_ )<sup>_β_</sup> directly yields the mean-field exponent: 



<!-- Start of picture text -->
β = 1 (49)<br>2<br><!-- End of picture text -->

#### **4. Problem-Solving Algorithm** 

##### **Evaluating Scaling Relations and Critical Exponents** 

To find an unknown critical exponent or verify a scaling law: 

1. **List Given Exponents:** Note the values of the known exponents (e.g., _α, β, γ_ ). 

2. **Select the Appropriate Scaling Equation:** Match the variables to the standard equalities: 

   -  If you need to relate _α_ , _β_ , and _γ_ , use the **Rushbrooke Equality** : _α_ +2 _β_ + _γ_ = 2. 

   -  If you need to relate _β_ , _γ_ , and _δ_ , use the **Widom Scaling** : _γ_ = _β_ ( _δ −_ 1). 

3. **Solve Algebrically:** Rearrange the scaling equation to isolate the target exponent. 

4. **Check Hyper-scaling (if spatial dimension** _d_ **is involved):** Use the Josephson relation 2 _− α_ = _dν_ to calculate the correlation exponent _ν_ or determine the spatial dimension. 

#### **5. Connections to Observables** 

-  **Magnetic Susceptibility (** _χ_ **):** Diverges as _χ ∼|T − Tc|_<sup>_−_1</sup> (Mean-Field) or _|T − Tc|_<sup>_−_1</sup><sup>_._24</sup> (3D Ising Model) near the transition. 

-  **Order Parameter (Magnetization** _M_ **):** The spontaneous magnetization below _Tc_ , which is directly measurable via magnetic induction. 

13 

GATE PHYSICS 

THERMODYNAMICS & PHASE TRANSITIONS 

#### **6. Crucial Pitfalls** 

##### **Critical Phenomena & Landau Theory Traps** 

-  **The Dimensionality Hyper-scaling Limit:** Attempting to apply the Josephson hyper-scaling relation (2 _− α_ = _dν_ ) in dimensions greater than the **Upper Critical Dimension** ( _d_ uc = 4). Above _d_ = 4, mean-field theory is exact, but hyper-scaling relations fail because fluctuations are completely suppressed. 

-  **Landau Symmetry Expansion Error:** Including odd power terms (like _η_<sup>3</sup> ) in the expansion when the physical system possesses inversion symmetry (like a ferromagnet under zero field, where _G_ ( _M_ ) = _G_ ( _−M_ )). Odd terms are strictly forbidden by symmetry unless a first-order transition is explicitly modeled. 

#### **7. Standard Textbook Systems** 

-  **The 2D Ising Model (exact Onsager solution):** A model of interacting spins on a square lattice. Its exact critical exponents are _α_ = 0 (logarithmic divergence), _β_ = 1 _/_ 8, and _γ_ = 7 _/_ 4, proving that mean-field theory fails to capture true low-dimensional fluctuations. 

-  **The Curie-Weyl Ferromagnet:** A classical system solved via Mean-Field Theory, yielding the standard exponents _α_ = 0 (discontinuity), _β_ = 1 _/_ 2, and _γ_ = 1. 

14 

GATE PHYSICS 

THERMODYNAMICS & PHASE TRANSITIONS 

### **References** 

1. Satya Prakash. _Statistical Mechanics_ . Kedar Nath Ram Nath, 2019. 

2. Huang, Kerson. _Statistical Mechanics_ . Wiley, 1987. 

3. Agarwal, Bipin K. & Eisner, Melvin. _Statistical Mechanics_ . Wiley, 1988. 

15 

GATE PHYSICS STUDY NOTES 

STATISTICAL MECHANICS 

# **GATE PHYSICS STUDY NOTES Statistical Mechanics & Ensemble Theory** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics** 

### **Contents** 

|**1**<br>**Mic**|**rostates, Macrostates, Phase Space, and Liouville’s Theorem**|**2**|
|---|---|---|
|1.1|Core Theory<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>2|
|1.2|Mathematical Framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>2|
|1.3|Derivation Milestones<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>3|
|1.4|Problem-Solving Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>4|
|1.5|Connections to Observables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>4|
|1.6|Crucial Pitfalls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>4|
|1.7|Standard Textbook Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>4|
|**2**<br>**The**|**Statistical Ensembles (Microcanonical, Canonical, Grand Canonical)**|**6**|
|2.1|Core Theory<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>6|
|2.2|Mathematical Framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>6|
|2.3|Derivation Milestones<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>7|
|2.4|Problem-Solving Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>7|
|2.5|Connections to Observables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>8|
|2.6|Crucial Pitfalls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>8|
|2.7|Standard Textbook Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>8|
|**3**<br>**Cal**|**culation of Thermodynamic Quantities from the Partition Function**|**9**|
|3.1|Core Theory<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>9|
|3.2|Mathematical Framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>9|
|3.3|Derivation Milestones<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>10|
|3.4|Problem-Solving Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>10|
|3.5|Connections to Observables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>11|
|3.6|Crucial Pitfalls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>11|
|3.7|Standard Textbook Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>11|



1 

GATE PHYSICS STUDY NOTES 

STATISTICAL MECHANICS 

### **1 Microstates, Macrostates, Phase Space, and Liouville’s Theorem** 

#### **1.1 Core Theory** 

Statistical mechanics forms the mathematical bridge connecting the microscopic quantum states of a system to its macroscopic thermodynamic observables. 

-  **Microstate:** A complete, detailed microscopic specification of a classical or quantum system. Classically, a microstate is defined by specifying the exact coordinates _qi_ and conjugate momenta _pi_ of all _N_ particles at any given instant. Quantum mechanically, it corresponds to a specific state vector _|ψ⟩_ or wave function in Hilbert space. 

-  **Macrostate:** A coarse-grained state of a system defined by a small set of macroscopic thermodynamic variables, such as energy ( _E_ ), volume ( _V_ ), pressure ( _P_ ), temperature ( _T_ ), and particle count ( _N_ ). A single macrostate typically corresponds to an extremely large number (Ω) of compatible microscopic configurations. 

-  **Phase Space (** Γ **-Space):** A continuous 2 _f_ -dimensional mathematical space (where _f_ is the number of degrees of freedom) whose axes correspond to the coordinates _qi_ and conjugate momenta _pi_ of the system. The instantaneous microscopic state of the entire system is represented by a single point, called a **representative point** , in this phase space. As the system evolves in time, this point traces out a path called a **phase trajectory** . 

-  **Liouville’s Theorem:** Governs the temporal evolution of a representative group of identical systems, represented as a continuous cloud of points in phase space. The theorem states that the local density of these representative points, _ρ_ ( _q, p, t_ ), behaves like an **incompressible fluid** in phase space. That is, the local density remains constant along any trajectory. 

-  **Postulate of Equal A Priori Probability:** For an isolated system in thermodynamic equilibrium, all accessible microstates compatible with the macrostate constraints (e.g., lying in the energy shell [ _E, E_ + ∆ _E_ ]) are equally likely to be occupied. 

#### **1.2 Mathematical Framework** 

* **Phase Space Volume Element (** _d_ Γ **):** Classically, for a system with _N_ identical particles in 3D ( _f_ = 3 _N_ degrees of freedom): 



<!-- Start of picture text -->
3 N<br>1<br>d Γ = N ! h 3 N � dqidpi (1)<br>i =1<br><!-- End of picture text -->

where the factor _h_<sup>3</sup><sup>_N_</sup> represents the minimum quantum volume of a single microstate in phase space, and the _N_ ! factor corrects for the physical indistinguishability of the particles (resolving Gibbs’ paradox). * **Phase Density and Probability Distribution (** _ρ_ **):** The probability of finding the system’s representative point in a volume element _d_ Γ at time _t_ is: 



<!-- Start of picture text -->
dP =  ρ ( q, p, t )  dq 1  . . . dqf dp 1  . . . dpf<br><!-- End of picture text -->



<!-- Start of picture text -->
(2)<br><!-- End of picture text -->

with the normalization condition: 



<!-- Start of picture text -->
ρ ( q, p, t )  dqdp  = 1 (3)<br>�<br><!-- End of picture text -->

2 

GATE PHYSICS STUDY NOTES 

STATISTICAL MECHANICS 

* **Liouville’s Equation:** The partial time derivative of the density satisfies: 



<!-- Start of picture text -->
∂ρ<br>∂t +  {ρ, H}  = 0 (4)<br><!-- End of picture text -->

where _{ρ, H}_ is the classical **Poisson Bracket**: 



<!-- Start of picture text -->
f<br>∂H − ∂ρ ∂H<br>{ρ, H} ≡ � (5)<br>i =1 � ∂q∂ρi ∂pi ∂pi ∂qi �<br><!-- End of picture text -->

* **Equilibrium Condition:** For a system in thermodynamic equilibrium, the phase density must be stationary in time ( _∂ρ/∂t_ = 0), which requires: 

_{ρ, H}_ = 0 = _⇒ ρ_ = _ρ_ ( _H_ ) (6) 

This implies that at equilibrium, the probability density must be a function of the Hamiltonian (energy) of the system only. 

#### **1.3 Derivation Milestones** 

Let us derive Liouville’s theorem by evaluating the conservation of representative points in phase space: 

1. **Apply the Equation of Continuity:** Consider an arbitrary closed volume _V_ Γ in phase space bounded by a surface _S_ Γ. The rate of change of the number of representative points inside _V_ Γ must equal the net flux of points entering or leaving across the boundary, which yields the continuity equation: 



<!-- Start of picture text -->
f<br>∂ρ<br>∂t + � i =1 � ∂q∂ i ( ρ  ˙ qi ) + ∂p ∂ i ( ρ  ˙ pi )� = 0 (7)<br><!-- End of picture text -->

2. **Expand using the Product Rule:** 



<!-- Start of picture text -->
f f<br>∂ρ ∂ρ ∂ρ<br>∂t + � i =1 � q ˙ i ∂qi + p ˙ i ∂pi � +  ρ � i =1 � ∂q∂q ˙ ii + ∂p ∂p ˙ i i � = 0 (8)<br><!-- End of picture text -->

3. **Apply Hamilton’s Equations of Motion:** Hamilton’s equations state that _q_ ˙ _i_ =<sup>_<u>∂H</u>_</sup> _∂pi_<sup>and</sup> _p_ ˙ _i_ = _−_<sup>_<u>∂H</u>_</sup> _∂qi_<sup>.Substitutingtheseintothesecondtermoftheexpandedequation:</sup> 



<!-- Start of picture text -->
f f<br>� + ∂p ˙ i = � − ∂ 2 H = 0 (9)<br>i =1 � ∂q∂q ˙ ii ∂pi � i =1 � ∂q∂ 2 i∂pH i ∂pi∂qi �<br><!-- End of picture text -->

Since the mixed second partial derivatives of the Hamiltonian are continuous and symmetric, this divergence term vanishes identically. 

4. **Isolate the Total (Substantial) Derivative:** This simplifies the equation of continuity to: 



<!-- Start of picture text -->
f<br>∂∂tρ + � i =1 � ∂q∂ρi q ˙ i  + ∂p ∂ρ i p ˙ i � = 0 = ⇒ d dt ρ = 0 (10)<br><!-- End of picture text -->

proving that the total derivative of the probability density along any phase flow trajectory is zero. 

3 

GATE PHYSICS STUDY NOTES 

STATISTICAL MECHANICS 

#### **1.4 Problem-Solving Algorithm** 

##### **Analyzing Phase Space Volume and Density Constraints** 

1. **Identify Degrees of Freedom (** _f_ **):** For a classical system of _N_ point particles, _f_ = 3 _N_ . For rigid diatomic molecules, _f_ = 5 _N_ . 

2. **Determine Energy Boundaries:** Note the energy shell bounds [ _E, E_ + ∆ _E_ ]. 

3. **Evaluate the Phase Space Integral:** Calculate the volume of the accessible phase space, Ω( _E_ ), by integrating over the allowed region: 



<!-- Start of picture text -->
Γ( E ) = dqdp = ⇒ Ω( E ) = ∂ Γ( E ) ∆ E (11)<br>� H ( q,p ) ≤E ∂E<br><!-- End of picture text -->

4. **Verify Stationarity using Poisson Brackets:** To check if a given phase distribution _ρ_ ( _q, p_ ) represents an equilibrium state, compute _{ρ, H}_ and confirm it equals 0. 

#### **1.5 Connections to Observables** 

* **Entropy (** _S_ **):** Connected directly to the phase volume Ω( _E_ ) of the microcanonical ensemble through Boltzmann’s formula: 



<!-- Start of picture text -->
S =  kB  ln Ω( E ) (12)<br><!-- End of picture text -->

* **Ensemble Average of an Observable (** _⟨A⟩_ **):** 



<!-- Start of picture text -->
⟨A⟩ = A ( q, p ) ρ ( q, p )  dqdp (13)<br>�<br><!-- End of picture text -->

By the **Ergodic Hypothesis**, the time average of any physical observable along a trajectory is equal to this ensemble average over phase space. 

#### **1.6 Crucial Pitfalls** 

##### **Phase Space Errors to Avoid** 

-  **Gibbs’ Indistinguishability Paradox:** Forgetting to divide the classical phase space volume by the factorial factor _N_ !. Without this correction, the calculated entropy violates the thermodynamic property of extensivity. 

-  **Misinterpreting the Density Derivative:** Confusing the local time derivative ( _∂ρ/∂t_ ) with the total derivative along the flow ( _dρ/dt_ ). Liouville’s theorem states that _dρ/dt_ = 0, meaning density is constant from the frame of reference of a moving point. This is compatible with non-zero local changes ( _∂ρ/∂t̸_ = 0) for non-equilibrium states. 

#### **1.7 Standard Textbook Systems** 

-  **The Classical 1D Simple Harmonic Oscillator:** Governed by the Hamiltonian _H_ ( _q, p_ ) = 2 _<u>pm</u>_<sup>2+</sup> 2<sup><u>1</u></sup><sup>_mω_2</sup><sup>_q_2=</sup><sup>_E_.Thephasespaceis2</sup><sup>_D_,andthetrajectoryofconstantenergyformsan</sup> 

4 

GATE PHYSICS STUDY NOTES 

STATISTICAL MECHANICS 



<!-- Start of picture text -->
**ellipse**:<br>q 2 p 2<br>(2 E/mω 2 ) + (2 mE ) = 1<br><!-- End of picture text -->

(14) 

-  **The Classical Ideal Gas:** An isolated system of _N_ non-interacting point masses inside a _<u>p</u>_<sup>2</sup> _<u>i</u>_ 

- container of volume _V_ , where the Hamiltonian is purely kinetic: _H_ =<sup>�3</sup> _i_ =1<sup>_N_</sup> 2 _m_<sup>.</sup> 

5 

GATE PHYSICS STUDY NOTES 

STATISTICAL MECHANICS 

### **2 The Statistical Ensembles (Microcanonical, Canonical, Grand Canonical)** 

#### **2.1 Core Theory** 

To evaluate systems with different environmental constraints, statistical mechanics introduces three standard types of imaginary collections of identical systems, called **ensembles**: 

-  **The Microcanonical Ensemble (MCE):** Represents an **isolated system** with fixed particle count ( _N_ ), volume ( _V_ ), and exact internal energy ( _E_ ). The system cannot exchange energy or particles with its surroundings. 

-  **The Canonical Ensemble (CE):** Represents a system in **thermal contact** with a massive heat reservoir at constant temperature _T_ . The system can exchange energy with the reservoir, meaning its internal energy fluctuates, but _N_ , _V_ , and _T_ are constant. 

-  **The Grand Canonical Ensemble (GCE):** Represents an **open, non-isolated system** in both thermal and chemical contact with a reservoir. Both energy and particles can fluctuate between the system and reservoir, keeping the temperature ( _T_ ), volume ( _V_ ), and chemical potential ( _µ_ ) constant. 

#### **2.2 Mathematical Framework** 

* **Microcanonical Ensemble (MCE):** The equilibrium phase space density is: 



<!-- Start of picture text -->
Constant if E < H ( q, p )  < E  + ∆ E<br>ρ ( q, p ) = (15)<br>0 otherwise<br>�<br><!-- End of picture text -->

The state function is the microstate count Ω( _N, V, E_ ). * **Canonical Ensemble (CE):** The probability of finding the system in a microstate _r_ with energy _Er_ is given by the **Boltzmann Distribution**: 



<!-- Start of picture text -->
e −βEr<br>Pr = (16)<br>ZN ( V, T )<br><!-- End of picture text -->

where _β_ = _kB_ <u>1</u> _T_<sup>is the inverse temperature, and the normalization factor is the **Canonical Partition</sup> Function**: 



<!-- Start of picture text -->
1<br>ZN ( V, T ) = � e −βEr (Quantum) , ZN ( V, T ) = N ! h 3 N � e −βH ( q,p ) dqdp (Classical) (17)<br>r<br><!-- End of picture text -->

* **Grand Canonical Ensemble (GCE):** The probability of finding the system in a state with _N_ particles and energy _Er_ is: 



<!-- Start of picture text -->
Pr,N = e Ξ( −β T, V, µ ( Er−µN ) ) = Ξ( zN T, V, µ e−βEr ) (18)<br><!-- End of picture text -->

where _z ≡ e_<sup>_βµ_</sup> is the **fugacity**, and the normalization factor is the **Grand Canonical Partition Function**: 



<!-- Start of picture text -->
∞<br>Ξ( T, V, µ ) = � z N ZN ( V, T ) (19)<br>N =0<br><!-- End of picture text -->

6 

GATE PHYSICS STUDY NOTES 

STATISTICAL MECHANICS 

#### **2.3 Derivation Milestones** 

Let us derive the Boltzmann distribution of the Canonical Ensemble by analyzing a system in contact with a reservoir: 

1. **Set up the Closed Composite System:** Consider a small system _A_ with energy _Er_ coupled to a massive reservoir _AR_ . The combined composite system _A_ 0 = _A_ + _AR_ is completely isolated, so MCE applies to _A_ 0 with total energy _E_ 0 = _Er_ + _ER_ = Constant. 

2. **Formulate Probability via Reservoir State Count:** The probability _Pr_ of finding system _A_ in a specific microstate _r_ of energy _Er_ is directly proportional to the number of accessible microstates of the reservoir, Ω _R_ ( _ER_ ): 



<!-- Start of picture text -->
Pr ∝ Ω R ( E 0  − Er )  ·  (1) (20)<br><!-- End of picture text -->

Since the reservoir is massive, we can assume _Er ≪ E_ 0. 

3. **Perform a Taylor Series Expansion of Entropy:** Expand ln Ω _R_ ( _E_ 0 _− Er_ ) in a Taylor series about _Er_ = 0: 



<!-- Start of picture text -->
ln Ω R ( E 0  − Er )  ≈ ln Ω R ( E 0)  − Er (21)<br>� ∂∂E ln Ω RR � ER = E 0<br><!-- End of picture text -->

Since entropy is defined as _S_ = _kB_ ln Ω, the derivative term corresponds to the inverse temperature of the reservoir: 



<!-- Start of picture text -->
∂SR 1<br>= 1 = (22)<br>� ∂∂E ln Ω RR � kB ∂ER kBT ≡ β<br><!-- End of picture text -->

4. **Exponentiate to obtain the Boltzmann Factor:** Substituting this back into the logarithm and exponentiating: 



<!-- Start of picture text -->
Ω R ( E 0  − Er )  ≈ Ω R ( E 0) e −βEr = ⇒ Pr ∝ e −βEr (23)<br><!-- End of picture text -->

Normalizing this probability over all possible states yields _Pr_ = _e_<sup>_−βEr_</sup> _/Z_ . 

#### **2.4 Problem-Solving Algorithm** 

##### **Formulating the Partition Function for a System** 

1. **Determine the Ensemble Type:** Look at the boundary parameters. If _N, V, T_ are given, use the Canonical Ensemble. If chemical potential _µ_ or particle fluctuation is mentioned, use the Grand Canonical Ensemble. 

2. **Identify the Quantum State Spectrum:** Write down the allowed energy eigenvalues _Er_ of the system. 

3. **Perform the Summation/Integration:** * For discrete quantum states: _Z_ = � _n_<sup>_gne−βEn_(where</sup><sup>_gn_is the degeneracy of energy level</sup><sup>_En_).* For classical continuous</sup> states: _Z_ = _N_ ! _h_ <u>1</u><sup>3</sup><sup>_N_</sup> � _e_<sup>_−βH_(</sup><sup>_q,p_)</sup> _dqdp_ . 

4. **Simplify algebraic expressions:** Use Taylor expansions, geometric series, or Gaussian integrals to simplify _Z_ or Ξ. 

7 

GATE PHYSICS STUDY NOTES 

STATISTICAL MECHANICS 

#### **2.5 Connections to Observables** 

* **Fluctuations in Energy (Canonical Ensemble):** The spread of energy states is given by: 



<!-- Start of picture text -->
σE 2 ≡⟨E 2 ⟩−⟨E⟩ 2 =  − ∂⟨E⟩ =  kBT 2 CV (24)<br>∂β<br><!-- End of picture text -->

This <u>proves</u> that in the thermodynamic limit ( _N →∞_ ), relative fluctuations scale as _σE/⟨E⟩∝_ 1 _/_ _~~√~~ N →_ 0, rendering the ensembles thermodynamically equivalent. * **Fluctuations in Particle Count (Grand Canonical Ensemble):** 



<!-- Start of picture text -->
∂ 2 ln Ξ<br>σN 2 ≡⟨N 2 ⟩−⟨N ⟩ 2 = 1 =  kBT N 2 (25)<br>β 2 ∂µ 2 V κT<br><!-- End of picture text -->

where _κT_ is the isothermal compressibility. 

#### **2.6 Crucial Pitfalls** 

##### **Ensemble Pitfalls to Avoid** 

-  **Neglecting Degeneracy Factors (** _gn_ **):** Forgetting to multiply each term in the partition sum by its respective quantum degeneracy. For example, in a hydrogen-like atom, level _n_ has a degeneracy of 2 _n_<sup>2</sup> . Skipping this factor will lead to incorrect energy and specific heat evaluations. 

-  **Summing over Levels instead of States:** Confusing �states<sup>_e−βEs_</sup> with �levels<sup>_e−βEl_.</sup> If summing over energy levels, you **must** include the degeneracy factor _gl_ in front of the exponential. 

#### **2.7 Standard Textbook Systems** 

-  **The Quantum 1D Harmonic Oscillator (Canonical Ensemble):** A system with nondegenerate, equidistant energy eigenvalues _En_ = � _n_ + 2<sup><u>1</u></sup> � ℏ _ω_ for _n ∈{_ 0 _,_ 1 _,_ 2 _, . . . }_ . 

-  **The Ideal Quantum Gas (Grand Canonical Ensemble):** A gas of non-interacting particles where occupancy of single-particle energy levels is governed by quantum statistics (Fermi-Dirac or Bose-Einstein). 

8 

GATE PHYSICS STUDY NOTES 

STATISTICAL MECHANICS 

### **3 Calculation of Thermodynamic Quantities from the Partition Function** 

#### **3.1 Core Theory** 

The partition function contains the complete statistical profile of the system’s microscopic states. By taking systematic partial derivatives of the logarithm of the partition function with respect to its natural parameters (such as _β_ , _V_ , and _µ_ ), we can extract all macroscopic thermodynamic state functions. 

#### **3.2 Mathematical Framework** 

The primary bridge equations between the partition functions and thermodynamic potentials are: 



<!-- Start of picture text -->
 Helmholtz Free Energy ( F ):<br><!-- End of picture text -->



<!-- Start of picture text -->
F ( T, V, N ) =  −kBT ln  ZN ( V, T ) (26)<br><!-- End of picture text -->



<!-- Start of picture text -->
 Grand Potential ( Φ G ):<br><!-- End of picture text -->



<!-- Start of picture text -->
Φ G ( T, V, µ )  ≡−kBT ln Ξ( T, V, µ ) =  −PV (27)<br><!-- End of picture text -->

From these potentials, we derive all macroscopic variables: 



<!-- Start of picture text -->
 Internal Energy (Mean Energy, ⟨E⟩ ):<br><!-- End of picture text -->



<!-- Start of picture text -->
⟨E⟩ =  − ∂ ln  Z =  kBT 2 (28)<br>∂β � ∂∂T ln  Z � V,N<br><!-- End of picture text -->



<!-- Start of picture text -->
 Entropy ( S ):<br><!-- End of picture text -->



<!-- Start of picture text -->
S =  − =  kB  ln  Z  + ⟨E⟩ (29)<br>� ∂F∂T � V,N T<br><!-- End of picture text -->



<!-- Start of picture text -->
 Pressure ( P ):<br><!-- End of picture text -->



<!-- Start of picture text -->
P =  − =  kBT (30)<br>� ∂V∂F � T,N � ∂∂V ln  Z � T,N<br><!-- End of picture text -->

 **Chemical Potential (** _µ_ **):** 



<!-- Start of picture text -->
µ  = =  −kBT (31)<br>� ∂N∂F � T,V � ∂∂N ln  Z � T,V<br><!-- End of picture text -->

 **Average Particle Count in GCE (** _⟨N ⟩_ **):** 



<!-- Start of picture text -->
⟨N ⟩ = 1 =  z (32)<br>β � ∂∂µ ln Ξ � T,V � ∂ ∂z ln Ξ � T,V<br><!-- End of picture text -->

9 

GATE PHYSICS STUDY NOTES 

STATISTICAL MECHANICS 

#### **3.3 Derivation Milestones** 

Let us derive the fundamental connection between entropy, internal energy, and the partition function: 

1. **Define the Gibbs-Shannon Entropy:** The statistical definition of entropy is: 



<!-- Start of picture text -->
S =  −kB � Pr  ln  Pr (33)<br>r<br><!-- End of picture text -->

2. **Substitute the Canonical Probability:** Substitute the Boltzmann distribution _Pr_ = _e_<sup>_−βEr_</sup> _/Z_ : 



<!-- Start of picture text -->
S =  −kB � r Pr  ln � e−ZβEr � =  −kB � r Pr  ( −βEr − ln  Z ) (34)<br><!-- End of picture text -->

3. **Expand and Distribute the Summation:** 



<!-- Start of picture text -->
S =  kBβ � PrEr  +  kB  ln  Z � Pr (35)<br>r r<br><!-- End of picture text -->

4. **Apply Probability Constraints:** Recall that the sum of all probabilities is normalized to 1 (<sup>�</sup> _Pr_ = 1), and the average energy is _⟨E⟩_ =<sup>�</sup> _PrEr_ : 



<!-- Start of picture text -->
S = ⟨E⟩ +  kB  ln  Z = ⇒ F ≡⟨E⟩− TS =  −kBT ln  Z (36)<br>T<br><!-- End of picture text -->

This completes the formal proof. 

#### **3.4 Problem-Solving Algorithm** 

**Calculating Specific Heat and Pressure from** _Z_ 

1. **Evaluate the Partition Function** _Z_ ( _T, V, N_ ) **:** Simplify _Z_ into a neat analytic function. 

2. **Take the Logarithm:** Compute ln _Z_ . 

3. **Evaluate Internal Energy:** Differentiate with respect to _β_ : 



<!-- Start of picture text -->
U =  − ∂ ln  Z (37)<br>∂β<br><!-- End of picture text -->

4. **Differentiate to find Specific Heat:** Differentiate _U_ with respect to temperature: 



<!-- Start of picture text -->
CV = =  kBβ 2 ∂ 2 ln  Z (38)<br>� ∂U∂T � V ∂β 2<br><!-- End of picture text -->

10 

GATE PHYSICS STUDY NOTES 

STATISTICAL MECHANICS 

#### **3.5 Connections to Observables** 

* **Specific Heat Peak (Schottky Anomaly):** In a two-level system, the specific heat exhibits a characteristic peak when the temperature matches the energy splitting ( _kBT ∼_ ∆ _E_ ), which is a key experimental signature of quantum transitions. * **Magnetic Susceptibility (** _χ_ **):** For a spin system with magnetic partition function _Z_ : 



<!-- Start of picture text -->
⟨M ⟩ = 1 ∂ ln  Z = ⇒ χ ≡ = 1 ∂ 2 ln  Z (39)<br>β ∂B � ∂∂B⟨M ⟩ � β ∂B 2<br><!-- End of picture text -->

#### **3.6 Crucial Pitfalls** 

##### **Thermodynamic Extraction Errors to Avoid** 

-  **Incorrect Derivative Constraints:** Forgetting which variables must be held constant during partial differentiation. For instance, when calculating pressure _P_ = _kBT_ ( _∂_ ln _Z/∂V_ ), the temperature _T_ and particle count _N_ must be held strictly constant. 

-  **Confusion of Logarithm Bases:** Using base-10 logarithms (log10) in Boltzmann calculations. The thermodynamic equations are defined strictly using the natural logarithm (ln, base _e_ ). 

#### **3.7 Standard Textbook Systems** 

-  **The Two-Level Paramagnetic Spin System:** A system of _N_ non-interacting, localized spin-1/2 particles in an external magnetic field _B_ . The energy levels of each spin are _Es_ = _∓µBB_ , yielding the single-particle partition function _Z_ 1 = 2 cosh( _βµBB_ ). 

- _<u>V</u>_<sup>_N_</sup> 

-  **The Classical Monoatomic Ideal Gas:** Using _ZN_ = _N_ ! _λ_<sup>3</sup><sup>_N_,weextracttheidealgaslaw</sup> _PV_ = _NkBT_ and the specific heat _CV_ = 2<sup><u>3</u></sup><sup>_NkB_.</sup> 

11 

GATE PHYSICS STUDY NOTES 

STATISTICAL MECHANICS 

### **References** 

1. Huang, Kerson. _Statistical Mechanics_ . Wiley, 1987. 

2. Satya Prakash. _Statistical Mechanics_ . Kedar Nath Ram Nath, 2019. 

3. Agarwal, Bipin K. & Eisner, Melvin. _Statistical Mechanics_ . dokumen.pub, 2011. 

12 

GATE PHYSICS 

<u>QUANTUM</u> STATISTICS & DEGENERATE GAS 

# **GATE PHYSICS STUDY NOTES Quantum Statistics & The Degenerate Fermi Gas** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

### **Contents** 

|**1**<br>**Classical vs. Quantum Statistics & Indistinguishability**|**2**|
|---|---|
|**2**<br>**The Pauli Exclusion Principle & Fermi-Dirac Statistics**|**5**|
|**3**<br>**The Degenerate Fermi Gas (Zero-Point Energy, Pressure & Fermi Energy)**|**8**|



1 

GATE PHYSICS 

<u>QUANTUM</u> STATISTICS & DEGENERATE GAS 

### **1 Classical vs. Quantum Statistics & Indistinguishability** 

#### **1. Core Theory** 

Statistical mechanics describes macroscopic systems by averaging over microscopic configurations. The fundamental distinction between classical and quantum statistics lies in the **indistinguishability** of identical particles and the quantum mechanical constraints placed on their wave functions: 

-  **Maxwell-Boltzmann (MB) Statistics (Classical):** Identical particles are treated as **distinguishable** . Each particle can be labeled and tracked. There are no restrictions on the number of particles that can occupy any single-particle microstate. Classically, phase space coordinates are continuous. 

-  **Quantum Statistics (Bose-Einstein & Fermi-Dirac):** Identical particles are completely **indistinguishable** . It is physically impossible to label or track individual particles. The state of the system is determined strictly by the occupancy numbers of the discrete quantum states. 

-  **The Wave Function Symmetry Constraint:** Under the exchange of any two identical particles, the total wave function of a quantum system must remain symmetric (for bosons) or antisymmetric (for fermions): 

_P_ ˆ12Ψ(1 _,_ 2) = _±_ Ψ(1 _,_ 2) 



<!-- Start of picture text -->
(1)<br><!-- End of picture text -->

#### **2. Mathematical Framework** 

* **The Three Distribution Functions:** The average number of particles _⟨ni⟩_ in a single-particle state with energy _ϵi_ at temperature _T_ is given by: 



<!-- Start of picture text -->
1<br><!-- End of picture text -->



<!-- Start of picture text -->
⟨ni⟩ = (2)<br>e β ( ϵi−µ ) +  a<br><!-- End of picture text -->

where _β_ = _kB_ <u>1</u> _T_<sup>,</sup><sup>_µ_isthechemicalpotential(orFermienergyinsomelimits),and</sup><sup>_a_definesthe</sup> statistics: 



<!-- Start of picture text -->
 a  = 0 : Maxwell-Boltzmann (MB) distribution:<br><!-- End of picture text -->



<!-- Start of picture text -->
⟨ni⟩MB =  e −β ( ϵi−µ ) (3)<br><!-- End of picture text -->



<!-- Start of picture text -->
 a  =  − 1 : Bose-Einstein (BE) distribution (for integer-spin bosons, S ∈{ 0 ,  1 ,  2 , . . . } ):<br>1<br>⟨ni⟩BE = (4)<br>e β ( ϵi−µ ) − 1<br><!-- End of picture text -->

The chemical potential for bosons must satisfy _µ < ϵ_ ground to avoid unphysical negative occupancies. 

 _a_ = +1 **:** Fermi-Dirac (FD) distribution (for half-integer spin fermions, _S ∈{_ 1 _/_ 2 _,_ 3 _/_ 2 _, . . . }_ ): 



<!-- Start of picture text -->
1<br>⟨ni⟩FD = (5)<br>e β ( ϵi−µ ) + 1<br><!-- End of picture text -->

* **The Classical Limit Condition:** Quantum statistics converge asymptotically to classical Maxwell-Boltzmann statistics in the high-temperature, low-density limit where: 



<!-- Start of picture text -->
e β ( ϵi−µ ) ≫ 1 = ⇒ N V λ 3 ≪ 1 (6)<br><!-- End of picture text -->

where _λ_ = _~~√~~_ 2 _πmkh BT_<sup>isthethermaldeBrogliewavelength.</sup> 

2 

GATE PHYSICS 

<u>QUANTUM</u> STATISTICS & DEGENERATE GAS 

#### **3. Derivation Milestones** 

Let us derive the number of ways, _W_ , of distributing _N_ identical particles among a set of energy levels, where each level _i_ has degeneracy _gi_ and contains _ni_ particles: 

##### 1. **Maxwell-Boltzmann (Distinguishable, No Constraints):** 



<!-- Start of picture text -->
WMB =  N ! � gi ni (7)<br>ni !<br>i<br><!-- End of picture text -->

To transition to the semi-classical indistinguishable limit (resolving Gibbs’ paradox), we divide by _N_ !: 



<!-- Start of picture text -->
WMB, corrected = � gi ni (8)<br>ni !<br>i<br><!-- End of picture text -->

2. **Bose-Einstein (Indistinguishable, Symmetric States):** Since particles are indistinguishable, the distribution of _ni_ bosons in _gi_ degenerate states is mathematically equivalent to placing _ni_ identical balls in _gi_ compartments separated by _gi −_ 1 identical partitions: 



<!-- Start of picture text -->
( ni  + gi − 1)!<br>WBE = � (9)<br>i ni !( gi − 1)!<br><!-- End of picture text -->

3. **Fermi-Dirac (Indistinguishable, Antisymmetric States):** Since each state can hold at most 1 fermion (Pauli Exclusion Principle), we must choose _ni_ occupied states out of _gi_ available degenerate states: 



<!-- Start of picture text -->
gi !<br>WFD = � (10)<br>i ni !( gi − ni )!<br><!-- End of picture text -->

#### **4. Problem-Solving Algorithm** 

##### **Evaluating Classical vs. Quantum Distinguishability Limits** 

1. **Identify the System Parameters:** Find the particle mass _m_ , temperature _T_ , and volume density _n_ = _N/V_ . 

2. **Calculate the Thermal de Broglie Wavelength (** _λ_ **):** 



<!-- Start of picture text -->
h<br>λ  = (11)<br>√ 2 πmkBT<br><!-- End of picture text -->

3. **Compute the Degeneracy Parameter (** _nλ_<sup>3</sup> **):** 

-  If _nλ_<sup>3</sup> _≪_ 1 (mean particle spacing is much larger than the quantum wavepacket size), the system is classical: use **Maxwell-Boltzmann** statistics. 

-  If _nλ_<sup>3</sup> _≥_ 1, the wavefunctions overlap significantly. Use **Bose-Einstein** for bosons and **Fermi-Dirac** for fermions. 

3 

GATE PHYSICS 

<u>QUANTUM</u> STATISTICS & DEGENERATE GAS 

#### **5. Connections to Observables** 

* **Pressure (** _P_ **):** The thermodynamic pressure is derived from the grand potential Φ _G_ = _−kBT_ ln Ξ: 



<!-- Start of picture text -->
P =  − = kBT ln Ξ (12)<br>� ∂∂V Φ G � T,µ V<br><!-- End of picture text -->

For quantum gases, the pressure relates to the internal energy density by: 



<!-- Start of picture text -->
P = 2 U (for non-relativistic particles) , P = 1 U (for relativistic particles) (13)<br>3 V 3 V<br><!-- End of picture text -->

* **Entropy (** _S_ **):** In quantum systems, the entropy approaches 0 as _T →_ 0, satisfying the Third Law. This is because the ground state becomes uniquely occupied (Ω _→_ 1 = _⇒ S →_ 0). 

#### **6. Crucial Pitfalls** 

##### **Statistics and Indistinguishability Errors** 

-  **Gibbs’ Paradox Oversight:** Forgetting to divide the classical Maxwell-Boltzmann partition function by _N_ ! when analyzing macroscopic ideal gases. This leads to nonextensive expressions for entropy. 

-  **The Bose-Einstein Chemical Potential Trap:** Allowing _µ >_ 0 for a free boson gas. Since the ground state energy is _ϵ_ 0 = 0, having _µ ≥_ 0 would yield a negative or infinite average occupancy, which is physically impossible. 

#### **7. Standard Textbook Systems** 

-  **The Blackbody Radiation Gas (Photon Gas):** A gas of massless spin-1 bosons with _µ_ = 0 (since photon number is not conserved). This system is used to illustrate Planck’s radiation law under Bose-Einstein statistics. 

-  **Liquid Helium-4 (**<sup>4</sup> **He):** A bosonic fluid that undergoes Bose-Einstein Condensation (BEC) at _Tλ ≈_ 2 _._ 17 K, transitioning into a zero-viscosity superfluid. 

4 

GATE PHYSICS 

<u>QUANTUM</u> STATISTICS & DEGENERATE GAS 

### **2 The Pauli Exclusion Principle & Fermi-Dirac Statistics** 

#### **1. Core Theory** 

* **The Pauli Exclusion Principle:** A fundamental quantum mechanical principle stating that no two identical fermions can occupy the same single-particle quantum state simultaneously. * **Physical Origin:** The spin-statistics theorem states that half-integer spin particles (fermions) must possess a completely antisymmetric total wavefunction. If two fermions were placed in the same state, swapping them would yield: 



<!-- Start of picture text -->
Ψ(1 ,  2) =  − Swap[Ψ(1 ,  2)] =  − Ψ(2 ,  1) =  − Ψ(1 ,  2) = ⇒ Ψ(1 ,  2) = 0 (14)<br><!-- End of picture text -->

The wavefunction vanishes, meaning such a state has zero probability of existence. This principle is responsible for the shell structure of atoms, the stability of bulk matter, and the unique properties of conductors. 

#### **2. Mathematical Framework** 



<!-- Start of picture text -->
* The Fermi-Dirac Distribution Function ( f ( ϵ ) ):<br><!-- End of picture text -->



<!-- Start of picture text -->
1<br>f ( ϵ ) = (15)<br>e β ( ϵ−µ ) + 1<br><!-- End of picture text -->

* **Behavior at Absolute Zero (** _T →_ 0 **):** As _T →_ 0 = _⇒ β →∞_ : 



<!-- Start of picture text -->
1 if ϵ < µ 0<br>f ( ϵ ) = (16)<br>�0 if ϵ > µ 0<br><!-- End of picture text -->

where _µ_ 0 _≡ ϵF_ is the **Fermi Energy** . At _T_ = 0, the fermions fill every single available energy level up to _ϵF_ , leaving all higher levels empty. This sharp boundary is called the **Fermi Surface**. * **Behavior at Finite Temperatures (** _T >_ 0 **):** Thermal excitation blurs the Fermi surface over an energy band of width _∼ kBT_ centered around _µ_ : 



<!-- Start of picture text -->
1<br>f ( µ ) = (17)<br>e 0 + 1 = 2 1<br><!-- End of picture text -->

At any temperature, the occupancy at the chemical potential is exactly 1 _/_ 2. 

#### **3. Derivation Milestones** 

Let us derive the Fermi-Dirac distribution using the Grand Canonical Ensemble: 

1. **Write the Single-Particle Partition Function (** _ξi_ **):** For a single quantum state _i_ , the Pauli principle restricts the allowed occupancy to _ni ∈{_ 0 _,_ 1 _}_ . The grand partition function of this state is: 



<!-- Start of picture text -->
1<br>ξi = � e −βni ( ϵi−µ ) = 1 +  e −β ( ϵi−µ ) (18)<br>ni =0<br><!-- End of picture text -->

2. **Determine the Average Occupancy (** _⟨ni⟩_ **):** Using the grand canonical derivative relation: 



<!-- Start of picture text -->
⟨ni⟩ =  − 1 ∂ ln ξi = 1 ∂ ln (19)<br>β ∂ϵi β ∂ϵi �1 +  e −β ( ϵi−µ )�<br><!-- End of picture text -->

5 

GATE PHYSICS 

<u>QUANTUM</u> STATISTICS & DEGENERATE GAS 

##### 3. **Evaluate the Derivative:** 



<!-- Start of picture text -->
⟨ni⟩ = 1 −βe −β ( ϵi−µ ) e −β ( ϵi−µ ) (20)<br>β 1 +  e −β ( ϵi−µ ) = 1 +  e −β ( ϵi−µ )<br><!-- End of picture text -->

4. **Multiply Denominator and Numerator by** _e_<sup>_β_(</sup><sup>_ϵi−µ_)</sup> **:** 



<!-- Start of picture text -->
1<br>⟨ni⟩ = (21)<br>e β ( ϵi−µ ) + 1<br><!-- End of picture text -->

which is the Fermi-Dirac distribution. 

#### **4. Problem-Solving Algorithm** 

##### **Calculating Occupancy and Excitation Fractions** 

To calculate the occupancy probability at a specific energy level _ϵ_ at finite temperature _T_ : 

1. **Identify the Fermi Energy (** _ϵF_ **or** _µ_ **) and Temperature (** _T_ **):** Calculate the thermal energy _kBT_ . 

2. **Express the Energy Difference:** Compute ∆= _ϵ − µ_ . 3. **Evaluate the Distribution Exponential:** 1 

_f_ ( _ϵ_ ) = (22) _e_<sup>∆</sup><sup>_/kBT_</sup> + 1 

4. **For Symmetric States:** Note that the occupancy of a state at _µ_ + _δ_ and the vacancy at _µ − δ_ are symmetric: 1 _− f_ ( _µ − δ_ ) = _f_ ( _µ_ + _δ_ ) (23) 

#### **5. Connections to Observables** 

* **Electronic Specific Heat (** _C_ **el):** At low temperatures ( _T ≪ TF_ ), only fermions within _∼ kBT_ of the Fermi surface can absorb thermal energy. The number of active fermions scales as _N_ active _≈ N_ ( _kBT/ϵF_ ). This directly suppresses the electronic specific heat, making it linear with temperature: 



<!-- Start of picture text -->
kB<br>C el =  γT ∝ T (where γ = π 2 2 NkB ϵF ) (24)<br><!-- End of picture text -->

This resolves the classical paradox where the classical Dulong-Petit law predicted a temperatureindependent electronic specific heat of 3 _/_ 2 _NkB_ . 

6 

GATE PHYSICS 

<u>QUANTUM</u> STATISTICS & DEGENERATE GAS 

#### **6. Crucial Pitfalls** 

##### **Fermi-Dirac Distribution Traps** 

-  **Assuming** _µ_ **is Constant with Temperature:** Believing that the chemical potential _µ_ ( _T_ ) is exactly equal to the Fermi energy _ϵF_ at all temperatures. In fact, _µ_ ( _T_ ) decreases slightly as temperature rises according to the Sommerfeld expansion: 



<!-- Start of picture text -->
µ ( T )  ≈ ϵF 1  − π 2 (25)<br>12 � kϵBFT<br>� �2 �<br><!-- End of picture text -->

-  **Ignoring Spin Degeneracy:** Forgetting the factor of (2 _S_ +1) (equal to 2 for spin-1/2 electrons) when calculating the density of states. 

#### **7. Standard Textbook Systems** 

-  **The Free Electron Gas in Metals:** Conduction electrons are treated as non-interacting fermions moving in a constant potential background, demonstrating linear specific heat. 

-  **Semiconductors (Intrinsic Carrier Concentration):** The Fermi level lies in the band gap, and the tail of the Fermi-Dirac distribution extending into the conduction band is approximated by Maxwell-Boltzmann statistics. 

7 

GATE PHYSICS 

<u>QUANTUM</u> STATISTICS & DEGENERATE GAS 

### **3 The Degenerate Fermi Gas (Zero-Point Energy, Pressure & Fermi Energy)** 

#### **1. Core Theory** 

* **Degenerate Fermi Gas:** A system of fermions at temperatures far below the Fermi temperature ( _T ≪ TF ≡ ϵF /kB_ ). In this regime, the system’s physical properties are dominated by quantum mechanics and the Pauli exclusion principle rather than thermal motion. * **Degeneracy Pressure:** The outward pressure exerted by a degenerate Fermi gas, which persists even at absolute zero temperature ( _T_ = 0 K). It does not originate from thermal kinetic collisions or electrostatic repulsion; instead, it is a purely quantum-mechanical consequence of the Pauli principle. Since no two fermions can occupy the same momentum state, compressing the gas forces the fermions into high-momentum states, yielding a massive **zero-point kinetic energy** and a corresponding outward pressure. 

#### **2. Mathematical Framework** 

For a 3D non-relativistic degenerate Fermi gas of spin-1/2 particles of mass _m_ : * **Density of States (** _g_ ( _E_ ) **):** 



<!-- Start of picture text -->
g ( E ) dE = V E 1 / 2 dE (26)<br>2 π 2 � 2ℏ m 2 �3 / 2<br><!-- End of picture text -->



<!-- Start of picture text -->
* Fermi Energy ( ϵF  ): Derived by setting �0 ϵF g ( E ) dE =  N :<br><!-- End of picture text -->



<!-- Start of picture text -->
ϵF = ℏ2 3 π 2 N = ℏ2 �3 π 2 n �2 / 3 (27)<br>2 m � V �2 / 2 2 m<br><!-- End of picture text -->

* **Fermi Wavevector (** _kF_ **) and Momentum (** _pF_ **):** 



<!-- Start of picture text -->
kF = 3 π 2 N , pF = ℏ kF = ℏ 3 π 2 N (28)<br>� V �1 / 3 � V �1 / 3<br><!-- End of picture text -->

* **Zero-Point Internal Energy (** _U_ 0 **):** The total kinetic energy of the gas at _T_ = 0 K: 



<!-- Start of picture text -->
U 0 = �0 ϵF Eg ( E ) dE = 5 3 NϵF (29)<br><!-- End of picture text -->

* **Degeneracy Pressure (** _P_ 0 **):** The pressure of the gas at _T_ = 0 K: 



<!-- Start of picture text -->
P 0 = 2 U 0 N �3 π 2�2 / 3 (30)<br>3 V = 5 2 V ϵF = 5 ℏ m 2 � NV �5 / 3<br><!-- End of picture text -->

Note that _P_ 0 _∝ n_<sup>5</sup><sup>_/_3</sup> , indicating a strong dependence on particle density. 

#### **3. Derivation Milestones** 

Let us derive the Fermi energy and zero-point energy of a 3D degenerate Fermi gas at _T_ = 0 K: 

8 

GATE PHYSICS 

<u>QUANTUM</u> STATISTICS & DEGENERATE GAS 

1. **Map the Momentum Space (k-space):** Due to boundary conditions in a box of volume _V_ = _L_<sup>3</sup> , the allowed wavevector states are spaced by _π/L_ . The volume of a single state in k-space is ( _π/L_ )<sup>3</sup> = _π_<sup>3</sup> _/V_ . The number of states with wavevector magnitude less than _k_ in the positive octant is: 



<!-- Start of picture text -->
Nk = 2  × 81 � 43 πk 3� =  V k 3 (31)<br>π 3 /V 6 π 2<br><!-- End of picture text -->

where the leading factor of 2 accounts for the spin-1/2 states. 

2. **Relate Particle Count to the Fermi Wavevector (** _kF_ **):** At _T_ = 0, the ground state is constructed by filling all states up to _k_ = _kF_ : 



<!-- Start of picture text -->
F<br>N =  V 3 k π 32 = ⇒ kF = �3 π 2 N V �1 / 3 (32)<br><!-- End of picture text -->

3. **Calculate the Fermi Energy (** _ϵF_ **):** Substitute the dispersion relation _ϵ_ =<sup><u>ℏ</u></sup> 2<sup>2</sup> _m_<sup>_<u>k</u>_2at</sup><sup>_k_=</sup><sup>_kF_:</sup> 



<!-- Start of picture text -->
F<br>ϵF = ℏ2 k 2 3 π 2 N (33)<br>2 m = 2 ℏ m 2 � V �2 / 3<br><!-- End of picture text -->

4. **Integrate to find the Total Internal Energy (** _U_ 0 **):** 



<!-- Start of picture text -->
ℏ 2 k 2 k 5<br>F<br>U 0 = 2 � 2 m = 2 � 8 Vπ 3 ��0 kF � ℏ22 mk 2 � 4 πk 2 dk = 2 V π  ℏ2 m 2 5 (34)<br>k≤kF<br><!-- End of picture text -->

Using _N_ = _V kF_<sup>3</sup><sup>_/_3</sup><sup>_π_2,wesimplifythisexpressionto:</sup> 



<!-- Start of picture text -->
F<br>U 0 = 3 = 3 (35)<br>5 N � ℏ22 mk 2 � 5 NϵF<br><!-- End of picture text -->

#### **4. Problem-Solving Algorithm** 

##### **Solving Degenerate Fermi Gas Numerical Problems** 

1. **Identify the Spatial Dimension (** _d_ **):** Check if the system is 1D, 2D, or 3D, as the density of states depends on the dimension: 

   -  1D: _g_ ( _E_ ) _∝ E_<sup>_−_1</sup><sup>_/_2</sup> = _⇒ ϵF ∝ n_<sup>2</sup> 

   -  2D: _g_ ( _E_ ) _∝_ Constant = _⇒ ϵF ∝ n_<sup>1</sup> 

   -  3D: _g_ ( _E_ ) _∝ E_<sup>1</sup><sup>_/_2</sup> = _⇒ ϵF ∝ n_<sup>2</sup><sup>_/_3</sup> 

2. **Calculate the Density (** _n_ = _N/V_ **or** _N/L_<sup>_d_</sup> **):** Note the particle density and spin degeneracy. 

3. **Determine the Fermi Parameters:** Calculate the Fermi energy _ϵF_ , momentum _pF_ =<sup>_~~√~~_</sup> 2 _mϵF_ , and temperature _TF_ = _ϵF /kB_ . 

4. **Calculate Zero-Point Properties:** Use _U_ 0 = _d_ +2 _<u>d</u>_<sup>_NϵF_tofindthezero-pointenergy</sup> in _d_ dimensions. 

9 

GATE PHYSICS 

<u>QUANTUM</u> STATISTICS & DEGENERATE GAS 

#### **5. Connections to Observables** 

* **Bulk Modulus (** _B_ **):** The stiffness or resistance to compression of a degenerate gas: 



<!-- Start of picture text -->
B ≡−V = 5 (36)<br>� ∂V∂P � 3 P 0<br><!-- End of picture text -->

This indicates that a Fermi gas possesses a massive, temperature-independent mechanical resistance to compression even at absolute zero. * **Paramagnetic Susceptibility (Pauli Paramagnetism):** Applying a magnetic field _B_ shifts the energy of up-spins and down-spins, creating a net magnetization. Since only conduction electrons near the Fermi surface can flip their spins, the resulting susceptibility is temperature-independent: 



<!-- Start of picture text -->
χ Pauli =  µ 2 B g ( ϵF ) = 3 N µ B 2 (37)<br>2 ϵF<br><!-- End of picture text -->

#### **6. Crucial Pitfalls** 

##### **Degeneracy and Relativistic Traps** 

-  **The Relativistic Transition Error:** Using the non-relativistic formula _ϵF ∝ n_<sup>2</sup><sup>_/_3</sup> and _P_ 0 _∝ n_<sup>5</sup><sup>_/_3</sup> for ultra-relativistic systems (e.g., in massive stars where particle speeds approach the speed of light _c_ ). For ultra-relativistic particles, the dispersion relation is _ϵ_ = _pc_ , yielding: 



<!-- Start of picture text -->
U 0<br>ϵF = ℏ c �3 π 2 n �1 / 3  , P 0 = 1 (38)<br>3 V ∝ n 4 / 3<br><!-- End of picture text -->

Because the pressure scaling drops from _n_<sup>5</sup><sup>_/_3</sup> to _n_<sup>4</sup><sup>_/_3</sup> , relativistic stars become highly unstable against gravitational collapse. 

-  **Dimensional Neglect:** Attempting to use the 3D average energy formula _U_ 0 = 5<sup><u>3</u></sup><sup>_NϵF_</sup> for a 1D or 2D system. Always re-derive or check the dimensional factor. 

#### **7. Standard Textbook Systems** 

-  **White Dwarf Stars (Chandrasekhar Limit):** Stars that have exhausted their nuclear fuel and are held stable against gravitational collapse exclusively by the **degeneracy pressure of electrons**. If the star’s mass exceeds the **Chandrasekhar limit** ( _≈_ 1 _._ 4 _M⊙_ ), electron degeneracy pressure is overcome, and the star collapses. 

-  **Neutron Stars:** Ultra-dense stellar remnants supported against gravity by **neutron degeneracy pressure**. 

10 

GATE PHYSICS 

<u>QUANTUM</u> STATISTICS & DEGENERATE GAS 

### **References** 

1. Huang, Kerson. _Statistical Mechanics_ . Wiley, 1987. 

2. Prakash, Satya. _Statistical Mechanics_ . Kedar Nath Ram Nath, 2019. 

3. Beiser, Arthur. _Concepts of Modern Physics_ . McGraw-Hill, 2003. 

11 

BEC & Blackbody Radiation 

GATE Physics Exam Study Guide 

## **GATE Physics Graduate Study Notes Bose-Einstein Condensation & Thermodynamics of Blackbody Radiation** 

_Prepared by Expert GATE Physics Faculty_ 

### **1 Topic 1: Bose-Einstein Condensation (BEC) & Critical Temperature** 

#### **1. Core Theory** 

**Bose-Einstein Condensation (BEC)** is a quantum phase transition occurring in a gas of noninteracting or weakly interacting bosons (particles with integer spin, such as<sup>4</sup> He atoms or alkali metal vapours) when cooled below a specific **critical temperature** _Tc_ . 

**Physical Significance:** Unlike classical particles, bosons are not restricted by the Pauli exclusion principle, and multiple particles can occupy the same quantum state. As the temperature drops towards absolute zero, the thermal de Broglie wavelength _λ_ of the bosons expands until it becomes comparable to the average interparticle spacing _d_ = ( _V/N_ )<sup>1</sup><sup>_/_3</sup> . At this juncture, the individual wave packets of the bosons begin to overlap and merge, undergoing a phase transition. A macroscopically large fraction of the total number of bosons (up to 100% at 0 K) suddenly falls into the singleparticle ground state ( _ϵ_ 0 = 0), acting as a single, giant, coherent quantum wave packet described by a macroscopic wavefunction. This is a purely quantum-mechanical transition driven solely by Bose-Einstein statistics and phase-space density requirements, in the complete absence of any interparticle attractive forces. 

#### **2. Mathematical Framework** 

The statistics and onset of BEC are governed by the following relations: 

 **Bose-Einstein Occupancy (Average Number of Particles in State** _ϵi_ **):** 



<!-- Start of picture text -->
1<br>⟨ni⟩ = (1)<br>e β ( ϵi−µ ) − 1<br><!-- End of picture text -->

where _β_ = _kB_ <u>1</u> _T_<sup>istheinversetemperatureand</sup><sup>_µ_isthechemicalpotential.</sup> 

 **Chemical Potential Constraint:** To ensure that the average occupancy is positive for all states, _µ_ must always be less than the ground-state energy: 



<!-- Start of picture text -->
µ < ϵ 0 = 0 (2)<br><!-- End of picture text -->

As the temperature _T_ decreases at constant density _n_ = _N/V_ , the chemical potential _µ_ ( _T_ ) rises from its negative high-temperature classical value towards 0. The condensation transition begins exactly when the chemical potential touches the ground state: 



<!-- Start of picture text -->
µ ( Tc ) = 0 (3)<br><!-- End of picture text -->

1 

BEC & Blackbody Radiation 

GATE Physics Exam Study Guide 

 **Total Particle Count Decomposition (** _N_ **):** 



<!-- Start of picture text -->
N =  N 0 +  Ne (4)<br><!-- End of picture text -->

where _N_ 0 is the number of particles in the ground state ( _ϵ_ 0 = 0), and _Ne_ is the number of particles in all excited states ( _ϵi >_ 0): 



<!-- Start of picture text -->
1 1<br>N 0 = Ne = g ( ϵ ) (5)<br>e −βµ − 1 , �0 ∞ e β ( ϵ−µ ) − 1 dϵ<br><!-- End of picture text -->

where _g_ ( _ϵ_ ) is the single-particle density of states. 

 **Density of States in 3D (** _g_ ( _ϵ_ ) **):** For a non-relativistic particle of mass _m_ in a 3D box of volume _V_ : 



<!-- Start of picture text -->
g ( ϵ ) dϵ  = 2 πV ϵ 1 / 2 dϵ (6)<br>h 3 (2 m )3 / 2 ϵ 1 / 2 dϵ  = 4 V π 2 � 2ℏ m 2 �3 / 2<br><!-- End of picture text -->

 **The Bose Integral (Polylogarithm function** _gs_ ( _z_ ) **):** 



<!-- Start of picture text -->
1 x s− 1 ∞ z k<br>gs ( z ) = Γ( s ) �0 ∞ z − 1 e x − 1 dx  = � k s (7)<br>k =1<br><!-- End of picture text -->

where Γ( _s_ ) is the Euler Gamma function, and _z ≡ e_<sup>_βµ_</sup> is the fugacity. At the onset of condensation ( _T ≤ Tc_ ), _z_ = 1, and the function simplifies to the Riemann Zeta function _ζ_ ( _s_ ): 



<!-- Start of picture text -->
g 3 / 2(1) =  ζ (3 / 2)  ≈ 2 . 612 , g 5 / 2(1) =  ζ (5 / 2)  ≈ 1 . 341 (8)<br><!-- End of picture text -->

-  **Critical Temperature (** _Tc_ **):** The temperature below which excited states can no longer accommodate the entire particle population _N_ at a given volume _V_ : 



<!-- Start of picture text -->
Tc = h 2 N ≈ 3 . 31ℏ2 (9)<br>2 πmkB � V ζ (3 / 2) �2 / 3 mkB � NV �2 / 3<br><!-- End of picture text -->

 **Condensate Fraction (for** _T < Tc_ **):** 



<!-- Start of picture text -->
N 0( T )<br>= 1  − (10)<br>N � TTc �3 / 2<br><!-- End of picture text -->

 **Excited Fraction (for** _T < Tc_ **):** 



<!-- Start of picture text -->
Ne ( T )<br>=<br>(11)<br>N � TTc �3 / 2<br><!-- End of picture text -->

2 

BEC & Blackbody Radiation 

GATE Physics Exam Study Guide 

#### **3. Derivation Milestones** 

The derivation of the critical temperature and condensate fraction consists of these key steps: 

1. **Isolate the Ground State:** Formulate the total particle number relation. Since _g_ ( _ϵ_ = 0) = 0, continuous integration over excited states completely ignores the ground-state population. We must write the discrete sum as: 



<!-- Start of picture text -->
1<br>N =  N 0 + �0 ∞ g ( ϵ ) e β ( ϵ−µ ) − 1 dϵ (12)<br><!-- End of picture text -->

2. **Set the Condensation Boundary Condition:** Set _µ_ = 0 (meaning fugacity _z_ = 1) and _N_ 0 _≈_ 0 to define the absolute upper limit of particles that the excited states can hold. This defines the critical point where the excited states are completely saturated: 



<!-- Start of picture text -->
V 1<br>N = ϵ 1 / 2 (13)<br>�0 ∞ � 4 π 2 � 2ℏ m 2 �3 / 2 � e ϵ/kBTc − 1 dϵ<br><!-- End of picture text -->

3. **Evaluate the Integral using substitution (** _x ≡ ϵ/kBTc_ **):** 



<!-- Start of picture text -->
N = V ( kBTc ) 3 / 2 x 1 / 2 (14)<br>4 π 2 � 2ℏ m 2 �3 / 2 �0 ∞ e x − 1 dx<br><!-- End of picture text -->

_<u>x</u>_<sup>1</sup><sup>_/_2</sup> _~~<u>√</u>~~_ _<u>π</u>_ Recognizing that �0 _∞ e_<sup>_<u>x</u>_</sup> _−_ 1<sup>_dx_= Γ(3</sup><sup>_/_2)</sup><sup>_ζ_(3</sup><sup>_/_2) =</sup> 2<sup>_ζ_(3</sup><sup>_/_2):</sup> 



<!-- Start of picture text -->
N =  V ζ (3 / 2) = V ζ (3 / 2) (15)<br>� 2 πmkh 2 BTc �3 / 2 λ 3 c<br><!-- End of picture text -->

where _λc_ is the thermal de Broglie wavelength at _Tc_ . 

4. **Invert to find** _Tc_ **and the Condensate Fraction:** Isolating _Tc_ yields the critical temperature formula. For _T < Tc_ , since _µ_ remains pinned at 0, the excited state population is: 



<!-- Start of picture text -->
Ne ( T ) =  V ζ (3 / 2) (16)<br>� 2 πmkh 2 BT �3 / 2<br><!-- End of picture text -->



<!-- Start of picture text -->
Dividing by N =  V � 2 πmkh 2 BTc �3 / 2 ζ (3 / 2) gives:<br>Ne ( T )<br>= = ⇒ N 0( T ) = 1  − (17)<br>N � TTc �3 / 2 N � TTc �3 / 2<br><!-- End of picture text -->

#### **4. Problem-Solving Algorithm** 

To solve numerical and analytical questions on BEC: 

1. **Identify the Spatial Dimension (** _d_ **):** Check the system’s dimensionality, as it completely alters the density of states exponent _s_ in _g_ ( _ϵ_ ) _∝ ϵ_<sup>_s−_1</sup> . 

3 

BEC & Blackbody Radiation 

GATE Physics Exam Study Guide 

   -  In a 3D system: _g_ ( _ϵ_ ) _∝ ϵ_<sup>1</sup><sup>_/_2</sup> , leading to an integration exponent of 3 _/_ 2. Thus, _Tc ∝ n_<sup>2</sup><sup>_/_3</sup> and _N_ 0 _/N_ = 1 _−_ ( _T/Tc_ )<sup>3</sup><sup>_/_2</sup> . 

   -  In a 2D system: _g_ ( _ϵ_ ) _∝_ Constant, meaning the excited state integral diverges logarithmically as _µ →_ 0. **Consequently, BEC cannot occur in a 2D uniform system at any non-zero temperature (** _Tc_ = 0 **).** 

   -  In a 1D system: _g_ ( _ϵ_ ) _∝ ϵ_<sup>_−_1</sup><sup>_/_2</sup> , preventing condensation ( _Tc_ = 0). 

2. **Determine the dispersion relation:** Check if the particles are non-relativistic ( _ϵ ∝ p_<sup>2</sup> ) or ultra-relativistic ( _ϵ ∝ p_ ). This changes the density of states and the corresponding critical exponent. 

3. **Calculate the Critical Temperature (** _Tc_ **):** For a standard 3D non-relativistic system, substitute the particle mass _m_ and number density _n_ = _N/V_ into the critical temperature equation. Ensure all parameters are converted to consistent SI units (or CGS if specified). 

4. **Evaluate the Condensate Population at a Given Temperature** _T < Tc_ **:** Use the condensate fraction formula to find the ratio _N_ 0 _/N_ , and multiply by the total particle count _N_ to find the exact number of condensed particles. 

#### **5. Connections to Observables** 

-  **Specific Heat (** _CV_ **):** 

   - For _T < Tc_ , since _N_ 0 does not contribute to the thermal energy, the internal energy is _U_ ( _T_ ) _∝ T_<sup>5</sup><sup>_/_2</sup> . Thus, the specific heat is: 



<!-- Start of picture text -->
CV  ( T ) = 15 4 kBN ζ ζ ( (3 5 / / 2 2) ) � TTc �3 / 2 ≈ 1 . 925 NkB � TTc �3 / 2 (18)<br><!-- End of picture text -->

   - At _T_ = _Tc_ , the specific heat exhibits a **cusp** (a continuous peak but with a discontinuous derivative, displaying a _λ_ -like profile). 

   - For _T > Tc_ , the specific heat decreases and asymptotically approaches the classical limit: lim _T →∞ CV_ =<sup><u>3</u></sup> 2<sup>_NkB_.</sup> 

-  **Entropy (** _S_ **):** For _T < Tc_ : 



<!-- Start of picture text -->
S ( T ) = 5 ∝ T 3 / 2 (19)<br>2 kBN ζ ζ ( (3 5 / / 2 2) ) � TTc �3 / 2<br><!-- End of picture text -->

As _T →_ 0, _S →_ 0 in accordance with the Third Law of Thermodynamics. 

-  **Pressure (** _P_ **):** For _T < Tc_ , the pressure of the gas is entirely independent of the volume _V_ and depends only on temperature: 



<!-- Start of picture text -->
U<br>P ( T ) = 2 ∝ T 5 / 2 (20)<br>3 V =  kBT ζ ( λ 5 / 32)<br><!-- End of picture text -->

#### **6. Crucial Pitfalls** 

4 

BEC & Blackbody Radiation 

GATE Physics Exam Study Guide 

##### **Bose-Einstein Condensation Traps** 

-  **The 2D Uniform BEC Fallacy:** Assuming that a 2D uniform non-interacting Bose gas can undergo BEC at finite temperature. In 2D, the density of states is constant ( _g_ ( _ϵ_ ) _∝ ϵ_<sup>0</sup> ). The excited state integral diverges as _µ →_ 0, meaning the excited states can accommodate an infinite number of particles at any non-zero temperature, preventing a macroscopic ground-state condensation ( _Tc_ = 0). Note, however, that BEC _can_ occur in a 2D system if the particles are confined in a harmonic trap, which modifies the effective density of states. 

-  **Ignoring Ground-State Population in excited integrals:** Evaluating the excited state integral with _µ_ = 0 and assuming it represents the total particle population at all temperatures. This is only valid at and above _Tc_ . Below _Tc_ , the excited integral strictly yields _Ne < N_ , and the remaining particles ( _N −Ne_ ) reside in the ground state. 

#### **7. Standard Textbook Systems** 

-  **The Non-Interacting 3D Bose Gas in a Box:** The benchmark system of non-relativistic particles of mass _m_ confined to a volume _V_ with _g_ ( _ϵ_ ) _∝ ϵ_<sup>1</sup><sup>_/_2</sup> . 

-  **Harmonically Trapped Bosons (3D):** A system of bosons in a 3D isotropic harmonic potential _V_ ( _r_ ) = 2<sup><u>1</u></sup><sup>_mω_2</sup><sup>_r_2.Thetrappingpotentialaltersthedensityofstatesto</sup><sup>_g_(</sup><sup>_ϵ_)</sup><sup>_∝ϵ_2.</sup> This alters the critical parameters: 



<!-- Start of picture text -->
N 0( T )<br>Tc ∝ N 1 / 3 , = 1  − (21)<br>N � TTc �3<br><!-- End of picture text -->

5 

BEC & Blackbody Radiation 

GATE Physics Exam Study Guide 

### **2 Topic 2: Thermodynamics of Blackbody Radiation** 

#### **1. Core Theory** 

A **blackbody** is an idealized physical body that completely absorbs all electromagnetic radiation incident upon it, regardless of frequency or angle of incidence. When in thermodynamic equilibrium at temperature _T_ , a blackbody emits a continuous spectrum of electromagnetic radiation, known as **blackbody radiation** . 

**Physical Significance:** Blackbody radiation represents the equilibrium state of an electromagnetic field in a cavity, behaving as a gas of massless, non-interacting bosons ( **Photons** ) with a non-conserved particle count. Because photons can be created or destroyed at the cavity walls to maintain thermal equilibrium, the chemical potential of a photon gas is strictly zero: 

_µ_ = 0 (22) 

Historically, classical physics (the Rayleigh-Jeans law, based on the equipartition theorem) predicted that the energy density would diverge quadratically at high frequencies ( _ρ_ ( _ν_ ) _∝ ν_<sup>2</sup> ), a failure known as the **Ultraviolet Catastrophe** . Max Planck resolved this by postulating that electromagnetic energy is quantized in discrete packets, or quanta, of energy _E_ = _hν_ , marking the birth of quantum mechanics. 

#### **2. Mathematical Framework** 

The thermodynamics of a photon gas are governed by the following laws: 

-  **Planck’s Law of Radiation:** The spectral energy density _ρ_ ( _ν, T_ ) (energy per unit volume per unit frequency) of a blackbody at temperature _T_ is: 



<!-- Start of picture text -->
1<br>ρ ( ν, T ) dν = 8 πhν 3 (23)<br>c 3 e hν/kBT − 1 dν<br><!-- End of picture text -->

In terms of wavelength _λ_ (where _ν_ = _c/λ_ and _dν_ = _− λ_<sup>_<u>c</u>_2</sup><sup>_dλ_):</sup> 



<!-- Start of picture text -->
ρ ( λ, T ) dλ  = 8 πhc 1 (24)<br>λ 5 e hc/λkBT − 1 dλ<br><!-- End of picture text -->

-  **Wien’s Displacement Law:** The wavelength _λ_ max at which the spectral energy density peaks is inversely proportional to the absolute temperature: 



<!-- Start of picture text -->
λ max T =  b ≈ 2 . 898  ×  10 − 3 m  ·  K (25)<br><!-- End of picture text -->

where _b_ is Wien’s displacement constant. 

-  **The Stefan-Boltzmann Law:** The total energy radiated per unit surface area of a blackbody per unit time (the emissive power _E_ total) is directly proportional to the fourth power of its absolute temperature: 



<!-- Start of picture text -->
E total =  σT 4 (26)<br><!-- End of picture text -->

where _σ_ is the Stefan-Boltzmann constant: 



<!-- Start of picture text -->
B<br>σ = 15 2 π c 52 k h 43 ≈ 5 . 670  ×  10 − 8 W  ·  m − 2  ·  K − 4 (27)<br><!-- End of picture text -->

6 

BEC & Blackbody Radiation 

GATE Physics Exam Study Guide 

 **Total Energy Density (** _u_ = _U/V_ **):** 



<!-- Start of picture text -->
u ( T ) = ρ ( ν, T ) dν =  aT 4 where a  = 4 σ B (28)<br>�0 ∞ c = 15 8 π c 53 k h 43<br><!-- End of picture text -->

-  **Radiation Pressure (** _P_ **):** Because photons are ultra-relativistic ( _E_ = _pc_ ), the pressure exerted by a photon gas on the cavity walls is: 



<!-- Start of picture text -->
P = 1 (29)<br>3 u  = 1 3 aT  4<br><!-- End of picture text -->

#### **3. Derivation Milestones** 

The mathematical derivation of these radiation laws consists of these key steps: 

1. **Formulate the Density of States in a Cavity:** The number of electromagnetic wave modes (standing waves) in a 3D cavity of volume _V_ within frequency range [ _ν, ν_ + _dν_ ], incorporating a factor of 2 for the two independent transverse polarization states of photons: 



<!-- Start of picture text -->
g ( ν ) dν = 2  × 4 πV ν 2 dν = 8 πV ν 2 dν (30)<br>c 3 c 3<br><!-- End of picture text -->

2. **Integrate over the Planck Distribution:** Multiply the density of states per unit volume by the average energy of a quantum harmonic oscillator of frequency _ν_ in thermal equilibrium, given by the Planck energy expectation _⟨E⟩_ = _e_<sup>_hν/kBT_</sup> _<u>hν</u> −_ 1<sup>(where</sup><sup>_µ_= 0):</sup> 



<!-- Start of picture text -->
ρ ( ν, T ) dν = g ( ν ) ⟨E⟩dν = 8 πν 2 hν dν = 8 πhν 3 1 (31)<br>V c 3 � e hν/kBT − 1 � c 3 e hν/kBT − 1 dν<br><!-- End of picture text -->

3. **Derive Stefan’s Law via Integration over all Frequencies:** Calculate total energy density _u_ ( _T_ ) = �0 _∞_<sup>_ρ_(</sup><sup>_ν, T_)</sup><sup>_dν_:</sup> 



<!-- Start of picture text -->
u ( T ) = 8 πh ν 3 (32)<br>c 3 �0 ∞ e hν/kBT − 1 dν<br><!-- End of picture text -->

Using substitution _x_ = _khνBT_<sup>=</sup><sup>_⇒dν_=</sup><sup>_<u>kB</u>_</sup> _h_<sup>_Tdx_:</sup> 



<!-- Start of picture text -->
u ( T ) = 8 πh x 3 (33)<br>c 3 � kBhT �4 �0 ∞ e x − 1 dx<br><!-- End of picture text -->

The definite integral is �0 _∞ e_<sup>_<u>x</u>_</sup> _<u>x−</u>_<sup>3</sup> 1<sup>_dx_= Γ(4)</sup><sup>_ζ_(4) = 6</sup> _<u>π</u>_ 90<sup>4</sup> =<sup>_<u>π</u>_</sup> 15<sup>4.Substitutingthisvalue:</sup> � � _<u>B</u> u_ ( _T_ ) = 15<sup>8</sup><sup>_π_</sup> _c_<sup>53</sup><sup>_k_</sup> _h_<sup>43</sup><sup>_T_4=</sup><sup>_aT_4=</sup><sup>_⇒E_total=</sup> 4<sup>_cu_(</sup><sup>_T_) =</sup><sup>_σT_4</sup> (34) 

4. **Derive Wien’s Law via Extremum Differentiation:** To find the peak wavelength, differentiate _ρ_ ( _λ, T_ ) with respect to _λ_ and set to zero: 



<!-- Start of picture text -->
d<br>e hc/λkBT − 1 = 0 (35)<br>dλ � λ − 5 � � − 1 �<br><!-- End of picture text -->

7 

BEC & Blackbody Radiation 

GATE Physics Exam Study Guide 

Substituting _y ≡ λkhcBT_<sup>leadstothetranscendentalequation:</sup> _<u>ye</u>_<sup>_y_</sup> _e_<sup>_y_</sup> _−_ 1<sup>= 5=</sup><sup>_⇒y≈_4</sup><sup>_._965</sup> (36) 

Thus, _λ_ max = 4 _._ 965 _<u>hckBT</u>_<sup>=</sup> _T_<sup>_<u>b</u>_,provingWien’sdisplacementlaw.</sup> 

#### **4. Problem-Solving Algorithm** 

To approach blackbody radiation problems: 

1. **Check the Given Parameter (Frequency vs. Wavelength):** Make sure to use the correct peak form. Note that the peak frequency _ν_ max is **NOT** simply _c/λ_ max. 

   -  For peak wavelength: Differentiating _ρ_ ( _λ, T_ ) gives: 

_hc λ_ max _kBT_<sup>_≈_4</sup><sup>_._965</sup> (37) 

 For peak frequency: Differentiating _ρ_ ( _ν, T_ ) gives: 

_hν_ max _≈_ 2 _._ 822 (38) _kBT_ 

2. **Apply the Stefan-Boltzmann Power Relation:** For a blackbody of surface area _A_ and emissivity _e_ (where _e_ = 1 for an ideal blackbody): 

_P_ radiated = _eσAT_<sup>4</sup> (39) 

If the body is in an environment at temperature _T_ 0, the net power radiated is: 

_P_ net = _eσA_ ( _T_<sup>4</sup> _− T_ 0<sup>4)</sup> (40) 

3. **Evaluate Dimensional Scaling:** In _d_ dimensions, the blackbody energy density scales as: _ud_ ( _T_ ) _∝ T_<sup>_d_+1</sup> (41) 

For instance, in a 2D blackbody system, the total energy density scales as _u_ 2 _∝ T_<sup>3</sup> . 

#### **5. Connections to Observables** 

-  **Entropy of a Photon Gas (** _S_ **):** Derived from the Helmholtz free energy _F_ = _U − TS_ . Since _U_ = _aV T_<sup>4</sup> and _P_ =<sup><u>1</u></sup> 3<sup>_aT_4:</sup> 



<!-- Start of picture text -->
S =  − = 4 (42)<br>� ∂F∂T � V 3 aV T  3 ∝ T  3<br><!-- End of picture text -->

This is directly proportional to the total number of photons in the cavity, _N ∝ V T_<sup>3</sup> .  **Specific Heat (** _CV_ **):** 



<!-- Start of picture text -->
CV = = 4 aV T 3 ∝ T 3 (43)<br>� ∂U∂T � V<br><!-- End of picture text -->

The specific heat of radiation has a cubic temperature dependence, dominating over the specific heat of lattice vibrations at extremely high temperatures. 

8 

BEC & Blackbody Radiation 

GATE Physics Exam Study Guide 

#### **6. Crucial Pitfalls** 

##### **Blackbody Radiation Traps** 

-  **The Peak Frequency and Wavelength Conversion Trap:** Assuming that the peak frequency satisfies _ν_ max = _c/λ_ max. This is incorrect because the integration volume elements are different ( _dν̸_ = _dλ_ ). Always use the correct constant factor. 

-  **The Emissivity Confusion:** Assuming the net power radiated is simply _σAT_<sup>4</sup> when the body is not in a vacuum. You must subtract the ambient radiation of the environment: _P_ net = _σA_ ( _T_<sup>4</sup> _− T_ 0<sup>4).</sup> 

#### **7. Standard Textbook Systems** 

-  **The Cavity Resonator (Photon Gas):** A hollow box with perfectly reflective inner walls held at constant temperature _T_ , containing a small aperture to sample the emitted radiation. 

-  **The Cosmic Microwave Background (CMB):** The universe is modeled as a massive blackbody cavity expanding adiabatically. As the volume increases, the photon gas cools while maintaining its perfect blackbody distribution, currently peaking in the microwave range at _T ≈_ 2 _._ 725 K. 

9 

