<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-bloch-wavefunction-and-theorem.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

To see how a constant spatial phase shift ∆ _ϕ_ = _ka_ turns a periodic wave pattern into a **propagating traveling wave** with a non-zero probability current, we can look at the math and physics step-by-step. 

## **1. The Time-Dependent Bloch Wavefunction** 

Including the time dependence _e_<sup>_−iωt_</sup> (where _E_ = _hω_ ¯ is the energy eigenvalue), the full time-dependent Bloch wavefunction in 1D is: 



<!-- Start of picture text -->
Ψ k ( x, t ) =  ψk ( x ) e −iωt =  uk ( x ) e i ( kx−ωt )<br><!-- End of picture text -->

- _uk_ ( _x_ ) is the local atomic modulation, which repeats identically in every unit cell ( _uk_ ( _x_ + _a_ ) = _uk_ ( _x_ )). 

- _e_<sup>_i_(</sup><sup>_kx−ωt_)</sup> is the underlying traveling wave envelope. 

## **2. Shift Across Adjacent Unit Cells** 

Evaluating the wavefunction one lattice constant _a_ further down the crystal ( _x → x_ + _a_ ) gives: 



<!-- Start of picture text -->
Ψ k ( x  +  a, t ) =  uk ( x  +  a ) e i ( k ( x + a ) −ωt )<br><!-- End of picture text -->

Because _uk_ ( _x_ + _a_ ) = _uk_ ( _x_ ), we factor out the phase shift: 



<!-- Start of picture text -->
Ψ k ( x  +  a, t ) = [ uk ( x ) e i ( kx−ωt )] · e ika = Ψ k ( x, t )  · e i ∆ ϕ<br><!-- End of picture text -->

where ∆ _ϕ_ = _ka_ is a pure phase shift. 

## **3. How a Constant Phase Shift Forces Wave Propagation** 

To see how this phase shift moves the wave through space, look at the **total phase** Φ( _x, t_ ) of the wave: 

Notes 

2 



<!-- Start of picture text -->
Φ( x, t ) =  kx − ωt  +  θu ( x )<br><!-- End of picture text -->

_(where θu_ ( _x_ ) _is the phase angle of the complex function uk_ ( _x_ ) _)_ . 

**Tracking a Point of Constant Phase (a Wave Crest)** Suppose you are standing at position _x_ 1 at time _t_ 1, watching a specific wave crest where the phase equals Φ0. As time advances to _t_ 1 + ∆ _t_ , where must that crest move (∆ _x_ )? 

To keep the phase constant (Φ0): 



<!-- Start of picture text -->
k ( x 1 + ∆ x )  − ω ( t 1 + ∆ t ) =  kx 1  − ωt 1<br><!-- End of picture text -->



<!-- Start of picture text -->
k ∆ x − ω ∆ t  = 0 = ⇒ ￿x<br>￿t = ω k =  v phase<br><!-- End of picture text -->

Because the phase advances by ∆ _ϕ_ = _ka_ from cell to cell, **the entire wave pattern must continuously glide to the right at the phase velocity** _vp_ = _ω_ / _k_ to maintain constant phase fronts. 

## **4. Proof via Quantum Probability Current Density (** _J_ **)** 

The ultimate test of a **traveling wave** versus a **standing wave** is whether it carries a steady flow of probability (or electric charge) across space. 

The quantum mechanical **probability current density** _J_ is defined as: 



<!-- Start of picture text -->
J = h ¯ Ψ ∗ ∂ Ψ<br>2 mi ( ∂x − Ψ ∂ ∂x Ψ ∗ )<br><!-- End of picture text -->

Plugging in the Bloch wavefunction Ψ( _x, t_ ) = _uk_ ( _x_ ) _e_<sup>_i_(</sup><sup>_kx−ωt_)</sup> : 

1. Calculate the spatial derivative: 



<!-- Start of picture text -->
∂ Ψ<br>∂x = ( dudxk +  ikuk ) e i ( kx−ωt )<br><!-- End of picture text -->

2. Substitute into _J_ : 



<!-- Start of picture text -->
duk<br>J = hk ¯ u ∗ k<br>m |uk ( x ) | 2 + m h ¯ Im dx<br>( )<br><!-- End of picture text -->

## **What does this tell us?** 

- **In a Standing Wave (e.g., at Brillouin zone boundaries** _k_ = _±π_ / _a_ **):** The wave becomes a real cosine/sine wave, forcing _J_ = 0 (zero net probability flow; no energy propagates). 

- **In a Bloch State (** _k̸_ = 0 **):** The first term<sup>_<u>hk</u>_¯</sup> _m_<sup>_|uk_(</sup><sup>_x_)</sup><sup>_|_2is</sup><sup>**non-zero**!Theconstant</sup> phase gradient _k_ =<sup>∆</sup> _a_<sup>_<u>ϕ</u>_drivesasteadystreamofprobability/electronfluxfromcell</sup> to cell without decay. 

Notes 

3 

## **Summary Visual** 

Unit Cell N Unit Cell N+1 Unit Cell N+2 |-------- u_k(x) --------| |-------- u_k(x) --------| |-------- u_k(x) _�→_ --------| | | | Phase: _φ_ Phase: _φ_ + ka Phase: _φ_ + 2ka 

===============> CONSTANT PHASE GRADIENT ==============> DRIVES UNHINDERED TRAVELING WAVE FLOW (J _̸_ = 0) 

The periodic potential modifies the local shape _uk_ ( _x_ ) inside each cell, but the **step-bystep phase shift** ∆ _ϕ_ = _ka_ **locks all cells together into a single continuous, propagating wave train** . 

