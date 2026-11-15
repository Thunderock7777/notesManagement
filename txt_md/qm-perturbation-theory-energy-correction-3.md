<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-perturbation-theory-energy-correction-3.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Here is a master summary chart and detailed breakdown comparing **Non-Degenerate Time-Independent** , **Degenerate Time-Independent** , and **Time-Dependent Perturbation Theory** for quantum mechanics and GATE Physics preparation. 

## **Master Summary Comparison Chart** 

|Feature / Aspect|**Non-Degenerate**<br>**Time-Independent**<br>**PT**|**Degenerate**<br>**Time-Independent**<br>**PT**|**Time-Dependent**<br>**PT**|
|---|---|---|---|
|**Hamiltonian Setup**|ˆ_H_ = ˆ_H_0+_λ_ˆ_H_<sup>_′_ </sup>(ˆ_H_<sup>_′_ </sup>is<br>static and small)|ˆ_H_ = ˆ_H_0+_λ_ˆ_H_<sup>_′_ </sup>(ˆ_H_0<br>has _g_-fold<br>degeneracy)|ˆ_H_(_t_) = ˆ_H_0+ ˆ_V_(_t_)<br>( <sup>ˆ</sup>_V_(_t_) depends<br>explicitly on time)|
|**Primary Goal**|Calculate static<br>energy shifts<br>(_E_<sup>(1)</sup><br>_n _<sup>_, E_(2)</sup><br>_n_ <sup>) and</sup><br>perturbed state _|n⟩_|Lift _g_-fold degeneracy<br>& find “good”<br>unperturbed states<br>_|ϕ_<sup>(0)</sup>_⟩_|Calculate transition<br>probability _Pi→f_(_t_)<br>and transition rate<br>_Wi→f_|
|**Validity Condition**|_∥⟨k_<sup>(0)</sup>_∥_<sup>ˆ</sup>_H_<sup>_′_</sup>_∥n_<sup>(0)</sup>_⟩∥≪_<br>_∥E_<sup>(0)</sup><br>_n_<br>_−E_<sup>(0)</sup><br>_k _<sup>_∥_for all</sup><br>_k̸_ =_n_|Degenerate subspace<br>_D_ isolated from<br>distant energy levels<br>_E_<sup>(0)</sup><br>_k_|Weak perturbation<br>(_∥cf_(_t_)_∥≪_1) over<br>finite time intervals|
|**Zeroth-Order**<br>**State**|_|n_<sup>(0)</sup>_⟩_(Unique<br>unperturbed state)|_|ϕ_<sup>(0)</sup><br>_k _<sup>_⟩_= �</sup><sup>_g_</sup><br>_i_=1 <sup>_ai|i_(0)</sup><sup>_⟩_</sup><br>(Diagonalizing basis)|_|i⟩_(System initially<br>in state _|i⟩_at _t_= 0)|
|1<sup>**st**</sup>**-Order Energy**<br>**Correction (**_E_<sup>(1)</sup>**)**|_E_<sup>(1)</sup><br>_n_<br>=_⟨n_<sup>(0)</sup>_∥_<sup>ˆ</sup>_H_<sup>_′_</sup>_∥n_<sup>(0)</sup>_⟩_|Roots _E_<sup>(1)</sup><br>_k_<br>of _g × g_<br>Secular Eq.:<br>det<br>�<br>_Wij −E_<sup>(1)</sup>_δij_<br>�<br>=<br>0|**N/A** (Energy is not<br>conserved during<br>non-stationary time<br>evolution)|
|2<sup>**nd**</sup>**-Order Energy**<br>**Correction (**_E_<sup>(2)</sup>**)**|_E_<sup>(2)</sup><br>_n_<br>=<br>�<br>_k̸_=_n_<br>_∥⟨k_<sup>(0)</sup>_∥_<sup>ˆ</sup>_H_<sup>_′_</sup>_∥n_<sup>(0)</sup>_⟩∥_<sup>2</sup><br>_E_<sup>(0)</sup><br>_n _<sup>_−E_(0)</sup><br>_k_|_E_<sup>(2)</sup><br>_k_<br>=<br>�<br>_m_/_∈D_<br>_∥⟨m_<sup>(0)</sup>_∥_<sup>ˆ</sup>_H_<sup>_′_</sup>_∥ϕ_<sup>(0)</sup><br>_k _<sup>_⟩∥_2</sup><br>_E_<sup>(0)</sup><br>_D _<sup>_−E_(0)</sup><br>_m_|Energy shift ∆_i_ =<br>_Vii_+<sup>�</sup><br>_m̸_=_i_<br>_∥Vmi∥_<sup>2</sup><br>_Ei−Em_+_i_¯_hη_|
|1<sup>**st**</sup>**-Order State /**|_∥n_<sup>(1)</sup>_⟩_=|<br>Includes mixing from|_c_<sup>(1)</sup><br>_f_ <sup>(</sup><sup>_t_) =</sup>|
|**Amplitude**<br>**Correction**|�<br>_k̸_=_n_<br>_⟨k_<sup>(0)</sup>_∥_<sup>ˆ</sup>_H_<sup>_′_</sup>_∥n_<sup>(0)</sup>_⟩_<br>_E_<sup>(0)</sup><br>_n _<sup>_−E_(0)</sup><br>_k_<br>_∥k_<sup>(0)</sup>|_⟩_<br>non-degenerate states<br>_m_ /_∈D_|<br>_−_<sup>_i_</sup><br>¯_h_<br>�_t_<br>0 <sup>_eiωfit′Vfi_(</sup><sup>_t′_)</sup><sup>_dt′_</sup>|
|**Total Energy /**<br>**Transition Formula**|_En ≈_<br>_E_<sup>(0)</sup><br>_n_<br>+_E_<sup>(1)</sup><br>_n_<br>+_E_<sup>(2)</sup><br>_n_|_Ek ≈_<br>_E_<sup>(0)</sup><br>_D_ <sup>+</sup><sup>_E_(1)</sup><br>_k_<br>+_E_<sup>(2)</sup><br>_k_|**Fermi’s Golden**<br>**Rule**: _Wi→f_ =<br>2_π_<br>¯_h_ <sup>_∥Vfi∥_2</sup><sup>_ρ_(</sup><sup>_Ef_)</sup>|



Notes 

2 

||**Non-Degenerate**<br>**Time-Independent**|**Degenerate**<br>**Time-Independent**|**Time-Dependent**|
|---|---|---|---|
|Feature / Aspect|**PT**|**PT**|**PT**|
|**Classic GATE**|_•_ Anharmonic<br>|_•_ Linear Stark Effect|_•_ Absorption &|
|**Applications**|Oscillator (_βx_<sup>4</sup>)|in _n_= 2 Hydrogen<br>f|Stimulated Emission|
||_•_ Quadratic Stark<br>f|_•_ Zeeman Effect &|_•_ Harmonic &|
||Effect in 1_s_ Hydrogen|Fine Structure|Sudden/Adiabatic<br>Pulses|



**1. Non-Degenerate Time-Independent Perturbation Theory** 

- Used when the unperturbed state _|n_<sup>(0)</sup> _⟩_ is non-degenerate ( _En_<sup>(0)</sup> = _Ek_<sup>(0)</sup> for all _k̸_ = _n_ ). 

   - **Power Series Expansions:** 

      - _En_ = _En_<sup>(0)+</sup><sup>_λE_</sup> _n_<sup>(1)+</sup><sup>_λ_2</sup><sup>_E_</sup> _n_<sup>(2)+</sup><sup>_. . ._</sup> and _|n⟩_ = _|n_<sup>(0)</sup> _⟩_ + _λ|n_<sup>(1)</sup> _⟩_ + _λ_<sup>2</sup> _|n_<sup>(2)</sup> _⟩_ + _. . ._ 

   - **First-Order Energy Shift (** _En_<sup>(1)</sup><sup>**):**</sup> 



<!-- Start of picture text -->
En (1) =  ⟨n (0) |H ˆ ′ |n (0) ⟩ (Expectation value of perturbation)<br><!-- End of picture text -->

- **First-Order Wave Function Correction (** _|n_<sup>(1)</sup> _⟩_ **):** 



<!-- Start of picture text -->
⟨k (0) |H ˆ ′ |n (0) ⟩<br>|n (1) ⟩ = � |k (0) ⟩<br>k̸ = n En (0) − E k (0)<br><!-- End of picture text -->

- **Second-Order Energy Shift (** _En_<sup>(2)</sup><sup>**):**</sup> 



<!-- Start of picture text -->
|⟨k (0) |H ˆ ′ |n (0) ⟩| 2<br>E (2) =<br>n �<br>k̸ = n En (0) − E k (0)<br><!-- End of picture text -->

   - **Critical Theorem:** For the **ground state (** _n_ = 0 **)** , _E_ 0<sup>(0)</sup> _< Ek_<sup>(0)</sup> for all _k̸_ = 0. Therefore, _E_ 0<sup>(2)</sup> _≤_ 0 **is strictly non-positive** (ground state energy is always lowered at 2nd order). 

**2. Degenerate Time-Independent Perturbation Theory** 

- Used when _g_ unperturbed states _{|i_<sup>(0)</sup> _⟩}_<sup>_g_</sup> _i_ =1<sup>share the sameunperturbed energylevel</sup><sup>_E_</sup> _D_<sup>(0).</sup> 

   - **The** _g × g_ **Secular Matrix Equation:** To find the first-order energy corrections _E_<sup>(1)</sup> , solve the characteristic determinant inside the degenerate subspace _D_ : 

det � _Wij − E_<sup>(1)</sup> _δij_ � = 0 where _Wij_ = _⟨i_<sup>(0)</sup> _|H_<sup>ˆ</sup><sup>_′_</sup> _|j_<sup>(0)</sup> _⟩_ 

Notes 

3 



<!-- Start of picture text -->
W 11  − E (1) W 12 . . . W 1 g<br>W 21 W 22  − E (1) . . . W 2 g<br>= 0<br>... ... ... ...<br>. . .<br>��������� Wg 1 Wg 2 Wgg − E (1) ���������<br><!-- End of picture text -->

- **“Good” Zeroth-Order Wave Functions:** For each eigenvalue _Ek_<sup>(1), solving (</sup><sup>_W −_</sup> _Ek_<sup>(1)</sup><sup>_I_)</sup><sup>**a**=0yieldsthenormalizedcoefficients</sup><sup>**a**=(</sup><sup>_a_1</sup><sup>_, . . . , ag_)</sup><sup>_T_,givingthecorrect</sup> unperturbed state: 



<!-- Start of picture text -->
g<br>|ϕ (0) k ⟩ = � ai|i (0) ⟩<br>i =1<br><!-- End of picture text -->

- **Symmetry Shortcut:** If the perturbation matrix _Wij_ is already diagonal in your chosen basis (or if a state has a unique symmetry eigenvalue), you do **not** need to solve the secular determinant—its first-order shift is simply its diagonal matrix element _Ei_<sup>(1)</sup> = _Wii_ . 

## **3. Time-Dependent Perturbation Theory** 

Used when the Hamiltonian contains an explicit time dependence _V_<sup>ˆ</sup> ( _t_ ) turned on at _t_ = 0, causing transitions between stationary states. 

- **First-Order Transition Amplitude (** _c_<sup>(1)</sup> _f_<sup>(</sup><sup>_t_)</sup><sup>**):**Ifthesystemisinitiallyinstate</sup> _|i⟩_ at _t_ = 0, the probability amplitude to find it in state _|f ⟩_ at time _t_ is: 



<!-- Start of picture text -->
c (1) f ( t ) =  − i ⟨f |V ˆ  ( t ′ ) |i⟩e iωfit′ dt ′ where ωfi = Ef − Ei<br>h ¯ �0 t h ¯<br><!-- End of picture text -->

- **Transition Probability (** _Pi→f_ ( _t_ ) **):** 



<!-- Start of picture text -->
Pi→f ( t ) =  |c (1) f ( t ) | 2<br><!-- End of picture text -->

- **Constant Perturbation (** _V_<sup>ˆ</sup> ( _t_ ) = _V_<sup>ˆ</sup> 0 **):** 



<!-- Start of picture text -->
sin 2<br>Pi→f ( t ) = 4 |⟨f |  ˆ V 0 |i⟩| 2<br>h ¯ 2 ωfi 2 � ω 2 f it �<br><!-- End of picture text -->



<!-- Start of picture text -->
• Fermi’s Golden Rule (Constant Perturbation into Continuum): As  t →∞ ,<br>becomes:<br>the transition rate per unit time Wi→f = dP dt i→f<br>Wi→f = 2 π<br>h ¯ |⟨f |  ˆ V 0 |i⟩| 2 ρ ( Ef ) δ ( Ef − Ei )<br><!-- End of picture text -->

- **Harmonic Perturbation (** _V_<sup>ˆ</sup> ( _t_ ) = _Fe_<sup>ˆ</sup><sup>_−iωt_</sup> + _F_<sup>ˆ</sup><sup>_†_</sup> _e_<sup>_iωt_</sup> **):** 

   - **Absorption:** _Ef_ = _Ei_ + ¯ _hω_ = _⇒ Wi_<sup>abs</sup> _→f_<sup>=</sup><sup><u>2</u></sup> _h_ ¯<sup>_<u>π</u>|⟨f|_ˆ</sup><sup>_F †|i⟩|_2</sup><sup>_ρ_(</sup><sup>_Ef_)</sup> 

   - **– Stimulated Emission:** _Ef_ = _Ei − hω_ ¯ = _⇒ Wi_<sup>emi</sup> _→f_<sup>=</sup><sup><u>2</u></sup> _h_ ¯<sup>_<u>π</u>|⟨f|_ˆ</sup><sup>_F|i⟩|_2</sup><sup>_ρ_(</sup><sup>_Ef_)</sup> 

Notes 

4 

## **Key Exam Traps & Pitfalls for GATE** 

1. **Division-by-Zero Trap:** Never use non-degenerate formulas if _En_<sup>(0)</sup> = _Ek_<sup>(0)</sup> for offdiagonal matrix elements _⟨k_<sup>(0)</sup> _|H_<sup>ˆ</sup><sup>_′_</sup> _|n_<sup>(0)</sup> _⟩̸_ = 0—you must use degenerate perturbation theory. 

2. **Ground-State Sign Check:** If your calculated 2nd-order ground state energy correction _E_ 0<sup>(2)</sup> comes out positive, there is an algebraic sign error. 

3. **Parity Selection Rule:** If the perturbation operator _H_<sup>ˆ</sup><sup>_′_</sup> is odd under spatial parity ( _x, z, r_<sup>3</sup> ), all diagonal matrix elements _⟨n_<sup>(0)</sup> _|H_<sup>ˆ</sup><sup>_′_</sup> _|n_<sup>(0)</sup> _⟩_ for states of definite parity vanish identically, making _E_<sup>(1)</sup> = 0. 

**Would you like me to compile this into a printable PDF study guide or generate practice GATE numerical problems on Stark effect and Fermi’s Golden Rule?** 

