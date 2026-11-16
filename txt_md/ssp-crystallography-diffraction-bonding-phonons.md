<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-crystallography-diffraction-bonding-phonons.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

GATE PHYSICS 

SOLID STATE PHYSICS 

# **GATE PHYSICS STUDY NOTES Solid State Physics: Crystallography, Diffraction, Bonding, and Phonons** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**|**Elements of Crystallography**|**2**|
|---|---|---|
|**2**|**Diffraction Methods for Structure Determination**|**6**|
|**3**|**Bonding in Solids**|**10**|
|**4**|**Lattice Vibrations & Thermal Properties**|**14**|



1 

GATE PHYSICS 

SOLID STATE PHYSICS 

## **1 Elements of Crystallography** 

### **1. Core Theory** 

**Crystallography** is the branch of science that studies the arrangement of atoms in crystalline solids. A crystalline solid is characterized by a periodic, repeating spatial pattern of its constituent atoms. 

-  **Crystal Lattice:** A mathematical abstraction consisting of an infinite, periodic array of points in space. It is defined by a set of discrete translation operations. 

-  **Basis (or Motif):** An atom, a group of atoms, or a molecule attached identically to each lattice point. The physical crystal structure is created by the mathematical combination: 

   - Crystal Structure = Lattice + Basis (1) 

-  **Bravais Lattices:** In three dimensions, there are exactly **14 distinct Bravais lattices** that describe all possible periodic spatial arrangements of lattice points. These lattices are classified into **7 crystal systems** based on the symmetry of their unit cell axes ( _a, b, c_ ) and interaxial angles ( _α, β, γ_ ): Cubic, Tetragonal, Orthorhombic, Monoclinic, Triclinic, Hexagonal, and Trigonal (Rhombohedral). 

-  **Miller Indices:** A mathematical notation system used to uniquely identify planes and directions in a crystal lattice. They are defined as the reciprocals of the fractional intercepts that a plane makes with the crystallographic unit cell axes, reduced to the smallest integers. 

-  **Reciprocal Lattice:** A mathematical lattice constructed in momentum space ( _k_ -space) from the real-space (direct) lattice. Every set of parallel planes in the direct lattice corresponds to a single point in the reciprocal lattice. The reciprocal lattice represents the spatial Fourier transform of the crystal’s periodic density, acting as the fundamental geometric space for analyzing wave diffraction and electronic band structures in solids. 

### **2. Mathematical Framework** 

-  **Direct Lattice Translation Vector (T):** 



<!-- Start of picture text -->
T  =  n 1 a 1 +  n 2 a 2 +  n 3 a 3 (2)<br><!-- End of picture text -->

where **a** 1 _,_ **a** 2 _,_ **a** 3 are the primitive translation vectors of the direct lattice, and _n_ 1 _, n_ 2 _, n_ 3 are arbitrary integers. 

-  **Wigner-Seitz Primitive Unit Cell:** The smallest volume cell that retains the full translational symmetry of the lattice. It is constructed by drawing lines from a lattice point to all neighboring points, and constructing the perpendicular bisector planes. 

-  **Reciprocal Lattice Primitive Vectors (b** 1 _,_ **b** 2 _,_ **b** 3 **):** 



<!-- Start of picture text -->
a 2  ×  a 3 a 3  ×  a 1 a 1  ×  a 2<br>b 1 = 2 π b 2 = 2 π b 3 = 2 π (3)<br>a 1  ·  ( a 2  ×  a 3) , a 1  ·  ( a 2  ×  a 3) , a 1  ·  ( a 2  ×  a 3)<br><!-- End of picture text -->

satisfying the orthonormality relation: 



<!-- Start of picture text -->
a i ·  b j = 2 πδij (4)<br><!-- End of picture text -->

2 

GATE PHYSICS 

SOLID STATE PHYSICS 

-  **Reciprocal Lattice Translation Vector (G):** 



<!-- Start of picture text -->
G  =  h b 1 +  k b 2 +  l b 3 (5)<br><!-- End of picture text -->

where _h, k, l_ are the integers corresponding to the Miller indices ( _hkl_ ) of the direct lattice plane. 

-  **Interplanar Spacing (** _dhkl_ **):** The perpendicular distance between adjacent parallel planes of Miller indices ( _hkl_ ). 

   - For a general **Orthorhombic** lattice ( _a̸_ = _b̸_ = _c_ , _α_ = _β_ = _γ_ = 90<sup>_◦_</sup> ): 



<!-- Start of picture text -->
1 = h 2 (6)<br>d 2 a 2 + k b 22 + c l 22<br>hkl<br><!-- End of picture text -->

- For a **Cubic** lattice ( _a_ = _b_ = _c_ ): 



<!-- Start of picture text -->
a<br>dhkl = (7)<br>√ h 2 +  k 2 +  l 2<br><!-- End of picture text -->

- Relation to Reciprocal Lattice Vector: 



<!-- Start of picture text -->
2 π<br>dhkl = (8)<br>| G hkl|<br>Primitive Unit Cell:<br>Vc =  | a 1  ·  ( a 2  ×  a 3) |, Vr =  | b 1  ·  ( b 2  ×  b 3) |  = (2 π )3 (9)<br>Vc<br><!-- End of picture text -->

-  **Volume of the Primitive Unit Cell:** 

### **3. Derivation Milestones** 

The properties of reciprocal lattices and Miller indices are derived via these critical mathematical milestones: 

1. **Defining the Plane Equation:** A crystal plane with Miller indices ( _hkl_ ) intercepts the primitive axes at **a** 1 _/h_ , **a** 2 _/k_ , and **a** 3 _/l_ . The vector equation representing two points lying in this plane is: 



<!-- Start of picture text -->
v 1 = a 1 v 2 = a 2 (10)<br>h − a k 2 , k − a l 3<br><!-- End of picture text -->

2. **Orthogonality of G and** ( _hkl_ ) **Planes:** Take the dot product of the reciprocal lattice vector **G** = _h_ **b** 1 + _k_ **b** 2 + _l_ **b** 3 with the plane vectors **v** 1 and **v** 2: 



<!-- Start of picture text -->
G  ·  v 1 = ( h b 1 +  k b 2 +  l b 3)  · = 2 π − 2 π = 0 (11)<br>� a h 1 − a k 2 �<br><!-- End of picture text -->

This proves that the reciprocal lattice vector **G** _hkl_ is strictly **perpendicular** to the ( _hkl_ ) plane. 

3. **Calculating** _dhkl_ **:** The interplanar spacing _dhkl_ is the projection of the intercept vector **a** 1 _/h_ onto the unit normal vector **n** ˆ = **G** _hkl/|_ **G** _hkl|_ : 



<!-- Start of picture text -->
2 π<br>=<br>dhkl = a 1 (12)<br>h ·  ˆ n  = a h 1 · | G G hkl hkl| = a h 1 · h b 1 + | G  k b hkl 2 + |  l b 3 | G hkl|<br><!-- End of picture text -->

3 

GATE PHYSICS 

SOLID STATE PHYSICS 

### **4. Problem-Solving Algorithm** 

#### **Algorithm for Finding Miller Indices and Interplanar Spacings** 

1. **Identify Intercepts:** Determine the intercepts of the crystal plane with the unit cell axes in terms of the lattice parameters ( _x · a_ , _y · b_ , _z · c_ ). Let the intercepts be _p, q, r_ . 

- <u>1</u> 

- 2. **Take Reciprocals:** Calculate the reciprocals of the fractional intercepts: � _p_<sup>_,_</sup><sup><u>1</u></sup> _q_<sup>_,_</sup><sup><u>1</u></sup> _r_ �. 

3. **Clear Fractions:** Multiply by the lowest common multiple (LCM) of the denominators to obtain three integers _h, k, l_ . Present them enclosed in parentheses as ( _hkl_ ). 

   -  If a plane is parallel to an axis, its intercept is infinity ( _∞_ ), and its reciprocal index is 0. 

   -  If an intercept is negative (e.g., _−_ 2), denote it with a bar over the number: (<sup>¯</sup> 2 _kl_ ). 

4. **Calculate** _dhkl_ **:** Substitute _h, k, l_ and the given unit cell parameters _a, b, c_ into the appropriate interplanar spacing formula. 

### **5. Connections to Macroscopic Observables** 

-  **Anisotropy of Mechanical and Optical Properties:** Crystal planes have different packing densities of atoms. Consequently, mechanical strength (cleavage planes), electrical conductivity, and refractive index are anisotropic and vary depending on the crystallographic direction [ _uvw_ ] and plane ( _hkl_ ). 

-  **Elastic Moduli:** The Young’s modulus of a crystal depends directly on the packing density along specific directions. For instance, the [111] direction in FCC crystals is typically stiffer than the [100] direction due to denser atomic packing. 

4 

GATE PHYSICS 

SOLID STATE PHYSICS 

### **6. Crucial Pitfalls** 

#### **Crystallography and Reciprocal Lattice Traps** 

-  **Confusing Miller Indices brackets:** Enclosing indices in parentheses ( _hkl_ ) represents a single plane or set of parallel planes. Square brackets [ _uvw_ ] represent a specific crystallographic direction. Curly braces _{hkl}_ represent a family of symmetryequivalent planes, and angle brackets _⟨uvw⟩_ represent a family of equivalent directions. Using the wrong brackets in an exam will result in a loss of marks. 

-  **The** 2 _π_ **Factor in Reciprocal Lattices:** Solid State Physics textbooks (like Kittel) include a factor of 2other materials (such _π_ in the definition of reciprocal lattice vectors (as crystallography or engineering texts) define **b** _i_ = 2them _π_<sup>**a**</sup><sup>_<u>j</u>_</sup> without<sup>_×_</sup> _..._<sup>**a**</sup><sup>_k_</sup> ), while2 _π_ **a** ( **b** _i ·i_ **b** = _j_ = 2<sup>**a**</sup><sup>_<u>j</u>×_</sup> _...πδ_<sup>**a**</sup><sup>_k_</sup> ). _ij_ andFor _d_ GATE _hkl_ = 2 _π/_ Physics, _|_ **G** _|_ . **always use the** 2 _π_ **convention** , which makes 

-  **Assuming Simple Reciprocal Scaling:** Falsely assuming that the reciprocal of an FCC lattice is an FCC lattice. **The reciprocal of an FCC lattice is a BCC lattice** , and the reciprocal of a BCC lattice is an FCC lattice. A Simple Cubic (SC) lattice is self-reciprocal. 

### **7. Standard Textbook Systems** 

-  **The Simple Cubic (SC) Lattice:** The primitive unit cell has axes **a** 1 = _a_ **x** ˆ, **a** 2 = _a_ **y** ˆ, **a** 3 = _a_ **z** ˆ. The reciprocal lattice vectors are **b** 1 =<sup><u>2</u></sup> _a_<sup>_<u>π</u>_</sup><sup>**x**ˆ,</sup><sup>**b**2=</sup><sup><u>2</u></sup> _a_<sup>_<u>π</u>_</sup><sup>**y**ˆ,</sup><sup>**b**3=</sup><sup><u>2</u></sup> _a_<sup>_<u>π</u>_</sup><sup>**z**ˆ,showingitis</sup> self-reciprocal with lattice constant 2 _π/a_ . 

-  **The Body-Centered Cubic (BCC) Lattice:** The primitive translation vectors connect the corner to the body center: **a** 1 =<sup>_<u>a</u>_</sup> 2<sup>(ˆ</sup><sup>**x**+</sup><sup>**y**ˆ</sup><sup>_−_</sup><sup>**z**ˆ),</sup><sup>**a**2=</sup><sup>_<u>a</u>_</sup> 2<sup>(</sup><sup>_−_</sup><sup>**x**ˆ +</sup><sup>**y**ˆ + ˆ</sup><sup>**z**),</sup><sup>**a**3=</sup><sup>_<u>a</u>_</sup> 2<sup>(ˆ</sup><sup>**x**</sup><sup>_−_</sup><sup>**y**ˆ + ˆ</sup><sup>**z**).</sup> Its reciprocal vectors map directly to an FCC lattice of side 4 _π/a_ . 

5 

GATE PHYSICS 

SOLID STATE PHYSICS 

## **2 Diffraction Methods for Structure Determination** 

### **1. Core Theory** 

Because interatomic distances in solids are on the order of several<sup>˚</sup> Angstr¨oms (1<sup>˚</sup> A = 10<sup>_−_10</sup> m), electromagnetic radiation must have a wavelength of the same order of magnitude to undergo diffraction. This condition is met by **X-rays**, as well as thermal neutrons and high-energy electrons. 

-  **Bragg’s Law:** Models X-ray diffraction as the specular reflection of incident waves from parallel planes of atoms in the crystal lattice. Specular reflection from successive planes interferes constructively only when the optical path difference is an integer multiple of the wavelength. 

-  **Laue Equations:** A more rigorous formulation of diffraction that models the crystal as a periodic 3D array of scattering centers. Diffraction occurs when the scattered waves from all lattice points interfere constructively, which requires the scattering vector (change in wave vector) to be equal to a reciprocal lattice vector. 

-  **Structure Factor (** _SG_ **):** Represents the total amplitude of the wave scattered by all the atoms inside a single unit cell. While the Bravais lattice geometry determines the *directions* where diffraction can occur, the specific arrangement of atoms within the basis determines the *intensity* of each diffraction peak. If the structure factor for a specific set of planes ( _hkl_ ) is zero ( _SG_ = 0), that diffraction peak is systematically extinguished (missing peak). 

### **2. Mathematical Framework** 

####  **Bragg’s Law:** 



<!-- Start of picture text -->
2 dhkl  sin  θ =  nλ (13)<br><!-- End of picture text -->

where: 

- _dhkl_ is the interplanar spacing. 

- _θ_ is the Bragg angle (angle between the incident beam and the crystal plane, **not** the normal to the plane). 

- _λ_ is the wavelength of the incident X-ray. 

- _n_ is the integer order of diffraction ( _n_ = 1 _,_ 2 _,_ 3 _, . . ._ ). 

In modern crystallography, _n_ is usually absorbed into the Miller indices by writing _d_ = _dhkl/n_ , reducing the equation to 2 _d_ sin _θ_ = _λ_ . 

-  **The Laue Condition (Vector Form):** 



<!-- Start of picture text -->
∆ k  ≡ k f − k i =  G (14)<br><!-- End of picture text -->

where **k** _i_ is the incident wave vector ( _|_ **k** _i|_ = 2 _π/λ_ ), **k** _f_ is the scattered wave vector, and **G** is a reciprocal lattice vector. 



<!-- Start of picture text -->
– For elastic scattering ( | k i|  =  | k f |  =  k ), the Laue condition simplifies to:<br><!-- End of picture text -->



<!-- Start of picture text -->
2 k i ·  G  =  G 2 or 2 k i ·  G  +  G 2 = 0 (depending on sign convention) (15)<br><!-- End of picture text -->

6 

GATE PHYSICS 

SOLID STATE PHYSICS 

-  **The Structure Factor (** _Shkl_ **):** 



<!-- Start of picture text -->
N<br>Shkl = � fje − 2 πi ( hxj + kyj + lzj ) (16)<br>j =1<br><!-- End of picture text -->

where: 

   - _N_ is the number of atoms in the basis (within the unit cell). 

   - _fj_ is the atomic form factor (scattering power) of the _j_ -th atom. 

   - ( _xj, yj, zj_ ) are the fractional coordinates of the _j_ -th atom within the unit cell (0 _≤ xj, yj, zj <_ 1). 

   - ( _hkl_ ) are the Miller indices of the reflection. 

-  **Diffraction Intensity (** _Ihkl_ **):** 



<!-- Start of picture text -->
Ihkl ∝|Shkl| 2 (17)<br><!-- End of picture text -->

### **3. Derivation Milestones** 

1. **The Bragg Path Difference:** Draw two parallel planes separated by _d_ . An incident wave strikes the top plane at angle _θ_ and is reflected. A parallel wave strikes the lower plane. Construct perpendicular lines from the reflection point of the first wave to the path of the second wave. The extra path traveled by the second wave is: 



<!-- Start of picture text -->
∆=  s 1 +  s 2 =  d  sin  θ  +  d  sin  θ = 2 d  sin  θ (18)<br><!-- End of picture text -->

Constructive interference requires this path difference to equal an integer number of wavelengths: 2 _d_ sin _θ_ = _nλ_ . 2. **Equivalence of Bragg and Laue Formulations:** Consider elastic scattering **k** _f −_ **k** _i_ = **G** . Since _|_ **k** _i|_ = _|_ **k** _f |_ = _k_ , the vector subtraction forms an isosceles triangle. The angle of deviation is 2 _θ_ , meaning the angle between **k** _i_ and the reflecting plane is _θ_ . The magnitude of the reciprocal vector is _|_ **G** _|_ = 2 _k_ sin _θ_ . Substitute _|_ **G** _|_ = 2 _π/d_ and _k_ = 2 _π/λ_ : 



<!-- Start of picture text -->
2 π<br>d = 2 � 2 λπ � sin  θ = ⇒ 2 d  sin  θ =  λ (19)<br><!-- End of picture text -->

3. **The Brillouin Zone Construction:** The Laue condition 2 **k** _·_ **G** = _G_<sup>2</sup> can be divided by 4: 



<!-- Start of picture text -->
2<br>1<br>k  · � 21 G � = ���� 2 G ���� (20)<br><!-- End of picture text -->

This represents the equation of a plane that perpendicular-bisects the reciprocal lattice vector **G** . The region enclosed by these perpendicular bisector planes of all reciprocal lattice vectors surrounding the origin is the **First Brillouin Zone**. Diffraction occurs strictly at the boundaries of this zone. 

7 

GATE PHYSICS 

SOLID STATE PHYSICS 

### **4. Problem-Solving Algorithm** 

#### **Algorithm for Structure Factor and Systematic Extinctions** 

1. **Identify Basis Coordinates:** Write the fractional coordinates ( _xj, yj, zj_ ) for all atoms in the unit cell. 

2. **Set Up the Structure Factor Sum:** Substitute these coordinates into the structure factor formula: _Shkl_ = _f_ � _e_<sup>_−_2</sup><sup>_πi_(</sup><sup>_hxj_+</sup><sup>_kyj_+</sup><sup>_lzj_)</sup> (21) _j_ 

(Assuming identical atoms of form factor _f_ ). 

3. **Evaluate the Complex Exponential:** Apply Euler’s identity _e_<sup>_iθ_</sup> = cos _θ_ + _i_ sin _θ_ and the relations: 



<!-- Start of picture text -->
e iπn = ( − 1) n for integer n (22)<br><!-- End of picture text -->

4. **Derive Extinction Rules:** 

 For **BCC** (basis points at (0 _,_ 0 _,_ 0) and (1 _/_ 2 _,_ 1 _/_ 2 _,_ 1 _/_ 2)): 



<!-- Start of picture text -->
Shkl =  f =  f (23)<br>�1 +  e −iπ ( h + k + l )� �1 + ( − 1) h + k + l �<br><!-- End of picture text -->

Diffraction occurs only when ** _h_ + _k_ + _l_ is even**. If _h_ + _k_ + _l_ is odd, _Shkl_ = 0, and the peak is extinguished. 

 For **FCC** (basis points at (0 _,_ 0 _,_ 0), (1 _/_ 2 _,_ 1 _/_ 2 _,_ 0), (1 _/_ 2 _,_ 0 _,_ 1 _/_ 2), (0 _,_ 1 _/_ 2 _,_ 1 _/_ 2)): 



<!-- Start of picture text -->
Shkl =  f (24)<br>�1 + ( − 1) h + k + ( − 1) h + l + ( − 1) k + l �<br><!-- End of picture text -->

Diffraction occurs only when ** _h, k, l_ are all even or all odd** (unmixed). If they are mixed, _Shkl_ = 0. 

### **5. Connections to Macroscopic Observables** 

-  **Crystal Structure Identification (XRD Powder Diffraction):** Macroscopic powder diffraction profiles display intense peaks at specific angles 2 _θ_ . By measuring the ratio of sin<sup>2</sup> _θ_ for successive peaks, we can uniquely identify the crystal structure: 

   - SC: sin<sup>2</sup> _θ_ ratios scale as 1 : 2 : 3 : 4 : 5 : 6 : 8 : 9 _. . ._ 

   - BCC: sin<sup>2</sup> _θ_ ratios scale as 2 : 4 : 6 : 8 : 10 : 12 : 14 : 16 _. . ._ (even sums of _h_<sup>2</sup> + _k_<sup>2</sup> + _l_<sup>2</sup> ) 

   - FCC: sin<sup>2</sup> _θ_ ratios scale as 3 : 4 : 8 : 11 : 12 : 16 : 19 _. . ._ (unmixed _h, k, l_ , so _h_<sup>2</sup> + _k_<sup>2</sup> + _l_<sup>2</sup> _∈ {_ 3 _,_ 4 _,_ 8 _,_ 11 _,_ 12 _,_ 16 _,_ 19 _}_ ) 

8 

GATE PHYSICS 

SOLID STATE PHYSICS 

### **6. Crucial Pitfalls** 

#### **Diffraction Interpretation Errors** 

-  **Misidentifying the Bragg Angle** _θ_ **:** The angle given in a problem is often the angle of deviation (2 _θ_ , the angle between the transmitted and diffracted beams) or the angle relative to the plane normal. Always ensure you extract the true Bragg angle _θ_ (the grazing angle relative to the plane surface) before inserting it into 2 _d_ sin _θ_ = _λ_ . 

-  **Mixing** _dhkl_ **and Unit Cell Side** _a_ **:** Bragg’s law contains _d_ , while many crystallography questions ask for the unit cell edge _a_ . You must always link them using the geometry-specific formula: _d_ = _a/_ _~~√~~ h_<sup>2</sup> + _k_<sup>2</sup> + _l_<sup>2</sup> for cubic crystals. 

-  **Failing to Recognize the** _h_<sup>2</sup> + _k_<sup>2</sup> + _l_<sup>2</sup> = 7 **Extinction in SC:** In Simple Cubic systems, all integer values of _h_<sup>2</sup> + _k_<sup>2</sup> + _l_<sup>2</sup> are allowed. However, the number 7 cannot be written as the sum of three squared integers ( _h_<sup>2</sup> + _k_<sup>2</sup> + _l_<sup>2</sup><sup>_̸_</sup> = 7). Therefore, there is a ”missing” peak in simple cubic spectra between the 6th ( _h_<sup>2</sup> + _k_<sup>2</sup> + _l_<sup>2</sup> = 6, e.g., (211)) and 7th observed peak ( _h_<sup>2</sup> + _k_<sup>2</sup> + _l_<sup>2</sup> = 8, e.g., (220)). 

### **7. Standard Textbook Systems** 

-  **The NaCl Crystal (FCC with basis):** Consists of two interpenetrating FCC lattices of Na<sup>+</sup> and Cl<sup>_−_</sup> . Because the atomic form factors of sodium and chlorine are different, reflections where _h, k, l_ are mixed do not cancel completely, but their intensities are modulated by the difference _|f_ Na _− f_ Cl _|_<sup>2</sup> . 

-  **The KCl Crystal:** Chemically identical structure to NaCl. However, because the K<sup>+</sup> and Cl<sup>_−_</sup> ions are isoelectronic (both have 18 electrons), their atomic form factors are virtually identical: _f_ K _≈ f_ Cl. This causes the diffraction profile of KCl to look like a Simple Cubic unit cell of half the lattice parameter, as the alternating differences cancel out completely. 

9 

GATE PHYSICS 

SOLID STATE PHYSICS 

## **3 Bonding in Solids** 

### **1. Core Theory** 

Solid structures are held together by attractive electrostatic forces between atoms or ions, balanced at short distances by repulsive quantum mechanical Pauli exclusion forces. 

-  **Ionic Bonding:** Formed by the complete electrostatic transfer of valence electrons from electropositive atoms (metals) to electronegative atoms (non-metals), creating closed-shell ions. The long-range electrostatic interaction is calculated via the **Madelung Constant**. 

-  **Covalent Bonding:** Formed by the sharing of valence electrons between adjacent atoms, which localized electron density in the bonding region. It is highly directional and characterized by overlapping atomic orbitals (hybridization). 

-  **Metallic Bonding:** Formed by a regular array of positive metal cores held together by a highly delocalized, mobile ”sea” of free valence electrons. 

-  **Van der Waals (Molecular) Bonding:** Weak, non-directional electrostatic forces between neutral molecules, driven by fluctuating dipole-dipole interactions, modeled by the **LennardJones potential**. 

-  **Cohesive Energy:** The net energy required to disassemble a solid crystal into its constituent, isolated neutral atoms at infinite separation. 

### **2. Mathematical Framework** 

-  **The Lennard-Jones Potential (** _V_ **LJ) for Van der Waals Crystals:** 



<!-- Start of picture text -->
−<br>V LJ( r ) = 4 ϵ (25)<br>�� σr �12 � σr �6 �<br><!-- End of picture text -->

where: 

   - _ϵ_ is the depth of the potential well. 

   - _σ_ is the distance at which the potential is zero ( _V_ ( _σ_ ) = 0). 

   - _r_ is the interatomic distance. 

   - _r_<sup>_−_6</sup> represents the attractive van der Waals dipole-dipole dispersion. 

   - _r_<sup>_−_12</sup> represents the short-range, empirical repulsive Pauli exclusion force. 

-  **The Total Potential Energy of an Ionic Crystal (** _U_ **total):** 



<!-- Start of picture text -->
αe 2<br>U total( R ) =  N (26)<br>� RB n − 4 πϵ 0 R �<br><!-- End of picture text -->

where: 

- _N_ is the number of ion pairs in the crystal. 

- _R_ is the nearest-neighbor interionic distance. 

- _B/R_<sup>_n_</sup> is the Born-Land´e power-law repulsive potential ( _n ≈_ 5 _−_ 12). 

10 

GATE PHYSICS 

SOLID STATE PHYSICS 

**–** _α_ is the dimensionless **Madelung Constant** of the crystal geometry: 



<!-- Start of picture text -->
( ± )<br>α ≡ � (27)<br>rij/R<br>j̸ = i<br><!-- End of picture text -->

 **The Equilibrium Cohesive Energy (** _U_ 0 **):** 



<!-- Start of picture text -->
U 0 ≡ U total( R 0) =  − Nαe 2 1  − 1 (28)<br>4 πϵ 0 R 0 � n �<br><!-- End of picture text -->

where _R_ 0 is the equilibrium interionic spacing. 

### **3. Derivation Milestones** 

The derivation of the equilibrium cohesive energy of an ionic solid follows these critical steps: 

1. **Writing the Energy Expression:** Formulate the total potential energy per ion pair by summing the electrostatic attraction and Born-Land´e repulsion over all ions: 



<!-- Start of picture text -->
αe 2<br>U ( R ) = B (29)<br>R n − 4 πϵ 0 R<br><!-- End of picture text -->

2. **Enforcing the Equilibrium Minimization Condition:** At the equilibrium interionic spacing _R_ = _R_ 0, the net force on the ions is zero, meaning the potential energy is at a minimum: 



<!-- Start of picture text -->
dU ( R ) αe 2<br>= 0 = ⇒− nB + = 0 (30)<br>DR ���� R = R 0 R 0 n +1 4 πϵ 0 R 0 2<br><!-- End of picture text -->

3. **Isolating the Repulsive Parameter** _B_ **:** Rearrange this minimization result to solve for _B_ : 



<!-- Start of picture text -->
0<br>B = αe 2 Rn− 1 (31)<br>4 πϵ 0 n<br><!-- End of picture text -->

4. **Substituting Back to Yield** _U_ 0 **:** Substitute this expression for _B_ back into the original potential energy equation: 



<!-- Start of picture text -->
αe 2 αe 2<br>U ( R 0) = αe 2 R 0 n− 1 − =  − 1  − 1 (32)<br>4 πϵ 0 nR 0 n 4 πϵ 0 R 0 4 πϵ 0 R 0 � n �<br><!-- End of picture text -->

11 

GATE PHYSICS 

SOLID STATE PHYSICS 

### **4. Problem-Solving Algorithm** 

#### **Algorithm for Cohesive Energy and Lennard-Jones Parameters** 

1. **Identify the Potential Equation:** Determine if the system is ionic (Born-Land´e) or molecular (Lennard-Jones). 

2. **Minimize the Potential:** Differentiate the given potential _V_ ( _r_ ) with respect to _r_ and set the derivative to zero: 



<!-- Start of picture text -->
dV ( r )<br>= 0 (33)<br>dr<br><!-- End of picture text -->

For a single pair of Lennard-Jones atoms: 



<!-- Start of picture text -->
dV LJ = 4 ϵ − 12 σ 12 + 6 σ 6 = 0 = ⇒ r 0 = 2 1 / 6 σ ≈ 1 . 122 σ (34)<br>dr � r 13 r 7 �<br><!-- End of picture text -->

3. **Calculate Cohesive Energy:** Substitute the equilibrium distance _r_ 0 back into the potential energy equation to find the minimum well depth _V_ 0: 



<!-- Start of picture text -->
σ σ<br>V min =  V  ( r 0) = 4 ϵ − = 4 ϵ =  −ϵ (35)<br>�� 2 1 / 6 σ �12 � 2 1 / 6 σ �6 � � 41 − 2 1 �<br><!-- End of picture text -->

Multiply by _N_ (or the appropriate lattice sum factors for crystals) to find the total cohesive energy. 

### **5. Connections to Macroscopic Observables** 

-  **Bulk Modulus (** _BK_ **):** The compressibility and stiffness of a crystal are directly related to the second derivative of its cohesive energy at equilibrium: 



<!-- Start of picture text -->
BK =  V 0 d 2 U = ( n − 1) αe 2 (36)<br>dV 2 ���� V 0 18(4 πϵ 0) R 0 4<br><!-- End of picture text -->

This proves that solids with highly charged ions (large _Z_ ) and short interionic spacings _R_ 0 are highly incompressible (high bulk modulus, e.g., MgO). 

-  **Melting Points:** Strongly bound solids (high cohesive energy, like ionic or covalent crystals) have very high melting points, whereas weakly bound molecular crystals (low cohesive energy, like Argon or methane) melt at low temperatures. 

12 

GATE PHYSICS 

SOLID STATE PHYSICS 

### **6. Crucial Pitfalls** 

#### **Cohesive Energy and Power-Law Traps** 

-  **The Repulsive Exponent Sign:** Ensure you write the Born-Land´e factor as �1 _− n_<sup><u>1</u></sup> �, not (1 _− n_ ). Since _n >_ 1, �1 _− n_<sup><u>1</u></sup> � is always positive, making the cohesive energy _U_ 0 strictly negative (representing a bound, stable crystal). 

-  **Summation Limits for the Madelung Constant:** Forgetting that _α_ is a property of the crystal geometry, not the atoms. Calculating _α_ requires summing an alternating series. If you truncate the series too early or neglect the sign of the charging shells, you will get an incorrect value. 

### **7. Standard Textbook Systems** 

-  **The Sodium Chloride (NaCl) Crystal:** Consists of alternating Na<sup>+</sup> and Cl<sup>_−_</sup> ions. The Madelung constant is _α_ NaCl _≈_ 1 _._ 7476, and the Born exponent is _n ≈_ 9. 

-  **Solid Argon (Ar):** A classic molecular crystal held together by weak van der Waals forces. It crystallized into an FCC structure, with total cohesive energy described by summing the Lennard-Jones potential over all lattice sites: _U_ tot = 2 _Nϵ_ 12 _._ 13 � _Rσ_ �12 _−_ 14 _._ 45 � _Rσ_ . � �6<sup>�</sup> 

13 

GATE PHYSICS 

SOLID STATE PHYSICS 

## **4 Lattice Vibrations & Thermal Properties** 

### **1. Core Theory** 

Atoms in solids are not stationary but oscillate about their equilibrium positions. These coupled mechanical oscillations propagate through the crystal as elastic waves. 

-  **Phonons:** The quantized packets of elastic wave energy in a crystal lattice, analogous to photons in electromagnetic waves. They are bosons with energy _E_ = ℏ _ω_ and momentum **p** = ℏ **k** . 

-  **1D Monatomic Chain:** Models a 1D crystal as a string of identical masses _M_ connected by identical springs of force constant _β_ . This system acts as a low-pass filter, transmitting low frequencies but creating a sharp maximum cutoff frequency at the boundary of the Brillouin zone. 

-  **1D Diatomic Chain:** Models a crystal with two alternating masses _M_ 1 and _M_ 2. This introduces two distinct branches of vibrations: 

   - **Acoustic Branch:** Adjacent atoms oscillate in phase, representing sound propagation ( _k →_ 0 = _⇒ ω ∝ k_ ). 

   - **Optical Branch:** Adjacent atoms oscillate out of phase, producing electric dipoles that couple with light waves ( _k →_ 0 = _⇒ ω ≈_ constant _̸_ = 0). 

-  **Specific Heat Capacity Models:** Microscopic theories explaining how lattice vibrations absorb thermal energy: 

   - **Einstein Model:** Assumes all atoms oscillate independently as isolated 3D quantum harmonic oscillators with a single frequency _ωE_ . 

   - **Debye Model:** Models vibrations as a continuum of elastic sound waves with a density of states scaling as _g_ ( _ω_ ) _∝ ω_<sup>2</sup> , terminating at a maximum cutoff frequency _ωD_ . 

### **2. Mathematical Framework** 

-  **Monatomic Dispersion Relation:** 



<!-- Start of picture text -->
4 β<br>ω ( k ) = (37)<br>� M ����sin � ka 2 �����<br><!-- End of picture text -->

where _β_ is the spring force constant, _M_ is the atomic mass, and _a_ is the lattice spacing. 

- Cutoff frequency at the zone boundary ( _k_ = _±π/a_ ): 



<!-- Start of picture text -->
4 β<br>ω max = (38)<br>� M<br><!-- End of picture text -->

-  **Diatomic Dispersion Relation:** 



<!-- Start of picture text -->
ω 2 =  β + 1 ± β + 1 − 4 sin2( ka/ 2) (39)<br>� M 11 M 2 � � � M 11 M 2 �2 M 1 M 2<br>1 1<br>– Optical Branch (+ sign): At k = 0, ω opt = � 2 β � M 1 + M 2 �.<br><!-- End of picture text -->

14 

GATE PHYSICS 

SOLID STATE PHYSICS 

- **Acoustic Branch (- sign):** At _k_ = 0, _ω_ ac _≈ vsk →_ 0. 

- **Forbidden Band Gap:** A frequency region between the top of the acoustic branch and the bottom of the optical branch where no propagating wave solutions exist: 



<!-- Start of picture text -->
2 β 2 β<br>< ω < (40)<br>� M heavy � M light<br><!-- End of picture text -->

-  **Einstein Specific Heat (** _CV_ **):** 



<!-- Start of picture text -->
e θE /T<br>CV = 3 R (41)<br>� θTE �2 e θE /T − 1<br>� �2<br><!-- End of picture text -->

where _θE ≡_ ℏ _ωE/kB_ is the Einstein Temperature. 

-  **Debye Density of States (** _g_ ( _ω_ ) **):** 



<!-- Start of picture text -->
g ( ω ) = 3 V ω 2 for ω ≤ ωD (42)<br>2 π 2 vs 3<br><!-- End of picture text -->

-  **Debye Specific Heat (** _CV_ **):** 



<!-- Start of picture text -->
x 4 e x<br>CV = 9 R (43)<br>� θTD �3 �0 θD/T ( e x − 1) 2 dx<br><!-- End of picture text -->

where _θD ≡_ ℏ _ωD/kB_ is the Debye Temperature. 

### **3. Derivation Milestones** 

The 1D monatomic chain dispersion relation is derived via these critical milestones: 

1. **Equations of Motion:** Write Newton’s second law for the _n_ -th atom, considering force contributions from its nearest neighbors _n_ + 1 and _n −_ 1: 



<!-- Start of picture text -->
M d dt 2 u 2 n =  β ( un +1  − un )  − β ( un − un− 1) =  β ( un +1 +  un− 1  − 2 un ) (44)<br><!-- End of picture text -->

2. **Applying the Traveling Wave Ansatz:** Propose a harmonic plane-wave solution: 



<!-- Start of picture text -->
un ( t ) =  Ae i ( kna−ωt ) (45)<br><!-- End of picture text -->

3. **Substituting and Factoring:** Substitute the ansatz into the differential equation: 



<!-- Start of picture text -->
e ika +  e −ika − 2 (46)<br>−Mω 2 Ae i ( kna−ωt ) =  βAe i ( kna−ωt ) � �<br><!-- End of picture text -->

Cancel common terms to yield: 



<!-- Start of picture text -->
−Mω 2 =  β [2 cos( ka )  − 2] =  − 2 β [1  − cos( ka )] (47)<br><!-- End of picture text -->

4. **Isolating Frequency via Trigonometric Half-Angle Identity:** Apply 1 _−_ cos( _ka_ ) = 2 sin<sup>2</sup> ( _ka/_ 2): 



<!-- Start of picture text -->
4 β<br>Mω 2 = 4 β  sin 2 = ⇒ ω ( k ) = (48)<br>� ka 2 � � M ����sin � ka 2 �����<br><!-- End of picture text -->

15 

GATE PHYSICS 

SOLID STATE PHYSICS 

### **4. Problem-Solving Algorithm** 

#### **Algorithm for Specific Heat Temperature Limits** 

1. **Determine the Temperature Regime:** Identify if _T ≫ θ_ (high-temperature limit) or _T ≪ θ_ (low-temperature limit). 

2. **High-Temperature Limit (** _T ≫ θD_ **or** _T ≫ θE_ **):** 

   -  Expand exponentials using Taylor series: _e_<sup>_x_</sup> _≈_ 1 + _x_ . 

   -  Both the Einstein and Debye models collapse back to the classical **Dulong-Petit Law**: 

_CV ≈_ 3 _R_ (or 3 _NkB_ ) (49) 

3. **Low-Temperature Limit (** _T ≪ θ_ **):** 

   -  **Einstein Model:** As _T →_ 0, _CV_ decays exponentially: _CV ∝ e_<sup>_−θE/T_</sup> _→_ 0. **This is physically inaccurate** because it neglects low-frequency acoustic modes. 

   -  **Debye Model:** As _T →_ 0, the integration limits can be extended to infinity, yielding the **Debye _T_<sup>3</sup> Law**: 



<!-- Start of picture text -->
CV = 12 π 4 R ∝ T 3 (50)<br>5 � θTD �3<br><!-- End of picture text -->

This is highly accurate for non-magnetic insulators. 

### **5. Connections to Macroscopic Observables** 

-  **Specific Heat of Metals vs. Insulators:** At low temperatures, the heat capacity of an insulator is dominated by phonons: _CV ≈ AT_<sup>3</sup> . For a metal, free conduction electrons add a linear term: 

_CV ≈ γT_ + _AT_<sup>3</sup> (51) 

Plotted as _CV /T_ vs _T_<sup>2</sup> , this yields a straight line with intercept _γ_ and slope _A_ , allowing experimental determination of the electronic and phonon density of states. 

-  **Thermal Expansion and Thermal Conductivity:** Lattice anharmonicity causes the average interatomic distance to increase with temperature, driving macroscopic thermal expansion. Phonon-phonon collisions (Umklapp scattering) limit the thermal conductivity of insulators at high temperatures ( _K ∝_ 1 _/T_ ). 

16 

GATE PHYSICS 

SOLID STATE PHYSICS 

### **6. Crucial Pitfalls** 

#### **Lattice Vibration and Heat Capacity Traps** 

-  **Confusing Phase and Group Velocity:** The phase velocity is _vp_ = _ω/k_ , representing the speed of individual wave crests. The group velocity is _vg_ = _dω/dk_ , representing the speed of envelope and energy propagation (phonon speed). At the zone boundary ( _k_ = _π/a_ ), the dispersion curve is flat: _dω/dk_ = 0. Thus, **the group velocity of phonons is zero at the Brillouin zone boundary** , forming a standing wave. Falsely using _vp_ instead of _vg_ in transport calculations is a common mistake. 

-  **Monatomic vs. Diatomic Chain branches:** A 1D monatomic unit cell contains 1 atom, yielding exactly 1 acoustic branch and 0 optical branches. A 1D diatomic unit cell contains 2 atoms, yielding 1 acoustic branch and 1 optical branch. For a general 3D unit cell containing _p_ atoms in the basis, there are always exactly **3 acoustic branches** and 3 _p −_ 3 **optical branches** . 

### **7. Standard Textbook Systems** 

-  **The 1D Monatomic Chain:** The standard model demonstrating acoustic wave dispersion and Brillouin zone boundaries. 

-  **The 1D Diatomic Chain (GaAs-like):** Demonstrates the formation of the optical branch and the forbidden frequency band gap, which allows materials to absorb infrared light at the resonant optical frequency. 

17 

GATE PHYSICS 

SOLID STATE PHYSICS 

## **References** 

1. Kittel, Charles. _Introduction to Solid State Physics_ . Wiley, 2005. 

2. Pillai, S. O. _Solid State Physics_ . New Age International, 2018. 

18 

GATE PHYSICS 

ELECTRONIC BANDS IN SOLIDS 

# **GATE PHYSICS STUDY NOTES Free Electron Theory & Band Theory of Solids** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

|**Contents**||
|---|---|
|**1**<br>**The Free Electron Theory of Metals**|**2**|
|**2**<br>**The Band Theory of Solids**|**6**|
|**3**<br>**The Nearly Free Electron Model**|**9**|
|**4**<br>**Distinction Between Metals, Semiconductors, and Insulators**|**12**|



1 

GATE PHYSICS 

ELECTRONIC BANDS IN SOLIDS 

## **1 The Free Electron Theory of Metals** 

### **1. Core Theory** 

The **free electron theory** describes the behavior of conduction electrons in metallic solids. 

-  **Classical Free Electron Theory (Drude-Lorentz Model):** Treats conduction electrons as a classical gas of non-interacting particles moving through a periodic lattice of positive ion cores. The electrons are assumed to obey Maxwell-Boltzmann statistics, colliding only occasionally with ion cores to establish thermal equilibrium. 

-  **Quantum Free Electron Theory (Sommerfeld Model):** Replaces classical statistics with quantum mechanics. Conduction electrons are modeled as non-interacting fermions trapped in a 3D infinite potential well (the metal boundary). They are governed by the Schr¨odinger equation and must satisfy the Pauli exclusion principle, meaning they obey FermiDirac statistics. At _T_ = 0 K, they fill energy states up to a maximum limiting energy, the **Fermi Energy (** _EF_ **)** . 

The physical origin of this theory is the high delocalization of valence electrons in metallic bonds, where the atomic outer orbitals overlap so strongly that valence electrons are pulled away from parent nuclei, becoming free to wander throughout the entire crystal volume. 

### **2. Mathematical Framework** 

* **The 3D Schr¨odinger Equation (Free Particle):** 



<!-- Start of picture text -->
− ℏ2<br>2 m ∇ 2 ψ ( r ) =  Eψ ( r ) (1)<br><!-- End of picture text -->

* **Allowed Wave Vectors (k):** Under periodic boundary conditions over a cube of side _L_ ( _V_ = _L_<sup>3</sup> ): 



<!-- Start of picture text -->
kx = 2 πnx , ky = 2 πny , kz = 2 πnz ( ni ∈{ 0 , ± 1 , ± 2 , . . . } ) (2)<br>L L L<br><!-- End of picture text -->

* **Energy Eigenvalues:** 



<!-- Start of picture text -->
E ( k ) = ℏ2 k 2 x +  k y 2 +  k z 2) (3)<br>2 m = 2 ℏ m 2 ( k 2<br><!-- End of picture text -->

* **Density of States ( _D_ ( _E_ ) or _g_ ( _E_ )):** The number of electron states per unit energy range per unit volume: 



<!-- Start of picture text -->
D ( E ) = V E (4)<br>2 π 2 � 2ℏ m 2 �3 / 2 √<br><!-- End of picture text -->

* **Fermi Energy ( _EF_ ) at _T_ = 0 K:** 



<!-- Start of picture text -->
EF = ℏ2 �3 π 2 n �2 / 3 (5)<br>2 m<br><!-- End of picture text -->

where _n_ = _N/V_ is the free electron carrier concentration (number density). * **Fermi Wave Vector ( _kF_ ) and Fermi Velocity ( _vF_ ):** 



<!-- Start of picture text -->
kF = �3 π 2 n �1 / 3  , vF = ℏ kF (6)<br>m<br><!-- End of picture text -->

2 

GATE PHYSICS 

ELECTRONIC BANDS IN SOLIDS 

* **Fermi Temperature ( _θF_ ):** 



<!-- Start of picture text -->
θF ≡ EF (7)<br>kB<br><!-- End of picture text -->

* **Fermi-Dirac Distribution Function ( _f_ ( _E_ )):** The probability that an electron state of energy _E_ is occupied at temperature _T_ : 



<!-- Start of picture text -->
1<br>f ( E ) = (8)<br>e ( E−µ ) /kBT + 1<br><!-- End of picture text -->

where _µ_ is the chemical potential (at _T_ = 0 K, _µ ≡ EF_ ). 

### **3. Derivation Milestones** 

The derivation of the quantum density of states and Fermi energy proceeds through these critical mathematical milestones: 

1. **Wave Vector Space Volume Element:** Each allowed state occupies a volume element in _k_ -space of: 



<!-- Start of picture text -->
Vk = = 8 π 3 (9)<br>� 2 Lπ �3 V<br><!-- End of picture text -->

2. **State Counting in** _k_ **-Space Sphere:** The number of allowed states _N_ ( _k_ ) within a sphere in _k_ -space of radius _k_ , accounting for electron spin degeneracy ( _gs_ = 2): 



<!-- Start of picture text -->
N ( k ) = 2  × VolumeVolumeofofsingle k -spherestate = 2  × 438 πk π 3 3 = 3 V π 2 k 3 (10)<br>V<br><!-- End of picture text -->

3. **Fermi Energy Quantization (** _T_ = 0 **K):** At absolute zero, all electrons occupy the lowest available states up to the Fermi wave vector _kF_ . Setting the total number of electrons equal to _N_ ( _kF_ ): 



<!-- Start of picture text -->
N = 3 V π 2 k F 3 = ⇒ kF = �3 π 2 N V �1 / 3 = �3 π 2 n �1 / 3 (11)<br><!-- End of picture text -->

Substituting _kF_ into the free-particle energy expression yields _EF_ : 



<!-- Start of picture text -->
EF = ℏ2 k F 2 �3 π 2 n �2 / 3 (12)<br>2 m = 2 ℏ m 2<br><!-- End of picture text -->

4. **Density of States Derivation:** By relating the number of states to the energy interval ( _N_ = �0 _E_<sup>_D_(</sup><sup>_E′_)</sup><sup>_dE′_),differentiate</sup><sup>_N_(</sup><sup>_E_)withrespectto</sup><sup>_E_:</sup> 



<!-- Start of picture text -->
N ( E ) = V = ⇒ D ( E ) = dN ( E ) = V E (13)<br>3 π 2 � 2 mE ℏ 2 �3 / 2 dE 2 π 2 � 2ℏ m 2 �3 / 2 √<br><!-- End of picture text -->

3 

GATE PHYSICS 

ELECTRONIC BANDS IN SOLIDS 

### **4. Problem-Solving Algorithm** 

#### **Algorithm for Free Electron Calculations** 

1. **Calculate Electron Concentration (** _n_ **):** Given the metal’s density ( _ρ_ ), molar mass ( _Ma_ ), and valence ( _v_ ), calculate the free electron density: 



<!-- Start of picture text -->
n  = ρ · NA · v (in electrons/m 3 ) (14)<br>Ma<br><!-- End of picture text -->

2. **Calculate the Fermi Wave Vector (** _kF_ **):** 



<!-- Start of picture text -->
kF = (3 π 2 n ) 1 / 3 (in m − 1 ) (15)<br><!-- End of picture text -->

3. **Calculate the Fermi Energy (** _EF_ **):** 



<!-- Start of picture text -->
F<br>EF = ℏ2 k 2 (in Joules) (16)<br>2 me<br><!-- End of picture text -->

Divide by 1 _._ 602 _×_ 10<sup>_−_19</sup> J/eV to express the final answer in electron-volts (eV). Typical metallic values range from 1 _._ 5 to 12 eV. 

4. **Calculate Fermi Velocity (** _vF_ **) and Temperature (** _θF_ **):** 



<!-- Start of picture text -->
vF = ℏ kF ≈ 10 6 m/s , θF = EF ≈ 10 4 K (17)<br>me kB<br><!-- End of picture text -->

### **5. Connections to Macroscopic Observables** 

* **Electronic Specific Heat (** _C_ **el):** Classical theory predicted _C_ el = 2<sup><u>3</u></sup><sup>_R_, violating room-temperature</sup> measurements. Quantum theory explains that only a tiny fraction of electrons near the Fermi surface ( _∼ T/θF_ ) can absorb thermal energy, yielding the linear linear specific heat capacity: 



<!-- Start of picture text -->
C el = π 2 2 R � θTF � ∝ T (18)<br><!-- End of picture text -->

* **Electrical Conductivity (** _σc_ **):** Sommerfeld replaced Drude’s classical velocity with the Fermi velocity _vF_ : 



<!-- Start of picture text -->
σc = ne 2 τ (19)<br>m<br><!-- End of picture text -->

where the relaxation time is determined by scattering at the Fermi surface: _τ_ = _λ_ mfp _/vF_ . * **Pauli Paramagnetism:** The magnetic susceptibility ( _χ_ ) of metals is small, positive, and nearly independent of temperature because only electrons within _kBT_ of the Fermi level can align their spins parallel to an external field: 



<!-- Start of picture text -->
χP ≈ µ 0 µ 2 B D ( EF ) (20)<br><!-- End of picture text -->

4 

GATE PHYSICS 

ELECTRONIC BANDS IN SOLIDS 

### **6. Crucial Pitfalls** 

#### **Free Electron Theory Pitfalls** 

-  **Dimensionality Errors in** _D_ ( _E_ ) **:** Assuming _D_ ( _E_ ) _∝_ _~~√~~ E_ in all systems. This is true ONLY for 3D bulk metals. 

      - **2D systems (Quantum Wells):** _D_ ( _E_ ) is constant, independent of energy: _D_ 2 _D_ ( _E_ ) = _πm_ ℏ<sup>2.</sup> 

   - **1D systems (Quantum Wires):** _D_ ( _E_ ) _∝ E_<sup>_−_1</sup><sup>_/_2</sup> (diverges at the band edge). 

   - Always check the dimensionality of the system in the GATE question before selecting a formula. 

-  **Confusing Chemical Potential with Fermi Energy:** Assuming _µ_ = _EF_ at all _<u>kBT</u>_ 

- temperatures. _µ_ decreases slightly with temperature: _µ_ ( _T_ ) _≈ EF_ 1 _−_<sup>_<u>π</u>_</sup> 12<sup>2</sup> � _EF_ . � �2<sup>�</sup> 

### **7. Standard Textbook Systems** 

* **Metallic Sodium (Na):** A monovalent Alkali metal ( _v_ = 1, BCC structure) where the single outer 3 _s_ electron is highly delocalized, forming an almost perfect 3D free-electron gas with _EF ≈_ 3 _._ 2 eV. * **The 2D Electron Gas (2DEG) in AlGaAs/GaAs Heterostructures:** A physical setup where conduction electrons are restricted to an ultra-thin planar interface, forming a 2D quantum well system with a constant density of states. 

5 

GATE PHYSICS 

ELECTRONIC BANDS IN SOLIDS 

## **2 The Band Theory of Solids** 

### **1. Core Theory** 

While the free electron theory successfully describes many metallic properties, it fails to explain why some solids are insulators or semiconductors. The **band theory of solids** resolves this by incorporating the **periodic electrostatic potential** of the crystal lattice. * **Physical Origin:** Conduction electrons do not move through a flat vacuum but through a periodic potential _V_ ( **r** + **R** ) = _V_ ( **r** ) generated by the positively charged ion cores. This periodic potential breaks the continuous free-particle parabola into discrete **energy bands** separated by **forbidden energy gaps (band gaps)**. * **Bloch’s Theorem:** Assumes that the eigenfunctions of a Schr¨odinger equation with a periodic potential are not plane waves, but plane waves modulated by a periodic function of the same lattice periodicity: 



<!-- Start of picture text -->
ψ k ( r ) =  u k ( r ) e i k · r where u k ( r  +  R ) =  u k ( r ) (21)<br><!-- End of picture text -->

* **The Kronig-Penney Model:** An idealized 1D mathematical model that replaces the real atomic periodic potential with a periodic array of rectangular potential barriers. It demonstrates analytically how periodic boundaries force the formation of allowed energy bands and forbidden gaps. 

### **2. Mathematical Framework** 

* **Periodic Potential Constraint:** 



<!-- Start of picture text -->
V  ( x  +  a ) =  V  ( x ) (where a is the lattice constant) (22)<br><!-- End of picture text -->



<!-- Start of picture text -->
* Bloch Wave Function (1D):<br><!-- End of picture text -->



<!-- Start of picture text -->
ψk ( x ) =  uk ( x ) e ikx where uk ( x  +  a ) =  uk ( x ) (23)<br><!-- End of picture text -->

An equivalent statement of Bloch’s theorem is: 



<!-- Start of picture text -->
ψk ( x  +  a ) =  ψk ( x ) e ika (24)<br><!-- End of picture text -->

* **Kronig-Penney Transcendental Dispersion Equation:** By modeling the barriers as Dirac delta functions of strength _P_ (where _P_ = lim _b→_ 0 _,V_ 0 _→∞_<sup>_<u>mV</u>_</sup> ℏ<sup><u>02</u></sup><sup>_<u>ba</u>_</sup> ): 



<!-- Start of picture text -->
P sin( αa ) + cos( αa ) = cos( ka ) (25)<br>αa<br><!-- End of picture text -->

where: * ** _P_ ** is the ”barrier strength” or ”binding energy” parameter. * ** _a_ ** is the periodic lattice spacing. * ** _k_ ** is the crystal wave vector ( _k ∈_ [ _−π/a, π/a_ ] in the first Brillouin zone). * ** _α_ ** is related to the energy of the electron: 



<!-- Start of picture text -->
√ 2 mE<br>α  = (26)<br>ℏ<br><!-- End of picture text -->

### **3. Derivation Milestones** 

The derivation of the Kronig-Penney dispersion relation relies on these milestones: 

6 

GATE PHYSICS 

ELECTRONIC BANDS IN SOLIDS 

1. **Segmenting the Piecewise Potential:** Divide the 1D space into a potential well of width _a_ ( _V_ = 0 for 0 _< x < a_ ) and a barrier of width _b_ ( _V_ = _V_ 0 for _−b < x <_ 0). Write the TISE in both zones: 



<!-- Start of picture text -->
ψI ( x ) =  Ae iαx +  Be −iαx (0  < x < a ) (27)<br><!-- End of picture text -->



<!-- Start of picture text -->
� 2 m ( V 0  − E )<br>ψII ( x ) =  Ce βx +  De −betax ( −b < x <  0) β = (28)<br>ℏ<br>� �<br><!-- End of picture text -->

2. **Enforcing Bloch Boundary Conditions:** Apply Bloch’s theorem to express the boundary conditions at _x_ = _a_ in terms of the values at _x_ = _−b_ : 



<!-- Start of picture text -->
ψI ( a ) =  ψII ( −b ) e ik ( a + b ) , ψI ′ ( a ) =  ψ II ′ ( −b ) eik ( a + b ) (29)<br><!-- End of picture text -->

3. **The Boundary Matching Matrix:** Match wave function and derivative continuity at the boundaries _x_ = 0 and _x_ = _a_ . This yields a set of four linear equations for the constants _A, B, C, D_ . For a non-trivial solution to exist, the determinant of the coefficients must vanish. 

4. **The Delta-Function Limit:** To simplify the dense transcendental determinant, take the limit as the barrier width _b →_ 0 and height _V_ 0 _→∞_ such that the product _V_ 0 _b_ remains constant. This collapses the complex determinant to the Kronig-Penney relation: 



<!-- Start of picture text -->
P sin( αa ) + cos( αa ) = cos( ka ) (30)<br>αa<br><!-- End of picture text -->

### **4. Problem-Solving Algorithm** 

#### **Analyzing Allowed and Forbidden Bands in Kronig-Penney Problems** 

1. **Formulate the Boundary Bounds:** Let the left-hand side of the Kronig-Penney equation be defined as the function: 



<!-- Start of picture text -->
F ( αa )  ≡ P sin( αa ) + cos( αa ) (31)<br>αa<br><!-- End of picture text -->

2. **Apply the Right-Hand Side Constraint:** Since the right-hand side is cos( _ka_ ), and the cosine function is mathematically bounded by _±_ 1 for real wave vectors _k_ : 



<!-- Start of picture text -->
|F ( αa ) | ≤ 1 = ⇒− 1  ≤ P sin( αa ) + cos( αa )  ≤ 1 (32)<br>αa<br><!-- End of picture text -->

3. **Identify Allowed Energies:** Calculate the values of _αa_ (and thus energies _E_ ) for which _|F_ ( _αa_ ) _| ≤_ 1. These ranges represent the **allowed energy bands**. 

4. **Identify Forbidden Band Gaps:** Identify the zones where _|F_ ( _αa_ ) _| >_ 1. In these regions, the wave vector _k_ becomes complex, meaning waves decay exponentially; these represent **forbidden band gaps**. 

### **5. Connections to Macroscopic Observables** 

* **Lifting of Free-Particle Degeneracy:** The Kronig-Penney model proves that as the barrier strength _P →∞_ (isolated atoms), the allowed bands contract to infinitely sharp atomic energy 

7 

GATE PHYSICS 

ELECTRONIC BANDS IN SOLIDS 

levels: _αa_ = _nπ_ = _⇒ En_ =<sup>_<u>n</u>_</sup> 2<sup>2</sup> _ma_<sup>_<u>π</u>_2ℏ22.*</sup><sup>**RecoveryofFreeElectronBehavior:**As</sup><sup>_P→_0</sup> (weak potential, free space), the gaps vanish, and we recover the continuous free-electron parabola: cos( _αa_ ) = cos( _ka_ ) = _⇒ α_ = _k_ = _⇒ E_ =<sup><u>ℏ</u></sup> 2<sup>2</sup> _m_<sup>_<u>k</u>_2.</sup> 

### **6. Crucial Pitfalls** 

#### **Kronig-Penney Model Traps** 

-  **Assuming Constant Band Gap Widths:** Assuming that all band gaps are of equal size. As energy _E_ increases (larger _αa_ ), the term _P_<sup>sin</sup> _αa_<sup><u>(</u></sup><sup>_αa_</sup><sup><u>)</u></sup> decays to zero because _αa_ is in the denominator. Consequently, the allowed bands become **wider** and the forbidden band gaps become **narrower** at higher energies. 

-  **Sign Errors in the Transcendental Function:** Ensure you calculate the function using the correct signs: _P_<sup>sin</sup> _αa_<sup><u>(</u></sup><sup>_αa_</sup><sup><u>)</u></sup> **+** cos( _αa_ ). A negative sign will reverse allowed and forbidden zones. 

### **7. Standard Textbook Systems** 

* **The Delta-Function Potential Comb:** An infinite 1D periodic array of attractive or repulsive Dirac delta functions, used to solve for the dispersion curves of a 1D crystal lattice. * **The Empty Lattice Model:** A cubic crystal where the periodic potential is set to zero ( _V_ 0 _→_ 0), used to map free-particle dispersion curves folded back into the first Brillouin zone. 

8 

GATE PHYSICS 

ELECTRONIC BANDS IN SOLIDS 

## **3 The Nearly Free Electron Model** 

### **1. Core Theory** 

The **nearly free electron model** describes the behavior of conduction electrons in a weak periodic lattice potential. * **Physical Origin:** Unlike the Kronig-Penney model, which handles arbitrary potential strengths, the nearly free electron model treats the periodic potential _V_ ( **r** ) as a very small perturbation relative to the free-electron kinetic energy. * **Bragg Reflection in** _k_ **-Space:** Away from the Brillouin zone boundaries, the weak potential has negligible effect, and the electrons behave like free particles. However, when the electron wave vector **k** is close to a Brillouin zone boundary, the electron wave satisfies the Bragg diffraction condition ( **k** _·_ **G** = 2<sup><u>1</u></sup><sup>_G_2).At this critical</sup> point, the incident wave and the Bragg-reflected wave undergo constructive interference, forming a standing wave. * **Band Gap Formation:** The standing wave can have its maximum density either on top of the positive ion cores (minimizing energy) or between them (maximizing energy). This split in potential energy at the zone boundary lifts the degeneracy of the free-electron states, opening up a **forbidden band gap**. 

### **2. Mathematical Framework** 

* **Weak Periodic Potential Expansion:** The periodic potential is expanded as a Fourier series in reciprocal lattice vectors **G** : 



<!-- Start of picture text -->
V  ( r ) = � U G e i G · r (33)<br><!-- End of picture text -->

##### **G** 

where the Fourier coefficients _U_ **G** represent the strength of the potential components. * **Standing Wave Configurations (1D, Zone Boundary** _k_ = _π/a_ **):** The two orthogonal standing wave combinations are: 



<!-- Start of picture text -->
ψ +( x )  ∝ cos (maximum probability density at x  = 0 , a, . . . [ion sites]) (34)<br>� πxa �<br>ψ− ( x )  ∝ sin (maximum probability density at x  =  a/ 2 ,  3 a/ 2  . . . [midpoints]) (35)<br>� πxa �<br><!-- End of picture text -->

* **Band Gap Magnitude (** _Eg_ **):** The energy gap opened at the first Brillouin zone boundary ( _k_ = _±π/a_ ) is twice the absolute value of the corresponding Fourier coefficient of the potential: 



<!-- Start of picture text -->
Eg = 2 |UG|  = 2 |Uπ/a| (36)<br><!-- End of picture text -->

* **Effective Mass (** _m_<sup>_∗_</sup> **):** Inside a crystal band, the electron’s curvature deviates from the freeelectron mass. It is governed by the curvature of the dispersion curve: 



<!-- Start of picture text -->
1 d 2 E<br>(37)<br>m ∗ ≡ ℏ 12 dk 2<br><!-- End of picture text -->

### **3. Derivation Milestones** 

The opening of the band gap in the nearly free electron model is derived as follows: 

1. **Degenerate State Formulation:** At the first Brillouin zone boundary _k_ = _π/a_ , the two free-particle plane-wave states _e_<sup>_iπx/a_</sup> and _e_<sup>_−iπx/a_</sup> are degenerate, sharing the same energy _E_<sup>0</sup> =<sup><u>ℏ2</u></sup><sup>_<u>π</u>_2</sup> 2 _ma_<sup>2.</sup> 

9 

GATE PHYSICS 

ELECTRONIC BANDS IN SOLIDS 

2. **Standing Wave Probability Densities:** Normalize the two standing wave configurations: 



<!-- Start of picture text -->
= 1 + cos (38)<br>|ψ +( x ) | 2 = 2 cos 2 � πx a � � 2 πxa �<br><!-- End of picture text -->



<!-- Start of picture text -->
= 1  − cos (39)<br>|ψ− ( x ) | 2 = 2 sin 2 � πx a � � 2 πxa �<br><!-- End of picture text -->

3. **First-Order Perturbation Integration:** Treat the weak periodic potential _V_ ( _x_ ) = _U_ cos � <u>2</u> _<u>πxa</u>_ � as a perturbation. Calculate the first-order energy corrections for both states: 



<!-- Start of picture text -->
E + =  E 0 + |ψ +( x ) | 2 V  ( x ) dx  =  E 0 +  U (40)<br>�0 a<br>E− =  E 0 + |ψ− ( x ) | 2 V  ( x ) dx  =  E 0 − U (41)<br>�0 a<br><!-- End of picture text -->

4. **Energy Split (Band Gap):** The potential energy difference between the two configurations represents the band gap: 



<!-- Start of picture text -->
Eg =  E +  − E− = ( E 0 +  U )  − ( E 0 − U ) = 2 U (42)<br><!-- End of picture text -->

### **4. Problem-Solving Algorithm** 

#### **Calculating Effective Mass and Band Gaps** 

1. **Identify the Dispersion Relation:** Write out the given _E_ ( _k_ ) relation (e.g., _E_ ( _k_ ) = _Ak_<sup>2</sup> + _Bk_<sup>4</sup> ). 

2. **Compute the Second Derivative:** Differentiate the energy with respect to _k_ twice: 



<!-- Start of picture text -->
dE<br>(43)<br>dk = 2 Ak  + 4 Bk 3 = ⇒ d dk 2 E 2 = 2 A  + 12 Bk 2<br><!-- End of picture text -->

3. **Calculate Effective Mass (** _m_<sup>_∗_</sup> **):** 



<!-- Start of picture text -->
ℏ 2<br>=<br>m ∗ ( k ) = d ℏ22 E 2 A  + 12 Bk 2 (44)<br>dk 2<br><!-- End of picture text -->

4. **Identify Physical States based on** _m_<sup>_∗_</sup> **Sign:** 

   -  If _m_<sup>_∗_</sup> _>_ 0 (near the bottom of the band), the electron behaves like a free positive mass particle. 

   -  If _m_<sup>_∗_</sup> _<_ 0 (near the top of the band), the negative mass implies the state behaves physically like a **hole**. 

   -  If<sup>_<u>d</u>_</sup> _dk_<sup>2</sup><sup>_<u>E</u>_2= 0(inflectionpoint),theeffectivemassdivergestoinfinity(</sup><sup>_m∗→∞_).</sup> 

### **5. Connections to Macroscopic Observables** 

* **Optical Absorption Threshold:** A nearly free electron solid is transparent to photons of energy less than the band gap ( _hν < Eg_ ). When _hν ≥ Eg_ , a sharp increase in absorption occurs as electrons are excited across the gap, providing a direct measurement of 2 _|UG|_ . 

10 

GATE PHYSICS 

ELECTRONIC BANDS IN SOLIDS 

### **6. Crucial Pitfalls** 

#### **Nearly Free Electron Traps** 

-  **Effective Mass Sign Confusion:** Forgetting that the effective mass is negative at the top of a band. When calculating carrier dynamics, a negative effective mass under an electric field means the charge carrier accelerates in the direction **opposite** to a free electron, which is mathematically handled by introducing the concept of a positively charged **hole**. 

-  **Assuming Free Mass at all Wave Vectors:** Assuming _m_<sup>_∗_</sup> = _me_ everywhere. _m_<sup>_∗_</sup> deviates significantly from _me_ near Brillouin zone boundaries, where the dispersion curve bends horizontally to meet the zone boundary at a right angle ( _vg_ = 0 = _⇒ m_<sup>_∗_</sup> _→∞_ or negative). 

### **7. Standard Textbook Systems** 

* **Aluminum (Al):** A trivalent metal ( _v_ = 3, FCC structure) where the lattice potential is so weak that its electronic structure is almost perfectly modeled by the nearly free electron approximation, showing tiny band-gap splits at Brillouin zone boundaries. * **The 1D Weak Cosine Potential:** A mathematical model potential _V_ ( _x_ ) = _−_ 2 _U_ 1 cos(2 _πx/a_ ) used in introductory solid state physics to derive the exact 2 _U_ 1 energy splitting at the first Brillouin zone boundary. 

11 

GATE PHYSICS 

ELECTRONIC BANDS IN SOLIDS 

## **4 Distinction Between Metals, Semiconductors, and Insulators** 

### **1. Core Theory** 

The vast differences in electrical conductivities across materials—spanning over 30 orders of magnitude—cannot be explained by classical mechanics. The band theory of solids provides a unified physical explanation based on **band filling** and the magnitude of the **band gap ( _Eg_ )**. * **Physical Origin:** Conduction requires electrons to gain kinetic energy from an external electric field. This means they must transition to nearby, unoccupied momentum states. If a band is completely filled and separated from the next empty band by a large energy gap, electrons cannot transition because there are no available states within reach, rendering the material inert to conduction. * **Metals:** Characterized by a partially filled energy band or overlapping bands. Available empty states lie immediately adjacent to the occupied states, allowing conduction even at _T_ = 0 K under microscopic fields. * **Insulators:** Characterized by a completely filled valence band and a completely empty conduction band, separated by a **large forbidden band gap** ( _Eg >_ 3 eV). Thermal energy at room temperature ( _kBT ≈_ 0 _._ 025 eV) is insufficient to excite electrons across this gap. * **Semiconductors:** Characterized by a filled valence band and empty conduction band at _T_ = 0 K, but with a **small forbidden band gap** ( _Eg ≈_ 1 eV). At room temperature, thermal excitation successfully promotes a small fraction of carriers into the conduction band, leaving behind vacant states ( **holes** ) in the valence band, enabling moderate conduction. 

### **2. Mathematical Framework** 

- **Temperature Dependence of Carrier Concentration (** _n_ **) in Semiconductors:** 



<!-- Start of picture text -->
e kBT<br>n ( T ) =  Nce − ( Ec−EF  ) /kBT = 2 e − ( Ec−EF  ) /kBT (45)<br>� m 2 ∗π ℏ 2 �3 / 2<br><!-- End of picture text -->

- **Intrinsic Carrier Concentration (** _ni_ **):** 



<!-- Start of picture text -->
ni ( T ) = � NcNve −Eg/ 2 kBT = 2 ( m ∗ e m∗ h )3 / 4 e−Eg/ 2 kBT (46)<br>� 2 kπB ℏ T 2 �3 / 2<br>Electrical Conductivity ( σcc ):<br>σc =  e ( nµe  +  pµh ) (47)<br><!-- End of picture text -->

* **Intrinsic Electrical Conductivity (** _σcc_ **):** 

where _µe_ and _µh_ are the electron and hole mobilities, respectively, and for intrinsic materials _n_ = _p_ = _ni_ . 

### **3. Derivation Milestones** 

The temperature-dependent conductivity of semiconductors is derived as follows: 

1. **Valence and Conduction Density of States:** Approximate the bottom of the conduction band and the top of the valence band as parabolic: 



<!-- Start of picture text -->
Dc ( E ) = 1 e E − Ec, Dv ( E ) = 1 h Ev − E (48)<br>2 π 2 � 2ℏ m 2 ∗ �3 / 2 � 2 π 2 � 2ℏ m 2 ∗ �3 / 2 �<br><!-- End of picture text -->

12 

GATE PHYSICS 

ELECTRONIC BANDS IN SOLIDS 

2. **Maxwell-Boltzmann Approximation:** Since the Fermi level _EF_ lies deep inside the band gap, the Fermi-Dirac distribution simplifies to the Maxwell-Boltzmann limit: 



<!-- Start of picture text -->
1<br>f ( E ) = e ( E−EF  ) /kBT + 1 ≈ e− ( E−EF  ) /kBT (49)<br><!-- End of picture text -->

3. **Carrier Concentration Integration:** Integrate the product of the density of states and the occupancy probability: 



<!-- Start of picture text -->
n  = Dc ( E ) f ( E ) dE ≈ Nce − ( Ec−EF  ) /kBT (50)<br>� E∞c<br><!-- End of picture text -->

Similarly, the hole concentration is _p ≈ Nve_<sup>_−_(</sup><sup>_EF −Ev_)</sup><sup>_/kBT_</sup> . 

4. **Intrinsic Fermi Level (** _EF_ **):** For an intrinsic semiconductor, charge neutrality requires _n_ = _p_ = _ni_ . Equating _n_ and _p_ yields the intrinsic Fermi level: 



<!-- Start of picture text -->
h<br>EF = Ec  +  Ev + 3 (51)<br>2 4 kBT ln � mm∗ ∗ e �<br><!-- End of picture text -->

At _T_ = 0 K (or if _m_<sup>_∗_</sup> _e_<sup>=</sup><sup>_m∗_</sup> _h_<sup>),theFermilevelsits**exactlyatthemiddleofthebandgap**.</sup> 

### **4. Problem-Solving Algorithm** 

#### **Algorithm for Semiconductor Carrier Concentrations** 

1. **Find the Intrinsic Concentration (** _ni_ **):** Use the intrinsic relation: _ni ∝ T_<sup>3</sup><sup>_/_2</sup> _e_<sup>_−Eg/_2</sup><sup>_kBT_</sup> (52) 

2. **Analyze Doping (Extrinsic):** 

   -  For N-type doping with donor concentration _Nd_ : _n ≈ Nd_ (assuming complete ionization). 

   -  For P-type doping with acceptor concentration _Na_ : _p ≈ Na_ . 

3. **Apply the Law of Mass Action:** At any given temperature, the product of electron and hole concentrations is constant: 



<!-- Start of picture text -->
n · p  =  n 2 i (53)<br><!-- End of picture text -->

Use this to find the minority carrier concentration (e.g., in N-type: _p_ = _n_<sup>2</sup> _i_<sup>_/Nd_).</sup> 

4. **Calculate Temperature-Dependent Ratios:** For comparative temperature problems: 



<!-- Start of picture text -->
ln ≈ Eg − 1 (54)<br>� nnii 21 � 2 kB � T 12 T 1 �<br><!-- End of picture text -->

### **5. Connections to Macroscopic Observables** 

- **Temperature Dependence of Electrical Resistivity (** _ρ_ **):** 

13 

GATE PHYSICS 

ELECTRONIC BANDS IN SOLIDS 

-  **Metals:** Resistivity **increases** with temperature ( _ρ ∝ T_ ). Lattice vibrations (phonon scattering) increase at higher temperatures, reducing the relaxation time _τ_ . 

-  **Semiconductors:** Resistivity **decreases exponentially** with temperature ( _ρ ∝ e_<sup>_Eg/_2</sup><sup>_kBT_</sup> ). Although scattering increases, the exponential generation of new charge carriers ( _ni_ ) dominates the conductivity. 

### **6. Crucial Pitfalls** 

#### **Material Classification Pitfalls** 

-  **Doping vs. Band Gap Changes:** Assuming that doping a semiconductor changes its band gap. **Doping does NOT alter the band gap width _Eg_ **. It simply introduces discrete donor or acceptor energy levels inside the forbidden gap close to the band edges, and shifts the Fermi level _EF_ toward the conduction (N-type) or valence (Ptype) bands. 

-  **The** _Eg_ **vs.** _Eg/_ 2 **Factor Trap:** Forgetting the factor of 2 in the exponential term of the intrinsic carrier concentration _ni ∝ e_<sup>_−Eg/_2</sup><sup>_kBT_</sup> . The factor of 2 arises because carriers are generated in pairs (one electron and one hole), split across the gap. 

### **7. Standard Textbook Systems** 

* **Intrinsic Silicon (Si):** The classic semiconductor ( _Eg ≈_ 1 _._ 12 eV at room temperature), showing a highly temperature-dependent conductivity. * **Diamond (C):** An allotrope of carbon with a massive band gap ( _Eg ≈_ 5 _._ 5 eV), making it a high-performance insulator. 

14 

GATE PHYSICS 

ELECTRONIC BANDS IN SOLIDS 

## **References** 

1. Kittel, Charles. _Introduction to Solid State Physics_ . Wiley, 2005. 

2. Pillai, S. O. _Solid State Physics_ . New Age International, 2010. 

15 

GATE PHYSICS 

SEMICONDUCTOR PHYSICS & JUNCTIONS 

# **GATE PHYSICS STUDY NOTES Semiconductor Physics & Metal-Semiconductor Junctions** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**|**Electrical Conductivity, Effective Mass, and Mobility**|**2**|
|---|---|---|
|**2**|**Semiconductor Carrier Statistics and the Mass Action Law**|**5**|
|**3**|**Physics of Metal-Semiconductor Junctions: Schottky vs. Ohmic**|**9**|



1 

GATE PHYSICS 

SEMICONDUCTOR PHYSICS & JUNCTIONS 

## **1 Electrical Conductivity, Effective Mass, and Mobility** 

### **1. Core Theory** 

**Electrical conductivity** ( _σ_ ) in solids represents the ease with which charge carriers drift under an applied electric field, reflecting a steady-state balance between field-driven acceleration and dissipative scattering events. 

The physical origin of conductivity is the relaxation of the electron momentum distribution via scattering off lattice vibrations (phonons), impurities, and defects. 

The **effective mass** ( _m_<sup>_∗_</sup> ) is a quantum mechanical concept that encapsulates the influence of the periodic crystal potential on the acceleration of a charge carrier. Rather than solving the complex multi-body forces of all core ions on a conduction electron, the electron is treated as a free-like particle whose inertial response to an external force is modified by the curvature of the electronic energy band. 

**Mobility** ( _µ_ ) measures the drift velocity attained by a charge carrier per unit of applied electric field. It acts as the direct physical bridge linking microscopic scattering parameters (relaxation time _τc_ and band structure curvature _m_<sup>_∗_</sup> ) to macroscopic electrical current flow. 

### **2. Mathematical Framework** 



<!-- Start of picture text -->
 Effective Mass Formulation:<br>1 d 2 E<br>(1)<br>m ∗ ≡ ℏ 12 dk 2<br><!-- End of picture text -->

where _m_<sup>_∗_</sup> is the effective mass of the charge carrier, ℏ is the reduced Planck constant, _E_ ( _k_ ) is the dispersion relation of the energy band, and _k_ is the wave vector. 

####  **Mobility (** _µ_ **):** 



<!-- Start of picture text -->
µ  = eτc (2)<br>m ∗<br><!-- End of picture text -->

where _e_ is the elementary charge, _τc_ is the mean collision relaxation time, and _m_<sup>_∗_</sup> is the effective mass of the carrier. The drift velocity **v** _d_ is related to the applied electric field **E** by: 



<!-- Start of picture text -->
v d =  µ E (3)<br><!-- End of picture text -->

####  **Electrical Conductivity (** _σ_ **):** 



<!-- Start of picture text -->
σ =  neµe  +  peµh (4)<br><!-- End of picture text -->

where _n_ and _p_ are the electron and hole concentrations, and _µe_ and _µh_ are their respective mobilities. For a single-carrier metal, this simplifies to: 



<!-- Start of picture text -->
σ =  neµe = ne 2 τc (5)<br>m ∗ e<br><!-- End of picture text -->

### **3. Derivation Milestones** 

1. **Semiclassical Equation of Motion:** Express the acceleration of a Bloch wave packet under an external electric force _F_ = _−eE_ : 



<!-- Start of picture text -->
F = dp (6)<br>dt = ℏ dk dt<br><!-- End of picture text -->

2 

GATE PHYSICS 

SEMICONDUCTOR PHYSICS & JUNCTIONS 



<!-- Start of picture text -->
2. Evaluating Group Velocity Acceleration: Differentiate the group velocity vg = ℏ 1 dEdk<br>with respect to time:<br>a  = dvg d = 1 d 2 E dk (7)<br>dt = ℏ 1 dt � dEdk � ℏ dk 2 dt<br><!-- End of picture text -->

3. **Extracting Effective Mass:** Substitute<sup>_<u>dk</u>_</sup> _dt_<sup>=</sup><sup>_<u>F</u>_</sup> ℏ<sup>intotheaccelerationequation:</sup> 



<!-- Start of picture text -->
a  = d 2 E F ≡ F 1 d 2 E (8)<br>� ℏ1 2 dk 2 � m ∗ = ⇒ m ∗ = ℏ 12 dk 2<br><!-- End of picture text -->

This demonstrates that the effective mass is inversely proportional to the second derivative of the energy band curvature. 

4. **Drift Current and Conductivity:** Set up the steady-state drift velocity under a scattering force modeled by the relaxation time approximation: 



<!-- Start of picture text -->
m ∗ vd =  eEτc = ⇒ vd = E =  µE (9)<br>� meτ ∗ c �<br><!-- End of picture text -->

Using the current density relation _J_ = _nevd_ = _σE_ yields the conductivity equation _σ_ = _neµ_ . 

### **4. Problem-Solving Algorithm** 

#### **Calculating Effective Mass and Conductivity** 

1. **Isolate the Dispersion Relation:** Look for the given energy dispersion function _E_ ( _k_ ), which is often presented as a cosine expansion (tight-binding model), e.g., _E_ ( _k_ ) = _E_ 0 _− A_ cos( _ka_ ). 

2. **Calculate the Second Derivative:** Differentiate _E_ ( _k_ ) twice with respect to _k_ : 



<!-- Start of picture text -->
dE<br>(10)<br>dk =  Aa  sin( ka ) = ⇒ d dk 2 E 2 =  Aa 2 cos( ka )<br><!-- End of picture text -->

3. **Solve for Effective Mass:** Substitute the second derivative into the mass equation: 



<!-- Start of picture text -->
ℏ 2 ℏ 2<br>m ∗ ( k ) = (11)<br>d 2 E/dk 2 = Aa 2 cos( ka )<br><!-- End of picture text -->

_Note: At the bottom of the band (k_ = 0 _), m_<sup>_∗_</sup> = _Aa_ <u>ℏ</u><sup>22</sup><sup>_>_0</sup><sup>_(electron-like).Atthetopof_</sup> _the band (k_ = _π/a), m_<sup>_∗_</sup> = _− Aa_<sup><u>ℏ22</u></sup><sup>_<_0</sup><sup>_(hole-like)._</sup> 

4. **Compute Conductivity/Mobility:** Substitute the calculated mass, carrier concentration, and relaxation time into _µ_ = _eτc/m_<sup>_∗_</sup> and _σ_ = _neµ_ to solve for macroscopic parameters. 

### **5. Connections to Macroscopic Observables** 

-  **Temperature Dependency of Conductivity (Semiconductors vs. Metals):** 

3 

GATE PHYSICS 

SEMICONDUCTOR PHYSICS & JUNCTIONS 

- **Metals:** The carrier concentration _n_ is constant. As temperature _T_ increases, lattice vibrations (phonons) increase, reducing the relaxation time _τc ∝ T_<sup>_−_1</sup> . Thus, mobility and conductivity decrease with temperature, resulting in a positive temperature coefficient of resistance ( _ρ ∝ T_ ). 

- **Semiconductors:** The carrier concentration _n_ ( _T_ ) increases exponentially with temperature due to thermal excitation across the band gap, completely dominating the powerlaw decrease of mobility. Thus, semiconductor conductivity increases exponentially with temperature, resulting in a negative temperature coefficient of resistance. 

### **6. Crucial Pitfalls** 

#### **Effective Mass and Mobility Traps to Avoid** 

-  **Confusing Phase Velocity with Group Velocity:** Remember that the velocity of an electron wave packet is the group velocity _vg_ = ℏ<sup><u>1</u></sup> _<u>dEdk</u>_<sup>, not the phase velocity</sup><sup>_E/_(ℏ</sup><sup>_k_).</sup> 

-  **Sign of Effective Mass at Band Boundaries:** Neglecting the cosine sign in the tight-binding model. The effective mass becomes strictly negative near the top of the Brillouin zone. A negative effective mass physically represents a state where momentum transfer from the lattice ions during Bragg scattering accelerates the electron in the opposite direction of the applied external force; this is modeled as a positive hole with a positive effective mass. 

-  **Ignoring the Mass-Scaling of Mobility:** Assuming a lighter effective mass results in lower mobility. Since _µ ∝_ 1 _/m_<sup>_∗_</sup> , carriers with highly curved, sharp bands (e.g., electrons in GaAs, _m_<sup>_∗_</sup> _e_<sup>_≈_0</sup><sup>_._067</sup><sup>_m_0)exhibitexceptionallyhighmobilitiescomparedto</sup> heavy, flat bands. 

### **7. Standard Textbook Systems** 

-  **The Tight-Binding 1D Chain:** A system with dispersion relation _E_ ( _k_ ) = _E_ 0 _−_ 2 _t_ cos( _ka_ ), where _t_ is the overlap transfer integral and _a_ is the lattice constant. This serves as the primary system to illustrate how the effective mass scales from positive to infinite (at the inflection point _ka_ = _π/_ 2) and finally to negative values at the zone boundaries. 

-  **Conduction Band of Gallium Arsenide (GaAs):** An isotropic, direct-gap semiconductor with a highly curved conduction band minimum at _k_ = 0, resulting in a very light effective mass ( _m_<sup>_∗_</sup> _≈_ 0 _._ 067 _m_ 0) and exceptionally high electron mobility. 

4 

GATE PHYSICS 

SEMICONDUCTOR PHYSICS & JUNCTIONS 

## **2 Semiconductor Carrier Statistics and the Mass Action Law** 

### **1. Core Theory** 

Semiconductor statistics describe the equilibrium distribution of charge carriers (electrons in the conduction band, holes in the valence band) as a function of temperature and doping concentration. 

The physical origin is the **Fermi-Dirac distribution** , which dictates the probability that a quantum state of energy _E_ is occupied by a fermion (electron) at thermodynamic temperature _T_ . 

In an **intrinsic (pure) semiconductor** , charge carriers are created solely by the thermal excitation of electrons from the valence band to the conduction band, creating exactly equal numbers of electrons and holes ( _n_ 0 = _p_ 0 = _ni_ ). 

In an **extrinsic (doped) semiconductor** , the introduction of donor (n-type) or acceptor (ptype) impurities introduces localized energy levels close to the band edges. This breaks the carrier balance, causing one carrier type to dominate. 

Despite these drastic concentration shifts, the product of electron and hole concentrations remains a thermodynamic constant at a given temperature, governed by the **Law of Mass Action** . 

### **2. Mathematical Framework** 

-  **Fermi-Dirac Distribution Function (** _f_ ( _E_ ) **):** 



<!-- Start of picture text -->
1<br>f ( E ) = (12)<br>1 +  e ( E−EF  ) /kBT<br><!-- End of picture text -->

where _EF_ is the **Fermi Energy Level** (representing the chemical potential of the electron system) and _kB_ is the Boltzmann constant. 

-  **Carrier Concentration Equations:** Under the Maxwell-Boltzmann approximation ( _E − EF ≫ kBT_ in the conduction band), the thermal equilibrium concentrations are: 



<!-- Start of picture text -->
n 0 =  NCe − ( EC −EF  ) /kBT (13)<br><!-- End of picture text -->



<!-- Start of picture text -->
p 0 =  NV e − ( EF −EV  ) /kBT (14)<br><!-- End of picture text -->

where _EC_ and _EV_ are the conduction and valence band edges, and _NC_ and _NV_ are the **Effective Density of States** at the band edges: 



<!-- Start of picture text -->
e kBT h kBT<br>NC = 2 , NV = 2 (15)<br>� 2 πmh∗ 2 �3 / 2 � 2 πmh∗ 2 �3 / 2<br><!-- End of picture text -->

-  **The Law of Mass Action:** 



<!-- Start of picture text -->
n 0 p 0 =  n 2 i =  NCNV e−Eg/kBT (16)<br><!-- End of picture text -->

where _Eg_ = _EC − EV_ is the band gap energy. The **intrinsic carrier concentration** is: 



<!-- Start of picture text -->
ni = � NCNV e −Eg/ 2 kBT (17)<br><!-- End of picture text -->

-  **Fermi Level Positioning (** _EF_ **):** 

   - _Intrinsic semiconductor:_ 



<!-- Start of picture text -->
h<br>EFi = EC +  EV + 3 (18)<br>2 4 kBT ln � mm∗ ∗ e �<br><!-- End of picture text -->

5 

GATE PHYSICS 

SEMICONDUCTOR PHYSICS & JUNCTIONS 

**–** _Extrinsic n-type semiconductor (doping ND):_ 



<!-- Start of picture text -->
EF =  EC − kBT ln (19)<br>� NNDC �<br><!-- End of picture text -->

**–** _Extrinsic p-type semiconductor (doping NA):_ 



<!-- Start of picture text -->
EF =  EV +  kBT ln (20)<br>� NNVA �<br><!-- End of picture text -->

### **3. Derivation Milestones** 

1. **Integrating Conduction Band Carrier Density:** Express the electron concentration as the integral over the conduction band of the product of the density of states _DC_ ( _E_ ) and the Fermi-Dirac distribution _f_ ( _E_ ): 



<!-- Start of picture text -->
4 π (2 m ∗ e )3 / 2 1<br>n 0 = DC ( E ) f ( E ) dE = � E − EC dE (21)<br>� E∞C � E∞C h 3 � 1 +  e ( E−EF  ) /kBT �<br><!-- End of picture text -->

2. **Applying the Maxwell-Boltzmann Approximation:** Assume the Fermi level is in the band gap and far from _EC_ by at least 3 _kBT_ . This simplifies the Fermi-Dirac distribution to the exponential Boltzmann tail: 



<!-- Start of picture text -->
e )3 / 2<br>n 0 ≈ 4 π (2 m∗ e − ( EC −EF  ) /kBT � E − ECe − ( E−EC ) /kBT dE (22)<br>h 3 � E∞C<br><!-- End of picture text -->

3. **Evaluating the Gamma Integral:** Set up a dimensionless variable _x_ = ( _E − EC_ ) _/kBT_ : 



<!-- Start of picture text -->
√ π<br>x 1 / 2 e −x dx  = Γ(3 / 2) = (23)<br>�0 ∞ 2<br><!-- End of picture text -->

Substituting this integral recovers the final carrier concentration formula: _n_ 0 = _NCe_<sup>_−_(</sup><sup>_EC−EF_)</sup><sup>_/kBT_</sup> . 

4. **Thermodynamic Product Invariance (Mass Action):** Multiply the analytical expressions for _n_ 0 and _p_ 0: 



<!-- Start of picture text -->
n 0 p 0 = =  NCNV e − ( EC −EV  ) /kBT =  n 2 i (24)<br>� NCe − ( EC −EF  ) /kBT  �� NV e − ( EF −EV  ) /kBT  �<br><!-- End of picture text -->

Because the Fermi level term _EF_ cancels out completely during the multiplication, this proves that the product _n_ 0 _p_ 0 is independent of doping concentration and remains a thermodynamic constant at any given temperature. 

6 

GATE PHYSICS 

SEMICONDUCTOR PHYSICS & JUNCTIONS 

### **4. Problem-Solving Algorithm** 

#### **Algorithm for Extrinsic Semiconductor Calculations** 

1. **Identify Doping Regime:** Determine if the semiconductor is doped with donors ( _ND_ ) or acceptors ( _NA_ ). 

2. **Apply Charge Neutrality / Complete Ionization:** Under complete thermal ionization at room temperature (300 K), set: 

   -  _For n-type (ND ≫ ni):_ The majority carrier concentration is _n_ 0 _≈ ND_ . 

   -  _For p-type (NA ≫ ni):_ The majority carrier concentration is _p_ 0 _≈ NA_ . 

3. **Calculate Minority Carrier Concentration via Mass Action:** Use the mass action law to find the minority carrier concentration: 



<!-- Start of picture text -->
i i<br> In n-type: p 0 = n n 0 2 ≈ N n D 2 .<br>i i<br> In p-type: n 0 = n p 0 2 ≈ N n A 2 .<br>Determine Fermi Level Positioning: Use the corresponding energy difference for-<br>mula. For example, to find the shift of EFF relative to the intrinsic Fermi level EFiFi in<br>n-type:<br>EF − EFi =  kBT ln ≈ kBT ln (25)<br>� nn 0 i � � NnDi �<br><!-- End of picture text -->

4. **Determine Fermi Level Positioning:** Use the corresponding energy difference formula. For example, to find the shift of _EFF_ relative to the intrinsic Fermi level _EFiFi_ in n-type: 

### **5. Connections to Macroscopic Observables** 

-  **Temperature-Dependent Hall Effect:** Doping concentrations and majority carrier types are directly measured using the **Hall Coefficient (** _RH_ **)** : 



<!-- Start of picture text -->
RH ≈− 1 (n-type) , RH ≈ + 1 (p-type) (26)<br>n 0 e p 0 e<br><!-- End of picture text -->

By measuring the sign of the Hall voltage, one determines whether the material conducts via electrons or holes, and the magnitude yields the active carrier density. 

7 

GATE PHYSICS 

SEMICONDUCTOR PHYSICS & JUNCTIONS 

### **6. Crucial Pitfalls** 

#### **Semiconductor Carrier Statistics Traps to Avoid** 

-  **The** _Eg_ **vs.** _Eg/_ 2 **Exponential Factor Trap:** Forgetting the factor of **2** in the denominator of the exponential term of the intrinsic carrier concentration formula: 



<!-- Start of picture text -->
ni = � NCNV e −Eg/ 2 kBT (27)<br><!-- End of picture text -->

A transition equation at two different temperatures _T_ 1 and _T_ 2 satisfies: 



<!-- Start of picture text -->
ln ≈ Eg − 1 (28)<br>� nnii 21 � 2 kB � T 12 T 1 �<br><!-- End of picture text -->

Forgetting the factor of 2 in this term leads to extremely wrong calculated energy gaps or carrier density ratios. 

-  **The Law of Mass Action Doping Misconception:** Believing that the law of mass action _n_ 0 _p_ 0 = _n_<sup>2</sup> _i_<sup>onlyappliestointrinsicsemiconductors.Theproduct</sup><sup>_n_0</sup><sup>_p_0is</sup> independent of doping and remains constant. 

-  **Assuming Fixed Fermi Levels under Doping Changes:** Forgetting that the Fermi level is a dynamic chemical potential that shifts up/down with doping. 

### **7. Standard Textbook Systems** 

-  **Intrinsic Silicon (Si) at Room Temperature:** A standard reference system where the band gap is _Eg ≈_ 1 _._ 12 eV, resulting in an intrinsic carrier concentration of _ni ≈_ 1 _._ 5 _×_ 10<sup>10</sup> cm<sup>_−_3</sup> at 300 K. 

-  **Phosphorus-Doped Silicon (n-type):** A system illustrating extrinsic statistics where silicon is doped with phosphorus atoms ( _ND_ = 10<sup>16</sup> cm<sup>_−_3</sup> ). This increases the electron concentration to _n_ 0 _≈_ 10<sup>16</sup> cm<sup>_−_3</sup> and suppresses the hole concentration to _p_ 0 _≈_ 2 _._ 25 _×_ 10<sup>4</sup> cm<sup>_−_3</sup> at room temperature. 

8 

GATE PHYSICS 

SEMICONDUCTOR PHYSICS & JUNCTIONS 

## **3 Physics of Metal-Semiconductor Junctions: Schottky vs. Ohmic** 

### **1. Core Theory** 

A **metal-semiconductor (M-S) junction** is a solid-state interface formed by placing a metal in intimate contact with a semiconductor surface. 

The physical origin of the resulting electrical characteristics is the alignment of their chemical potentials (Fermi energy levels) under thermodynamic equilibrium. Because the work function of the metal (Φ _m_ ) typically differs from that of the semiconductor (Φ _s_ ), charge carriers must transfer across the interface to align the Fermi levels. This transfer creates an electrostatic double layer and bends the electronic bands of the semiconductor near the interface. 

-  **Schottky (Rectifying) Contacts:** Occur when band bending creates an electrostatic potential barrier (the **Schottky Barrier** ) that restricts the flow of majority carriers. Under an external voltage, this junction acts as a diode, allowing large currents to flow in only one direction (rectification). 

-  **Ohmic (Non-Rectifying) Contacts:** Occur when band bending does not create a barrier to majority carriers, or when the barrier is made extremely narrow via heavy doping. This interface allows charge carriers to flow easily in both directions with minimal resistance, satisfying Ohm’s law. 

### **2. Mathematical Framework** 

Consider an n-type semiconductor with electron affinity _χs_ : 

-  **Schottky Barrier Height (** Φ _Bn_ **):** 



<!-- Start of picture text -->
Φ Bn = Φ m − χs (29)<br><!-- End of picture text -->

where Φ _m_ is the metal work function and _χs_ is the semiconductor electron affinity. 

-  **Built-in Potential (** _Vbi_ **):** 



<!-- Start of picture text -->
eVbi = Φ m − Φ s = Φ Bn − ( EC − EF  ) (30)<br><!-- End of picture text -->

-  **Depletion Region Width (** _W_ **):** Solving Poisson’s equation under the depletion approximation yields: 



<!-- Start of picture text -->
2 ϵs ( Vbi − Va )<br>W = (31)<br>� eND<br><!-- End of picture text -->

where _ϵs_ is the semiconductor permittivity, _ND_ is the donor doping concentration, and _Va_ is the applied bias voltage. 

 **Schottky Diode I-V Characteristics (Thermionic Emission Model):** 



<!-- Start of picture text -->
I =  Is e eVa/kBT − 1 (32)<br>� �<br><!-- End of picture text -->

where the saturation current _Is_ is: 



<!-- Start of picture text -->
Is =  AA ∗ T 2 e − Φ Bn/kBT (33)<br><!-- End of picture text -->

where _A_ is the junction area and _A_<sup>_∗_</sup> is the effective Richardson constant. 

9 

GATE PHYSICS 

SEMICONDUCTOR PHYSICS & JUNCTIONS 

-  **Ohmic Tunneling Probability (Field Emission):** For heavily doped semiconductors ( _ND ≥_ 10<sup>19</sup> cm<sup>_−_3</sup> ), the depletion width _W ∝_ 1 _/_<sup>_~~√~~_</sup> _ND_ becomes narrow enough ( _W ≤_ 30<sup>˚</sup> A) for electrons to quantum tunnel directly through the barrier. The tunneling transmission probability is: 



<!-- Start of picture text -->
T tunnel ∝ e − 2 W ℏ √ 2 m ∗ Φ Bn ∝ e− � 2 √ ϵ ℏ sm ∗ � √ Φ BnND (34)<br><!-- End of picture text -->

### **3. Derivation Milestones** 

1. **Poisson’s Equation Setup:** Apply the depletion approximation in the semiconductor region (0 _≤ x ≤ W_ ), assuming all mobile electrons are swept away, leaving only positive donor ions of density _ρ_ ( _x_ ) = _eND_ : 



<!-- Start of picture text -->
d 2 ϕ ( x ) =  − ρ ( x ) =  − eND (35)<br>dx 2 ϵs ϵs<br><!-- End of picture text -->

2. **Integrating for Electric Field:** Integrate once using the boundary condition that the electric field must vanish at the edge of the depletion region, _E_ ( _W_ ) = _−_<sup>_d_</sup> _dx_<sup>_<u>ϕ</u>_(</sup><sup>_W_) = 0:</sup> 



<!-- Start of picture text -->
E ( x ) = eND ( x − W ) (36)<br>ϵs<br><!-- End of picture text -->

3. **Integrating for Potential Profile:** Integrate a second time to find the potential profile, setting the reference potential at the bulk boundary to zero ( _ϕ_ ( _W_ ) = 0): 



<!-- Start of picture text -->
ϕ ( x ) =  − eND ( x − W ) 2 (37)<br>2 ϵs<br><!-- End of picture text -->

4. **Extracting Depletion Width (** _W_ **):** Match the potential at the metal interface ( _x_ = 0), which must be equal to the negative built-in potential ( _−ϕ_ (0) = _Vbi_ ): 



<!-- Start of picture text -->
2 ϵsVbi<br>Vbi = eND W 2 = ⇒ W = (38)<br>2 ϵs � eND<br><!-- End of picture text -->

This derives the quadratic dependency of the depletion width on doping concentration. 

10 

GATE PHYSICS 

SEMICONDUCTOR PHYSICS & JUNCTIONS 

### **4. Problem-Solving Algorithm** 

#### **Predicting M-S Junction Properties** 

1. **Compare Work Functions:** Identify the semiconductor type and compare the work functions: 

   -  _For n-type semiconductor:_ 

      - If Φ _m >_ Φ _s_ , the junction forms a **Schottky (rectifying) contact** . 

      - If Φ _m <_ Φ _s_ , the junction forms an **Ohmic (non-rectifying) contact** . 

   -  _For p-type semiconductor:_ 

      - If Φ _m <_ Φ _s_ , the junction forms a **Schottky (rectifying) contact** . 

      - If Φ _m >_ Φ _s_ , the junction forms an **Ohmic (non-rectifying) contact** . 

2. **Calculate Barrier Heights (for Schottky):** Use Φ _Bn_ = Φ _m − χs_ for n-type, and Φ _Bp_ = ( _Eg/e_ ) + _χs −_ Φ _m_ for p-type. 

3. **Evaluate Built-in potential:** _Vbi_ = _|_ Φ _m −_ Φ _s|/e_ . 

4. **Check for Tunneling (Ohmic Doping):** If the doping concentration is extremely high ( _ND >_ 10<sup>19</sup> cm<sup>_−_3</sup> ), the contact will behave as an **Ohmic contact via tunneling** regardless of work function differences, as electrons can easily tunnel through the thin barrier. 

### **5. Connections to Macroscopic Observables** 

-  **Diode Rectification vs. Linear Conduction:** 

   - **Schottky Diode:** Exhibiting highly non-linear I-V characteristics. Under forward bias, the current increases exponentially; under reverse bias, only a tiny, voltage-independent leakage current _Is_ flows. 

   - **Ohmic Contact:** Exhibiting strictly linear, symmetric I-V curves ( _I_ = _V/Rc_ ) in both positive and negative voltage regimes, with a very small contact resistance ( _Rc →_ 0). 

11 

GATE PHYSICS 

SEMICONDUCTOR PHYSICS & JUNCTIONS 

### **6. Crucial Pitfalls** 

#### **Metal-Semiconductor Junction Traps to Avoid** 

-  **The Work Function Comparison Reversal Trap:** Accidentally applying the n- type work function rule to a p-type semiconductor. Remember that the rule flips completely: for p-type, Φ _m <_ Φ _s_ is rectifying, and Φ _m >_ Φ _s_ is Ohmic. 

-  **The Electron Affinity vs. Work Function Confusion:** Calculating the Schottky barrier height Φ _Bn_ using the semiconductor work function Φ _s_ instead of the electron affinity _χs_ . The barrier height is strictly determined by the difference between the metal work function and the semiconductor’s conduction band edge: Φ _Bn_ = Φ _m − χs_ . 

-  **Ignoring Fermi Level Pinning:** In real-world systems, high densities of surface states at the semiconductor boundary trap charge, pinning the Fermi level at a fixed energy. This makes the real barrier height virtually independent of the metal work function Φ _m_ . In the GATE exam, however, always solve using the ideal Schottky-Mott limit unless surface states are explicitly specified. 

### **7. Standard Textbook Systems** 

-  **The Gold/n-Silicon (Au/n-Si) Schottky Diode:** A classic rectifying junction where the high work function of gold (Φ _m ≈_ 5 _._ 1 eV) relative to n-Si (Φ _s ≈_ 4 _._ 05 eV, affinity _χs ≈_ 4 _._ 01 eV) creates a substantial Schottky barrier (Φ _Bn ≈_ 1 _._ 1 eV). 

-  **The Aluminum/n-Silicon (Al/n-Si) Ohmic Contact:** A standard non-rectifying interface. Under heavy arsenic/phosphorus surface doping ( _ND ≥_ 10<sup>20</sup> cm<sup>_−_3</sup> ), the barrier width shrinks to less than 20<sup>˚</sup> A, allowing conduction electrons to tunnel through the interface and creating a low-resistance Ohmic contact. 

12 

GATE PHYSICS 

SEMICONDUCTOR PHYSICS & JUNCTIONS 

## **References** 

1. Neamen, Donald A. _Semiconductor Physics and Devices_ . McGraw-Hill, 2003. 

2. Kittel, Charles. _Introduction to Solid State Physics_ . Wiley, 2005. 

3. Pillai, S. O. _Solid State Physics_ . New Age International, 2006. 

13 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

# **GATE PHYSICS STUDY NOTES Dielectrics, Magnetism, & Superconductivity in Solids** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**|**Dielectric Properties of Solids & Ferroelectricity**|**2**|
|---|---|---|
|**2**|**Magnetic Properties of Solids**|**6**|
|**3**|**Ferromagnetic Domains & Bloch Walls**|**10**|
|**4**|**Superconductivity**|**14**|



1 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

## **1 Dielectric Properties of Solids & Ferroelectricity** 

### **1. Core Theory** 

**Dielectrics** are materials that do not possess free charge carriers but are highly polarizable under the influence of an external electric field. 

-  **Microscopic Polarizability (** _α_ **):** When an external electric field is applied, bound charges undergo microscopic displacements, creating local electric dipole moments. The total induced dipole moment **p** of an atom or molecule is proportional to the local electric field acting on it: **p** = _α_ **E** loc. The total polarizability consists of three main physical contributions: 

   1. **Electronic Polarizability (** _αe_ **):** The elastic displacement of the negative electron cloud relative to the positive nucleus. This occurs in all atoms and is temperature-independent. 

   2. **Ionic Polarizability (** _αi_ **):** The elastic displacement of positive ions relative to negative ions in ionic crystals (e.g., NaCl). It is temperature-independent. 

   3. **Orientational (or Dipolar) Polarizability (** _αd_ **):** The spatial alignment of permanent molecular dipoles (e.g., H2O or polar polymers) along the field axis. This process is highly temperature-dependent, scaling as 1 _/T_ . 

-  **Lorentz Local Field (Eloc):** In a condensed solid, the field polarising an individual atom is not simply the macroscopic Maxwellian field **E** . Instead, it is the local field **E** loc which includes the field contributions from all surrounding induced dipoles. For cubic site symmetries, the local field is the sum of the macroscopic field and the Lorentz cavity field: **E** loc = **E** + 3<sup>**<u>P</u>**</sup> _ϵ_ 0<sup>.</sup> 

-  **The Clausius-Mossotti Equation:** A fundamental bridge in solid-state physics that mathematically relates the macroscopic dielectric constant _ϵr_ to the microscopic, intrinsic electronic polarizability _αe_ of the constituent atoms. 

-  **Ferroelectricity:** A solid-state phenomenon where crystals possess a spontaneous, non-zero macroscopic electric polarization **P** in the complete absence of an external electric field, which can be reoriented or reversed by an applied field. This is driven by cooperative structural phase transitions below a critical Curie temperature _TC_ . 

### **2. Mathematical Framework** 

The macroscopic and microscopic dielectric parameters are governed by the following equations: 

 **Macroscopic Polarization and Displacement:** 



<!-- Start of picture text -->
P  =  N p  =  Nα E loc (1)<br><!-- End of picture text -->



<!-- Start of picture text -->
D  =  ϵ 0 E  +  P  =  ϵ 0 ϵr E = ⇒ P  =  ϵ 0( ϵr − 1) E (2)<br><!-- End of picture text -->

where _N_ is the number density of polarizable atoms, **p** is the induced dipole moment, and _ϵr_ is the relative dielectric constant. 

-  **Lorentz Local Field (Cubic Crystals):** 



<!-- Start of picture text -->
E loc =  E  + P (3)<br>3 ϵ 0<br><!-- End of picture text -->

2 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

-  **The Clausius-Mossotti Equation:** 



<!-- Start of picture text -->
ϵr − 1<br>(4)<br>ϵr  + 2 = Nα 3 ϵ 0<br><!-- End of picture text -->

For optical frequencies where only electronic polarizability contributes ( _ϵr ≈ n_<sup>2</sup> , where _n_ is the refractive index), this reduces to the **Lorentz-Lorenz equation** : 



<!-- Start of picture text -->
n 2 − 1<br>(5)<br>n 2 + 2 = Nα 3 ϵ 0 e<br><!-- End of picture text -->

-  **Curie-Weiss Law of Ferroelectrics:** For temperatures above the Curie temperature ( _T > TC_ ), the static dielectric constant obeys: 



<!-- Start of picture text -->
C<br>ϵr =  ϵ∞ + (6)<br>T − TC<br><!-- End of picture text -->

where _C_ is the Curie constant and _TC_ is the Curie-Weiss temperature. 



<!-- Start of picture text -->
 Lyddane-Sachs-Teller (LST) Relation: Relates the static ( ϵ (0)) and high-frequency<br>( ϵ ( ∞ )) dielectric constants to the frequencies of longitudinal ( ωL ) and transverse ( ωT  ) optical<br>phonons:<br>ω 2<br>L<br>= ϵ (0) (7)<br>ωT 2 ϵ ( ∞ )<br><!-- End of picture text -->

### **3. Derivation Milestones** 

The derivation of the Clausius-Mossotti equation relies on these critical milestones: 

1. **The Lorentz Cavity Model:** To evaluate the local electric field **E** loc at a specific atomic site, we construct a virtual sphere of radius _R_ centered at that site. The radius is chosen to be macroscopically small but microscopically large compared to the lattice constant. The local field is written as: 



<!-- Start of picture text -->
E loc =  E  +  E 2 +  E 3 (8)<br><!-- End of picture text -->

where **E** is the macroscopic field, **E** 2 is the field due to polarization charges on the boundary of the Lorentz sphere, and **E** 3 is the field due to individual atomic dipoles located inside the sphere. 

2. **Evaluation of the Cavity and Dipole Fields:** 

   -  Integrating the bound surface charge density _σb_ = **P** _·_ **n** ˆ = _P_ cos _θ_ over the spherical cavity boundary yields: 



<!-- Start of picture text -->
E 2 = (9)<br>� 4 σπϵb  cos0 R θ 2 dA  = 3 P ϵ 0<br><!-- End of picture text -->

-  For a crystal site with cubic symmetry (e.g., Simple Cubic, BCC, or FCC), the contributions of the individual dipoles inside the sphere sum to zero: **E** 3 = 0. Thus, we obtain the Lorentz local field: **E** loc = **E** + 3<sup>**<u>P</u>**</sup> _ϵ_ 0<sup>.</sup> 

3 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

3. **Combining Local and Macroscopic Polarization:** Equate the microscopic and macroscopic polarization definitions: 



<!-- Start of picture text -->
P  =  Nα E loc =  Nα E  + P (10)<br>� 3 ϵ 0 �<br><!-- End of picture text -->

Factor out and solve for **P** : 



<!-- Start of picture text -->
P 1  − Nα =  Nα E = ⇒ P  = Nα E (11)<br>� 3 ϵ 0 � 1  − Nα<br>3 ϵ 0<br><!-- End of picture text -->

4. **Extracting the Clausius-Mossotti Relation:** Substitute the macroscopic relation **P** = _ϵ_ 0( _ϵr −_ 1) **E** into the equation: 



<!-- Start of picture text -->
Nα<br>ϵ 0( ϵr − 1) E  = Nα E = ⇒ ϵr − 1 = ϵ 0 (12)<br>1  − Nα 1  − Nα<br>3 ϵ 0 3 ϵ 0<br><!-- End of picture text -->

Solving for the ratio directly yields the Clausius-Mossotti equation: 



<!-- Start of picture text -->
ϵr − 1<br>(13)<br>ϵr  + 2 = Nα 3 ϵ 0<br><!-- End of picture text -->

### **4. Problem-Solving Algorithm** 

#### **Calculating Microscopic Polarizability from Macroscopic Dielectric Constants** 

1. **Compute Atomic Density (** _N_ **):** If the density _ρ_ ( _g/cm_<sup>3</sup> ) and molar mass _M_ ( _g/mol_ ) are given, calculate the atomic concentration: 



<!-- Start of picture text -->
N = ρ · NA (14)<br>M<br><!-- End of picture text -->

where _NA ≈_ 6 _._ 022 _×_ 10<sup>23</sup> is Avogadro’s number. Convert _N_ to units of m<sup>_−_3</sup> by multiplying by 10<sup>6</sup> . 

2. **Set up the Clausius-Mossotti Equation:** 



<!-- Start of picture text -->
ϵr − 1<br>(15)<br>ϵr  + 2 = Nα 3 ϵ 0<br><!-- End of picture text -->

3. **Solve for Polarizability (** _α_ **):** 



<!-- Start of picture text -->
α  = 3 ϵ 0 (16)<br>N � ϵϵrr  + 2  − 1 �<br><!-- End of picture text -->

Use _ϵ_ 0 _≈_ 8 _._ 854 _×_ 10<sup>_−_12</sup> F/m. The resulting polarizability _α_ will be in SI units (F _·_ m<sup>2</sup> ). 

4. **Determine Polarizability Volume:** Often, texts express the electronic polarizability as a volume _α_<sup>_′_</sup> (defined by _α_ = 4 _πϵ_ 0 _α_<sup>_′_</sup> ). Calculate: 



<!-- Start of picture text -->
3<br>α ′ = (expressed in m 3 or ˚ A 3 ) (17)<br>4 πN � ϵϵrr  + 2  − 1 �<br><!-- End of picture text -->

4 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

### **5. Connections to Macroscopic Observables** 

-  **The Polarization Catastrophe:** If the density _N_ or polarizability _α_ increases such that _<u>Nα</u>_ 3 _ϵ_ 0<sup>_→_1, the denominator in the polarization equation goes to zero.This causes the dielectric</sup> constant _ϵr →∞_ . This instability physically triggers the spontaneous shift of ionic sublattices, causing a structural transition into a **ferroelectric phase** with a permanent, spontaneous polarization. 

-  **Soft Mode Ferroelectric Transition:** According to the LST relation, as a ferroelectric crystal cools toward _TC_ , the static dielectric constant _ϵ_ (0) diverges according to the CurieWeiss law. For _ϵ_ (0) _→∞_ , the transverse optical phonon frequency must go to zero ( _ωT →_ 0). This corresponds to a ”soft mode” where the lattice becomes mechanically unstable against the transverse vibrational displacement, locking the ions into a permanently polarized, noncentrosymmetric configuration. 

### **6. Crucial Pitfalls** 

#### **Dielectric and Polarizability Pitfalls to Avoid** 

-  **The High-Frequency Limit Trap:** Attempting to calculate optical refractive indices using static dielectric constants. At high optical frequencies (UV-Visible light), the heavy ions and polar molecules cannot precess or vibrate fast enough to keep up with the oscillating electric field, so _αi →_ 0 and _αd →_ 0. Only electronic polarizability survives. Therefore, you must use _ϵr_ ( _∞_ ) = _n_<sup>2</sup> instead of the static dielectric constant _ϵ_ (0) in the Clausius-Mossotti (Lorentz-Lorenz) equation. 

-  **The Lorentz Field Limit:** Confusing the macroscopic Maxwell field **E** with the local polarizing field **E** loc. In dilute gases, the dipoles are far apart, making **E** loc _≈_ **E** . However, in condensed phases (solids and liquids), the local field is significantly larger, making the Lorentz correction **P** _/_ 3 _ϵ_ 0 mandatory. 

-  **Curie-Weiss Temperature Offset:** Assuming the transition temperature _TC_ in the Curie-Weiss law is exactly the physical transition temperature of the crystal. For firstorder ferroelectric transitions, the physical transition occurs at a temperature slightly higher than _TC_ . 

### **7. Standard Textbook Systems** 

-  **Barium Titanate (BaTiO** 3 **):** The classic prototype of a displacive ferroelectric. Above _TC ≈_ 120<sup>_◦_</sup> C, it is cubic and paraelectric. Below _TC_ , the central Ti<sup>4+</sup> ion shifts off-center relative to the surrounding O<sup>2</sup><sup>_−_</sup> octahedron, stretching the unit cell along the c-axis into a tetragonal ferroelectric structure. 

-  **Potassium Dihydrogen Phosphate (KDP, KH** 2 **PO** 4 **):** Illustrates an order-disorder ferroelectric transition, where the ferroelectric phase is driven by the low-temperature ordering of protons within hydrogen bonds. 

5 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

## **2 Magnetic Properties of Solids** 

### **1. Core Theory** 

Magnetism in solids originates microscopically from the orbital motion of electrons and the intrinsic quantum-mechanical spins of electrons and nuclei. 

-  **Diamagnetism (Langevin):** An intrinsic property of all closed-shell atoms. When an external magnetic field is applied, it induces a precession of the electronic orbits (Larmor precession) that, by Lenz’s law, generates an internal magnetic moment pointing opposite to the applied field. Diamagnetism is strictly negative, weak, and temperature-independent. 

-  **Paramagnetism (Langevin and Brillouin):** Occurs in materials containing atoms with partially filled shells that possess permanent magnetic moments (unpaired electron spins). In the absence of a field, these moments are randomly oriented due to thermal fluctuations. An external field aligns them, creating a positive magnetization. Langevin theory models this classically, whereas Brillouin theory incorporates quantum spin quantization. It is strongly temperature-dependent, obeying Curie’s law (1 _/T_ ). 

-  **Ferromagnetism (Weiss Mean Field):** Characterized by spontaneous, parallel alignment of neighboring magnetic moments below a Curie temperature _TC_ , driven by quantum mechanical **exchange interactions** which are modeled macroscopically as a powerful internal Weiss molecular field **B** exchange = _λ_ **M** . 

-  **Antiferromagnetism (N´eel):** Characterized by an antiparallel, alternating alignment of magnetic moments on two interpenetrating sublattices, resulting in a net-zero macroscopic magnetization below the N´eel temperature _TN_ . 

-  **Ferrimagnetism:** Occurs when the alternating sublattices have unequal magnetic moments (due to different chemical species or coordination sites), leaving a net, spontaneous macroscopic magnetization below the transition temperature. 

### **2. Mathematical Framework** 

The magnetic behaviors are governed by the following equations: 

-  **Langevin Diamagnetic Susceptibility:** 



<!-- Start of picture text -->
χ dia =  − µ 0 NZe 2 ⟨r 2 ⟩ (18)<br>6 me<br><!-- End of picture text -->

where _N_ is the atomic density, _Z_ is the atomic number, _e_ is the electron charge, _me_ is the electron mass, and _⟨r_<sup>2</sup> _⟩_ is the mean-square atomic radius. 

 **Quantum Paramagnetic Magnetization (Brillouin):** 



<!-- Start of picture text -->
M =  NgJµBBJ ( x ) (19)<br><!-- End of picture text -->

where _J_ is the total angular momentum quantum number, _g_ is the Land´e g-factor, _µB_ = 2 _<u>em</u>_ <u>ℏ</u> _e_ is the Bohr magneton, and _BJ_ ( _x_ ) is the **Brillouin function** : 



<!-- Start of picture text -->
BJ ( x ) = 2 J + 1 coth x − 1 with x  = gJµBB (20)<br>2 J � 2 J 2 J + 1 � 2 J coth � 21 J x � kBT<br><!-- End of picture text -->

6 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

* For _J →∞_ (classical limit), _BJ_ ( _x_ ) reduces to the **Langevin function** _L_ ( _x_ ) = coth _x− x_<sup><u>1</u>.</sup> * For _J_ = 1 _/_ 2 (pure spin limit), _B_ 1 _/_ 2( _x_ ) = tanh _x_ , yielding Curie’s Law in the weak-field limit ( _x ≪_ 1): 



<!-- Start of picture text -->
M ≈ N g 2 µ B 2 J ( J + 1) B = ⇒ χ para = µ 0 M = C (21)<br>3 kBT B T<br><!-- End of picture text -->

where _C_ =<sup>_<u>µ</u>_0</sup><sup>_N_</sup><sup>_<u>g</u>_2</sup><sup>_<u>µ</u>_</sup> _<u>B</u>_<sup>2</sup><sup>_J_</sup><sup><u>(</u></sup><sup>_J_+1)</sup> is the Curie Constant. 3 _kB_ 

 **Curie-Weiss Law (Ferromagnetism for** _T > TC_ **):** 



<!-- Start of picture text -->
C<br>χ ferro = with TC =  Cλ (22)<br>T − TC<br><!-- End of picture text -->

where _λ_ is the Weiss molecular exchange field constant. 

-  **Antiferromagnetism Susceptibility (** _T > TN_ **):** 



<!-- Start of picture text -->
C<br>χ AFM = (23)<br>T +  θ<br><!-- End of picture text -->

where _θ_ is a temperature constant representing the strength of the antiferromagnetic exchange coupling. 

### **3. Derivation Milestones** 

The derivations of these magnetic susceptibilities are built upon these steps: 

1. **Langevin Diamagnetism (Larmor Precession):** When a magnetic field _B_ **z** ˆ is applied to an electron orbiting in a plane perpendicular to the field, the magnetic torque induces an angular Larmor precession of frequency _ωL_ = 2 _<u>eBme</u>_<sup>.</sup> 

2. **Induced Current and Orbital Area:** The precession corresponds to an induced loop current _I_ = _−_<sup>_<u>Ze</u>_</sup> 2 _π_<sup>_ωL_=</sup><sup>_−_</sup><sup>_<u>Ze</u>_</sup> 4 _πm_<sup>2</sup><sup>_<u>B</u>_</sup> _e_<sup>.Themagneticmoment</sup><sup>_µ_ofthisloopis:</sup> 



<!-- Start of picture text -->
µ  =  IA  =  I ( π⟨ρ 2 ⟩ ) =  − Ze 2 B ⟨x 2 +  y 2 ⟩ (24)<br>4 me<br><!-- End of picture text -->

For a spherically symmetric atom, _⟨x_<sup>2</sup> _⟩_ = _⟨y_<sup>2</sup> _⟩_ = _⟨z_<sup>2</sup> _⟩_ =<sup><u>1</u></sup> 3<sup>_⟨r_2</sup><sup>_⟩_,making</sup><sup>_⟨x_2+</sup><sup>_y_2</sup><sup>_⟩_=</sup><sup><u>2</u></sup> 3<sup>_⟨r_2</sup><sup>_⟩_.</sup> Substituting this yields the diamagnetic moment per atom: _µ_ = _−_<sup>_<u>Ze</u>_</sup> 6 _m_<sup>2</sup><sup>_<u>B</u>_</sup> _e_<sup>_⟨r_2</sup><sup>_⟩_,fromwhich</sup> _χ_ dia = _µ_ 0 _Nµ/B_ is derived. 

3. **Quantum Paramagnetism (Boltzmann Partition Sum):** For a quantum spin in a magnetic field, the Zeeman energy states are _Em_ = _−mJ gµBB_ where _mJ ∈{−J, . . . , J}_ . The partition function is: 



<!-- Start of picture text -->
J<br>Z = � e mJ � gµBkBTB � (25)<br>mJ = −J<br><!-- End of picture text -->

Evaluating this geometric series and taking the derivative of its logarithm ( _⟨M ⟩_ = _NkBT_<sup>_<u>∂</u>_</sup> _∂B_<sup><u>ln</u></sup><sup>_<u>Z</u>_)</sup> yields the Brillouin function. 

7 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

4. **Weiss Ferromagnetism (Self-Consistent Mean Field):** Weiss assumed that the electrostatic exchange interaction is equivalent to a powerful internal field proportional to the magnetization: **B** eff = **B** 0+ _λ_ **M** . Substituting this into the paramagnetic equation for _T > TC_ : 



<!-- Start of picture text -->
C C<br>M = 1  − Cλ = CB 0 (26)<br>µ 0 T B eff = µ 0 T ( B 0 +  µ 0 λM ) = ⇒ M � T � µ 0 T<br><!-- End of picture text -->

Solving for the susceptibility _χ_ =<sup>_<u>µ</u>_</sup> _B_<sup><u>0</u></sup><sup>_M_</sup> 0 directly yields the Curie-Weiss relation: _χ_ = _T −CCλ_<sup>.</sup> 

### **4. Problem-Solving Algorithm** 

#### **Solving Magnetic Susceptibility and Exchange Fields** 

1. **Identify the Magnetic Phase:** Check if the system is described as diamagnetic, paramagnetic, or ferromagnetic to apply the correct susceptibility equation. 

2. **Compute Langevin Diamagnetism:** Given the electron cloud radius _R_ and atomic number _Z_ , calculate: 



<!-- Start of picture text -->
χ dia =  − µ 0 NZe 2 R 2 (27)<br>6 me<br><!-- End of picture text -->

Ensure you use _µ_ 0 = 4 _π ×_ 10<sup>_−_7</sup> H/m, _me_ = 9 _._ 109 _×_ 10<sup>_−_31</sup> kg, and _R_ in meters. 

3. **Calculate Weiss Exchange Fields (** _B_ **ex):** Given the Curie temperature _TC_ and the Curie constant _C_ , find the exchange constant: 



<!-- Start of picture text -->
λ  = TC (28)<br>C<br><!-- End of picture text -->

Then, the internal exchange field at saturation magnetization _M_ sat is: 



<!-- Start of picture text -->
B ex =  µ 0 λM sat =  µ 0 M sat (expressed in Tesla) (29)<br>� TCC �<br><!-- End of picture text -->

### **5. Connections to Macroscopic Observables** 

-  **Thermal Behavior of Magnetic Phases:** Measuring magnetic susceptibility _χ_ vs. temperature _T_ acts as the premier experimental tool to identify solid-state magnetic transitions: 

   1. **Paramagnet** : _χ_ diverges as 1 _/T_ as _T →_ 0. 

   2. **Ferromagnet** : _χ_ diverges at the critical Curie temperature _TC_ . Below _TC_ , a macroscopic spontaneous magnetization is observed. 

   3. **Antiferromagnet** : _χ_ increases with cooling, reaching a sharp maximum peak at the N´eel temperature _TN_ , below which it decreases as the sublattices freeze into locked antiparallel orientations. 

-  **Superlattice Neutron Diffraction Peaks:** Since antiferromagnetic ordering has alternating antiparallel spins, the magnetic unit cell has a lattice parameter that is twice as large as the chemical unit cell. Below _TN_ , neutron diffraction reveals new, sharp ”superlattice” reflection peaks that are completely absent in normal X-ray diffraction, serving as the definitive proof of antiferromagnetism. 

8 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

### **6. Crucial Pitfalls** 

#### **Magnetic Susceptibility Traps to Avoid** 

-  **The Classical Langevin vs. Quantum Spin-1/2 Formula:** Using the classical Langevin function for systems with quantum spins. For spin-1/2 systems (like electrons in free radicals), you must use the tanh function instead of the classical coth( _x_ ) _−_ 1 _/x_ function. 

-  **The Weiss Exchange Field Magnitude Paradox:** Expecting the Weiss exchange field to be of the same order of magnitude as a standard dipole field ( _∼_ 0 _._ 1 T). The exchange field is driven by electrostatic exchange energy, yielding typical values of _B_ ex _∼_ 10<sup>3</sup> T. Attempting to explain ferromagnetism using classical dipole-dipole interactions is a critical physical error (dipolar fields can only support ferromagnetism below _∼_ 1 K). 

-  **Sign Conventions in Temperature Offsets:** Confusing the sign in the denominator of the antiferromagnetic susceptibility: _χ_ = _TC_ + _θ_<sup>.The positive sign in the denominator</sup> reflects that the internal antiferromagnetic exchange forces oppose external magnetization, suppressing susceptibility. 

### **7. Standard Textbook Systems** 

-  **Manganese Oxide (MnO):** The classic textbook example of an antiferromagnet. Below _TN ≈_ 116 K, the Mn<sup>2+</sup> ions form two alternating, antiparallel sublattices, which was originally mapped experimentally using neutron diffraction. 

-  **Yttrium Iron Garnet (YIG, Y** 3 **Fe** 5 **O** 12 **):** A prototypical ferrimagnetic insulator. The five Fe<sup>3+</sup> ions in the unit cell reside on different coordination sites (two octahedral, three tetrahedral) with opposing orientations, leaving a net unbalanced moment of one Fe<sup>3+</sup> spin per formula unit. 

9 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

## **3 Ferromagnetic Domains & Bloch Walls** 

### **1. Core Theory** 

A macroscopic specimen of a ferromagnetic material, even when cooled below _TC_ , does not necessarily exhibit a net macroscopic magnetization. 

-  **Magnetic Domains:** The solid spontaneously divides into many small, localized regions called **magnetic domains**. Within each individual domain, the spins are completely parallel and saturated. However, the magnetizations of different domains point in different directions, causing the vector sum over the entire macroscopic specimen to be zero. 

-  **Energy Minimization Origin:** The formation of domains is driven by the thermodynamic minimization of the total free energy, which is a balance of five competing contributions: 

   1. **Magnetostatic (or Demagnetizing) Energy:** The energy stored in the magnetic field lines outside the crystal. Dividing the specimen into closed-loop domains with fluxclosure configurations eliminates external field lines, drastically reducing this energy. 

   2. **Exchange Energy:** The quantum electrostatic energy that favors parallel alignment of spins. This energy is minimized within each domain but is penalized within the boundary walls. 

   3. **Magnetocrystalline Anisotropy Energy:** Solid crystals have easy and hard axes of magnetization. This energy is minimized when spins align along the crystallographic easy axes. 

   4. **Magnetostrictive (Elastic) Energy:** Aligning spins causes the lattice to deform slightly (magnetostriction). This deforming strain is penalized at domain boundaries. 

-  **The Bloch Wall:** The boundary layer that separates two adjacent magnetic domains pointing in opposite directions (e.g., a 180<sup>_◦_</sup> wall). Instead of a sharp, discontinuous transition over a single atomic plane, the magnetization vector rotates gradually and continuously over many lattice spacings to minimize the quantum exchange energy penalty. 

### **2. Mathematical Framework** 

* **Exchange Energy between adjacent spins:** 



<!-- Start of picture text -->
E ex =  − 2 J ex S i ·  S j =  − 2 J ex S 2 cos  ϕij (30)<br><!-- End of picture text -->

where _J_ ex is the exchange integral and _ϕij_ is the angle between adjacent spins. * **Bloch Wall Energy per unit area (** _σW_ **):** 



<!-- Start of picture text -->
σW =  σ exchange +  σ anisotropy = π 2 S 2 J ex +  KNW a (31)<br>NW a 2<br><!-- End of picture text -->

where _NW_ is the number of lattice spacings across the wall, _a_ is the lattice constant, and _K_ is the magnetocrystalline anisotropy energy constant (J/m<sup>3</sup> ). * **Equilibrium Bloch Wall Width (** _NW_<sup>_∗a_</sup><sup>**):**Minimizing</sup><sup>_σW_withrespecttothewallthickness</sup><sup>_NW_yieldstheoptimalspacing:</sup> 



<!-- Start of picture text -->
π 2 S 2 J ex<br>NW ∗ = (32)<br>� Ka 3<br><!-- End of picture text -->

10 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 



<!-- Start of picture text -->
π 2 S 2 J ex<br>WW ∗ =  N W ∗ a  = (expressed in meters) (33)<br>� Ka<br><!-- End of picture text -->

* **Optimal Bloch Wall Energy per unit area (** _σW_<sup>_∗_</sup><sup>**):**</sup> 



<!-- Start of picture text -->
J ex K<br>σW ∗ = 2 πS (expressed in J/m 2 ) (34)<br>� a<br><!-- End of picture text -->

### **3. Derivation Milestones** 

The mathematical model of the Bloch wall is derived through these steps: 

1. **Gradual Angle Rotation:** If a 180<sup>_◦_</sup> spin flip occurs abruptly over a single atomic plane ( _NW_ = 1), the exchange energy penalty is: 



<!-- Start of picture text -->
∆ E ex =  − 2 J ex S 2 cos( π )  − ( − 2 J ex S 2 ) = 4 J ex S 2 (35)<br><!-- End of picture text -->

If the rotation occurs gradually over _NW_ steps, the angle between adjacent spins is small: _ϕ ≈ π/NW_ . Expanding the cosine term: 



<!-- Start of picture text -->
E ex( ϕ ) =  − 2 J ex S 2 1  − ϕ 2 = ⇒ ∆ E ex ≈ J ex S 2 ϕ 2 ≈ J ex S 2 (36)<br>� 2 � � NπW �2<br><!-- End of picture text -->

This shows that the exchange energy penalty between a single pair scales down as 1 _/NW_<sup>2.</sup> 

2. **Exchange Energy per Unit Area:** Along a line of _NW_ spins across the wall, the total energy is _NW ·_ ∆ _E_ ex _≈ π_<sup>2</sup> _J_ ex _S_<sup>2</sup> _/NW_ . For a crystal with atomic surface density 1 _/a_<sup>2</sup> per unit area, the total exchange energy per unit area is: 



<!-- Start of picture text -->
σ exchange = π 2 S 2 J ex (37)<br>NW a 2<br><!-- End of picture text -->

This energy term favors an infinitely wide wall ( _NW →∞_ ) to reduce the exchange penalty. 

3. **Anisotropy Energy Penalty:** However, as the wall widens, more spins are forced to point along the crystallographic hard axes, which is penalized by the anisotropy constant _K_ . The anisotropy energy per unit area is proportional to the wall volume: 



<!-- Start of picture text -->
σ anisotropy =  K · WW =  KNW a (38)<br><!-- End of picture text -->

This term acts as a restoring force, pulling the wall to be as thin as possible ( _NW →_ 0). 

4. **Energy Minimization Optimization:** Express the total wall energy as the sum of these competing terms, and take the derivative with respect to _NW_ : 



<!-- Start of picture text -->
dσW =  − π 2 S 2 J ex +  Ka  = 0 = ⇒ NW ∗ = π 2 S 2 J ex (39)<br>dNW NW 2 a 2 � Ka 3<br><!-- End of picture text -->

Substituting _NW_<sup>_∗_backintotheenergyequationyieldstheoptimalwallenergy:</sup> _σW_<sup>_∗_=</sup> _<u>J</u>_ <u>ex</u> _<u>K</u>_ 2 _πS_ . ~~�~~ _a_ 

11 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

### **4. Problem-Solving Algorithm** 

#### **Calculating Bloch Wall Properties** 

1. **Identify the Input Parameters:** Note the exchange integral _J_ ex (often in Joules), spin _S_ , anisotropy constant _K_ (J/m<sup>3</sup> ), and lattice parameter _a_ (meters). 

2. **Calculate the Wall Width in Lattice Spacings (** _NW_<sup>_∗_</sup><sup>**):**</sup> 



<!-- Start of picture text -->
J ex<br>NW ∗ =  πS (40)<br>� Ka 3<br><!-- End of picture text -->

3. **Calculate the Physical Wall Width (** _WW_<sup>_∗_</sup><sup>**):**</sup> 



<!-- Start of picture text -->
J ex<br>WW ∗ =  N W ∗ a  =  πS (in meters) (41)<br>� Ka<br><!-- End of picture text -->

* *Example:* For iron, _J_ ex _≈_ 2 _×_ 10<sup>_−_21</sup> J, _K ≈_ 4 _×_ 10<sup>4</sup> J/m<sup>3</sup> , and _a ≈_ 2 _._ 86<sup>˚</sup> A. This yields a wall width of _WW_<sup>_∗≈_40nm(</sup><sup>_∼_140latticespacings).</sup> 

4. **Compute the Wall Energy per Unit Area (** _σW_<sup>_∗_</sup><sup>**):**</sup> 



<!-- Start of picture text -->
J ex K<br>σW ∗ = 2 πS (in J/m 2 ) (42)<br>� a<br><!-- End of picture text -->

### **5. Connections to Macroscopic Observables** 

-  **Hysteresis and Coercivity:** When an external magnetic field is applied to a demagnetized material, the magnetization increases via **domain wall motion** (favorable domains grow at the expense of unfavorable ones) and **domain rotation** (spins rotate toward the field axis). Defect sites and grain boundaries ”pin” domain walls, preventing them from moving smoothly. This pinning creates a resistance to demagnetization, resulting in the **magnetic hysteresis loop** (remanence _Mr_ and coercivity _Hc_ ). 

-  **The Barkhausen Effect:** During the magnetization process, the pinning of domain walls causes their motion to be jerky rather than continuous. As a wall suddenly snaps past a pin site, it produces a tiny, rapid step-change in local magnetization. This can be detected by a pickup coil as a series of audible voltage clicks (**Barkhausen noise**), providing direct experimental proof of the existence of domains and their boundary walls. 

12 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

### **6. Crucial Pitfalls** 

#### **Bloch Wall Analysis Pitfalls to Avoid** 

-  **Assuming One-Dimensional Step Walls:** Expecting the magnetization direction to flip abruptly over a single atomic plane. This is chemically and physically incorrect because it would cost a massive exchange energy penalty. The gradual rotation over hundreds of atomic planes is a highly favorable compromise that minimizes total free energy. 

-  **Unmatched Dimensional Units:** Confusing the units of the anisotropy constant _K_ (J/m<sup>3</sup> ) with energy per unit area (J/m<sup>2</sup> ). Ensure all dimensions are in SI units, converting lattice parameters from<sup>˚</sup> Angstr¨oms to meters before performing calculations. 

### **7. Standard Textbook Systems** 

-  **The** 180<sup>_◦_</sup> **Bloch Wall in Iron (** _α_ **-Fe):** A classic system where magnetization rotates 180<sup>_◦_</sup> between antiparallel domains. Because the easy axis of BCC iron is along the _⟨_ 100 _⟩_ directions, the wall spans about 140 lattice spacings to minimize the exchange-anisotropy trade-off. 

-  **The** 90<sup>_◦_</sup> **Closure Domains:** Formed near the physical boundaries of crystals to eliminate external magnetic field lines, redirecting the magnetic flux completely inside the specimen to minimize the magnetostatic energy. 

13 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

## **4 Superconductivity** 

### **1. Core Theory** 

**Superconductivity** is a low-temperature quantum state of matter characterized by the complete vanishing of electrical resistivity and the active exclusion of magnetic fields from the interior of the material. 

-  **Zero Resistivity:** Below a critical temperature _TC_ , the electrical resistance of a superconductor drops to exactly zero. Persistent currents induced in a superconducting loop can circulate indefinitely without any power loss. 

-  **The Meissner Effect:** A superconductor behaves as a **perfect diamagnet**. When cooled below _TC_ in a weak magnetic field, the material actively expels all magnetic flux from its interior ( **B** = 0). This is a fundamental physical property that is completely distinct from perfect conductivity; a perfect conductor would merely ”freeze” the existing flux inside, whereas a superconductor expels it. 

-  **Type-I vs. Type-II Superconductors:** 

   1. **Type-I Superconductors:** Exhibit a complete Meissner effect up to a single critical field _Hc_ , above which superconductivity is abruptly destroyed. 

   2. **Type-II Superconductors:** Exhibit a complete Meissner effect up to a lower critical field _Hc_ 1. Above _Hc_ 1, magnetic flux penetrates the material in the form of quantized filament tubes called **vortices** (the mixed or vortex state). Superconductivity is completely destroyed only at a much higher upper critical field _Hc_ 2. 

-  **BCS Theory (Cooper Pairs):** The microscopic mechanism of superconductivity. Electrons near the Fermi surface form bound pairs (**Cooper Pairs**) mediated by a weak, attractive interaction with the positive ion lattice (electron-phonon-electron coupling). These Cooper pairs act as bosons, condensing into a single, coherent quantum ground state protected by an **energy gap ( _Eg_ = 2∆)** at the Fermi level, which prevents scattering. 

-  **Flux Quantization:** The magnetic flux trapped inside a superconducting ring is quantized in discrete units of the flux quantum Φ0 = _h/_ 2 _e_ . The factor of 2 in the denominator is direct physical proof of the pairing of electrons into Cooper pairs. 

### **2. Mathematical Framework** 

The electromagnetic behavior of a superconductor is governed by the following equations: 

-  **London First Equation (Perfect Conductivity):** 



<!-- Start of picture text -->
∂ J s<br>∂t = n m se 2 E (43)<br><!-- End of picture text -->

where **J** _s_ is the superconducting current density, _ns_ is the density of superconducting electrons, and _m_ is the electron mass. 

-  **London Second Equation (Meissner Effect):** 



<!-- Start of picture text -->
∇×  J s =  − n m se 2 B (44)<br><!-- End of picture text -->

14 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

 **Magnetic Field Penetration (London Equation):** 



<!-- Start of picture text -->
∇ 2 B  = 1 B = ⇒ B ( x ) =  B 0 e −x/λL (45)<br>λ 2<br>L<br><!-- End of picture text -->

where _λL_ is the **London Penetration Depth**: 



<!-- Start of picture text -->
m<br>λL = (expressed in meters) (46)<br>� µ 0 nse 2<br><!-- End of picture text -->

-  **BCS Energy Gap Relation at** 0 **K:** 



<!-- Start of picture text -->
Eg (0) = 2∆(0)  ≈ 3 . 52 kBTC (47)<br><!-- End of picture text -->

-  **Critical Field Temperature Dependence:** 



<!-- Start of picture text -->
Hc ( T ) =  Hc (0) 1  − (48)<br>� TTC<br>� �2 �<br><!-- End of picture text -->

-  **London Penetration Depth Temperature Dependence:** 



<!-- Start of picture text -->
λ ( T ) =  λ (0) 1  − (49)<br>� TTC<br>� �4 � − 1 / 2<br><!-- End of picture text -->

 **Flux Quantization:** 



<!-- Start of picture text -->
Φ n =  n Φ0 =  n ≈ n ·  (2 . 07  ×  10 − 15 Wb) (50)<br>� 2 he �<br><!-- End of picture text -->

### **3. Derivation Milestones** 

The mathematical formulations of superconductivity rely on these key steps: 

1. **London First Equation (Zero Scattering):** Assume superconducting electrons move completely without scattering. The equation of motion is: 



<!-- Start of picture text -->
m d dt v s =  −e E (51)<br><!-- End of picture text -->

Substitute the superconducting current density **J** _s_ = _−ens_ **v** _s_ : 



<!-- Start of picture text -->
∂ J s d v s<br>(52)<br>∂t =  −ens dt = n m se 2 E<br><!-- End of picture text -->

This is London’s first equation, which states that an electric field does not maintain a constant current but accelerates it. 

2. **London Second Equation (Faraday Integration):** Take the curl of London’s first equation: 



<!-- Start of picture text -->
∂<br>∂t ( ∇×  J s ) = n m se 2 ( ∇×  E ) (53)<br><!-- End of picture text -->

15 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

Substitute Faraday’s law _∇×_ **E** = _−_<sup>_<u>∂</u>_</sup> _∂t_<sup>**<u>B</u>**:</sup> 



<!-- Start of picture text -->
∂ ∂ B ∂<br>= ⇒ ∇×  J s  + nse 2 = 0 (54)<br>∂t ( ∇×  J s ) =  − n m se 2 ∂t ∂t � m B �<br><!-- End of picture text -->

To enforce the Meissner effect (expulsion of magnetic fields), F. and H. London postulated that the constant of integration must be strictly zero: 



<!-- Start of picture text -->
∇×  J s =  − n m se 2 B (55)<br><!-- End of picture text -->

This is London’s second equation. 

3. **Magnetic Field Decoupling (Penetration Depth):** Take the curl of Ampere’s law _∇×_ **B** = _µ_ 0 **J** _s_ : 



<!-- Start of picture text -->
∇×  ( ∇×  B ) =  µ 0( ∇×  J s ) (56)<br><!-- End of picture text -->

- Apply the vector identity _∇×_ ( _∇×_ **B** ) = _∇_ ( _∇·_ **B** ) _−∇_<sup>2</sup> **B** and use Gauss’s law for magnetism ( _∇·_ **B** = 0): 



<!-- Start of picture text -->
−∇ 2 B  =  µ 0( ∇×  J s ) (57)<br><!-- End of picture text -->

Substitute London’s second equation into this relation: 



<!-- Start of picture text -->
−∇ 2 B  =  µ 0 � − n m se 2 B � = ⇒∇ 2 B  = µ 0 m nse 2 B  ≡ λ 12 L B (58)<br><!-- End of picture text -->

This second-order differential equation proves that the magnetic field decays exponentially inside a superconductor, penetrating only within a thin surface boundary layer of thickness _λL_ . 

16 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

### **4. Problem-Solving Algorithm** 

#### **Solving Temperature-Dependent Critical Fields and Penetration Depths** 

1. **Calculate Critical Field at Temperature** _T_ **:** Given the critical temperature _TC_ and the critical field at absolute zero _Hc_ (0), calculate the critical field at temperature _T_ : 



<!-- Start of picture text -->
Hc ( T ) =  Hc (0) 1  − (59)<br>� TTC<br>� �2 �<br><!-- End of picture text -->

2. **Solve for** _T_ **or** _TC_ **:** If _Hc_ ( _T_ ) is given, find the operating temperature: 



<!-- Start of picture text -->
T =  TC 1  − Hc ( T ) (60)<br>� Hc (0)<br><!-- End of picture text -->

3. **Calculate the Penetration Depth at Temperature** _T_ **:** Given the penetration depth at absolute zero _λ_ (0), calculate: 



<!-- Start of picture text -->
λ (0)<br>λ ( T ) = (61)<br>1  − T<br>� � TC �4<br><!-- End of picture text -->

4. **Determine Ginzburg-Landau Classification:** Compute the Ginzburg-Landau parameter: _κ_ =<sup>_λL_</sup> (62) _ξ_ 

where _ξ_ is the coherence length (representing Cooper pair size). 

5. **Classify the Superconductor:** 



<!-- Start of picture text -->
 If κ <  1 / √ 2  ≈ 0 . 707, the material is a **Type-I superconductor**.<br> If κ >  1 / √ 2  ≈ 0 . 707, the material is a **Type-II superconductor**.<br><!-- End of picture text -->

### **5. Connections to Macroscopic Observables** 

-  **The Thermodynamic Specific Heat Jump:** The transition of a metal into a superconducting phase is a second-order thermodynamic phase transition. At _T_ = _TC_ , the specific heat capacity _CV_ exhibits a sharp discontinuous jump. Below _TC_ , the specific heat decays exponentially: 

_CV ∝ e_<sup>_−_∆</sup><sup>_/kBT_</sup> (63) 

This exponential decay is the direct macroscopic proof of the presence of a finite energy gap 2∆at the Fermi surface, which protects Cooper pairs from thermal scattering. 

-  **The Josephson Junction Effect (SQUIDs):** Placing a thin insulating barrier between two superconductors forms a Josephson junction. Under a DC bias, a supercurrent tunnels through the barrier. Josephson junctions are highly sensitive to external magnetic fields, allowing for the construction of **SQUIDs** (Superconducting Quantum Interference De- 

17 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

vices) which can resolve extremely small magnetic fields ( _∼_ 10<sup>_−_15</sup> T), with applications in magnetocardiography and quantum computing. 

### **6. Crucial Pitfalls** 

#### **Superconductivity Pitfalls to Avoid** 

-  **The Cooper Pair Electron Charge Trap:** Forgetting the factor of **2** in the electron charge in the flux quantum formula: 



<!-- Start of picture text -->
Φ0 = h (64)<br>2 e<br><!-- End of picture text -->

A common error in GATE numerical questions is using _e_ instead of 2 _e_ in the denominator, which causes calculated flux quantization values to be off by a factor of 2. The 2 _e_ term is a direct physical consequence of electron pairing in BCS theory. 

-  **Conflating Perfect Conductors with Superconductors:** Assuming that a hypothetical ”perfect conductor” with zero resistivity is equivalent to a superconductor. A perfect conductor preserves the existing magnetic flux inside it ( _d_ **B** _/dt_ = 0), whereas a superconductor actively expels all magnetic flux ( **B** = 0) upon cooling below _TC_ (Meissner effect). 

-  **Incorrect Coordinate Decays:** When solving _∇_<sup>2</sup> _B_ = _B/λ_<sup>2</sup> for a 1D interface, write the spatial decay as _B_ 0 _e_<sup>_−x/λ_</sup> , not _B_ 0 _e_<sup>_−x_2</sup><sup>_/λ_2</sup> . 

### **7. Standard Textbook Systems** 

-  **Mercury (Hg):** The historical birthplace of superconductivity, discovered by Heike Kamerlingh Onnes in 1911. It is a prototypical Type-I superconductor with a critical temperature _TC ≈_ 4 _._ 15 K. 

-  **Niobium-Tin (Nb** 3 **Sn):** A highly critical Type-II superconductor ( _TC ≈_ 18 _._ 3 K) with an upper critical field of _Hc_ 2 _≈_ 30 T at absolute zero, making it the premier material for winding high-field superconducting electromagnets used in MRI systems and particle accelerators. 

18 

GATE PHYSICS 

DIELECTRICS, MAGNETISM, & SUPERCONDUCTIVITY 

## **References** 

1. Kittel, Charles. _Introduction to Solid State Physics_ . Wiley, 2005. 

2. Pillai, S. O. _Solid State Physics_ . New Age International, 2010. 

3. Griffiths, David J. _Introduction to Electrodynamics_ . Prentice Hall, 1999. 

19 

