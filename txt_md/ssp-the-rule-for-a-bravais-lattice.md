<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-the-rule-for-a-bravais-lattice.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**No — graphene’s honeycomb arrangement of carbon atoms is NOT a Bravais lattice.** Instead, graphene is a **crystal structure** formed by a **2D hexagonal Bravais lattice combined with a two-atom basis** . 

## **1. The Rule for a Bravais Lattice** 

By definition, a **space (Bravais) lattice** is a set of mathematical points where **the surroundings look completely identical from every single point** when you jump from one point to another by a pure integer translation **T** = _u_ 1 **a** 1 + _u_ 2 **a** 2 (where _u_ 1 _, u_ 2 are integers). 

You are **not** allowed to rotate or flip your viewpoint when checking if two points are equivalent—only straight-line shifting (translation) is allowed. 

## **2. Why Graphene’s Honeycomb Fails This Test** 

In graphene, every atom is an identical _sp_<sup>2</sup> -bonded carbon atom, which makes it look like a Bravais lattice at first glance. However, look at two neighbouring carbon atoms in the honeycomb sheet—call them **Atom A** and **Atom B** : 

- Stand on **Atom A** : its three nearest-neighbour bonds point **straight down, upleft, and up-right** (like an upright **Y** ). 

- Slide directly over to its neighbour **Atom B** (without rotating): its three nearestneighbour bonds point **straight up, down-left, and down-right** (like an upsidedown **Y** ). 

\ / | (A) (B) | / \ Upright ”Y” Flipped ”Y” (180<sup>_◦_</sup> rotated) 

Because **Atom A** and **Atom B** do **not** have the same surrounding bond directions under pure translation, the full set of carbon atom positions in graphene **cannot be a Bravais lattice** . 

## **3. How Crystal** = **Lattice** + **Basis Fixes It** 

To describe graphene properly, we separate the pure translational grid from the pair of flipped atoms: 

Notes 

2 

1. **The Bravais Lattice** : Keep only the atoms that have the _exact same_ orientation (for instance, just the upright **Y** atoms). As shown in Kittel’s diagram of the graphene sheet, the primitive translation vectors **a** 1 and **a** 2 skip the immediate neighbour and connect only these equivalent sites. This underlying grid is one of the five true 2D Bravais lattices—specifically the **2D hexagonal Bravais lattice** ( _|_ **a** 1 _|_ = _|_ **a** 2 _|_ with an interaxial angle of 120<sup>_◦_</sup> , whose points form equilateral triangles). _(In physics, this 2D Bravais lattice is often informally called a “triangular lattice” because of those equilateral triangles, while Kittel names it the 2D hexagonal lattice.)_ 

2. **The Basis** : Attach a **two-atom basis** (one **A** carbon atom + one **B** carbon atom) to every single point on that 2D hexagonal Bravais lattice. 

## **4. Why This Matters for GATE Physics** 

This exact same trick shows up in 3D crystal structures even when all atoms are the same element: 

- **Diamond (C, Si, Ge)** : All atoms are identical, yet diamond is **not** a Bravais lattice—it is an **FCC Bravais lattice with a 2-atom basis** . 

- **HCP (Mg, Zn)** : Every atom has 12 nearest neighbours, yet the atom positions do not form a space lattice—it is a **simple hexagonal Bravais lattice with a 2-atom basis** . 

Does that distinction between the lattice and the atomic positions make sense now? If you’d like, we can trace how the **2-atom basis in diamond or HCP** creates systematic absences in X-ray diffraction next. 

