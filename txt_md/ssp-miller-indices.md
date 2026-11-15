<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-miller-indices.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **1. What are Miller Indices?** 

A crystal is made of a periodic, 3D array of atoms. Within this array, we can draw infinite sets of parallel, equally spaced imaginary flat surfaces passing through lattice points. These are called **crystal planes** or **lattice planes** . 

**Miller Indices** —denoted by three integers inside parentheses ( _hkl_ )—provide a universal mathematical notation to uniquely specify the **orientation of a set of parallel planes** relative to the unit cell axes. 

**2. How to Find Miller Indices** ( _hkl_ ) **— Step-by-Step** 

To determine the Miller indices for any plane: 

1. **Find Intercepts:** Identify where the plane cuts the crystal axes _x, y, z_ in terms of unit cell dimensions _a, b, c_ . _Example Intercepts:_ 2 _a,_ 3 _b,_ 1 _c_ = _⇒_ (2 _,_ 3 _,_ 1). 

2. **Take Reciprocals:** Take the inverse of these fractional intercept values. _Reciprocals:_ ( 12<sup>_,_</sup><sup><u>1</u></sup> 3<sup>_,_</sup> 1<sup><u>1</u></sup> ). 

3. **Clear Fractions:** Multiply by the Lowest Common Multiple (LCM) of the denominators to convert them into the smallest set of whole numbers. _LCM is 6:_ ( 12<sup>_×_6</sup><sup>_,_</sup><sup><u>1</u></sup> 3<sup>_×_6</sup><sup>_,_1</sup><sup>_×_6</sup> ) = (3 _,_ 2 _,_ 6). 

4. **Enclose in Parentheses:** Write the resulting set as (326). 

## **Special Cases to Remember:** 

- **Plane parallel to an axis:** The intercept is at infinity ( _∞_ ), so its reciprocal is zero (1/ _∞_ = 0). _Example:_ A plane parallel to the _y_ and _z_ axes intersects _x_ at 1 _a_ , _y_ at _∞_ , and _z_ at 

   - _∞_ . 

Intercepts: (1 _, ∞, ∞_ ) = _⇒_ Reciprocals: (1 _,_ 0 _,_ 0) = _⇒_ Miller Index: (100). 

- **Negative Intercepts:** If a plane cuts an axis on the negative side, a bar is placed over the index (e.g., (<sup>¯</sup> 100) read as “bar 1 zero zero”). 

Notes 

2 

## **3. Key Notation Standards in Crystallography** 

|Notation|Type|Meaning|
|---|---|---|
|(_hkl_)|**Specific Plane**|Represents a single plane or a<br>set of parallel planes.|
|_{hkl}_|**Family of Planes**|Represents all<br>crystallographically<br>equivalent planes by<br>symmetry. _(e.g., {_100_}_<br>_includes_<br>(100)_,_(010)_,_(001)_,_(<sup>¯</sup>100)_,_(0<sup>¯</sup>10)_,_(00<sup>¯</sup>1)_)_.|
|[_uvw_]|**Specific Direction**|Vector pointing along a<br>direction inside the crystal.|
|_⟨uvw⟩_|**Family of Directions**|All symmetry-equivalent<br>directions.|



**GATE Trap:** In **cubic crystals** , the direction [ _hkl_ ] is strictly perpendicular to the plane ( _hkl_ ). **This does not hold true for non-cubic crystal systems** (like monoclinic or triclinic). 

## **4. Interplanar Distance (** _dhkl_ **)** 

**What is** _dhkl_ **? Interplanar distance (** _dhkl_ **)** is the **perpendicular separation distance** between two consecutive, adjacent parallel planes belonging to the same Miller index family ( _hkl_ ). 

**Formulas for** _dhkl_ **:** 

1. **Cubic Crystal (** _a_ = _b_ = _c_ **):** 



<!-- Start of picture text -->
a<br>dhkl =<br>√ h 2 +  k 2 +  l 2<br><!-- End of picture text -->

2. **Orthorhombic Crystal (** _a̸_ = _b̸_ = _c, α_ = _β_ = _γ_ = 90<sup>_◦_</sup> **):** 



<!-- Start of picture text -->
1 = h 2<br>d 2 a 2 + k b 22 + c l 22<br>hkl<br><!-- End of picture text -->

3. **Connection to Reciprocal Lattice Vector (** _⃗G_ **):** The reciprocal lattice vector _Ghkl_ = _h⃗b_ 1 + _k⃗b_ 2 + _l⃗b_ 3 is strictly normal to the plane ( _hkl_ ), and its magnitude relates directly to _dhkl_ : 



<!-- Start of picture text -->
2 π<br>dhkl =<br>|⃗Ghkl|<br><!-- End of picture text -->

Notes 

3 

**5. Classic GATE Practice Concept: Ratio of** _dhkl_ **in Simple Cubic** 

For a **Simple Cubic (SC)** crystal with lattice parameter _a_ : 



<!-- Start of picture text -->
• d 100 = a<br>√ 1 2 +0 2 +0 2 =  a<br>• d 110 = a a<br>√ 1 2 +1 2 +0 2 = √ 2<br>• d 111 = a a<br>√ 1 2 +1 2 +1 2 = √ 3<br><!-- End of picture text -->

Ratio of interplanar spacings: 



<!-- Start of picture text -->
d 100 :  d 110 :  d 111 = 1 : √ 1 2 : √ 1 3 = √ 6 : √ 3 : √ 2<br><!-- End of picture text -->

_Now that Miller Indices and dhkl are crystal clear, would you like to solve a numerical problem on Bragg’s law (_ 2 _d_ sin _θ_ = _λ) using dhkl, or continue to_ **_Reciprocal Lattice & Structure Factors_** _?_ 

