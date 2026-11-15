<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-3d-cubic-box-energy-degeneracy.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**Correct Answer** 

## **6** 

## **Detailed Step-by-Step Solution** 

**1. Energy Expression for a 3D Cubic Box** The energy eigenvalues for a particle of mass _m_ in a 3D cubic box of side _L_ are given by: 



<!-- Start of picture text -->
Enx,ny,nz = π 2 h ¯2 ( n 2 x +  n 2 y +  n z 2 ) =  E 0 ( n 2 x +  n 2 y +  n z 2 )<br>2 mL 2<br><!-- End of picture text -->

_<u>π</u>_<sup>2</sup> _<u>h</u>_ ¯<sup>2</sup> where _E_ 0 = 2 _mL_<sup>2istheenergyfactor,and</sup><sup>_nx, ny, nz∈{_1</sup><sup>_,_2</sup><sup>_,_3</sup><sup>_, . . . }_arepositiveintegers</sup> representing the quantum numbers along each spatial dimension. 

The energy level is determined by the sum of squares: 



<!-- Start of picture text -->
S =  n 2 x +  n 2 y +  n z 2<br><!-- End of picture text -->

**2. Order of Energy Levels (from Ground State upwards)** We determine the sequence of energy levels by finding all combinations of positive integers ( _nx, ny, nz_ ) and arranging the total sum _S_ in strictly increasing order: 

1. **Ground State (** _S_ = 3 **):** 

   - State: (1 _,_ 1 _,_ 1) 

   - Sum: 1<sup>2</sup> + 1<sup>2</sup> + 1<sup>2</sup> = 3 

   - **Degeneracy = 1** 

2. 1<sup>**st**</sup> **Excited State (** _S_ = 6 **):** 

   - States: (2 _,_ 1 _,_ 1) _,_ (1 _,_ 2 _,_ 1) _,_ (1 _,_ 1 _,_ 2) 

   - Sum: 2<sup>2</sup> + 1<sup>2</sup> + 1<sup>2</sup> = 6 

   - **Degeneracy = 3** 

3. 2<sup>**nd**</sup> **Excited State (** _S_ = 9 **):** 

   - States: (2 _,_ 2 _,_ 1) _,_ (2 _,_ 1 _,_ 2) _,_ (1 _,_ 2 _,_ 2) 

   - Sum: 2<sup>2</sup> + 2<sup>2</sup> + 1<sup>2</sup> = 9 

   - **Degeneracy = 3** 

Notes 

2 

4. 3<sup>**rd**</sup> **Excited State (** _S_ = 11 **):** 

   - States: (3 _,_ 1 _,_ 1) _,_ (1 _,_ 3 _,_ 1) _,_ (1 _,_ 1 _,_ 3) 

   - Sum: 3<sup>2</sup> + 1<sup>2</sup> + 1<sup>2</sup> = 11 

- **Degeneracy = 3** 

- 5. 4<sup>**th**</sup> **Excited State (** _S_ = 12 **):** 

   - State: (2 _,_ 2 _,_ 2) 

   - Sum: 2<sup>2</sup> + 2<sup>2</sup> + 2<sup>2</sup> = 12 

   - **Degeneracy = 1** 

6. 5<sup>**th**</sup> **Excited State (** _S_ = 14 **):** 

   - States: Permutations of (1 _,_ 2 _,_ 3) 

   - Sum: 1<sup>2</sup> + 2<sup>2</sup> + 3<sup>2</sup> = 1 + 4 + 9 = 14 

   - Since all three quantum numbers are distinct (1 _,_ 2 _,_ 3), the total number of distinct permutations is: 

Degeneracy = 3! = 6 

- The 6 distinct states are: 

(1 _,_ 2 _,_ 3) _,_ (1 _,_ 3 _,_ 2) _,_ (2 _,_ 1 _,_ 3) _,_ (2 _,_ 3 _,_ 1) _,_ (3 _,_ 1 _,_ 2) _,_ (3 _,_ 2 _,_ 1) 

## **Summary Table: Energy Levels in a 3D Cubic Box** 

|Energy Level|_S_ =_n_<sup>2</sup><br>_x_ <sup>+</sup><sup>_n_2</sup><br>_y_ <sup>+</sup><sup>_n_2</sup><br>_z_|Energy (_E_)|Possible State<br>Triples<br>(_nx, ny, nz_)<br>Dege|neracy (_g_)|
|---|---|---|---|---|
|**Ground State**|3|3_E_0|(1_,_1_,_1)|1|
|1<sup>**st **</sup>**Excited**<br>**State**|6|6_E_0|(2_,_1_,_1)_,_(1_,_2_,_1)_,_(1_,_1_,_2)|3|
|2<sup>**nd **</sup>**Excited**<br>**State**|9|9_E_0|(2_,_2_,_1)_,_(2_,_1_,_2)_,_(1_,_2_,_2)|3|
|3<sup>**rd **</sup>**Excited**<br>**State**|11|11_E_0|(3_,_1_,_1)_,_(1_,_3_,_1)_,_(1_,_1_,_3)|3|
|4<sup>**th **</sup>**Excited**<br>**State**|12|12_E_0|(2_,_2_,_2)|1|
|5<sup>**th **</sup>**Excited**<br>**State**|14|14_E_0|(1_,_2_,_3) **and its**<br>**6**<br>**permutations**|**6**|



**Follow-up suggestion:** Would you like to practice calculating the degeneracy for higher energy levels (such as _S_ = 27 or _S_ = 66) or explore how degeneracy changes when the box dimensions are non-cubic (e.g., _Lx_ = _Ly_ = _L, Lz_ = 2 _L_ )? 

