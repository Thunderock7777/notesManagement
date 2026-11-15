<!-- ===================================================================== -->
<!-- AUTO-GENERATED SURROGATE SOURCE (FOR SEARCH & CATALOGING ONLY)       -->
<!-- Source PDF: math-cauchy-sequence1.pdf
<!-- Status: PROVISIONAL SURROGATE (DO NOT RECOMPILE)                      -->
<!-- Purpose: Instant full-text search, AI context retrieval & knowledge graph mapping. -->
<!-- Note: Will be automatically replaced when an authentic manual source note is provided. -->
<!-- ===================================================================== -->

Notes 

1 

# Reference Notes 

Made By Abhik Biswas 

**No, if a sequence does not converge, it does NOT mean the sum converges.** In fact, it is the exact opposite! 

To see why, it helps to separate two concepts that are often easy to mix up: a **Sequence** vs. a **Series (Sum)** . 

## **1. Sequence vs. Series (Sum)** 

- **Sequence:** An ordered list of state vectors: 



<!-- Start of picture text -->
|v 1 ⟩, |v 2 ⟩, |v 3 ⟩, . . .<br><!-- End of picture text -->

For a sequence to converge, the list of vectors must approach a single fixed limit vector _|v⟩_ . 

- **Series (Sum):** Adding vectors together one by one: 



<!-- Start of picture text -->
∞<br>∑ |uk⟩ =  |u 1 ⟩ +  |u 2 ⟩ +  |u 3 ⟩ +  . . .<br>k =1<br><!-- End of picture text -->

## **2. How an Infinite Sum is Tested for Convergence** 

How do we mathematically decide if an infinite sum<sup>∑</sup> _|uk⟩_ converges? 

We turn the sum into a **sequence of partial sums** _|sn⟩_ : 

- _|s_ 1 _⟩_ = _|u_ 1 _⟩_ 

- _|s_ 2 _⟩_ = _|u_ 1 _⟩_ + _|u_ 2 _⟩_ 

- _|s_ 3 _⟩_ = _|u_ 1 _⟩_ + _|u_ 2 _⟩_ + _|u_ 3 _⟩_ 

- _. . ._ 

- _|sn⟩_ =<sup>∑</sup><sup>_n_</sup> _k_ =1<sup>_|uk⟩_</sup> 

**The infinite sum converges IF AND ONLY IF this sequence of partial sums** _|sn⟩_ **converges (which means** _|sn⟩_ **must be a Cauchy sequence).** 

Notes 

2 

**3. What Happens If Things Do NOT Converge?** 

   1. **If the sequence of partial sums** _|sn⟩_ **is NOT Cauchy (does not converge):** 

      - The total sum<sup>∑</sup> _|uk⟩_ **fails to converge** (it diverges to infinity or oscillates endlessly). 

   2. **The Term Test for Sums:** 

      - For an infinite sum<sup>∑</sup> _|uk⟩_ to have any chance of converging, the individual terms _|uk⟩_ being added **MUST shrink to zero** (lim _k→∞ |uk⟩_ = 0). 

      - If the individual terms _|uk⟩_ do **not** converge to zero, the infinite sum **automatically diverges** . 

## **Summary** 

- **Sequence Not Converging** = _⇒_ The vectors keep growing, bouncing around, or drifting, so they never settle down. 

- **Sum Not Converging** = _⇒_ Adding up the terms produces an unstable/infinite result because the partial sums are not a Cauchy sequence. 

