<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-python-visualization-code-impor.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

Here is a complete, publication-quality Python script that models and visualizes the **6 conduction band valleys of Silicon** in both 3D momentum space ( _k_ -space) and a 2D slice ( _kz_ = 0). 

The generated visualization (silicon_valleys.png) has been published to your Studio panel. 

## **1. Python Visualization Code** 

**import** matplotlib matplotlib.use('Agg') _# Headless rendering for clean file output_ **import** matplotlib.pyplot **as** plt **import** numpy **as** np **from** mpl_toolkits.mplot3d **import** Axes3D **import** os **import** shutil 

os.makedirs('/workspace/scratch', exist_ok=True) 

_# Set up figure with two panels: 3D Valleys & 2D Projection Slice_ fig = plt.figure(figsize=(14, 6.5), dpi=150) 

_#_ 

- _�→ ==============================================================================_ 

_# Panel 1: 3D Representation of 6 Ellipsoidal Conduction Band Valleys in_ 

- _�→ Silicon_ 

_#_ 

- _�→ ==============================================================================_ 

ax1 = fig.add_subplot(121, projection='3d') 

- _# Parameters for Silicon valleys along <100> directions_ k0 = 0.85 _# Position of conduction band minimum in units of (2*pi/a)_ a_long = 0.28 _# Longitudinal semi-axis (heavy mass direction)_ a_trans = 0.12 _# Transverse semi-axis (light mass direction)_ 

- _# Base parametric sphere coordinates_ 

u = np.linspace(0, 2 * np.pi, 30) 

Notes 

2 

v = np.linspace(0, np.pi, 20) 

_# 6 Valley centers located along <100> axes_ valley_centers = [ ( k0, 0, 0, 'x'), (-k0, 0, 0, 'x'), _# +x, -x_ ( 0, k0, 0, 'y'), ( 0, -k0, 0, 'y'), _# +y, -y_ ( 0, 0, k0, 'z'), ( 0, 0, -k0, 'z') _# +z, -z_ ] 

colors = ['#1f77b4', '#1f77b4', '#ff7f0e', '#ff7f0e', '#2ca02c', '#2ca02c'] 

**for** idx, (cx, cy, cz, axis) **in** enumerate(valley_centers): x_unit = np.outer(np.cos(u), np.sin(v)) y_unit = np.outer(np.sin(u), np.sin(v)) z_unit = np.outer(np.ones(np.size(u)), np.cos(v)) 

**if** axis == 'x': 

X = cx + a_long * x_unit Y = cy + a_trans * y_unit Z = cz + a_trans * z_unit **elif** axis == 'y': X = cx + a_trans * x_unit Y = cy + a_long * y_unit Z = cz + a_trans * z_unit **else** : _# axis == 'z'_ X = cx + a_trans * x_unit Y = cy + a_trans * y_unit Z = cz + a_long * z_unit 

- _�→_ 

- ax1.plot_surface(X, Y, Z, color=colors[idx], alpha=0.75, edgecolor='k', linewidth=0.2) 

_# Draw k-space coordinate axes_ 

- ax1.quiver(-1.1, 0, 0, 2.2, 0, 0, color='black', arrow_length_ratio=0.05, _�→_ linewidth=1.2) 

- ax1.quiver(0, -1.1, 0, 0, 2.2, 0, color='black', arrow_length_ratio=0.05, _�→_ linewidth=1.2) 

- ax1.quiver(0, 0, -1.1, 0, 0, 2.2, color='black', arrow_length_ratio=0.05, _�→_ linewidth=1.2) 

_# Labels and view angle_ 

ax1.set_xlabel(r'$k_x **\** quad **(** 2 **\** pi/a **)** $', fontsize=10, labelpad=5) ax1.set_ylabel(r'$k_y **\** quad **(** 2 **\** pi/a **)** $', fontsize=10, labelpad=5) ax1.set_zlabel(r'$k_z **\** quad **(** 2 **\** pi/a **)** $', fontsize=10, labelpad=5) ax1.set_xlim([-1.1, 1.1]) ax1.set_ylim([-1.1, 1.1]) ax1.set_zlim([-1.1, 1.1]) 

- ax1.set_title('3D Momentum Space (k-space)\n6 Ellipsoidal Conduction Band _�→_ Valleys', fontsize=12, fontweight='bold', pad=10) 

Notes 

3 

ax1.view_init(elev=22, azim=38) 

_#_ 

- _�→ ==============================================================================_ 

_# Panel 2: 2D Cross-Section in the kx - ky Plane (kz = 0)_ 

_#_ 

- _�→ ==============================================================================_ 

- ax2 = fig.add_subplot(122) 

t = np.linspace(0, 2*np.pi, 200) 

_# +x & -x valleys (elongated along kx)_ 

ax2.fill(k0 + a_long*np.cos(t), a_trans*np.sin(t), color='#1f77b4', alpha=0.6, 

- _�→_ 

- label='X-Valleys (Major along $k_x$)') 

ax2.plot(k0 + a_long*np.cos(t), a_trans*np.sin(t), color='black', lw=1) ax2.fill(-k0 + a_long*np.cos(t), a_trans*np.sin(t), color='#1f77b4', alpha=0.6) ax2.plot(-k0 + a_long*np.cos(t), a_trans*np.sin(t), color='black', lw=1) 

_# +y & -y valleys (elongated along ky)_ 

ax2.fill(a_trans*np.cos(t), k0 + a_long*np.sin(t), color='#ff7f0e', alpha=0.6, 

- _�→_ 

- label='Y-Valleys (Major along $k_y$)') 

ax2.plot(a_trans*np.cos(t), k0 + a_long*np.sin(t), color='black', lw=1) 

ax2.fill(a_trans*np.cos(t), -k0 + a_long*np.sin(t), color='#ff7f0e', alpha=0.6) ax2.plot(a_trans*np.cos(t), -k0 + a_long*np.sin(t), color='black', lw=1) 

_# Mark the Zone Center Gamma Point (k=0)_ 

ax2.plot(0, 0, 'ko', markersize=6) 

ax2.text(0.04, 0.04, r'$\Gamma **(** k=0 **)** $', fontsize=11, fontweight='bold') 

_# Annotations for Mass Anisotropy_ 

ax2.annotate(r'Longitudinal Mass $m_l \approx 0.98 m_0$' + '\n' + r' **(** Heavy, Slow 

- _�→_ 

- along $k_x$ **)** ', 

xy=(k0, 0), xytext=(0.42, -0.45), 

   - arrowprops=dict(facecolor='black', shrink=0.08, width=1, 

- _�→_ 

   - headwidth=6), 

      - fontsize=9, bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 

- _�→_ 

   - alpha=0.9)) 

- ax2.annotate(r'Transverse Mass $m_t \approx 0.19 m_0$' + '\n' + r' **(** Light, Fast 

- _�→_ along $k_y$ **)** ', 

xy=(k0, a_trans), xytext=(0.42, 0.35), 

arrowprops=dict(facecolor='black', shrink=0.08, width=1, 

- _�→_ 

- headwidth=6), 

fontsize=9, bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 

- _�→_ 

- alpha=0.9)) 

_# Formatting_ 

ax2.axhline(0, color='gray', linestyle='--', linewidth=0.8) ax2.axvline(0, color='gray', linestyle='--', linewidth=0.8) 

Notes 

4 

ax2.set_xlim([-1.1, 1.1]) ax2.set_ylim([-1.1, 1.1]) ax2.set_xlabel(r'$k_x **\** quad **(** 2 **\** pi/a **)** $', fontsize=11, fontweight='bold') ax2.set_ylabel(r'$k_y **\** quad **(** 2 **\** pi/a **)** $', fontsize=11, fontweight='bold') ax2.set_title('2D Slice ($k_z = 0$): Anisotropy of Constant-Energy Surfaces', fontsize=12, fontweight='bold', pad=10) ax2.legend(loc='lower left', fontsize=9) ax2.grid(True, linestyle=':', alpha=0.5) 

### plt.tight_layout() 

plt.savefig('/workspace/scratch/silicon_valleys.png', dpi=150, bbox_ inches='tight') 

plt.close() 

_# Publish to out directory_ 

shutil.copy('/workspace/scratch/silicon_valleys.png', '/workspace/out/silicon_ valleys.png') 



<!-- Start of picture text -->
3D Momentum Space (k-space)<br>6 Ellipsoidal Conduction Band Valleys 2D Slice (kz = 0): Anisotropy of Constant-Energy Surfaces<br>1.00<br>0.75<br>0.50<br>1.00 Transverse Mass m ≈ 0.19m0<br>(Light, Fast along ky)<br>0.75<br>0.25<br>0.50<br>0.25 Γ(k=0)<br>0.00 (2na) 0.00<br>-0.25<br>-0.50 -0.25<br>-0.75 Longitudinal Mass m, ≈ 0.98m<br>-1.00 -0.50 (Heavy, Slow along kx)<br>-1.00.750.50.250.00.250.500.75ky (2π/a) 1.00 1.000.75 0.50 Kx(2π/a) -0.75-1.00 x-Valleys (Major along kx)Y-Valleys (Major along ky)<br>-1.00 -0.75 -0.50 -0.25 0.00 0.25 0.50 0.75 1.00<br>kx (2π/a)<br><!-- End of picture text -->

## **2. Detailed Physical Explanation of the Plot** 

## **A. Why are there 6 Valleys?** 

- **Silicon is an Indirect Bandgap Semiconductor:** Unlike Gallium Arsenide (GaAs), where the conduction band minimum sits right at the center (Γ-point, _k_ = 0), Silicon’s conduction band minima sit at _k_ 0 _≈_ 0 _._ 85 ( 2 _aπ_ ) away from the center along the 6 equivalent _⟨_ 100 _⟩_ crystallographic axes. 

- Because cubic symmetry treats all 6 Cartesian direction vectors ( _±kx, ±ky, ±kz_ ) identically, there are **6 degenerate conduction band energy minima (valleys)** in _k_ -space. 

Notes 

5 

**B. What do the Prolate Ellipsoids Represent?** Every point on the surface of one of these ellipsoids represents an electron state possessing the **exact same constant kinetic energy (** _E_ **)** above the conduction band minimum _Ec_ : 



<!-- Start of picture text -->
∆ E =  E − Ec = h ¯2( kx − kx 0)2 + h ¯2( ky − ky 0)2 + h ¯2( kz − kz 0)2<br>2 mx 2 my 2 mz<br><!-- End of picture text -->

Because the energy surface is elongated into a cigar shape (prolate ellipsoid) rather than a sphere: 

1. **Along the Major Axis (Longitudinal direction along the valley axis):** The energy curve _E_ ( _k_ ) has low curvature (<sup>_<u>d</u>_</sup> _dk_<sup>2</sup><sup>_<u>E</u>_2is small), resulting in a</sup><sup>**heavylongitudi-**</sup> **nal effective mass (** _ml ≈_ 0 _._ 98 _m_ 0 **)** . Electrons moving in this direction accelerate slowly under an electric field. 

2. **Along the Minor Axes (Transverse direction perpendicular to valley axis):** The energy curve _E_ ( _k_ ) opens up steeply (<sup>_<u>d</u>_</sup> _dk_<sup>2</sup><sup>_<u>E</u>_2islarge),resultingina</sup><sup>**lighttrans-**</sup> **verse effective mass (** _mt ≈_ 0 _._ 19 _m_ 0 **)** . Electrons accelerate rapidly in this direction. 

**C. Connecting the Plot to Density-of-States Mass vs. Conductivity Mass** Looking at the 2D slice on the right panel reveals why we need two different scalar mass definitions: 

1. **Density-of-States Effective Mass (** _m_<sup>_∗_</sup> _dn_<sup>= 1</sup><sup>_._08</sup><sup>_m_0</sup><sup>**):**</sup> 

   - Counting carrier populations involves integrating the total volume enclosed by **all 6 ellipsoidal valleys** in 3D momentum space. 

   - To map 6 ellipsoids into an equivalent single isotropic sphere with the same momentum volume, we take the **geometric mean** : 

      - _m_<sup>_∗_</sup> _dn_<sup>= 62/3(</sup><sup>_mlm_2</sup> _t_<sup>)1/3</sup><sup>_≈_1</sup><sup>_._08</sup><sup>_m_0</sup> 

   - The factor 6<sup>2/3</sup> boosts the value significantly above the free electron mass _m_ 0. 

2. **Conductivity Effective Mass (** _m_<sup>_∗_</sup> _cn_<sup>= 0</sup><sup>_._26</sup><sup>_m_0</sup><sup>**):**</sup> 

   - When an electric field is applied (e.g., along the + _kx_ direction), the electrons in the 2 X-valleys experience heavy mass _ml_ , but the electrons in the 4 Y- and Z-valleys experience light mass _mt_ . 

   - Averaging the reciprocal acceleration (1/ _m_<sup>_∗_</sup> ) across all 6 valleys at thermal equilibrium yields the **harmonic mean** : 



<!-- Start of picture text -->
1 = 1 + 2 = ⇒ m ∗ cn = 3 mlmt ≈ 0 . 26 m 0<br>m ∗ cn 3 ( m 1 l mt ) mt  + 2 ml<br><!-- End of picture text -->

- Because transport is dominated by the lighter transverse direction ( _mt_ = 0 _._ 19 _m_ 0), _m_<sup>_∗_</sup> _cn_<sup>is much lighter (0</sup><sup>_._26</sup><sup>_m_0), making electron drift mobility in Silicon</sup> higher than a heavy mass would suggest. 

_Would you like to explore how hole effective masses in Silicon differ (heavy hole vs. light hole bands at k_ = 0 _), or solve a numerical problem on carrier mobility using these values?_ 

