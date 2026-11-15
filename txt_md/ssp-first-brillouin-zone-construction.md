<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-first-brillouin-zone-construction.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Here is a complete, self-contained Python script to plot both fundamental graphs of the **Kronig-Penney Model** : 

1. **Condition Graph:** _F_ ( _αa_ ) = _P_<sup>sin</sup> _αa_<sup><u>(</u></sup><sup>_αa_</sup><sup><u>)</u></sup> + cos( _αa_ ) vs _αa_ (showing allowed bands and forbidden gaps bounded between _−_ 1 and +1). 

2. **Dispersion Relation Graph:** _E_ ( _k_ ) vs _k_ in the First Brillouin Zone ( _−π_ / _a ≤ k ≤ π_ / _a_ ), showing energy band bending and forbidden gaps at zone boundaries. 

## **Python Code** 

**import** matplotlib.pyplot **as** plt **import** numpy **as** np 

_# Set figure and subplots_ 

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), dpi=150) 

_#_ 

- _�→ ==============================================================================_ 

- _# Graph 1: F(alpha*a) vs alpha*a (Allowed Bands & Forbidden Gaps) #_ 

- _�→ ==============================================================================_ 

P = 3.0 * np.pi _# Barrier strength parameter (P = 3*pi)_ alpha_a = np.linspace(0.01, 4 * np.pi, 2000) 

- _# Calculate Kronig-Penney function F(alpha*a)_ 

F = P * np.sin(alpha_a) / alpha_a + np.cos(alpha_a) 

- _# Plot F(alpha*a) curve and boundary lines (+1 and -1)_ 

- ax1.plot(alpha_a / np.pi, F, 'b-', linewidth=2, label=r'$F **(** \alpha a **)** = P 

- _�→_ \frac{\sin **(** \alpha a **)** }{\alpha a} + **\** cos **(** \alpha a **)** $') 

- ax1.axhline(1.0, color='r', linestyle='--', linewidth=1.5, label=r'Upper Bound _�→_ **(** +1 **)** ') 

- ax1.axhline(-1.0, color='r', linestyle='--', linewidth=1.5, label=r'Lower Bound _�→_ **(** -1 **)** ') 

- _# Identify allowed (|F| <= 1) and forbidden (|F| > 1) regions_ allowed_mask = (F >= -1.0) & (F <= 1.0) 

Notes 

2 

ax1.fill_between(alpha_a / np.pi, -3, 3, where=allowed_mask, color='green', 

- _�→_ alpha=0.2, label='Allowed Bands') 

ax1.fill_between(alpha_a / np.pi, -3, 3, where=~allowed_mask, color='red', _�→_ alpha=0.1, label='Forbidden Gaps') 

_# Format Graph 1_ 

ax1.set_ylim(-2.5, 3.5) ax1.set_xlim(0, 4) ax1.set_xlabel(r'$\alpha a / **\** pi$', fontsize=12, fontweight='bold') ax1.set_ylabel(r'$F **(** \alpha a **)** $', fontsize=12, fontweight='bold') ax1.set_title(r'Kronig-Penney Condition: $F **(** \alpha a **)** $ vs $\alpha a$ **(** $P = _�→_ 3 **\** pi$ **)** ', fontsize=13, fontweight='bold', pad=12) ax1.legend(loc='upper right', frameon=True, fontsize=9) ax1.grid(True, linestyle=':', alpha=0.6) 

_# �→ ============================================================================== # Graph 2: E(k) Dispersion Relation (Reduced Zone Scheme) # �→ ============================================================================== # Filter allowed alpha_a and calculate crystal wavevector ka = arccos(F)_ allowed_alpha = alpha_a[allowed_mask] allowed_F = F[allowed_mask] ka = np.arccos(allowed_F) _# ka ranges from 0 to pi_ 

_# Separate contiguous energy bands_ bands = [] curr_alpha, curr_ka = [], [] **for** i **in** range(len(allowed_alpha)): **if** i == 0 **or** (allowed_alpha[i] - allowed_alpha[i-1]) < 0.05: curr_alpha.append(allowed_alpha[i]) curr_ka.append(ka[i]) **else** : bands.append((np.array(curr_alpha), np.array(curr_ka))) curr_alpha, curr_ka = [allowed_alpha[i]], [ka[i]] **if** curr_alpha: bands.append((np.array(curr_alpha), np.array(curr_ka))) _# Plot E(k) for the first 4 bands_ colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'] **for** idx, (b_alpha, b_ka) **in** enumerate(bands[:4]): b_E = (b_alpha / np.pi)**2 _# Energy proportional to (alpha*a)^2 # Symmetric branches in the First Brillouin Zone [-pi/a, +pi/a]_ ax2.plot(b_ka / np.pi, b_E, color=colors[idx], linewidth=2.5, label=f'Band _�→_ {idx+1}') ax2.plot(-b_ka / np.pi, b_E, color=colors[idx], linewidth=2.5) 

_# Format Graph 2_ 

Notes 

3 

ax2.set_xlim(-1.1, 1.1) ax2.set_ylim(0, 16) 

ax2.set_xlabel(r'Crystal Wavevector $ka / **\** pi$ **(** First Brillouin Zone **)** ', fontsize=12, fontweight='bold') 

- ax2.set_ylabel(r'Energy $E **\** propto **(** \alpha a / **\** pi **)** ^2$', fontsize=12, fontweight='bold') 

- ax2.set_title(r'$E **(** k **)** $ Dispersion Relation & Energy Gaps', fontsize=13, fontweight='bold', pad=12) 

ax2.axvline(0, color='k', linestyle=':', alpha=0.5) 

ax2.legend(loc='upper right', frameon=True, fontsize=10) ax2.grid(True, linestyle=':', alpha=0.6) 

### plt.tight_layout() 

plt.savefig('kronig_penney_model.png', dpi=150, bbox_inches='tight') plt.show() 



<!-- Start of picture text -->
Kronig-Penney Condition: F(αa) vs αa (P = 3π) E(k) Dispersion Relation & Energy Gaps<br>16<br>F(a) = isa + pcs(a)Upper Bound (+1) Band 2Band 1<br>Lower Bound (-1) 14 Band<br>Allowed Bands Band 4<br>Forbidden Gaps<br>2 12<br>10<br>F(αa)<br>Energy Eα (αa/n)²<br>4<br>-2<br>0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 -1.00 -0.75 -0.50 -0.25 0.00 0.25 0.50 0.75 1.00<br>αa/π Crystal Wavevector ka/π (First Brillouin Zone)<br><!-- End of picture text -->

## **Detailed Graph Explanations** 

**Left Graph:** _F_ ( _αa_ ) **vs** _αa_ 

1. **The Condition Line (Blue Curve):** Represents the function _F_ ( _αa_ ) = _P_<sup>sin</sup> _αa_<sup><u>(</u></sup><sup>_αa_</sup><sup><u>)</u></sup> + cos( _αa_ ). 

2. **Boundary Lines (Red Dashed):** Since cos( _ka_ ) can only take values between _−_ 1 and +1, physical wavevector solutions _k_ exist **only** when _−_ 1 _≤ F_ ( _αa_ ) _≤_ +1. 

3. **Green Regions (Allowed Bands):** Where the blue curve sits between the red dashed lines. The electron wavevector _k_ is real, forming unattenuated, propagating Bloch traveling waves. 

4. **Red Regions (Forbidden Band Gaps):** Where the curve exceeds +1 or drops below _−_ 1. _k_ becomes complex, causing exponential wave attenuation ( _e_<sup>_−κx_</sup> ). No electron stationary states exist at these energies. 

5. **Damping at Higher Energies:** As energy increases ( _αa →∞_ ), the amplitude of the<sup>sin</sup> _αa_<sup><u>(</u></sup><sup>_αa_</sup><sup><u>)</u></sup> term decays, making **allowed bands wider** and **forbidden gaps narrower** . 

Notes 

4 

## **Right Graph:** _E_ ( _k_ ) **Dispersion Curve** 

1. **Band Formation:** Plotting energy _E ∝_ ( _αa_ )<sup>2</sup> against wavevector _k_ in the First Brillouin Zone ( _−π ≤ ka ≤ π_ ). 

2. **Band Bending & Standing Waves:** Near _ka_ = _±π_ , the slope<sup>_<u>dE</u>_</sup> _dk_<sup>=0(group</sup> velocity _vg_ = 0). Electron waves undergo Bragg reflection, forming standing waves. 

3. **Energy Discontinuities (Gaps):** Clear vertical energy gaps separate Band 1, Band 2, Band 3, and Band 4 at the Brillouin zone boundaries ( _k_ = _±π_ / _a_ ). 

I have also rendered and saved the high-resolution visualization file kronig_penney_ model.png in your Studio panel. 

Would you like to analyze how changing the barrier strength parameter _P_ affects the width of these band gaps? 

