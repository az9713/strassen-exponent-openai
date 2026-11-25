# HANDOFF — resume point for the 9/4 matrix multiplication tutorial

**Read this first, then `~/.claude/CLAUDE.md` for standing conventions.** `proof-map.md` is the older proof map;
read it only if you must re-derive something.
Folder: `C:\Users\simon\Downloads\strassen_exponent_openai`. Not a git repository. Nothing is published.

## Current state (verified 2026-11-25, about 11:00 local)

- **`nine-fourths-tutorial.html` is complete in structure** (692 KB, dark mode, one self-contained file; MathJax
  from CDN without SRI). It contains: status section, background A.1–A.6, proof map M, paper §1–§27, AHA list,
  audit section, references, five widgets, timeline figure.
- Who wrote what:
  - Main session, from the LaTeX sources read in full: §0, A, M, §1–§14, AHA list, audit, references, widgets.
  - Subagent fragments, spliced between `<!--PARTn-BEGIN-->` / `<!--PARTn-END-->` markers:
    Part II = §15–18, Part III = §19–22, Part IV = §23–27.
- **The main session did not read the text of §15–27.** Only script checks were done on it.
- **Part IV (§23–27) is unreviewed even by its author.** `part4-writer` stopped at a usage limit while it was
  "applying four fixes and symbol clarifications" from its own review. Its fragment was well formed (tags
  balanced, `checktex` 0, `checklt` 0) and was spliced as it stood at 10:57. A red box at the top of Part IV and
  the audit section say this.
- Checks that pass on the final file: `checktex` 0 issues (9,102 math segments), `checklt` 0, `check_links` 0
  broken of 334, `check_svg` 0 hard issues, `check_overlap` 0, `check_frame` 0, `verify_dom` 0 `mjx-merror`;
  `accept.py`: 49 statement boxes, 0 page problems, no statement of the index without a box, 84 equation tags all
  present in the paper; at 390 px `scrollWidth` = 390 and no element overflows; widget values correct
  (tripod (1,1,1) → D* = 2.6667, ratio 2.25; (3/8,3/8,3/8) → D* = 1, perimeter 2.25; (1,1,0) → 2;
  (1,1,19) → 20.51282).
- Box counts in the file: 17 "not verified", 21 imported, 136 "filled here".

## Next task

**Review §15–27 against the LaTeX, starting with Part IV.** Suggested order:
1. §27 (`build/shaving.tex`, 6 KB): compare the parameter list and every inequality of the tutorial's
   "Proof of Theorem 2.1" with the source. This is where the proof closes; an error here is the most visible.
2. §23–26 (`rounds.tex`, `core-width.tex`, `round-iteration.tex`, `assembly.tex`): read the `.fill` and `.open`
   boxes; delete or correct any gap fill that does not hold.
3. §16–18 and §19–22: sample the `.fill` boxes. Items the subagents flagged as their own computations:
   `d_* ≥ 45000`, `C = 208`, `p > 3/2` (Part II); the scalar in Lemma 19.2 and the `D^4` segment count (Part III).
4. After the review: update the audit section (`#audit-7`) and remove the red box at the top of Part IV if the
   review supports that.
5. Not done at all: a visual pass of the whole page (one desktop screenshot of Fig. 1 was inspected; a phone
   screenshot call timed out). `check_proofs.py` gives advisories because it does not know the classes
   `proof sketch` / `proof walk`; they were not triaged for §15–27.
6. Optional, Simon decides: publish (not requested; decision 1 says local HTML only).

Rerun after any edit: `checktex.py`, `checklt.py`, `check_links.py`, `verify_dom.py`
(in `~/.claude/skills/rigorous-explainer/scripts/`, each takes the HTML path), and
`python -I -X utf8 .ignore/frag/accept.py nine-fourths-tutorial.html .ignore/frag/index.txt <paper.txt>`.

## Decisions Simon made on 2026-11-25 (still in force)

1. Output: local HTML file only. Do not publish an artifact.
2. Depth: walk the main paper, all 27 sections. Companion papers [42], [43] are black boxes: state exactly what
   each imported result says and mark it as imported.
3. Prose in the tutorial: normal mathematical prose. Chat replies stay in ASD-STE100.
4. "Fill in all gaps especially in background maths and gaps in proofs." Default used: gaps inside [42]/[43] are
   marked "not verified"; the companion papers were not read.

## Facts found in this session that correct `proof-map.md`

- **The PDF text layer drops overlines and underlines.** Lemma 2.4 is `rank_{\overline F}(T_s) ≤ 2q` (algebraic
  closure), not `rank_F`. §7.4 uses `\underline D`. Use `build/*.tex` for every formula.
- File → section map of `build/`: obstruction §2.1–2.3; consequences §2.4; background §3; list §4; prices §5;
  valued §6; motion §7; boundary §8; contact §9–11; sync §12; fermions §13; sphere §14; incidence §15;
  sorting (+lookup) §16–18; local (+local-plant §20, local-motion §21) §19–22; rounds (+core-width §24,
  round-iteration §25.2) §23–25; assembly §26; shaving §27.
- Pages: §15 is in Part I; Part II starts on p. 59; §18 is pp. 67–73; Part III is pp. 73–86.
- `e ≥ 2(1−s^{−1/2})V` is Corollary 15.2 only; `C_0 = 100` is from Lemma 17.2; (20.4) is argued on p. 79 and,
  by the Part III subagent's report, is the only use of ω_k < 9/4 in Part III. (Subagent reports, not rechecked.)
- Theorem 7.1 is conditional and is used only in contrapositive form in §12. The tutorial says this in §8.
- Companion folder names on GitHub are verified: `Euclidean-geometry-in-the-asymptotic-spectrum-of-tensors-November-24-2026`
  and `Circuit-lower-bounds-for-Hamiltonian-cycle-and-the-permanent-November-24-2026`.

## Workflow provenance and evidence

- Skills used: `rigorous-explainer` (check scripts, MathJax configuration). Advisor consulted once before writing.
- Agents: three `general-purpose` subagents (`part2-writer`, `part3-writer`, `part4-writer`), briefed by
  `spec.md`. Parts II and III sent final reports; Part IV did not (usage limit).
- Sources were downloaded with `curl` from
  `raw.githubusercontent.com/openai/math/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/build/<name>.tex`.
- Project files added in this session: `nine-fourths-tutorial.html`; `.ignore/frag/` (fragment copies
  `part2.html`, `part3.html`, `part4.html`, and `splice.py`, `accept.py`, `index.txt`, `spec.md`);
  `.impeccable/config.json` (an ignore for the design hook's `side-tab` rule, scoped to the tutorial; the
  coloured left border of each box is the provenance code).
- Known limits: MathJax needs network on first open; the history values 1978–2025 in Fig. 1 are from memory.

## Session-transient scratch

- Scratchpad `C:\Users\simon\AppData\Local\Temp\claude\cf3486734e4d0103\9aa0dc67-6a45-4868-9126-a13c02b06a49\scratchpad`
  holds `paper.txt`, `tex/*.tex`, `index.py`; a reboot can clear it. Regenerate:
  - `paper.txt`: `python -I -X utf8 -c "import pypdf,sys; r=pypdf.PdfReader(sys.argv[1]); f=open(sys.argv[2],'w',encoding='utf-8'); [f.write(f'\n=====PAGE {i}=====\n'+(p.extract_text() or '')) for i,p in enumerate(r.pages,1)]" paper.pdf <scratch>/paper.txt`
  - `tex/<name>.tex`: `curl -sfL -o <name>.tex <raw URL above>`

## How to work

- State what is verified and what is not. Do not write that the result is settled.
- One HTML file. Add no build system.
- Report in ASD-STE100, with what is done and what is not done.
