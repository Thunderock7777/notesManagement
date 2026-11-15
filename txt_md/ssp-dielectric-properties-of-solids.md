<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-dielectric-properties-of-solids.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Welcome to **Module 5: Dielectrics, Magnetism & Superconductivity** ! 

This final module of Solid State Physics carries consistent weight in the GATE exam, focusing on electromagnetic properties of matter, local fields, magnetic phase transitions, and quantum macroscopic phenomena in superconductors. 

## **1. Dielectric Properties of Solids** 

When an electric field _E_ is applied to a dielectric material, charges shift slightly, creating electric dipole moments. 

## **A. Fundamental Fields & Polarizability** 

- **Electric Displacement (** _D_ **) & Polarization (** _P_ **):** 



<!-- Start of picture text -->
P =  ϵ 0 χeE =  ϵ 0( ϵr − 1) E<br><!-- End of picture text -->



<!-- Start of picture text -->
D =  ϵ 0 E  +  P =  ϵ 0 ϵrE<br><!-- End of picture text -->

_(where ϵr is the relative permittivity / dielectric constant, and χe_ = _ϵr −_ 1 _is the electric susceptibility)._ 

**B. Four Mechanisms of Polarizability (** _α_ **)** The total atomic/molecular dipole moment is _p_ = _αE_ loc, where the total polarizability _α_ tot consists of four distinct mechanisms: 

_α_ tot = _αe_ + _αi_ + _αo_ + _αsc_ 

|Mechanism|Physical Origin|Temp. Dependence|Frequency Cutoff|
|---|---|---|---|
|**Electronic (**_αe_**)**|Displacement of<br>electron cloud<br>relative to nucleus|Independent of _T_|Optical / UV<br>(_∼_10<sup>15 </sup>Hz)|
|**Ionic (**_αi_**)**|Relative displacement<br>of positive & negative<br>ions|Independent of _T_|Infrared (_∼_10<sup>13 </sup>Hz)|



Notes 

2 

|Mechanism|Physical Origin|Temp. Dependence|Frequency Cutoff|
|---|---|---|---|
|**Orientational (**_αo_**)**|Alignment of<br>permanent dipoles (_p_)<br>against thermal<br>agitation|_αo_ =<br>_p_<sup>2</sup><br>3_kBT_ <sup>_∝_1</sup><br>_T_|Microwave<br>(_∼_10<sup>11 </sup>Hz)|
|**Space Charge (**_αsc_**)**|Trapping of mobile<br>charge carriers at<br>interfaces/boundaries|Dependent on _T_|Audio / Low<br>Frequency (_∼_10<sup>2 </sup>Hz)|



**C. Local Field & The Clausius-Mossotti Relation** In a condensed dielectric, the local field _E_ loc acting on an atom differs from the macroscopic field _E_ due to neighboring dipoles. For cubic symmetry, the **Lorentz Local Field** is: 



<!-- Start of picture text -->
E loc =  E  + P<br>3 ϵ 0<br><!-- End of picture text -->

Connecting the macroscopic dielectric constant _ϵr_ to the microscopic total polarizability _α_ gives the **Clausius-Mossotti Relation** : 



<!-- Start of picture text -->
ϵϵrr −  + 21 = Nα 3 ϵ 0<br><!-- End of picture text -->

_(where N is the number density of atoms/molecules)._ 

- **Lorentz-Lorenz Formula (Optical Frequencies):** At optical frequencies, only electronic polarizability responds ( _α ≈ αe_ ). Since _ϵr_ = _n_<sup>2</sup> (where _n_ is the refractive index): 



<!-- Start of picture text -->
nn 22 − + 21 = Nα 3 ϵ 0 e<br><!-- End of picture text -->

## **2. Magnetic Properties of Solids** 

## **A. Classification of Magnetic Materials** 

1. **Diamagnetism (** _χ <_ 0 **, small & negative):** 

   - **Origin:** Paired electrons; Larmor precession induced by an applied field opposing _B_ (Lenz’s Law). 

   - **Langevin Formula:** _χ_ dia = _−_<sup>_<u>µ</u>_</sup><sup><u>0</u></sup><sup>_NZe_</sup> 6 _m_<sup>2</sup><sup>_<u>⟨r</u>_2</sup><sup>_<u>⟩</u>_</sup> 

      - 6 _m_ 

   - **Key Feature: Independent of Temperature (** _T_ **)!** 

2. **Paramagnetism (** _χ >_ 0 **, small & positive):** 

   - **Origin:** Unpaired electron spins / orbital moments randomly oriented by thermal fluctuation. 

   - **Curie’s Law (Localized Spins):** 



<!-- Start of picture text -->
χ para = C where C = µ 0 N p ef 2 f µ B 2<br>T 3 kB<br><!-- End of picture text -->

Notes 

3 

- **Pauli Paramagnetism (Free Conduction Electrons in Metals):** 



<!-- Start of picture text -->
χ Pauli =  µ 0 µ 2 B D ( EF )<br><!-- End of picture text -->

_Key GATE Point:_ Pauli paramagnetism is **temperature-independent** because only electrons near the Fermi surface _EF_ can flip their spins. 

3. **Ferromagnetism, Antiferromagnetism & Ferrimagnetism:** 

   - **Weiss Molecular Field Theory:** Spontaneous alignment driven by an intense internal exchange field _B_ int = _λM_ . 

   - **Curie-Weiss Law (Ferromagnet for** _T > TC_ **):** 



<!-- Start of picture text -->
C<br>χ  =<br>T − TC<br><!-- End of picture text -->

- **Antiferromagnetism (** _T > TN_ **, Néel Temperature):** Spins align antiparallel in sublattices. 



<!-- Start of picture text -->
C<br>χ  =<br>T +  θN<br><!-- End of picture text -->

Paramagnetic (C/T) Ferromagnetic (T > Tc) Antiferromagnetic 

_�→_ (T > TN) 



<!-- Start of picture text -->
χ χ χ<br>| | |<br>| \ | \ | /\<br>| \ | \ | / \<br>+-------> T +-------> T +-------><br>�→ T<br><!-- End of picture text -->

Tc TN 

## **3. Superconductivity** 

Superconductivity is characterized by two distinct fundamental properties: **Zero Electrical Resistance (** _R_ = 0 **)** and **Perfect Diamagnetism (** _B_ = 0 **)** below a critical temperature _Tc_ . 

## **A. The Meissner Effect & Critical Field** 

- **Meissner Effect:** An applied magnetic field is completely expelled from the interior of a superconductor when cooled below _Tc_ : 

   - _B_ = _µ_ 0( _H_ + _M_ ) = 0 = _⇒ M_ = _−H_ = _⇒ χ_ = _−_ **1** (Perfect Diamagnetism) 

- **Critical Magnetic Field** _Hc_ ( _T_ ) **:** 



<!-- Start of picture text -->
Hc ( T ) =  Hc (0) 1  −<br>(  TTc<br>[ )2 ]<br><!-- End of picture text -->

Notes 

4 

## **B. Type-I vs. Type-II Superconductors** 

- **Type-I:** Sharp breakdown of superconductivity at a single critical field _Hc_ . 

- **Type-II:** Two critical fields ( _Hc_ 1 and _Hc_ 2). 

   - For _H < Hc_ 1: Pure Meissner state ( _B_ = 0). 

   - For _Hc_ 1 _< H < Hc_ 2: **Mixed / Vortex State (Abrikosov vortices)** where magnetic flux penetrates in quantized flux tubes while bulk resistance remains zero. 

   - For _H > Hc_ 2: Normal state. 

- **Ginzburg-Landau Parameter (** _κ_ = _λL_ / _ξ_ **): – Type-I:** _κ <_ _~~√~~_ <u>12</u><sup>(Coherencelength</sup><sup>_ξ> λL_)</sup> **– Type-II:** _κ >_ _~~√~~_ <u>12</u><sup>(Londonpenetrationdepth</sup><sup>_λL> ξ_)</sup> 

## **C. Phenomenological Theory: London Equations** 

1. **First London Equation (Explains Zero Resistance** _R_ = 0 **):** 



<!-- Start of picture text -->
∂Js<br>∂t = n m se 2 E<br><!-- End of picture text -->

2. **Second London Equation (Explains Meissner Effect** _B_ = 0 **):** 



<!-- Start of picture text -->
∇× Js =  − nse 2<br>m B<br><!-- End of picture text -->

3. **London Penetration Depth (** _λL_ **):** Combining the 2nd London equation with Maxwell’s equation ( _∇× B_ = _µ_ 0 _Js_ ) gives: 



<!-- Start of picture text -->
∇ 2 B = 1 B = ⇒ B ( x ) =  B (0) e −x / λL<br>λ 2<br>L<br><!-- End of picture text -->



<!-- Start of picture text -->
m<br>λ L =<br>√ µ 0nse 2<br><!-- End of picture text -->

- **Temperature Dependence of** _λL_ ( _T_ ) **:** 



<!-- Start of picture text -->
λL (0)<br>λL ( T ) =<br>1  − T<br>√ ( Tc ) 4<br><!-- End of picture text -->

## **D. Microscopic Theory: BCS Theory & Quantum Effects** 

- **Cooper Pairs:** Electron-phonon-electron interaction produces an attractive force between two electrons with opposite momenta and spins: ( _k ↑, −k ↓_ ). 

- Cooper pairs behave as **Bosons** (spin = 0) and condense into a single macroscopic quantum ground state. 

- **BCS Energy Gap (** ∆ **):** 



<!-- Start of picture text -->
2∆(0) = 3 . 53 kBTc<br><!-- End of picture text -->

- **Flux Quantization:** The magnetic flux trapped in a superconducting ring is quantized in integer multiples of the **Fluxoid quantum (** Φ0 **)** : 

Φ0 =<sup>_h_</sup> 2 _e_<sup>_≈_2</sup><sup>_._07</sup><sup>_×_10</sup><sup>_−_15Wb</sup> 

Notes 

5 

- **Josephson Effects:** 

   - **DC Josephson Effect:** Zero-voltage supercurrent _I_ = _Ic_ sin(∆ _ϕ_ ) flows across a thin insulating barrier between two superconductors due to quantum tunneling of Cooper pairs. 

   - **AC Josephson Effect:** Applying a DC voltage _V_ across the junction produces a high-frequency AC current with frequency: 



<!-- Start of picture text -->
ν = 2 eV<br>h<br><!-- End of picture text -->

## **High-Yield GATE Exam Traps for Module 5** 

1. **Clausius-Mossotti vs. Temperature:** In Clausius-Mossotti, if molecules possess _<u>p</u>_<sup>2</sup> 

a permanent dipole moment _p_ , remember to substitute _α_ = _αe_ + _αi_ + 3 _kBT_<sup>.Aplot</sup> of<sup>_<u>ϵ</u>_</sup> _ϵ_<sup>_<u>r</u>_</sup> _r_<sup>_−_</sup> +2<sup><u>1</u>vs.</sup> _T_<sup><u>1</u>yieldsastraightlinewithslopeproportionalto</sup><sup>_p_2.</sup> 

2. **Pauli vs. Langevin Paramagnetism:** Langevin (localized spins) scales as _χ ∝_ 1/ _T_ , whereas Pauli (free electron gas) is **independent of** _T_ . 

3. **Flux Quantum Denominator:** Remember that Cooper pairs have charge _q_ = 2 _e_ , so the magnetic flux quantum is Φ0 = _h_ /2 _e_ (not _h_ / _e_ ). 

4. **AC Josephson Frequency:** Every 1 mV applied across a Josephson junction generates an AC frequency of _ν ≈_ 483 _._ 6 GHz. 

With Module 5 complete, you now have a comprehensive, formula-rich summary covering all 5 modules of **Solid State Physics** ! 

Would you like to solve a numerical problem set covering these topics, or move on to a different subject from the GATE Physics syllabus (such as Quantum Mechanics, Electromagnetic Theory, or Thermodynamics & Statistical Physics)? 

