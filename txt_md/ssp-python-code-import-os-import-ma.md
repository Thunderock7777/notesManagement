<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-python-code-import-os-import-ma.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Here is the complete Python script to plot and model the **spherical constant-energy surface** and **isotropic** _E_ ( _k_ ) **band dispersion** of **Gallium Arsenide (GaAs)** . 

I have generated and saved the visualization (gaas_spherical_band.png) in your Studio panel. The script below includes path handling so it runs smoothly both locally on Windows/macOS and in Linux sandbox environments. 

## **1. Python Code** 

**import** os **import** matplotlib.pyplot **as** plt **import** numpy **as** np **from** mpl_toolkits.mplot3d **import** Axes3D 

- _# Set up figure with two panels: 3D Spherical Energy Surface & 1D E(k)_ 

- _�→ Dispersion_ 

fig = plt.figure(figsize=(14, 6.5), dpi=150) 

_#_ 

- _�→ ==============================================================================_ 

_# Panel 1: 3D Spherical Constant-Energy Surface centered at Gamma (k = 0) #_ 

> _�→ ==============================================================================_ ax1 = fig.add_subplot(121, projection='3d') 

- _# Parametric spherical surface centered at k = 0_ 

u = np.linspace(0, 2 * np.pi, 40) v = np.linspace(0, np.pi, 30) 

r_gaas = 0.55 _# Radius of constant-energy sphere in k-space_ 

X = r_gaas * np.outer(np.cos(u), np.sin(v)) Y = r_gaas * np.outer(np.sin(u), np.sin(v)) Z = r_gaas * np.outer(np.ones(np.size(u)), np.cos(v)) 

_# Plot the smooth, isotropic sphere_ 

Notes 

2 

ax1.plot_surface(X, Y, Z, color='#2ca02c', alpha=0.7, edgecolor='k', 

- _�→_ linewidth=0.2) 

_# Mark the Gamma point (k=0) at the origin_ ax1.plot([0],[0],[0], 'ko', markersize=7) 

_# Draw k-space coordinate axes_ ax1.quiver(-1.0, 0, 0, 2.0, 0, 0, color='black', arrow_length_ratio=0.05, _�→_ linewidth=1.2) ax1.quiver(0, -1.0, 0, 0, 2.0, 0, color='black', arrow_length_ratio=0.05, _�→_ linewidth=1.2) 

- ax1.quiver(0, 0, -1.0, 0, 0, 2.0, color='black', arrow_length_ratio=0.05, _�→_ linewidth=1.2) 

_# Labels and view angle_ ax1.set_xlabel(r'$k_x$', fontsize=11, labelpad=5) ax1.set_ylabel(r'$k_y$', fontsize=11, labelpad=5) ax1.set_zlabel(r'$k_z$', fontsize=11, labelpad=5) ax1.set_xlim([-1.0, 1.0]) ax1.set_ylim([-1.0, 1.0]) ax1.set_zlim([-1.0, 1.0]) ax1.set_title(r'3D Momentum Space **(** $k$-space **)** ' + '\n' + r'Isotropic Spherical _�→_ Energy Surface at $\Gamma **(** k=0 **)** $', fontsize=12, fontweight='bold', pad=10) ax1.view_init(elev=22, azim=38) 

_#_ 

- _�→ ==============================================================================_ 

_# Panel 2: Isotropic Parabolic E(k) Band Dispersion in GaAs #_ 

- _�→ ==============================================================================_ 

ax2 = fig.add_subplot(122) 

_# Wavevector k range_ 

k_vals = np.linspace(-1.0, 1.0, 400) 

_# E(k) = hbar^2 k^2 / (2 m*) with m* = 0.067 m0 for GaAs_ 

_# For comparison, show a heavier reference band (m* = 0.50 m0)_ E_gaas = (k_vals**2) / 0.067 _# Steep parabola (light mass)_ E_heavy = (k_vals**2) / 0.50 _# Flatter parabola (heavy mass)_ 

- ax2.plot(k_vals, E_gaas, color='#2ca02c', linewidth=2.8, label=r'GaAs 

- _�→_ Conduction Band **(** $m^* = 0.067 m_0$, Steep & Light **)** ') 

- ax2.plot(k_vals, E_heavy, color='gray', linestyle='--', linewidth=1.8, 

- _�→_ label=r'Reference Heavy Band **(** $m^* = 0.50 m_0$, Flat & Heavy **)** ') 

_# Mark conduction band minimum Ec at k=0_ ax2.plot(0, 0, 'ro', markersize=8) 

- ax2.text(0.04, -0.8, r'$E_c \text{ at } \Gamma **(** k=0 **)** $', fontsize=11, 

- _�→_ fontweight='bold', color='red') 

Notes 

3 

_# Annotations_ 

ax2.annotate(r'High Band Curvature $\frac{d^2E}{dk^2}$' + '\n' + 

- _�→_ 

   - r'$\rightarrow$ Light Mass **(** $m^* = 0.067 m_0$ **)** ' + '\n' + r'$\rightarrow$ 

- _�→_ High Mobility **(** $\mu_n \approx 8500 \text{ cm}^2/\text{V} **\** cdot\text{s}$ **)** ', xy=(0.35, E_gaas[np.argmin(np.abs(k_vals - 0.35))]), xytext=(0.20, 

- _�→_ 8.0), 

   - arrowprops=dict(facecolor='black', shrink=0.08, width=1, 

- _�→_ headwidth=6), 

fontsize=9.5, bbox=dict(boxstyle='round,pad=0.4', 

- _�→_ facecolor='white', alpha=0.9)) 

_# Formatting_ 

ax2.axhline(0, color='black', linestyle='-', linewidth=0.8) ax2.axvline(0, color='gray', linestyle=':', linewidth=0.8) ax2.set_xlim([-1.0, 1.0]) ax2.set_ylim([-1.5, 15.0]) 

ax2.set_xlabel(r'Wavevector $k = \sqrt{k_x^2 + k_y^2 + k_z^2}$ **(** Any Direction **)** ', 

- _�→_ fontsize=11, fontweight='bold') 

ax2.set_ylabel(r'Energy $ **(** E - E_c **)** $ **(** a.u. **)** ', fontsize=11, fontweight='bold') 

ax2.set_title(r'Isotropic Parabolic Dispersion $E **(** k **)** = **\** hbar^2 k^2 / **(** 2m^* **)** $' + 

- _�→_ '\n' + r'Identical in ALL directions', fontsize=12, fontweight='bold', 

- _�→_ 

- pad=10) 

ax2.legend(loc='upper left', fontsize=9.5) ax2.grid(True, linestyle=':', alpha=0.5) 

plt.tight_layout() 

_# Save image locally_ output_path = ”gaas_spherical_band.png” plt.savefig(output_path, dpi=150, bbox_inches=”tight”) plt.show() print(f”Successfully generated and saved plot as '{output_path}'”) 

Notes 

4 



<!-- Start of picture text -->
3D Momentum Space (k-space) Isotropic Parabolic Dispersion E(k) = n²k²/(2m*)<br>Isotropic Spherical Energy Surface at Γ(k = 0) Identical in ALL directions<br>14 GaAs Conduction Band (m * = 0.067m0. Steep & Light)<br>Reference Heavy Band (m* = 0.50m0, Flat & Heavy)<br>12<br>1.00 10<br>0.75 High Band Curvature<br>→ Light Mass (m* = 0.067m0)<br>0.50 8 → High Mobility (μn = 8500 cm2V · s)<br>0.25<br>0.00<br>-0.25<br>-0.50<br>-0.75 Energy (E � Ec) (a.u.)<br>-1.00<br>-0.5050.5.00<br>0.00 -0.25<br>0<br>1-1.0.750.50.250.00 0.250.50 0.75<br>1.001.00 0.750.500.25 Kx Ec at F(k = 0)<br>-1.00 -0.75 -0.50 -0.25 0.00 0.25 0.50 0.75 1.00<br>Wavevector k = √k2 + k2 + k2 (Any Direction)<br><!-- End of picture text -->

**2. Detailed Physical Explanation for GaAs** 

- **A. Why is the Energy Surface Spherical in GaAs?** 

   1. **Direct Band Gap at the** Γ **-Point (** _k_ = 0 **):** Unlike Silicon, where the 6 conduction band minima lie along the _⟨_ 100 _⟩_ directions off-center, GaAs is a **direct bandgap semiconductor** . Its conduction band minimum sits right at the exact center of the Brillouin zone ( _kx_ = 0 _, ky_ = 0 _, kz_ = 0). 

   2. **Cubic Symmetry at the Origin:** Because the origin _k_ = 0 possesses full cubic point-group symmetry, the energy dispersion _E_ ( _⃗k_ ) must be **100% isotropic** (identical in every spatial direction): 



<!-- Start of picture text -->
E ( ⃗k )  − Ec = h ¯2( k x 2 +  k y 2 +  k z 2) = h ¯2 k 2<br>2 m ∗ 2 m ∗<br><!-- End of picture text -->

Setting energy _E_ = constant gives the standard 3D sphere equation: 



<!-- Start of picture text -->
kx 2 +  k y 2 +  k z 2 = constant<br><!-- End of picture text -->

- **B. Why is the Mass so Light (** _m_<sup>_∗_</sup> = 0 _._ 067 _m_ 0 **)?** 

   - **Band Curvature:** Effective mass is inversely proportional to the second derivative of the energy band: 



<!-- Start of picture text -->
m ∗ = h ¯2<br>d 2 E<br>dk 2<br><!-- End of picture text -->

- In GaAs, the conduction band minimum at _k_ = 0 rises **very steeply** (high<sup>_<u>d</u>_</sup> _dk_<sup>2</sup><sup>_<u>E</u>_2).</sup> 

- This steep curvature results in an extremely light effective mass ( _m_<sup>_∗_</sup> = 0 _._ 067 _m_ 0, roughly 15 _×_ lighter than a free electron!). 

- **High Electron Mobility:** Because mobility _µn_ = _meτ_<sup>_∗_isinverselyproportionalto</sup> effective mass, GaAs electrons move extremely fast ( _µn ≈_ 8500 cm<sup>2</sup> /V _·_ s, compared 

Notes 

5 

to Silicon’s _∼_ 1400 cm<sup>2</sup> /V _·_ s), making GaAs ideal for high-frequency RF devices and optoelectronics. 

**C. Density-of-States Mass vs. Conductivity Mass in GaAs** Because GaAs has **only 1 valley** located at _k_ = 0 ( _Mc_ = 1) and its mass is **completely isotropic** ( _mx_ = _my_ = _mz_ = _m_<sup>_∗_</sup> ), both scalar effective mass definitions simplify to the **exact same number** : 

1. **Density-of-States Effective Mass (** _m_<sup>_∗_</sup> _dn_<sup>**):**</sup> 



<!-- Start of picture text -->
m ∗ dn =  M  2/3 c ( mxmymz ) 1/3 = 1 2/3 ( m ∗ · m ∗ · m ∗ ) 1/3 =  m ∗ =  0 . 067m0<br>2. Conductivity Effective Mass ( m ∗ cn ):<br>1 = 1 + 1 + 1 = 1 = ⇒ m ∗ cn =  m ∗ =  0 . 067m0<br>m ∗ cn 3 ( m 1 x my mz ) 3 ( m 3 ∗ )<br><!-- End of picture text -->

**Key Takeaway for GATE:** In isotropic direct gap semiconductors like GaAs, _m_<sup>_∗_</sup> _dn_<sup>=</sup><sup>_m_</sup> _cn_<sup>_∗_=</sup><sup>_m∗_,whereasinanisotropicmulti-valleysemiconductorslike</sup> Silicon, _m_<sup>_∗_</sup> _dn̸_<sup>=</sup><sup>_m_</sup> _cn_<sup>_∗_(1</sup><sup>_._08</sup><sup>_m_0vs0</sup><sup>_._26</sup><sup>_m_0).</sup> 

_Would you like to explore hole band structures (Heavy Hole vs Light Hole bands) or solve another numerical problem next?_ 

