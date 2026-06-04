# CRAFT: Chains Reveal Attested Falsifiable Truth

CRAFT is an open meta-standard for evaluation chains. An evaluation chain is any system that takes in information from the world, processes it through a sequence of steps, and produces a claim that drives a decision about real people, organizations, funds, or risks. CRAFT states the conditions an evaluation chain must satisfy for the claim at the end of it to be reliable, and it states them without prescribing any particular technology or mechanism. CRAFT specifies what must be true; it does not specify how to build it.

## What it is for

Many failures of measurement and evaluation are not failures of execution. They are failures of specification: the system was never required to state what it measures, under what conditions its readings hold, and how an error would be caught. When the design is left implicit, there is no record of what the system is for, so it cannot be held accountable to a standard that was never written down. CRAFT closes that gap by requiring the design choices to be explicit before the system operates, so a claim can be audited before it is acted on rather than after it breaks.

## A meta-standard

CRAFT is a meta-standard, which means its purpose is to let others build domain standards correctly. A third party can use CRAFT's construction grammar to write a conformant evaluation standard for a specific field, through inside analysis of that field's own failure modes, without coordinating with the CRAFT maintainers. The six conditions and the construction grammar are domain-agnostic; the worked detail of any one domain belongs to that domain's own application.

## How it relates to the other open standards

CRAFT sits within a set of open, freely licensed standards, each building on the one beneath it. The Coordination Structural Integrity Suite specifies what must be structurally present for any evaluation or coordination structure to be sound, independent of domain. Frame Language is the shared vocabulary those standards use to distinguish structural grounding from aspiration. CRAFT builds on both to specify the conditions a domain-specific evaluation standard must meet. Each layer inherits from the one beneath it, and nothing in a higher layer is coherent without the layer below. All of them are free to use.

CROSS, the Common Reporting Outcome Standards Schema, is the first domain application built on CRAFT, the proof that the construction grammar produces a conformant standard and the example later applications follow; see the CROSS standard itself for its requirements. How CRAFT relates to the other open standards in the suite, and how they compose, is documented in the framework overview rather than here, so that the cross-standard relationships are maintained in one place.

## Documents in this repository

- `craft-specification-0_4_0.md`: the meta-standard itself. Six conditions for a reliable evaluation chain, plus the construction grammar and inheritance requirements for building a conformant domain application.
- `craft-condition-composition-principles-0_1_0.md`: how the six conditions compose at the boundary between CRAFT and a domain application.

## License

The specification documents in this repository are licensed under the Creative Commons Attribution 4.0 International License; see `LICENSE-SPEC`. Any code or software artifacts are licensed under the Apache License 2.0; see `LICENSE`. This matches the licensing of the Coordination Structural Integrity Suite.
