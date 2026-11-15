<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-density-of-states-effective-mass-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

In solid-state physics, when we talk about **mass** inside a crystal lattice, we are referring to the quantum mechanical concept of **Effective Mass (** _m_<sup>_∗_</sup> **)** . 

## **1. What is Effective Mass (** _m_<sup>_∗_</sup> **)?** 

In a vacuum, a free electron has a fixed rest mass _m_ 0 _≈_ 9 _._ 11 _×_ 10<sup>_−_31</sup> kg. However, inside a solid crystal, an electron moves through a periodic electrostatic potential _V_ ( _r_ ) created by positively charged ion cores. 

When an external electric or magnetic field is applied, the electron experiences two forces: 

1. The **external force** ( **F** ext = _−e_ **E** ). 

2. The **internal periodic forces** ( **F** int) from electrostatic attraction and Bragg scattering off lattice ions. 

Rather than attempting to calculate these complex internal forces every single time, quantum mechanics incorporates all lattice interactions directly into the particle’s mass. The electron is treated as an “almost free” particle whose response to external forces is governed by an **Effective Mass (** _m_<sup>_∗_</sup> **)** : 



<!-- Start of picture text -->
F ext =  m ∗ a = ⇒ a  = F ext<br>m ∗<br><!-- End of picture text -->

## **2. Mathematical Definition: Curvature of the Energy Band** 

Quantum mechanically, an electron in a crystal moves as a wave packet with group velocity _vg_ = _h_ ¯<sup><u>1</u></sup> _<u>dEdk</u>_<sup>.Differentiatingvelocitywithrespecttotimeunderanexternalforce</sup><sup>_F_=</sup><sup>_h_¯</sup><sup>_<u>dk</u>_</sup> _dt_ gives: 



<!-- Start of picture text -->
a  = dvg d 2 E dk d 2 E F ext<br>dt = h ¯ 1 dk 2 dt = ( h ¯1 2 dk 2 )<br><!-- End of picture text -->

Comparing this with _a_ = _F_ ext/ _m_<sup>_∗_</sup> yields the fundamental definition of effective mass: 



<!-- Start of picture text -->
1 d 2 E = ⇒ m ∗ = h ¯ 2<br>d 2 E<br>m ∗ = h ¯ 12 dk 2<br>dk 2<br><!-- End of picture text -->

Notes 

2 

## **Physical Meaning of Band Curvature:** 

- **High / Sharp Curvature (**<sup>_<u>d</u>_</sup> _dk_<sup>2</sup><sup>_<u>E</u>_2</sup><sup>**islarge):**Theeffectivemass</sup><sup>_m∗_is</sup><sup>**small**.The</sup> electron accelerates rapidly under an electric field, leading to high carrier mobility. 

- • **Low / Flat Curvature (**<sup>_<u>d</u>_</sup> _dk_<sup>2</sup><sup>_<u>E</u>_2</sup><sup>**issmall):**Theeffectivemass</sup><sup>_m∗_is</sup><sup>**heavy**.The</sup> electron accelerates slowly. 

- **Negative Curvature (**<sup>_<u>d</u>_</sup> _dk_<sup>2</sup><sup>_<u>E</u>_2</sup><sup>_<_0</sup><sup>**):**Nearthetopofanallowedenergyband,the</sup> curve bends downward. Here _m_<sup>_∗_</sup> becomes **negative** . This negative effective mass physically represents a state where Bragg scattering off lattice planes transfers more momentum to the lattice than the external force provides. This missing electron state near the top of the band is modeled as a positively charged particle called a **hole** with positive effective mass ( _m_<sup>_∗_</sup> _h_<sup>=</sup><sup>_−m_</sup> _e_<sup>_∗_).</sup> 

## **3. Why are there Different “Masses” in Semiconductors (like Silicon)?** 

In isotropic semiconductors (like GaAs), energy bands near the band edge are spherical, so _m_<sup>_∗_</sup> is a single number (0 _._ 067 _m_ 0). 

In anisotropic semiconductors like **Silicon (Si)** , the constant-energy surfaces near the 6 conduction band minima are **cigar-shaped prolate ellipsoids** in 3D _k_ -space. This creates direction-dependent mass parameters: 

- **Longitudinal Mass (** _ml ≈_ 0 _._ 98 _m_ 0 **in Si):** Mass measured along the major axis of the ellipsoid (heavy/slow direction). 

- **Transverse Mass (** _mt ≈_ 0 _._ 19 _m_ 0 **in Si):** Mass measured along the minor axes (light/fast direction). 

To use these in standard isotropic equations, two distinct scalar averages are defined: 

1. **Density-of-States Effective Mass (** _m_<sup>_∗_</sup> _dn_<sup>**):**</sup> 

   - **Purpose:** Used for state counting and calculating total carrier populations ( _Nc, n_ 0). 

   - **Formula:** Geometric mean across all 6 conduction valleys: 

      - _m_<sup>_∗_</sup> _dn_<sup>= 62/3(</sup><sup>_mlm_2</sup> _t_<sup>)1/3</sup><sup>_≈_1</sup><sup>_._08</sup><sup>_m_0</sup> (for Silicon) 

2. **Conductivity Effective Mass (** _m_<sup>_∗_</sup> _cn_<sup>**):**</sup> 

   - **Purpose:** Used for charge transport, drift velocity, and mobility ( _µ_ = _meτ_<sup>_∗_</sup> _cn_<sup>).</sup> 

   - **Formula:** Harmonic mean averaging acceleration over 3 orthogonal directions: 



<!-- Start of picture text -->
1 = 1 + 2 = ⇒ m ∗ cn = 3 mlmt ≈ 0 . 26 m 0 (for Silicon)<br>m ∗ cn 3 ( m 1 l mt ) mt  + 2 ml<br><!-- End of picture text -->

_Would you like to work through a GATE problem calculating carrier mobility or density of states using these effective masses?_ 

