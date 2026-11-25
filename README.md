# Nine fourths: a guided tutorial

A tutorial on the preprint **"The matrix multiplication exponent is nine fourths"** (author line "OpenAI",
dated 24 November 2026, 111 pages).

The preprint states that the exponent of square matrix multiplication is 9/4 over every field. The upper bound
ω ≤ 9/4 is prior work that the preprint cites. The lower bound ω ≥ 9/4 is the new part.

## Status of the claim and of this tutorial

Read this before you rely on anything here.

- The source is an unrefereed preprint. This project did **not** verify the proof, and the tutorial does not
  certify it.
- The lower bound depends on two companion OpenAI preprints of the same date. They were not read. The tutorial
  marks each imported statement.
- The upper-bound papers that the preprint cites were not read.
- The [preprint folder](https://github.com/openai/math/tree/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026)
  states that a Lean development proves the square exponent 9/4 for **division-free** circuits. This project did
  not open the Lean files.
- Sections 15–27 of the tutorial were not reviewed by a second reader. They were drafted by subagents, and the
  main session ran only script checks on them.
- The review of Part IV (§23–27; §27 proves the compression theorem, Theorem 2.1) by its own author is
  incomplete. Compare §27 with `build/shaving.tex` in the preprint folder before you rely on it.

This list is not complete. The tutorial section "What this tutorial checked, and what it did not" gives the
other limits.

## Contents

| File | What it is |
|---|---|
| `nine-fourths-tutorial.html` | The tutorial: status, background, proof map, paper §1–§27, audit, references, five widgets. One dark-mode HTML file. |
| `paper.pdf` | Copy of the preprint. On 25 November 2026 it was byte-identical to the upstream file (SHA-256 `ddde9ab7755596c6f0210c148985f9761f2c291582e4d0a045987ad1766e5a01`). |
| `proof-map.md` | Working notes made before the tutorial. `HANDOFF.md` lists corrections to them. |
| `HANDOFF.md` | Resume notes: what was checked, and the next review task. |

## How to read it

Clone the repository and open `nine-fourths-tutorial.html` in a browser. MathJax loads from a CDN, so the
formulas need a network connection on first open. There is no build step.

## References

1. Ryan Williams, post on X: <https://x.com/rrwilliams/status/2125393802554757618>.
   The project notes record it as: "Apparently Strassen was right: the matrix mult exponent is (exactly) 2.25".
   The post could not be fetched when this README was written, so the wording was not re-checked.
2. OpenAI, preprint folder (paper, LaTeX sources in `build/`, repository notes):
   <https://github.com/openai/math/tree/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026>
3. OpenAI, *The matrix multiplication exponent is nine fourths*, PDF:
   <https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf>
4. Andreas Klappenecker, *Strassen's Matrix Multiplication* (CSCE 411 slides, partly based on slides by
   Prof. Welch; the URL path indicates spring 2019):
   <https://people.engr.tamu.edu/andreas-klappenecker/csce411-s19/csce411-divideconquer2.pdf>.
   A 10-page introduction to Strassen's seven products and the master theorem, which give O(n^2.81). Useful
   background before the tutorial. The slides give O(n^2.3727) as the fastest known method and Ω(n²) as the best
   known lower bound; both are statements of their own date.
