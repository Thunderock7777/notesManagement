<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: ssp-ewald-brillouin.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

I have generated the visual diagram for the **Ewald Sphere Construction** and the **1st Brillouin Zone** (ewald_brillouin.png is published in your Studio panel). 

Below, you’ll find both the complete **Python script** (using matplotlib) and the standalone **LaTeX (TikZ)** code so you can use whichever format suits your needs best. 

## **1. Python Code (Matplotlib)** 

**import** matplotlib.pyplot **as** plt **import** numpy **as** np 

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6.5), dpi=200) 

_# ============================================================= # PANEL 1: EWALD SPHERE # =============================================================_ ax1.set_aspect('equal') a_recip = 1.5 

grid_x, grid_y = [], [] **for** i **in** range(-2, 3): **for** j **in** range(-2, 3): grid_x.append(i * a_recip) grid_y.append(j * a_recip) 

ax1.scatter(grid_x, grid_y, color='#2b5c8f', s=35, zorder=5, label='Reciprocal 

- _�→_ Lattice Points') 

O = np.array([0.0, 0.0]) G = np.array([1.5, 1.5]) ax1.scatter(O[0], O[1], color='#d95f02', s=70, zorder=6) ax1.text(O[0] + 0.15, O[1] - 0.25, r'Origin $O **(** 0,0 **)** $', fontsize=11, _�→_ fontweight='bold', color='#d95f02') ax1.scatter(G[0], G[1], color='#e7298a', s=70, zorder=6) ax1.text(G[0] + 0.15, G[1] + 0.15, r'$G **(** h,k **)** $', fontsize=11, fontweight='bold', _�→_ color='#e7298a') 

Notes 

2 

C = np.array([-0.5, 2.0]) R = np.linalg.norm(C - O) 

circle = plt.Circle(C, R, color='#1b9e77', fill=False, linestyle='--', 

- _�→_ linewidth=2.0, label=r'Ewald Sphere **(** $R = k = 2 **\** pi/ **\** lambda$ **)** ') 

ax1.add_patch(circle) 

ax1.scatter(C[0], C[1], color='#1b9e77', s=50, zorder=6) 

- ax1.text(C[0] - 0.7, C[1] + 0.2, r'Center $C$', fontsize=11, color='#1b9e77', 

- _�→_ fontweight='bold') 

- _# FIX: Convert numpy arrays to tuples for xy and xytext_ 

- ax1.annotate('', xy=tuple(O), xytext=tuple(C), arrowprops=dict(arrowstyle=”-|>”, _�→_ color='#7570b3', lw=2.5, mutation_scale=15)) 

- ax1.text((C[0]+O[0])/2 - 0.6, (C[1]+O[1])/2, r'$\vec{k}_i$', fontsize=13, 

- _�→_ color='#7570b3', fontweight='bold') 

- ax1.annotate('', xy=tuple(G), xytext=tuple(C), arrowprops=dict(arrowstyle=”-|>”, 

- _�→_ color='#1b9e77', lw=2.5, mutation_scale=15)) 

- ax1.text((C[0]+G[0])/2 + 0.1, (C[1]+G[1])/2 + 0.2, r'$\vec{k}_f$', fontsize=13, _�→_ color='#1b9e77', fontweight='bold') 

- ax1.annotate('', xy=tuple(G), xytext=tuple(O), arrowprops=dict(arrowstyle=”-|>”, 

- _�→_ color='#e7298a', lw=2.5, mutation_scale=15)) 

- ax1.text((O[0]+G[0])/2 + 0.2, (O[1]+G[1])/2 - 0.2, r'$\vec{G} = \vec{k}_f - 

- _�→_ \vec{k}_i$', fontsize=12, color='#e7298a', fontweight='bold') 

plane_dir = np.array([-1.0, 1.0]) / np.sqrt(2) p1, p2 = O + 1.2 * plane_dir, O - 1.2 * plane_dir 

ax1.plot([p1[0], p2[0]], [p1[1], p2[1]], color='#666666', linestyle=':', 

- _�→_ linewidth=1.8, label=r'Crystal Plane $ **(** hkl **)** $') 

ax1.set_xlim(-3.5, 3.5) ax1.set_ylim(-1.5, 4.5) 

- ax1.set_title('Ewald Sphere Construction\n' + r'Diffraction occurs when sphere _�→_ intersects a lattice point **(** $\Delta\vec{k} = \vec{G}$ **)** ', fontsize=12, 

- _�→_ fontweight='bold', pad=12) 

ax1.set_xlabel(r'$k_x$', fontsize=11) ax1.set_ylabel(r'$k_y$', fontsize=11) ax1.grid(True, linestyle=':', alpha=0.5) ax1.legend(loc='lower left', fontsize=9, framealpha=0.9) 

_# =============================================================_ 

_# PANEL 2: FIRST BRILLOUIN ZONE_ 

_# =============================================================_ 

ax2.set_aspect('equal') b = 2.0 

**for** i **in** range(-2, 3): **for** j **in** range(-2, 3): **if not** (i == 0 **and** j == 0): 

Notes 

3 

ax2.scatter(i*b, j*b, color='#2b5c8f', s=45, zorder=5) 

ax2.scatter(0, 0, color='#d95f02', s=70, zorder=6) ax2.text(0.1, -0.3, r'$\Gamma **(** 0,0 **)** $', fontsize=11, fontweight='bold', _�→_ color='#d95f02') 

bz_x = [-b/2, b/2, b/2, -b/2, -b/2] bz_y = [-b/2, -b/2, b/2, b/2, -b/2] ax2.fill(bz_x, bz_y, color='#1b9e77', alpha=0.18, label='1st Brillouin Zone') ax2.plot(bz_x, bz_y, color='#1b9e77', linewidth=2.5) 

G_right = np.array([b, 0.0]) 

_# FIX: Convert numpy arrays to tuples for xy and xytext_ 

ax2.annotate('', xy=tuple(G_right), xytext=(0,0), 

- _�→_ arrowprops=dict(arrowstyle=”-|>”, color='#e7298a', lw=2.0, mutation_ 

- _�→_ 

   - scale=12)) 

- ax2.text(b/2 - 0.2, -0.35, r'$\vec{G}$', fontsize=12, color='#e7298a', _�→_ fontweight='bold') 

ax2.plot([b/2, b/2], [-1.8, 1.8], color='#d95f02', linestyle='--', 

- _�→_ linewidth=2.0, label=r'Bragg Plane **(** $\vec{k} **\** cdot \frac{1}{2}\vec{G} = 

- _�→_ **|** \frac{1}{2}\vec{G} **|** ^2$ **)** ') 

k_b = np.array([b/2, 0.8]) 

_# FIX: Convert numpy arrays to tuples for xy and xytext_ 

- ax2.annotate('', xy=tuple(k_b), xytext=(0,0), arrowprops=dict(arrowstyle=”-|>”, _�→_ color='#7570b3', lw=2.5, mutation_scale=15)) 

ax2.scatter(k_b[0], k_b[1], color='#7570b3', s=60, zorder=7) 

- ax2.text(k_b[0]/2 - 0.4, k_b[1]/2 + 0.2, r'$\vec{k}$', fontsize=13, _�→_ color='#7570b3', fontweight='bold') 

k_ref = k_b - G_right 

_# FIX: Convert numpy arrays to tuples for xy and xytext_ 

ax2.annotate('', xy=tuple(k_ref), xytext=tuple(k_b), 

- _�→_ 

- _�→_ 

   - arrowprops=dict(arrowstyle=”-|>”, color='#d95f02', lw=2.0, linestyle='--', 

   - mutation_scale=12)) 

- ax2.text((k_b[0]+k_ref[0])/2 + 0.1, (k_b[1]+k_ref[1])/2 + 0.2, r'$\vec{k} - 

- _�→_ 

   - \vec{G}$', fontsize=11, color='#d95f02', fontweight='bold') 

- ax2.text(b/2 + 0.1, 0.1, r'$X **\** left **(** \frac{ **\** pi}{a}, 0\right **)** $', fontsize=10, 

- _�→_ fontweight='bold') 

- ax2.text(b/2 + 0.1, b/2 + 0.1, r'$M **\** left **(** \frac{ **\** pi}{a}, \frac{ **\** pi}{a}\right **)** $', 

- _�→_ fontsize=10, fontweight='bold') 

ax2.set_xlim(-2.8, 2.8) ax2.set_ylim(-2.8, 2.8) 

ax2.set_title('1st Brillouin Zone Construction\n' + r'Boundary is the 

- _�→_ perpendicular bisector of $\vec{G}$ **(** $2\vec{k} **\** cdot\vec{G} = G^2$ **)** ', 

- _�→_ fontsize=12, fontweight='bold', pad=12) 

- ax2.set_xlabel(r'$k_x$', fontsize=11) 

Notes 

4 

ax2.set_ylabel(r'$k_y$', fontsize=11) ax2.grid(True, linestyle=':', alpha=0.5) ax2.legend(loc='lower left', fontsize=9, framealpha=0.9) 

### plt.tight_layout() 

plt.savefig('ewald_brillouin.png', dpi=200, bbox_inches='tight') plt.show() 



<!-- Start of picture text -->
Ewald Sphere Construction 1st Brillouin Zone Construction<br>Diffraction occurs when sphere intersects a lattice point (� = ) Boundary is the perpendicular bisector of  (2k·  = G²)<br>4<br>2 ● ● ●<br>3<br>1 k-G M(g, )<br>Center C<br>2 kr<br>● G(h, k) 0 ● x(, 0)<br>1 k r(0,0)<br>=kf�k<br>-1<br>0 ●<br>'Origin O(0, 0)<br>-2 ●<br>-1 C2Reciprocal Lattice PointsEwald Sphere (R = k = 2π/λ) 1st Brillouin Zone<br>Crystal Plane (hk/) Bragg Plane (k · G = |2G|2)<br>ε� -2 -1 0 1 2 3 -2 -1 0 2<br>kx kx<br><!-- End of picture text -->

## **2. LaTeX / TikZ Code** 

You can paste this code directly into your LaTeX document (requires \usepackage{tikz} and \usepackage{amsmath}): 

\documentclass{article} 

- \usepackage{tikz} 

\usepackage{amsmath,amssymb} 

\usetikzlibrary{arrows.meta,patterns,decorations.markings} 

**\begin** {document} 

**\begin** {figure}[htbp] \centering 

**\begin** {tikzpicture}[scale=1.2, >=Stealth] 

_% --- Left Panel: Ewald Sphere ---_ 

**\begin** {scope}[shift={(0,0)}] 

_% Title_ 

\node[align=center, font=\bfseries] at (0, 3.8) {Ewald Sphere Construction \\ \small $\Delta\vec{k} = \vec{G}$}; 

_% Reciprocal Lattice Grid_ 

\foreach \x in {-2,-1,0,1,2} { 

Notes 

5 

\foreach \y in {-1,0,1,2,3} { \fill[blue!70!black] (\x*1.2, \y*1.2) circle (1.8pt); } } _% Points: Origin O(0,0) and Point G(1,1)_ \coordinate (O) at (0,0); \coordinate (G) at (1.2,1.2); \coordinate (C) at (-0.5, 1.8); _% Center of sphere % Ewald Circle_ \draw[teal, thick, dashed] (C) circle (1.868); \fill[teal] (C) circle (2pt) node[above left, teal] {\textbf{Center _�→_ $C$}}; \fill[orange!90!black] (O) circle (2.5pt) node[below right, _�→_ orange!90!black] {\textbf{$O(0,0)$}}; \fill[magenta] (G) circle (2.5pt) node[above right, magenta] _�→_ {\textbf{$G(h,k)$}}; _% Wavevectors_ \draw[->, purple!80!black, ultra thick] (C) -- (O) node[midway, left] _�→_ {$\vec{k}_i$}; \draw[->, teal, ultra thick] (C) -- (G) node[midway, above] {$\vec{k} �→_ f$}; \draw[->, magenta, ultra thick] (O) -- (G) node[midway, below right] _�→_ {$\vec{G}$}; _% Crystal plane line_ \draw[gray, thick, dotted] (-0.8, 0.8) -- (0.8, -0.8) node[right, gray] _�→_ {Plane $(hkl)$}; **\end** {scope} _% --- Right Panel: 1st Brillouin Zone ---_ **\begin** {scope}[shift={(7,0)}] _% Title_ \node[align=center, font=\bfseries] at (0, 3.8) {1st Brillouin Zone _�→_ Construction \\ \small $2\vec{k}\cdot\vec{G} = G^2$}; _% Reciprocal Grid Points_ \foreach \x in {-2,-1,0,1,2} { \foreach \y in {-2,-1,0,1,2} { \fill[blue!70!black] (\x*1.4, \y*1.4) circle (1.8pt); } } _% 1st BZ Shaded Square_ \fill[teal!15] (-0.7,-0.7) rectangle (0.7,0.7); \draw[teal, ultra thick] (-0.7,-0.7) rectangle (0.7,0.7); \node[teal!80!black, font=\small] at (-0.35,-0.35) {1st BZ}; 

Notes 

6 

_% Origin \Gamma_ 

\fill[orange!90!black] (0,0) circle (2.5pt) node[below left, 

- _�→_ orange!90!black] {$\Gamma(0,0)$}; 

_% Vector G_ 

\draw[->, magenta, thick] (0,0) -- (1.4,0) node[midway, below] _�→_ {$\vec{G}$}; 

_% Bragg Plane (Bisector)_ 

- \draw[orange!80!black, dashed, line width=1.2pt] (0.7,-1.8) -- (0.7,1.8) _�→_ node[above] {Bragg Plane}; 

_% Wavevector k to BZ boundary_ 

\coordinate (K) at (0.7, 0.6); 

\draw[->, purple!80!black, ultra thick] (0,0) -- (K) node[midway, above 

_�→_ left] {$\vec{k}$}; 

\fill[purple!80!black] (K) circle (2pt); 

_% Reflected k' = k - G_ 

\draw[->, orange!90!black, thick, dashed] (K) -- (-0.7, 0.6) 

- _�→_ node[midway, above] {$\vec{k}-\vec{G}$}; 

_% Symmetry labels_ 

\node[font=\tiny] at (1.1, 0.15) {$X(\frac{\pi}{a},0)$}; 

\node[font=\tiny] at (1.1, 0.85) {$M(\frac{\pi}{a},\frac{\pi}{a})$}; **\end** {scope} 

**\end** {tikzpicture} 

\caption{Ewald Sphere construction in momentum space (left) and 1st Brillouin _�→_ Zone boundary condition for Bragg reflection (right).} 

**\end** {figure} 

**\end** {document} 

## **Key Physics Connection:** 

- **Ewald Sphere (Left):** Gives the geometric condition for diffraction in 3D reciprocal space. Whenever the sphere of radius _k_ = 2 _π_ / _λ_ touches a reciprocal lattice point _G_ , Bragg’s law _⃗kf −⃗ki_ = _⃗G_ is satisfied. 

- **Brillouin Zone (Right):** The boundaries of the 1st BZ are defined by the perpendicular bisectors of the reciprocal lattice vectors _⃗G_ , which directly satisfy the vector Bragg condition 2 _⃗k ·⃗G_ = _G_<sup>2</sup> . 

Would you like to move on to **Module 3: Free Electron Theory & Lattice Vibrations (Phonons)** next 

Notes 

7 



<!-- Start of picture text -->
Ewald Sphere Construction<br>∆ ⃗k = ⃗G<br>Center C<br>⃗kf<br>G ( h, k )<br>⃗ki<br>⃗G<br>O (0 ,  0)<br>Plane ( hkl )<br><!-- End of picture text -->



<!-- Start of picture text -->
1st Brillouin Zone Construction<br>2 ⃗k ·⃗G  =  G 2<br>Bragg Plane<br>⃗k −⃗G M ( π a , π a )<br>⃗k<br>X ( π a ,  0)<br>Γ(01st ,  0)BZ ⃗G<br><!-- End of picture text -->

**Figure 1:** Ewald Sphere construction in momentum space (left) and 1st Brillouin Zone boundary condition for Bragg reflection (right). 

