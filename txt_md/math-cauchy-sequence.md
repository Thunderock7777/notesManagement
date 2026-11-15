<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: math-cauchy-sequence.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

In plain English, a **Cauchy sequence** is a sequence of elements (like numbers, vectors, or wave functions) whose terms get **arbitrarily close to** **_each other_** as you move further and further out in the sequence. 

The key difference between a standard convergent sequence and a Cauchy sequence comes down to how you test them: 

- **Standard Convergence:** You check if the terms get closer and closer to a _specific target limit L_ . 

- **Cauchy Property:** You check if the terms get closer and closer _to one another_ , even if you don’t know what (or where) the final limit is! 

## **1. The Mathematical Definition** 

A sequence of state vectors _|v_ 1 _⟩, |v_ 2 _⟩, |v_ 3 _⟩, . . ._ is a **Cauchy sequence** if, for any tiny distance _ϵ >_ 0 you choose, there exists a point _N_ in the sequence such that for all terms beyond that point ( _m, n > N_ ), the distance (norm) between them becomes smaller than _ϵ_ : 



<!-- Start of picture text -->
∥|vm⟩−|vn⟩∥ < ϵ for all m, n > N<br><!-- End of picture text -->

## **2. The “Hole in the Space” Problem (Why Cauchy Sequences Matter)** 

You might wonder: _If terms get infinitely close to each other, don’t they automatically converge to a point inside the space?_ 

**Not always!** It depends on whether the space has “holes” or missing points. 

**Classic Example (Rational Numbers vs. Real Numbers):** Consider the sequence of decimal approximations for _π_ : 



<!-- Start of picture text -->
x 1 = 3 , x 2 = 3 . 1 , x 3 = 3 . 14 , x 4 = 3 . 141 , x 5 = 3 . 1415 , . . .<br><!-- End of picture text -->

1. Every single number in this list is a **rational fraction** (e.g., 314/100). 

2. As you go down the list, the terms get infinitely close to _each other_ . This is a **Cauchy sequence** . 

Notes 

2 

3. But the limit it approaches is _π_ , which is an **irrational number** . 

- **If your mathematical space is ONLY the rational numbers (** Q **):** The sequence tries to converge to _π_ , but _π_ doesn’t exist in Q! There is a “hole” where _π_ should be. Therefore, Q is **not complete** . 

- **If your space is the Real Numbers (** R **):** The “hole” is filled, and the limit _π_ lies safely inside R. Therefore, R **is complete** . 

## **3. What This Means in Quantum Mechanics (Hilbert Space)** 

In quantum mechanics, wave functions are frequently written as infinite series over energy eigenstates: 



<!-- Start of picture text -->
∞<br>|ψ⟩ = ∑ cn|n⟩<br>n =1<br><!-- End of picture text -->

If you take the sequence of partial sums: 

- _|ψ_ 1 _⟩_ = _c_ 1 _|_ 1 _⟩_ 

- • _|ψ_ 2 _⟩_ = _c_ 1 _|_ 1 _⟩_ + _c_ 2 _|_ 2 _⟩_ • _|ψ_ 3 _⟩_ = _c_ 1 _|_ 1 _⟩_ + _c_ 2 _|_ 2 _⟩_ + _c_ 3 _|_ 3 _⟩_ • _. . ._ 

This sequence of state vectors forms a **Cauchy sequence** . 

Because a **Hilbert space is complete** , it guarantees there are **no mathematical holes** . Adding up an infinite number of quantum wave functions will _always_ converge to a limit _|ψ⟩_ that is a valid, physical state **inside the same Hilbert space** . You will never end up with an unphysical “missing” state! 

**Only Cauchy sequences can converge.** An arbitrary sequence of state vectors will **not** automatically converge. 

In fact, in a Hilbert space, a sequence of state vectors converges **if and only if** it is a Cauchy sequence! 

## **1. Why Arbitrary Sequences Don’t Always Converge** 

For a sequence of state vectors to converge, its terms cannot behave wildly. Here are two simple examples of sequences that do **not** converge: 

1. **Diverging Sequence (Blowing Up):** Consider the sequence: 



<!-- Start of picture text -->
|vn⟩ =  n|ψ⟩ = ⇒{ 1 |ψ⟩,  2 |ψ⟩,  3 |ψ⟩,  4 |ψ⟩, . . . }<br><!-- End of picture text -->

The norm (“length”) of these vectors grows to infinity (\|v_n\| _→∞_ ) _, sothesequenceneversettlesdownatanyfixedstatevector._ 

Notes 

3 

1. **Oscillating Sequence (Bouncing Forever):** Consider a state bouncing back and forth: 

   - _|vn⟩_ = ( _−_ 1)<sup>_n_</sup> _|ψ⟩_ = _⇒{−|ψ⟩,_ + _|ψ⟩, −|ψ⟩,_ + _|ψ⟩, . . . }_ 

The distance between consecutive terms is always \|v_{n+1} - v_n\| = 2\|| _ψ⟩\|̸_ = 0 _\.Thetermsnevergetclosertoeachother, sothesequencebouncesforeverwithoutconverging._ 

## **2. The Two-Way Rule in Hilbert Space** 

Because a Hilbert space is **complete** , the relationship between Cauchy sequences and convergent sequences is a two-way street: 

**Direction A: Convergent** = _⇒_ **Cauchy (Necessary)** If a sequence of state vectors _|vn⟩_ converges to a limit _|v⟩_ , then as _n_ grows, all terms get closer to _|v⟩_ . By the triangle inequality, the terms **must also get arbitrarily close to one another** . 

- **Meaning:** It is physically and mathematically impossible for a non-Cauchy sequence to converge. 

**Direction B: Cauchy** = _⇒_ **Convergent (Sufficient, thanks to Completeness)** In a general space with “holes” (like rational numbers), a Cauchy sequence might _try_ to converge to a missing point. But because a **Hilbert space is complete** , every Cauchy sequence is **guaranteed to converge** to a valid state vector that lies safely inside the Hilbert space. 

## **Summary** 

|Sequence Type|Do the terms get close to<br>each other?|Does it converge in Hilbert<br>Space?|
|---|---|---|
|**Arbitrary Sequence**|Not necessarily (could blow<br>up or bounce around).|**No** (in general).|
|**Cauchy Sequence**|**Yes** (by definition:<br>_∥vm −vn∥→_0).|**Yes, 100% guaranteed**<br>(because Hilbert space is<br>complete).|



