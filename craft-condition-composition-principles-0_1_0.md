# CRAFT Condition Composition Principles

**Version:** 0.1.0
**Date:** 2026-05-27
**Status:** Architecture principle capture. Establishes how CRAFT conditions compose when addressing domain failure modes, and the decomposition logic required at the CRAFT-to-domain-application boundary.

**Relevant files:**
- `craft-specification-0_4_3.md`

---

## The Basic Principle

CRAFT conditions have composition dependencies. Some failure modes require specific condition pairs or triplets applied in coordination to achieve precision. Neither condition alone is sufficient; the composition is what produces a claim that can be falsified and does not overreach what the evidence demonstrates.

This is a structural property of the chain architecture: each condition is derived from and constrained by the prior conditions. A condition applied without its prior conditions in place is applied to an undeclared context. Outputs from an undeclared context cannot be precise regardless of how carefully the condition itself is applied, because precision requires knowing what claim is being made before evaluating whether that claim is supportable.

## The Paradigm Example

Mechanism design adversarial testing illustrates the principle. Determining whether a protocol's economic mechanism is sound under adversarial capital deployment requires two conditions in composition:

Condition 1 (decision context specification) declares what the mechanism is designed to do, for whom, under what conditions, and what adversarial conditions would make it invalid.

Condition 4 (pre-specified evaluation criteria with adversarial gate) tests whether the specification produces rejections under realistic adversarial conditions, including adversarial capital strategies.

Applying Condition 4 without Condition 1 in place produces adversarial testing against an undeclared context. You may find that certain inputs are rejected, but you cannot determine whether those rejections correspond to the mechanism's actual design intent, because the intent was never declared. The adversarial gate catches technical failures; it cannot catch design intent failures without the declared context to test against.

Applying Condition 1 without Condition 4 produces a well-specified decision context that has not been tested. A mechanism design can be precisely specified and still be exploitable if the adversarial strategies it was designed to resist were never applied before deployment.

The Euler Finance exploit ($197M, code correct, mechanism exploitable) is a case where neither condition was applied in a composition that could have caught the failure. The liquidation mechanism's economic vulnerability was not a code error; it was a design intent that was never tested against adversarial capital strategy. That test requires both conditions in coordination. The decision context was a hollow link: formally present, satisfying documentation requirements, but producing no real constraint on the mechanism's behavior under adversarial conditions. Condition 1 without Condition 4 produces a hollow link regardless of how carefully Condition 1 is applied; the link has no functional constraint until the adversarial gate tests it.

## Domain Evaluation Implication

When analyzing a new domain's failure modes, the discovery work must identify which condition compositions address each failure class, not just which individual conditions apply. The question is not "does this failure implicate Condition 3?" but "which conditions, composed in what order, would have produced a specification precise enough to make this failure class detectable before exploitation?"

A failure class that requires Conditions 1, 3, and 4 in composition is a fundamentally different domain requirement than one that requires only Condition 3. The domain application must implement all required conditions in coordination, with the composition logic declared explicitly.

## The Composition-Decomposition Boundary

At the boundary between CRAFT (meta-standard) and a domain application (derived specification), composition logic must be preserved through decomposition. The principle concerns how composition and decomposition are handled at that boundary specifically.

A domain application decomposes each CRAFT condition into domain-specific requirements. But if the domain's primary failure class requires Conditions 1 and 4 in composition, decomposing each condition independently into domain-specific language without specifying their coordination produces a specification that satisfies each condition in isolation while leaving the composition gap undeclared.

The gap is a precision failure: the domain specification makes claims about failure-mode coverage that it cannot demonstrate, because the conditions that must work together have been specified as if they work independently. The interactions between conditions are where the precision lives.

The decomposition procedure at the CRAFT-to-domain-application boundary therefore has two phases: decompose each required condition into domain-specific requirements, then specify the composition logic that those decomposed conditions must preserve. The second phase is not optional. A domain application without explicit composition logic has not fully specified its coverage claims. A domain application that decomposes each condition independently without specifying their coordination produces weak links at each condition: the conditions exist and are named, but the load-bearing connection between them has not been declared and cannot be tested.

## Connection to the Gauge Block Principle

This principle is structurally parallel to the PFDS gauge block principle: precision does not transfer between layers automatically. A domain application that inherits CRAFT conditions does not automatically inherit the composition logic that makes those conditions jointly precise for a given failure class. That logic must be declared explicitly at the domain level.

Stated as a practical rule: for each failure class a domain application claims to address, it must name which conditions are required in composition to address it, and specify how those conditions coordinate. A claim to address a failure class without specifying the required composition is an ungrounded precision claim.

## Connection to the Discovery Pedagogy

The discovery pedagogy (pre-engagement, ask-specific, engagement phases) should produce, as one of its required outputs, a composition map for the domain: which condition pairs or triplets address which failure classes in that domain. This is not an optional finding from the discovery work; it is a precision requirement for the domain application that follows. A domain analysis that identifies failure classes without mapping them to condition compositions has not completed the specification work the domain application requires.
