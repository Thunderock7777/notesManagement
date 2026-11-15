<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-multiple-eigenvalues-eigenstates-comp.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

## **No, having multiple eigenstates and having multiple eigenvalues are NOT the same thing!** 

While they are closely related, they describe two completely different concepts in quantum mechanics—one is a **physical state (a wave shape)** , and the other is a **measurable number (a value)** . 

## **1. What Do They Mean Physically?** 

Think of a quantum system like a vibrating guitar string: 

- **Eigenstate (The Wave Pattern / Orbital Cloud):** 

   - **What it is:** A specific **physical state or wave pattern** ( _ψ_ ( _⃗r_ )) in which the electron can exist. 

   - **Physical Meaning:** It tells you **WHERE** the electron cloud is located and **HOW** its probability density is distributed in space. 

   - **Analogy:** The specific physical shape of the standing wave on a vibrating guitar string. 

- **Eigenvalue (The Measurable Number):** 

   - **What it is:** A single, sharp **numerical value** ( _En_ , _Lz_ , etc.) produced when an operator acts on an eigenstate. 

   - **Physical Meaning:** It is the **exact meter reading** you get on your experimental detector when you measure a physical property (like energy or angular momentum) for that state. 

   - **Analogy:** The exact musical pitch or frequency (e.g., 440 Hz) produced by that vibrating string. 

## **2. Why Are They Not Always the Same?** 

The key reason they are not identical is **Degeneracy** : 

**Case 1: Multiple Eigenstates** _→_ **ONE Eigenvalue (Degeneracy)** You can have **multiple different spatial states (eigenstates)** that happen to yield the **exact same measurement value (eigenvalue)** . 

- **Example in Hydrogen (** _n_ = 2 **):** 

Notes 

2 

- **4 Distinct Eigenstates:** The 2 _s_ , 2 _px_ , 2 _py_ , and 2 _pz_ orbitals have completely different shapes and spatial directions in space. 

- **1 Shared Eigenvalue:** Yet, all four share the **exact same energy eigenvalue** : _E_ = _−_ 3 _._ 4 eV 

- **Physical picture:** You have 4 different physical electron clouds, but measuring the energy of any of them gives the exact same reading of _−_ 3 _._ 4 eV. 

**Case 2: Multiple Eigenstates** _→_ **MULTIPLE Eigenvalues (Non-Degenerate)** This occurs when every distinct state has its own unique measurement reading. 

- **Example in the Zeeman Effect:** 

   - When you turn on a magnetic field ( _B >_ 0), the symmetry is broken. 

   - The three 2 _p_ orbitals ( _ml_ = +1 _,_ 0 _, −_ 1) now split into **3 distinct energy eigenvalues** : 



<!-- Start of picture text -->
E +1 =  E 0 +  µBB<br>E 0 =  E 0<br><!-- End of picture text -->



<!-- Start of picture text -->
E− 1 =  E 0  − µBB<br><!-- End of picture text -->

- **Physical picture:** Now, each of the 3 different electron clouds gives a different numerical reading on your energy detector. 

## **Summary Comparison** 

|Term|What is it?|Physical Meaning|Example in Hydrogen<br>(_n_= 2_, B_ = 0)|
|---|---|---|---|
|**Eigenstate**|Wavefunction (_ψn_)|The **physical**<br>**shape/pattern** of<br>the electron cloud.|2_s,_2_px,_2_py,_2_pz_ (**4**<br>**states**)|
|**Eigenvalue**|Real Number (_En_)|The **exact meter**<br>**reading** from a<br>measurement.|_−_3_._4 eV (**1 shared**<br>**energy value**)|



- **Key Takeaway:** 

   - Every distinct eigenvalue has at least one eigenstate. 

   - But a single eigenvalue can belong to **multiple eigenstates** (Degeneracy). 

