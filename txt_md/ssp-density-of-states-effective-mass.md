<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-density-of-states-effective-mass.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

In anisotropic semiconductors like **Silicon (Si)** and **Germanium (Ge)** , the conduction band minima do not lie at the zone center ( _k_ = 0). Instead, Silicon has **6 equivalent conduction band minima (valleys)** along the _⟨_ 100 _⟩_ crystallographic directions in _k_ - space. 

Near each minimum, the constant-energy surfaces are **prolate ellipsoids of revolution** (cigar-shaped) defined by two different effective mass parameters: 

- **Longitudinal Mass (** _ml_ **):** Mass along the major axis of the ellipsoid ( _ml ≈_ 0 _._ 98 _m_ 0 for Si). 

- **Transverse Mass (** _mt_ **):** Mass along the two orthogonal minor axes ( _mt ≈_ 0 _._ 19 _m_ 0 for Si). 

Because scalar carrier populations and vector transport processes average _k_ -space differently, we define **two distinct scalar effective masses** for use in 3D isotropic equations. 

## **1. Density-of-States Effective Mass (** _m_<sup>_∗_</sup> _dn_<sup>**)**</sup> 

**Physical Purpose** Used to convert the complex multi-valley ellipsoidal band structure into an equivalent isotropic sphere so that standard 3D density-of-states formulas can be used to calculate **total carrier populations** ( _n_ 0 _, p_ 0), the **effective density of states** ( _Nc, Nv_ ), and the **intrinsic carrier concentration** ( _ni_ ). 

**Detailed Derivation** The equation for a single ellipsoidal constant-energy surface _E_ in momentum space ( _pi_ = ¯ _hki_ ) is: 



<!-- Start of picture text -->
2 mp 2 xtE + 2 mp 2 ytE + 2 mp 2 zlE = 1<br><!-- End of picture text -->

The semi-axes of this momentum-space ellipsoid are _a_ =<sup>_~~√~~_</sup> 2 _mtE_ , _b_ =<sup>_~~√~~_</sup> 2 _mtE_ , and _c_ =<sup>_~~√~~_</sup> 2 _mlE_ . 

1. **Volume of a single ellipsoid in momentum space:** 



<!-- Start of picture text -->
V single = 4 3 πabc  = 4 3 π (2 E )3/2 √ mt · mt · ml = 3 4 π (2 E )3/2( mlm t 2)1/2<br><!-- End of picture text -->



<!-- Start of picture text -->
2. Total momentum volume across all Mc = 6 equivalent valleys:<br>V total = 6  × 4 3 π (2 E )3/2( mlm t 2)1/2<br><!-- End of picture text -->

Notes 

2 

3. **Equating to an equivalent isotropic sphere of mass** _m_<sup>_∗_</sup> _dn_<sup>**:**</sup> 



<!-- Start of picture text -->
V sphere = 4 dn E )3/2 = 4 dn )3/2<br>3 π (2 m∗ 3 π (2 E )3/2( m∗<br><!-- End of picture text -->

Setting _V_ sphere = _V_ total: 



<!-- Start of picture text -->
( m ∗ dn )3/2 = 6  ·  ( mlm 2 t )1/2<br><!-- End of picture text -->

Taking the 2/3 power on both sides yields the **Geometric Mean** : 



<!-- Start of picture text -->
m ∗ dn =  62 / 3 ( mlm2 t ) 1 / 3<br><!-- End of picture text -->

**Numerical Calculation for Silicon:** Using _ml_ = 0 _._ 98 _m_ 0 and _mt_ = 0 _._ 19 _m_ 0: _m_<sup>_∗_</sup> _dn_<sup>= 62/3 [</sup> (0 _._ 98)(0 _._ 19)<sup>2]1/3</sup> _m_ 0 = (3 _._ 3019) _×_ (0 _._ 3283) _m_ 0 _≈_ **1** _._ **08m0** 

**Application in Equations:** 



<!-- Start of picture text -->
dn kBT<br>Nc = 2 = ⇒ n 0 =  Nce − ( Ec−EF  )/ kBT<br>h 2<br>( 2 πm∗ )3/2<br><!-- End of picture text -->

## **2. Conductivity Effective Mass (** _m_<sup>_∗_</sup> _cn_<sup>**)**</sup> 

**Physical Purpose** Governs **charge carrier transport** , including drift velocity, mobility ( _µ_ = _eτ_ / _m_<sup>_∗_</sup> _cn_<sup>), electrical conductivity (</sup><sup>_σ_=</sup><sup>_neµ_), and donor impurity binding energy</sup> calculations. 

**Detailed Derivation** Under an applied electric field _E_ , Newton’s second law gives acceleration _ai_ = _m_<sup>_<u>Fi</u>_</sup> _i_<sup>=</sup><sup>_−_</sup> _m_<sup>_<u>eE</u>_</sup> _i_<sup>_<u>i</u>_.Thecarrierresponsedependsonthe</sup><sup>**reciprocaleffective**</sup> **mass tensor** (1/ _m_<sup>_∗_</sup> ). 

In cubic crystals like Silicon, electrons are distributed equally across all 6 valleys at thermal equilibrium (1/3 of electrons in _x_ -oriented valleys, 1/3 in _y_ , 1/3 in _z_ ). 

1. **Averaging acceleration over 3 orthogonal directions:** 



<!-- Start of picture text -->
= 1 + 1 + 1 = 1 + 1 + 1 = 1 + 2<br>⟨ m 1 ∗ ⟩ 3 ( m 1 x my mz ) 3 ( m 1 l mt mt ) 3 ( m 1 l mt )<br><!-- End of picture text -->

2. **Defining the scalar conductivity mass (** _m_<sup>_∗_</sup> _cn_<sup>**):**</sup> 



<!-- Start of picture text -->
1 ≡ 1 + 2 = 1<br>m ∗ cn 3 ( m 1 l mt ) 3 ( mmt  + 2 lmtml )<br><!-- End of picture text -->

3. **Inverting to find the Harmonic Mean:** 



<!-- Start of picture text -->
3mlmt<br>m ∗<br>cn =<br>mt  +  2ml<br><!-- End of picture text -->

Notes 

3 

**Numerical Calculation for Silicon:** Using _ml_ = 0 _._ 98 _m_ 0 and _mt_ = 0 _._ 19 _m_ 0: 



<!-- Start of picture text -->
1 = 1 2 = 1<br>cn ≈ 0 . 26m0<br>m ∗ cn 3 ( 0 . 198 + 0 . 19 ) 3 (1 . 0204 + 10 . 5263) = 3 . 8489 = ⇒ m ∗<br><!-- End of picture text -->

**Why is** _m_<sup>_∗_</sup> _cn_<sup>**muchlighterthan**</sup><sup>_m∗_</sup> _dn_<sup>**?**</sup> Because acceleration is inversely proportional to mass ( _∝_ 1/ _m_ ), transport is heavily dominated by the lighter transverse direction ( _mt_ = 0 _._ 19 _m_ 0). The harmonic mean biases _m_<sup>_∗_</sup> _cn_<sup>towardthesmallertransversemass,</sup> resulting in 0 _._ 26 _m_ 0, whereas _m_<sup>_∗_</sup> _dn_<sup>includesthevalleydegeneracyfactor62/3whichboosts</sup> its value to 1 _._ 08 _m_ 0. 

## **Summary Comparison Table** 

|Feature|Density-of-States Mass (_m_<sup>_∗_</sup><br>_dn_<sup>)</sup>|Conductivity Mass (_m_<sup>_∗_</sup><br>_cn_<sup>)</sup>|
|---|---|---|
|**Physical Context**|Static carrier population /<br>state counting|Dynamic charge transport &<br>mobility|
|**Mathematical Type**|**Geometric Mean** (weighted<br>by valley count _Mc_)|**Harmonic Mean**<br>(directional average of 1/_m_)|
|**Formula (Silicon)**|_m_<sup>_∗_</sup><br>_dn_ <sup>= 62/3(</sup><sup>_mlm_2</sup><br>_t_ <sup>)1/3</sup>|_m_<sup>_∗_</sup><br>_cn_ <sup>=</sup><br>3_mlmt_<br>_mt_+2_ml_|
|**Value for Si**|_≈_**1**_._**08m0**|_≈_**0**_._**26m0**|
|**Key Applications**|_Nc, Nv, n_0_, p_0_, ni, EFi_|_µn, σn, J_drift_, ad_ (Donor<br>radius)|
|**Isotropic Case (GaAs)**|_m_<sup>_∗_</sup><br>_dn_ <sup>= 0</sup><sup>_._067</sup><sup>_m_0</sup>|_m_<sup>_∗_</sup><br>_cn_ <sup>= 0</sup><sup>_._067</sup><sup>_m_0</sup> <sup>(Identical for</sup><br>spherical bands)|



_Would you like to solve a numerical practice problem on calculating Nc or electron mobility µn using these effective masses for Silicon?_ 

