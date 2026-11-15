<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: qm-part1-lect.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Statistical Mechanics of Interacting Systems 

# **Perturbation and Variational Methods** 

Single-file LaTeX transcription 

August 24, 2026 

# **Contents** 

|**1**<br>**Per**|**turbation Theory for Interacting Systems**|**2**|
|---|---|---|
|1.1|The basic statistical problem<br>. . . . . . . . . . . . . . . . . . . . . . . . . . <br><sup>ˆˆ</sup>|. . .<br>2|
||1.1.1<br>For the case [_H_0_,_ _H_<sup>_′_</sup><br>1<sup>] = 0</sup><br>. . . . . . . . . . . . . . . . . . . . . . . . <br><sup>ˆˆ</sup>|. . .<br>2|
||1.1.2<br>For the case [_H_0_,_ <br>_H_<sup>_′_</sup>1]_̸_= 0 . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>3|
|1.2|Choice of reference system . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>4|
|**2**<br>**Var**|**iational Approximation**|**6**|
|2.1|Why a variational method is needed<br>. . . . . . . . . . . . . . . . . . . . . .|. . .<br>6|
|2.2|Bogoliubov inequality from the coupling curve. . . . . . . . . . . . . . . . .|. . .<br>6|
|2.3|The variational prescription . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>7|
|2.4|Example: harmonic trial approximation for an anharmonic oscillator . . . .|. . .<br>8|
|2.5|Strengths and limitations<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>8|
|**Conclu**|**ding remarks**|**10**|



1 

## **Chapter 1** 

# **Perturbation Theory for Interacting Systems** 

#### **Objectives** 

This chapter develops perturbation theory for the free energy and partition function of an interacting statistical-mechanical system. The formalism is based on a reference ensemble whose averages are known. The central point is that the perturbing part of the Hamiltonian enters through an average Boltzmann factor, while the logarithm of this average generates cumulants. The same formulation also leads naturally to the variational bound discussed in the next chapter. 

## **1.1 The basic statistical problem** 

Perturbation theory is particularly useful when the Hamiltonian of a system can be written as a sum of two terms: 



<!-- Start of picture text -->
H ˆ = H ˆ0 + H ˆ1 , (1.1)<br><!-- End of picture text -->

where the canonical partition function corresponding to the part _H_<sup>ˆ</sup> 0 can be exactly evaluated, and _H_<sup>ˆ</sup> 1 introduces small corrections to that. One has to find out the partition function for the system with whole Hamiltonian, provided the correction term _H_<sup>ˆ</sup> 1 _≡ λH_<sup>ˆ</sup> 1<sup>_′_ismuchsmall</sup> compared to _H_<sup>ˆ</sup> 0 (i.e. _λ ≪_ 1, when _H_<sup>ˆ</sup> 0 _≃ H_<sup>ˆ</sup> 1<sup>_′_).</sup> 

**1.1.1 For the case** [ _H_<sup>ˆ</sup> 0 _, H_<sup>ˆ</sup> 1<sup>_′_] = 0</sup> 

Perturbation expansion finds the partition function as a power series in this parameter _λ_ . In other words, we will write 



<!-- Start of picture text -->
ln  Z = ln  Z 0 +  λ � d  ln dλ Z � λ =0 + 2 1 λ 2 � d 2 dλ ln 2  Z � λ =0 +  · · · (1.2)<br><!-- End of picture text -->

The first term on the right hand side of this equation contains the partition function evaluated with _λ_ = 0, i.e., the partition function for the Hamiltonian _H_ 0. As already mentioned, this part can be evaluated exactly. 

Let us now look at the next term. The definition of the partition function is 



<!-- Start of picture text -->
Z = Tr( e −β H ˆ ) = Tr( e−β ( H 0+ λH 1 ′ ) ) . (1.3)<br><!-- End of picture text -->

This is equivalent to a classical system where _e_<sup>_A_+</sup><sup>_B_</sup> = _e_<sup>_A_</sup> _e_<sup>_B_</sup> . For a purely classical system Tr stands for the integration over all phase-space, and a division by an appropriate power of 2 _π_ ℏ to make the resulting integral dimensionless. 

2 

For this case it can be shown that, 



<!-- Start of picture text -->
=  −β⟨H ˆ 1 ′ ⟩ 0 (1.4)<br>� d  ln dλ Z � λ =0<br><!-- End of picture text -->

and 



<!-- Start of picture text -->
d 2 ln  Z<br>=  β 2 ( ⟨H ˆ ′ 2 1 ⟩ 0 −⟨H ˆ 1 ′ ⟩ 2 0 ) . (1.5)<br>dλ 2<br>� �<br><!-- End of picture text -->

Here the suffix ‘0’ stands for the average over the canonical ensemble based on _H_<sup>ˆ</sup> 0 only. 

In this fashion the higher order terms may be expressed in terms of different higher order moments of _H_<sup>ˆ</sup> 0<sup>_′_basedontheensemblefor</sup><sup>_H_ˆ0only.(Seethereference1,forthedetailed</sup> calculations.) 

Consider a system whose energy in a microstate _r_ can be separated into a soluble reference part and a perturbing part: 



<!-- Start of picture text -->
Er =  Er (0) +  λEr (1) . (1.6)<br><!-- End of picture text -->

Here _Er_<sup>(0)</sup> is the energy eigenvalue of the unperturbed Hamiltonian, _Er_<sup>(1)</sup> is the same for perturbing Hamiltonian scaled by _λ_ , and _λ_ is a dimensionless parameter that keeps track of the order of the perturbation. 

The canonical partition function of the full system is 



<!-- Start of picture text -->
Z ( λ ) = � exp[ −β ( Er (0) +  λEr (1))] , (1.7)<br>r<br><!-- End of picture text -->

where _β_ = 1 _/_ ( _k_ B _T_ ). The unperturbed partition function and the corresponding unperturbed average are defined as 



<!-- Start of picture text -->
Z 0 = � exp( −βEr (0)) , ⟨A⟩ 0 = 1 � Ar  exp( −βEr (0)) . (1.8)<br>r Z 0 r<br><!-- End of picture text -->

Using these definitions, the full partition function may be written exactly as 



<!-- Start of picture text -->
Z ( λ ) =  Z 0 exp( −βλE (1) ) (1.9)<br>� �0 .<br><!-- End of picture text -->

This equation is the starting point of canonical perturbation theory. It says that the full partition function is obtained by multiplying the known partition function _Z_ 0 by an average correction factor calculated in the known ensemble. 

The Helmholtz free energy is 



<!-- Start of picture text -->
F ( λ ) =  −k B T ln  Z ( λ ) , (1.10)<br><!-- End of picture text -->

so that 



<!-- Start of picture text -->
F ( λ )  − F 0 =  −k B T ln exp( −βλH ˆ ′ 1) (1.11)<br>� �0 .<br><!-- End of picture text -->

The important point is that the free-energy correction is not simply the average perturbing energy. It is the logarithm of an average exponential. 

### **1.1.2 For the case** [ _H_<sup>ˆ</sup> 0 _, H_<sup>ˆ</sup><sup>_′_</sup> 1] _̸_ = 0 

Any perturbation theory, classical or quantum, has to start from a decomposition of the Hamiltonian of the form shown in Eq.(1.1). Also the idea is always the same: to perform a power series expansion in the ‘small’ parameter _λ_ . 

The reason behind discussing this separately is that quantum mechanics deals with operators which do not always commute (henceforth for the sake convenience of typing we drop caret symbol with the operator unless there is any scope of confusion). Of course not all pairs of 

3 

operators have non-vanishing commutators. If _H_<sup>ˆ</sup> 0 and _H_<sup>ˆ</sup> 1 happen to commute, we can use all the results of previous subsection. But if 



<!-- Start of picture text -->
[ H 0 , H 1] ̸  = 0 , (1.12)<br><!-- End of picture text -->

we have to be careful about their order while taking the derivatives with respect to _λ_ . This is what we will undertake in this subsection. 

Let us consider the operator, 



<!-- Start of picture text -->
U ( β )  ≡ e βH 0 e −β ( H 0+ λH 1 ′ ) .<br><!-- End of picture text -->

As _H_ 0 and _H_ 1<sup>_′_donotcommute,</sup> 



<!-- Start of picture text -->
e −β ( H 0+ λH 1 ′ ) ̸ =  e −βH 0 e −βλH 1 ′<br><!-- End of picture text -->

so that _U_ ( _β_ ) _̸_ = _e_<sup>_−βλH_</sup> 1<sup>_′_</sup> . However, in the special case when _β_ = 0, we obtain 



<!-- Start of picture text -->
U (0) = 1 . (1.13)<br><!-- End of picture text -->

Now (see reference 1, for details), 



<!-- Start of picture text -->
dU<br>dβ =  −λeβH 0 H 1 ′ e−βH 0 U.<br><!-- End of picture text -->

We can integrate this equation to obtain 



<!-- Start of picture text -->
U ( β ) = 1  − λ dβ 1 e β 1 H 0 H 1 ′ e−β 1 H 0 U ( β 1) , (1.14)<br>�0 β<br><!-- End of picture text -->

where the constant of integration has been fixed by _U_ (0) in equation (1.13). We can write a general term in the solution in the form, 



<!-- Start of picture text -->
Ur ( β ) = 1  − λ dβ 1 e β 1 H 0 H 1 ′ e−β 1 H 0 Ur− 1( β 1) . (1.15)<br>�0 β<br><!-- End of picture text -->

We may now use _U_ to obtain the canonical partition function as, 



<!-- Start of picture text -->
Z ≡ Tr[ e −βH ] = Tr[ e −βH 0 U ] =  Z 0 +  λZ 1 +  λ 2 Z 2 +  · · · . (1.16)<br><!-- End of picture text -->

Whence one gets (see reference 1 for details), 



<!-- Start of picture text -->
ln  Z = ln  Z 0  − βλ⟨H 1 ′ ⟩ 0 + 1 β dβ ′ ⟨e β′H 0 H 1 ′ e−β′H 0 H 1 ′ ⟩ 0 − β 2 ⟨H 1 ′ ⟩ 2 0 +  O ( λ 3 )<br>2 λ 2 �0 β<br>� �<br>1<br>= ln  Z 0  − β⟨H 1 ⟩ 0 + 1 dβ ′ ⟨e β′H 0 H 1 e −β′H 0 H 1 ⟩ 0  −⟨H 1 ⟩ 2 0 +  · · · (1.17)<br>2 β 2 � β �0 β �<br><!-- End of picture text -->

#### **Physical idea** 

In mechanics, perturbation theory often means expanding the energy levels or the equations of motion. In statistical mechanics, the object being expanded is the Boltzmann weight. Since the free energy is proportional to the logarithm of the partition function, its expansion contains connected fluctuation terms, rather than ordinary moments alone. 

## **1.2 Choice of reference system** 

The formal expressions above do not by themselves guarantee a useful approximation. A reference system must be chosen so that it is both solvable and physically close to the actual system. A hard-core repulsion, for example, is not a good perturbation of an ideal gas because the ideal-gas ensemble gives nonzero probability to overlapping configurations that the true system strongly suppresses. In a dense fluid, it is usually better to incorporate the repulsive core into the reference Hamiltonian and treat the smoother attractive tail as a perturbation. 

4 



<!-- Start of picture text -->
full Hamiltonian H<br>dominant physics small correction<br>solvable H 0 residual H 1<br>F =  F 0  − k B T ln  ⟨ exp( −βH 1) ⟩ 0<br><!-- End of picture text -->

A good split makes the ensemble average calculable and well behaved. 

Figure 1.1: A useful perturbation expansion begins with a physically sensible separation of the Hamiltonian into a reference part and a residual part. 

#### **Worked example: Concavity of the free energy** 



<!-- Start of picture text -->
For H ( λ ) =  H 0 +  λH 1, show that F ( λ ) is concave. The first derivative is<br><!-- End of picture text -->



<!-- Start of picture text -->
∂F<br>∂λ =  ⟨H 1 ⟩λ . (1.18)<br><!-- End of picture text -->

Differentiating an ensemble average with respect to _λ_ gives 



<!-- Start of picture text -->
∂<br>∂λ ⟨H 1 ⟩λ =  −β �� H 1 2 � λ −⟨H 1 ⟩ λ 2 � . (1.19)<br><!-- End of picture text -->

Since the variance is non-negative, 



<!-- Start of picture text -->
∂ 2 F<br>∂λ 2 ≤ 0 . (1.20)<br><!-- End of picture text -->

Thus the curve lies below any tangent line. This result is the bridge to the variational inequality. 

#### **Summary** 

With _H_ = _H_ 0 + _λH_ 1, the exact relation _Z_ = _Z_ 0 _⟨_ exp( _−βλH_ 1) _⟩_ 0 expresses the full partition function in terms of an unperturbed ensemble average. The first-order correction to the free energy is _⟨H_ 1 _⟩_ 0, while the second-order correction is _−β/_ 2 times the variance of _H_ 1. 

#### **Suggested problems** 

1. Starting from Eq. (1.9), derive the first-order correction _F_<sup>(1)</sup> = _⟨H_ 1 _⟩_ 0. 

2. Derive Eq. (1.17) by expanding both the exponential and the logarithm to second order. 

3. Explain why a hard-core potential is usually not a good perturbation of an ideal gas. 

5 

## **Chapter 2** 

# **Variational Approximation** 

#### **Objectives** 

This chapter introduces the variational approach to interacting systems. The Gibbs– Bogoliubov inequality is derived from the concavity of the coupling-parameter free energy and also from Jensen’s inequality. The method is then interpreted as minimisation over a restricted family of trial Hamiltonians or trial probability distributions. 

## **2.1 Why a variational method is needed** 

Perturbation theory is powerful when the difference between the real Hamiltonian and a soluble reference Hamiltonian is small. Many interacting systems do not possess such a small parameter. A variational approximation avoids this difficulty by introducing a family of tractable trial Hamiltonians, 



<!-- Start of picture text -->
H 0 =  H 0( α 1 , α 2 , . . . ) , (2.1)<br><!-- End of picture text -->

where the _αi_ are adjustable parameters. For each choice of the parameters, one obtains an upper bound on the exact free energy. The best approximation inside the chosen family is obtained by minimising that bound. 

The method is especially useful when the qualitative physics is known but the correlations are difficult to calculate exactly. For instance, an interacting spin system may be approximated by independent spins placed in an effective field. The effective field is then fixed by a variational condition, not by arbitrary choice. 

## **2.2 Bogoliubov inequality from the coupling curve** 

Let 



<!-- Start of picture text -->
H ( λ ) =  H 0 +  λ ( H − H 0) , 0  ≤ λ ≤ 1 , (2.2)<br><!-- End of picture text -->

so that _H_ (0) = _H_ 0 and _H_ (1) = _H_ . Define 



<!-- Start of picture text -->
∆ H =  H − H 0 . (2.3)<br><!-- End of picture text -->

From the coupling-parameter result, 



<!-- Start of picture text -->
∂F ∂ 2 F<br>∂λ =  ⟨ ∆ H⟩λ , ∂λ 2 =  −β ��(∆ H ) 2� λ −⟨ ∆ H⟩ λ 2 � ≤ 0 . (2.4)<br><!-- End of picture text -->

Thus _F_ ( _λ_ ) is concave. A concave curve lies below its tangent. The tangent at _λ_ = 0 gives 



<!-- Start of picture text -->
F (1)  ≤ F (0) + ∂F . (2.5)<br>∂λ ���� λ =0<br><!-- End of picture text -->

6 

Substitution of _F_ (1) = _F_ , _F_ (0) = _F_ 0, and _∂F/∂λ|_ 0 = _⟨H − H_ 0 _⟩_ 0 yields 



<!-- Start of picture text -->
F ≤ F 0 +  ⟨H − H 0 ⟩ 0  . (2.6)<br><!-- End of picture text -->

This is the Gibbs–Bogoliubov inequality. 



<!-- Start of picture text -->
F ( λ )<br>F 0<br>F 0 +  ⟨H − H 0 ⟩ 0<br>F<br>λ<br>1<br><!-- End of picture text -->

Figure 2.1: The Gibbs–Bogoliubov inequality follows from the concavity of the coupling-parameter free energy. The tangent at the reference system gives an upper bound on the exact free energy. 

## **2.3 The variational prescription** 

Suppose the trial Hamiltonian depends on parameters _α_ 1 _, . . . , αn_ . For every choice of these parameters, the Gibbs–Bogoliubov inequality gives 



<!-- Start of picture text -->
F ≤ Φ( α 1 , . . . , αn ) , Φ =  F 0 +  ⟨H − H 0 ⟩ 0  . (2.7)<br><!-- End of picture text -->

The best approximation within the chosen family is found by minimising Φ: 



<!-- Start of picture text -->
∂ Φ<br>= 0 , i  = 1 ,  2 , . . . , n. (2.8)<br>∂αi<br><!-- End of picture text -->

One must then check that the stationary point is actually the relevant minimum. If several local minima exist, the lowest value of Φ gives the best variational upper bound. 



<!-- Start of picture text -->
Φ( α )<br>minimum bound<br>exact F<br>trial parameter α<br><!-- End of picture text -->

Figure 2.2: A variational calculation converts a statistical-mechanical problem into an optimisation problem. The minimum of Φ is the best upper bound within the chosen trial family. 

The inequality is rigorous, but the approximation depends on the chosen trial family. A very restrictive family may give a well-defined optimum while still missing important physical correlations or symmetry-breaking patterns. 

7 

#### **Physical idea** 

A variational approximation chooses the best member of a restricted family of probability distributions. Its strength is that it is non-perturbative and thermodynamically controlled. Its weakness is that it cannot represent physical structures absent from the trial family. 

## **2.4 Example: harmonic trial approximation for an anharmonic oscillator** 

Consider the classical one-dimensional Hamiltonian 



<!-- Start of picture text -->
H = p 2 b >  0 . (2.9)<br>2 m + a 2 x 2 + 4 b x 4 ,<br><!-- End of picture text -->

Choose a harmonic trial Hamiltonian 



<!-- Start of picture text -->
H 0 = 2 p m 2 + k 2 x 2 , k >  0 . (2.10)<br><!-- End of picture text -->

The trial averages are 



<!-- Start of picture text -->
. (2.11)<br>� x 2� 0 = k B k T , � x 4� 0 = 3 � k B kT �2<br><!-- End of picture text -->

The variational function is 



<!-- Start of picture text -->
k B T<br>Φ( k ) =  F 0( k ) + a − k + 3 b . (2.12)<br>2 k 4 � k B kT �2<br><!-- End of picture text -->

Using 



<!-- Start of picture text -->
∂F 0<br>(2.13)<br>∂k = 2 1 � x 2� 0 = k 2 B k T ,<br><!-- End of picture text -->

the stationarity condition gives 



<!-- Start of picture text -->
0 = ∂ Φ − 3 b ( k B T )2 . (2.14)<br>∂k = k 2 B k T − ak 2 k B2 T 2 k 3<br><!-- End of picture text -->

Hence 



<!-- Start of picture text -->
k 2 − ak − 3 bk B T = 0 , (2.15)<br><!-- End of picture text -->

and the physical solution is 



<!-- Start of picture text -->
� a 2 + 12 bk B T<br>k opt = a  + . (2.16)<br>2<br><!-- End of picture text -->

The quartic term increases the effective stiffness. At higher temperature the oscillator explores larger displacements and the anharmonic part becomes more important. 

## **2.5 Strengths and limitations** 

The variational method is non-perturbative in the sense that it does not require _H − H_ 0 to be small. It is also thermodynamically controlled because it provides an upper bound on the exact free energy. However, its quality is limited by the trial Hamiltonian. A single-site trial Hamiltonian neglects pair correlations. A translationally invariant trial Hamiltonian cannot describe crystalline order unless the possibility of symmetry breaking is built into the trial family. A scalar trial order parameter cannot represent an intrinsically vector or tensor order parameter. 

Increasing the number of variational parameters may improve the numerical bound, but it does not automatically improve physical understanding. A useful variational approximation should balance physical insight, mathematical tractability and sufficient flexibility. 

8 

#### **Worked example: Shifted oscillator and broken symmetry** 



<!-- Start of picture text -->
Consider<br>H = 2 p m 2 + 4 b ( x 2  − a 2)2 , b >  0 , (2.17)<br><!-- End of picture text -->

which has two equivalent minima at _x_ = _±a_ . A symmetric harmonic trial Hamiltonian centred at the origin cannot represent localisation in either well. A more flexible trial Hamiltonian is 



<!-- Start of picture text -->
H 0 = 2 p m 2 + k 2 ( x − x 0)2 . (2.18)<br><!-- End of picture text -->

The variational parameters are _k_ and _x_ 0. If the optimum has _x_ 0 = 0, the trial state preserves the symmetry _x →−x_ . If two equivalent optima with _x_ 0 _̸_ = 0 appear, the variational solution displays broken symmetry. This anticipates the Landau idea that symmetry breaking can occur only if the relevant order parameter is allowed in the free energy. 

#### **Summary** 

The Bogoliubov inequality 



<!-- Start of picture text -->
F ≤ F 0 +  ⟨H − H 0 ⟩ 0<br><!-- End of picture text -->

follows either from the concavity of the coupling-parameter free energy or from Jensen’s inequality. A trial Hamiltonian with adjustable parameters gives an upper-bound function Φ, and the best variational approximation within that family is obtained by minimising Φ. The free-energy functional interpretation shows that the variational method is an optimisation over probability distributions. Mean-field theory is a central example of this approach. 

#### **Suggested problems** 

1. Starting from _∂_<sup>2</sup> _F/∂λ_<sup>2</sup> _≤_ 0, derive the Bogoliubov inequality as a tangent-line bound. 

2. Complete the minimisation of Eq. (2.12) and verify Eq. (2.16). 

9 

# **Concluding remarks** 

Perturbation theory and variational theory are complementary approximation strategies. Perturbation theory is systematic when a small residual interaction is available; its higher-order corrections reveal the role of fluctuations through cumulants. Variational theory is more flexible when no small parameter exists; it replaces expansion by optimisation and provides a controlled upper bound to the free energy. Together these two methods form a foundation for mean-field theory, Landau theory, and many approximate descriptions of interacting many-particle systems. 

10 

# **References** 

1. "An Introductory Course of Statistical Mechanics" – Palash B. Pal. 

11 

