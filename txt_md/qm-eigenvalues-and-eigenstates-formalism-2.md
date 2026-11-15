<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-eigenvalues-and-eigenstates-formalism-2.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Here is a comprehensive summary of quantum state formalism, Hilbert space structure, the Bloch sphere, time evolution, and phase dynamics. 

## **Detailed Summary Notes on Quantum States** 

**1. State Representation & Hilbert Space (** _H_ **)** 

   - **State Vector (** _|ψ⟩_ **):** In quantum mechanics, the complete physical state of an isolated system is represented by a unit vector _|ψ⟩_ (called a _ket_ ) belonging to a complex vector space equipped with an inner product, known as a **Hilbert space** ( _H_ ). 

   - **Dual Space (** _⟨ψ|_ **):** For every ket vector _|ψ⟩∈H_ , there exists a corresponding dual vector _⟨ψ|_ (called a _bra_ ) in the dual Hilbert space _H_<sup>_∗_</sup> . The inner product _⟨ϕ|ψ⟩_ satisfies _⟨ϕ|ψ⟩_ = _⟨ψ|ϕ⟩_<sup>_∗_</sup> . 

   - **Normalization & Completeness:** 

      - **Normalization:** _⟨ψ|ψ⟩_ = 1, ensuring the sum of probabilities over all outcomes equals 1. 

      - **Discrete Basis Expansion:** Any state vector can be expanded as a linear superposition over an orthonormal basis _{|n⟩}_ : 

_|ψ⟩_ = ∑ _cn|n⟩_ where _cn_ = _⟨n|ψ⟩_ and ∑ _|cn|_<sup>2</sup> = 1 _n n_ 

**– Completeness (Closure Relation):** ∑ _n_<sup>_|n⟩⟨n|_</sup> = _I_ ˆ (discrete) or ∫ _|x⟩⟨x|dx_ = _I_<sup>ˆ</sup> (continuous). 

## **2. Global Phase vs. Relative Phase** 

- **Global Phase (** _e_<sup>_iγ_</sup> **):** Multiplying an entire state vector by a complex phase factor _e_<sup>_iγ_</sup> yields _|ψ_<sup>_′_</sup> _⟩_ = _e_<sup>_iγ_</sup> _|ψ⟩_ . 

   - **Physical Effect: Unobservable.** Expectation values _⟨A_<sup>ˆ</sup> _⟩_ = _⟨ψ_<sup>_′_</sup> _|A_<sup>ˆ</sup> _|ψ_<sup>_′_</sup> _⟩_ = _⟨ψ|A_<sup>ˆ</sup> _|ψ⟩_ and measurement probabilities _|⟨ϕ|ψ_<sup>_′_</sup> _⟩|_<sup>2</sup> = _|⟨ϕ|ψ⟩|_<sup>2</sup> are completely invariant. 

- **Relative Phase (** _e_<sup>_iϕ_</sup> **):** The phase difference between distinct orthonormal components in a superposition state, e.g., _|ψ⟩_ = _c_ 1 _|_ 0 _⟩_ + _c_ 2 _e_<sup>_iϕ_</sup> _|_ 1 _⟩_ . 

Notes 

2 

**– Physical Effect: Observably vital.** Controls quantum interference patterns, determines physical orientation (such as spin direction on the _x_ - _y_ plane), and alters transition probabilities. 

**3. The Bloch Sphere (Two-Level System / Qubit Space)** A normalized state of a two-level quantum system (such as spin-1/2 or a qubit) can be parameterized on the surface of a unit sphere up to an unobservable global phase: 



<!-- Start of picture text -->
|ψ ( θ, ϕ ) ⟩ = cos | 0 ⟩ +  e iϕ sin | 1 ⟩<br>2 2<br>( θ ) ( θ )<br><!-- End of picture text -->

where _θ ∈_ [0 _, π_ ] is the polar angle and _ϕ ∈_ [0 _,_ 2 _π_ ) is the azimuthal angle. 

   - **Key Landmarks on the Bloch Sphere:** 

      - **North Pole (** _θ_ = 0 **):** Eigenstate _|_ 0 _⟩_ = _|_ + _z⟩_ . 

      - **South Pole (** _θ_ = _π_ **):** Eigenstate _|_ 1 _⟩_ = _| − z⟩_ . 

      - **Equator (** _θ_ = _π_ /2 **):** Equal-weight superpositions such as _|_ + _x⟩_ = _<u>|</u>_ 0 _<u>⟩</u>_ _~~√~~_ <u>+2</u> _<u>|</u>_ 1 _<u>⟩</u>_ ( _ϕ_ = 0) and _|_ + _y⟩_ =<sup>_<u>|</u>_0</sup><sup>_<u>⟩</u>_</sup> _~~√~~_<sup><u>+</u></sup> 2<sup>_i|_1</sup><sup>_<u>⟩</u>_</sup> ( _ϕ_ = _π_ /2). 

   - **Orthogonality Property:** Antipodal (opposite) points on the Bloch sphere correspond to mutually orthogonal state vectors in Hilbert space ( _⟨_ **n** 1 _|_ **n** 2 _⟩_ = 0 when ∆ _θ_ = _π_ ). 

**4. Eigenstates, Eigenvalues, & Stationary States** 

   - **Eigenvalue Equation:** An observable represented by a self-adjoint (Hermitian) operator _A_<sup>ˆ</sup> satisfies _A_<sup>ˆ</sup> _|an⟩_ = _an|an⟩_ , where the eigenvalue _an_ is strictly real and represents a possible measurement outcome. 

   - **Stationary States (Energy Eigenstates):** Solutions to the Time-Independent Schrödinger Equation (TISE), _H_<sup>ˆ</sup> _|En⟩_ = _En|En⟩_ . 

      - **Temporal Behavior:** Stationary states evolve in time solely through a phase factor: _|_ Ψ _n_ ( _t_ ) _⟩_ = _e_<sup>_−iEnt_/</sup><sup>_h_¯</sup> _|En⟩_ . 

      - **Stationary Property:** The probability density _|_ Ψ _n_ ( _x, t_ ) _|_<sup>2</sup> = _|ψn_ ( _x_ ) _|_<sup>2</sup> and expectation values of all time-independent observables are strictly constant over time. 

**5. Time Evolution & Quantum Dynamics** 

   - **Time-Dependent Schrödinger Equation (TDSE):** 

         - _ih_ ¯<sup>_∂_</sup> _∂t_<sup>_|ψ_(</sup><sup>_t_)</sup><sup>_⟩_=</sup><sup>_H_ˆ</sup><sup>_|ψ_(</sup><sup>_t_)</sup><sup>_⟩_</sup> 

   - **Time-Evolution Operator (** _U_<sup>ˆ</sup> ( _t, t_ 0) **):** Maps an initial state _|ψ_ ( _t_ 0) _⟩_ to a future state _|ψ_ ( _t_ ) _⟩_ = _U_<sup>ˆ</sup> ( _t, t_ 0) _|ψ_ ( _t_ 0) _⟩_ . 



<!-- Start of picture text -->
− i  ˆ H ( t−t 0) .<br>– For a time-independent Hamiltonian H ˆ : U ˆ ( t, t 0) = exp h ¯<br>( )<br><!-- End of picture text -->

Notes 

3 

   - **Unitarity (** _U_<sup>ˆ</sup><sup>_†_ˆ</sup> _U_ = _I_<sup>ˆ</sup> **):** Guarantees probability conservation ( _⟨ψ_ ( _t_ ) _|ψ_ ( _t_ ) _⟩_ = 1 for all _t_ ). 

- **Non-Stationary States (Superpositions):** 



<!-- Start of picture text -->
| Ψ( t ) ⟩ = ∑ cne −iEnt / h ¯ |En⟩<br>n<br><!-- End of picture text -->

In non-stationary states, expectation values of non-commuting observables oscillate at **Bohr transition frequencies** _ωnm_ =<sup>_<u>En−</u>_</sup> _h_ ¯<sup>_<u>Em</u>_</sup> . 

## **Summary Table: Core Quantum State Concepts** 

|Concept|Mathematical<br>Representation|Core Physical<br>Significance|Key Properties &<br>Theorems|
|---|---|---|---|
|**State Vector (Ket)**|_|ψ⟩∈H_ with<br>_⟨ψ∥ψ⟩_= 1|Contains all<br>physically accessible<br>information about<br>the quantum system.|Vector in complex<br>Hilbert space;<br>expands over any<br>complete basis<br>(<sup>∑</sup><br>_n _<sup>_∥n⟩⟨n∥_= ˆ</sup><sup>_I_).</sup>|
|**Global Phase**|_|ψ_<sup>_′_</sup>_⟩_=_e_<sup>_iγ_</sup>_|ψ⟩_|Represents an overall<br>complex phase shift<br>of the entire system<br>state.|**Unobservable**;<br>leaves all expectation<br>values and transition<br>probabilities<br>invariant.|
|**Relative Phase**|_∥ψ⟩_=_c_1_∥_0_⟩_+_c_2_e_<sup>_iϕ_</sup>_∥_1_⟩_|Phase difference<br>between<br>superposition<br>components.|**Observable**; dictates<br>quantum interference,<br>spin orientation, and<br>transition dynamics.|
|**Bloch Sphere**<br>**State**|_∥ψ⟩_=<br>cos <sup>_θ_</sup><br>2<sup>_∥_0</sup><sup>_⟩_+</sup><sup>_eiϕ_ sin</sup> <sup>_θ_</sup><br>2<sup>_∥_1</sup><sup>_⟩_</sup>|Geometric<br>representation of a<br>two-level quantum<br>system<br>(qubit/spin-1/2).|Polar angle _θ_ governs<br>state populations;<br>azimuthal angle _ϕ_<br>governs relative<br>phase.|
|**Eigenstate &**<br>**Eigenvalue**|ˆ_A∥an⟩_=_an∥an⟩_|_an_ is the definite<br>outcome when<br>measuring observable<br>ˆ_A_.|Hermitian operators<br>have real eigenvalues<br>and orthogonal<br>eigenvectors.|
|**Stationary State**|_∥_Ψ_n_(_t_)_⟩_=<br>_e_<sup>_−iEnt_/¯</sup><sup>_h_</sup>_∥ψn⟩_|Pure energy<br>eigenstate<br>( <sup>ˆ</sup>_H∥ψn⟩_=_En∥ψn⟩_).|Probability density<br>_∥_Ψ_n∥_<sup>2 </sup>and all<br>expectation values<br>are time-independent.|
|**Non-Stationary**<br>**State**|_∥_Ψ(_t_)_⟩_=<br>∑<br>_n _<sup>_cne−iEnt_/¯</sup><sup>_h∥En⟩_</sup>|Linear superposition<br>of multiple distinct<br>energy eigenstates.|Expectation values<br>oscillate over time at<br>Bohr transition<br>frequencies<br>_ωnm_ = <sup>_En−Em_</sup><br>¯_h_<br>.|



Notes 

4 

||Mathematical|Core Physical|Key Properties &|
|---|---|---|---|
|Concept|Representation|Significance|Theorems|
|**Time Evolution**<br>**Operator**|ˆ_U_(_t, t_0) =_e_<sup>_−i_ ˆ</sup><sup>_H_(</sup><sup>_t−t_</sup>0<sup>)/¯</sup><sup>_h_</sup>|Propagates quantum<br>states<br>deterministically<br>forward in time.|**Unitary Operator**<br>( <sup>ˆ</sup>_U _<sup>_†_ ˆ</sup>_U_ = <sup>ˆ</sup>_I_);<br>guarantees total<br>probability<br>conservation.|



In a two-level quantum system (such as a spin-1/2 particle or a qubit), the **Pauli spin matrices** **_σ_** = ( _σx, σy, σz_ ) provide the fundamental bridge connecting abstract state vectors in Hilbert space, physical observables, density matrices, and geometric locations on the Bloch sphere. 

Here is the precise mathematical and physical connection between Pauli matrices and quantum states: 

## **1. Basis for Quantum Operators & Observables** 

The three Pauli matrices, along with the 2 _×_ 2 identity matrix _I_ , form a complete orthogonal basis for all 2 _×_ 2 Hermitian operators acting on the two-dimensional state space. 

- **Spin Operators:** The physical spin observables **S**<sup>**^**</sup> = ( _S_<sup>ˆ</sup> _x, S_<sup>ˆ</sup> _y, S_<sup>ˆ</sup> _z_ ) are directly proportional to the Pauli matrices: 

- **^S** =<sup>_h_¯</sup> 2<sup>**_σ_**=</sup><sup>_h_¯</sup> 2<sup>(</sup><sup>_σx_ˆ</sup><sup>_i_+</sup><sup>_σy_ˆ</sup><sup>_j_+</sup><sup>_σzk_ˆ)</sup> 

- • **Algebraic Identities: –** _σi_<sup>2=</sup><sup>_I_=</sup><sup>_⇒S_ˆ</sup> _x_<sup>2=</sup><sup>_S_ˆ</sup> _y_<sup>2=</sup><sup>_S_ˆ</sup> _z_<sup>2=</sup><sup>_<u>h</u>_¯</sup> 4<sup>2</sup><sup>_I_</sup> 

   - Anti-commutation: _{σi, σj}_ = 2 _δijI_ 

   - Commutation: [ _σi, σj_ ] = 2 _iϵijkσk_ 

   - Vector Product Identity: ( **_σ_** _·_ **A** )( **_σ_** _·_ **B** ) = ( **A** _·_ **B** ) _I_ + _i_ **_σ_** _·_ ( **A** _×_ **B** ) 

## **2. Measurement Bases & Eigenstate Coordinates** 

Each Pauli matrix specifies an orthonormal measurement basis in Hilbert space. Measuring a spin component projects an arbitrary state _|ψ⟩_ = _c_ 1 _|_ 0 _⟩_ + _c_ 2 _|_ 1 _⟩_ onto the corresponding Pauli eigenstate: 

- _σz_ **Basis (Computational / Standard Basis):** 



<!-- Start of picture text -->
0<br>σz = = ⇒|  +  z⟩ =  | 0 ⟩ = (+1) , | − z⟩ =  | 1 ⟩ = ( − 1)<br>0 − 1 0 1<br>(1 ) (1) (0)<br>Basis:<br>1<br>σx = = ⇒|  +  x⟩ = | 0 ⟩ + | 1 ⟩ (+1) , | − x⟩ = | 0 ⟩ − | 1 ⟩ ( − 1)<br>(10 0) √ 2 √ 2<br><!-- End of picture text -->

- _σx_ **Basis:** 

Notes 

5 



<!-- Start of picture text -->
• σy Basis:<br><!-- End of picture text -->



<!-- Start of picture text -->
σy = −i = ⇒|  +  y⟩ = | 0 ⟩ +  i| 1 ⟩ (+1) , | − y⟩ = | 0 ⟩ − i| 1 ⟩ ( − 1)<br>(0 i 0 ) √ 2 √ 2<br><!-- End of picture text -->

**General Spin Projection Along Unit Vector** _n_ ˆ **:** For an arbitrary spatial direction _n_ ˆ = (sin _θ_ cos _ϕ,_ sin _θ_ sin _ϕ,_ cos _θ_ ), the projection operator **_σ_** _· n_ ˆ has eigenvalues _±_ 1. The normalized eigenstate for eigenvalue +1 generates the exact **Bloch sphere state** : 



<!-- Start of picture text -->
|χ +(ˆ n ) ⟩ = cos | 0 ⟩ +  e iϕ sin | 1 ⟩<br>2 2<br>( θ ) ( θ )<br><!-- End of picture text -->

## **3. Expectation Values & the Bloch Vector** 

For any normalized pure state _|ψ⟩_ = _c_ 1 _|_ 0 _⟩_ + _c_ 2 _|_ 1 _⟩_ , the expectation values of the three Pauli matrices map the quantum state vector directly to 3D Cartesian coordinates **a** = ( _ax, ay, az_ ) on the Bloch sphere: 



<!-- Start of picture text -->
a  =  ⟨ σ ⟩ = ( ⟨σx⟩, ⟨σy⟩, ⟨σz⟩ )<br><!-- End of picture text -->



<!-- Start of picture text -->
• ax =  ⟨σx⟩ = 2 Re ( c ∗ 1 c 2) → Measures relative phase along the x -axis.<br>• ay =  ⟨σy⟩ = 2 Im ( c 1 ∗c 2) → Measures relative phase along the y -axis.<br>• az =  ⟨σz⟩ =  |c 1 | 2 −|c 2 | 2 → Measures state population difference along the z -axis.<br>For a pure state, | a | 2 =  a 2 x +  a 2 y +  a z 2 = 1.<br><!-- End of picture text -->

## **4. Density Matrix Representation (Pure vs. Mixed Ensembles)** 

The most general 2 _×_ 2 density matrix _ρ_ (describing both pure states and mixed statistical ensembles) can be expanded using Pauli matrices: 



<!-- Start of picture text -->
ρ  = 1 2 ( I +  a  ·  σ ) = 1 2 ( a 1 + x  +  a iazy a 1 x − − aiazy )<br><!-- End of picture text -->

where **a** = _⟨_ **_σ_** _⟩_ = Tr( _ρ_ **_σ_** ) is the **Bloch vector** : 

- **Pure State:** _|_ **a** _|_ = 1 = _⇒_ Tr( _ρ_<sup>2</sup> ) = 1 (State lies on the surface of the Bloch sphere). 

- **Mixed State:** _|_ **a** _| <_ 1 = _⇒_ Tr( _ρ_<sup>2</sup> ) _<_ 1 (State lies strictly inside the Bloch sphere). 

- • **Completely Unpolarized / Maximally Mixed State: a** = 0 = _⇒ ρ_ =<sup><u>1</u></sup> 2<sup>_I_=</sup> 0 

- (1/20 1/2). 

Notes 

6 

## **5. Unitary State Rotations & Time Evolution** 

Any physical rotation of a spin state or time evolution under a magnetic field **B** is generated by exponentiating the Pauli matrices: 



<!-- Start of picture text -->
U ( θ,  ˆ n ) = exp −i 2 θ σ  ·  ˆ n = cos 2 I − i  sin 2 ( σ  ·  ˆ n )<br>( ) ( θ ) ( θ )<br><!-- End of picture text -->

This operator rotates the state vector (and the corresponding Bloch vector) by an angle _θ_ around the spatial unit vector _n_ ˆ. 

## **Master Summary Table: Pauli Matrices vs. Quantum States** 

|Property / Feature|Pauli Matrix _σx_|Pauli Matrix _σy_|Pauli Matrix _σz_|
|---|---|---|---|
|**Matrix Form**<br>**Eigenstates**<br>**(**+1_, −_1**)**|~~(~~<br>0<br>1<br>1<br>0<br>~~)~~<br>_|_0_⟩±|_1_⟩_<br>_~~√~~_<br>2|~~(~~<br>0<br>_−i_<br>_i_<br>0<br>~~)~~<br>_|_0_⟩±i|_1_⟩_<br>_~~√~~_<br>2|~~(~~<br>1<br>0<br>0<br>_−_1<br>~~)~~<br>_|_0_⟩, |_1_⟩_|
|**Expectation Value**<br>**Formula**|2Re(_c_<sup>_∗_</sup><br>1<sup>_c_2)</sup>|2Im(_c_<sup>_∗_</sup><br>1<sup>_c_2)</sup>|_|c_1_|_<sup>2</sup> _−|c_2_|_<sup>2</sup>|
|**Bloch Sphere**<br>**Coordinate**|_ax_ =sin_θ_cos_ϕ_|_ay_ =sin_θ_sin_ϕ_|_az_ =cos_θ_|
|**Density Matrix**<br>**Component**|_ρ_12+_ρ_21 = 2Re(_ρ_12)|_i_(_ρ_12_−ρ_21) =<br>_−_2Im(_ρ_12)|_ρ_11_−ρ_22|
|**Physical Effect as**|Bit-Flip Operator|Bit & Phase-Flip|Phase-Flip Operator|
|**Gate**|(_|_0_⟩↔|_1_⟩_)|Operator|(_|_1_⟩→−|_1_⟩_)|



