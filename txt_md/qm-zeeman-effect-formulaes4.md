<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-zeeman-effect-formulaes4.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**1. What is the Magnetic Interaction Hamiltonian (** _H_<sup>ˆ</sup> **mag)?** 

In classical physics, the potential energy _U_ of a magnet with dipole moment _⃗µ_ placed in a magnetic field _⃗B_ is: 



<!-- Start of picture text -->
U =  −⃗µ ·⃗B<br><!-- End of picture text -->

In quantum mechanics, the **Hamiltonian** ( _H_<sup>ˆ</sup> ) is simply the **total energy operator** of a system. 

When you place an atom in a magnetic field, it gains extra magnetic potential energy. The **magnetic interaction Hamiltonian** ( _H_<sup>ˆ</sup> mag) is the quantum operator corresponding to that extra magnetic potential energy: 



<!-- Start of picture text -->
H ˆ mag =  −⃗µ ˆ J ·⃗B = µBB ( L ˆ z  + 2  S ˆ z )<br>h ¯<br><!-- End of picture text -->

## **2. Is it an Operator?** 

**Yes, absolutely.** In quantum mechanics, physical quantities like position, momentum, angular momentum, and energy are not simple numbers—they are **operators** ( _x,_ ˆ ˆ _p, L_<sup>ˆ</sup> _z, H_<sup>ˆ</sup> ). 

An operator is a mathematical instruction that “acts” on a quantum state (a wavefunction or ket vector _|ψ⟩_ ) to extract physical information. 

## **3. Why is the Energy Shift the Expectation Value?** 

Because _H_<sup>ˆ</sup> mag is an operator, it doesn’t automatically give you a single plain number. To get an actual measurable energy number (in Joules or eV), you must evaluate its **expectation value** —which is the quantum mechanical average value of an operator for a system in a state _|ψ⟩_ : 

Average Energy = _⟨ψ|H_<sup>ˆ</sup> mag _|ψ⟩_ 

According to **First-Order Perturbation Theory** , if you add a small extra energy term _H_ ˆ<sup>_′_</sup> to an unperturbed system with state _|n_<sup>(0)</sup> _⟩_ , the first-order change in energy (∆ _E_ ) is calculated as: 



<!-- Start of picture text -->
∆ E =  ⟨n (0) |H ˆ ′ |n (0) ⟩<br><!-- End of picture text -->

Notes 

2 

## **4. What Does “Expectation Value in the Unperturbed State” Mean Physically?** 

To picture this intuitively, break it down into two concepts: 

**A. What is the “Unperturbed State” (** _|n_<sup>(0)</sup> _⟩_ **)?** This is the electron’s state **before** you turn on the magnetic field. It describes the electron’s pre-existing wavefunction/cloud around the nucleus, specified by quantum numbers like _|j, mj, l, s⟩_ . 

**B. What does taking the expectation value in that state mean?** In quantum mechanics, an electron isn’t a sharp point orbiting on a fixed track—it is a probabilistic “wave cloud.” 

When we say _“the energy shift is the expectation value of H_<sup>ˆ</sup> _mag in the unperturbed state,”_ it physically means: 

- **“We assume the external magnetic field is weak enough that it doesn’t distort or reshape the electron’s wavefunction cloud. To find the extra magnetic energy, we simply calculate the average value of the magnetic energy operator (** _H_<sup>ˆ</sup> **mag) over the electron’s pre-existing, undistorted electron cloud (** _|j, mj⟩_ **).”** 

## **Summary Table** 

|Term|What it is|Physical Meaning|
|---|---|---|
|ˆ_H_**mag**|Magnetic Interaction<br>Operator|The quantum instruction<br>representing extra magnetic<br>potential energy (_−_<sup>ˆ</sup><sup>_⃗_</sup>_µ ·⃗B_).|
|**Unperturbed State** _|n_<sup>(0)</sup>_⟩_|Baseline Wavefunction|The undistorted electron<br>state/cloud before turning on<br>the external field.|
|**Expectation Value**<br>_⟨n_<sup>(0)</sup>_|_ <sup>ˆ</sup>_H_**mag**_|n_<sup>(0)</sup>_⟩_|Quantum Average Energy<br>(∆_E_)|The weighted average of the<br>magnetic energy operator<br>over the undistorted electron<br>cloud.|



Does this make the quantum mechanical picture and the need for expectation values clearer? 

