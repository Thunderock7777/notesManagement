<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: math-linear-vector-spaces-matrix-algebra.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

GATE PHYSICS 

LINEAR ALGEBRA & VECTOR SPACES 

# **GATE PHYSICS STUDY NOTES Linear Vector Spaces, Matrix Algebra & Diagonalization** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**<br>**Linear Vector Spaces, Basis, Orthogonality & Completeness**<br>**2**|
|---|
|**2**<br>**Matrix Algebra, Similarity Transformations & Diagonalization**<br>**5**|



1 

GATE PHYSICS 

LINEAR ALGEBRA & VECTOR SPACES 

## **1 Linear Vector Spaces, Basis, Orthogonality & Completeness** 

### **1. Core Theory** 

* **Linear Vector Space (** _V_ **):** A mathematical structure consisting of a set of elements (called vectors, _|x⟩_ ) defined over a scalar field _F_ (typically the complex numbers C or real numbers R). It is closed under two algebraic operations: vector addition and scalar multiplication, which satisfy ten fundamental axioms (including commutativity, associativity, the existence of a unique zero vector _|_ 0 _⟩_ , additive inverses, and scalar distributivity). * **Physical Significance:** In quantum mechanics, a physical state is represented as a state vector (or ket, _|ψ⟩_ ) residing in an infinitedimensional complex vector space with an inner product, known as a **Hilbert Space**. The linearity of the vector space is the mathematical foundation of the **Superposition Principle**, which allows quantum states to interfere constructively and destructively. 

### **2. Mathematical Framework & Theorems** 

* **Linear Independence:** A set of vectors _{|v_ 1 _⟩, |v_ 2 _⟩, . . . , |vn⟩}_ is linearly independent if and only if the vector equation: 



<!-- Start of picture text -->
n<br>� ci|vi⟩ =  | 0 ⟩ (1)<br>i =1<br><!-- End of picture text -->

has only the trivial solution: _c_ 1 = _c_ 2 = _· · ·_ = _cn_ = 0. If a non-trivial solution exists, the vectors are linearly dependent. * **Basis:** A set of linearly independent vectors _{|e_ 1 _⟩, |e_ 2 _⟩, . . . , |en⟩}_ that spans the entire vector space _V_ . Any arbitrary vector _|x⟩∈ V_ can be uniquely expressed as a linear combination: 



<!-- Start of picture text -->
n<br>|x⟩ = � xi|ei⟩ (2)<br>i =1<br><!-- End of picture text -->

where the scalars _xi_ are the expansion coefficients (or components) of the vector in that basis. * **Inner Product (Dirac Notation):** A mapping _V × V →_ C, denoted as _⟨x|y⟩_ , satisfying: 

   -  **Conjugate Symmetry:** _⟨x|y⟩_ = _⟨y|x⟩_<sup>_∗_</sup> 

   -  **Linearity in the Second Argument:** _⟨x|c_ 1 _y_ 1 + _c_ 2 _y_ 2 _⟩_ = _c_ 1 _⟨x|y_ 1 _⟩_ + _c_ 2 _⟨x|y_ 2 _⟩_ 

   -  **Positive Definiteness:** _⟨x|x⟩≥_ 0, and _⟨x|x⟩_ = 0 _⇐⇒|x⟩_ = _|_ 0 _⟩_ . 

- **Orthogonality:** Two vectors _|x⟩_ and _|y⟩_ are orthogonal if and only if their inner product vanishes: 



<!-- Start of picture text -->
⟨x|y⟩ = 0 (3)<br><!-- End of picture text -->

An **orthonormal basis** satisfies _⟨ei|ej⟩_ = _δij_ , where _δij_ is the Kronecker delta. * **Completeness (The Closure Relation):** A set of orthonormal basis vectors _{|ei⟩}_ is complete if and only if it satisfies the closure relation: 



<!-- Start of picture text -->
n<br>� |ei⟩⟨ei|  =  ˆ I (4)<br>i =1<br><!-- End of picture text -->

where<sup>ˆ</sup> I is the identity operator. This relation mathematically guarantees that any vector _|x⟩_ can be projected onto the basis: _|x⟩_ =<sup>ˆ</sup> I _|x⟩_ =<sup>�</sup> _i_<sup>_|ei⟩⟨ei|x⟩_.</sup> 

2 

GATE PHYSICS 

LINEAR ALGEBRA & VECTOR SPACES 

### **3. Analytical Milestones** 

Let us outline the standard **Gram-Schmidt Orthonormalization Process** used to construct an orthonormal basis _{|u_ 1 _⟩, |u_ 2 _⟩, . . . }_ from an arbitrary linearly independent set of vectors _{|v_ 1 _⟩, |v_ 2 _⟩, . . . }_ : 

1. **Establish the First Orthonormal Vector:** Set the first basis vector as the normalized version of _|v_ 1 _⟩_ : 



<!-- Start of picture text -->
|v 1 ⟩<br>|u 1 ⟩ = (5)<br>� ⟨v 1 |v 1 ⟩<br><!-- End of picture text -->

2. **Subtract Projections and Normalize the Second Vector:** Subtract the projection of _|v_ 2 _⟩_ along the _|u_ 1 _⟩_ direction to create an orthogonal vector _|w_ 2 _⟩_ : 



<!-- Start of picture text -->
|w 2 ⟩ =  |v 2 ⟩−|u 1 ⟩⟨u 1 |v 2 ⟩ (6)<br><!-- End of picture text -->

Then, normalize _|w_ 2 _⟩_ to obtain the second orthonormal basis vector _|u_ 2 _⟩_ : 



<!-- Start of picture text -->
|w 2 ⟩<br>|u 2 ⟩ = (7)<br>� ⟨w 2 |w 2 ⟩<br><!-- End of picture text -->

3. **Generalize for the** _k_ **-th Vector:** For any subsequent vector _|vk⟩_ , subtract its projections along all previously determined orthonormal vectors _{|u_ 1 _⟩, . . . , |uk−_ 1 _⟩}_ : 



<!-- Start of picture text -->
k− 1<br>|wk⟩ =  |vk⟩− � |ui⟩⟨ui|vk⟩ (8)<br>i =1<br><!-- End of picture text -->

The _k_ -th orthonormal basis vector is then: 



<!-- Start of picture text -->
|wk⟩<br>|uk⟩ = (9)<br>� ⟨wk|wk⟩<br><!-- End of picture text -->

### **4. Problem-Solving Algorithm** 

#### **Verifying Linear Independence using the Wronskian / Gram Determinant** 

To test if a set of functions or vectors _{f_ 1( _x_ ) _, f_ 2( _x_ ) _, . . . , fn_ ( _x_ ) _}_ is linearly independent over an interval: 

1. **Set up the Wronskian Matrix:** Construct the matrix of derivatives: 



<!-- Start of picture text -->
 ff 11 ′ ( ( x x ) ) ff 22 ′ ( ( x x ) ) . . .. . . ffnn ′ ( ( x x ) ) <br>W ( x ) =   (10)<br> ... . . . . . . ... <br> f 1 ( n− 1) ( x ) f 2 ( n− 1) ( x ) . . . fn ( n− 1) ( x )<br><!-- End of picture text -->

2. **Calculate the Determinant:** Evaluate det( _W_ ( _x_ )). 

3. **Apply the Independence Rule:** 

   -  If det( _W_ ( _x_ )) _̸_ = 0 for at least one point in the interval, the functions are **linearly independent**. 

   -  If det( _W_ ( _x_ )) _≡_ 0 everywhere on the interval, and the functions are solutions to a homogeneous linear ODE, they are **linearly dependent**. 

3 

GATE PHYSICS 

LINEAR ALGEBRA & VECTOR SPACES 

### **5. Crucial Pitfalls** 

#### **Complex Inner Product Conjugation Errors** 

-  **Conjugating the Wrong Element:** In a complex vector space, the inner product is sesquilinear. Flipping the arguments requires complex conjugation: _⟨x|y⟩_ = _⟨y|x⟩_<sup>_∗_</sup> . A common error in GATE calculations is treating _⟨x|cy⟩_ as _c_<sup>_∗_</sup> _⟨x|y⟩_ (correct for the first element, but incorrect for the second). Remember: 



<!-- Start of picture text -->
⟨cx|y⟩ =  c ∗ ⟨x|y⟩, ⟨x|cy⟩ =  c⟨x|y⟩ (11)<br><!-- End of picture text -->

-  **Assuming Completeness without Orthogonalization:** Assuming a set of vectors is complete or represents a valid projection basis without first ensuring they are orthogonal. The closure relation<sup>�</sup> _|ei⟩⟨ei|_ =<sup>ˆ</sup> I is strictly valid **only** for orthonormal sets. 

### **6. Standard Applications in Physics** 

-  **Quantum Mechanics State Representation:** In quantum mechanics, a physical state _|ψ⟩_ is expanded in the complete, orthonormal basis of eigenstates of an observable operator _A_ ˆ (where _A_ ˆ _|ai⟩_ = _ai|ai⟩_ ): 



<!-- Start of picture text -->
|ψ⟩ = � ci|ai⟩ with ci =  ⟨ai|ψ⟩ (12)<br>i<br><!-- End of picture text -->

The completeness relation<sup>�</sup> _|ai⟩⟨ai|_ =<sup>ˆ</sup> I guarantees that the sum of probabilities is conserved: � _|ci|_ 2 = 1. 

-  **Continuous Basis (Fourier Analysis):** In infinite-dimensional Hilbert spaces, the completeness of the continuous momentum basis _{|p⟩}_ yields the Fourier transform representation. The closure relation is expressed as: 



<!-- Start of picture text -->
|p⟩⟨p|dp  =  ˆ I = ⇒ ψ ( x ) =  ⟨x|ψ⟩ = ⟨x|p⟩⟨p|ψ⟩dp (13)<br>� −∞∞ �<br><!-- End of picture text -->

4 

GATE PHYSICS 

LINEAR ALGEBRA & VECTOR SPACES 

## **2 Matrix Algebra, Similarity Transformations & Diagonalization** 

### **1. Core Theory** 

* **Matrix Representation:** A linear operator _A_<sup>ˆ</sup> acting on an _n_ -dimensional vector space _V_ can be represented as an _n × n_ matrix _A_ relative to a chosen basis _{|ei⟩}_ . The matrix elements are defined as _Aij_ = _⟨ei|A_<sup>ˆ</sup> _|ej⟩_ . * **Similarity Transformation:** Represents a change of basis. If a linear operator has matrix representation _A_ in basis _{|ei⟩}_ and representation _B_ in basis _{|e_<sup>_′_</sup> _i_<sup>_⟩}_, the</sup> two matrices are related by: 



<!-- Start of picture text -->
B =  P − 1 AP (14)<br><!-- End of picture text -->

where _P_ is the non-singular transition matrix. Similarity transformations are equivalence relations that preserve the intrinsic properties of the linear operator, such as its determinant, trace, and eigenvalues. * **Diagonalization:** The process of finding a similarity transformation matrix _S_ such that _D_ = _S_<sup>_−_1</sup> _AS_ is a diagonal matrix. Physically, this corresponds to rotating the coordinate system to align with the principal axes of the operator, simplifying the equations of motion or system state descriptions. 

### **2. Mathematical Framework & Theorems** 

- **Special Matrices:** 

   -  **Hermitian Matrix:** _A_<sup>_†_</sup> = ( _A_<sup>_∗_</sup> )<sup>_T_</sup> = _A_ . (Represent physical observables in quantum mechanics; eigenvalues are strictly real). 

   -  **Unitary Matrix:** _U_<sup>_†_</sup> = _U_<sup>_−_1</sup> = _⇒ U_<sup>_†_</sup> _U_ =<sup>ˆ</sup> I. (Represent time evolution or coordinate rotations; preserve inner products). 

   -  **Orthogonal Matrix:** _O_<sup>_T_</sup> = _O_<sup>_−_1</sup> = _⇒ O_<sup>_T_</sup> _O_ =<sup>ˆ</sup> I. (Real analog of unitary matrices). 

- **Properties Invariant Under Similarity Transformations (** _B_ = _P_<sup>_−_1</sup> _AP_ **):** 

   -  **Determinant Invariance:** det( _B_ ) = det( _P_<sup>_−_1</sup> _AP_ ) = det( _P_<sup>_−_1</sup> ) det( _A_ ) det( _P_ ) = det( _A_ ). 

   -  **Trace Invariance:** Tr( _B_ ) = Tr( _P_<sup>_−_1</sup> _AP_ ) = Tr( _APP_<sup>_−_1</sup> ) = Tr( _A_ ). 

   -  **Characteristic Equation Invariance:** det( _B − λ_ I) = det( _A − λ_ I). Thus, eigenvalues are strictly identical. 

* **The Spectral Theorem (Unitary Diagonalization):** An _n × n_ matrix _A_ is unitarily diagonalizable (i.e., there exists a unitary matrix _U_ such that _U_<sup>_†_</sup> _AU_ = _D_ is diagonal) if and only if _A_ is a **Normal Matrix**: 



<!-- Start of picture text -->
[ A, A † ] =  AA † − A † A  = 0 (15)<br><!-- End of picture text -->

Hermitian, anti-Hermitian, unitary, orthogonal, and symmetric matrices are all normal and thus guaranteed to be unitarily diagonalizable. 

5 

GATE PHYSICS 

LINEAR ALGEBRA & VECTOR SPACES 

### **3. Analytical Milestones** 

Let us prove two critical theorems representing milestones in matrix mechanics: 

1. **Theorem: Eigenvalues of a Hermitian Matrix are Strictly Real.** Let _A_ be a Hermitian matrix ( _A_<sup>_†_</sup> = _A_ ), and let _|ψ⟩_ be an eigenvector with eigenvalue _λ_ : _A|ψ⟩_ = _λ|ψ⟩_ (16) 

Take the inner product with _⟨ψ|_ : _⟨ψ|A|ψ⟩_ = _λ⟨ψ|ψ⟩_ (17) Now take the Hermitian adjoint of the eigenvalue equation: _⟨ψ|A_<sup>_†_</sup> = _λ_<sup>_∗_</sup> _⟨ψ|_ = _⇒⟨ψ|A_ = _λ_<sup>_∗_</sup> _⟨ψ|_ (18) Take the inner product with _|ψ⟩_ from the right: _⟨ψ|A|ψ⟩_ = _λ_<sup>_∗_</sup> _⟨ψ|ψ⟩_ (19) Subtracting the two results yields: ( _λ − λ_<sup>_∗_</sup> ) _⟨ψ|ψ⟩_ = 0 (20) Since _|ψ⟩_ is a non-zero physical state, _⟨ψ|ψ⟩ >_ 0, forcing: _λ_ = _λ_<sup>_∗_</sup> (proving _λ_ is strictly real) (21) 2. **Theorem: Eigenvectors of a Hermitian Matrix Corresponding to Distinct Eigenvalues are Orthogonal.** Let _A|v_ 1 _⟩_ = _λ_ 1 _|v_ 1 _⟩_ and _A|v_ 2 _⟩_ = _λ_ 2 _|v_ 2 _⟩_ , where _λ_ 1 _̸_ = _λ_ 2. Compute the quantity: 

_⟨v_ 2 _|A|v_ 1 _⟩_ = _λ_ 1 _⟨v_ 2 _|v_ 1 _⟩_ (22) 

Also, because _A_<sup>_†_</sup> = _A_ and the eigenvalues are real ( _λ_<sup>_∗_</sup> 2<sup>=</sup><sup>_λ_2):</sup> _⟨v_ 2 _|A_ = _⟨Av_ 2 _|_ = _λ_ 2 _⟨v_ 2 _|_ = _⇒⟨v_ 2 _|A|v_ 1 _⟩_ = _λ_ 2 _⟨v_ 2 _|v_ 1 _⟩_ (23) Equating the two expressions yields: ( _λ_ 1 _− λ_ 2) _⟨v_ 2 _|v_ 1 _⟩_ = 0 (24) Since _λ_ 1 _̸_ = _λ_ 2, we must have: _⟨v_ 2 _|v_ 1 _⟩_ = 0 (proving orthogonality) (25) 

6 

GATE PHYSICS 

LINEAR ALGEBRA & VECTOR SPACES 

### **4. Problem-Solving Algorithm** 

**Methodological Guide to Diagonalize an** _n × n_ **Matrix** Given an _n × n_ matrix _A_ : 1. **Find the Eigenvalues:** Set up and solve the characteristic equation: det( _A − λ_ I) = 0 = _⇒ λ_<sup>_n_</sup> _−_ Tr( _A_ ) _λ_<sup>_n−_1</sup> + _· · ·_ + ( _−_ 1)<sup>_n_</sup> det( _A_ ) = 0 (26) Let the roots be _{λ_ 1 _, λ_ 2 _, . . . , λn}_ . 2. **Find the Eigenvectors:** For each eigenvalue _λi_ , solve the homogeneous linear system: ( _A − λi_ I) **x** _i_ = **0** (27) Express the solution as a normalized column vector **x** _i_ . 3. **Construct the Modal Matrix (** _S_ **):** Group the eigenvectors as columns to form _S_ : _S_ = � **x** 1 **x** 2 _. . ._ **x** _n_ � (28) If the matrix _A_ is normal, and you normalize the eigenvectors, _S_ becomes a unitary matrix _U_ ( _U_<sup>_−_1</sup> = _U_<sup>_†_</sup> ). 4. **Compute the Diagonal Representation (** _D_ **):** Calculate _D_ = _S_<sup>_−_1</sup> _AS_ . The resulting diagonal matrix will have the eigenvalues along its diagonal:  _λ_ 01 _λ_ 02 _. . .. . ._ 00  _D_ =   (29)  ... _. . ._ ... ...   0 0 _. . . λn_  

7 

GATE PHYSICS 

LINEAR ALGEBRA & VECTOR SPACES 

### **5. Crucial Pitfalls** 

#### **The Defective Matrix Trap (Non-Diagonalizability)** 

-  **Confusing Algebraic and Geometric Multiplicity:** 

   - **Algebraic Multiplicity (** _mi_ **):** The number of times an eigenvalue _λi_ appears as a root of the characteristic polynomial. 

   - **Geometric Multiplicity (** _gi_ **):** The number of linearly independent eigenvectors corresponding to _λi_ (equal to the nullity of _A − λi_ I). 

An _n×n_ matrix is diagonalizable **if and only if** _gi_ = _mi_ for every eigenvalue. If _gi < mi_ for even one eigenvalue, the matrix is **defective** and **cannot be diagonalized** (it can only be reduced to a Jordan Canonical Form). 



<!-- Start of picture text -->
1<br> GATE Exam Trap: Given a triangular matrix like  A  = . The eigenvalues are<br>0 2<br>�2 �<br>1<br>=<br>λ  = 2 ,  2 ( m 1 = 2). Solving ( A − 2I) x  = 0 = ⇒ = ⇒ y = 0. This<br>�00 0�� xy � �00�<br>yields only one independent eigenvector: ( g 1 = 1). Since g 1 < m 1, this matrix is<br>0<br>�1�<br>strictly non-diagonalizable.<br><!-- End of picture text -->

### **6. Standard Applications in Physics** 

-  **Coupled Harmonic Oscillators (Normal Modes):** The classical equations of motion for a system of coupled masses can be written as: 

**Mx** ¨ + **Kx** = **0** (30) 

where **M** is the mass matrix and **K** is the stiffness matrix. Multiplying by **M**<sup>_−_1</sup> yields **x** ¨ + **Ax** = **0** . Diagonalizing **A** = **M**<sup>_−_1</sup> **K** yields the **normal frequencies** (eigenvalues _ωi_<sup>2)</sup> and the **normal modes** (eigenvectors), decoupling the motion into independent harmonic oscillators. 

-  **Principal Axes of Inertia (Rigid Body Dynamics):** The angular momentum **L** of a rotating rigid body is related to its angular velocity **_ω_** by the symmetric Inertia Tensor matrix **I** : 



<!-- Start of picture text -->
L  =  I ω (31)<br><!-- End of picture text -->

Because **I** is a real symmetric matrix, it can always be diagonalized. The eigenvalues represent the **principal moments of inertia** ( _I_ 1 _, I_ 2 _, I_ 3), and the eigenvectors define the **principal axes of rotation**, about which the rigid body can rotate stably without precession. 

8 

GATE PHYSICS 

LINEAR ALGEBRA & VECTOR SPACES 

## **References** 

1. Mathematical Methods for Physicists. Arfken, Weber, & Harris. 7th Edition. 

2. Quantum Mechanics: Concepts and Applications. Nouredine Zettili. 2nd Edition. 

3. Introduction to Electrodynamics. David J. Griffiths. 3rd Edition. 

9 

GATE PHYSICS 

LINEAR DIFFERENTIAL EQUATIONS 

# **GATE PHYSICS STUDY NOTES Linear Ordinary Differential Equations** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

|**Contents**|
|---|



|**1**<br>**First-Order Linear Ordinary Differential Equations**|**2**|
|---|---|
|**2**<br>**Second-Order Linear Ordinary Differential Equations**|**6**|



1 

GATE PHYSICS 

LINEAR DIFFERENTIAL EQUATIONS 

## **1 First-Order Linear Ordinary Differential Equations** 

### **1. Core Theory** 

A **first-order linear ordinary differential equation (ODE)** is an equation that can be written in the form where the dependent variable _y_ ( _x_ ) and its first derivative _y_<sup>_′_</sup> ( _x_ ) appear linearly (i.e., to the first power, and not multiplied together or embedded inside non-linear functions like sin _y_ or _e_<sup>_y_</sup> ). 

-  **Mathematical Definition:** A first-order ODE is linear if it is expressible in the standard form: 



<!-- Start of picture text -->
dy<br>dx +  P ( x ) y =  Q ( x ) (1)<br><!-- End of picture text -->

where _P_ ( _x_ ) and _Q_ ( _x_ ) are continuous real- or complex-valued functions on an interval _I ⊆_ R. If _Q_ ( _x_ ) _≡_ 0 on _I_ , the ODE is **homogeneous** ; if _Q_ ( _x_ ) _̸_ = 0, it is **non-homogeneous** . 

-  **Physical Significance:** Mathematically, first-order linear ODEs model dynamic systems where the rate of change of a physical quantity is directly proportional to its current state, plus an external driving force or source term. This is the mathematical foundation of relaxation, dissipation, and growth processes throughout physics, including radioactive decay, electric circuit transients (RC and RL circuits), fluid drag at low speeds (terminal velocity), and thermal equalization (Newton’s law of cooling). 

### **2. Mathematical Framework & Theorems** 

* **Standard Form:** 



<!-- Start of picture text -->
y ′ ( x ) +  P ( x ) y ( x ) =  Q ( x ) (2)<br><!-- End of picture text -->

where the coefficient of the leading derivative _y_<sup>_′_</sup> must be exactly 1. * **Integrating Factor (IF):** To solve the non-homogeneous equation, we define the Integrating Factor: 



<!-- Start of picture text -->
I ( x ) = exp P ( x )  dx (3)<br>�� �<br><!-- End of picture text -->

which is guaranteed to be non-zero and differentiable on any interval where _P_ ( _x_ ) is continuous. * **Existence and Uniqueness Theorem (Picard–Lindel¨of):** Let _P_ ( _x_ ) and _Q_ ( _x_ ) be continuous functions on an open interval _I_ containing _x_ 0. For any real or complex number _y_ 0, there exists a **unique** solution _y_ ( _x_ ) to the initial value problem (IVP): 



<!-- Start of picture text -->
y ′ ( x ) +  P ( x ) y ( x ) =  Q ( x ) , y ( x 0) =  y 0 (4)<br><!-- End of picture text -->

that is defined and differentiable for all _x ∈ I_ . Continuity of _P_ ( _x_ ) and _Q_ ( _x_ ) is a strict required condition; singularities in these functions bound the domain of existence of the unique solution. 

### **3. Analytical Milestones** 

Let us derive the general solution of the first-order non-homogeneous linear ODE using the Integrating Factor method: 

2 

GATE PHYSICS 

LINEAR DIFFERENTIAL EQUATIONS 

1. **Define and Differentiate the Product:** Assume we seek a function _I_ ( _x_ ) such that multiplying the standard form by _I_ ( _x_ ) allows us to collapse the left-hand side into a single derivative of a product: 

_I_ ( _x_ ) _y_<sup>_′_</sup> ( _x_ ) + _I_ ( _x_ ) _P_ ( _x_ ) _y_ ( _x_ ) = _I_ ( _x_ ) _Q_ ( _x_ ) (5) 



<!-- Start of picture text -->
We want the left-hand side to be equal to dxd [ I ( x ) y ( x )]. By the product rule:<br>d<br>dx [ I ( x ) y ( x )] =  I ( x ) y′ ( x ) +  I ′ ( x ) y ( x ) (6)<br><!-- End of picture text -->

2. **Isolate the Integrating Factor Differential Equation:** Equating the two expressions for the left-hand side: 



<!-- Start of picture text -->
I ( x ) y ′ ( x ) +  I ′ ( x ) y ( x ) =  I ( x ) y ′ ( x ) +  I ( x ) P ( x ) y ( x ) = ⇒ I ′ ( x ) =  I ( x ) P ( x ) (7)<br><!-- End of picture text -->

This is a separable first-order differential equation for _I_ ( _x_ ): 



<!-- Start of picture text -->
dI<br>I =  P ( x )  dx = ⇒ ln  |I ( x ) |  = � P ( x )  dx = ⇒ I ( x ) =  e � P ( x )  dx (8)<br><!-- End of picture text -->

where we omit the constant of integration because any scaling of _I_ ( _x_ ) cancels out in the final solution. 

3. **Integrate the Product Equation:** Multiply the original standard form by _I_ ( _x_ ) and write the left-hand side as a product derivative: 

_d dx_<sup>[</sup><sup>_I_(</sup><sup>_x_)</sup><sup>_y_(</sup><sup>_x_)] =</sup><sup>_I_(</sup><sup>_x_)</sup><sup>_Q_(</sup><sup>_x_)</sup> (9) 

Integrating both sides with respect to _x_ yields: 

_I_ ( _x_ ) _y_ ( _x_ ) = _I_ ( _x_ ) _Q_ ( _x_ ) _dx_ + _C_ (10) � 

where _C_ is an arbitrary constant of integration. 

4. **Extract the General Solution:** Isolating _y_ ( _x_ ) gives the final general solution: 



<!-- Start of picture text -->
1<br>y ( x ) = I ( x ) Q ( x )  dx  +  C =  e − � P ( x )  dx e � P ( x )  dxQ ( x )  dx  +  C (11)<br>I ( x ) �� � �� �<br><!-- End of picture text -->

3 

GATE PHYSICS 

LINEAR DIFFERENTIAL EQUATIONS 

### **4. Problem-Solving Algorithm** 

#### **Solving First-Order Linear ODEs** 

1. **Convert to Standard Form:** Rearrange the given ODE so that the coefficient of _dx_<sup>_dy_</sup> is exactly 1. Identify the coefficient function _P_ ( _x_ ) and the source term _Q_ ( _x_ ). 

2. **Calculate the Integrating Factor (IF):** Compute the integral � _P_ ( _x_ ) _dx_ , and then evaluate: 



<!-- Start of picture text -->
I ( x ) =  e � P ( x )  dx (12)<br><!-- End of picture text -->

3. **Apply the General Solution Formula:** Set up the integration: 



<!-- Start of picture text -->
1<br>y ( x ) = I ( x ) Q ( x )  dx  +  C (13)<br>I ( x ) �� �<br><!-- End of picture text -->

Evaluate the integral of the product _I_ ( _x_ ) _Q_ ( _x_ ). Do not forget to include the constant _C_ inside the bracket! 

4. **Incorporate Initial Conditions (IVP):** If an initial condition _y_ ( _x_ 0) = _y_ 0 is provided, substitute _x_ = _x_ 0 and _y_ = _y_ 0 into the general solution to solve for the unique value of _C_ . Specify the domain of validity of the solution. 

### **5. Crucial Pitfalls** 

#### **First-Order Linear ODE Traps** 

-  **Failure to Standardize:** Calculating the integrating factor directly from an equation that is not in standard form. For example, in the equation _xy_<sup>_′_</sup> +2 _y_ = cos _x_ , attempting to set _P_ ( _x_ ) = 2 instead of the correct _P_ ( _x_ ) = 2 _/x_ . You must always divide by the leading coefficient _x_ first! 

-  **Integrating Factor Sign Errors:** Confusing the sign of the exponent when multiplying the solution. The integrating factor is _I_ ( _x_ ) = _e_ � _P_ ( _x_ ) _dx_ , but when isolating _y_ ( _x_ ), we multiply the entire right-hand side by _I_ ( _x_ )<sup>_−_1</sup> = _e_<sup>_−_</sup> � _P_ ( _x_ ) _dx_ . A common error is flipping these signs. 

-  **Constant of Integration Placement:** Neglecting the constant of integration during the final integration step or multiplying it outside of the 1 _/I_ ( _x_ ) term. The constant _C_ must be added **before** multiplying by 1 _/I_ ( _x_ ), so that the final solution contains the term _C · e_<sup>_−_</sup> � _P_ ( _x_ ) _dx_ . 

### **6. Standard Applications in Physics** 

-  **Transient RL Circuit (Electrodynamics):** A series circuit containing a constant resistance _R_ , self-inductance _L_ , and connected to a time-dependent voltage source _V_ ( _t_ ). The current _I_ ( _t_ ) satisfies: 



<!-- Start of picture text -->
L dI (14)<br>dt +  RI =  V  ( t ) = ⇒ dI dt + R L I = V L ( t )<br><!-- End of picture text -->

4 

GATE PHYSICS 

LINEAR DIFFERENTIAL EQUATIONS 

This is a first-order linear ODE with _P_ ( _t_ ) = _R/L_ and _Q_ ( _t_ ) = _V_ ( _t_ ) _/L_ . 

-  **Radioactive Decay Chains (Nuclear Physics):** A radioactive parent nucleus _N_ 1( _t_ ) decays into a daughter nucleus _N_ 2( _t_ ) with decay constants _λ_ 1 and _λ_ 2 respectively. The rate of change of the daughter population is: 



<!-- Start of picture text -->
dN 2 =  λ 1 N 1( t )  − λ 2 N 2 = ⇒ dN 2 (15)<br>dt dt +  λ 2 N 2 =  λ 1 N 0 e−λ 1 t<br><!-- End of picture text -->

where we have substituted the parent population _N_ 1( _t_ ) = _N_ 0 _e_<sup>_−λ_1</sup><sup>_t_</sup> . This is a first-order linear ODE for _N_ 2( _t_ ). 

5 

GATE PHYSICS 

LINEAR DIFFERENTIAL EQUATIONS 

## **2 Second-Order Linear Ordinary Differential Equations** 

### **1. Core Theory** 

A **second-order linear ordinary differential equation (ODE)** is an equation where the dependent variable _y_ ( _x_ ) and its first two derivatives _y_<sup>_′_</sup> ( _x_ ) _, y_<sup>_′′_</sup> ( _x_ ) appear linearly. 

-  **Mathematical Definition:** A second-order ODE is linear if it is expressible in the standard form: 



<!-- Start of picture text -->
d 2 y<br>(16)<br>dx 2 +  P ( x ) dx dy +  Q ( x ) y =  R ( x )<br><!-- End of picture text -->

where _P_ ( _x_ ), _Q_ ( _x_ ), and _R_ ( _x_ ) are continuous functions on an interval _I ⊆_ R. If _R_ ( _x_ ) _≡_ 0, it is **homogeneous** ; if _R_ ( _x_ ) _̸_ = 0, it is **non-homogeneous** . 

-  **Physical Significance:** Physically, second-order linear ODEs govern dynamic systems where acceleration (or secondary rate of change) depends on velocity (first rate of change, representing damping or friction), position (current state, representing restorative forces like Hooke’s law), and external forces. It is the mathematical cornerstone of wave mechanics, acoustics, electromagnetism, and classical mechanics, modeling simple, damped, and forced harmonic oscillators. 

### **2. Mathematical Framework & Theorems** 

* **Linear Independence and the Wronskian:** Two solutions _y_ 1( _x_ ) and _y_ 2( _x_ ) of the homogeneous equation on an interval _I_ are linearly independent if and only if their **Wronskian determinant** is non-zero for all _x ∈ I_ : 



<!-- Start of picture text -->
y 2( x )<br>W ( y 1 , y 2)( x ) = det =  y 1( x ) y 2 ′ ( x )  − y 2( x ) y 1 ′ ( x ) ̸  = 0 (17)<br>� yy 11 ′ ( ( x x ) ) y 2 ′ ( x ) �<br><!-- End of picture text -->

* **Abel’s Identity:** The Wronskian of any two solutions to the homogeneous ODE satisfies: 



<!-- Start of picture text -->
−<br>W ( x ) =  W ( x 0) exp P ( t )  dt (18)<br>� � x 0 x �<br><!-- End of picture text -->

This implies that _W_ ( _x_ ) is either identically zero everywhere on _I_ (meaning the solutions are linearly dependent) or never zero anywhere on _I_ (meaning the solutions are linearly independent). * **Principle of Superposition:** If _y_ 1( _x_ ) and _y_ 2( _x_ ) are linearly independent solutions to the homogeneous second-order linear ODE, then the general homogeneous solution (Complementary Function, _yc_ ) is: 



<!-- Start of picture text -->
yc ( x ) =  C 1 y 1( x ) +  C 2 y 2( x ) (19)<br><!-- End of picture text -->

* **General Solution of the Non-Homogeneous Equation:** The complete general solution _y_ ( _x_ ) of the non-homogeneous equation is the sum of the complementary function _yc_ ( _x_ ) and any particular solution (Particular Integral, _yp_ ( _x_ )): 



<!-- Start of picture text -->
y ( x ) =  yc ( x ) +  yp ( x ) =  C 1 y 1( x ) +  C 2 y 2( x ) +  yp ( x ) (20)<br><!-- End of picture text -->

6 

GATE PHYSICS 

LINEAR DIFFERENTIAL EQUATIONS 

### **3. Analytical Milestones** 

Let us analyze the critical steps for the two primary methods used to find _yp_ ( _x_ ): * **Method 1: Variation of Parameters (Universal Method):** This method derives a particular solution using the Wronskian of the homogeneous solutions _y_ 1( _x_ ) and _y_ 2( _x_ ): 

1. **Formulate Variable Parameters:** Assume a particular solution of the form: 



<!-- Start of picture text -->
yp ( x ) =  u 1( x ) y 1( x ) +  u 2( x ) y 2( x ) (21)<br>Differentiate ypp ( x ):<br>yp ′ ( x ) =  u 1 y 1 ′ +  u 2 y 2 ′ +  u 1 ′ y 1 +  u 2 ′ y 2 (22)<br><!-- End of picture text -->

Differentiate _ypp_ ( _x_ ): 

To simplify, assert the constraint: 



<!-- Start of picture text -->
u ′ 1 ( x ) y 1( x ) +  u 2 ′ ( x ) y 2( x ) = 0 = ⇒ y p ′ ( x ) =  u 1 y 1 ′ +  u 2 y 2 ′ (23)<br><!-- End of picture text -->



<!-- Start of picture text -->
2. Substitute into the ODE: Differentiate yp ′ ( x ) again:<br>yp ′′ ( x ) =  u 1 y 1 ′′ +  u 2 y 2 ′′ +  u′ 1 y 1 ′ +  u′ 2 y 2 ′ (24)<br><!-- End of picture text -->

Substitute _yp, yp_<sup>_′, y_</sup> _p_<sup>_′′_intothenon-homogeneousstandardform:</sup> _u_ 1[ _y_ 1<sup>_′′_+</sup><sup>_Py_</sup> 1<sup>_′_+</sup><sup>_Qy_1] +</sup><sup>_u_2[</sup><sup>_y_</sup> 2<sup>_′′_+</sup><sup>_Py_</sup> 2<sup>_′_+</sup><sup>_Qy_2] +</sup><sup>_u_</sup> 1<sup>_′y_</sup> 1<sup>_′_+</sup><sup>_u′_</sup> 2<sup>_y_</sup> 2<sup>_′_=</sup><sup>_R_(</sup><sup>_x_)</sup> (25) 

Since _y_ 1 and _y_ 2 are solutions to the homogeneous equation, the bracketed terms are zero, yielding: 



<!-- Start of picture text -->
u ′ 1 ( x ) y 1 ′ ( x ) +  u′ 2 ( x ) y 2 ′ ( x ) =  R ( x ) (26)<br><!-- End of picture text -->

3. **Solve the Linear System for** _u_<sup>_′_</sup> 1<sup>_, u′_</sup> 2<sup>**:**UsingCramersRuleonthesystemoftwoequations:</sup> 



<!-- Start of picture text -->
u ′ 1 ( x ) y 1( x ) +  u′ 2 ( x ) y 2( x ) = 0 , u ′ 1 ( x ) y 1 ′ ( x ) +  u′ 2 ( x ) y 2 ′ ( x ) =  R ( x ) (27)<br><!-- End of picture text -->

gives: 



<!-- Start of picture text -->
y 1( x ) R ( x )<br>u ′ 1 ( x ) =  − y 2( x ) R ( x ) u ′ 2 ( x ) = (28)<br>W ( y 1 , y 2)( x ) , W ( y 1 , y 2)( x )<br><!-- End of picture text -->

4. **Integrate to Find the Particular Integral:** Integrating these terms directly gives the components of _yp_ ( _x_ ): 



<!-- Start of picture text -->
y 2( x ) R ( x ) y 1( x ) R ( x )<br>yp ( x ) =  −y 1( x ) (29)<br>� W ( y 1 , y 2)( x ) dx  +  y 2( x ) � W ( y 1 , y 2)( x ) dx<br><!-- End of picture text -->

* **Method 2: Complementary Function for Constant Coefficients:** Solve _ay_<sup>_′′_</sup> + _by_<sup>_′_</sup> + _cy_ = 0 by assuming a trial solution _y_ = _e_<sup>_mx_</sup> : 



<!-- Start of picture text -->
1. Substitute y, y ′ , y ′′ into the ODE to get the **Characteristic (Auxiliary) Equation**:<br>am 2 +  bm  +  c  = 0 (30)<br><!-- End of picture text -->

7 

GATE PHYSICS 

LINEAR DIFFERENTIAL EQUATIONS 

2. Solve the quadratic equation for roots _m_ 1 _, m_ 2: 



<!-- Start of picture text -->
√ b 2 − 4 ac<br>m 1 , 2 = −b ± (31)<br>2 a<br><!-- End of picture text -->

3. Classify the roots into three cases: 



<!-- Start of picture text -->
 Case I: Real and Distinct (Discriminant b 2 − 4 ac >  0 ):<br>yc ( x ) =  C 1 e m 1 x +  C 2 e m 2 x (32)<br><!-- End of picture text -->

 **Case II: Real and Repeated (** _b_<sup>2</sup> _−_ 4 _ac_ = 0 **,** _m_ 1 = _m_ 2 = _m_ **):** 

_yc_ ( _x_ ) = ( _C_ 1 + _C_ 2 _x_ ) _e_<sup>_mx_</sup> (33) 

 **Case III: Complex Conjugates (** _b_<sup>2</sup> _−_ 4 _ac <_ 0 **,** _m_ = _α ± iβ_ **):** _yc_ ( _x_ ) = _e_<sup>_αx_</sup> [ _C_ 1 cos( _βx_ ) + _C_ 2 sin( _βx_ )] (34) 

### **4. Problem-Solving Algorithm** 

#### **Method of Undetermined Coefficients (for Constant Coefficients)** 

Use this highly efficient method if _R_ ( _x_ ) is a polynomial, exponential, sine, or cosine function: 

1. **Solve the Homogeneous Equation:** Find the complementary function _yc_ ( _x_ ) = _C_ 1 _y_ 1( _x_ ) + _C_ 2 _y_ 2( _x_ ) using the characteristic equation. 

2. **Formulate the Particular Trial Form (** _yp_ **):** Select the trial form based on _R_ ( _x_ ): 

   -  If _R_ ( _x_ ) = _Pn_ ( _x_ ) (polynomial of degree _n_ ), try _yp_ ( _x_ ) = _Anx_<sup>_n_</sup> + _· · ·_ + _A_ 0. 

   -  If _R_ ( _x_ ) = _e_<sup>_kx_</sup> , try _yp_ ( _x_ ) = _Ae_<sup>_kx_</sup> . 

   -  If _R_ ( _x_ ) = cos( _ωx_ ) or sin( _ωx_ ), try _yp_ ( _x_ ) = _A_ cos( _ωx_ ) + _B_ sin( _ωx_ ). 

3. **Apply the Modification Rule (Resonance Check):** Compare the terms of your trial _yp_ ( _x_ ) with the terms in the complementary function _yc_ ( _x_ ). If any term in _yp_ ( _x_ ) is a solution to the homogeneous equation, multiply the entire trial form of that section by _x_ (or _x_<sup>2</sup> if it is a repeated root) to eliminate duplication. 

4. **Solve for Coefficients:** Differentiate your modified trial form, substitute _yp, yp_<sup>_′, y_</sup> _p_<sup>_′′_</sup> into the original non-homogeneous ODE, and equate coefficients of like terms to solve for the undetermined constants ( _A_ , _B_ , etc.). 

5. **Construct the General Solution and Apply Boundaries:** Formulate _y_ ( _x_ ) = _yc_ ( _x_ ) + _yp_ ( _x_ ). Substitute boundary or initial conditions to solve for _C_ 1 and _C_ 2. 

8 

GATE PHYSICS 

LINEAR DIFFERENTIAL EQUATIONS 

### **5. Crucial Pitfalls** 

#### **Second-Order Linear ODE Traps** 

-  **Boundary Condition Timing Trap:** Attempting to apply initial or boundary conditions directly to the complementary function _yc_ ( _x_ ) before finding and adding the particular solution _yp_ ( _x_ ). Boundary conditions are strictly defined for the **total complete solution** _y_ ( _x_ ) = _yc_ ( _x_ ) + _yp_ ( _x_ ), and applying them early will result in incorrect values for _C_ 1 and _C_ 2. 

-  **The Resonance Oversight:** Forgetting to check for duplicate terms between _yp_ ( _x_ ) and _yc_ ( _x_ ). For example, in the equation _y_<sup>_′′_</sup> _− y_ = _e_<sup>_x_</sup> , the homogeneous solution is _yc_ = _C_ 1 _e_<sup>_x_</sup> + _C_ 2 _e_<sup>_−x_</sup> . If you try _yp_ = _Ae_<sup>_x_</sup> , substituting it yields 0 = _e_<sup>_x_</sup> , which is impossible. You must multiply by _x_ , trying _yp_ = _Axe_<sup>_x_</sup> instead! 

-  **The Single-Term Sine/Cosine Fallacy:** If _R_ ( _x_ ) = cos( _ωx_ ), assuming that the trial solution only requires a cosine term. You must include both sine and cosine terms: _yp_ = _A_ cos( _ωx_ ) + _B_ sin( _ωx_ ), because the first derivative _y_<sup>_′_</sup> converts cosines to sines. 

### **6. Standard Applications in Physics** 

-  **The Damped Forced Harmonic Oscillator (Classical Mechanics):** A particle of mass _m_ attached to a spring of stiffness _k_ , experiencing a viscous damping force _−b_ ˙ _x_ and an external periodic driving force _F_ 0 cos( _ωt_ ). Its equation of motion is: 



<!-- Start of picture text -->
m d dt 2 x 2 +  bdx dt +  kx  =  F 0 cos( ωt ) = ⇒ x ¨ + 2 γ  ˙ x  +  ω 0 2 x  = F m 0 cos( ωt ) (35)<br><!-- End of picture text -->

where _γ_ = _b/_ 2 _m_ is the damping coefficient, and _ω_ 0 = ~~�~~ _k/m_ is the natural frequency. 

-  **The 1D Time-Independent Schr¨odinger Equation (Quantum Mechanics):** The wave function _ψ_ ( _x_ ) of a particle of mass _m_ and energy _E_ inside a constant potential well _V_ 0 satisfies: 



<!-- Start of picture text -->
− ℏ2 d 2 ψ<br>ψ = 0 (36)<br>2 m dx 2 +  V 0 ψ =  Eψ = ⇒ d dx 2 ψ 2 + 2 m ( E ℏ  − 2 V 0)<br><!-- End of picture text -->

For _E > V_ 0, this is a homogeneous second-order linear ODE with constant coefficients, yielding sinusoidal solutions. For _E < V_ 0, it yields exponential tunneling solutions. 

9 

GATE PHYSICS 

LINEAR DIFFERENTIAL EQUATIONS 

## **References** 

1. Arfken, George. _Mathematical Methods for Physicists_ . Wiley, 1999. 

2. Kreyszig, Erwin. _Advanced Engineering Mathematics_ . Wiley, 2011. 

3. Griffiths, David J. _Introduction to Quantum Mechanics_ . Prentice Hall, 1995. 

10 

GATE PHYSICS 

COMPLEX ANALYSIS & CONTOUR INTEGRATION 

# **GATE PHYSICS STUDY NOTES Complex Analysis, Cauchy Theorems & Contour Integration** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**|**Functions of a Complex Variable & Cauchy-Riemann Conditions**|**2**|
|---|---|---|
|**2**|**Cauchy’s Integral Theorem & Formula**|**5**|
|**3**|**Laurent Series & Classification of Singularities**|**8**|
|**4**|**The Residue Theorem & Contour Integration**|**11**|



1 

GATE PHYSICS 

COMPLEX ANALYSIS & CONTOUR INTEGRATION 

## **1 Functions of a Complex Variable & Cauchy-Riemann Conditions** 

### **1. Core Theory** 

A function of a complex variable _f_ ( _z_ ) maps a subset of the complex plane C to another subset of C. We express _f_ ( _z_ ) in terms of its real and imaginary parts as _f_ ( _z_ ) = _u_ ( _x, y_ ) + _iv_ ( _x, y_ ), where _z_ = _x_ + _iy_ . 

-  **Analyticity (Holomorphy):** A function _f_ ( _z_ ) is said to be **analytic** (or holomorphic) at a point _z_ 0 if it is single-valued and possesses a unique, path-independent derivative _f_<sup>_′_</sup> ( _z_ 0) in some open neighborhood of _z_ 0. If _f_ ( _z_ ) is analytic everywhere in the entire complex plane, it is called an **entire function** . 

-  **Physical Significance:** Complex analysis is highly crucial in physics due to **Potential Theory** . The real and imaginary parts of an analytic function automatically satisfy the 2D Laplace equation ( _∇_<sup>2</sup> _u_ = 0, _∇_<sup>2</sup> _v_ = 0), making them ideal for representing physical potentials (such as electrostatic potentials, gravitational potentials, and stream functions in fluid dynamics). 

### **2. Mathematical Framework & Theorems** 

* **Definition of the Derivative:** 



<!-- Start of picture text -->
f ( z  + ∆ z )  − f ( z )<br>f ′ ( z )  ≡ lim (1)<br>∆ z→ 0 ∆ z<br><!-- End of picture text -->

For this limit to exist and be unique, it must yield the same complex number regardless of the path along which ∆ _z_ = ∆ _x_ + _i_ ∆ _y →_ 0. * **The Cauchy-Riemann (C-R) Conditions (Cartesian):** If _f_ ( _z_ ) = _u_ ( _x, y_ ) + _iv_ ( _x, y_ ) is differentiable at _z_ , then the first-order partial derivatives of _u_ and _v_ must exist and satisfy: 



<!-- Start of picture text -->
∂u ∂u<br>and (2)<br>∂x = ∂y ∂v ∂y =  − ∂x ∂v<br><!-- End of picture text -->

* **Sufficient Conditions for Analyticity:** For _f_ ( _z_ ) to be analytic in a domain, the C-R conditions are necessary but not sufficient on their own. The **sufficient conditions** require that: 

   1. The partial derivatives _ux, uy, vx, vy_ exist and satisfy the C-R equations. 

   2. These partial derivatives are **continuous** functions of ( _x, y_ ) everywhere within the domain. 

- **Cauchy-Riemann Conditions in Polar Coordinates (** _z_ = _re_<sup>_iθ_</sup> **):** 



<!-- Start of picture text -->
∂u ∂v ∂v ∂u<br>and (3)<br>∂r = 1 r ∂θ ∂r =  − 1 r ∂θ<br><!-- End of picture text -->

* **Harmonic Conjugates:** Since _u_ and _v_ satisfy the C-R equations, taking further derivatives yields: 



<!-- Start of picture text -->
∂ 2 u ∂ 2 u<br>(4)<br>∂x 2 = ∂x∂y ∂ 2 v , ∂y 2 =  − ∂y∂x ∂ 2 v = ⇒∇ 2 u  = ∂ ∂x 2 u 2 + ∂ ∂y 2 u 2 = 0<br><!-- End of picture text -->

Thus, _u_ ( _x, y_ ) and _v_ ( _x, y_ ) are **harmonic functions** . _v_ ( _x, y_ ) is called the **harmonic conjugate** of _u_ ( _x, y_ ). 

2 

GATE PHYSICS 

COMPLEX ANALYSIS & CONTOUR INTEGRATION 

### **3. Analytical Milestones** 

Let us prove that the differentiability of _f_ ( _z_ ) strictly implies the Cauchy-Riemann conditions: 

1. **Path 1: Real Axis Transition (** ∆ _z →_ ∆ _x_ **with** ∆ _y_ = 0 **):** Write the derivative definition using the components: 



<!-- Start of picture text -->
[ u ( x  + ∆ x, y ) +  iv ( x  + ∆ x, y )]  − [ u ( x, y ) +  iv ( x, y )]<br>f ′ ( z ) = lim<br>∆ x→ 0 ∆ x<br>= lim +  i lim<br>∆ x→ 0 � u ( x  + ∆ x ∆ , yx )  − u ( x, y ) � ∆ x→ 0 � v ( x  + ∆ x ∆ , yx )  − v ( x, y ) �<br>= ∂u (5)<br>∂x +  i∂v ∂x<br><!-- End of picture text -->

2. **Path 2: Imaginary Axis Transition (** ∆ _z → i_ ∆ _y_ **with** ∆ _x_ = 0 **):** Evaluate the same limit along the vertical direction: 



<!-- Start of picture text -->
[ u ( x, y  + ∆ y ) +  iv ( x, y  + ∆ y )]  − [ u ( x, y ) +  iv ( x, y )]<br>f ′ ( z ) = lim<br>∆ y→ 0 i ∆ y<br>= 1 = ∂v (6)<br>i � ∂u∂y +  i∂v ∂y � ∂y − i∂u ∂y<br><!-- End of picture text -->

3. **Equate the Two Results:** Since the derivative is unique, the two expressions must be identical: 



<!-- Start of picture text -->
∂u<br>(7)<br>∂x +  i∂v ∂x = ∂y ∂v − i∂u ∂y<br><!-- End of picture text -->

Equating the real parts yields _ux_ = _vy_ , and equating the imaginary parts yields _vx_ = _−uy_ (or _uy_ = _−vx_ ). This completes the proof. 

### **4. Problem-Solving Algorithm** 

**Finding the Harmonic Conjugate and Constructing** _f_ ( _z_ ) 

Given a harmonic function _u_ ( _x, y_ ), construct the analytic function _f_ ( _z_ ) = _u_ + _iv_ using the **Milne-Thomson Method** : 

1. **Calculate the Partial Derivatives:** Compute _ϕ_ 1( _x, y_ ) _≡_<sup>_<u>∂u</u>_</sup> _∂x_<sup>and</sup><sup>_ϕ_2(</sup><sup>_x, y_)</sup><sup>_≡_</sup><sup>_<u>∂u</u>_</sup> _∂y_<sup>.</sup> 

2. **Substitute** _x_ = _z_ **and** _y_ = 0 **:** Evaluate _ϕ_ 1( _z,_ 0) and _ϕ_ 2( _z,_ 0) by replacing _x_ with the complex variable _z_ and setting _y_ to 0. 

3. **Integrate to find** _f_ ( _z_ ) **:** Use the Milne-Thomson theorem: 



<!-- Start of picture text -->
f ( z ) = [ ϕ 1( z,  0)  − iϕ 2( z,  0)]  dz  +  C (8)<br>�<br><!-- End of picture text -->

where _C_ is a complex constant of integration. 

4. **Extract** _v_ ( _x, y_ ) **if needed:** Expand _f_ ( _z_ ) back into _x_ and _y_ components and isolate the imaginary part to find the harmonic conjugate _v_ ( _x, y_ ). 

3 

GATE PHYSICS 

COMPLEX ANALYSIS & CONTOUR INTEGRATION 

### **5. Crucial Pitfalls** 

#### **Cauchy-Riemann Traps to Avoid** 

-  **The Conjugate Function Order Trap:** Assuming _u_ ( _x, y_ )+ _iv_ ( _x, y_ ) is analytic means _v_ ( _x, y_ ) + _iu_ ( _x, y_ ) is also analytic. In fact, if _f_ = _u_ + _iv_ is analytic, then _g_ = _v_ + _iu_ is **not** analytic (unless _f_ is a constant) because the C-R equations would require _vx_ = _uy_ and _vy_ = _−ux_ , which directly contradicts _ux_ = _vy_ and _uy_ = _−vx_ . 

-  **Forgetting the Sign in the polar C-R equations:** Writing<sup>_<u>∂v</u>_</sup> _∂r_<sup>=</sup><sup><u>1</u></sup> _r_ _<u>∂u∂θ</u>_<sup>insteadof</sup> the correct<sup>_<u>∂v</u>_</sup> _<u>∂u</u> ∂r_<sup>=</sup><sup>_−_</sup><sup><u>1</u></sup> _r ∂θ_<sup>.ThissignerrorisacommoncauseoflostmarksinGATE</sup> 

- polar coordinate transformations. 

### **6. Standard Applications in Physics** 

-  **2D Electrostatics (Field and Equipotential Lines):** In a charge-free 2D region, the electrostatic potential Φ( _x, y_ ) satisfies Laplace’s equation _∇_<sup>2</sup> Φ = 0. By treating Φ( _x, y_ ) as the real part _u_ ( _x, y_ ) of a complex potential _W_ ( _z_ ) = Φ+ _i_ Ψ, the C-R equations guarantee that the curves of constant potential (equipotential lines, Φ = _C_ 1) are orthogonal to the curves of constant Ψ (electric field lines, Ψ = _C_ 2). 

-  **Ideal Fluid Flow (Complex Velocity Potential):** For an incompressible, irrotational 2D fluid, the velocity vector field **v** can be represented by a velocity potential _ϕ_ ( _x, y_ ) and a stream function _ψ_ ( _x, y_ ) coupled via an analytic complex potential _F_ ( _z_ ) = _ϕ_ + _iψ_ . The physical fluid velocity components are given by _vx_ = _ϕx_ = _ψy_ and _vy_ = _ϕy_ = _−ψx_ . 

4 

GATE PHYSICS 

COMPLEX ANALYSIS & CONTOUR INTEGRATION 

## **2 Cauchy’s Integral Theorem & Formula** 

### **1. Core Theory** 

Integrals of complex functions depend in general on the path taken between the limits. However, for analytic functions, the integral along a closed curve is entirely dictated by the topology of the region and the presence of singularities. 

-  **Cauchy’s Integral Theorem (Cauchy-Goursat):** If a function _f_ ( _z_ ) is analytic and singlevalued in a simply connected domain _D_ , then for any simple closed contour _C_ lying entirely within _D_ : 



<!-- Start of picture text -->
f ( z )  dz = 0 (9)<br>� C<br><!-- End of picture text -->

-  **Simply Connected vs. Multiply Connected Domains:** A domain is simply connected if any closed loop can be shrunk continuously to a point without leaving the domain (i.e., it has no ”holes”). For multiply connected domains, the presence of internal singular ”holes” violates the theorem, requiring the deformation of contours. 

-  **Cauchy’s Integral Formula:** If _f_ ( _z_ ) is analytic within and on a simple closed contour _C_ , and _z_ 0 is any point in the interior of _C_ , then _f_ ( _z_ 0) is completely determined by the boundary values of _f_ ( _z_ ) on _C_ : 



<!-- Start of picture text -->
1 f ( z )<br>f ( z 0) = dz (10)<br>2 πi � C z − z 0<br><!-- End of picture text -->

### **2. Mathematical Framework & Theorems** 

* **The Generalised Cauchy’s Integral Formula:** If _f_ ( _z_ ) is analytic within and on a closed contour _C_ , then its _n_ -th derivative at an interior point _z_ 0 exists, implying that an analytic function is infinitely differentiable: 



<!-- Start of picture text -->
f ( z )<br>f ( n ) ( z 0) = n ! (11)<br>2 πi � C ( z − z 0) n +1 dz<br><!-- End of picture text -->

* **Liouville’s Theorem:** If _f_ ( _z_ ) is entire (analytic everywhere in C) and bounded (there exists a real constant _M_ such that _|f_ ( _z_ ) _| ≤ M_ for all _z ∈_ C), then _f_ ( _z_ ) must be a constant. * **The Fundamental Theorem of Algebra:** Every non-constant polynomial of degree _n_ has exactly _n_ complex roots (derived directly as a consequence of Liouville’s theorem). 

### **3. Analytical Milestones** 

Let us derive Cauchy’s Integral Formula using Cauchy’s Integral Theorem: 

- _<u>f</u>_ <u>(</u> _z_ <u>)</u> 

- 1. **Set up the Singular Integrand:** Define the function _g_ ( _z_ ) _≡ z−z_ 0<sup>.Since</sup><sup>_f_(</sup><sup>_z_)isanalytic</sup> within and on _C_ , _g_ ( _z_ ) is analytic everywhere except at the single point _z_ = _z_ 0. 

2. **Deform the Contour:** Construct a tiny circle _C_ 0 of radius _r_ centered at _z_ 0 lying entirely inside _C_ . By Cauchy’s theorem for multiply connected domains (contour deformation): 



<!-- Start of picture text -->
f ( z ) f ( z )<br>dz = dz (12)<br>� C z − z 0 � C 0 z − z 0<br><!-- End of picture text -->

5 

GATE PHYSICS 

COMPLEX ANALYSIS & CONTOUR INTEGRATION 

3. **Parametrise the Small Circle** _C_ 0 **:** Express _z_ on _C_ 0 as _z_ = _z_ 0 + _re_<sup>_iθ_</sup> , where _θ_ ranges from 0 to 2 _π_ . Thus, _dz_ = _ire_<sup>_iθ_</sup> _dθ_ , and: 



<!-- Start of picture text -->
f ( z ) f ( z 0 +  re iθ )<br>dz = ( ire iθ )  dθ =  i f ( z 0 +  re iθ )  dθ (13)<br>� C 0 z − z 0 �02 π re iθ �02 π<br><!-- End of picture text -->



<!-- Start of picture text -->
4. Take the Limit r → 0 : Since this equality holds for any arbitrarily small radius  r , let  r → 0.<br>Because f ( z ) is continuous at z 0, lim r→ 0  f ( z 0 +  re iθ ) =  f ( z 0):<br>f ( z )<br>dz =  i f ( z 0)  dθ =  if ( z 0)[2 π ] = 2 πif ( z 0) (14)<br>� C z − z 0 �02 π<br><!-- End of picture text -->

Dividing by 2 _πi_ yields the classic Cauchy’s Integral Formula. 

### **4. Problem-Solving Algorithm** 

#### **Evaluating Integrals using Cauchy’s Integral Formulas** 

_<u>g</u>_ <u>(</u> _z_ <u>)</u> To evaluate a contour integral of the form _I_ = � _C_ ( _z−z_ 0)<sup>_<u>m</u>dz_:</sup> 

1. **Locate the Singularity:** Identify the point _z_ 0 where the denominator vanishes. 

2. **Check the Contour Boundary:** Check if the singularity _z_ 0 lies **inside** or **outside** the closed contour _C_ : 

   -  If _z_ 0 is **outside** _C_ , the integrand is analytic everywhere inside the contour. By Cauchy’s theorem: _I_ = 0. 

   -  If _z_ 0 is **inside** _C_ , proceed to Step 3. 

3. **Identify the Power and Derivative Order:** Note the exponent _m_ in the denominator: 

   -  If _m_ = 1: Use _I_ = 2 _πi · g_ ( _z_ 0). 

   -  If _m >_ 1: Identify _n_ = _m −_ 1. Calculate the _n_ -th derivative _g_<sup>(</sup><sup>_n_)</sup> ( _z_ ) and evaluate it at _z_ 0. Use: _I_ =<sup>2</sup> _n_<sup>_πi_</sup> !<sup>_· g_(</sup><sup>_n_)(</sup><sup>_z_0)</sup> (15) 

### **5. Crucial Pitfalls** 

#### **Contour Integration Traps to Avoid** 

-  **The Outside Singularity Oversight:** Blindly applying the formula 2 _πig_ ( _z_ 0) without checking if _z_ 0 lies inside the specified contour. If the contour is _|z|_ = 1 and the integral is � <u>sin</u> _z− z_ 5<sup>_dz_,thepole</sup><sup>_z_=5liesoutsidetheboundary,meaningtheintegralisstrictly</sup> **0**, not 2 _πi_ sin(5). 

-  **Derivative Factorial Omissions:** Forgetting the division by _n_ ! when evaluating higher-order poles. For a second-order pole ( _m_ = 2 _, n_ = 1), the divider is 1! = 1, but for a third-order pole ( _m_ = 3 _, n_ = 2), you must divide by 2! = 2. 

6 

GATE PHYSICS 

COMPLEX ANALYSIS & CONTOUR INTEGRATION 

### **6. Standard Applications in Physics** 

-  **Kramers-Kronig Relations (Optics & Materials Physics):** Relate the real and imaginary parts of the complex susceptibility _χ_ ( _ω_ ) = _χ_ 1( _ω_ ) + _iχ_ 2( _ω_ ) of a physical medium. Because _χ_ ( _ω_ ) is analytic in the upper half-plane (a consequence of physical causality), applying Cauchy’s Integral Formula to a contour along the real axis yields: 



<!-- Start of picture text -->
χ 1( ω ) = π 1 P � −∞∞ ωχ 2 ′ ( −ω ′ ω ) dω′, χ 2( ω ) =  − π 1 P � −∞∞ ωχ 1 ′ ( −ω ′ ω ) dω′ (16)<br><!-- End of picture text -->

where _P_ denotes the Cauchy Principal Value. 

7 

GATE PHYSICS 

COMPLEX ANALYSIS & CONTOUR INTEGRATION 

## **3 Laurent Series & Classification of Singularities** 

### **1. Core Theory** 

When a complex function ceases to be analytic at certain points, Taylor series expansions become invalid. Instead, we expand the function in a **Laurent Series**, which includes terms with negative powers of ( _z − z_ 0) to describe the behavior near the singular points. 

-  **Singularity:** A point _z_ 0 at which a complex function _f_ ( _z_ ) fails to be analytic, although it may be analytic in neighboring points. 

-  **Isolated Singularity:** A singularity _z_ 0 is isolated if there exists an open neighborhood of _z_ 0 that contains no other singularities of _f_ ( _z_ ). 

-  **Non-Isolated Singularity:** Occurs when every neighborhood of _z_ 0 contains other singular points (e.g., limit points of poles, or branch cuts of multi-valued functions). 

### **2. Mathematical Framework & Theorems** 

* **Laurent’s Theorem:** If _f_ ( _z_ ) is analytic inside an annular domain _R_ 1 _< |z − z_ 0 _| < R_ 2, it can be uniquely represented as: 



<!-- Start of picture text -->
∞ ∞ bn<br>f ( z ) = � an ( z − z 0) n + � (17)<br>n =0 n =1 ( z − z 0) n<br><!-- End of picture text -->

where the first term is the **analytic part** (regular part) and the second term is the **principal part** . * **Classification of Isolated Singularities:** Based on the structure of the principal part of the Laurent series about _z_ 0: 

1. **Removable Singularity:** The principal part has zero terms ( _bn_ = 0 for all _n ≥_ 1). The limit lim _z→z_ 0 _f_ ( _z_ ) exists and is finite. * *Example:* _f_ ( _z_ ) =<sup><u>sin</u></sup> _z_<sup>_<u>z</u>_</sup> at _z_ = 0. 

2. **Pole of Order** _m_ **:** The principal part has a finite number of terms ( _bm̸_ = 0 and _bn_ = 0 for all _n > m_ ). * *Example:* _f_ ( _z_ ) = ( _z_ <u>cos</u> _−a z_ )<sup>2hasapoleoforder2at</sup><sup>_z_=</sup><sup>_a_.If</sup><sup>_m_=1,itisa</sup> **simple pole** . 

3. **Essential Singularity:** The principal part contains an infinite number of non-zero terms. The function exhibits wild, infinite oscillations near _z_ 0 (described by Picard’s Theorem). * *Example:* _f_ ( _z_ ) = _e_<sup>1</sup><sup>_/z_</sup> at _z_ = 0. 

* **Branch Points and Branch Cuts (Non-Isolated):** For multi-valued functions (such as ln _z_ or _z_<sup>1</sup><sup>_/_2</sup> ), the point around which a complete circuit changes the value of the function is a **branch point** . To make the function single-valued, we restrict the domain by drawing a boundary line called a **branch cut** . 

### **3. Analytical Milestones** 

Let us mathematically classify the singularity of _f_ ( _z_ ) = _e_<sup>1</sup><sup>_/z_</sup> at _z_ = 0: 

1. **Write the Expansion of the Exponential Function:** We know the Taylor series of _e_<sup>_w_</sup> is entire: 



<!-- Start of picture text -->
∞ w n<br>e w = � n ! = 1 +  w  + w 2! 2 + w 3! 3 +  . . . (18)<br>n =0<br><!-- End of picture text -->

8 

GATE PHYSICS 

COMPLEX ANALYSIS & CONTOUR INTEGRATION 

2. **Substitute** _w_ = 1 _/z_ **:** This substitution is valid for all _z̸_ = 0: 



<!-- Start of picture text -->
e 1 /z = 1 + z 1 + 2!1 z 2 + 3!1 z 3 +  · · ·  = 1 + � ∞ n !  · 1  z n (19)<br>n =1<br><!-- End of picture text -->

3. **Analyze the Principal Part:** The Laurent series has no positive powers of _z_ (the analytic part is just the constant 1), but the principal part: 



<!-- Start of picture text -->
� ∞ zbn n where bn = n 1 ! ̸ = 0 (20)<br>n =1<br><!-- End of picture text -->

possesses infinitely many non-zero negative power terms. Thus, by definition, _z_ = 0 is an **essential singularity** . 

### **4. Problem-Solving Algorithm** 

#### **Classifying Singularities without Laurent Expansion** 

To classify the isolated singularity of _f_ ( _z_ ) at _z_ = _z_ 0: 

1. **Evaluate the Limit** lim _z→z_ 0 _f_ ( _z_ ) **:** 

   -  If the limit is finite, _z_ 0 is a **removable singularity** . 

   -  If the limit is infinite ( _∞_ ), _z_ 0 is a **pole** . Proceed to Step 2. 

   -  If the limit does not exist (oscillates between multiple values), _z_ 0 is an **essential singularity** . 

2. **Determine the Pole Order (** _m_ **):** Find the smallest positive integer _m_ such that: _z_ lim _→z_ 0<sup>[(</sup><sup>_z −z_0)</sup><sup>_mf_(</sup><sup>_z_)] =</sup><sup>_L_</sup> where 0 _< |L| < ∞_ (21) 

This integer _m_ is the order of the pole. 

### **5. Crucial Pitfalls** 

#### **Singularity and Limit Errors** 

-  **Confusing Essential Singularities with Poles:** Assuming _f_ ( _z_ ) = sin(1 _/z_ ) has a pole at _z_ = 0. Because sin(1 _/z_ ) = _z_<sup><u>1</u></sup><sup>_−_</sup> 3!1 _z_<sup>3+</sup><sup>_. . ._,theprincipalparthasinfiniteterms,</sup> making _z_ = 0 an essential singularity, not a simple pole. 

-  **Forgetting to check the Limit Condition:** Assuming _f_ ( _z_ ) =<sup>_<u>z</u>_</sup> _z_<sup>2</sup> _−_<sup>_−_</sup> 2<sup><u>4</u>hasapoleat</sup> _z_ = 2. Since lim _z→_ 2 _f_ ( _z_ ) = lim( _z_ + 2) = 4, the singularity is actually removable. 

### **6. Standard Applications in Physics** 

-  **Green’s Functions in Quantum Mechanics & Electrodynamics:** The Green’s function (propagator) for a physical system often contains poles on the real frequency or energy axis. 

9 

GATE PHYSICS 

COMPLEX ANALYSIS & CONTOUR INTEGRATION 

For example, the free particle propagator contains poles at _E_ = _p_<sup>2</sup> _/_ 2 _m_ . To resolve these non-isolated physical singularities, we apply an infinitesimal complex shift: 



<!-- Start of picture text -->
1<br>G ± ( E ) = (where ϵ → 0 + ) (22)<br>E − H ˆ 0  ± iϵ<br><!-- End of picture text -->

shifting the poles off the real axis to construct retarded (+) or advanced ( _−_ ) boundary propagators. 

10 

GATE PHYSICS 

COMPLEX ANALYSIS & CONTOUR INTEGRATION 

## **4 The Residue Theorem & Contour Integration** 

### **1. Core Theory** 

* **The Residue:** The coefficient _b_ 1 of the 1 _/_ ( _z − z_ 0) term in the Laurent series of _f_ ( _z_ ) about the isolated singularity _z_ 0. It represents the ”residue” or left-over portion of a contour integral around _z_ 0. * **Cauchy’s Residue Theorem:** If _f_ ( _z_ ) is analytic within and on a simple closed contour _C_ , except at a finite number of isolated singularities _{z_ 1 _, z_ 2 _, . . . , zm}_ in the interior of _C_ , then the closed loop integral is simply 2 _πi_ times the sum of the residues at those points: 



<!-- Start of picture text -->
m<br>f ( z )  dz = 2 πi � Res( f, zk ) (23)<br>� C<br>k =1<br><!-- End of picture text -->

* **Physical Significance:** Allows us to evaluate highly complex real definite integrals (such as Fourier transforms, scattering cross-sections, and spectral densities) that are difficult or impossible to integrate using classical real variable techniques. 

### **2. Mathematical Framework & Theorems** 

* **Residue Formula for a Simple Pole (** _m_ = 1 **):** 



<!-- Start of picture text -->
Res( f, z 0) = z lim →z 0 ( z − z 0) f ( z ) (24)<br><!-- End of picture text -->

*If _f_ ( _z_ ) = _Q_<sup>_P_</sup><sup><u>(</u></sup> (<sup>_z_</sup> _z_<sup><u>)</u></sup> )<sup>where</sup><sup>_P_(</sup><sup>_z_0)</sup><sup>_̸_= 0and</sup><sup>_Q_(</sup><sup>_z_)hasasimplezeroat</sup><sup>_z_0(</sup><sup>_Q_(</sup><sup>_z_0) = 0</sup><sup>_, Q′_(</sup><sup>_z_0)</sup><sup>_̸_= 0):*</sup> 



<!-- Start of picture text -->
Res( f, z 0) = P ( z 0) (25)<br>Q ′ ( z 0)<br><!-- End of picture text -->

* **Residue Formula for a Pole of Order** _m_ **:** 



<!-- Start of picture text -->
1 d m− 1<br>Res( f, z 0) = ( m − 1)! z lim →z 0 dz m− 1 [( z − z 0) mf ( z )] (26)<br><!-- End of picture text -->

* **Jordan’s Lemma:** If _f_ ( _z_ ) converges uniformly to 0 as _|z| →∞_ in the upper half-plane (Im( _z_ ) _≥_ 0), then for any real positive _k_ : 



<!-- Start of picture text -->
lim f ( z ) e ikz dz = 0 (27)<br>R→∞ � CR<br><!-- End of picture text -->

where _CR_ is a semicircular arc of radius _R_ in the upper half-plane. 

### **3. Analytical Milestones** 

Let us prove Cauchy’s Residue Theorem using Cauchy’s Integral Theorem for multiply connected domains: 

1. **Isolate the Singularities with Small Circles:** Let _C_ be the outer contour enclosing singularities _{z_ 1 _, z_ 2 _, . . . , zm}_ . Enclose each singularity _zk_ in a tiny circle _Ck_ of radius _rk_ such that no two circles overlap. 

11 

GATE PHYSICS 

COMPLEX ANALYSIS & CONTOUR INTEGRATION 

2. **Deform the Boundary:** By Cauchy’s multi-boundary theorem, the integral along the outer boundary _C_ equals the sum of integrals along the inner circular boundaries: 



<!-- Start of picture text -->
m<br>f ( z )  dz = � f ( z )  dz (28)<br>� C k =1 � Ck<br><!-- End of picture text -->

3. **Substitute the Laurent Expansion on each circle** _Ck_ **:** For each circle _Ck_ , substitute the Laurent series of _f_ ( _z_ ) about _zk_ : 



<!-- Start of picture text -->
∞ ∞<br>f ( z )  dz = � cn ( z − zk ) n dz = � cn ( z − zk ) n dz (29)<br>� Ck � Ck � n = −∞ � n = −∞ � Ck<br><!-- End of picture text -->

4. **Evaluate the Term-by-Term Integrals:** Using parametrisation _z_ = _zk_ + _rke_<sup>_iθ_</sup> : 



<!-- Start of picture text -->
2 πi for n  =  − 1<br>( z − zk ) n dz = (30)<br>� Ck �0 for n̸  =  − 1<br><!-- End of picture text -->

Thus, only the _n_ = _−_ 1 term (which is the residue _b_ 1 _≡ c−_ 1) survives: 



<!-- Start of picture text -->
f ( z )  dz = 2 πi · c− 1 = 2 πi Res( f, zk ) (31)<br>� Ck<br><!-- End of picture text -->

Summing over all _m_ circles yields the Residue Theorem. 

### **4. Problem-Solving Algorithm** 

#### **Evaluating Real Definite Integrals using Contour Integration** 

To evaluate a real infinite integral of the form _I_ = 

� _−∞∞ QP_ <u>((</u> _xx_ <u>))</u><sup>_dx_:</sup> 

1. **Transform to the Complex Plane:** Replace _x_ with _z_ to form _f_ ( _z_ ) =<sup>_P_</sup><sup><u>(</u></sup><sup>_z_</sup><sup><u>)</u></sup> _Q_ ( _z_ )<sup>.</sup> 

2. **Select the Closed Contour** _C_ **:** Choose a semicircular contour consisting of the real axis from _−R_ to + _R_ , and a large semicircular arc _CR_ of radius _R_ in the upper half-plane. Let _R →∞_ . 

3. **Locate the Poles:** Find all roots of _Q_ ( _z_ ) = 0. 

4. **Filter Poles in the Upper Half-Plane:** Identify which of these poles have a positive imaginary part (Im( _z_ ) _>_ 0). Only these poles lie **inside** the upper half-plane contour. 

5. **Calculate the Residues:** Compute the residues for all active poles inside the boundary. 

6. **Apply the Residue Theorem:** Use Jordan’s lemma to set the contribution along _CR_ to zero, leaving: 

_I_ = _f_ ( _x_ ) _dx_ = 2 _πi_ � Res( _f, zk_ ) (32) � _−∞∞_ Im( _zk_ ) _>_ 0 

12 

GATE PHYSICS 

COMPLEX ANALYSIS & CONTOUR INTEGRATION 

### **5. Crucial Pitfalls** 

#### **Residue Theorem Traps to Avoid** 

-  **Including Lower Half-Plane Poles:** Calculating residues for poles in the lower half-plane (Im( _z_ ) _<_ 0) when integrating over the upper half-plane semicircle. This is a highly frequent source of numerical errors. 

-  **Simple Pole Formula for Multiple Poles:** Attempting to calculate the residue of a second-order pole using the simple pole formula lim( _z − z_ 0) _f_ ( _z_ ). This yields an infinite result. You must apply the derivative formula: Res = lim _dz_<sup>_<u>d</u>_[(</sup><sup>_z −z_0)2</sup><sup>_f_(</sup><sup>_z_)].</sup> 

-  **Incorrect Contour Direction:** Assuming all closed paths are counterclockwise. If a contour is oriented clockwise, the Residue Theorem must include a negative sign: � = _−_ 2 _πi_<sup>�</sup> Res. 

### **6. Standard Applications in Physics** 

-  **Propagators in Quantum Field Theory (QFT):** In calculating the scattering amplitude or propagator of a scalar boson of mass _m_ , the Fourier transform leads to: 



<!-- Start of picture text -->
d 4 p e −ip· ( x−y )<br>∆ F  ( x − y ) = (33)<br>� (2 π ) 4 p 2 − m 2 +  iϵ<br><!-- End of picture text -->

This integration is performed in the complex _p_ 0 plane using the residue theorem, where the poles are located at _p_ 0 = _±_ ( ~~�~~ **p**<sup>2</sup> + _m_<sup>2</sup> _− iϵ_ ). 

-  **Dispersion Relations in Scattering Theory:** In particle physics, scattering amplitudes _A_ ( _E_ ) are analytical functions of the energy. By setting up a contour integral around a closed loop in the complex energy plane, we express the real part of the scattering amplitude (representing elastic dispersion) as an integral over the imaginary part (representing absorption/total cross-section), establishing a direct link to the **Optical Theorem**. 

13 

GATE PHYSICS 

COMPLEX ANALYSIS & CONTOUR INTEGRATION 

## **References** 

1. Arfken, George, and Weber, Hans. _Mathematical Methods for Physicists_ . Elsevier, 2005. 

2. Kreyszig, Erwin. _Advanced Engineering Mathematics_ . Wiley, 2011. 

3. Zettili, Nouredine. _Quantum Mechanics: Concepts and Applications_ . Wiley, 2009. 

14 

GATE PHYSICS 

FOURIER ANALYSIS & TENSOR CALCULUS 

# **GATE PHYSICS STUDY NOTES Fourier Analysis & Fundamentals of Tensor Calculus** 

**Author: Expert GATE Physics Professor Target Exam: GATE Physics (Graduate Aptitude Test in Engineering)** 

## **Contents** 

|**1**<br>**Fourier Analysis: Fourier Series & Fourier Transforms**|**2**|
|---|---|
|**2**<br>**Fundamentals of Tensor Calculus**|**6**|



1 

GATE PHYSICS 

FOURIER ANALYSIS & TENSOR CALCULUS 

## **1 Fourier Analysis: Fourier Series & Fourier Transforms** 

### **1. Core Theory** 

-  **Fourier Series:** A mathematical tool used to represent any periodic function _f_ ( _x_ ) of period _T_ as an infinite linear combination of orthogonal trigonometric basis functions (sines and cosines) or complex exponentials. 

-  **Fourier Transform:** An extension of the Fourier series to non-periodic, square-integrable functions by taking the limit of the period _T →∞_ . It maps a continuous function from the time or spatial domain to the frequency or wavevector domain, revealing its spectral density. 

-  **Physical Significance:** 

   - **Spectral Decomposition:** In wave mechanics and optics, it decomposes a complex, polychromatic waveform into individual monochromatic harmonic components. 

   - **Quantum Momentum Space:** In quantum mechanics, the spatial wave function _ψ_ ( _x_ ) and momentum-space wave function _ϕ_ ( _p_ ) are Fourier transform pairs, representing the dual wave-particle aspects of physical states. 

### **2. Mathematical Framework & Theorems** 

-  **Dirichlet Conditions (Sufficient Conditions for Convergence):** For a periodic function _f_ ( _x_ ) of period _T_ = 2 _L_ to be representable as a Fourier series, it must satisfy: 

   1. _f_ ( _x_ ) must be single-valued and piecewise continuous (possessing only a finite number of finite discontinuities) on any period. 

   2. _f_ ( _x_ ) must have a finite number of local maxima and minima within a single period. 

   3. _f_ ( _x_ ) must be absolutely integrable over a period: � _−LL_<sup>_|f_(</sup><sup>_x_)</sup><sup>_|dx < ∞_.</sup> 

At a point of discontinuity _x_ 0, the Fourier series converges to the average value: 2<sup><u>1</u></sup> �lim _x→x_ +0<sup>_f_(</sup><sup>_x_) + lim</sup><sup>_x→x−_</sup> 0<sup>_f_(</sup> 

-  **Trigonometric Fourier Series:** 



<!-- Start of picture text -->
∞<br>f ( x ) = a 2 0 + � � an  cos � nπxL � +  bn  sin � nπxL �� (1)<br>n =1<br><!-- End of picture text -->

where the Fourier coefficients are defined by the **Euler-Fourier Formulas** : 



<!-- Start of picture text -->
a 0 = 1 f ( x ) dx, an = 1 f ( x ) cos dx (2)<br>L � −LL L � −LL � nπxL �<br><!-- End of picture text -->



<!-- Start of picture text -->
bn = 1 f ( x ) sin dx (3)<br>L � −LL � nπxL �<br><!-- End of picture text -->

 **Complex Exponential Fourier Series:** 



<!-- Start of picture text -->
∞<br>f ( x ) = n =� −∞ cne i nπx L with cn = 2 1 L � −LL f ( x ) e −i nπx L dx (4)<br>the real and complex coefficients are related by:<br>c 0 = a 0 cn = an − ibn , c−n = an  +  ibn ( n ≥ 1) (5)<br>2 , 2 2<br><!-- End of picture text -->

where the real and complex coefficients are related by: 

2 

GATE PHYSICS 

FOURIER ANALYSIS & TENSOR CALCULUS 

 **Continuous Fourier Transform (Symmetric Convention):** 



<!-- Start of picture text -->
1<br>F ( k ) =  F [ f ( x )] = f ( x ) e −ikx dx (6)<br>√ 2 π � ∞∞<br><!-- End of picture text -->



<!-- Start of picture text -->
1<br>f ( x ) =  F − 1 [ F ( k )] = F ( k ) e ikx dk (7)<br>√ 2 π � ∞∞<br><!-- End of picture text -->

where _x_ is the spatial coordinate, and _k_ is the conjugate wavevector. 

-  **Parseval’s Identity & Plancherel’s Theorem:** Guarantees the conservation of total energy or probability between the physical and spectral domains: 



<!-- Start of picture text -->
1 ∞ ∞<br>Series: 2 L � −LL |f ( x ) | 2 dx  = n =� −∞ |cn| 2 = a 40 2 + 2 1 n �=1( a 2 n +  b n 2 ) (8)<br><!-- End of picture text -->



<!-- Start of picture text -->
Transform: |f ( x ) | 2 dx  = |F ( k ) | 2 dk (9)<br>� −∞∞ � −∞∞<br><!-- End of picture text -->

-  **The Convolution Theorem:** The Fourier transform of the convolution of two functions _f_ ( _x_ ) and _g_ ( _x_ ), defined as ( _f ∗ g_ )( _x_ ) _≡_ � _−∞∞_<sup>_f_(</sup><sup>_u_)</sup><sup>_g_(</sup><sup>_x −u_)</sup><sup>_du_,isproportionaltotheproductof</sup> their individual transforms: 



<!-- Start of picture text -->
F [( f ∗ g )( x )] = √ 2 πF [ f ( x )]  · F [ g ( x )] = √ 2 πF ( k ) G ( k ) (10)<br><!-- End of picture text -->

### **3. Analytical Milestones** 

Let us step through two foundational derivations in Fourier analysis: 

1. **Orthogonality Proof of the Trigonometric Basis:** To prove that the basis functions _{_ 1 _,_ cos( _nx_ ) _,_ sin( _nx_ ) _}_ are mutually orthogonal over the interval [ _−π, π_ ]: 

(a) Evaluate the inner product of two distinct cosine terms: 



<!-- Start of picture text -->
I = cos( nx ) cos( mx ) dx  = 1 [cos(( n  +  m ) x ) + cos(( n − m ) x )]  dx (11)<br>� −ππ 2 � −ππ<br><!-- End of picture text -->

(b) For _n̸_ = _m_ , integrating over the symmetric boundaries yields: 



<!-- Start of picture text -->
I = 1 + sin(( n − m ) x ) = 0 (12)<br>2 � sin(( nn  + +  m m ) x ) n − m � π−π<br><!-- End of picture text -->

(c) For _n_ = _m >_ 0, the second cosine term becomes cos(0) = 1: 



<!-- Start of picture text -->
I = 1 [cos(2 nx ) + 1]  dx  = 1 +  x =  π (13)<br>2 � −ππ 2 � sin(22 nnx ) � π−π<br><!-- End of picture text -->

This establishes � _−ππ_<sup>cos(</sup><sup>_nx_) cos(</sup><sup>_mx_)</sup><sup>_dx_=</sup><sup>_πδnm_(for</sup><sup>_n, m≥_1).Asimilarintegration</sup> yields � _−ππ_<sup>sin(</sup><sup>_nx_) sin(</sup><sup>_mx_)</sup><sup>_dx_=</sup><sup>_πδnm_,and</sup> � _−ππ_<sup>cos(</sup><sup>_nx_) sin(</sup><sup>_mx_)</sup><sup>_dx_= 0forall</sup><sup>_n, m_.</sup> 

2. **Transition from Fourier Series to Fourier Integral (** _L →∞_ **):** 

3 

GATE PHYSICS 

FOURIER ANALYSIS & TENSOR CALCULUS 

(a) Represent _f_ ( _x_ ) via the complex exponential Fourier series over [ _−L, L_ ]: 



<!-- Start of picture text -->
∞<br>f ( x ) = n =� −∞ � 21 L � −LL f ( t ) e −iknt dt � e iknx where kn = nπ L (14)<br><!-- End of picture text -->

(b) Define the discrete interval spacing: ∆ _k_ = _kn_ +1 _− kn_ = _L_<sup>_<u>π</u>_=</sup><sup>_⇒_</sup> 21 _L_<sup>=</sup><sup><u>∆</u></sup> 2 _π_<sup>_<u>k</u>_.Rewritethe</sup> sum: 



<!-- Start of picture text -->
∞<br>f ( x ) = 2 1 π n =� −∞ �� −LL f ( t ) e −iknt dt � e iknx ∆ k (15)<br><!-- End of picture text -->

- (c) Take the limit _L →∞_ . The discrete wavevector spacing becomes infinitesimal (∆ _k → dk_ ), and the summation converges to a continuous integral over _k_ : 



<!-- Start of picture text -->
f ( x ) = 1 f ( t ) e −ikt dt e ikx dk (16)<br>2 π � −∞∞ �� −∞∞ �<br><!-- End of picture text -->

This is the double integral representation that defines the forward and inverse Fourier transforms. 

### **4. Problem-Solving Algorithm** 

#### **Calculating Fourier Coefficients and Simplifying Series** 



<!-- Start of picture text -->
1. Check for Symmetry (Even/Odd Functions): Before integrating, check if<br>f ( −x ) =  f ( x ) (even) or f ( −x ) =  −f ( x ) (odd) over the symmetric interval [ −L, L ]:<br><!-- End of picture text -->



<!-- Start of picture text -->
 If f ( x ) is even : bn = 0 for all n . You only need to calculate:<br><!-- End of picture text -->



<!-- Start of picture text -->
a 0 = 2 f ( x ) dx, an = 2 f ( x ) cos dx (17)<br>L �0 L L �0 L � nπxL �<br><!-- End of picture text -->



<!-- Start of picture text -->
 If f ( x ) is odd : a 0 = 0 and an = 0 for all n . You only need to calculate:<br><!-- End of picture text -->



<!-- Start of picture text -->
bn = 2 f ( x ) sin dx (18)<br>L �0 L � nπxL �<br><!-- End of picture text -->

2. **Evaluate the Integrals:** Use standard integration techniques, particularly integration by parts. 

3. **Handle Discontinuity Boundaries:** If the function is defined piecewise, split the integral across the boundary zones. 

4. **Apply Truncation or Summation Values:** If asked to evaluate an infinite numerical series (e.g.,<sup>�</sup> _n_<sup><u>12</u>),evaluatetheFourierseriesataspecificboundarypoint</sup><sup>_x_0(using</sup> Dirichlet’s average value rule at discontinuities) or apply Parseval’s identity. 

4 

GATE PHYSICS 

FOURIER ANALYSIS & TENSOR CALCULUS 

### **5. Crucial Pitfalls** 

#### **Fourier Analysis Traps to Avoid** 

-  **The Gibbs Phenomenon Overshoot:** Assuming that a Fourier series represents a discontinuous function perfectly at the boundary. At any sharp step discontinuity, truncating the Fourier series at _N_ terms always leaves a persistent **9.0% overshoot** on either side of the step, regardless of how large _N_ becomes. The overshoot width shrinks to zero as _N →∞_ , but its amplitude does not. 

-  **Normalization Constant Mismatches:** Mixing different Fourier transform conventions. The symmetric convention uses 1 _/_ _~~√~~_ 2 _π_ for both the forward and inverse transforms. The asymmetric engineering convention uses 1 for the forward transform and 1 _/_ 2 _π_ for the inverse. Mixing these conventions within a single problem will introduce factors of _~~√~~_ 2 _π_ or 2 _π_ into your final answer. 

-  **Neglecting Phase Factors in Shifts:** Forgetting the exponential phase shift factor. If _F_ [ _f_ ( _x_ )] = _F_ ( _k_ ), then the Fourier transform of a shifted function _f_ ( _x−x_ 0) is _F_ [ _f_ ( _x− x_ 0)] = _e_<sup>_−ikx_0</sup> _F_ ( _k_ ). 

### **6. Standard Applications in Physics** 

-  **The 1D Heat Equation (Thermal Diffusion):** A long, thin rod of length _L_ with initial temperature profile _T_ ( _x,_ 0) = _f_ ( _x_ ) and endpoints held at 0<sup>_◦_</sup> C satisfies: 



<!-- Start of picture text -->
∂T<br>(19)<br>∂t =  α∂ ∂x 2 T 2<br><!-- End of picture text -->

Solving by separation of variables yields _T_ ( _x, t_ ) =<sup>�</sup><sup>_∞_</sup> _n_ =1<sup>_bn_sin(</sup><sup>_nπx/L_)</sup><sup>_e−α_(</sup><sup>_nπ/L_)2</sup><sup>_t_,wherethe</sup> coefficients _bn_ are the Fourier sine coefficients of the initial temperature profile _f_ ( _x_ ). 

-  **Quantum Momentum Probability Density:** A particle in a 1D spatial quantum state is represented by the wave function _ψ_ ( _x_ ). The probability amplitude of finding the particle with momentum _p_ = ℏ _k_ is given by the Fourier transform: 



<!-- Start of picture text -->
1<br>ϕ ( p ) = ψ ( x ) e −i p ℏ x dx (20)<br>√ 2 π ℏ � −∞∞<br><!-- End of picture text -->

which directly illustrates the Heisenberg Uncertainty Principle as a property of Fourier transform scaling (squeezing _ψ_ ( _x_ ) spreads _ϕ_ ( _p_ )). 

5 

GATE PHYSICS 

FOURIER ANALYSIS & TENSOR CALCULUS 

## **2 Fundamentals of Tensor Calculus** 

### **1. Core Theory** 

-  **Tensors:** Geometric entities whose coordinate representations (components) transform in specific, linear ways under changes of the coordinate system. Tensors are coordinate-independent objects, making them the standard mathematical language for expressing physical laws covariantly across all reference frames. 

-  **Covariant vs. Contravariant Components:** 

   - **Contravariant Tensors (Upper Indices,** _A_<sup>_i_</sup> **):** Represent quantities whose components transform like coordinate differentials ( _dx_<sup>_i_</sup> ), scaling _inversely_ with changes to the basis vector lengths. Examples include position differentials, velocity, and force. 

   - **Covariant Tensors (Lower Indices,** _Ai_ **):** Represent quantities whose components transform like the gradient of a scalar field ( _∂ϕ/∂x_<sup>_i_</sup> ), scaling _directly_ with changes to the basis vector lengths. Examples include the gradient of a potential, dual vectors, and normals to surfaces. 

-  **Physical Significance:** In general relativity and classical mechanics, physical properties must be independent of the arbitrary coordinate grids we use to measure them. Tensors ensure this covariance. 

### **2. Mathematical Framework & Theorems** 

Let _x_<sup>_i_</sup> _→ x_ ¯<sup>_i_</sup> represent a smooth coordinate transformation from an unbarred to a barred system. 

-  **Contravariant Vector (Rank 1 Contravariant Tensor):** A set of components _A_<sup>_i_</sup> that transform according to: 



<!-- Start of picture text -->
A ¯ i = ∂x ∂x ¯ ji Aj (using Einstein Summation Convention) (21)<br><!-- End of picture text -->

where repeated indices (one upper, one lower) are implicitly summed over:<sup>�</sup> _j ∂x∂x_ ¯<sup>_jiAj_.</sup> 

-  **Covariant Vector (Rank 1 Covariant Tensor):** A set of components _Ai_ that transform according to: 



<!-- Start of picture text -->
A ¯ i = ∂x ∂x ¯ ji Aj (22)<br><!-- End of picture text -->

-  **Rank 2 Tensors:** 

**– Contravariant Rank 2:** _T_<sup>¯</sup><sup>_ij_</sup> = _∂x_<sup>_<u>∂x</u>_¯</sup><sup>_ki_</sup><sup>_<u>∂</u>_</sup> _∂x_<sup>_<u>x</u>_¯</sup><sup>_jlT kl_</sup> **– Covariant Rank 2:** _T_<sup>¯</sup> _ij_ =<sup>_<u>∂x</u>_</sup> _∂x_ ¯<sup>_ki_</sup> _∂_<sup>_<u>∂x</u>_</sup> _x_ ¯<sup>_jlTkl_</sup> **– Mixed Rank 2:** _T_<sup>¯</sup><sup>_i_</sup> _j_<sup>=</sup> _∂x_<sup>_<u>∂x</u>_¯</sup><sup>_ki_</sup> _∂_<sup>_<u>∂x</u>_</sup> _x_ ¯<sup>_jlT k_</sup> _l_ 

-  **The Metric Tensor (** _gij_ **):** A symmetric covariant rank 2 tensor that defines the inner product, arc length ( _ds_<sup>2</sup> = _gijdx_<sup>_i_</sup> _dx_<sup>_j_</sup> ), and the geometry of the space. 



<!-- Start of picture text -->
∂x l<br>g ¯ ij = ∂xk (23)<br>∂x ¯ i ∂x ¯ j gkl<br><!-- End of picture text -->

The conjugate metric tensor _g_<sup>_ij_</sup> (where _g_<sup>_ik_</sup> _gkj_ = _δj_<sup>_i_)iscontravariantrank2.</sup> 

6 

GATE PHYSICS 

FOURIER ANALYSIS & TENSOR CALCULUS 

-  **Index Raising and Lowering:** The metric tensor acts as an operator that maps vectors between their contravariant and covariant representations: 



<!-- Start of picture text -->
Ai =  gijA j , A i =  g ij Aj, Tj i =  gjkT ik (24)<br><!-- End of picture text -->

### **3. Analytical Milestones** 

Let us step through two critical proofs that demonstrate tensor behavior: 

1. **Proof that the Inner Product of a Contravariant and Covariant Vector is a Scalar Invariant:** Let _S ≡ A_<sup>_i_</sup> _Bi_ . We want to show that _S_ is invariant under a coordinate transformation ( _S_<sup>¯</sup> = _S_ ): 

   - (a) Write the transformed components of _A_<sup>¯</sup><sup>_i_</sup> and _B_<sup>¯</sup> _i_ : 



<!-- Start of picture text -->
A ¯ i = ∂x ∂x ¯ ki Ak, B ¯ i = ∂ ∂x x ¯ il Bl (25)<br><!-- End of picture text -->

- (b) Formulate the inner product in the barred system: 



<!-- Start of picture text -->
S ¯ = A ¯ i B ¯ i = � ∂x∂x ¯ k i Ak �� ∂∂xx ¯ i l Bl � = ∂x ∂x ¯ ki ∂∂xx ¯ il AkBl (26)<br><!-- End of picture text -->

(c) Apply the chain rule of partial differentiation: 



<!-- Start of picture text -->
∂x ¯ i ∂x l<br>k (27)<br>∂x k ∂x ¯ i = ∂x ∂xkl =  δl<br><!-- End of picture text -->

where _δk_<sup>_l_isthemixedKroneckerdelta.</sup> 

(d) Substitute this back into the inner product expression: 



<!-- Start of picture text -->
S ¯ =  δk l AkBl =  AkBk =  S (28)<br><!-- End of picture text -->

This proves that the inner product is a coordinate-independent scalar invariant (a rank 0 tensor). 

2. **The Quotient Rule Proof:** If a set of components _B_ ( _i_ ) satisfies _A_<sup>_i_</sup> _B_ ( _i_ ) = _S_ (an invariant scalar) for _any_ arbitrary contravariant vector _A_<sup>_i_</sup> , we want to prove that _B_ ( _i_ ) must be a covariant vector _Bi_ : 

   - (a) Since _S_ is an invariant scalar, we have _S_<sup>¯</sup> = _S_ = _⇒ A_ ¯<sup>_i_</sup> _B_ ¯( _i_ ) = _A_<sup>_k_</sup> _B_ ( _k_ ). 

   - (b) Express _A_<sup>¯</sup><sup>_i_</sup> in terms of _A_<sup>_k_</sup> using the contravariant transformation law: 



<!-- Start of picture text -->
� ∂x∂x ¯ k i Ak � B ¯( i ) =  A k B ( k ) (29)<br><!-- End of picture text -->

(c) Rearranging the equation: 



<!-- Start of picture text -->
A k � ∂x∂x ¯ k i B ¯( i )  − B ( k ) � = 0 (30)<br><!-- End of picture text -->

7 

GATE PHYSICS 

FOURIER ANALYSIS & TENSOR CALCULUS 

- (d) Since this must hold for any _arbitrary_ vector _A_<sup>_k_</sup> , the bracketed term must vanish identically: 



<!-- Start of picture text -->
∂x ¯ i<br>∂x k B ¯( i ) =  B ( k ) (31)<br><!-- End of picture text -->



<!-- Start of picture text -->
(e) Multiply both sides by ∂ ∂x x ¯ mk and sum over k :<br>∂x k ∂x ¯ i<br>m B ¯( i ) = ∂xk (32)<br>∂x ¯ m ∂x k B ¯( i ) = ∂ ∂x x ¯ mk B ( k ) = ⇒ δi ∂x ¯ m B ( k )<br><!-- End of picture text -->



<!-- Start of picture text -->
B ¯( m ) = ∂ ∂x x ¯ mk B ( k ) (33)<br><!-- End of picture text -->

This matches the covariant transformation law, proving that _B_ ( _i_ ) _≡ Bi_ is a covariant tensor of rank 1. 

### **4. Problem-Solving Algorithm** 

#### **Writing Transformation Equations and Computing Metric Components** 

1. **Identify the Tensor Rank and Component Type:** Note the positions of the indices. Each upper index requires a Jacobian factor of the form _∂x_<sup>_<u>∂x</u>_¯,andeachlower</sup> index requires a factor of the form _∂_<sup>_<u>∂x</u>_</sup> _x_ ¯<sup>.</sup> 

2. **Construct the Jacobian Matrix of the Transformation:** Write the coordinate relationships (e.g., Cartesian to Spherical: _x_ = _r_ sin _θ_ cos _ϕ, y_ = _r_ sin _θ_ sin _ϕ, z_ = _r_ cos _θ_ ). Compute the partial derivatives to build the Jacobian matrix: 



<!-- Start of picture text -->
Jj i = ∂x ¯ i (34)<br>∂x j<br><!-- End of picture text -->

3. **Compute the Metric Tensor Elements (** _gij_ **):** If working in non-Cartesian coordinates, evaluate the line element _ds_<sup>2</sup> : 



<!-- Start of picture text -->
ds 2 = ( dx ) 2 + ( dy ) 2 + ( dz ) 2 −−−−−−→ transform g 11( dx ¯ 1 ) 2 +  g 22( dx ¯ 2 ) 2 +  g 33( dx ¯ 3 ) 2 (35)<br><!-- End of picture text -->

For orthogonal coordinate systems, the metric is diagonal ( _gij_ = 0 for _i̸_ = _j_ ). 

4. **Raise or Lower Indices:** To convert a contravariant vector to a covariant vector, multiply by the metric tensor: _Ai_ = _giiA_<sup>_i_</sup> (no sum over _i_ if diagonal). To convert back, multiply by the inverse metric: _A_<sup>_i_</sup> = (1 _/gii_ ) _Ai_ . 

8 

GATE PHYSICS 

FOURIER ANALYSIS & TENSOR CALCULUS 

### **5. Crucial Pitfalls** 

#### **Tensor Calculus Traps to Avoid** 

-  **Derivatives of Non-Cartesian Tensor Components:** Assuming that the partial derivative of a tensor component ( _∂A_<sup>_i_</sup> _/∂x_<sup>_j_</sup> ) is also a tensor. Because the transformation Jacobians depend on position, their derivatives are non-zero, making partial derivatives non-tensorial. You must use the **Covariant Derivative** ( _∇jA_<sup>_i_</sup> = _∂jA_<sup>_i_</sup> +Γ<sup>_i_</sup> _jk_<sup>_Ak_), which</sup> introduces Christoffel symbols Γ<sup>_i_</sup> _jk_<sup>tocorrectforcoordinatecurvature.</sup> 

-  **Cartesian Coordinate Complacency:** Assuming that covariant and contravariant components are always physically distinct. In flat, orthonormal Cartesian coordinates, the metric tensor is the Kronecker delta ( _gij_ = _δij_ ). Consequently, _Ai_ = _δijA_<sup>_j_</sup> = _A_<sup>_i_</sup> , making covariant and contravariant components identical. The distinction only becomes important in curvilinear coordinates (cylindrical, spherical) or curved spacetime. 

-  **Incorrect Summation Coordinates:** Violating the Einstein summation convention by attempting to sum over two indices that are both in the upper position or both in the lower position (e.g., _A_<sup>_i_</sup> _B_<sup>_i_</sup> ). Summation must strictly occur between one upper and one lower index (e.g., _A_<sup>_i_</sup> _Bi_ = _gijA_<sup>_i_</sup> _B_<sup>_j_</sup> ). 

### **6. Standard Applications in Physics** 

-  **Special Relativity (Minkowski Spacetime):** Spacetime coordinates are represented as a contravariant four-vector _x_<sup>_µ_</sup> = ( _x_<sup>0</sup> _, x_<sup>1</sup> _, x_<sup>2</sup> _, x_<sup>3</sup> ) = ( _ct, x, y, z_ ). The flat-space metric tensor is the Minkowski metric: 



<!-- Start of picture text -->
ηµν = diag(1 , − 1 , − 1 , − 1) (or diag( − 1 ,  1 ,  1 ,  1)) (36)<br><!-- End of picture text -->

The covariant four-vector is _xµ_ = _ηµνx_<sup>_ν_</sup> = ( _ct, −x, −y, −z_ ). The invariant spacetime interval is the inner product: _ds_<sup>2</sup> = _x_<sup>_µ_</sup> _xµ_ = _c_<sup>2</sup> _dt_<sup>2</sup> _− d_ **r**<sup>2</sup> . 

-  **The Electromagnetic Field Tensor (** _F_<sup>_µν_</sup> **):** Combines the electric field **E** and magnetic field **B** into a single, antisymmetric contravariant rank-2 tensor in Minkowski spacetime: 



<!-- Start of picture text -->
F µν =  EExy 0 /c/c −EB 0 xz/c −−E 0 By/cz −−EBBzy/cx  (37)<br> Ez/c −By Bx 0 <br><!-- End of picture text -->

The covariant Maxwell equations can then be written compactly as _∂µF_<sup>_µν_</sup> = _µ_ 0 _J_<sup>_ν_</sup> and _∂µFαβ_ + _∂βFµα_ + _∂αFβµ_ = 0, demonstrating coordinate covariance. 

9 

GATE PHYSICS 

FOURIER ANALYSIS & TENSOR CALCULUS 

## **References** 

1. Arfken, George B., and Hans J. Weber. _Mathematical Methods for Physicists_ . Academic Press, 2005. 

2. Kreyszig, Erwin. _Advanced Engineering Mathematics_ . John Wiley & Sons, 2011. 

3. Rana, N. C., and P. S. Joag. _Classical Mechanics_ . Tata McGraw-Hill, 1991. 

10 

