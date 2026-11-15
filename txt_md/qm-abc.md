<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-abc.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Let’s slow down completely and build this step-by-step from absolute first principles. Forget complex equations for a moment—let’s understand the **physical picture** of what is actually happening inside an atom when you bring a magnet near it. 

## **Step 1: An Atom is a Tiny Magnet** 

In classical physics, what is a magnet? Any time electric charge moves in a loop, it creates a magnetic field. 

1. **Orbiting Motion:** An electron (which has charge _−e_ ) circles around the atomic nucleus. Because a moving charge is an electric current, this orbiting electron acts like a tiny current loop. 

2. **Magnetic Moment (** _⃗µL_ **):** Because it orbits in a loop, the electron acts like a miniature bar magnet. We describe how “strong” this tiny magnet is using its **orbital magnetic dipole moment** ( _⃗µL_ ): 



<!-- Start of picture text -->
µL =  − L<br>( 2 me e )<br><!-- End of picture text -->

_(The minus sign just means the magnetic arrow points opposite to the orbital angular momentum arrow⃗L, because the electron’s charge is negative)._ 

## **Step 2: What Happens When You Put a Magnet in an External Magnetic Field?** 

Think of a compass needle placed near a refrigerator magnet: 

- If the compass needle aligns **with** the magnetic field, it is in a low-energy, relaxed state. 

- If you force the compass needle to point **against** the magnetic field, it stores potential energy (high-energy state). 

The potential energy _E_ of a magnetic dipole in an external magnetic field _⃗B_ is: 



<!-- Start of picture text -->
E =  −⃗µL ·⃗B<br><!-- End of picture text -->

If we align the magnetic field along the _z_ -axis ( _⃗B_ = _Bz_ ˆ), only the _z_ -component matters: _E_ = _−µL,zB_ 

Notes 

2 

## **Step 3: Quantum Mechanics & Space Quantization** 

In classical physics, a compass needle can point at _any_ continuous angle. But in **quantum mechanics** , nature restricts the electron’s orientation! 

The _z_ -component of orbital angular momentum _Lz_ can only take discrete values: 



<!-- Start of picture text -->
Lz =  mlh ¯ where ml ∈{−l, −l  + 1 , . . . ,  0 , . . . ,  + l}<br><!-- End of picture text -->

Because _Lz_ is restricted, the magnetic potential energy is also restricted to discrete levels: 

∆ _E_ = _mlµBB_ 

where _µB_ = 2 _<u>emh</u>_ ¯ _e_<sup>isjustafundamentalunitcalledthe</sup><sup>**BohrMagneton**.</sup> 

**What does this mean physically?** 

- **Without a magnetic field (** _B_ = 0 **):** All (2 _l_ + 1) orientations of an orbital level have the **exact same energy** (they are _degenerate_ ). 

- **With a magnetic field (** _B̸_ = 0 **):** The single energy level **splits apart** into (2 _l_ +1) distinct, equally spaced energy levels! 

## **Step 4: What is a Spectral Line, and Why Does it Split?** 

An atom emits light (a photon) when an electron drops from a higher energy level _E_ 2 to a lower energy level _E_ 1. The frequency _ν_ of the emitted photon depends directly on the energy gap: 

_hν_ = _E_ 2 _− E_ 1 

- **Without a magnetic field:** You have **one** upper energy level and **one** lower energy level. The difference ( _E_ 2 _− E_ 1) gives **one single frequency** _ν_ 0—observed as **a single spectral line** on a detector. 

- **With a magnetic field:** 

   - The upper level splits into multiple sub-levels. 

   - The lower level splits into multiple sub-levels. 

   - Now, electrons can jump between various split sub-levels! 

However, electrons cannot jump randomly; they must follow **Selection Rules** (∆ _ml_ = 0 _, ±_ 1): 

Without Magnetic Field (B = 0) With Magnetic Field (B > 0) ============================== =========================== --- m_l = +1 Upper Level (l = 1) --- m_l = 0 --- m_l = -1 | / | \ | (1 transition) / | \ (3 transitions) v v v v 

Notes 

3 

Lower Level (l = 0) --- m_l = 0 -------------------------------------------------------1 Spectral Line ( _ν_ 0) 3 Spectral Lines 

3 Spectral Lines (Lorentz Triplet) 

This splitting of 1 spectral line into 3 components is called the **Normal Zeeman Effect** . 

## **Step 5: Introducing Electron Spin & Landé** _g_ **-Factor** 

So far, we only talked about the electron **orbiting** the nucleus. But the electron also has an intrinsic property called **spin (** _S_ **)** —it behaves as if it is spinning on its own axis like a top. 

1. Spin also creates its own magnetic moment _⃗µS_ . 

2. But nature added a twist: **spin is twice as effective at producing magnetism as orbital motion!** 

   - Orbital _g_ -factor: _gL_ = 1 

   - Spin _g_ -factor: _gS ≈_ 2 

Because spin and orbital magnetism have different strengths (2 vs 1), when both are present, the total angular momentum is _⃗J_ = _⃗L_ + _⃗S_ . 

To calculate how much the energy levels split when both spin and orbit are involved, we use a correction factor called the **Landé** _g_ **-factor (** _gJ_ **)** : 



<!-- Start of picture text -->
gJ = 1 + j ( j  + 1) +  s ( s  + 1)  − l ( l  + 1)<br>2 j ( j  + 1)<br>becomes:<br>∆ E =  gJ µBBmj<br><!-- End of picture text -->

The energy shift then becomes: 

Because _gJ_ is different for different states, the sublevels split by **unequal amounts** . This creates patterns of **4, 6, or 10 spectral lines** , known as the **Anomalous Zeeman Effect** ! 

## **Core Takeaways to Remember** 

|Concept|What it means in plain<br>English|Key Formula|
|---|---|---|
|**Bohr Magneton (**_µB_**)**|The fundamental “unit” of<br>atomic magnetism.|_µB_ =<br>_e_¯_h_<br>2_me _<sup>_≈_5</sup><sup>_._79</sup><sup>_×_10</sup><sup>_−_5 eV/T</sup>|
|**Normal Zeeman Effect**|Occurs when spin is zero<br>(_S_ = 0). Splits 1 line into **3**<br>**equally spaced lines**.|∆_E_ =_µBBml_|



Notes 

4 

|Concept|What it means in plain<br>English|Key Formula|
|---|---|---|
|**Anomalous Zeeman Effect**|Occurs when spin is present<br>(_S̸_ = 0). Splits 1 line into<br>**multiple unequally spaced**<br>**lines**.|∆_E_ =_gJµBBmj_|
|**Selection Rules**|Rules specifying which jumps<br>electrons are allowed to make.|∆_m_= 0_, ±_1|



Does this step-by-step breakdown make the physical picture clearer? Let me know which specific part (e.g. quantum numbers, Landé _g_ -factor, or line counting) you’d like to walk through next! 

