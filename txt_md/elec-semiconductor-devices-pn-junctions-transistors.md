<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: elec-semiconductor-devices-pn-junctions-transistors.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

GATE PHYSICS 

SEMICONDUCTOR DEVICES 

# **GATE PHYSICS STUDY NOTES Semiconductor Devices: p-n Junctions, BJTs, and MOSFETs** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**|**The p-n Junction Diode: Physics & I-V Characteristics**|**2**|
|---|---|---|
|**2**|**Bipolar Junction Transistors (BJTs)**|**6**|
|**3**|**Field Effect Transistors (JFETs & MOSFETs)**|**10**|



1 

GATE PHYSICS 

SEMICONDUCTOR DEVICES 

## **1 The p-n Junction Diode: Physics & I-V Characteristics** 

### **1. Core Theory** 

A **p-n junction diode** is formed by joining a p-type semiconductor (abundant in mobile holes) and an n-type semiconductor (abundant in mobile conduction electrons) to create a single, continuous crystal lattice. 

-  **The Depletion Region:** Upon metallurgical contact, the massive carrier concentration gradient drives the **diffusion** of electrons from the n-side to the p-side, and holes from the p-side to the n-side. This diffusion leaves behind uncompensated, immobile ionized impurity cores: positive donor ions ( _ND_<sup>+)onthen-sideandnegativeacceptorions(</sup><sup>_N_</sup> _A_<sup>_−_)onthep-side.</sup> These static space charges create a built-in electric field ( **E** bi) pointing from the n-side to the p-side. 

-  **Drift-Diffusion Balance:** The built-in electric field opposes further diffusion by driving a counter-balancing **drift** current of minority carriers. At thermodynamic equilibrium, the net electron and hole currents are strictly zero: 



<!-- Start of picture text -->
Jn, total =  Jn, drift +  Jn, diff = 0 , Jp, total =  Jp, drift +  Jp, diff = 0 (1)<br><!-- End of picture text -->

The region containing the immobile space charges and stripped of mobile carriers is called the **depletion region** (or space-charge region). 

### **2. Mathematical Framework & Transfer Functions** 

The electrostatics of an abrupt, step p-n junction are modeled as follows: 

-  **Built-in Potential (** _V_ **bi):** The electrostatic potential difference across the depletion region at equilibrium: 



<!-- Start of picture text -->
V bi = kBT ln =  Vt  ln (2)<br>e � NAnN 2 i D � � NAnN 2 i D �<br><!-- End of picture text -->

where _Vt_ = _kBT/e ≈_ 25 _._ 9 mV is the thermal voltage at 300 K, _NA_ and _ND_ are the acceptor and donor doping concentrations, and _ni_ is the intrinsic carrier concentration. 

-  **Depletion Width (** _W_ **):** Under an applied external voltage _Va_ (positive for forward bias, negative for reverse bias): 



<!-- Start of picture text -->
2 ϵs ( V bi  − Va )<br>W = =  xp  +  xn (3)<br>� e � NNA  + AN NDD �<br><!-- End of picture text -->

where _ϵs_ is the semiconductor permittivity, and _xp, xn_ are the penetration depths into the p- and n-sides: 



<!-- Start of picture text -->
ND NA<br>xp =  W , xn =  W (4)<br>� NA  +  ND � � NA  +  ND �<br><!-- End of picture text -->

Note that charge neutrality requires: _eNAxp_ = _eNDxn_ . 

2 

GATE PHYSICS 

SEMICONDUCTOR DEVICES 

 **Ideal Diode Equation (Shockley Equation):** 



<!-- Start of picture text -->
I =  I 0 e Va/ηVt − 1 (5)<br>� �<br><!-- End of picture text -->

where _η_ is the ideality factor ( _η_ = 1 for dominant diffusion/ideal recombination, _η ≈_ 2 for dominant space-charge recombination), and _I_ 0 is the **reverse saturation current**: 



<!-- Start of picture text -->
n 2 n 2<br>i i<br>I 0 =  eA + Dp (6)<br>� DLnn NA Lp ND �<br><!-- End of picture text -->

where _A_ is the junction area, _Dn, Dp_ are diffusion coefficients, and _Ln, Lp_ are the minority carrier diffusion lengths: _L_ = _~~√~~ Dτ_ . 

 **Junction (Depletion) Capacitance (** _Cj_ **- dominant in reverse bias):** 



<!-- Start of picture text -->
eϵsNAND<br>Cj = ϵsA (7)<br>W =  A � 2( V bi  − Va )( NA  +  ND ) ∝ ( V bi  − Va ) − 1 / 2<br><!-- End of picture text -->

 **Diffusion Capacitance (** _Cd_ **- dominant in forward bias):** 



<!-- Start of picture text -->
Cd ≈ τp ∝ IQ (8)<br>� keIBQT �<br><!-- End of picture text -->

where _IQ_ is the DC quiescent bias current and _τp_ is the minority carrier lifetime. 

### **3. Circuit Analysis Milestones** 

When solving circuits containing p-n diodes: 

1. **Model Selection:** Choose the appropriate diode model based on required accuracy: 

   -  **Ideal Diode Model:** _V_ on = 0 V, zero forward resistance. 

   -  **Constant Voltage Drop (CVD) Model:** _V_ on _≈_ 0 _._ 7 V (for Si), zero forward resistance. 

   -  **Piecewise Linear (PWL) Model:** _V_ on _≈_ 0 _._ 7 V with a small series resistance _rf_ . 

2. **Initial State Assumption:** Assume the state of each diode (ON/forward-biased or OFF/reversebiased). 

3. **Consistency Check via Circuit Solving:** Replace ON diodes with their voltage-drop equivalent ( _V_ on) and OFF diodes with open circuits. Solve for loop currents and node potentials: 

   -  For an assumed **ON** diode, check that the calculated current is strictly positive: _ID >_ 0. 

   -  For an assumed **OFF** diode, check that the calculated terminal voltage is less than the turn-on threshold: _VD < V_ on. 

4. **Iterate if Inconsistent:** If any check fails, change the assumed state(s) and re-solve. 

3 

GATE PHYSICS 

SEMICONDUCTOR DEVICES 

### **4. Problem-Solving Algorithm** 

#### **Solving p-n Junction Electrostatics** 

1. **Calculate the thermal voltage (** _Vt_ **):** At the operating temperature _T_ (usually 300 K, where _Vt ≈_ 0 _._ 0259 V). 

2. **Determine the built-in potential (** _V_ **bi):** Substitute the doping concentrations _NA_ , _ND_ , and the intrinsic concentration _ni_ (for Si, _ni ≈_ 1 _._ 5 _×_ 10<sup>10</sup> cm<sup>_−_3</sup> at 300 K) into the built-in potential formula. 

3. **Evaluate the depletion width (** _W_ **) at a given bias:** Ensure all values are in consistent units (preferably SI or cm): 



<!-- Start of picture text -->
ϵ silicon ≈ 11 . 7  ×  8 . 854  ×  10 − 14 F/cm = 1 . 04  ×  10 − 12 F/cm (9)<br>4. Find the peak electric field ( E max) at the metallurgical interface ( x  = 0 ):<br>E max = eNDxn = eNAxp = 2( V bi  − Va ) (10)<br>ϵs ϵs W<br><!-- End of picture text -->

### **5. Truth Tables & Characteristics** 

The p-n junction exhibits highly asymmetric, non-linear I-V characteristics: 

-  **Forward Bias (** _Va >_ 0 **):** The applied potential opposes the built-in potential, reducing the barrier height to _V_ bi _− Va_ . The depletion width narrows, and the carrier diffusion current increases exponentially according to _I ∝ e_<sup>_Va/Vt_</sup> . No significant current flows until _Va_ exceeds the turn-on voltage ( _V_ on _≈_ 0 _._ 7 V for Si, 0 _._ 3 V for Ge). 

-  **Reverse Bias (** _Va <_ 0 **):** The applied potential reinforces the built-in potential, widening the barrier to _V_ bi + _|Va|_ . The depletion width expands, and the forward diffusion of majority carriers is completely suppressed. Only a tiny, temperature-dependent drift current of minority carriers flows, saturating at _I ≈−I_ 0. 

-  **Breakdown Region (** _Va →−V_ **BD):** At a high reverse voltage, the electric field becomes intense enough to initiate a massive current increase through: 

   - **Zener Breakdown (dominant for high doping,** _<_ 6 **V):** Quantum-mechanical tunneling of valence electrons directly from the p-side valence band into the n-side conduction band. 

   - **Avalanche Breakdown (dominant for lower doping,** _>_ 6 **V):** Impact ionization where accelerated carriers gain enough kinetic energy to knock valence electrons into the conduction band, triggering a runaway multiplication cascade. 

4 

GATE PHYSICS 

SEMICONDUCTOR DEVICES 

### **6. Crucial Pitfalls** 

#### **p-n Junction Pitfalls to Avoid** 

-  **Forward Current and Temperature Misunderstanding:** Assuming _I_ 0 is temperature-independent. In reality, _I_ 0 _∝ n_<sup>2</sup> _i_<sup>_∝T_3</sup><sup>_e−Eg/kBT_.Eventhoughthethermal</sup> voltage _Vt_ increases with temperature (reducing the exponent in _e_<sup>_V/Vt_</sup> ), the exponential increase in _I_ 0 dominates, causing the turn-on voltage of a diode to decrease by approximately _−_ 2 mV _/_<sup>_◦_</sup> C as temperature rises. 

-  **Confusion of Junction and Diffusion Capacitance:** Attempting to calculate diffusion capacitance in reverse bias. _Cd_ is strictly due to minority carrier storage in forward bias. In reverse bias, the capacitance is dominated purely by the depletion capacitance _Cj_ . 

-  **One-Sided Junction Approximations:** Forgetting to simplify equations for heavily 2 _ϵs_ <u>(</u> _V_ <u>bi</u> _−Va_ <u>)</u> 

- asymmetric junctions (e.g., _p_<sup>+</sup> - _n_ where _NA ≫ ND_ ). In such cases, _W ≈_ ~~�~~ _eND_ , meaning the depletion region penetrates almost entirely into the lighter-doped n-side ( _xn ≈ W_ , _xp ≈_ 0). 

### **7. Standard Textbook Systems** 

-  **The Half-Wave and Full-Wave Rectifier:** Used to illustrate the AC-to-DC conversion capability of diodes. The full-wave bridge rectifier utilizes four diodes to steer both halves of an AC wave through a load in the same direction. 

-  **The Varactor Diode:** A reverse-biased p-n junction designed specifically to exploit its voltage-variable junction capacitance ( _Cj ∝ V_<sup>_−_1</sup><sup>_/_2</sup> ), acting as a voltage-controlled tuning capacitor in RF oscillators and phase-locked loops. 

5 

GATE PHYSICS 

SEMICONDUCTOR DEVICES 

## **2 Bipolar Junction Transistors (BJTs)** 

### **1. Core Theory** 

A **Bipolar Junction Transistor (BJT)** is a three-terminal, double-junction active semiconductor device consisting of three adjacent doped regions: Emitter (E), Base (B), and Collector (C). It is fabricated as either an **npn** or a **pnp** sandwich structure. 

-  **Operational Principle (npn Active Mode):** The Emitter-Base (E-B) junction is forwardbiased, lowering the potential barrier and allowing massive injection of electrons from the heavily doped Emitter into the thin, lightly doped Base. These injected electrons become minority carriers in the Base. 

-  **Base Transport:** Because the Base is extremely narrow ( _WB ≪ Ln_ ), the injected electrons do not recombine significantly; instead, they diffuse rapidly across the Base toward the Collector. 

-  **Collector Collection:** The Base-Collector (B-C) junction is reverse-biased. The intense electric field across this reverse-biased junction sweeps the arriving minority electrons out of the Base and collects them into the Collector, generating the collector current. Since Emitter injection is controlled by the E-B forward voltage, the BJT behaves as a **current-controlled current source**. 

### **2. Mathematical Framework & Transfer Functions** 

The operational currents are governed by the following relationships: 

-  **Kirchhoff’s Current Law for BJT Terminals:** 



<!-- Start of picture text -->
IE =  IC +  IB (11)<br><!-- End of picture text -->

-  **Current Gain Definitions:** 



<!-- Start of picture text -->
– **Common-Base Current Gain ( α ):**<br><!-- End of picture text -->



<!-- Start of picture text -->
α ≡ IC (typically 0 . 95  − 0 . 998) (12)<br>IE<br><!-- End of picture text -->



<!-- Start of picture text -->
– **Common-Emitter Current Gain ( β ):**<br><!-- End of picture text -->



<!-- Start of picture text -->
β ≡ IC (typically 50  − 300) (13)<br>IB<br><!-- End of picture text -->

**–** **Mathematical Interrelations:** 



<!-- Start of picture text -->
α β<br>β = α  = (14)<br>1  − α , β  + 1<br><!-- End of picture text -->

 **BJT Operating Regions (for npn):** 

 **Current Components in Active Mode:** 



<!-- Start of picture text -->
IC =  ISe VBE /Vt 1 + VCE (15)<br>� VA �<br><!-- End of picture text -->

where _IS_ is the saturation scale current and _VA_ is the **Early Voltage** (accounting for basewidth modulation). 

6 

GATE PHYSICS 

SEMICONDUCTOR DEVICES 

|**Operating Region**|**E-B Junction Bias**|**B-C Junction Bias**|**Voltage Conditions**|
|---|---|---|---|
|**Cutoff**|Reverse|Reverse|_VBE <_0_._7 V_, IB_ = 0|
|**Active (Linear)**|Forward|Reverse|_VBE ≈_0_._7 V_, VCE > VCE,_sat|
|**Saturation**|Forward|Forward|_VBE ≈_0_._7 V_, VCE_ =_VCE,_sat _≈_0_._2 V|
|**Reverse-Active**|Reverse|Forward|(Heavily degraded _β_rev)|



### **3. Circuit Analysis Milestones** 

To perform DC bias analysis on a BJT circuit: 

1. **Assume Active Region:** Assume the BJT is in the active region: _VBE_ = 0 _._ 7 V and _IC_ = _βIB_ . 

2. **Apply KVL to Input (Base-Emitter) Loop:** Solve for the base current _IB_ . For example, in a voltage-divider bias: 

   - _V_ TH _− VBE_ 

   - _V_ TH _− IBR_ TH _− VBE − IERE_ = 0 = _⇒ IB_ = (16) _R_ TH + ( _β_ + 1) _RE_ 

3. **Determine Collector Current and Collector-Emitter Voltage (** _VCE_ **):** Compute _IC_ = _βIB_ and apply KVL to the output loop: 

   - _VCE_ = _VCC − ICRC − IERE_ (17) 

4. **Verify Active Region Condition:** Check that the calculated _VCE_ is greater than the saturation limit: 

   - _VCE ≥ VCE,_ sat _≈_ 0 _._ 2 V (and _IB >_ 0) (18) 

*If _VCE <_ 0 _._ 2 V, the assumption of active mode was false. Re-solve the circuit in the **Saturation Region** by setting _VCE_ = 0 _._ 2 V and solving for _IC_ and _IB_ independently (where _IC < βIB_ ).* 

7 

GATE PHYSICS 

SEMICONDUCTOR DEVICES 

### **4. Problem-Solving Algorithm** 

#### **Solving Common-Emitter (CE) Amplifiers** 

To perform small-signal AC analysis on a CE BJT amplifier: 

1. **Perform DC Analysis:** Find the DC collector bias current _ICQ_ and confirm active operation. 

2. **Calculate Small-Signal Parameters:** 

   -  Transconductance: _gm_ =<sup>_IC_</sup> _Vt_<sup>_<u>Q</u>_</sup>  Input resistance: _rπ_ =<sup>_<u>βVt</u>_</sup> _<u>β</u> ICQ_<sup>=</sup> _gm_ 

   -  Output resistance: _ro ≈ IVCQA_<sup>(oftenneglectedif</sup><sup>_VA→∞_)</sup> 

3. **Replace BJT with Hybrid-** _π_ **AC Model:** Short-circuit all DC voltage sources and coupling/bypass capacitors. Replace the BJT with its equivalent AC model: resistor _rπ_ between B and E, and a dependent current source _gmvbe_ (or _βib_ ) between C and E. 

4. **Solve for AC Voltage Gain (** _Av_ = _vo/vs_ **):** 



<!-- Start of picture text -->
Av ≈−gm ( RC ∥ RL ) =  − ICQ ( RC ∥ RL ) (19)<br>Vt<br><!-- End of picture text -->

### **5. Truth Tables & Characteristics** 

BJTs are characterized by three standard configurations: 

-  **Common-Emitter (CE):** Input applied to Base, output taken from Collector. 

   - **Characteristics:** High voltage gain, high current gain ( _β_ ), moderate input/output resistances. Provides 180<sup>_◦_</sup> phase inversion. 

-  **Common-Base (CB):** Input applied to Emitter, output taken from Collector. 

   - **Characteristics:** High voltage gain, current gain less than unity ( _α <_ 1), extremely low input resistance, high output resistance. No phase inversion (used for high-frequency isolation/cascode). 

-  **Common-Collector (CC / Emitter Follower):** Input applied to Base, output taken from Emitter. 

   - **Characteristics:** Voltage gain of approximately unity ( _Av ≈_ 1), high current gain ( _β_ + 1), high input resistance, low output resistance. No phase inversion (used as a buffer). 

8 

GATE PHYSICS 

SEMICONDUCTOR DEVICES 

### **6. Crucial Pitfalls** 

#### **BJT Analysis Pitfalls to Avoid** 

-  **Blindly using** _IC_ = _βIB_ **in Saturation:** Applying the active-mode current gain equation when the BJT is in saturation. In saturation, both junctions are forwardbiased, and _IC_ is limited by the external collector-collector loop resistance. You must set _VCE_ = 0 _._ 2 V and calculate _IC_ and _IB_ separately. The saturation condition is checked by verifying that: 

   - _β_ forced _≡_<sup>_IC,_sat</sup> _< β_ active (20) _IB,_ sat 

-  **Neglecting the Base Current (** _IB_ = 0 **):** Assuming the base current is zero in DC biasing calculations, which is only valid for FETs. For a BJT, _IB_ = _IC/β_ , which is small but non-zero, especially in voltage-divider biasing where the Thevenin resistance _R_ TH is comparable to ( _β_ + 1) _RE_ . 

-  **Confusing npn and pnp polarities:** Forgetting that in a pnp transistor, all current directions and terminal voltage polarities are reversed. For active mode in a pnp: _VEB ≈_ 0 _._ 7 V and _VEC >_ 0 _._ 2 V with currents exiting the collector and base. 

### **7. Standard Textbook Systems** 

-  **The CE Voltage-Divider Self-Bias Circuit:** The standard BJT bias network. It uses a base voltage divider ( _R_ 1 _, R_ 2) and an emitter resistor ( _RE_ ) to stabilize the DC Q-point ( _ICQ, VCEQ_ ) against temperature-driven variations in _β_ . 

-  **The Emitter Follower Buffer:** A CC configuration used to match a high-resistance source to a low-resistance load, exploiting its high input impedance and low output impedance. 

9 

GATE PHYSICS 

SEMICONDUCTOR DEVICES 

## **3 Field Effect Transistors (JFETs & MOSFETs)** 

### **1. Core Theory** 

A **Field Effect Transistor (FET)** is a three-terminal unipolar device (conduction occurs via majority carriers only) where the current flow is controlled by an electrostatic field. 

-  **Junction Field Effect Transistor (JFET):** Consists of a conducting channel (n- or p-type) sandwiched between two reverse-biased p-n junctions (the Gate). The reverse bias widens the depletion regions, narrowing the physical channel and modulating its electrical resistance. 

-  **Metal-Oxide-Semiconductor FET (MOSFET):** Features a Gate electrode electrically isolated from the semiconductor channel by a thin silicon dioxide (SiO2) insulating layer. 

-  **Operational Principle (n-channel Enhancement MOSFET):** With zero gate voltage, the p-type substrate blocks current flow between the n-type Source and Drain (normallyoff). Applying a positive gate-to-source voltage ( _VGS > Vt_ ) repels holes from the oxidesemiconductor interface and attracts electrons. This creates an **inversion layer** (the n- channel) connecting the Source and Drain, allowing electron drift under a drain-source voltage ( _VDS_ ). Because the gate is insulated, the gate current is strictly zero ( _IG_ = 0), making the MOSFET a **voltage-controlled current source**. 

### **2. Mathematical Framework & Transfer Functions** 

The operational current-voltage equations of an n-channel enhancement MOSFET are: 

-  **Cutoff Region:** 



<!-- Start of picture text -->
ID = 0 for VGS < Vth (21)<br><!-- End of picture text -->

where _Vth_ is the threshold voltage required to initiate inversion. 

 **Linear (Triode/Non-Saturation) Region:** 



<!-- Start of picture text -->
ID =  Kn �2( VGS − Vth ) VDS − VDS 2 � for VGS ≥ Vth and VDS < VGS − Vth (22)<br><!-- End of picture text -->

where _Kn_ =<sup><u>1</u></sup> 2<sup>_µnC_ox</sup><sup>_<u>W</u>_</sup> _L_<sup>istheconductionparameter(</sup><sup>_C_oxistheoxidecapacitanceperunit</sup> area, _W_ and _L_ are channel width and length). 

-  **Saturation (Pinch-off) Region:** At high _VDS_ , the inversion layer charge shrinks to zero near the drain (pinch-off). The current saturates: 



<!-- Start of picture text -->
ID =  Kn ( VGS − Vth ) 2 (1 +  λVDS ) for VGS ≥ Vth and VDS ≥ VGS − Vth (23)<br><!-- End of picture text -->

where _λ_ is the **channel-length modulation parameter** (analogous to the Early effect in BJTs). 

-  **n-channel JFET / Depletion MOSFET Current (Saturation):** 



<!-- Start of picture text -->
ID =  IDSS 1  − VGS (24)<br>� Vp �2<br><!-- End of picture text -->

where _IDSS_ is the drain-source saturation current at _VGS_ = 0, and _Vp_ is the pinch-off voltage (normally negative for n-channel JFET). 

10 

GATE PHYSICS 

SEMICONDUCTOR DEVICES 

### **3. Circuit Analysis Milestones** 

To analyze a MOSFET biasing circuit: 

1. **Use Gate-Insulation Property:** Set the gate current strictly to zero: _IG_ = 0. Solve for the gate voltage _VG_ using the input divider network: 



<!-- Start of picture text -->
R 2<br>VG =  VDD (25)<br>� R 1 +  R 2 �<br><!-- End of picture text -->

2. **Assume Saturation Region:** Assume the MOSFET is in saturation. Relate _VGS_ to the source resistance _RS_ : 



<!-- Start of picture text -->
VGS =  VG − IDRS (26)<br><!-- End of picture text -->

Substitute this into the saturation current equation _ID_ = _Kn_ ( _VGS − Vth_ )<sup>2</sup> and solve the resulting quadratic equation for _ID_ (and select the physically valid root where _VGS > Vth_ ). 

3. **Calculate Drain-to-Source Voltage (** _VDS_ **):** 



<!-- Start of picture text -->
VDS =  VDD − IDRD − IDRS (27)<br><!-- End of picture text -->

4. **Verify Saturation Assumption:** Check if the calculated drain voltage satisfies the saturation condition: 



<!-- Start of picture text -->
VDS ≥ VGS − Vth (and VGS > Vth ) (28)<br><!-- End of picture text -->

*If _VDS < VGS − Vth_ , the MOSFET is in the **Linear region** . Re-solve the circuit using the linear triode current equation.* 

### **4. Problem-Solving Algorithm** 

#### **Small-Signal AC Analysis of Common-Source (CS) Amplifiers** 

To analyze the AC voltage gain of a CS MOSFET amplifier: 

1. **Perform DC Bias Analysis:** Find the quiescent drain current _IDQ_ and check for saturation. 

2. **Determine Small-Signal Transconductance (** _gm_ **):** 



<!-- Start of picture text -->
gm ≡ ∂ID = 2 Kn ( VGS − Vth ) = 2 � KnIDQ (29)<br>∂VGS ���� Q− pt<br><!-- End of picture text -->

3. **Draw the AC Equivalent Circuit:** Replace the MOSFET with its small-signal model: an open-circuit at the input (between G and S) and a dependent current source _gmvgs_ in parallel with output resistance _ro_ = 1 _/_ ( _λIDQ_ ) between D and S. 

4. **Evaluate the Voltage Gain (** _Av_ = _vo/vs_ **):** 



<!-- Start of picture text -->
Av =  −gm ( RD ∥ RL ∥ ro ) (30)<br><!-- End of picture text -->

11 

GATE PHYSICS 

SEMICONDUCTOR DEVICES 

### **5. Truth Tables & Characteristics** 

MOSFETs are characterized by distinct I-V curves plotting _ID_ versus _VDS_ for different values of _VGS_ : 

-  **Linear/Triode Region (** _VDS < VGS − Vth_ **):** At low drain voltages, the channel behaves as a simple voltage-controlled resistor, where the current increases almost linearly with _VDS_ . 

-  **Pinch-off and Saturation (** _VDS ≥ VGS −Vth_ **):** As _VDS_ reaches the value _V_ DS,sat = _VGS −Vth_ , the field near the drain is reduced to the threshold limit, pinching off the channel. Further increases in _VDS_ do not increase the current, resulting in flat, saturated current plateaus controlled exclusively by _VGS_ . 

### **6. Crucial Pitfalls** 

#### **FET/MOSFET Pitfalls to Avoid** 

-  **Incorrect Quadratic Root Selection:** Solving the quadratic equation for _ID_ during DC bias and choosing the wrong root. Mathematically, the quadratic equation yields two roots. You must choose the root that satisfies _VGS > Vth_ . The other root corresponds to the unphysical virtual extension of the parabola below threshold where the device is actually turned off. **Transconductance Equation Confusions:** Using the BJT transconductance formula ( _gm_ = _IC/Vt_ ) for a MOSFET. For a MOSFET, _gm_ = 2<sup>_~~√~~_</sup> _KnID_ , meaning the transconductance is proportional to the **square root** of the bias current rather than being directly proportional to the current as in a BJT. 

-  **Confusing Depletion and Enhancement Symbols:** Misidentifying Depletion-type MOSFETs (which have a pre-existing physical channel and can operate at zero or negative gate bias, _Vth <_ 0) with Enhancement-type MOSFETs (normally-off, requiring _VGS > Vth >_ 0). 

### **7. Standard Textbook Systems** 

-  **The MOSFET Voltage-Divider Common-Source Amplifier:** The primary amplifying configuration. It features a very high input impedance (limited only by the bias divider resistors, _R_ in = _R_ 1 _∥ R_ 2) and moderate voltage gain. 

-  **The CMOS Inverter:** The core building block of digital logic. It pairs an n-channel enhancement MOSFET with a p-channel enhancement MOSFET in series between _VDD_ and Ground, resulting in virtually zero static power consumption because one of the two transistors is always turned off. 

12 

GATE PHYSICS 

SEMICONDUCTOR DEVICES 

## **References** 

1. Neamen, Donald A. _Semiconductor Physics and Devices_ . McGraw-Hill, 2012. 

2. Boylestad, Robert L., and Nashelsky, Louis. _Electronic Devices and Circuit Theory_ . Pearson, 2013. 

3. Kittel, Charles. _Introduction to Solid State Physics_ . Wiley, 2005. 

13 

GATE PHYSICS 

FEEDBACK & OSCILLATORS 

# **GATE PHYSICS STUDY NOTES Feedback Circuits & Oscillators** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**<br>**Theory of Negative & Positive Feedback Circuits**|**2**|
|---|---|
|**2**<br>**The Barkhausen Criteria for Oscillation**|**5**|
|**3**<br>**Design & Analysis of RC Oscillators**|**7**|
|**4**<br>**Design & Analysis of LC Oscillators**|**10**|



1 

GATE PHYSICS 

FEEDBACK & OSCILLATORS 

## **1 Theory of Negative & Positive Feedback Circuits** 

### **1. Core Theory** 

Feedback is a foundational circuit design technique where a fraction of the output signal (voltage or current) is returned and combined with the input signal. The behavior of the system is governed by the relative phase of the returned signal: 

-  **Negative Feedback (NFB):** The returned signal is out of phase (180<sup>_◦_</sup> phase shift) with the external input signal, opposing it. 

-  **Physical Origin:** Negative feedback decreases the net input driving the amplifier. This selfcorrecting action stabilizes the closed-loop voltage gain, dramatically increases the operational bandwidth, decreases harmonic distortion, and alters the input/output impedances to more ideal characteristics depending on the specific coupling topology. 

-  **Positive Feedback (PFB):** The returned signal is in phase (0<sup>_◦_</sup> or 360<sup>_◦_</sup> phase shift) with the external input, reinforcing it. 

-  **Physical Origin:** Positive feedback triggers regenerative amplification. If the loop gain exceeds unity, the circuit enters unstable saturation (such as in Schmitt triggers and bistable multivibrators) or sustains steady-state oscillations (harmonic oscillators) where the internal noise triggers a self-sustaining sinusoidal current. 

### **2. Mathematical Framework & Transfer Functions** 

- **Feedback Closed-Loop Gain (** _Af_ **):** The fundamental feedback relation is given by: 



<!-- Start of picture text -->
A A<br>Af = (for Negative Feedback) , Af = (for Positive Feedback) (1)<br>1 +  Aβ 1  − Aβ<br><!-- End of picture text -->

where _A_ is the open-loop gain of the internal amplifier, and _β_ is the feedback factor representing the transfer function of the feedback network. * **Loop Gain (** _Aβ_ **):** The product of the amplifier gain and the feedback factor, representing the total transmission gain around the complete closed loop. * **Feedback Sensitivity (** 1 + _Aβ_ **):** Measures the reduction of gain and the corresponding stabilization: 



<!-- Start of picture text -->
dAf = 1<br>(2)<br>Af 1 +  Aβ � dAA �<br><!-- End of picture text -->

This proves that fractional variations in closed-loop gain are suppressed by the sensitivity factor (1 + _Aβ_ ) relative to open-loop variations. * **Bandwidth Expansion:** If the open-loop amplifier has a single-pole frequency response with upper cutoff frequency _fH_ , the closed-loop bandwidth expands: 



<!-- Start of picture text -->
fL<br>fHf =  fH (1 +  Aβ ) , fLf = (3)<br>1 +  Aβ<br><!-- End of picture text -->



<!-- Start of picture text -->
* Feedback Topologies and Impedance Modifiers:<br><!-- End of picture text -->

2 

GATE PHYSICS 

FEEDBACK & OSCILLATORS 

|**Feedback Topology**|**Input Mixing**|**Output Sampling**|**Input Impedance** _Rif_|**Output Impedanc**|
|---|---|---|---|---|
|**Voltage-Series**|Series (voltage)|Shunt (voltage)|_Ri_(1 +_Aβ_)|_Ro/_(1 +_Aβ_)|
|**Voltage-Shunt**|Shunt (current)|Shunt (voltage)|_Ri/_(1 +_Aβ_)|_Ro/_(1 +_Aβ_)|
|**Current-Series**|Series (voltage)|Series (current)|_Ri_(1 +_Aβ_)|_Ro_(1 +_Aβ_)|
|**Current-Shunt**|Shunt (current)|Series (current)|_Ri/_(1 +_Aβ_)|_Ro_(1 +_Aβ_)|



Table 1: Impedance scaling as a function of the four feedback topologies. 

### **3. Circuit Analysis Milestones** 

To systematically analyze a multi-stage feedback amplifier circuit: 

1. **Identify the Output Sampling Method:** Check how the feedback network connects to the output node. If it connects directly in parallel (shunt) to the output, it samples **voltage** . If it connects in series with the output branch, it samples **current** . 

2. **Identify the Input Mixing Method:** Check how the feedback signal combines with the source at the input. If the feedback is in series with the source, it mixes as a **voltage** . If it connects in parallel (shunt) to the input node, it mixes as a **current** . 

3. **Construct the Loaded Open-Loop Circuit:** Determine the loaded open-loop amplifier by incorporating the loading effects of the feedback network ( _h_ 11 and _h_ 22 parameter equivalents) at both the input and output terminals: 

   -  For voltage sampling, short-circuit the output ( _Vo_ = 0) to find input loading. 

   -  For current sampling, open-circuit the output ( _Io_ = 0) to find input loading. 

   -  For series mixing, open-circuit the input loop ( _Ii_ = 0) to find output loading. 

   -  For shunt mixing, short-circuit the input ( _Vi_ = 0) to find output loading. 

4. **Compute** _A_ **,** _β_ **, and the Closed-Loop Parameters:** Solve the loaded open-loop circuit for _A_ , evaluate _β_ from the isolated feedback network, and calculate _Af_ = _A/_ (1 + _Aβ_ ). 

### **4. Problem-Solving Algorithm** 

#### **Biasing and Gain Analysis of Feedback Topologies** 

1. **Determine the Topology Type:** Use the sampling-mixing tests. 

2. **Calculate the Feedback Factor (** _β_ **):** Express the feedback signal _Xf_ returned to the input as a ratio of the output quantity _Xo_ : 

_β_ =<sup>_Xf_</sup> (4) _Xo_ 

For a resistive voltage divider (voltage-series feedback), _β_ = _R_ 1 _/_ ( _R_ 1 + _R_ 2). 

3. **Evaluate Open-loop Gain (** _A_ **):** Solve the open-loop circuit including the loading of the feedback resistors. 

4. **Solve for** _Af_ **,** _Rif_ **, and** _Rof_ **:** Apply the matching scaling factors from Table 1. 

3 

GATE PHYSICS 

FEEDBACK & OSCILLATORS 

### **5. Characteristics** 

* **Gain-Bandwidth Product Conservation:** The gain-bandwidth product of a single-pole amplifier remains constant under negative feedback: 



<!-- Start of picture text -->
A<br>GBW =  Af · fHf = · fH (1 +  Aβ ) =  A · fH (5)<br>� 1 +  Aβ �<br><!-- End of picture text -->

This establishes that negative feedback trades gain directly for an identical increase in flat frequency response. 

### **6. Crucial Pitfalls** 

#### **Feedback Theory Mistakes** 

-  **Ignoring Feedback Network Loading:** Simply calculating the open-loop gain _A_ of the amplifier by completely disconnecting the feedback network. You must include the loading resistances of the feedback network at the input and output terminals to get the correct open-loop gain. 

-  **Incorrect Impedance Formula Application:** Blindly dividing input impedance by (1 + _Aβ_ ) for all topologies. Input impedance only decreases for shunt mixing and increases for series mixing. 

### **7. Standard Textbook Systems** 

-  **The Non-Inverting Op-Amp Amplifier:** An ideal Voltage-Series negative feedback configuration. The open-loop gain _A ≈_ 10<sup>5</sup> , and the feedback factor is _β_ = _R_ 1 _/_ ( _R_ 1 + _Rf_ ). This results in an extremely high input impedance and a stabilized closed-loop gain of _Af_ = 1 + _Rf /R_ 1. 

-  **The Common-Emitter Amplifier with Emitter Degeneration (** _RE_ **):** An npn BJT amplifier featuring Current-Series negative feedback. The unbypassed emitter resistor _RE_ samples the output emitter current and subtracts a proportional voltage _IERE_ from the input loop, stabilizing the AC voltage gain to _Av ≈−RC/RE_ . 

4 

GATE PHYSICS 

FEEDBACK & OSCILLATORS 

## **2 The Barkhausen Criteria for Oscillation** 

### **1. Core Theory** 

An **oscillator** is an active electronic circuit that converts DC power from a power supply into a continuous, self-sustaining AC output signal (usually a sinusoid) without requiring any external AC input source. 

-  **The Physical Principle:** Sustained oscillation is achieved by utilizing positive feedback to return a portion of the output signal back to the input of an amplifier. If the returned signal is identical in amplitude and phase to the virtual input, the circuit no longer requires an external source to drive it and will continuously reinforce its own internal currents. 

-  **The Noise-Startup Mechanism:** When the DC power supply is first switched on, thermal charge fluctuations and transient turn-on current surges generate a wide spectrum of electrical noise throughout the circuit. The frequency-selective positive feedback network selects and amplifies only one specific resonant frequency components ( _ω_ 0). The signal builds up exponentially until non-linearities in the active device limit the loop gain to exactly unity, establishing a stable, constant-amplitude sinusoid. 

### **2. Mathematical Framework & Transfer Functions** 

Consider a closed-loop system with positive feedback. The transfer function is: 



<!-- Start of picture text -->
A ( s )<br>Af ( s ) = (6)<br>1  − A ( s ) β ( s )<br><!-- End of picture text -->

* **The Barkhausen Criteria:** For the system to maintain stable, steady-state sinusoidal oscillations at a specific frequency _ω_ 0 ( _s_ = _iω_ 0), the loop transfer function must satisfy: 



<!-- Start of picture text -->
A ( iω 0) β ( iω 0) = 1 (7)<br><!-- End of picture text -->

This vector equation is split into two independent mathematical conditions: 

1. **The Magnitude Condition:** The magnitude of the loop gain must be exactly equal to unity: 



<!-- Start of picture text -->
|A ( iω 0) β ( iω 0) |  = 1 (8)<br><!-- End of picture text -->

2. **The Phase Condition:** The net phase shift around the closed loop must be 0<sup>_◦_</sup> or an integer multiple of 360<sup>_◦_</sup> : 



<!-- Start of picture text -->
∠ A ( iω 0) β ( iω 0) = 2 nπ ( n ∈{ 0 ,  1 ,  2 , . . . } ) (9)<br><!-- End of picture text -->

### **3. Circuit Analysis Milestones** 

To derive the frequency of oscillation and gain threshold for any feedback oscillator circuit: 

1. **Identify and Break the Feedback Loop:** Open the feedback loop at a high-impedance terminal (such as the gate of a FET or the input of an op-amp). Insert a virtual test signal _V_ test at the input of the broken loop. 

5 

GATE PHYSICS 

FEEDBACK & OSCILLATORS 

2. **Solve for the Loop Transfer Function:** Trace the signal path around the broken loop and calculate the returned signal _V_ return as a function of _V_ test: 

      - _Aβ_ ( _s_ ) =<sup>_V_return(</sup><sup>_s_</sup><sup><u>)</u></sup> (10) _V_ test( _s_ ) 

3. **Enforce Phase Match (Determine** _ω_ 0 **):** Substitute _s_ = _iω_ and separate _Aβ_ ( _iω_ ) into its real and imaginary components: 

      - _Aβ_ ( _iω_ ) = Re [ _Aβ_ ( _iω_ )] + _i_ Im [ _Aβ_ ( _iω_ )] (11) 

   - Set the imaginary component to exactly zero to satisfy the 0<sup>_◦_</sup> or 180<sup>_◦_</sup> phase alignment: Im [ _Aβ_ ( _iω_ 0)] = 0 = _⇒_ Solve for _ω_ 0 (12) 

4. **Enforce Magnitude Match (Determine Gain Threshold):** Substitute the derived resonant frequency _ω_ 0 back into the real component and set the magnitude to exactly 1: 

      - Re [ _Aβ_ ( _iω_ 0)] = 1 = _⇒_ Determine the minimum required amplifier gain _A_ min (13) 

### **4. Problem-Solving Algorithm** 

* **Check Startup Conditions:** In real hardware, the loop gain at power-up must be designed slightly greater than unity ( _|Aβ| >_ 1) to ensure that the initial microscopic thermal noise builds up. The signal amplitude then grows until non-linear device limiting stabilizes the average loop gain to _|Aβ|_ = 1. In GATE exam problems, always solve using the exact threshold condition: _|Aβ|_ = 1. 

### **5. Characteristics** 

* **S-Plane Pole Trajectories:** At startup, the poles of the closed-loop transfer function lie in the right half of the complex _s_ -plane (Re[ _s_ ] _>_ 0), resulting in an exponentially growing sinusoidal response. As the amplitude limits, the poles migrate back to the imaginary axis (Re[ _s_ ] = 0), establishing a stable, constant-amplitude sinusoid. 

### **6. Crucial Pitfalls** 

#### **Barkhausen Criteria Traps** 

-  **Flipping Phase Shifts:** Combining a 180<sup>_◦_</sup> inverting amplifier with a feedback network that has a 0<sup>_◦_</sup> phase shift at resonance. This violates the phase condition, resulting in degenerative dampening instead of oscillation. 

-  **Neglecting Phase Shift Loading:** Assuming that individual passive stages in a feedback network do not load each other. For example, in an RC phase-shift network, you cannot calculate the phase shift of three RC stages by simply multiplying three isolated single-stage RC phase shifts. You must solve the complete, coupled 3-loop network. 

### **7. Standard Textbook Systems** 

- The Barkhausen criteria are illustrated by the following standard classes of harmonic oscillators: 

   -  **RC Oscillators:** Best suited for low-to-medium audio frequencies (1 Hz _−_ 1 MHz). 

   -  **LC Oscillators:** Best suited for high radio frequencies (100 kHz _−_ 100 MHz). 

6 

GATE PHYSICS 

FEEDBACK & OSCILLATORS 

## **3 Design & Analysis of RC Oscillators** 

### **1. Core Theory** 

RC oscillators utilize resistors and capacitors to construct a frequency-selective positive feedback loop. They are highly stable and easily tunable over the audio frequency range. 

-  **RC Phase-Shift Oscillator:** Uses an inverting amplifier (which provides a 180<sup>_◦_</sup> phase shift). To satisfy the Barkhausen phase condition (360<sup>_◦_</sup> total), the feedback loop contains a three-section RC ladder network where each section gradually shifts the phase by 60<sup>_◦_</sup> at the resonant frequency, contributing an additional 180<sup>_◦_</sup> phase shift. 

-  **Wien Bridge Oscillator:** Uses a non-inverting amplifier (which provides a 0<sup>_◦_</sup> phase shift). The feedback loop contains a lead-lag bridge circuit that acts as a band-pass filter, yielding a phase shift of exactly 0<sup>_◦_</sup> and maximum transmission at its resonant frequency. 

### **2. Mathematical Framework & Transfer Functions** 

|**Parameter**|**RC Phase-Shift (Op-Amp)**|**Wien Bridge**|
|---|---|---|
|**Feedback Network**|3-stage high-pass RC ladder|Series-Parallel lead-lag bridge|
|**Oscillation Frequency (**_f_0**)**|_f_0 =<br>1<br>2_πRC_<br>_~~√~~_<br>6<br>|_f_0 =<br>1<br>2_πRC_<br>|
|**Feedback Factor at** _f_0 **(**_β_**)**|_β_ =_−_<sup>1</sup><br>29|_β_ = +<sup>1</sup><br>3|
|**Amplifier Phase Shift (**∠_A_**)**|180<sup>_◦_</sup>(Inverting)|0<sup>_◦_</sup>(Non-Inverting)<br>|
|**Min. Gain for Oscillation (**_|A|_**)**|_|A| ≥_29|_A ≥_3 =_⇒_<br>_Rf_<br>_R_1 <sup>_≥_2</sup>|



Table 2: Design parameters of RC Phase-Shift and Wien Bridge oscillators. 

### **3. Circuit Analysis Milestones** 

Let us derive the parameters for the **Wien Bridge Oscillator** : 

1. **Solve Feedback Factor** _β_ ( _s_ ) **:** The feedback network consists of a series RC combination ( _Zs_ = _R_ + 1 _/sC_ ) connected in series with a parallel RC combination ( _Zp_ = _R ∥_ 1 _/sC_ ). The transfer function _β_ ( _s_ ) is: 



<!-- Start of picture text -->
Zp = sRC<br>β ( s ) = (14)<br>Zs  +  Zp s 2 R 2 C 2 + 3 sRC  + 1<br><!-- End of picture text -->

2. **Isolate the Imaginary Term (Phase Shift):** Substitute _s_ = _iω_ : 



<!-- Start of picture text -->
iωRC<br>β ( iω ) = (15)<br>(1  − ω 2 R 2 C 2 ) + 3 iωRC<br><!-- End of picture text -->

To obtain a phase shift of exactly 0<sup>_◦_</sup> , the transfer function must be purely real. Thus, set the real-axis offset term in the denominator to zero: 



<!-- Start of picture text -->
1 1<br>1  − ω 2 R 2 C 2 = 0 = ⇒ ω 0 = RC = ⇒ f 0 = 2 πRC (16)<br><!-- End of picture text -->

7 

GATE PHYSICS 

FEEDBACK & OSCILLATORS 

3. **Calculate the Feedback Attenuation** _β_ ( _iω_ 0) **:** Substitute _ω_ 0 = 1 _/RC_ back into the transfer function: 



<!-- Start of picture text -->
i (1)<br>β ( iω 0) = (17)<br>(0) + 3 i = 3 1<br><!-- End of picture text -->

This proves that the feedback network attenuates the signal by a factor of 3 at the resonant frequency. 

4. **Determine the Minimum Closed-loop Gain:** To satisfy Barkhausen’s magnitude condition _|Aβ|_ = 1, the non-inverting op-amp gain must be: 



<!-- Start of picture text -->
A ≥ 1 ≥ 3 = ⇒ Rf ≥ 2 (18)<br>β ( iω 0) = 3 = ⇒ 1 + R R f 1 R 1<br><!-- End of picture text -->

### **4. Problem-Solving Algorithm** 

#### **Analyzing RC Phase-Shift and Wien Bridge Circuits** 

1. **Identify the Oscillator Type:** Locate the feedback loop. If it contains a three-stage RC chain, it is an RC phase-shift oscillator. If it is a lead-lag network connected to the non-inverting terminal, it is a Wien bridge. 

2. **Compute the Resonant Frequency (** _f_ 0 **):** Apply the correct formula from Table 2. 

3. **Calculate Resistors/Capacitors:** If _f_ 0 and _C_ are given, solve for _R_ . 

4. **Verify Gain Threshold Requirements:** Confirm that the feedback resistors on the amplifier satisfy: 

   -  For Wien Bridge: _Rf ≥_ 2 _R_ 1. 

   -  For RC Phase Shift: Inverting closed-loop gain _Rf /R ≥_ 29. 

### **5. Characteristics** 

- **The Lead-Lag Transfer Curve:** For a Wien bridge, plotting the feedback magnitude _|β_ ( _iω_ ) _|_ 

- and phase _θ_ ( _ω_ ) against normalized frequency _ω/ω_ 0: 

   -  At low frequencies ( _ω ≪ ω_ 0), the series capacitor blocks transmission ( _β →_ 0 _, θ →_ +90<sup>_◦_</sup> ). 

   -  At high frequencies ( _ω ≫ ω_ 0), the parallel capacitor shunts the signal ( _β →_ 0 _, θ →−_ 90<sup>_◦_</sup> ). 

   -  At resonance ( _ω_ = _ω_ 0), the transmission peaks at _|β|_ = 1 _/_ 3 and the phase is exactly _θ_ = 0<sup>_◦_</sup> . 

8 

GATE PHYSICS 

FEEDBACK & OSCILLATORS 

### **6. Crucial Pitfalls** 

#### **RC Oscillator Errors** 

-  **Using the Wrong Frequency Formula:** Confusing the frequency coefficient _~~√~~_ 6 of the RC phase-shift oscillator with the Wien bridge. Remember: 



<!-- Start of picture text -->
1 1<br>f 0 , phase-shift = f 0 , Wien = (19)<br>2 πRC √ 6 , 2 πRC<br><!-- End of picture text -->

-  **BJT Phase-Shift Load Correction:** Forgetting that in a discrete BJT RC phaseshift oscillator, the output collector resistor _RC_ acts as part of the first RC stage. The oscillation frequency is shifted: 



<!-- Start of picture text -->
1<br>f 0 = (20)<br>2 πRC � 6 + 4( RC/R )<br><!-- End of picture text -->

### **7. Standard Textbook Systems** 

-  **The Op-Amp Wien Bridge Oscillator:** Utilises a dual-feedback op-amp circuit: a negative feedback path with a temperature-dependent tungsten lamp or thermistor to stabilize gain, and a positive feedback path containing the series-parallel RC lead-lag bridge. 

-  **The Op-Amp RC Phase-Shift Oscillator:** Uses an inverting op-amp with three identical RC high-pass sections in cascade, feeding back to the inverting input. 

9 

GATE PHYSICS 

FEEDBACK & OSCILLATORS 

## **4 Design & Analysis of LC Oscillators** 

### **1. Core Theory** 

LC oscillators utilize an LC resonant ”tank” circuit to construct the frequency-selective feedback loop. They are highly suited for radio frequency (RF) designs due to their high quality factor ( _Q_ -factor) and excellent spectral purity. 

-  **Colpitts Oscillator:** The tank circuit features a single inductor in parallel with a capacitive voltage divider (two series capacitors, _C_ 1 and _C_ 2, with a grounded center tap). The feedback signal is sampled across _C_ 1 or _C_ 2. 

-  **Hartley Oscillator:** The tank circuit features a single capacitor in parallel with an inductive voltage divider (two inductors, _L_ 1 and _L_ 2, with a grounded center tap). The feedback signal is sampled across _L_ 1 or _L_ 2. 

### **2. Mathematical Framework & Transfer Functions** 

|**Parameter**|**Colpitts Oscillator**|**Hartley Oscillator**|
|---|---|---|
|**Tank Inductance**|Single inductor _L_|Two inductors _L_1_, L_2 with mutual induct|
|**Tank Capacitance**|Two capacitors _C_1_, C_2 in series<br>|Single capacitor _C_|
|**Equivalent Parameter**|_C_eq =<br>_C_1_C_2<br>_C_1+_C_2<br>|_L_eq =_L_1+_L_2+ 2_M_ (usually _M ≈_<br>|
|**Oscillation Frequency (**_f_0**)**|_f_0 =<br>1<br>2_π_<sup>_~~√~~_</sup><br>_LC_eq<br>|_f_0 =<br>1<br>2_π_<sup>_~~√~~_</sup><br>_L_eq_C_<br>|
|**Feedback Factor (**_β_**)**|_β ≈_<sup>_C_1</sup><br>_C_2<br>|_β ≈_<sup>_L_2</sup><br>_L_1<br>|
|**Min. Gain for Oscillation (**_Av_**)**|_Av ≥_<sup>_C_2</sup><br>_C_1|_Av ≥_<sup>_L_1</sup><br>_L_2|



Table 3: Design parameters of Colpitts and Hartley oscillators. 

### **3. Circuit Analysis Milestones** 

Let us derive the parameters of the **Colpitts Oscillator** using the equivalent loop impedance: 

1. **Establish the Tank Impedance Loop:** The active device (e.g., a BJT CE amplifier) has input impedance _hie_ and output current source _gmvbe_ . The tank circuit can be modeled as a continuous loop of three reactances: _X_ 1 = _−_ 1 _/ωC_ 1, _X_ 2 = _−_ 1 _/ωC_ 2, and _X_ 3 = _ωL_ . 

2. **Formulate the Loop Equation:** Sum the reactances around the closed tank loop: 



<!-- Start of picture text -->
1<br>−<br>X 1 +  X 2 +  X 3 = 0 = ⇒− 1 +  ωL  = 0 (21)<br>ωC 1 ωC 2<br><!-- End of picture text -->

3. **Extract the Resonant Frequency (** _ω_ 0 **):** 



<!-- Start of picture text -->
ωL  = 1 + 1 = ⇒ ω 0 = 1 (22)<br>ω � C 11 C 2 � � LC eq<br><!-- End of picture text -->

This derives the standard Colpitts frequency equation. 

10 

GATE PHYSICS 

FEEDBACK & OSCILLATORS 

4. **Evaluate the Minimum Current Gain:** Apply the loop current balance. The feedback ratio is determined by the capacitive voltage divider ratio: 



<!-- Start of picture text -->
β = Vf = X 1 = C 2 (23)<br>Vo X 2 C 1<br><!-- End of picture text -->

To satisfy Barkhausen’s magnitude condition, the minimum gain of the amplifier must be: 



<!-- Start of picture text -->
Av ≥ 1 (24)<br>β = C C 2 1<br><!-- End of picture text -->

### **4. Problem-Solving Algorithm** 

#### **Solving Colpitts and Hartley Numerical Problems** 

1. **Identify the Oscillator Type:** Locate the grounded tap in the tank circuit. If the center tap is between two capacitors, it is a Colpitts oscillator. If it is between two inductors, it is a Hartley oscillator. 

2. **Calculate the Equivalent Tank Parameter:** 



<!-- Start of picture text -->
 For Colpitts: C eq = CC 11+ CC 22 .<br><!-- End of picture text -->

   -  For Hartley: _L_ eq = _L_ 1 + _L_ 2 (assume mutual coupling _M_ = 0 unless explicitly given). 

3. **Solve for the Oscillation Frequency (** _f_ 0 **):** Apply the LC resonant equation: 



<!-- Start of picture text -->
1<br>f 0 = (25)<br>2 π � L eq C eq<br><!-- End of picture text -->

4. **Verify Gain Threshold Requirements:** Confirm the ratio of the split tank components matches the amplifier gain. 

### **5. Characteristics** 

* **The Tank Circuit Selectivity:** Plotting the impedance magnitude of the parallel LC tank circuit shows a sharp peak at _f_ 0. The sharpness of this peak is determined by the quality factor ( _Q_ = _ω_ 0 _L/R_ series). High- _Q_ tank circuits suppress off-resonance noise, resulting in exceptional frequency stability and low phase noise. 

11 

GATE PHYSICS 

FEEDBACK & OSCILLATORS 

### **6. Crucial Pitfalls** 

#### **LC Oscillator Traps** 

-  **Inverting Series Capacitance:** Incorrectly calculating _C_ eq for a Colpitts oscillator by adding the capacitors in parallel ( _C_ 1 + _C_ 2). Because the capacitors are in series around the tank loop, you must use the reciprocal formula: 



<!-- Start of picture text -->
C 1 C 2<br>C eq = (26)<br>C 1 +  C 2<br><!-- End of picture text -->

-  **Neglecting Mutual Inductance (** _M_ **):** Calculating the frequency of a Hartley oscillator using _L_ eq = _L_ 1 + _L_ 2 when a non-zero mutual coupling coefficient _M_ is explicitly provided. You must use the complete formula: 

_L_ eq = _L_ 1 + _L_ 2 + 2 _M_ (27) 

### **7. Standard Textbook Systems** 

-  **The Transistor Colpitts Oscillator:** A discrete npn BJT amplifier circuit where the collector-emitter voltage is fed back to the base-emitter terminal through a split capacitive divider ( _C_ 1 _, C_ 2), providing RF positive feedback. 

-  **The Op-Amp Hartley Oscillator:** An op-amp circuit where the non-inverting terminal is fed back from the center tap of two coupled inductors in parallel with a tuning capacitor. 

12 

GATE PHYSICS 

FEEDBACK & OSCILLATORS 

## **References** 

1. Boylestad, Robert L., and Louis Nashelsky. _Electronic Devices and Circuit Theory_ . 11th ed. 

2. Floyd, Thomas L. _Digital Fundamentals_ . 11th ed. 

13 

GATE PHYSICS 

OP-AMPS, FILTERS & WAVEFORMS 

# **GATE PHYSICS STUDY NOTES Operational Amplifiers, Active Filters, & Waveform Generators** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**<br>**Ideal and Practical Operational Amplifiers & Linear Applications**|**2**|
|---|---|
|**2**<br>**Active Filters: Low-Pass, High-Pass, and Band-Pass**|**6**|
|**3**<br>**Waveform Generators: Sine, Square, and Triangular Wave Oscillators**|**10**|



1 

GATE PHYSICS 

OP-AMPS, FILTERS & WAVEFORMS 

## **1 Ideal and Practical Operational Amplifiers & Linear Applications** 

### **1. Core Theory** 

An **Operational Amplifier (Op-Amp)** is a direct-coupled, high-gain, differential-input, singleended output integrated circuit amplifier. 

-  **Ideal Op-Amp Model:** Operates as a voltage-controlled voltage source (VCVS) with: 

   - Infinite open-loop differential gain ( _AOL →∞_ ). 

   - Infinite input resistance ( _Rin →∞_ ), meaning zero input bias currents ( _I_ + = _I−_ = 0). 

   - Zero output resistance ( _Rout_ = 0), allowing it to drive any load without loading effects. 

   - **–** Infinite bandwidth ( _BW →∞_ ), amplifying AC signals from DC to infinite frequencies without attenuation or phase shift. 

   - Infinite Common-Mode Rejection Ratio ( _CMRR →∞_ ), completely rejecting noise voltages common to both input terminals. 

   - Zero offset voltage ( _Vio_ = 0) and zero offset current ( _Iio_ = 0), meaning _Vout_ = 0 when _V_ + = _V−_ = 0. 

   - Infinite Slew Rate ( _SR →∞_ ), allowing the output to track instantaneous changes in the input signal. 

-  **The Virtual Short Concept:** In a negative feedback configuration, the extremely high open-loop gain forces the differential input voltage to approach zero: 



<!-- Start of picture text -->
Vd =  V +  − V− = Vout → 0 = ⇒ V + ≈ V−<br>AOL<br><!-- End of picture text -->

If one input is physically tied to ground, this becomes a **virtual ground** ( _V− ≈_ 0). 

-  **Practical Op-Amp Non-Idealities:** Practical devices (e.g., UA741) have finite values ( _AOL ≈_ 2 _×_ 10<sup>5</sup> , _Rin ≈_ 2 MΩ, _Rout ≈_ 75 Ω, finite CMRR _≈_ 90 dB, and a finite slew rate _SR ≈_ 0 _._ 5 V _/µ_ s). Input bias currents ( _IB_ ) and input offset voltages ( _Vio_ ) introduce DC offsets at the output, requiring compensation techniques. 

### **2. Mathematical Framework & Transfer Functions** 

 **Inverting Amplifier:** 



<!-- Start of picture text -->
Vout =  − Rf Vin = ⇒ Av = Vout =  − Rf (1)<br>R 1 Vin R 1<br><!-- End of picture text -->

where _Rf_ is the feedback resistor and _R_ 1 is the input resistor. 

 **Non-Inverting Amplifier:** 



<!-- Start of picture text -->
Vout = 1 + Rf Vin = ⇒ Av = 1 + Rf (2)<br>� R 1 � R 1<br><!-- End of picture text -->

 **Summing Amplifier (Adder):** 



<!-- Start of picture text -->
Vout =  − V 1 + Rf V 2 +  · · ·  + Rf Vn (3)<br>� RRf 1 R 2 Rn �<br><!-- End of picture text -->

2 

GATE PHYSICS 

OP-AMPS, FILTERS & WAVEFORMS 

 **Ideal Integrator (Time-Domain & s-Domain):** 



<!-- Start of picture text -->
1 1<br>vout ( t ) =  − vin ( τ ) dτ +  vout (0) = ⇒ Vout ( s ) =  − Vin ( s ) (4)<br>R 1 Cf �0 t sR 1 Cf<br><!-- End of picture text -->

where _Cf_ is the feedback capacitor. 

-  **Practical Integrator (Lossy Integrator):** A shunt resistor _Rf_ is placed in parallel with _Cf_ to prevent DC input offsets from driving the op-amp into saturation. The transfer function is: 



<!-- Start of picture text -->
Rf /R 1<br>H ( s ) = Vout ( s ) (5)<br>Vin ( s ) =  − 1 +  sRf Cf<br><!-- End of picture text -->

 **Ideal Differentiator (Time-Domain & s-Domain):** 



<!-- Start of picture text -->
dvin ( t )<br>vout ( t ) =  −Rf C 1 = ⇒ Vout ( s ) =  −sRf C 1 Vin ( s ) (6)<br>dt<br><!-- End of picture text -->

-  **Practical Differentiator:** A series resistor _R_ 1 is placed in series with the input capacitor _C_ 1 to limit high-frequency gain and prevent instability/high-frequency noise amplification. The transfer function is: 



<!-- Start of picture text -->
sRf C 1<br>H ( s ) =  − (7)<br>1 +  sR 1 C 1<br><!-- End of picture text -->

### **3. Circuit Analysis Milestones** 

Linear operational amplifier circuits can be analyzed using these four systematic milestones: 

1. **Assert Ideal Input Currents:** State that no current enters or leaves the op-amp’s differential input terminals due to infinite input impedance: _I_ + = _I−_ = 0. 

2. **Apply the Virtual Short Condition (for Negative Feedback):** Set the potential at the inverting terminal equal to the non-inverting terminal: _V−_ = _V_ +. Identify _V_ + directly if it is connected to a known voltage source or ground. 

3. **Apply Kirchhoff’s Current Law (KCL) at the Inverting Node (** _V−_ **):** 



<!-- Start of picture text -->
� I entering = 0 = ⇒ Vin − V− + Vout − V− = 0 (8)<br>R 1 Zf<br><!-- End of picture text -->

where _Zf_ is the feedback impedance ( _Rf_ , 1 _/sCf_ , or parallel combinations). 

4. **Solve the Algebraic Node Equation for** _Vout_ **:** Substitute _V−_ = _V_ + and simplify the equation to express the output voltage _Vout_ as a function of the input voltage _Vin_ . 

3 

GATE PHYSICS 

OP-AMPS, FILTERS & WAVEFORMS 

### **4. Problem-Solving Algorithm** 

#### **Analysis of Op-Amp Circuits with Mixed Passive Networks** 

1. **Identify the Feedback Path:** Verify that negative feedback is present (a path exists from the output terminal back to the inverting input terminal). If positive feedback is present, do NOT use the virtual short concept; the op-amp will behave as a comparator or bistable multivibrator. 

2. **Calculate the Non-Inverting Terminal Voltage (** _V_ + **):** Solve the passive circuit network connected to the non-inverting terminal using voltage dividers or KCL. 

3. **Write the Inverting Node KCL Equation:** Set the sum of currents leaving the _V−_ node to zero: 



<!-- Start of picture text -->
V− − V 1 + V− − Vout +  I− = 0<br>R 1 Zf<br><!-- End of picture text -->

Set _I−_ = 0 and replace _V−_ with the calculated value of _V_ + (since _V−_ = _V_ +). 

4. **Solve for** _Vout_ **and check Saturation Limits:** Calculate _Vout_ . Ensure that the calculated output voltage does not exceed the power supply rails: 



<!-- Start of picture text -->
−VEE < Vout <  + VCC<br><!-- End of picture text -->

If the calculated value exceeds these boundaries, the output saturates: _Vout_ = _±V_ sat _≈ ±_ ( _VCC −_ 1 _._ 5 V). 

### **5. Truth Tables & Characteristics** 

The transfer characteristics of an open-loop comparator and a closed-loop linear inverting amplifier are illustrated below: 

 **Open-Loop Voltage Transfer Curve:** 



<!-- Start of picture text -->
+ V sat for v + > v−<br>vout = (9)<br>� −V sat for v + < v−<br><!-- End of picture text -->

Because the open-loop gain _AOL_ is extremely large ( _>_ 10<sup>5</sup> ), even a tiny microvolt-scale difference between inputs drives the output into saturation. 

-  **Closed-Loop Inverting Amplifier I-V Characteristic:** The slope of the linear region is defined by the closed-loop gain _Av_ = _−Rf /R_ 1: 



<!-- Start of picture text -->
vout =  − Rf vin for vin (10)<br>R 1 ���� − RRf 1 ���� ≤ V sat<br><!-- End of picture text -->

Outside this range, the output clamps flat at _±V_ sat. 

4 

GATE PHYSICS 

OP-AMPS, FILTERS & WAVEFORMS 

### **6. Crucial Pitfalls** 

#### **Linear Op-Amp Traps to Avoid** 

-  **Assuming Virtual Ground under Positive Feedback:** Applying _V−_ = _V_ + to comparator, Schmitt trigger, or oscillator circuits. The virtual short condition is **only** valid when the op-amp operates in a stable, closed-loop negative feedback configuration. 

-  **Forgetting Output Saturation Limits:** Calculating a massive closed-loop gain (e.g., _Av_ = _−_ 100, with _Vin_ = 0 _._ 5 V) and writing _Vout_ = _−_ 50 V when the power supply rails are only _±_ 15 V. The output will be clipped flat at _−V_ sat _≈−_ 13 _._ 5 V. 

-  **Neglecting Slew Rate Distortion:** Assuming the output of a high-frequency amplifier can track a large-signal sine wave perfectly. If the maximum rate of change of the input signal exceeds the slew rate (2 _πfVp > SR_ ), the output sine wave deforms into a triangular wave. 

### **7. Standard Textbook Systems** 

-  **The Practical Integrator with Low-Frequency Stabilization:** An op-amp with a parallel _Rf Cf_ feedback network. It behaves as an inverting amplifier with gain _−Rf /R_ 1 at low frequencies (DC), preventing drift saturation, and behaves as an integrator at frequencies above the corner frequency _fc_ = 1 _/_ (2 _πRf Cf_ ). 

-  **The Instrumentation Amplifier:** A three-op-amp configuration that provides exceptionally high input impedance, high differential gain, and outstanding CMRR, commonly used to amplify weak transducer signals. 

5 

GATE PHYSICS 

OP-AMPS, FILTERS & WAVEFORMS 

## **2 Active Filters: Low-Pass, High-Pass, and Band-Pass** 

### **1. Core Theory** 

An **Active Filter** is a frequency-selective electronic circuit that utilizes active components (such as operational amplifiers) in combination with passive RC networks to isolate, attenuate, or amplify specific frequency bands. 

-  **Advantages Over Passive Filters:** Passive LC filters require bulky, heavy inductors that suffer from core losses and magnetic pickup at low frequencies. Active filters eliminate the need for inductors entirely, use compact capacitors, provide high input impedance (to prevent loading the source) and low output impedance, and can supply passband power gain. 

-  **Filter Types:** 

   - **Low-Pass Filter (LPF):** Passes low frequencies from DC up to a critical cutoff frequency _fc_ , while attenuating higher frequencies. 

   - **High-Pass Filter (HPF):** Attenuates low frequencies up to the cutoff _fc_ , while passing all higher frequencies. 

   - **Band-Pass Filter (BPF):** Passes a specific band of frequencies located between a lower cutoff _fc_ 1 and an upper cutoff _fc_ 2, while attenuating all frequencies outside this band. 

-  **Filter Responses (Butterworth):** The Butterworth approximation is characterized by a **maximally flat amplitude response** in the passband, with a roll-off rate of _−_ 20 dB/decade (or _−_ 6 dB/octave) per pole in the stopband. 

### **2. Mathematical Framework & Transfer Functions** 

* **First-Order Active Low-Pass Filter:** 



<!-- Start of picture text -->
A 0 A 0<br>=<br>H ( s ) = Vout ( s ) (11)<br>Vin ( s ) = 1 +  s/ωc 1 +  sRC<br><!-- End of picture text -->

where the passband gain is _A_ 0 = 1 + _Rf /R_ 1 (for non-inverting topology), and the critical cutoff frequency (in rad/s and Hz) is: 



<!-- Start of picture text -->
1 1<br>ωc = RC = ⇒ fc = 2 πRC (12)<br><!-- End of picture text -->

* **First-Order Active High-Pass Filter:** 



<!-- Start of picture text -->
H ( s ) = A 0  · ( s/ωc ) = A 0  · sRC (13)<br>1 +  s/ωc 1 +  sRC<br><!-- End of picture text -->

* **Second-Order Low-Pass Filter (Sallen-Key Topology):** The transfer function of a secondorder active low-pass filter is: 



<!-- Start of picture text -->
A 0  · ωc 2 A 0<br>=<br>H ( s ) = (14)<br>s 2 + � ωQc � s  +  ωc 2 s 2 R 2 C 2 +  sRC (3  − A 0) + 1<br><!-- End of picture text -->

6 

GATE PHYSICS 

OP-AMPS, FILTERS & WAVEFORMS 

where the quality factor _Q_ (which dictates the damping of the filter) is: 



<!-- Start of picture text -->
Q  = 1 with A 0 = 1 + Rf (15)<br>3  − A 0 R 1<br><!-- End of picture text -->

* For a **second-order Butterworth response** , set _Q_ = 1 _/_ _~~√~~_ 2 _≈_ 0 _._ 707, which requires a passband gain of _A_ 0 = 3 _−_ _~~√~~_ 2 _≈_ 1 _._ 586. * **Second-Order Active Band-Pass Filter (MultipleFeedback):** 



<!-- Start of picture text -->
ω 0<br>A 0  · s<br>� Q �<br>H ( s ) = (16)<br>s 2 + � ωQ 0 � s  +  ω 0 2<br><!-- End of picture text -->

where _ω_ 0 =<sup>_~~√~~_</sup> _<u>ωc</u>_ 1 _<u>ωc</u>_ 2 is the center frequency, and _Q_ = _ω_ 0 _/BW_ = _ω_ 0 _/_ ( _ωc_ 2 _− ωc_ 1) is the quality factor. 

### **3. Circuit Analysis Milestones** 

To analyze an active filter circuit and find its transfer function: 

1. **Represent passive elements in the s-domain:** Replace capacitors with their complex s-domain impedances: _ZC_ ( _s_ ) = _sC_ <u>1</u><sup>.</sup> 

2. **Formulate Node Voltage Equations:** Apply KCL at any intermediate nodes (such as the non-inverting input terminal _V_ + and any floating nodes in second-order filters) using complex impedances. 

3. **Apply Op-Amp Constraints:** Set _V−_ = _V_ + and relate the output node voltage to _V−_ via the feedback gain stage: _Vout_ = _A_ 0 _V−_ . 

4. **Solve for the Transfer Function** _H_ ( _s_ ) = _Vout_ ( _s_ ) _/Vin_ ( _s_ ) **:** Algebraically eliminate all intermediate node voltages to find the ratio of the output to the input, and write the resulting transfer function in standard normalized form. 

7 

GATE PHYSICS 

OP-AMPS, FILTERS & WAVEFORMS 

### **4. Problem-Solving Algorithm** 

#### **Designing and Analyzing Second-Order Sallen-Key Filters** 

1. **Identify the Filter Type:** Look at the arrangement of components in the Sallen-Key loop: 

   -  If resistors are in series on the input path and capacitors shunt to ground and feedback, it is a **Low-Pass Filter** . 

   -  If capacitors are in series and resistors shunt, it is a **High-Pass Filter** . 

2. **Calculate the Cutoff Frequency (** _fc_ **):** For equal-component designs ( _R_ 1 = _R_ 2 = _R_ and _C_ 1 = _C_ 2 = _C_ ), calculate: 



<!-- Start of picture text -->
1<br>fc =<br>2 πRC<br><!-- End of picture text -->

3. **Determine the Passband Gain (** _A_ 0 **) for Butterworth Response:** For a Butterworth response, the damping factor is _α_ = 1 _._ 414, making the quality factor _Q_ = 1 _/α ≈_ 0 _._ 707. Since _Q_ = 1 _/_ (3 _− A_ 0), enforce: 



<!-- Start of picture text -->
A 0 = 3  − 1<br>Q = 1 . 586 = ⇒ Rf = 0 . 586 R 1<br><!-- End of picture text -->

4. **Calculate Stopband Attenuation (Roll-Off):** Identify the filter order _n_ . The roll-off rate is _−_ 20 _n_ dB/decade. For a second-order filter ( _n_ = 2), the roll-off is _−_ 40 dB/decade. To find the gain at a frequency _f_ far in the stopband ( _f ≫ fc_ ): Gain( _f_ ) _≈ A_ 0 � _<u>ffc</u>_ � _n_ 

### **5. Truth Tables & Characteristics** 

The frequency response characteristics (Bode plots) of active low-pass and high-pass filters are described below: * **Low-Pass Filter Bode Plot:** 

   -  **Passband ( _f < fc_ ):** The gain is flat at _|H_ ( _iω_ ) _| ≈ A_ 0 (or 20 log10 _A_ 0 in dB). 

   -  **Cutoff frequency ( _f_ = _fc_ ):** The gain drops to _A_ 0 _/_ _~~√~~_ 2 (or drops by _−_ 3 dB below the passband gain). 

   -  **Stopband ( _f > fc_ ):** The gain drops off linearly on a logarithmic scale with a slope of _−_ 20 dB/decade (first-order) or _−_ 40 dB/decade (second-order). 

- **High-Pass Filter Bode Plot:** 

   -  **Stopband ( _f < fc_ ):** The gain increases with a slope of +20 dB/decade (first-order) or +40 dB/decade (second-order). 

   -  **Cutoff frequency ( _f_ = _fc_ ):** The gain is _−_ 3 dB below the passband gain. 

   -  **Passband ( _f > fc_ ):** The gain levels off flat at _A_ 0. 

8 

GATE PHYSICS 

OP-AMPS, FILTERS & WAVEFORMS 

### **6. Crucial Pitfalls** 

#### **Active Filter Design Traps** 

-  **The Multi-Stage Cutoff Frequency Inversion Trap:** Assuming that cascading two identical first-order filters with cutoff _fc_ creates a second-order filter with the same cutoff. In reality, cascading two identical stages with cutoff _fc_ reduces the overall _−_ 3 dB cutoff frequency to _fc_<sup>_′_=</sup><sup>_fc_</sup> ~~�~~ 2<sup>1</sup><sup>_/_2</sup> _−_ 1 _≈_ 0 _._ 643 _fc_ . You must use Sallen-Key designs with specific damping coefficients to maintain a constant cutoff. 

-  **Neglecting Op-Amp Gain-Bandwidth (GBW) Limits:** Designing an active highpass filter with a cutoff of 1 MHz using an op-amp with a GBW of 1 MHz. At high frequencies, the op-amp’s open-loop gain drops to unity, completely destroying the high-pass filter’s passband gain and turning it into a band-pass filter. 

### **7. Standard Textbook Systems** 

-  **The Sallen-Key Second-Order Low-Pass Filter:** A standard non-inverting active filter. It uses two series resistors on the input path, a shunt capacitor to ground, a feedback capacitor connected back to the junction of the resistors, and a non-inverting amplifier stage to define the gain. 

-  **The Multiple-Feedback (MFB) Band-Pass Filter:** An inverting active filter configuration that uses a single op-amp with a dual-feedback path (capacitive and resistive) to produce a narrow, high-Q band-pass response, commonly used in audio equalizers. 

9 

GATE PHYSICS 

OP-AMPS, FILTERS & WAVEFORMS 

## **3 Waveform Generators: Sine, Square, and Triangular Wave Oscillators** 

### **1. Core Theory** 

A **Waveform Generator** is an active electronic circuit that generates periodic AC signals (sine, square, or triangular waves) from a DC power supply without requiring an external AC input signal. 

-  **Sinusoidal Oscillators (Wien Bridge):** Generate low-distortion sine waves using linear positive feedback. The circuit stabilizes its frequency of oscillation at the point where the feedback loop’s total phase shift is exactly 0<sup>_◦_</sup> and the loop gain is unity, in accordance with the Barkhausen criteria. 

-  **Relaxation Oscillators (Square Wave):** Use non-linear feedback to switch an active device between two unstable, saturated states. An RC network controls the time constant of capacitor charging and discharging, defining the period of oscillation. 

-  **Triangular Wave Generators:** Cascade an astable square-wave generator (Schmitt trigger) with an integrating circuit. The square-wave output is integrated over time, producing linear rising and falling voltage ramps that sweep between the Schmitt trigger’s threshold limits. 

### **2. Mathematical Framework & Transfer Functions** 

- **Wien Bridge Sine-Wave Oscillator:** The frequency of oscillation ( _f_ 0) is: 



<!-- Start of picture text -->
1 1<br>=<br>f 0 = (for R 1 =  R 2 =  R, C 1 =  C 2 =  C ) (17)<br>2 π √ R 1 R 2 C 1 C 2 2 πRC<br><!-- End of picture text -->

The feedback factor at resonance is _β_ = 1 _/_ 3. To satisfy the Barkhausen criterion ( _Aβ_ = 1), the closed-loop gain of the non-inverting amplifier must be: 



<!-- Start of picture text -->
Rf<br>A  = 1 + ≥ 3 = ⇒ Rf ≥ 2 R gain (18)<br>R gain<br><!-- End of picture text -->

* **Astable Multivibrator (Square-Wave Generator):** An op-amp comparator with a positive feedback hysteresis loop (Schmitt trigger) and a negative feedback RC integrator. The output switches between + _V_ sat and _−V_ sat. The feedback fraction of the Schmitt trigger is: 



<!-- Start of picture text -->
R 2<br>β = (19)<br>R 1 +  R 2<br><!-- End of picture text -->

The upper and lower threshold limits are _V_ UT = + _βV_ sat and _V_ LT = _−βV_ sat. The period ( _T_ ) of the square-wave output is: 



<!-- Start of picture text -->
T = 2 RC  ln = 2 RC  ln 1 + 2 R 2 = ⇒ f = 1 (20)<br>� 1 +1  − ββ � � R 1 � T<br><!-- End of picture text -->

* **Triangular Wave Generator (Schmitt Trigger + Integrator):** The square-wave output of the Schmitt trigger ( _v_ sq = _±V_ sat) is integrated. The slope of the triangular ramp is: 



<!-- Start of picture text -->
dv out =  ∓ V sat (21)<br>dt R 3 Ci<br><!-- End of picture text -->

10 

GATE PHYSICS 

OP-AMPS, FILTERS & WAVEFORMS 

The peak-to-peak amplitude of the triangular wave is determined by the hysteresis thresholds of the Schmitt trigger: 



<!-- Start of picture text -->
Vp - p = 2 V sat (22)<br>� RR 12 �<br><!-- End of picture text -->

The frequency of oscillation ( _f_ ) of the cascaded system is: 



<!-- Start of picture text -->
R 1<br>f = (23)<br>4 R 2 R 3 Ci<br><!-- End of picture text -->

### **3. Circuit Analysis Milestones** 

To analyze an astable square-wave generator (relaxation oscillator): 

1. **Identify the Schmitt Trigger Thresholds:** Solve the positive feedback loop to find the upper and lower threshold voltages of the non-inverting terminal: 



<!-- Start of picture text -->
R 2<br>V + =  ±βV sat =  ±V sat (24)<br>� R 1 +  R 2 �<br><!-- End of picture text -->

2. **Model the Capacitor Charging Equation:** The capacitor connected to the inverting terminal charges toward the output saturation voltage: 



<!-- Start of picture text -->
vC ( t ) =  V final + ( V initial  − V final)  e −t/RC (25)<br><!-- End of picture text -->

3. **Apply Switching Conditions:** Set _V_ initial = _−βV_ sat, _V_ final = + _V_ sat, and solve for the time _t_ = _T/_ 2 at which the capacitor voltage reaches the upper threshold: 



<!-- Start of picture text -->
vC ( T/ 2) =  V UT = ⇒ + βV sat =  V sat + ( −βV sat  − V sat)  e −T/ 2 RC (26)<br><!-- End of picture text -->

4. **Solve for the Period (** _T_ **):** Simplify the exponential equation to isolate _T_ : 



<!-- Start of picture text -->
e −T/ 2 RC = 1 1 +  −  β β = ⇒ T = 2 RC  ln � 1 +1  − ββ � (27)<br><!-- End of picture text -->

11 

GATE PHYSICS 

OP-AMPS, FILTERS & WAVEFORMS 

### **4. Problem-Solving Algorithm** 

#### **Calculating Frequency and Waveform Amplitudes** 

1. **Check the Oscillator Configuration:** 

   -  For a **Wien Bridge** : Ensure _Rf ≥_ 2 _Rg_ is satisfied for self-starting oscillations. Calculate _f_ = 1 _/_ (2 _πRC_ ). The output is a sine wave of amplitude limited by the non-linear stabilization elements. 

   -  For an **Astable Multivibrator** : Calculate the feedback fraction _β_ = _R_ 2 _/_ ( _R_ 1 + _R_ 2). Calculate the period _T_ = 2 _RC_ ln[(1 + _β_ ) _/_ (1 _− β_ )] and find _f_ = 1 _/T_ . The output is a square wave. 

   -  For an **Integrator-Schmitt Trigger Cascade** : Identify the integrator components ( _R_ 3 _, Ci_ ) and the Schmitt trigger components ( _R_ 1 _, R_ 2). Use the frequency equation: 



<!-- Start of picture text -->
R 1<br>f =<br>4 R 2 R 3 Ci<br><!-- End of picture text -->

2. **Calculate peak-to-peak amplitude of the Triangle Wave:** Find the saturation voltage of the Schmitt trigger ( _V_ sat _≈ VCC −_ 1 _._ 5 V). Calculate: 



<!-- Start of picture text -->
Vp - p = 2 V sat<br>� RR 21 �<br><!-- End of picture text -->

### **5. Truth Tables & Characteristics** 

The operational waveforms of an astable multivibrator are illustrated below: * **Square-Wave Output (** _v_ **out):** Alternates symmetrically between + _V_ sat and _−V_ sat, creating a high-amplitude, high-speed pulse train. * **Capacitor Voltage (** _vC_ **):** A continuous, non-linear exponential charging and discharging curve that sweeps back and forth between the threshold limits: 



<!-- Start of picture text -->
−βV sat ≤ vC ( t )  ≤ + βV sat (28)<br><!-- End of picture text -->

When _vC_ ( _t_ ) reaches + _βV_ sat, the comparator input inverts, snapping _v_ out down to _−V_ sat. The capacitor then begins to discharge toward _−V_ sat until it hits the lower threshold _−βV_ sat, repeating the cycle. 

12 

GATE PHYSICS 

OP-AMPS, FILTERS & WAVEFORMS 

### **6. Crucial Pitfalls** 

#### **Waveform Generator Traps to Avoid** 

-  **The Inverting vs. Non-Inverting Schmitt Trigger Confusion:** Using the wrong threshold equation. In an inverting Schmitt trigger, the input is compared to a fraction of the output, giving _β_ = _R_ 2 _/_ ( _R_ 1 + _R_ 2). In a non-inverting Schmitt trigger, the thresholds are _±V_ sat( _R_ 1 _/R_ 2). Mixing up these configurations will yield completely incorrect period calculations. 

-  **Assuming Ideal Rails for Amplitude Calculations:** Calculating the peak-to-peak amplitude of a waveform using the exact supply voltage _VCC_ (e.g., 15 V) instead of the realistic output saturation limit _V_ sat (which is typically 1 _._ 5 V below the rails, i.e., 13 _._ 5 V). This is a frequent source of error in numerical answer questions. 

### **7. Standard Textbook Systems** 

-  **The Wien Bridge Oscillator with Automatic Gain Control (AGC):** A standard sinewave generator using a non-linear resistance (such as a tungsten lamp filament or JFET in the feedback path) to automatically adjust the closed-loop gain back to exactly 3 when the output amplitude fluctuates. 

-  **The Practical Integrator-Schmitt Trigger Triangle-Wave Generator:** A dual-opamp cascade where the first stage acts as a non-inverting Schmitt trigger and the second acts as an inverting integrator, producing highly linear, symmetrical triangular sweeps. 

13 

GATE PHYSICS 

OP-AMPS, FILTERS & WAVEFORMS 

## **References** 

1. Gayakwad, Ramakant A. _Op-Amps and Linear Integrated Circuits_ . Prentice Hall, 4th Edition. 

2. Boylestad, Robert L. & Nashelsky, Louis. _Electronic Devices and Circuit Theory_ . Pearson, 11th Edition. 

3. Floyd, Thomas L. _Digital Fundamentals_ . Pearson, 11th Edition. 

14 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

# **GATE PHYSICS STUDY NOTES Digital Electronics, Sequential Logic, Timers, & Data Converters** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**|**Digital Logic, Boolean Algebra, and Logic Gates**|**2**|
|---|---|---|
|**2**|**Combinational Circuits: Multiplexers and Decoders**|**5**|
|**3**|**Sequential Circuits: SR, JK, D, and T Flip-Flops**|**8**|
|**4**|**Counters and Shift Registers**|**10**|
|**5**|**The 555 Timer**|**13**|
|**6**|**Principles of A/D and D/A Conversion**|**16**|



1 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

## **1 Digital Logic, Boolean Algebra, and Logic Gates** 

### **1. Core Theory** 

* **Digital Logic:** Represents the mathematical processing of discrete-state information, where physical quantities are quantized into two binary states: High (1, representing a higher voltage level, typically 5 V or 3 _._ 3 V) and Low (0, representing ground or 0 V). * **Boolean Algebra:** The algebraic system formulated by George Boole, where variables can only take values of 0 or 1, and the principal operations are conjunction (AND, _·_ ), disjunction (OR, +), and negation (NOT, _X_ ¯ ). * **Logic Gates:** The fundamental hardware building blocks of digital systems. They are implemented using non-linear semiconductor switches (diodes and transistors) operating in their extreme regions (cutoff and saturation) to perform elementary Boolean operations. * **Universal Gates:** NAND and NOR gates are classified as universal gates because any arbitrary Boolean transfer function can be realized exclusively using combinations of only NAND or only NOR gates. 

### **2. Mathematical Framework & Transfer Functions** 

- **Boolean Postulates and Theorems:** 

   -  **Idempotent Law:** _A · A_ = _A_ , _A_ + _A_ = _A_ 

   -  **Complementarity:** _A · A_<sup>¯</sup> = 0, _A_ + _A_<sup>¯</sup> = 1 

   -  **Distributive Law:** _A_ + ( _B · C_ ) = ( _A_ + _B_ ) _·_ ( _A_ + _C_ ), _A ·_ ( _B_ + _C_ ) = ( _A · B_ ) + ( _A · C_ ) 

   -  **Absorption Law:** _A_ + ( _A · B_ ) = _A_ , _A ·_ ( _A_ + _B_ ) = _A_ 

   -  **Consensus Theorem:** _AB_ + _AC_<sup>¯</sup> + _BC_ = _AB_ + _AC_<sup>¯</sup> 

- **De Morgan’s Theorems:** 

_A · B_ = _A_<sup>¯</sup> + _B_<sup>¯</sup> (1) 

_A_ + _B_ = _A_<sup>¯</sup> _· B_<sup>¯</sup> (2) 

* **Shannon’s Expansion Theorem:** _F_ ( _A, B, C, . . ._ ) = _A · F_ (1 _, B, C, . . ._ ) + _A_<sup>¯</sup> _· F_ (0 _, B, C, . . ._ ) (3) 

* **Gate Operators:** 

_Y_ NAND = _A · B, Y_ NOR = _A_ + _B, Y_ XOR = _A ⊕ B_ = _AB_<sup>¯</sup> + _AB_<sup>¯</sup> (4) 

### **3. Circuit Analysis Milestones** 

To analyze and simplify a combinational logic expression: 

1. **Extract Boolean Expression:** Trace the logic diagram from left to right, writing down the output expression of each individual logic gate. 

2. **De Morgan Expansion:** Apply De Morgan’s laws to break down large overbars covering multiple terms. 

2 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

3. **Boolean Minimization:** Apply Boolean identity theorems (such as complementarity, absorption, or consensus) to systematically reduce the number of literal terms. 

4. **Karnaugh Map (K-Map) Optimization:** For functions of 2 to 4 variables, map the expression to a K-Map using Gray-code order. Group adjacent cells in powers of 2 (1s for Sum-of-Products, 0s for Product-of-Sums) to find the minimum literal expression. 

### **4. Problem-Solving Algorithm** 

#### **Boolean Minimization and Gate Count Determination** 

1. **Construct the Truth Table:** If the physical operation is described in text, construct a truth table listing all 2<sup>_n_</sup> input combinations and the corresponding desired outputs. 

2. **Map to a K-Map:** Fill the 1s into the Gray-coded K-map grids. 

3. **Group the Cells:** Identify the largest possible groups of adjacent 1s (octets, quads, pairs) using wrap-around rules. Grouping must prioritize larger cells to eliminate the maximum number of variables. 

4. **Extract Minimal Literals:** Write the minimized Sum-of-Products (SOP) expression. 

5. **Determine Gate Costs:** Draw the resulting minimal circuit. If implementing exclusively using NAND gates, apply double-complements and expand using De Morgan to convert all OR/AND operators into NAND form. 

### **5. Truth Tables & Characteristics** 

Standard truth tables for primary two-input gates: 

|**Input **|**A**|**Input **|**B**|**AND**|**OR**|**NAND**|**NOR**|**XOR**|
|---|---|---|---|---|---|---|---|---|
|0||0||0|0|1|1|0|
|0||1||0|1|1|0|1|
|1||0||0|1|1|0|1|
|1||1||1|1|0|0|0|



### **6. Crucial Pitfalls** 

#### **Boolean Algebra and Gate Reduction Traps** 

-  **The Distributive Law Misconception:** Forgetting that the distributive law also applies in reverse for addition over multiplication, i.e., _A_ + _AB_<sup>¯</sup> = _A_ + _B_ . Students often make the mistake of leaving the _A_<sup>¯</sup> term unsimplified. 

-  **Improper K-Map Grouping:** Grouping cells in non-binary counts (such as grouping 3 or 6 cells together) or failing to utilize the wrap-around boundary rules (which can group corners or opposite edges together). 

3 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

### **7. Standard Textbook Systems** 

-  **Universal NAND Realization of XOR:** The implementation of a two-input XOR gate using exactly four two-input NAND gates, representing the absolute minimum universal gate count. 

-  **The 4-Variable Prime Implicant K-Map:** A classic benchmark problem featuring redundant minterms designed to test the application of the Consensus Theorem. 

4 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

## **2 Combinational Circuits: Multiplexers and Decoders** 

### **1. Core Theory** 

Combinational circuits are digital logic networks whose outputs at any instant are determined strictly by the current state of their inputs, containing no internal feedback loops or memory elements. * **Multiplexer (MUX):** A data selector that routes digital information from one of several input lines to a single common output line, controlled by a set of select lines. * **Decoder:** A multi-input, multi-output device that converts a coded binary input of _n_ bits into one of 2<sup>_n_</sup> unique active-low or active-high output lines, effectively ”decoding” the binary address. 

### **2. Mathematical Framework & Transfer Functions** 

* **Multiplexer Transfer Function (** 2<sup>_n_</sup> **-to-1 MUX):** For a 4-to-1 MUX with inputs _I_ 0 _, I_ 1 _, I_ 2 _, I_ 3 and select lines _S_ 1 _, S_ 0: 



<!-- Start of picture text -->
Y = S ¯ 1 S ¯ 0 I 0 + S ¯ 1 S 0 I 1 +  S 1 S ¯ 0 I 2 +  S 1 S 0 I 3 (5)<br><!-- End of picture text -->

where the select lines act as a binary decoder for the input subscripts. * **Decoder Transfer Function (2-to-4 Decoder):** Given inputs _A, B_ and active-high outputs _Y_ 0 _, Y_ 1 _, Y_ 2 _, Y_ 3: 



<!-- Start of picture text -->
Y 0 = A ¯ B, ¯ Y 1 = AB, ¯ Y 2 =  AB, ¯ Y 3 =  AB (6)<br><!-- End of picture text -->

If an Enable ( _EN_ ) line is present, all outputs are multiplied by _EN_ : e.g., _Yi_ = minterm _i · EN_ . 

### **3. Circuit Analysis Milestones** 

To analyze combinational systems or implement Boolean equations using multiplexers: 

1. **Extract Select Path:** Identify the variables connected to the MUX select inputs ( _Sn−_ 1 _, . . . , S_ 0). These variables partition the Boolean truth table. 

2. **Formulate Sub-functions:** For each combination of the select variables, determine the required MUX input _Ij_ in terms of the remaining, unselected variables. 

3. **Connect constants or literals:** Connect the input lines _Ij_ to either 0, 1, or the literal/complement of the remaining variable. 

4. **Boolean Sum-of-Products via Decoders:** Since a decoder generates all 2<sup>_n_</sup> individual minterms of _n_ variables, any arbitrary Boolean function can be implemented by simply connecting an OR gate to the corresponding minterm outputs. 

5 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

### **4. Problem-Solving Algorithm** 

**Implementing an** _n_ **-Variable Boolean Function using an** ( _n −_ 1) **-Select Line Multiplexer** 

1. **Select** ( _n −_ 1) **variables:** Assign ( _n −_ 1) variables of the given _n_ -variable Boolean function to the select lines of the MUX (typically the most significant bits). 

2. **Isolate the Remaining Variable:** Let the unselected variable be _Z_ . Write down the truth table of the function, grouped in pairs of rows representing each select combination. 

3. **Examine Output Behavior for Each Select Pair:** 

   -  If the output is 0 for both rows, connect the corresponding MUX input to 0. 

   -  If the output is 1 for both rows, connect the corresponding MUX input to 1. 

   -  If the output matches _Z_ in both rows, connect the corresponding MUX input to _Z_ . 

   -  If the output matches _Z_<sup>¯</sup> in both rows, connect the corresponding MUX input to _Z_ ¯. 

4. **Construct Circuit:** Wire the constants and literals to the MUX data pins. 

### **5. Truth Tables & Characteristics** 

Truth table of a 4-to-1 Multiplexer showing data routing: 

|**Select line**|_S_1<br>**Select line** _S_0|**Output Y**|
|---|---|---|
|0|0|_I_0|
|0|1|_I_1|
|1|0|_I_2|
|1|1|_I_3|



### **6. Crucial Pitfalls** 

#### **Combinational Routing Traps** 

-  **The MUX Select Pin Order Swap:** Reversing the connection of select variables to the MUX select pins. If _S_ 1 is the MSB and _S_ 0 is the LSB, connecting the LSB variable to _S_ 1 completely scrambles the output routing and invalidates the Boolean transfer function. 

-  **Active-Low Decoder Misconception:** Forgetting that many standard TTL decoders (like the 74LS138) have active-low outputs. To implement a Sum-of-Products function using an active-low decoder, you must connect the outputs to a **NAND** gate, not an OR gate. 

6 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

### **7. Standard Textbook Systems** 

-  **The Full Adder implemented via 8-to-1 MUX:** A standard configuration where the inputs _A, B, C_ in are connected directly to the select lines, and the MUX data inputs are wired to high/low constants to generate the Sum and Carry outputs. 

-  **Cascaded Multiplexer Trees:** Connecting three 2-to-1 MUXes to synthesize a single 4-to-1 MUX, demonstrating hierarchical combinational logic. 

7 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

## **3 Sequential Circuits: SR, JK, D, and T Flip-Flops** 

### **1. Core Theory** 

Sequential circuits are digital networks whose outputs depend not only on the current inputs but also on the history of previous inputs, requiring the presence of internal memory elements. * **Latch:** An active-high or active-low asynchronous memory element that is level-sensitive. * **Flip-Flop:** A synchronous memory element that updates its state strictly at the rising or falling transition of an external clock signal (edge-triggered). * **SR Flip-Flop (Set-Reset):** The basic memory cell. Sets the state to 1 when _S_ = 1, and resets to 0 when _R_ = 1. The state is undefined if both inputs are asserted simultaneously ( _S_ = _R_ = 1). * **JK Flip-Flop:** A universal flip-flop that resolves the undefined SR state by **toggling** the output state when _J_ = _K_ = 1. * **D Flip-Flop (Data/Delay):** Acts as a single-bit delay cell, transferring the input _D_ directly to the output on the active clock edge ( _Qn_ +1 = _D_ ). * **T Flip-Flop (Toggle):** Toggles the state of the output if _T_ = 1 on the active clock edge; preserves the state if _T_ = 0. 

### **2. Mathematical Framework & Transfer Functions** 

The dynamic behavior of flip-flops is governed by their **Characteristic Equations**, which define the next state ( _Qn_ +1) in terms of the current inputs and the present state ( _Qn_ ): * **SR Flip-Flop:** 

|_Qn_+1 =_S_+ <sup>¯</sup>_RQn_|(subject to the constraint: _S · R_= 0)<br>(7)|
|---|---|



|* **JK Flip-Flop:**||
|---|---|
|_Qn_+1 =_J_ <sup>¯</sup>_Qn_+ <sup>¯</sup>_KQn_|(8)|
|* **D Flip-Flop:**||
|_Qn_+1 =_D_|(9)|
|* **T Flip-Flop:**||
|_Qn_+1 =_T ⊕Qn_ =_T_ <sup>¯</sup>_Qn_+ <sup>¯</sup>_TQn_|(10)|



### **3. Circuit Analysis Milestones** 

To find the next state or analyze a sequential network: 

1. **Write Input Equations:** Express the excitation inputs of each flip-flop ( _Di_ , _Ti_ , or _Ji, Ki_ ) as Boolean functions of the current state of the system ( _Qn_ ). 

2. **Substitute into Characteristic Equations:** Substitute these input equations directly into the respective flip-flop characteristic equations. 

3. **Evaluate the Next State:** Compute _Qn_ +1 for each possible combination of current states to construct the transition matrix. 

4. **Draw the State Diagram:** Map the transition matrix to a state transition graph showing nodes, inputs, and outputs. 

8 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

### **4. Problem-Solving Algorithm** 

#### **Converting Between Different Flip-Flop Types (Excitation Mapping)** 

1. **Construct the Target State Table:** Write down the transition columns showing Present State ( _Qn_ ), Next State ( _Qn_ +1), and the Target Input (e.g., _T_ ). 

2. **Map the Source Excitation Requirements:** Using the **Excitation Table** of the source flip-flop (the one you are converting *from*, e.g., JK), determine the required source inputs ( _J, K_ ) needed to force each _Qn → Qn_ +1 transition. 

3. **Formulate Excitation Equations:** Express the source inputs ( _J, K_ ) as Boolean functions of the target input ( _T_ ) and present state ( _Qn_ ) using a K-map. 

4. **Draw the Conversion Circuit:** Connect the calculated combinational logic to the pins of the source flip-flop. 

### **5. Truth Tables & Characteristics** 

Excitation Tables listing the inputs required to force a specific state transition ( _Qn → Qn_ +1): 

|**Transition** _Qn →Qn_+1|**SR Required**|**JK Required**|**D Required**|**T Required**|
|---|---|---|---|---|
|0_→_0|0_X_|0_X_|0|0|
|0_→_1|10|1_X_|1|1|
|1_→_0|01|_X_1|0|1|
|1_→_1|_X_0|_X_0|1|0|



*Note: _X_ represents a ”Don’t Care” state (either 0 or 1).* 

### **6. Crucial Pitfalls** 

#### **Sequential Logic and Excitation Traps** 

-  **The JK Race-Around Condition:** In level-triggered JK flip-flops, if _J_ = _K_ = 1 and the clock pulse width _tp_ is wider than the propagation delay of the flip-flop ( _tpd_ ), the output will toggle repeatedly within a single clock pulse, leaving the final output state completely unpredictable. This is prevented by using **edge-triggered** flip-flops or **master-slave** configurations. 

-  **SR Constraint Violation:** Designing a circuit that allows _S_ = _R_ = 1 to occur, which bypasses the feedback safety, leaving the output in an unstable, race-dependent state when the inputs are de-asserted. 

### **7. Standard Textbook Systems** 

-  **Master-Slave JK Flip-Flop:** Cascades two gated latches driven by complementary clocks to eliminate the level-triggered race-around condition, updating the output strictly on the clock edge. 

-  **The D-to-T Conversion:** Implementing a T flip-flop by feeding back the output of a D flip-flop through an XOR gate: _D_ = _T ⊕ Q_ . 

9 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

## **4 Counters and Shift Registers** 

### **1. Core Theory** 

* **Shift Register:** A cascaded chain of flip-flops configured to shift binary data from one stage to the next on each clock transition. They are used for serial-parallel data conversion (SISO, SIPO, PISO, PIPO) and temporary storage. * **Counters:** Cyclic sequential circuits that transition through a predetermined sequence of states on each clock pulse. * **Asynchronous (Ripple) Counter:** The clock input is connected only to the first flip-flop stage. Each subsequent stage is clocked by the output of the preceding stage. Because the clock signal ”ripples” through the chain, propagation delays accumulate, limiting the maximum operating frequency. * **Synchronous Counter:** All flip-flop stages share the same common clock signal, triggering simultaneously. This eliminates ripple delays, allowing for much higher operating speeds. 

### **2. Mathematical Framework & Transfer Functions** 

* **Modulus of a Counter (Mod-N):** The total number of unique states in the counter’s cycle. For _n_ flip-flops, the maximum modulus is _N_ max = 2<sup>_n_</sup> . * **Maximum Asynchronous Propagation Delay limit:** To ensure correct counting, the clock period _T_ clk must be greater than the total accumulated ripple delay: 



<!-- Start of picture text -->
1<br>T clk ≥ n · tpd = ⇒ f max = (11)<br>n · tpd<br><!-- End of picture text -->

where _n_ is the number of stages and _tpd_ is the propagation delay of a single flip-flop. * **Ring Counter (Mod-n Shift Register):** Connects the output of the last shift stage back to the first stage. Modulus is _N_ = _n_ . * **Johnson Counter (Twisted-Ring, Mod-2n):** Connects the inverted output of the last stage ( _Q_<sup>¯</sup> ) back to the first stage. Modulus is _N_ = 2 _n_ . 

### **3. Circuit Analysis Milestones** 

To analyze or design a synchronous counter: 

1. **Set up the State Table:** Write columns for Present State ( _Qn_ ), Next State ( _Qn_ +1), and the required flip-flop excitation inputs. 

2. **Determine Next States:** Write down the desired state transitions (e.g., 000 _→_ 001 _→_ 010 _. . ._ ). 

3. **Map Excitation Inputs:** Use the flip-flop excitation tables to fill the input columns (such as _Jk, Kk_ or _Tk_ ) required to force the transitions. 

4. **Minimize and Implement:** Use K-maps to minimize the excitation inputs as functions of the present states, and implement the combinational logic. 

10 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

### **4. Problem-Solving Algorithm** 

#### **Analyzing the Counting Sequence of a Synchronous Counter** 

1. **Write Down Input Equations:** Note the Boolean expressions for the excitation inputs of each flip-flop (e.g., _J_ 0 = 1 _, K_ 0 = 1 _, J_ 1 = _Q_ 0 _, K_ 1 = _Q_ 0). 

2. **Tabulate State Transitions:** Create a table with columns for the current state ( _Q_ 2 _Q_ 1 _Q_ 0), the excitation inputs ( _J_ 2 _K_ 2 _J_ 1 _K_ 1 _J_ 0 _K_ 0), and the resulting next state ( _Q_<sup>+</sup> 2<sup>_Q_</sup> 1<sup>+</sup><sup>_Q_+</sup> 0<sup>).</sup> 

3. **Apply the Characteristic Equations:** For each row, substitute the input values into the flip-flop’s next-state equation to calculate _Q_<sup>+</sup> _k_<sup>.</sup> 

4. **Construct the State Cycle:** Trace the transition sequence starting from 000. Continue until the sequence repeats to find the **Modulus** and identify any **unused or self-starting states**. 

### **5. Truth Tables & Characteristics** 

Counting sequence and states of a 3-bit binary asynchronous up-counter: 

|**Clock Pulse**|**Output** _Q_2|**Output** _Q_1|**Output** _Q_0|
|---|---|---|---|
|0|0|0|0|
|1|0|0|1|
|2|0|1|0|
|3|0|1|1|
|4|1|0|0|
|5|1|0|1|
|6|1|1|0|
|7|1|1|1|



### **6. Crucial Pitfalls** 

#### **Counter and Register Traps to Avoid** 

-  **The Ripple Glitch Hazard:** In asynchronous counters, the non-simultaneous transitions of flip-flops create transient intermediate states. For example, during the transition 011 _→_ 100, the state may temporarily read 010 or 000 for a few nanoseconds. If these outputs are connected to combinational decoding gates, it can trigger **glitches** and false outputs. 

-  **Lock-out in Synchronous Counters:** If the counter enters an unused state (e.g., if a Mod-5 counter enters state 6 or 7 due to noise), the excitation logic may trap the counter in a closed loop of unused states. Always verify that unused states are **self-starting**, i.e., they eventually lead back into the main count cycle. 

11 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

### **7. Standard Textbook Systems** 

-  **The Asynchronous Mod-10 (BCD) Counter:** A 4-bit ripple counter that uses a NAND gate feedback loop connected to the clear ( _CLR_ ) pins to reset the counter back to 0000 when the state hits 1010 (decimal 10). 

-  **The 4-Bit Johnson Counter:** Uses four D-flip-flops in a twisted ring, tracing an 8-state cyclic code (0000 _→_ 1000 _→_ 1100 _→_ 1110 _→_ 1111 _→_ 0111 _→_ 0011 _→_ 0001 _→_ 0000). 

12 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

## **5 The 555 Timer** 

### **1. Core Theory** 

The **555 Timer** is an extremely versatile mixed-signal integrated circuit capable of generating precise timing delays or continuous oscillations. * **Internal Structure:** It consists of: 1. A resistive voltage divider of three identical 5 kΩresistors that establishes reference voltages at _VCC/_ 3 and 2 _VCC/_ 3. 2. Two analog voltage comparators: the Threshold Comparator and the Trigger Comparator. 3. An SR latch that stores the output state. 4. An internal discharge transistor ( _Q_ dis) that provides a path to ground to discharge an external capacitor. * **Astable Multivibrator (Freerunning):** The circuit oscillates continuously between two unstable states, generating a periodic square-wave output. * **Monostable Multivibrator (One-shot):** The circuit remains in a stable state until a negative trigger pulse is applied. It then generates a single output pulse of a fixed duration before returning to its stable state. 

### **2. Mathematical Framework & Transfer Functions** 

* **Reference Voltages:** 



<!-- Start of picture text -->
V upper = 2 V lower = 1 (12)<br>3 VCC, 3 VCC<br><!-- End of picture text -->

* **Astable Multivibrator Time Parameters:** Let _RA_ be connected between _VCC_ and Pin 7 (Discharge), _RB_ between Pin 7 and Pin 6 (Threshold), and capacitor _C_ from Pin 6 to Ground. * **Charging Time (High Output,** _T_ **high):** Capacitor charges from _VCC/_ 3 to 2 _VCC/_ 3 through _RA_ + _RB_ : 



<!-- Start of picture text -->
T high = ln(2)( RA  +  RB ) C ≈ 0 . 693( RA  +  RB ) C (13)<br><!-- End of picture text -->

* **Discharging Time (Low Output,** _T_ **low):** Capacitor discharges from 2 _VCC/_ 3 to _VCC/_ 3 through _RB_ to the internal discharge transistor: 

_T_ low = ln(2) _RBC ≈_ 0 _._ 693 _RBC_ (14) 

* **Total Period (** _T_ **) and Frequency (** _f_ **):** 



<!-- Start of picture text -->
1 . 44<br>T =  T high +  T low = 0 . 693( RA  + 2 RB ) C = ⇒ f = (15)<br>( RA  + 2 RB ) C<br><!-- End of picture text -->

* **Duty Cycle (** _D_ **):** 



<!-- Start of picture text -->
D = T high = RA  +  RB (always >  50%) (16)<br>T RA  + 2 RB<br><!-- End of picture text -->

* **Monostable Multivibrator Pulse Width (** _W_ **):** 



<!-- Start of picture text -->
W = ln(3) RAC ≈ 1 . 1 RAC (17)<br><!-- End of picture text -->

### **3. Circuit Analysis Milestones** 

The internal operation of the 555 timer is analyzed in these steps: 

1. **Verify Comparator Inputs:** Compare the external capacitor voltage _VC_ to the reference thresholds: 

13 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

   -  If _VC >_ 2 _VCC/_ 3, the upper comparator sets the SR latch, forcing the output Low and turning ON the discharge transistor. 

   -  If _VC < VCC/_ 3, the lower comparator resets the SR latch, forcing the output High and turning OFF the discharge transistor. 

2. **Formulate Capacitor Charging Equation:** Solve the first-order RC transient charging equation: 



<!-- Start of picture text -->
vC ( t ) =  V final + [ V initial  − V final] e −t/τ (18)<br><!-- End of picture text -->

3. **Evaluate the Time Intervals:** Substitute the boundary conditions ( _V_ initial = _VCC/_ 3 and _V_ final = _VCC_ ) to find the charging time, and ( _V_ initial = 2 _VCC/_ 3 and _V_ final = 0) to find the discharging time. 

### **4. Problem-Solving Algorithm** 

#### **Designing a 555 Astable Multivibrator for a Given Frequency and Duty Cycle** 

1. **Note Design Specifications:** Target frequency _f_ , desired duty cycle _D_ , and select a standard value for capacitor _C_ (typically 0 _._ 1 _µ_ F or 0 _._ 01 _µ_ F). 

2. **Calculate the Total Period (** _T_ **):** _T_ = 1 _/f_ . 

3. **Solve for the Resistor Sum and Individual Values:** 



<!-- Start of picture text -->
RA  + 2 RB = 1 . 44 (19)<br>f · C<br>the duty cycle relation:<br>D = RA  +  RB = ⇒ RA =  RB (20)<br>RA  + 2 RB � 21 D − −D 1 �<br><!-- End of picture text -->

Using the duty cycle relation: 

4. **Substitute and Solve:** Find the standard resistor values for _RA_ and _RB_ . 

### **5. Truth Tables & Characteristics** 

Internal latch logic of the 555 Timer based on comparator inputs: 

|**Threshold (Pin 6)**|**Trigger (Pin 2)**|**Latch State**|**Output (Pin 3)**|**Discharge (Pin 7)**|
|---|---|---|---|---|
|_<_2_VCC/_3|_> VCC/_3|No Change|Hold Present|Hold State|
|_<_2_VCC/_3|_< VCC/_3|Reset|High (1)|Open (OFF)|
|_>_2_VCC/_3|_> VCC/_3|Set|Low (0)|Closed (ON)|



14 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

### **6. Crucial Pitfalls** 

#### **555 Timer Calculation and Layout Traps** 

-  **The 50% Duty Cycle Limit Trap:** Attempting to design a standard astable multivibrator with a duty cycle less than or equal to 50%. Since _T_ high _∝_ ( _RA_ + _RB_ ) and _T_ low _∝ RB_ , the charging path must always contain _RA >_ 0, making _T_ high _> T_ low and _D >_ 50%. To achieve a duty cycle _≤_ 50%, you must bypass _RB_ during charging by placing a diode in parallel with _RB_ . 

-  **Confusing the Astable and Monostable constants:** Using the factor of 0 _._ 693 for a monostable multivibrator, or 1 _._ 1 for an astable multivibrator. 

### **7. Standard Textbook Systems** 

-  **The Standard Astable Square-Wave Generator:** A self-running oscillator providing clock pulses to sequential circuits. 

-  **The Astable with Diode-Steering (50% duty cycle):** An astable circuit containing a steering diode across _RB_ to separate the charging and discharging paths, allowing for symmetric square waves ( _D_ = 50%). 

15 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

## **6 Principles of A/D and D/A Conversion** 

### **1. Core Theory** 

Mixed-signal conversion forms the interface between the physical analog world and digital processing systems. * **D/A Converter (DAC):** Reconstructs an analog output voltage _V_ out from an _n_ -bit digital binary word ( _D_ = _dn−_ 1 _dn−_ 2 _. . . d_ 0). * **Weighted-Resistor DAC:** Uses a set of binaryweighted resistors connected to an op-amp summing junction. * **R-2R Ladder DAC:** Resolves the practical limitations of the weighted-resistor design by utilizing only two resistor values ( _R_ and 2 _R_ ) arranged in a ladder network. * **A/D Converter (ADC):** Converts a continuous analog input voltage _V_ in into an _n_ -bit digital code. * **Flash (Simultaneous) ADC:** High-speed parallel converter using a resistive divider and a bank of 2<sup>_n_</sup> _−_ 1 comparators. * **Successive Approximation Register (SAR) ADC:** A feedback system that systematically tests each bit of a DAC from MSB to LSB, converging on the digital equivalent within exactly _n_ clock cycles. 

### **2. Mathematical Framework & Transfer Functions** 

* **Digital-to-Analog Output voltage (Weighted Resistor):** 



<!-- Start of picture text -->
V out =  −V ref + dn− 2 +  · · ·  + d 0 (21)<br>� dn 2 − 1 1 2 2 2 n �<br><!-- End of picture text -->

* **Resolution of an n-bit Converter:** 



<!-- Start of picture text -->
Resolution = 2 Vn FSR − 1 = Step Size = LSB Weight (22)<br><!-- End of picture text -->

where _V_ FSR is the Full-Scale Range voltage. * **Flash ADC Comparator Count (** _Nc_ **):** 

_Nc_ = 2<sup>_n_</sup> _−_ 1 (23) 

* **A/D Quantization Error (** _V_ **QE):** 



<!-- Start of picture text -->
V FSR<br>V QE =  ± 1 (24)<br>2 LSB =  ± 2(2 n − 1)<br><!-- End of picture text -->

### **3. Circuit Analysis Milestones** 

* **R-2R Ladder Node Analysis:** The R-2R ladder is analyzed by applying Thevenin’s theorem at each node. Looking back into any node of the ladder toward the termination resistance reveals an equivalent resistance of exactly _R_ , dividing the node voltages by factors of 2. * **WeightedResistor Virtual Ground Superposition:** The feedback op-amp summing junction acts as a virtual ground, summing the binary-weighted currents: 



<!-- Start of picture text -->
n− 1<br>dkV ref<br>I total = � 2 n− 1 −k R (25)<br>k =0<br><!-- End of picture text -->

16 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

### **4. Problem-Solving Algorithm** 

#### **Calculating Resolution and Quantization Parameters of an ADC/DAC** 

1. **Identify Bit-Width (** _n_ **) and Full-Scale Voltage (** _V_ **FSR):** Note the given converter specifications. 

2. **Calculate Step Size / Resolution:** 



<!-- Start of picture text -->
Step Size = V FSR (or V FSR (26)<br>2 n 2 n − 1 )<br><!-- End of picture text -->

3. **Determine the Output for a Given Digital Word (** _D_ **):** Convert the binary word to its decimal equivalent _N_ dec =<sup>�</sup><sup>_n_</sup> _k_ =0<sup>_−_1</sup><sup>_dk_2</sup><sup>_k_.</sup> 

4. **Compute Analog Output:** 



<!-- Start of picture text -->
V out =  N dec  ×  Step Size (27)<br><!-- End of picture text -->

### **5. Characteristics** 

* **The Staircase Transfer Function:** A DAC output is not truly continuous; instead, it is a staircase-like step function. As the digital input increments, the analog output increases in discrete jumps equal to the resolution step size (1 LSB). * **Flash ADC Resolution Complexity Table:** 

|**Resolution **|**(Bits** _n_**)**<br>**Comparator Count (**2<sup>_n _</sup>_−_1**)**|**Resistor Divider Count (**2<sup>_n_</sup>**)**|
|---|---|---|
|4|15|16|
|6|63|64|
|8|255|256|
|10|1023|1024|



### **6. Crucial Pitfalls** 

#### **Data Converter Design Pitfalls** 

-  **The Resistor Precision Trap:** In weighted-resistor DACs, the resistors span a massive range from _R_ to 2<sup>_n−_1</sup> _R_ . For a 10-bit DAC, the ratio is 1 : 512. Fabricating highly precise, matched resistors over such a large range on a single silicon chip is virtually impossible, causing severe linearity errors. This is why the R-2R ladder is preferred, as it requires only two resistor values. 

-  **Conversion Time vs. Frequency Confusion:** Assuming a Flash ADC and a Successive Approximation ADC have identical conversion speeds. A Flash ADC converts in a single clock cycle (highest speed), whereas a Successive Approximation ADC requires exactly _n_ clock cycles, making it slower but much less complex. 

### **7. Standard Textbook Systems** 

-  **The 4-Bit R-2R Ladder DAC:** The prototypical impedance-isolated digital-to-analog converter using an op-amp output buffer. 

17 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

-  **The 3-Bit Flash ADC with Priority Encoder:** A high-speed analog-to-digital converter utilizing 7 parallel comparators and a priority encoder to output a 3-bit digital word. 

18 

GATE PHYSICS 

DIGITAL ELECTRONICS & SYSTEMS 

## **References** 

1. Floyd, Thomas L. _Digital Fundamentals_ . 11th Edition, Pearson, 2015. 

2. Morris Mano, M. _Digital Design_ . Prentice-Hall, 1995. 

3. Gayakwad, Ramakant A. _Op-Amps and Linear Integrated Circuits_ . Prentice-Hall. 

19 

