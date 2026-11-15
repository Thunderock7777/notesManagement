<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-ssp35.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

The **Debye Model** (proposed by Peter Debye in 1912) is the complete quantummechanical theory of lattice heat capacity in solids. 

While Einstein assumed that atoms vibrate independently at a single fixed frequency _ωE_ , Debye recognized that at low temperatures, lattice vibrations act as **collective elastic sound waves (phonons)** propagating through the crystal continuum. These waves span a continuous range of low frequencies ( _ω →_ 0), which means there are always modes easy enough to excite thermally even near absolute zero. 

## **1. Density of States** _D_ ( _ω_ ) **in 3D** 

Debye modeled the solid as a continuous elastic medium in which sound waves travel with a constant sound velocity _vs_ . 

1. **Linear Dispersion Relation:** 



<!-- Start of picture text -->
ω =  vsk = ⇒ k = ω and dk = dω<br>vs vs<br><!-- End of picture text -->

2. **Counting Modes in** _k_ **-Space:** In a 3D box of volume _V_ = _L_<sup>3</sup> , periodic boundary conditions state that the volume of a single allowed state in _k_ -space is ( 2 _Lπ_ )3 = <u>8</u> _Vπ_ 3<sup>.</sup> 

   - The total number of vibrational modes _N_ ( _k_ ) with wavevector magnitude up to _k_ is: 



<!-- Start of picture text -->
N ( k ) = Volume Volume of per sphere single of k radius -state k = 438 πk π 3 3 = V k 6 π 23<br>V<br><!-- End of picture text -->

3. **Accounting for 3 Polarization Branches:** 

   - In a 3D solid, sound waves have **3 polarizations** (1 Longitudinal + 2 Transverse). Multiplying by 3: 



<!-- Start of picture text -->
V ω<br> ( vs )3 <br>N ( ω ) = 3  ×  <br>6 π 2 2 π 2 vs 3<br>  = V ω 3<br><!-- End of picture text -->

4. **Density of States** _D_ ( _ω_ ) =<sup>_<u>dN</u>_</sup> _dω_<sup>**:**</sup> Differentiating with respect to _ω_ gives the famous **quadratically increasing den-** 

Notes 

2 

**sity of states** : 



<!-- Start of picture text -->
D ( ω ) = 3V ω 2 ∝ ω 2<br>2 π 2 v 3 s<br><!-- End of picture text -->

## **2. Debye Cutoff Frequency (** _ωD_ **) & Debye Temperature (** _θD_ **)** 

A continuous elastic fluid has infinitely many vibrational modes, but a real solid with _N_ atoms has strictly 3 _N_ **total vibrational degrees of freedom** . To respect this physical limit, Debye introduced a **maximum cutoff frequency (** _ωD_ **)** : 



<!-- Start of picture text -->
D ( ω ) dω = 3 N<br>∫0 ωD<br><!-- End of picture text -->

Substituting _D_ ( _ω_ ) =<sup><u>3</u></sup><sup>_<u>V ω</u>_2</sup> 2 _π_<sup>2</sup> _vs_<sup>3:</sup> 



<!-- Start of picture text -->
3 V ω 2 dω = 3 N = ⇒ V ωD 3 = 3 N<br>2 π 2 vs 3 ∫0 ωD 2 π 2 vs 3<br><!-- End of picture text -->

Solving for the **Debye Cutoff Frequency (** _ωD_ **)** : 



<!-- Start of picture text -->
ωD =  vs<br>( 6 πV 2 N )1/3<br><!-- End of picture text -->

The **Debye Temperature (** _θD_ **)** translates this maximum phonon energy into Kelvin: 



<!-- Start of picture text -->
kBθD ≡ hω ¯ D = ⇒ θ D = hv ¯ s<br>kB ( 6 π V2N ) 1 / 3<br><!-- End of picture text -->

• **Rewriting** _D_ ( _ω_ ) **compactly:** Using _ωD_ , the density of states simplifies to: 



<!-- Start of picture text -->
D ( ω ) = 9 N ω 2 (for ω ≤ ωD )<br>ω 3<br>D<br><!-- End of picture text -->

## **3. Total Internal Energy (** _U_ **) and Heat Capacity (** _CV_ **)** 

The total thermal energy _U_ stored in the phonons is found by integrating energy _hω_ ¯ weighted by the Planck distribution _⟨n_ ( _ω_ ) _⟩_ = _e_<sup>_hω_¯/</sup><sup>_kBT_</sup> <u>1</u> _−_ 1<sup>acrossallmodesupto</sup><sup>_ωD_:</sup> 



<!-- Start of picture text -->
1<br>U = hωD ¯ ( ω ) ⟨n ( ω ) ⟩dω = hω ¯ ω 2<br>∫0 ωD ∫0 ωD ( 9 ωND 3 ) e hω ¯ / kBT − 1 dω<br><!-- End of picture text -->

Substitute the dimensionless variable _x ≡ khω_ ¯ _BT_<sup>(sothattheupperlimitbecomes</sup><sup>_xD_=</sup> _khω_ ¯ _BDT_<sup>=</sup><sup>_<u>θ</u>_</sup> _T_<sup>_<u>D</u>_):</sup> 



<!-- Start of picture text -->
x 3<br>U = 9 NkBT (  TθD )3 ∫0 θD / T e x − 1 dx<br><!-- End of picture text -->

Notes 

3 

Differentiating _U_ with respect to _T_ gives the general **Debye Specific Heat Formula** : 



<!-- Start of picture text -->
x 4 e x<br>CV = = 9 NkB<br>( ∂U∂T ) V (  TθD )3 ∫0 θD / T ( e x − 1) 2 dx<br><!-- End of picture text -->

## **4. Deriving the Low-Temperature Limit: The** _T_<sup>3</sup> **Law** 

When the temperature is very low ( _T ≪ θD_ ), the upper integration limit goes to infinity ( _xD_ =<sup>_<u>θ</u>_</sup> _T_<sup>_<u>D</u>→∞_)becausehigh-energyshort-wavelengthmodescannotbeexcited</sup> thermally. 

1. The definite integral evaluates to a standard mathematical constant: 



<!-- Start of picture text -->
∫0 ∞ e x x− 3 1 dx  = π 15 4<br><!-- End of picture text -->

2. Substituting this back into the total energy equation _U_ : 



<!-- Start of picture text -->
U ≈ 9 NkBT = 3 π 4 T 4<br>(  TθD )3 ( π 154 ) 5 NkB θD 3<br><!-- End of picture text -->

3. Differentiating _U_ with respect to _T_ yields the **Debye** _T_<sup>3</sup> **Law** : 



<!-- Start of picture text -->
C lat = ∂U ∂T = 12 5 π 4 NkB (  TθD )3<br><!-- End of picture text -->



<!-- Start of picture text -->
For 1 mole of a solid ( N =  NA and NAkB =  R , where 12 5 π 4 ≈ 234):<br>C lat ≈ 234R ∝ T 3<br>(  T θ D ) 3<br><!-- End of picture text -->

## **5. High-Temperature Limit (** _T ≫ θD_ **)** 

At high temperatures ( _T ≫ θD_ ), _xD_ =<sup>_<u>θ</u>_</sup> _T_<sup>_<u>D</u>≪_1.Intherange</sup><sup>_x∈_[0</sup><sup>_, xD_],</sup><sup>_x_issmallso</sup> _e_<sup>_x_</sup> _−_ 1 _≈ x_ . 



<!-- Start of picture text -->
x 3 x 3 D<br>x 2 dx  = x 3<br>∫0 xD e x − 1 dx ≈ ∫0 xD x dx  = ∫0 xD 3 = 1 3 ( θTD )3<br><!-- End of picture text -->

Substitute this back into _U_ : 



<!-- Start of picture text -->
U ≈ 9 NkBT θD 3 = 3 NkBT = 3 RT<br>(  TθD )3 ( 31 T 3 )<br><!-- End of picture text -->

Differentiating gives: 

**CV** = **3R (Dulong-Petit Law recovered!)** 

Notes 

4 

## **6. Spatial Dimensionality Rule (** _T_<sup>_d_</sup> **Scaling for GATE)** 

A very common GATE question asks how _CV_ scales at low temperatures in non-3D systems. For a _d_ -dimensional crystal: 

- **Density of States:** _D_ ( _ω_ ) _∝ ω_<sup>_d−_1</sup> 

- **Thermal Energy:** _U ∝ T_<sup>_d_+1</sup> 

- **Low-Temperature Heat Capacity: C** lat _∝_ **T**<sup>**d**</sup> 

|Spatial Dimension (_d_)|Physical System|Low-_T_ Heat Capacity _C_lat|
|---|---|---|
|**3D Bulk**|3D Crystal (Cu, Al, Si)|_CV ∝T_ <sup>3</sup>|
|**2D Sheet**|Graphene / Thin Film|_CV ∝T_ <sup>2</sup>|
|**1D Wire**|Carbon Nanotube / Nanowire|_CV ∝T_ <sup>1</sup>|



## **Einstein vs. Debye Summary Table** 

|Feature|Einstein Model|Debye Model|
|---|---|---|
|**Physical Picture**|Independent localized atomic<br>oscillators.|Collective continuous sound<br>waves (phonons).|
|**Frequency Spectrum**|Single frequency _ωE_ (delta<br>function _δ_(_ω −ωE_)).|Continuous spectrum<br>_D_(_ω_)_∝ω_<sup>2 </sup>up to _ωD_.|
|**Low-**_T_ **Behavior (**_T →_0**)**|_CV ∝e_<sup>_−θE_/</sup><sup>_T _</sup>_→_0 (drops off<br>**too fast**).|_CV ∝T_ <sup>3 </sup>(matches<br>experiment perfectly).|
|**High-**_T_ **Behavior (**_T ≫θ_**)**|_CV →_3_R_ (Dulong-Petit).|_CV →_3_R_ (Dulong-Petit).|
|**Best Application**|Optical phonon branches in<br>crystals.|Acoustic phonon branches /<br>low-_T_ lattice heat capacity.|



_Shall we proceed to_ **_Module 4: Band Theory & Semiconductor Physics_** _(covering Kronig-Penney model, effective mass, intrinsic/extrinsic carriers, and Hall effect)?_ 

