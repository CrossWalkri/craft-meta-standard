---
title: CRAFT Skill
version: 0.1.0
date: 2026-08-20
status: Procedural encoding of CRAFT v0.4.6 for AI-assisted specification and audit of evaluation chains and CRAFT-conformant domain applications. Structured so a partial task can be received and completed correctly.
related_documents:
  - craft-specification-0_4_4.md (internal v0.4.6)
  - machine-readable/ (the generated schema, Zod, and the three output shapes)
  - CROSS v0.5.7 (github.com/CrossWalkri/cross), the first domain application built on CRAFT
  - WALKRI v0.2.1 (github.com/CrossWalkri/walkri), CRAFT's sister at the field level
license: CC0 1.0
---

# CRAFT Skill

Invoke this skill when specifying an evaluation chain whose claims will drive a decision about real people, funds, or risks; when building a CRAFT-conformant domain application for a field; and when auditing either for conformance. This is a procedural encoding of CRAFT (Chains Reveal Attested Falsifiable Truth) v0.4.6, the meta-standard for evaluation chain legibility.

CRAFT states what an evaluation chain must satisfy for the claim at the end of it to be relied on, without prescribing any technology or mechanism. It specifies what must be true, not how to build it.

## The commitment that holds through every operation below

An evaluation chain is legible when a party who did not build it can determine what decision it was built for, what it measures and why that operationalizes the decision, how it decides, and how a detected error travels back to the stage that caused it. Illegibility is the failure this standard exists to replace: a chain whose design choices are implicit cannot be refuted, and a claim that cannot be refuted cannot be relied on.

Three consequences hold throughout and are not negotiable per task:

- **Legibility is the condition for refutability.** Every implicit design choice is a place the chain cannot be tested. Name the decision, the parties, the estimand, and the out-of-scope uses before any data is collected.
- **An outcome is a class, not a score.** A reading is accepted, rejected, or indeterminate against a pre-specified threshold while carrying the instrument's uncertainty. Indeterminate is its own class and never collapses into accept or reject; the non-resolution is information the feedback loop carries.
- **Preserve the layer.** Every finding declares whether it originates at the CRAFT base, the domain application, or a per-axis quality instrument. A finding with no layer cannot be routed to the stage that must correct it.

## Runtime Sequence

Identify which operation is requested and run the corresponding procedure in full.

1. **Chain specification against the six conditions.** Run when designing any evaluation chain. See Part I.
2. **Construction-grammar check for a domain application.** Run when building or auditing a domain application, beyond the six conditions. See Part II.
3. **Inheritance receipt production.** Run when a domain application declares CRAFT conformance. See Part III.
4. **Evaluation record production.** Run per input at runtime. See Part IV.
5. **Compliance report production.** Run at audit time, when someone asks whether a specification is CRAFT-conformant. See Part V.

---

## Part I: The six conditions

A chain satisfies CRAFT when all six hold. Each is a design obligation, checkable from the specification.

1. **Decision context specification.** Name the decision, the parties it is made for, the conditions under which the evaluation is a good input (stated so reality can refute them) and the conditions under which it is invalid, and the out-of-scope uses. A chain validated for one population or use context is not valid for another by default; declare the scope boundary before deployment. Where the chain faces adversarial actors, declare the threat model here, because it changes instrument choices, calibration, and detection thresholds downstream.
2. **Technical ontology adequate to the decision context.** State the constructs, and state the grounds on which they operationalize the Condition 1 estimand: empirical validation, logical derivation, or documented precedent. The grounds must apply to the actual risk-bearers, not a formally similar population. A present-state construct used as a proxy for a future-state claim requires the inferential step declared here and validated at Condition 3.
3. **Valid measurement instruments within the ontology.** Provide instruments that measure the constructs, name systematic uncertainty as a carried requirement referenced at Conditions 4 and 5, and declare the cohort-size resolution floor below which a statistical reading is not relied upon (routing instead to the determinate-resolution signal class rather than exempting the small cohort).
4. **Pre-specified evaluation criteria.** Fix the criteria and thresholds before the data arrives, and set them with reference to the Condition 3 uncertainty so a threshold does not fall inside the range the instrument cannot resolve.
5. **Explicit decision logic.** State how criteria results map to the decision the chain supports.
6. **Feedback mechanism with propagation.** Detected errors propagate to every prior stage they implicate; rejection and indeterminate outcomes carry their propagation targets; and version monitoring of every inherited standard is a named responsibility.

---

## Part II: Construction-grammar check for a domain application

A domain application that satisfies the six conditions but does not meet the construction grammar is a chain-quality standard, not a CRAFT-conformant domain application. Check all four.

- **Structural operativity (9.1).** Each of the six conditions runs on the execution path as a check on every instance of the process it applies to, cannot be bypassed without the bypass being a detectable adverse signal, and is logged as a coordination record entry. A condition that runs as a periodic audit or a bypassable manual review is compliance-scheduled, satisfying the letter while being structurally absent. Declare, per condition, how it is made structurally operative.
- **Response architecture (9.2).** For each detection condition, a response declaration exists before deployment, specifying the modality (automated, logged, or intervention), the speed requirement relative to the failure mode, and the response class (accidental failure calls for chain correction and propagation; deliberate manipulation calls for security response and notification of the Condition 1 risk-bearers).
- **Direction validation (9.3).** Examine the specification from at least two directional origins before accepting it. The deploying organization's origin is required but not sufficient; the affected party's origin reveals a failure class structurally invisible from the operator's.
- **Domain bifurcation (9.4).** Declare which instrument classes the application covers, which it does not, and the boundary criterion. Covering only the legally-constrained classes and leaving the impressionistic ones unaddressed is a design choice that must be stated, not a default.

---

## Part III: Inheritance receipt production

A CRAFT-conformant domain application produces an inheritance receipt with three components.

- **Chain-level receipt.** The decision context, technical ontology, and domain configuration in CRAFT-compliant form, traceable to Conditions 1 through 6.
- **Full Precision Toolkit scope.** A domain application does not inherit from CRAFT alone. Declare the active CSIS (Coordination Structural Integrity Suite) standards and what each requires, and the Frame Language vocabulary discipline. A receipt that declares CRAFT conformance without declaring CSIS and Frame Language inheritance is structurally incomplete.
- **Activity profile per declared inheritance,** with five elements: the standard name and version; which obligations apply and what they require; the trigger conditions that foreground them; the background state (background-satisfied with a dated reference, or background-unchecked as an explicit gap, never silence); and the version-coupling procedure that detects when the standard revises and enters version-bump-pending. Background-unchecked is not a valid operating state and must appear as a finding in any review; it is still better than an undeclared omission, because it is legible and actionable.

Where the domain application implements per-axis quality assessment, declare which CRAFT condition each axis serves and where it sits in the domain configuration.

---

## Part IV: Evaluation record production

At runtime the chain produces one evaluation record per input (the machine-readable tree root). Each record declares its type, the specification id and version in force, the timestamp, and the input provenance in checkable form, then:

- **Outcome:** accepted (the reading minus its uncertainty still clears the threshold), rejected (the reading plus its uncertainty still fails it), or indeterminate (the band straddles the threshold). Indeterminate is not collapsible and routes through its own signal class.
- **Condition findings:** for each condition, the result, the basis, and the layer attribution; carry the Condition 3 uncertainty band on any finding whose instrument specified one, so the outcome is independently checkable.
- **Gate check result:** the adversarial gate result at evaluation time.
- **Propagation targets:** for every rejection and indeterminate outcome, the prior conditions the signal must reach under Condition 6.

---

## Part V: Compliance report production

At audit time, when someone asks whether a specification meets CRAFT (not when the chain evaluates data), produce a compliance report naming the evaluated specification id and version, with one result per condition. Each result declares its layer (CRAFT base, domain application, or per-axis quality), so a domain-application finding is distinguishable from a base finding. No field in any of the three output schemas may require human interpretation to be processed by an automated consumer.

---

## Relations to the rest of the corpus

**CSIS (Coordination Structural Integrity Suite)** is the normative foundation. CRAFT must remain consistent with CSIS foundational commitments; a CRAFT requirement that would make CSIS-compliant behavior CRAFT-non-compliant requires resolution at the CSIS level first. A domain application declares its CSIS inheritance in the receipt.

**WALKRI** is CRAFT's sister at the field level. The two validate each other: CRAFT validates that WALKRI's own specification is itself a legitimate evaluation chain, and WALKRI validates that a CRAFT decomposition into a domain produced well-formed instruments whose capture points pass instrument-quality checks. Neither is exempt from the other, which is what keeps the pair from being gamed. WALKRI satisfies CRAFT's instrument-facing conditions (Conditions 2, 3, 4) rather than inheriting them.

**CROSS** is the first domain application, the proof that the construction grammar produces a conformant standard for grants. Third parties can build CRAFT-conformant domain applications for other fields without coordinating with the CRAFT maintainers; conformance is independently attested.

**Frame Language** actively checks vocabulary whenever any specification document at any level is authored or revised. The receipt triggers the initial check; each revision triggers it again.

## The machine-readable layer

`machine-readable/dist/craft.schema.json` (JSON Schema 2020-12) and `machine-readable/dist/craft.zod.ts` (Zod) validate an evaluation record's structure; the inheritance receipt and compliance report are companion classes in the schema's `$defs`. The schema enforces the Section 12 output shapes (required fields, the three outcome classes, layer attribution on every finding, propagation on non-accept, a dated background-satisfied claim). It does not decide whether the six conditions are satisfied, whether each is structurally operative, or whether the specification was examined from two directional origins; for a meta-standard those judgments are most of what conformance means. `machine-readable/src/craft-register.yaml` marks each obligation as shape, judgment, or mixed; do not report a schema pass as full CRAFT conformance.
