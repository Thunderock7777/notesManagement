# 04 - AI Knowledge Graph & Relational Mindmap

> [!NOTE]
> **MACHINE-READABLE CONTROL FILE**:
> This file is maintained exclusively for AI consumption, context retrieval, and relationship traversal.
> It does not contain human-facing diagrams. When the user asks about relationships, query this graph and explain in conversational text.

## Ingestion Rules
- **Source Notes**: `D:\STUDY\txt_md\` ONLY.
- **Direct PDF Imports**: `D:\STUDY\pdf\` ONLY (Verified LaTeX/digital text layers).
- **Ignore Filter**: Any file found outside authorized directories is strictly ignored and NEVER indexed.

---

## Semantic Relational Knowledge Graph

```yaml
version: '1.3'
total_nodes: 131
total_edges: 150
nodes:
- id: DOC-001
  file: qm-two-state-time-evolved-wavefunction.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Eigenstates
  summary: Write the Time-Evolved Wavefunction.
  source_note: qm-two-state-time-evolved-wavefunction.md
  section: SEC-07
  syllabus_topic: '`7.2` Time-Independent & Time-D'
- id: DOC-002
  file: qm-quantum-mechanics-gate-advanced.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Quantum Mechanics
  summary: 'GATE PHYSICS: ADVANCED QUANTUM MECHANICS.'
  source_note: qm-quantum-mechanics-gate-advanced.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of Quantum Me'
- id: DOC-003
  file: qm-parity-operator-algebraic-properties.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Parity Operator
  summary: Here is a detailed, step-by-step breakdown of the algebraic proof using operator algebra.
  source_note: qm-parity-operator-algebraic-properties.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of QM, Uncert'
- id: DOC-004
  file: qm-potential-wells-comparison-master-chart.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Potential Well
  summary: Here is a master summary chart and detailed breakdown of all major potential wells.
  source_note: qm-potential-wells-comparison-master-chart.md
  section: SEC-07
  syllabus_topic: '`7.3` One-Dimensional Potential'
- id: DOC-005
  file: nuc-liquid-drop-model-mass-formula.pdf
  source_type: surrogate_md
  domain: Nuclear & Particle Physics
  core_concepts:
  - Hydrogen Atom
  - Liquid Drop Model
  - Radioactive Decay
  summary: 'Welcome to Section 10: Nuclear and Particle Physics for GATE!.'
  source_note: nuc-liquid-drop-model-mass-formula.md
  section: SEC-10
  syllabus_topic: '`10.2` Semi-Empirical Mass Formu'
- id: DOC-006
  file: qm-ladder-operators-harmonic-oscillator.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Ladder Operators
  summary: 'Method 1: Step-by-Step Action of Ladder Operators.'
  source_note: qm-ladder-operators-harmonic-oscillator.md
  section: SEC-07
  syllabus_topic: '`7.5` Harmonic Oscillators (1D,'
- id: DOC-007
  file: qm-made-option-detailed.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Harmonic Oscillator
  - Wavefunction
  - Eigenvalues
  - Eigenstates
  summary: Check Normalization of the State.
  source_note: qm-made-option-detailed.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of Quantum Me'
- id: DOC-008
  file: qm-truncated-half-harmonic-oscillator.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Harmonic Oscillator
  - Wavefunction
  - Eigenvalues
  summary: Understand the Truncated (Half) Harmonic Oscillator Potential.
  source_note: qm-truncated-half-harmonic-oscillator.md
  section: SEC-07
  syllabus_topic: '`7.5` Harmonic Oscillators (1D,'
- id: DOC-009
  file: ssp-anisotropic-effective-masses-k-space.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Crystal Lattice
  - Brillouin Zone
  summary: To understand anisotropic effective masses, we must clarify the core geometrical language.
  source_note: ssp-anisotropic-effective-masses-k-space.md
  section: SEC-09
  syllabus_topic: '`9.6` Band Theory of Solids, Bl'
- id: DOC-010
  file: qm-spin-half-pauli-spin-matrices.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenvalues
  - Eigenstates
  - Spin-1/2
  summary: Identify the Initial Quantum State.
  source_note: qm-spin-half-pauli-spin-matrices.md
  section: SEC-07
  syllabus_topic: '`7.7` Orbital and Spin Angular'
- id: DOC-011
  file: qm-radial-wavefunction-hydrogen-atom.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Radial Wavefunction
  summary: Yes, that specific formula is strictly for R31(r), which corresponds to the 3p.
  source_note: qm-radial-wavefunction-hydrogen-atom.md
  section: SEC-07
  syllabus_topic: '`7.6` Central Potentials & Hydr'
- id: DOC-012
  file: qm-pauli-exclusion-principle-fermions.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Harmonic Oscillator
  - Wavefunction
  - Eigenvalues
  - Spin-1/2
  summary: The Pauli Exclusion Principle & Total Wavefunction.
  source_note: qm-pauli-exclusion-principle-fermions.md
  section: SEC-07
  syllabus_topic: '`7.8` Identical Particles, Paul'
- id: DOC-013
  file: qm-2d-isotropic-harmonic-oscillator.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Harmonic Oscillator
  - Eigenvalues
  summary: For a 2D Isotropic Quantum Harmonic Oscillator, the potential is V (x, y) =.
  source_note: qm-2d-isotropic-harmonic-oscillator.md
  section: SEC-07
  syllabus_topic: '`7.5` Harmonic Oscillators (1D,'
- id: DOC-014
  file: ssp-einstein-temperature-lattice-oscillations.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Crystal Lattice
  - Einstein Temperature
  summary: "When we call the Einstein Temperature (\u03B8E) the \u201Ccharacteristic thermal energy thresh-."
  source_note: ssp-einstein-temperature-lattice-oscillations.md
  section: SEC-09
  syllabus_topic: '`9.1` Crystallography, Bravais'
- id: DOC-015
  file: qm-identical-vs-distinguishable-particles.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Crystal Lattice
  summary: "It sounds like a paradox at first\u2014how can particles be identical and distinguishable."
  source_note: qm-identical-vs-distinguishable-particles.md
  section: SEC-07
  syllabus_topic: '`7.8` Identical Particles, Paul'
- id: DOC-016
  file: nuc-nuclear-shell-model-magic-numbers.pdf
  source_type: surrogate_md
  domain: Nuclear & Particle Physics
  core_concepts:
  - Nuclear Shell Model
  summary: "Nuclear and Particle Physics Study Boundary Guide (GATE Physics 2012\u2013."
  source_note: nuc-nuclear-shell-model-magic-numbers.md
  section: SEC-10
  syllabus_topic: '`10.3` Nuclear Shell Model & Mag'
- id: DOC-017
  file: qm-eigenvalues-and-eigenstates-formalism.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenvalues
  - Eigenstates
  - Pauli Matrices
  summary: Here is the step-by-step mathematical derivation for finding the eigenvalues and eigen-.
  source_note: qm-eigenvalues-and-eigenstates-formalism.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of QM, Uncert'
- id: DOC-018
  file: ssp-the-core-concept-in-classical-c.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Solid State Physics
  summary: In classical continuum physics, a solid is modeled as a continuous, homogeneous, and.
  source_note: ssp-the-core-concept-in-classical-c.md
  section: SEC-09
  syllabus_topic: '`9.1` Elements of Crystallograp'
- id: DOC-019
  file: ssp-python-code-import-os-import-ma.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Solid State Physics
  summary: Here is the complete Python script to plot and model the spherical constant-energy.
  source_note: ssp-python-code-import-os-import-ma.md
  section: SEC-09
  syllabus_topic: '`9.1` Elements of Crystallograp'
- id: DOC-020
  file: qm-3d-isotropic-harmonic-oscillator.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Harmonic Oscillator
  summary: The degeneracy of the 5th excited state is 6.
  source_note: qm-3d-isotropic-harmonic-oscillator.md
  section: SEC-07
  syllabus_topic: '`7.5` Harmonic Oscillators (1D,'
- id: DOC-021
  file: qm-degenerate-perturbation-theory.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenstates
  - Perturbation Theory
  summary: "Here is the step-by-step mathematical breakdown of why and how the 2\xD72 perturbation."
  source_note: qm-degenerate-perturbation-theory.md
  section: SEC-07
  syllabus_topic: '`7.9` Approximation Methods (Va'
- id: DOC-022
  file: ssp-ewald-brillouin.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Brillouin Zone
  - Ewald Sphere
  summary: I have generated the visual diagram for the Ewald Sphere Construction and the 1st.
  source_note: ssp-ewald-brillouin.md
  section: SEC-09
  syllabus_topic: '`9.2` Diffraction, Reciprocal L'
- id: DOC-023
  file: ssp-bloch-wavefunction-and-theorem.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Wavefunction
  - Brillouin Zone
  summary: "To see how a constant spatial phase shift \u2206\u03D5 = ka turns a periodic wave pattern into a."
  source_note: ssp-bloch-wavefunction-and-theorem.md
  section: SEC-09
  syllabus_topic: '`9.6` Band Theory of Solids, Bl'
- id: DOC-024
  file: qm-potential-wells-comparison-master-chart-2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Potential Well
  summary: Prompt for detailed syllabus.
  source_note: qm-potential-wells-comparison-master-chart-2.md
  section: SEC-07
  syllabus_topic: '`7.3` One-Dimensional Potential'
- id: DOC-025
  file: qm-spin-half-pauli-spin-matrices-2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Spin-1/2
  - Pauli Matrices
  summary: In the context of the spin problems we just solved (such as Q.
  source_note: qm-spin-half-pauli-spin-matrices-2.md
  section: SEC-07
  syllabus_topic: '`7.7` Orbital and Spin Angular'
- id: DOC-026
  file: qm-radial-probability-density-hydrogen.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Radial Wavefunction
  summary: Radial Probability Density Definition.
  source_note: qm-radial-probability-density-hydrogen.md
  section: SEC-07
  syllabus_topic: '`7.6` Central Potentials & Hydr'
- id: DOC-027
  file: nuc-nuclear-shell-model-magic-numbers-2.pdf
  source_type: surrogate_md
  domain: Nuclear & Particle Physics
  core_concepts:
  - Nuclear Shell Model
  - Liquid Drop Model
  summary: 'Phase 1: Foundational Interactions & Ground-State Nuclear Properties.'
  source_note: nuc-nuclear-shell-model-magic-numbers-2.md
  section: SEC-10
  syllabus_topic: '`10.3` Nuclear Shell Model & Mag'
- id: DOC-028
  file: qm-3d-isotropic-harmonic-oscillator-2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Harmonic Oscillator
  - Eigenvalues
  - Perturbation Theory
  summary: Energy Eigenvalues of a 3D Isotropic Quantum Harmonic Oscillator.
  source_note: qm-3d-isotropic-harmonic-oscillator-2.md
  section: SEC-07
  syllabus_topic: '`7.5` Harmonic Oscillators (1D,'
- id: DOC-029
  file: ssp-density-of-states-effective-mass.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Density of States
  summary: In anisotropic semiconductors like Silicon (Si) and Germanium (Ge), the conduction.
  source_note: ssp-density-of-states-effective-mass.md
  section: SEC-09
  syllabus_topic: '`9.5` Free Electron Theory, Ban'
- id: DOC-030
  file: ssp-lattice-basis.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Solid State Physics
  summary: The easiest way to understand the difference is through a simple formula:.
  source_note: ssp-lattice-basis.md
  section: SEC-09
  syllabus_topic: '`9.1` Crystallography, Bravais'
- id: DOC-031
  file: ssp-condition-for-the-crest-a-crest.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Solid State Physics
  summary: Here is a simple numerical example to show how tracking a constant phase allows you.
  source_note: ssp-condition-for-the-crest-a-crest.md
  section: SEC-09
  syllabus_topic: '`9.1` Elements of Crystallograp'
- id: DOC-032
  file: ssp-the-phase-shift-in-space.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Solid State Physics
  summary: 'That is a great catch! It sounds like a contradiction on the surface: how can we talk.'
  source_note: ssp-the-phase-shift-in-space.md
  section: SEC-09
  syllabus_topic: '`9.1` Elements of Crystallograp'
- id: DOC-033
  file: ssp-bloch-wavefunction-and-theorem-2.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Wavefunction
  - Eigenstates
  - Crystal Lattice
  summary: The function uk(r) (or uk(x) in 1D) is called the cell-periodic function or Bloch.
  source_note: ssp-bloch-wavefunction-and-theorem-2.md
  section: SEC-09
  syllabus_topic: '`9.6` Band Theory of Solids, Bl'
- id: DOC-034
  file: ssp-miller-indices.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Miller Indices
  summary: What are Miller Indices?.
  source_note: ssp-miller-indices.md
  section: SEC-09
  syllabus_topic: '`9.1` Crystallography, Bravais'
- id: DOC-035
  file: ssp-lau-condition.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Solid State Physics
  summary: Here is the step-by-step mathematical breakdown of how we get from the Laue condition.
  source_note: ssp-lau-condition.md
  section: SEC-09
  syllabus_topic: '`9.2` Diffraction, Reciprocal L'
- id: DOC-036
  file: qm-degenerate-perturbation-theory-2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenvalues
  - Perturbation Theory
  summary: Analyze the Unperturbed Hamiltonian (H0).
  source_note: qm-degenerate-perturbation-theory-2.md
  section: SEC-07
  syllabus_topic: '`7.9` Approximation Methods (Va'
- id: DOC-037
  file: math-cauchy-sequence.pdf
  source_type: surrogate_md
  domain: Mathematical Physics
  core_concepts:
  - Eigenstates
  - Cauchy Sequence
  summary: In plain English, a Cauchy sequence is a sequence of elements (like numbers, vectors, or.
  source_note: math-cauchy-sequence.md
  section: SEC-02
  syllabus_topic: '`2.4` Complex Analysis, Cauchy-'
- id: DOC-038
  file: qm-ladder-operators-harmonic-oscillator-2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenstates
  summary: Identify the Ladder Operator.
  source_note: qm-ladder-operators-harmonic-oscillator-2.md
  section: SEC-07
  syllabus_topic: '`7.5` Harmonic Oscillators (1D,'
- id: DOC-039
  file: nuc-the-actual-sub-topics.pdf
  source_type: surrogate_md
  domain: Nuclear & Particle Physics
  core_concepts:
  - Nuclear & Particle Physics
  summary: Analyze the selected GATE question papers for the broad subject of Atomic and Molecular.
  source_note: nuc-the-actual-sub-topics.md
  section: SEC-10
  syllabus_topic: '`10.1` Nuclear Properties & Mode'
- id: DOC-040
  file: qm-relative-global-phase.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenvalues
  - Eigenstates
  summary: "In quantum mechanics, phase refers to the complex angle \u03B8 in a term ei\u03B8."
  source_note: qm-relative-global-phase.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of QM, Uncert'
- id: DOC-041
  file: qm-perturbation-theory-energy-correction.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Perturbation Theory
  summary: 'Method 1: The Symmetry Shortcut (10-Second Method).'
  source_note: qm-perturbation-theory-energy-correction.md
  section: SEC-07
  syllabus_topic: '`7.9` Approximation Methods (Va'
- id: DOC-042
  file: qm-zeeman-effect-formulaes4.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Perturbation Theory
  summary: "What is the Magnetic Interaction Hamiltonian ( \u02C6Hmag)?."
  source_note: qm-zeeman-effect-formulaes4.md
  section: SEC-08
  syllabus_topic: '`8.4` External Field Effects (Z'
- id: DOC-043
  file: math-cauchy-sequence1.pdf
  source_type: surrogate_md
  domain: Mathematical Physics
  core_concepts:
  - Cauchy Sequence
  summary: No, if a sequence does not converge, it does NOT mean the sum converges.
  source_note: math-cauchy-sequence1.md
  section: SEC-02
  syllabus_topic: '`2.4` Complex Analysis, Cauchy-'
- id: DOC-044
  file: qm-made-option-step.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Eigenvalues
  summary: Write the Energy Eigenvalue Formula for a 2D Box.
  source_note: qm-made-option-step.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of Quantum Me'
- id: DOC-045
  file: qm-zeeman-effect-formulaes3.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenstates
  - Perturbation Theory
  summary: Here is the complete, step-by-step quantum mechanical derivation of the Anomalous.
  source_note: qm-zeeman-effect-formulaes3.md
  section: SEC-08
  syllabus_topic: '`8.4` External Field Effects (Z'
- id: DOC-046
  file: qm-pauli-exclusion-principle-fermions-2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Spin-1/2
  summary: Determine the Spin State of Ground State Helium.
  source_note: qm-pauli-exclusion-principle-fermions-2.md
  section: SEC-07
  syllabus_topic: '`7.8` Identical Particles, Paul'
- id: DOC-047
  file: ssp-dielectric-properties-of-solids.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Solid State Physics
  summary: 'Welcome to Module 5: Dielectrics, Magnetism & Superconductivity!.'
  source_note: ssp-dielectric-properties-of-solids.md
  section: SEC-09
  syllabus_topic: '`9.8` Dielectric Properties of'
- id: DOC-048
  file: qm-notebooklm-alternative.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Quantum Mechanics
  summary: If you need a completely free, cloud-based alternative that does not require a $20/month.
  source_note: qm-notebooklm-alternative.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of Quantum Me'
- id: DOC-049
  file: qm-made-option-detailed-2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Quantum Mechanics
  summary: 'Method 1: Operator Identity Expansion (Step-by-Step).'
  source_note: qm-made-option-detailed-2.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of Quantum Me'
- id: DOC-050
  file: qm-eigenvalues-and-eigenstates-formalism-2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenvalues
  - Eigenstates
  - Spin-1/2
  summary: Here is a comprehensive summary of quantum state formalism, Hilbert space structure,.
  source_note: qm-eigenvalues-and-eigenstates-formalism-2.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of QM, Uncert'
- id: DOC-051
  file: qm-spin-half-pauli-spin-matrices-3.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Spin-1/2
  summary: Quantum Coupling of Two Spin-1/2 Particles.
  source_note: qm-spin-half-pauli-spin-matrices-3.md
  section: SEC-07
  syllabus_topic: '`7.7` Orbital and Spin Angular'
- id: DOC-052
  file: ssp-a-bravais-lattice-is-purely-an.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Solid State Physics
  summary: "Yes\u2014you\u2019ve got the right idea, with one important wording tweak so it doesn\u2019t trip."
  source_note: ssp-a-bravais-lattice-is-purely-an.md
  section: SEC-09
  syllabus_topic: '`9.1` Crystallography, Bravais'
- id: DOC-053
  file: qm-evaluate-the-inner-commutator.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Quantum Mechanics
  summary: Evaluate the Inner Commutator [x, H].
  source_note: qm-evaluate-the-inner-commutator.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of QM, Uncert'
- id: DOC-054
  file: qm-degenerate-perturbation-theory-3.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenvalues
  - Perturbation Theory
  summary: 'Method 1: Degenerate Perturbation Theory.'
  source_note: qm-degenerate-perturbation-theory-3.md
  section: SEC-07
  syllabus_topic: '`7.9` Approximation Methods (Va'
- id: DOC-055
  file: qm-angular-momentum-commutation-relations.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Eigenvalues
  - Eigenstates
  - Hydrogen Atom
  summary: "3\xAFh2 (for the standard GATE question variant where the first term is \u03C8210)."
  source_note: qm-angular-momentum-commutation-relations.md
  section: SEC-07
  syllabus_topic: '`7.7` Orbital and Spin Angular'
- id: DOC-056
  file: ssp-pauli-exclusion-principle-fermions.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Potential Well
  - Crystal Lattice
  summary: "When we look at what reshapes the electron wave inside a crystal, the \u201Cpush\u201D and \u201Cpull\u201D."
  source_note: ssp-pauli-exclusion-principle-fermions.md
  section: SEC-07
  syllabus_topic: '`7.8` Identical Particles & Pau'
- id: DOC-057
  file: ssp-potential-wells-comparison-master-chart.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Wavefunction
  - Potential Well
  summary: The Kronig-Penney Model (1931) is the quintessential 1D quantum model used in.
  source_note: ssp-potential-wells-comparison-master-chart.md
  section: SEC-07
  syllabus_topic: '`7.3` One-Dimensional Potential'
- id: DOC-058
  file: qm-how-singlet-state-turns-into.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  summary: "The Rule of the Exchange Operator \u02C6P12."
  source_note: qm-how-singlet-state-turns-into.md
  section: SEC-07
  syllabus_topic: '`7.8` Identical Particles, Paul'
- id: DOC-059
  file: nuc-radial-probability-density-hydrogen.pdf
  source_type: surrogate_md
  domain: Nuclear & Particle Physics
  core_concepts:
  - Wavefunction
  - Eigenvalues
  - Hydrogen Atom
  - Potential Well
  summary: A particle of mass m is confined in a two-dimensional square well potential of dimension.
  source_note: nuc-radial-probability-density-hydrogen.md
  section: SEC-07
  syllabus_topic: '`7.6` Central Potentials & Hydr'
- id: DOC-060
  file: qm-perturbation-theory-energy-correction-2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenvalues
  - Perturbation Theory
  summary: Identify the Degenerate Subspace.
  source_note: qm-perturbation-theory-energy-correction-2.md
  section: SEC-07
  syllabus_topic: '`7.9` Approximation Methods (Va'
- id: DOC-061
  file: ssp-density-of-states-effective-mass-2.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Crystal Lattice
  summary: In solid-state physics, when we talk about mass inside a crystal lattice, we are referring.
  source_note: ssp-density-of-states-effective-mass-2.md
  section: SEC-09
  syllabus_topic: '`9.5` Free Electron Theory, Ban'
- id: DOC-062
  file: qm-parity-operator-algebraic-properties-2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Eigenvalues
  - Parity Operator
  summary: "The Parity Operator \u02C6P (also written as \u02C6\u03A0) performs a spatial reflection about the."
  source_note: qm-parity-operator-algebraic-properties-2.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of QM, Uncert'
- id: DOC-063
  file: qm-spin-half-pauli-spin-matrices-4.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenvalues
  - Spin-1/2
  summary: Here is the step-by-step mathematical proof explaining why and how finding E2 allows.
  source_note: qm-spin-half-pauli-spin-matrices-4.md
  section: SEC-07
  syllabus_topic: '`7.7` Orbital and Spin Angular'
- id: DOC-064
  file: qm-pauli-exclusion-principle-fermions-3.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Spin-1/2
  summary: '(Note: With full normalization, the overall prefactor is.'
  source_note: qm-pauli-exclusion-principle-fermions-3.md
  section: SEC-07
  syllabus_topic: '`7.8` Identical Particles, Paul'
- id: DOC-065
  file: qm-3d-isotropic-harmonic-oscillator-3.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Harmonic Oscillator
  - Wavefunction
  summary: The full wavefunction for a 1D Quantum Simple Harmonic Oscillator consists of a.
  source_note: qm-3d-isotropic-harmonic-oscillator-3.md
  section: SEC-07
  syllabus_topic: '`7.5` Harmonic Oscillators (1D,'
- id: DOC-066
  file: ssp-the-rule-for-a-bravais-lattice.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Solid State Physics
  summary: "No \u2014 graphene\u2019s honeycomb arrangement of carbon atoms is NOT a Bravais."
  source_note: ssp-the-rule-for-a-bravais-lattice.md
  section: SEC-09
  syllabus_topic: '`9.1` Crystallography, Bravais'
- id: DOC-067
  file: qm-radial-probability-density-hydrogen-2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Hydrogen Atom
  - Radial Wavefunction
  summary: Ground State Wavefunction of the Hydrogen Atom.
  source_note: qm-radial-probability-density-hydrogen-2.md
  section: SEC-07
  syllabus_topic: '`7.6` Central Potentials & Hydr'
- id: DOC-068
  file: qm-abc.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Quantum Mechanics
  summary: "Let\u2019s slow down completely and build this step-by-step from absolute first principles."
  source_note: qm-abc.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of Quantum Me'
- id: DOC-069
  file: ssp-wigner-seitz-primitive-cell.pdf
  source_type: txt_md
  source_note: ssp-wigner-seitz-primitive-cell.txt
  domain: Solid State Physics
  core_concepts:
  - Wigner-Seitz Cell
  - Primitive vs Conventional Unit Cells
  - Brillouin Zone
  - Metallic Cohesive Energy
  summary: Rigorous derivation of primitive and conventional unit cells, Wigner-Seitz polyhedra, and quantum boundary conditions.
  section: SEC-09
  syllabus_topic: '`9.1` Crystallography, Bravais'
- id: DOC-070
  file: ssp-ssp35.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Phonons
  - Debye Model
  - Density of States
  summary: The Debye Model (proposed by Peter Debye in 1912) is the complete quantum-.
  source_note: ssp-ssp35.md
  section: SEC-09
  syllabus_topic: '`9.1` Elements of Crystallograp'
- id: DOC-071
  file: qm-part1-lect.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Harmonic Oscillator
  - Perturbation Theory
  summary: Statistical Mechanics of Interacting Systems.
  source_note: qm-part1-lect.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of Quantum Me'
- id: DOC-072
  file: qm-attenuation-constant.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  summary: Standard Formula & Direct Answer.
  source_note: qm-attenuation-constant.md
  section: SEC-07
  syllabus_topic: '`7.3` One-Dimensional Potential'
- id: DOC-073
  file: qm-degenerate-perturbation-theory-4.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenvalues
  - Perturbation Theory
  summary: 'That is a very perceptive question! The short answer is: Finding the eigenvalues of a.'
  source_note: qm-degenerate-perturbation-theory-4.md
  section: SEC-07
  syllabus_topic: '`7.9` Approximation Methods (Va'
- id: DOC-074
  file: qm-hilbert-space.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Harmonic Oscillator
  - Eigenstates
  - Hydrogen Atom
  - Potential Well
  summary: "To understand what a Hilbert space is, let\u2019s start with a plain-English picture before."
  source_note: qm-hilbert-space.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of QM, Uncert'
- id: DOC-075
  file: ssp-first-brillouin-zone-construction.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Brillouin Zone
  summary: Here is a complete, self-contained Python script to plot both fundamental graphs of the.
  source_note: ssp-first-brillouin-zone-construction.md
  section: SEC-09
  syllabus_topic: '`9.2` Diffraction, Reciprocal L'
- id: DOC-076
  file: qm-bohr-energy-level-formula-for-h.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenvalues
  - Hydrogen Atom
  summary: Bohr Energy Level Formula for Hydrogen.
  source_note: qm-bohr-energy-level-formula-for-h.md
  section: SEC-07
  syllabus_topic: '`7.6` Central Potentials & Hydr'
- id: DOC-077
  file: qm-eigenstate.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenvalues
  - Eigenstates
  summary: In quantum mechanics, the difference between an eigenstate and any state (a general.
  source_note: qm-eigenstate.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of QM, Uncert'
- id: DOC-078
  file: qm-definition-of-electric-dipole-m.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Hydrogen Atom
  summary: Definition of Electric Dipole Moment Operator.
  source_note: qm-definition-of-electric-dipole-m.md
  section: SEC-08
  syllabus_topic: '`8.5` Electric Dipole Transitio'
- id: DOC-079
  file: qm-made-option-detailed-3.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenvalues
  summary: "Write the Time-Evolved State |\u03C8(t)\u27E9."
  source_note: qm-made-option-detailed-3.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of Quantum Me'
- id: DOC-080
  file: qm-potential-wells-comparison-master-chart-3.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Potential Well
  summary: Prompt for subtopics:.
  source_note: qm-potential-wells-comparison-master-chart-3.md
  section: SEC-07
  syllabus_topic: '`7.3` One-Dimensional Potential'
- id: DOC-081
  file: qm-eigenvalues-and-eigenstates-formalism-3.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenvalues
  summary: Understand the Matrix Structure.
  source_note: qm-eigenvalues-and-eigenstates-formalism-3.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of QM, Uncert'
- id: DOC-082
  file: qm-syllabus.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Harmonic Oscillator
  - Eigenvalues
  - Perturbation Theory
  - Nuclear Shell Model
  summary: IIT Madras  | Organizing Institute.
  source_note: qm-syllabus.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of Quantum Me'
- id: DOC-083
  file: ssp-miller-indices1.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Crystal Lattice
  - Miller Indices
  summary: When we talk about a set of parallel planes in crystallography, a common question.
  source_note: ssp-miller-indices1.md
  section: SEC-09
  syllabus_topic: '`9.1` Crystallography, Bravais'
- id: DOC-084
  file: math-cauchy-sequence2.pdf
  source_type: surrogate_md
  domain: Mathematical Physics
  core_concepts:
  - Cauchy Sequence
  summary: 'What I meant by that statement is a simple geometric fact: if two points are both.'
  source_note: math-cauchy-sequence2.md
  section: SEC-02
  syllabus_topic: '`2.4` Complex Analysis, Cauchy-'
- id: DOC-085
  file: qm-definition-of-the-density-matri.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Quantum Mechanics
  summary: Definition of the Density Matrix for a Mixed State.
  source_note: qm-definition-of-the-density-matri.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of Quantum Me'
- id: DOC-086
  file: qm-identical-vs-distinguishable-particles-2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Spin-1/2
  summary: Single-Particle Hilbert Space Dimension.
  source_note: qm-identical-vs-distinguishable-particles-2.md
  section: SEC-07
  syllabus_topic: '`7.8` Identical Particles, Paul'
- id: DOC-087
  file: qm-perturbation-theory-energy-correction-3.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Perturbation Theory
  - Zeeman Effect
  summary: Here is a master summary chart and detailed breakdown comparing Non-Degenerate.
  source_note: qm-perturbation-theory-energy-correction-3.md
  section: SEC-07
  syllabus_topic: '`7.9` Approximation Methods (Va'
- id: DOC-088
  file: nuc-zeeman-effect-energy-level-splitting.pdf
  source_type: surrogate_md
  domain: Nuclear & Particle Physics
  core_concepts:
  - Zeeman Effect
  summary: "Atomic and Molecular Physics Study Boundary Guide (GATE Physics 2012\u2013."
  source_note: nuc-zeeman-effect-energy-level-splitting.md
  section: SEC-08
  syllabus_topic: '`8.4` External Field Effects (Z'
- id: DOC-089
  file: ssp-wigner-seitz-primitive-cell-2.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Potential Well
  - Brillouin Zone
  - Miller Indices
  - Ewald Sphere
  summary: 'Phase 1: Real-Space Crystal Geometry & Interatomic Binding.'
  source_note: ssp-wigner-seitz-primitive-cell-2.md
  section: SEC-09
  syllabus_topic: '`9.1` Crystallography, Bravais'
- id: DOC-090
  file: ssp-potential-wells-comparison-master-chart-2.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Wavefunction
  - Potential Well
  - Crystal Lattice
  summary: 'Welcome to Module 4: Band Theory & Semiconductor Physics!.'
  source_note: ssp-potential-wells-comparison-master-chart-2.md
  section: SEC-07
  syllabus_topic: '`7.3` One-Dimensional Potential'
- id: DOC-091
  file: ssp-einstein-temperature-lattice-oscillations-2.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Harmonic Oscillator
  - Phonons
  - Einstein Temperature
  summary: The Einstein Model of Heat Capacity (1907) was a groundbreaking triumph because.
  source_note: ssp-einstein-temperature-lattice-oscillations-2.md
  section: SEC-09
  syllabus_topic: '`9.1` Crystallography, Bravais'
- id: DOC-092
  file: qm-potential-wells-comparison-master-chart-4.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Hydrogen Atom
  - Potential Well
  summary: For any power-law potential of the form V (r) = ark (or V (x) = axk in 1D), the General.
  source_note: qm-potential-wells-comparison-master-chart-4.md
  section: SEC-07
  syllabus_topic: '`7.3` One-Dimensional Potential'
- id: DOC-093
  file: qm-perturbation-theory-energy-correction-4.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Perturbation Theory
  summary: 'Method 1: The 10-Second Symmetry Shortcut.'
  source_note: qm-perturbation-theory-energy-correction-4.md
  section: SEC-07
  syllabus_topic: '`7.9` Approximation Methods (Va'
- id: DOC-094
  file: ssp-made-represents-number.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Solid State Physics
  summary: Yes, p represents the number of atoms in the primitive unit cell (the primitive.
  source_note: ssp-made-represents-number.md
  section: SEC-09
  syllabus_topic: '`9.1` Elements of Crystallograp'
- id: DOC-095
  file: qm-pauli-exclusion-principle-fermions-4.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Spin-1/2
  summary: "\u2022 Total Ground-State Energy (Etotal): 24 (in units of."
  source_note: qm-pauli-exclusion-principle-fermions-4.md
  section: SEC-07
  syllabus_topic: '`7.8` Identical Particles, Paul'
- id: DOC-096
  file: ssp-definitions-of-the-two-operator.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Wavefunction
  - Crystal Lattice
  summary: "To see why the crystal Hamiltonian \u02C6H commutes with the lattice translation operator \u02C6Ta,."
  source_note: ssp-definitions-of-the-two-operator.md
  section: SEC-09
  syllabus_topic: '`9.1` Elements of Crystallograp'
- id: DOC-097
  file: qm-3d-isotropic-harmonic-oscillator-4.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Harmonic Oscillator
  - Eigenvalues
  summary: Using the Virial Theorem (Fastest Method).
  source_note: qm-3d-isotropic-harmonic-oscillator-4.md
  section: SEC-07
  syllabus_topic: '`7.5` Harmonic Oscillators (1D,'
- id: DOC-098
  file: ssp-reciprocal-lattice-vectors-properties.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Crystal Lattice
  - Brillouin Zone
  - Miller Indices
  - Density of States
  summary: Here is a complete, step-by-step master roadmap for Solid State Physics tailored for.
  source_note: ssp-reciprocal-lattice-vectors-properties.md
  section: SEC-09
  syllabus_topic: '`9.1` Crystallography, Bravais'
- id: DOC-099
  file: qm-radial-wavefunction-hydrogen-atom-2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Hydrogen Atom
  - Radial Wavefunction
  summary: Quantum Numbers for the 3p Orbital.
  source_note: qm-radial-wavefunction-hydrogen-atom-2.md
  section: SEC-07
  syllabus_topic: '`7.6` Central Potentials & Hydr'
- id: DOC-100
  file: qm-perturbation-theory-energy-correction-5.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Perturbation Theory
  summary: Matrix Element Operator in Spherical Coordinates.
  source_note: qm-perturbation-theory-energy-correction-5.md
  section: SEC-07
  syllabus_topic: '`7.9` Approximation Methods (Va'
- id: DOC-101
  file: qm-spin-half-pauli-spin-matrices-5.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenstates
  - Spin-1/2
  summary: Represent the State Vector in Spinor Basis.
  source_note: qm-spin-half-pauli-spin-matrices-5.md
  section: SEC-07
  syllabus_topic: '`7.7` Orbital and Spin Angular'
- id: DOC-102
  file: qm-definition-of-a-hermitian-opera.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  summary: Definition of a Hermitian Operator.
  source_note: qm-definition-of-a-hermitian-opera.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of QM, Uncert'
- id: DOC-103
  file: ssp-pauli-exclusion-principle-fermions-2.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Solid State Physics
  summary: "\u2022 \xAFE0 (or \u27E8E\u27E90): The mean (average) energy per electron at absolute zero tem-."
  source_note: ssp-pauli-exclusion-principle-fermions-2.md
  section: SEC-07
  syllabus_topic: '`7.8` Identical Particles & Pau'
- id: DOC-104
  file: qm-zeeman-effect-energy-level-splitting.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenvalues
  - Zeeman Effect
  summary: 'Method 1: Pauli Vector Identity (Direct Operator Method).'
  source_note: qm-zeeman-effect-energy-level-splitting.md
  section: SEC-08
  syllabus_topic: '`8.4` External Field Effects (Z'
- id: DOC-105
  file: ssp-reciprocal-lattice-vectors-properties-2.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Crystal Lattice
  - Brillouin Zone
  - Miller Indices
  - Ewald Sphere
  summary: 'Welcome to Module 2: Reciprocal Lattice & Wave Diffraction!.'
  source_note: ssp-reciprocal-lattice-vectors-properties-2.md
  section: SEC-09
  syllabus_topic: '`9.1` Crystallography, Bravais'
- id: DOC-106
  file: qm-multiple-eigenvalues-eigenstates-comp.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Eigenvalues
  - Eigenstates
  - Zeeman Effect
  summary: No, having multiple eigenstates and having multiple eigenvalues are NOT the.
  source_note: qm-multiple-eigenvalues-eigenstates-comp.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of QM, Uncert'
- id: DOC-108
  file: qm-pauli-exclusion-principle-fermions-5.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Harmonic Oscillator
  - Eigenvalues
  summary: 'Phase 1: The Crisis (The Foundation).'
  source_note: qm-pauli-exclusion-principle-fermions-5.md
  section: SEC-07
  syllabus_topic: '`7.8` Identical Particles, Paul'
- id: DOC-109
  file: stat-thermodynamics-and-statistical-mechanics.pdf
  source_type: surrogate_md
  domain: Thermodynamics & Statistical Mechanics
  core_concepts:
  - Thermodynamics & Statistical Mechanics
  summary: THERMODYNAMICS & PHASE TRANSITIONS.
  source_note: stat-thermodynamics-and-statistical-mechanics.md
  section: SEC-04
  syllabus_topic: '`4.4` Classical and Quantum Sta'
- id: DOC-110
  file: ssp-python-visualization-code-impor.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Solid State Physics
  summary: Here is a complete, publication-quality Python script that models and visualizes the 6.
  source_note: ssp-python-visualization-code-impor.md
  section: SEC-09
  syllabus_topic: '`9.1` Elements of Crystallograp'
- id: DOC-111
  file: qm-zeeman-effect-formulaes1.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Quantum Mechanics
  summary: "Here is the step-by-step algebraic breakdown of HOW we arrive at \u2206E = ml\xB5BB."
  source_note: qm-zeeman-effect-formulaes1.md
  section: SEC-08
  syllabus_topic: '`8.4` External Field Effects (Z'
- id: DOC-112
  file: qm-radial-probability-density-hydrogen-3.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Hydrogen Atom
  - Radial Wavefunction
  summary: 'Quantum Spatial Architecture of the Hydrogen Atom: Ground and Excited.'
  source_note: qm-radial-probability-density-hydrogen-3.md
  section: SEC-07
  syllabus_topic: '`7.6` Central Potentials & Hydr'
- id: DOC-113
  file: qm-3d-cubic-box-energy-degeneracy.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Eigenvalues
  summary: Energy Expression for a 3D Cubic Box.
  source_note: qm-3d-cubic-box-energy-degeneracy.md
  section: SEC-07
  syllabus_topic: '`7.3` One-Dimensional Potential'
- id: DOC-114
  file: qm-radial-probability-density-hydrogen-4.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Radial Wavefunction
  summary: Yes, absolutely! There are exact general formulas for any principal quantum number n.
  source_note: qm-radial-probability-density-hydrogen-4.md
  section: SEC-07
  syllabus_topic: '`7.6` Central Potentials & Hydr'
- id: DOC-115
  file: qm-determine-the-well-boundaries-a.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  summary: Determine the Well Boundaries and Width.
  source_note: qm-determine-the-well-boundaries-a.md
  section: SEC-07
  syllabus_topic: '`7.3` One-Dimensional Potential'
- id: DOC-116
  file: qm-zeeman-effect-formulaes2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Perturbation Theory
  - Zeeman Effect
  summary: "In the case of the Zeeman effect, the energy shift \u2206E is precisely the additional mag-."
  source_note: qm-zeeman-effect-formulaes2.md
  section: SEC-08
  syllabus_topic: '`8.4` External Field Effects (Z'
- id: DOC-117
  file: qm-angular-momentum-commutation-relations-2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Quantum Mechanics
  summary: "What is \u201CSmall l\u201D? (Orbital Angular Momentum Quantum Number)."
  source_note: qm-angular-momentum-commutation-relations-2.md
  section: SEC-07
  syllabus_topic: '`7.7` Orbital and Spin Angular'
- id: DOC-118
  file: qm-angular-momentum-commutation-relations-3.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Hydrogen Atom
  summary: 'Method 1: Symmetry & Expectation Values (The 15-Second GATE Shortcut).'
  source_note: qm-angular-momentum-commutation-relations-3.md
  section: SEC-07
  syllabus_topic: '`7.7` Orbital and Spin Angular'
- id: DOC-119
  file: qm-set-up-the-wavefunction.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  summary: Here is the step-by-step mathematical proof showing that the probability of finding a.
  source_note: qm-set-up-the-wavefunction.md
  section: SEC-07
  syllabus_topic: '`7.2` Time-Independent & Time-D'
- id: DOC-120
  file: ssp-g-hkl-dbt.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Solid State Physics
  summary: To clear up this confusion, it helps to distinguish between a plane and a vector:.
  source_note: ssp-g-hkl-dbt.md
  section: SEC-09
  syllabus_topic: '`9.2` Diffraction, Reciprocal L'
- id: DOC-121
  file: ssp-bloch-wavefunction-and-theorem-3.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Wavefunction
  - Crystal Lattice
  - Brillouin Zone
  summary: In physics and engineering, modulation simply means altering or shaping the am-.
  source_note: ssp-bloch-wavefunction-and-theorem-3.md
  section: SEC-09
  syllabus_topic: '`9.6` Band Theory of Solids, Bl'
- id: DOC-122
  file: nuc-deuteron-bound-state-nuclear-force.pdf
  source_type: surrogate_md
  domain: Nuclear & Particle Physics
  core_concepts:
  - Nuclear & Particle Physics
  summary: "The decay process e\u2212+ p \u2192e\u2212+ p + \u03BD + \xAF\u03BD violates."
  source_note: nuc-deuteron-bound-state-nuclear-force.md
  section: SEC-10
  syllabus_topic: '`10.4` Nuclear Force & Two-Nucle'
- id: DOC-123
  file: stat-multiple-eigenstates.pdf
  source_type: surrogate_md
  domain: Thermodynamics & Statistical Mechanics
  core_concepts:
  - Wavefunction
  - Eigenvalues
  - Eigenstates
  - Zeeman Effect
  summary: In quantum mechanics, multiple eigenstates appear in two distinct physical situations:.
  source_note: stat-multiple-eigenstates.md
  section: SEC-04
  syllabus_topic: '`4.4` Classical and Quantum Sta'
- id: DOC-124
  file: nuc-zeeman-effect-energy-level-splitting-2.pdf
  source_type: surrogate_md
  domain: Nuclear & Particle Physics
  core_concepts:
  - Zeeman Effect
  summary: The ground state of sodium atom (11Na) is a 2S1/2 state.
  source_note: nuc-zeeman-effect-energy-level-splitting-2.md
  section: SEC-08
  syllabus_topic: '`8.4` External Field Effects (Z'
- id: DOC-125
  file: qm-zeeman-effect-energy-level-splitting-2.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Zeeman Effect
  summary: 'Master Comparison Table: Atomic Field Effects & Selection Rules.'
  source_note: qm-zeeman-effect-energy-level-splitting-2.md
  section: SEC-08
  syllabus_topic: '`8.4` External Field Effects (Z'
- id: DOC-126
  file: qm-ladder-operators-harmonic-oscillator-3.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Harmonic Oscillator
  - Perturbation Theory
  - Ladder Operators
  summary: First-Order Perturbation Theory Formula.
  source_note: qm-ladder-operators-harmonic-oscillator-3.md
  section: SEC-07
  syllabus_topic: '`7.5` Harmonic Oscillators (1D,'
- id: DOC-127
  file: ssp-the-golden-rule-of-the-translat.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Wavefunction
  summary: "The second term V (x + a)\u03C8(x + a) comes directly from how the Translation Operator."
  source_note: ssp-the-golden-rule-of-the-translat.md
  section: SEC-09
  syllabus_topic: '`9.1` Elements of Crystallograp'
- id: DOC-128
  file: qm-spin-half-pauli-spin-matrices-6.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Wavefunction
  - Spin-1/2
  summary: Yes, you are completely right to raise this! The overall requirement for symmetry depends.
  source_note: qm-spin-half-pauli-spin-matrices-6.md
  section: SEC-07
  syllabus_topic: '`7.7` Orbital and Spin Angular'
- id: DOC-129
  file: qm-multiple-eigenvalues.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Harmonic Oscillator
  - Wavefunction
  - Eigenvalues
  - Hydrogen Atom
  summary: Multiple distinct energy eigenvalues (E1, E2, E3,.
  source_note: qm-multiple-eigenvalues.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of QM, Uncert'
- id: DOC-130
  file: qm-parity-operator-algebraic-properties-3.pdf
  source_type: surrogate_md
  domain: Quantum Mechanics
  core_concepts:
  - Harmonic Oscillator
  - Wavefunction
  - Eigenvalues
  - Spin-1/2
  summary: "Quantum Mechanics Study Boundary Guide (GATE Physics 2012\u20132018)."
  source_note: qm-parity-operator-algebraic-properties-3.md
  section: SEC-07
  syllabus_topic: '`7.1` Foundations of QM, Uncert'
- id: DOC-131
  file: ssp-first-brillouin-zone-construction-2.pdf
  source_type: surrogate_md
  domain: Solid State Physics
  core_concepts:
  - Crystal Lattice
  - Brillouin Zone
  - Phonons
  - Density of States
  summary: 'Welcome to Module 3: Free Electron Theory & Lattice Vibrations (Phonons).'
  source_note: ssp-first-brillouin-zone-construction-2.md
  section: SEC-09
  syllabus_topic: '`9.2` Diffraction, Reciprocal L'
- id: DOC-132
  file: ssp-graphene-two-atom-basis-crystal-structure.pdf
  source_type: txt_md
  domain: Solid State Physics
  core_concepts:
  - Bravais Lattice
  - Crystal Structure
  - Graphene Honeycomb
  - Two-Atom Basis
  summary: Distinction between pure Bravais lattices and crystal structures with a two-atom basis (Crystal = Lattice + Basis), covering graphene, diamond, HCP, and optical phonons.
  source_note: ssp-graphene-two-atom-basis-crystal-structure.txt
  prerequisites:
  - DOC-066
  section: SEC-09
  syllabus_topic: '`9.1` Elements of Crystallograp'
edges:
- from: DOC-001
  to: DOC-007
  relation: shares Eigenstates
- from: DOC-001
  to: DOC-008
  relation: shares Wavefunction
- from: DOC-001
  to: DOC-010
  relation: shares Eigenstates
- from: DOC-007
  to: DOC-008
  relation: shares Eigenvalues
- from: DOC-007
  to: DOC-010
  relation: shares Eigenvalues
- from: DOC-007
  to: DOC-011
  relation: shares Wavefunction
- from: DOC-007
  to: DOC-012
  relation: shares Eigenvalues
- from: DOC-007
  to: DOC-013
  relation: shares Eigenvalues
- from: DOC-007
  to: DOC-015
  relation: shares Wavefunction
- from: DOC-008
  to: DOC-010
  relation: shares Eigenvalues
- from: DOC-008
  to: DOC-011
  relation: shares Wavefunction
- from: DOC-008
  to: DOC-012
  relation: shares Eigenvalues
- from: DOC-008
  to: DOC-013
  relation: shares Eigenvalues
- from: DOC-008
  to: DOC-015
  relation: shares Wavefunction
- from: DOC-008
  to: DOC-017
  relation: shares Eigenvalues
- from: DOC-009
  to: DOC-014
  relation: shares Crystal Lattice
- from: DOC-010
  to: DOC-012
  relation: shares Eigenvalues
- from: DOC-010
  to: DOC-013
  relation: shares Eigenvalues
- from: DOC-010
  to: DOC-017
  relation: shares Eigenvalues
- from: DOC-011
  to: DOC-012
  relation: shares Wavefunction
- from: DOC-011
  to: DOC-015
  relation: shares Wavefunction
- from: DOC-012
  to: DOC-013
  relation: shares Eigenvalues
- from: DOC-012
  to: DOC-015
  relation: shares Wavefunction
- from: DOC-012
  to: DOC-017
  relation: shares Eigenvalues
- from: DOC-012
  to: DOC-020
  relation: shares Harmonic Oscillator
- from: DOC-013
  to: DOC-017
  relation: shares Eigenvalues
- from: DOC-013
  to: DOC-020
  relation: shares Harmonic Oscillator
- from: DOC-017
  to: DOC-021
  relation: shares Eigenstates
- from: DOC-017
  to: DOC-025
  relation: shares Pauli Matrices
- from: DOC-018
  to: DOC-019
  relation: shares Solid State Physics
- from: DOC-020
  to: DOC-028
  relation: shares Harmonic Oscillator
- from: DOC-021
  to: DOC-028
  relation: shares Perturbation Theory
- from: DOC-022
  to: DOC-023
  relation: shares Brillouin Zone
- from: DOC-028
  to: DOC-036
  relation: shares Eigenvalues
- from: DOC-030
  to: DOC-031
  relation: shares Solid State Physics
- from: DOC-030
  to: DOC-032
  relation: shares Solid State Physics
- from: DOC-030
  to: DOC-035
  relation: shares Solid State Physics
- from: DOC-031
  to: DOC-032
  relation: shares Solid State Physics
- from: DOC-031
  to: DOC-035
  relation: shares Solid State Physics
- from: DOC-032
  to: DOC-035
  relation: shares Solid State Physics
- from: DOC-036
  to: DOC-040
  relation: shares Eigenvalues
- from: DOC-036
  to: DOC-041
  relation: shares Perturbation Theory
- from: DOC-036
  to: DOC-042
  relation: shares Perturbation Theory
- from: DOC-036
  to: DOC-044
  relation: shares Eigenvalues
- from: DOC-036
  to: DOC-045
  relation: shares Perturbation Theory
- from: DOC-037
  to: DOC-043
  relation: shares Cauchy Sequence
- from: DOC-038
  to: DOC-040
  relation: shares Eigenstates
- from: DOC-038
  to: DOC-045
  relation: shares Eigenstates
- from: DOC-040
  to: DOC-044
  relation: shares Eigenvalues
- from: DOC-040
  to: DOC-045
  relation: shares Eigenstates
- from: DOC-041
  to: DOC-042
  relation: shares Perturbation Theory
- from: DOC-041
  to: DOC-044
  relation: shares Wavefunction
- from: DOC-041
  to: DOC-045
  relation: shares Perturbation Theory
- from: DOC-041
  to: DOC-046
  relation: shares Wavefunction
- from: DOC-042
  to: DOC-044
  relation: shares Wavefunction
- from: DOC-042
  to: DOC-045
  relation: shares Perturbation Theory
- from: DOC-042
  to: DOC-046
  relation: shares Wavefunction
- from: DOC-042
  to: DOC-051
  relation: shares Wavefunction
- from: DOC-044
  to: DOC-046
  relation: shares Wavefunction
- from: DOC-044
  to: DOC-050
  relation: shares Eigenvalues
- from: DOC-044
  to: DOC-051
  relation: shares Wavefunction
- from: DOC-045
  to: DOC-050
  relation: shares Eigenstates
- from: DOC-045
  to: DOC-054
  relation: shares Perturbation Theory
- from: DOC-046
  to: DOC-050
  relation: shares Spin-1/2
- from: DOC-046
  to: DOC-051
  relation: shares Wavefunction
- from: DOC-046
  to: DOC-055
  relation: shares Wavefunction
- from: DOC-047
  to: DOC-052
  relation: shares Solid State Physics
- from: DOC-048
  to: DOC-049
  relation: shares Quantum Mechanics
- from: DOC-048
  to: DOC-053
  relation: shares Quantum Mechanics
- from: DOC-049
  to: DOC-053
  relation: shares Quantum Mechanics
- from: DOC-050
  to: DOC-051
  relation: shares Spin-1/2
- from: DOC-050
  to: DOC-054
  relation: shares Eigenvalues
- from: DOC-050
  to: DOC-055
  relation: shares Eigenvalues
- from: DOC-051
  to: DOC-055
  relation: shares Wavefunction
- from: DOC-051
  to: DOC-058
  relation: shares Wavefunction
- from: DOC-054
  to: DOC-055
  relation: shares Eigenvalues
- from: DOC-054
  to: DOC-060
  relation: shares Eigenvalues
- from: DOC-054
  to: DOC-062
  relation: shares Eigenvalues
- from: DOC-054
  to: DOC-063
  relation: shares Eigenvalues
- from: DOC-055
  to: DOC-058
  relation: shares Wavefunction
- from: DOC-055
  to: DOC-060
  relation: shares Eigenvalues
- from: DOC-055
  to: DOC-062
  relation: shares Eigenvalues
- from: DOC-055
  to: DOC-063
  relation: shares Eigenvalues
- from: DOC-055
  to: DOC-064
  relation: shares Wavefunction
- from: DOC-056
  to: DOC-057
  relation: shares Potential Well
- from: DOC-056
  to: DOC-061
  relation: shares Crystal Lattice
- from: DOC-058
  to: DOC-062
  relation: shares Wavefunction
- from: DOC-058
  to: DOC-064
  relation: shares Wavefunction
- from: DOC-058
  to: DOC-065
  relation: shares Wavefunction
- from: DOC-058
  to: DOC-067
  relation: shares Wavefunction
- from: DOC-060
  to: DOC-062
  relation: shares Eigenvalues
- from: DOC-060
  to: DOC-063
  relation: shares Eigenvalues
- from: DOC-062
  to: DOC-063
  relation: shares Eigenvalues
- from: DOC-062
  to: DOC-064
  relation: shares Wavefunction
- from: DOC-062
  to: DOC-065
  relation: shares Wavefunction
- from: DOC-062
  to: DOC-067
  relation: shares Wavefunction
- from: DOC-063
  to: DOC-064
  relation: shares Spin-1/2
- from: DOC-064
  to: DOC-065
  relation: shares Wavefunction
- from: DOC-064
  to: DOC-067
  relation: shares Wavefunction
- from: DOC-064
  to: DOC-072
  relation: shares Wavefunction
- from: DOC-065
  to: DOC-067
  relation: shares Wavefunction
- from: DOC-065
  to: DOC-071
  relation: shares Harmonic Oscillator
- from: DOC-065
  to: DOC-072
  relation: shares Wavefunction
- from: DOC-065
  to: DOC-074
  relation: shares Harmonic Oscillator
- from: DOC-067
  to: DOC-072
  relation: shares Wavefunction
- from: DOC-067
  to: DOC-074
  relation: shares Hydrogen Atom
- from: DOC-067
  to: DOC-076
  relation: shares Hydrogen Atom
- from: DOC-069
  to: DOC-075
  relation: shares Brillouin Zone
- from: DOC-071
  to: DOC-073
  relation: shares Perturbation Theory
- from: DOC-071
  to: DOC-074
  relation: shares Harmonic Oscillator
- from: DOC-072
  to: DOC-078
  relation: shares Wavefunction
- from: DOC-073
  to: DOC-076
  relation: shares Eigenvalues
- from: DOC-073
  to: DOC-077
  relation: shares Eigenvalues
- from: DOC-073
  to: DOC-079
  relation: shares Eigenvalues
- from: DOC-073
  to: DOC-081
  relation: shares Eigenvalues
- from: DOC-073
  to: DOC-082
  relation: shares Eigenvalues
- from: DOC-074
  to: DOC-076
  relation: shares Hydrogen Atom
- from: DOC-074
  to: DOC-077
  relation: shares Eigenstates
- from: DOC-074
  to: DOC-078
  relation: shares Hydrogen Atom
- from: DOC-074
  to: DOC-080
  relation: shares Potential Well
- from: DOC-074
  to: DOC-082
  relation: shares Harmonic Oscillator
- from: DOC-076
  to: DOC-077
  relation: shares Eigenvalues
- from: DOC-076
  to: DOC-078
  relation: shares Hydrogen Atom
- from: DOC-076
  to: DOC-079
  relation: shares Eigenvalues
- from: DOC-076
  to: DOC-081
  relation: shares Eigenvalues
- from: DOC-076
  to: DOC-082
  relation: shares Eigenvalues
- from: DOC-077
  to: DOC-079
  relation: shares Eigenvalues
- from: DOC-077
  to: DOC-081
  relation: shares Eigenvalues
- from: DOC-077
  to: DOC-082
  relation: shares Eigenvalues
- from: DOC-079
  to: DOC-081
  relation: shares Eigenvalues
- from: DOC-079
  to: DOC-082
  relation: shares Eigenvalues
- from: DOC-081
  to: DOC-082
  relation: shares Eigenvalues
- from: DOC-082
  to: DOC-087
  relation: shares Perturbation Theory
- from: DOC-083
  to: DOC-089
  relation: shares Miller Indices
- from: DOC-083
  to: DOC-090
  relation: shares Crystal Lattice
- from: DOC-086
  to: DOC-095
  relation: shares Spin-1/2
- from: DOC-087
  to: DOC-093
  relation: shares Perturbation Theory
- from: DOC-089
  to: DOC-090
  relation: shares Potential Well
- from: DOC-089
  to: DOC-098
  relation: shares Miller Indices
- from: DOC-090
  to: DOC-096
  relation: shares Crystal Lattice
- from: DOC-090
  to: DOC-098
  relation: shares Crystal Lattice
- from: DOC-092
  to: DOC-099
  relation: shares Hydrogen Atom
- from: DOC-093
  to: DOC-099
  relation: shares Wavefunction
- from: DOC-093
  to: DOC-100
  relation: shares Perturbation Theory
- from: DOC-093
  to: DOC-102
  relation: shares Wavefunction
- from: DOC-094
  to: DOC-103
  relation: shares Solid State Physics
- from: DOC-095
  to: DOC-101
  relation: shares Spin-1/2
- from: DOC-096
  to: DOC-098
  relation: shares Crystal Lattice
- from: DOC-096
  to: DOC-105
  relation: shares Crystal Lattice
- from: DOC-097
  to: DOC-104
  relation: shares Eigenvalues
framework: GATE 2027 PH Physics Syllabus (IIT Madras)
sections_represented: 6

```

---

## Relational Triples & Concept Associations

```text
# Subject (Doc ID) | Relation | Object (Concept / Related Doc)
DOC-001 | shares Eigenstates | DOC-007
DOC-001 | shares Wavefunction | DOC-008
DOC-001 | shares Eigenstates | DOC-010
DOC-007 | shares Eigenvalues | DOC-008
DOC-007 | shares Eigenvalues | DOC-010
DOC-007 | shares Wavefunction | DOC-011
DOC-007 | shares Eigenvalues | DOC-012
DOC-007 | shares Eigenvalues | DOC-013
DOC-007 | shares Wavefunction | DOC-015
DOC-008 | shares Eigenvalues | DOC-010
DOC-008 | shares Wavefunction | DOC-011
DOC-008 | shares Eigenvalues | DOC-012
DOC-008 | shares Eigenvalues | DOC-013
DOC-008 | shares Wavefunction | DOC-015
DOC-008 | shares Eigenvalues | DOC-017
DOC-009 | shares Crystal Lattice | DOC-014
DOC-010 | shares Eigenvalues | DOC-012
DOC-010 | shares Eigenvalues | DOC-013
DOC-010 | shares Eigenvalues | DOC-017
DOC-011 | shares Wavefunction | DOC-012
DOC-011 | shares Wavefunction | DOC-015
DOC-012 | shares Eigenvalues | DOC-013
DOC-012 | shares Wavefunction | DOC-015
DOC-012 | shares Eigenvalues | DOC-017
DOC-012 | shares Harmonic Oscillator | DOC-020
DOC-013 | shares Eigenvalues | DOC-017
DOC-013 | shares Harmonic Oscillator | DOC-020
DOC-017 | shares Eigenstates | DOC-021
DOC-017 | shares Pauli Matrices | DOC-025
DOC-018 | shares Solid State Physics | DOC-019
DOC-020 | shares Harmonic Oscillator | DOC-028
DOC-021 | shares Perturbation Theory | DOC-028
DOC-022 | shares Brillouin Zone | DOC-023
DOC-028 | shares Eigenvalues | DOC-036
DOC-030 | shares Solid State Physics | DOC-031
DOC-030 | shares Solid State Physics | DOC-032
DOC-030 | shares Solid State Physics | DOC-035
DOC-031 | shares Solid State Physics | DOC-032
DOC-031 | shares Solid State Physics | DOC-035
DOC-032 | shares Solid State Physics | DOC-035
DOC-036 | shares Eigenvalues | DOC-040
DOC-036 | shares Perturbation Theory | DOC-041
DOC-036 | shares Perturbation Theory | DOC-042
DOC-036 | shares Eigenvalues | DOC-044
DOC-036 | shares Perturbation Theory | DOC-045
DOC-037 | shares Cauchy Sequence | DOC-043
DOC-038 | shares Eigenstates | DOC-040
DOC-038 | shares Eigenstates | DOC-045
DOC-040 | shares Eigenvalues | DOC-044
DOC-040 | shares Eigenstates | DOC-045
DOC-041 | shares Perturbation Theory | DOC-042
DOC-041 | shares Wavefunction | DOC-044
DOC-041 | shares Perturbation Theory | DOC-045
DOC-041 | shares Wavefunction | DOC-046
DOC-042 | shares Wavefunction | DOC-044
DOC-042 | shares Perturbation Theory | DOC-045
DOC-042 | shares Wavefunction | DOC-046
DOC-042 | shares Wavefunction | DOC-051
DOC-044 | shares Wavefunction | DOC-046
DOC-044 | shares Eigenvalues | DOC-050
DOC-044 | shares Wavefunction | DOC-051
DOC-045 | shares Eigenstates | DOC-050
DOC-045 | shares Perturbation Theory | DOC-054
DOC-046 | shares Spin-1/2 | DOC-050
DOC-046 | shares Wavefunction | DOC-051
DOC-046 | shares Wavefunction | DOC-055
DOC-047 | shares Solid State Physics | DOC-052
DOC-048 | shares Quantum Mechanics | DOC-049
DOC-048 | shares Quantum Mechanics | DOC-053
DOC-049 | shares Quantum Mechanics | DOC-053
DOC-050 | shares Spin-1/2 | DOC-051
DOC-050 | shares Eigenvalues | DOC-054
DOC-050 | shares Eigenvalues | DOC-055
DOC-051 | shares Wavefunction | DOC-055
DOC-051 | shares Wavefunction | DOC-058
DOC-054 | shares Eigenvalues | DOC-055
DOC-054 | shares Eigenvalues | DOC-060
DOC-054 | shares Eigenvalues | DOC-062
DOC-054 | shares Eigenvalues | DOC-063
DOC-055 | shares Wavefunction | DOC-058
```
