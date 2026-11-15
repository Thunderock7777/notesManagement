<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-g-hkl-dbt.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

To clear up this confusion, it helps to distinguish between a **plane** and a **vector** : 

1. **The Plane** ( _hkl_ ) **is defined ONLY in real space using** _⃗a_ 1 _,⃗a_ 2 _,⃗a_ 3. 

2. _⃗Ghkl_ = _h⃗b_ 1 + _k⃗b_ 2 + _l⃗b_ 3 **is NOT a plane!** It is a **VECTOR** residing in reciprocal space. 

When we say _“⃗Ghkl is reciprocal to the plane_ ( _hkl_ ) _”_ , it means that **the vector** _⃗Ghkl_ **points in a direction strictly PERPENDICULAR (normal) to the real-space plane** ( _hkl_ ). 

**Step-by-Step Proof: Why** _⃗Ghkl_ **is Perpendicular to Plane** ( _hkl_ ) 

**1. How the Plane is Defined in Real Space (** _⃗a_ 1 _,⃗a_ 2 _,⃗a_ 3 **)** By definition of Miller indices, a crystal plane ( _hkl_ ) intersects the real-space crystallographic axes _⃗a_ 1 _,⃗a_ 2 _,⃗a_ 3 at three points: 



<!-- Start of picture text -->
A  = ⃗ a 1 B = ⃗ a 2 C = ⃗ a 3<br>h , k , l<br><!-- End of picture text -->

**2. Construct Vectors Lying Inside the Plane** Any vector connecting two points in this plane lies **completely inside the plane** . 

- Vector connecting point _A_ to point _B_ : 



<!-- Start of picture text -->
v 1 =  B − A  = ⃗ a k 2 −⃗a h 1<br><!-- End of picture text -->

- Vector connecting point _B_ to point _C_ : 



<!-- Start of picture text -->
v 2 =  C − B = ⃗ a l 3 −⃗a k 2<br><!-- End of picture text -->

**3. Test if** _⃗Ghkl_ **is Perpendicular to the Plane** Recall the fundamental definition connecting real space _⃗ai_ and reciprocal space _⃗bj_ : 



<!-- Start of picture text -->
 a 1  ·⃗b 1 = 2 π,⃗ a 1  ·⃗b 2 = 0 ,⃗<br><br> a 1  ·⃗b 3 = 0<br>ai ·⃗bj = 2 πδij = ⇒<br><br> a 2  ·⃗b 2 = 2 π,⃗ a 2  ·⃗b 1 = 0 ,<br><br><br> . . .<br><!-- End of picture text -->

Notes 

2 

Now, take the dot product of _⃗Ghkl_ = _h⃗b_ 1 + _k⃗b_ 2 + _l⃗b_ 3 with the plane vector _⃗v_ 1: 



<!-- Start of picture text -->
Ghkl ·⃗v 1 = ( h⃗b 1 +  k⃗b 2 +  l⃗b 3)  ·<br>k −⃗a h 1<br>( ⃗a 2 )<br><!-- End of picture text -->

Expanding the terms: 



<!-- Start of picture text -->
Ghkl ·⃗v 1 =  h⃗b 1  · −⃗ a 1 +  k⃗b 2  · =  − b 1  ·⃗a 1 + b 2  ·⃗a 2<br>h k ( ) ( )<br>( ) ( ⃗a 2 )<br>Ghkl ·⃗v 1 =  − 2 π  + 2 π =  0<br><!-- End of picture text -->

Similarly, taking the dot product with _⃗v_ 2 gives: 



<!-- Start of picture text -->
Ghkl ·⃗v 2 = 0<br><!-- End of picture text -->

## **Conclusion** 

Because the dot product of _⃗Ghkl_ with any vector lying inside the plane ( _hkl_ ) is strictly zero, _⃗Ghkl_ **is the normal vector (perpendicular) to the real-space plane** ( _hkl_ ). 

- **Real Space (** _⃗a_ 1 _,⃗a_ 2 _,⃗a_ 3 **):** Where the physical **Plane** ( _hkl_ ) exists. 

- **Reciprocal Space (** _⃗b_ 1 _,⃗b_ 2 _,⃗b_ 3 **):** Where the **Vector** _⃗Ghkl_ lives, pointing perpendicular to that plane with length _|⃗Ghkl|_ = _d_ <u>2</u> _hklπ_<sup>.</sup> 

