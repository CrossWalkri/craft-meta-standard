---
title: CRAFT Specification
version: 0.4.3
date: 2026-06-13
status: Working specification. Sections 10, 11, and 12 are now normatively specified; Section 12's three output schemas are specified in prose with pointer to external schema files. The runtime evaluation record schema is new in this version and has not yet been implemented in the reference tooling. Section 10's activity profile format is new and not yet implemented in tooling.
framework: CRAFT (Chains Reveal Attested Falsifiable Truth)
inherits-from: Coordination Structural Integrity Suite (CSIS) foundational commitments. Frame Language vocabulary discipline. Publication path for CSIS pending; see Section 10.
---

# CRAFT Specification

## Chains Reveal Attested Falsifiable Truth

---

## 1. Scope

This specification defines what CRAFT compliance requires for any system that aggregates external information to support decisions. It applies to evaluation chains in any domain where: data is collected from the world, assessed against criteria, and used to produce a record that influences decisions about real people, organizations, funds, or risks.

This specification is domain-agnostic and operates at two levels simultaneously.

As a chain quality standard, it specifies what a valid evaluation chain requires: the six conditions that must hold before any chain output can be relied upon for decisions.

As a meta-standard, it specifies what a CRAFT-conformant domain application must contain. A domain application is a CRAFT implementation specialized for a specific domain through inside analysis of that domain's evaluation failure modes. The construction grammar requirements (Section 9) and inheritance receipt structure (Section 10) address this second level. A third party wishing to build a CRAFT-conformant domain application for any domain where the chain of evaluation legibility problem is present can use this specification to do so without coordination with the CRAFT specification maintainers.

Domain applications of CRAFT inherit from this specification and add domain-specific requirements derived from inside analysis of the target domain's failure modes. A domain application in conflict with this specification is non-compliant; one that adds requirements not present here is compliant provided it does not contradict any normative requirement in this document.

Domain applications of this specification are developed separately, through inside analysis of each domain's failure modes. The first is CROSS, the Common Reporting Outcome Standards Schema, a freely available grants standard built on this specification.

---

## 2. The Problem: Chain of Evaluation Legibility

### 2.1 The failure mode

Every system that aggregates information for decisions has the same structural vulnerability: the chain from world to decision passes through stages where human or algorithmic judgment can introduce errors that are invisible to anyone who looks only at the final output. Garbage in, garbage out names this failure when it occurs at the data input stage. The complete problem is broader: the chain can break at any stage, and a break at any stage makes every downstream stage unreliable regardless of how sound those downstream stages are.

The name for the general problem class is Chain of Evaluation Legibility. A chain of evaluation legibility is structurally parallel to chain of custody in evidentiary law: chain of custody requires that every hand evidence passes through is documented and verifiable, and a break at any stage makes the evidence inadmissible regardless of whether the evidence itself is authentic. Chain of evaluation legibility requires that every stage an evaluation passes through is structured such that it can be inspected and refuted. A break at any stage makes the final output unreliable and, more precisely, unlearnable from.

### 2.2 Why GIGO understates the problem

Garbage in, garbage out locates the structural failure at the input stage, as though bad data is the primary risk. This framing is useful and incomplete. Input-stage failures are one class of chain of evaluation legibility failure. Equally important and less commonly named:

A decision context that was never specified before data collection began means the entire evaluation optimizes for internal coherence rather than for the actual decisions it will inform.

An ontology constructed without reference to a specified decision context produces categories that may be internally consistent but systematically irrelevant to what the decision requires.

Evaluation criteria specified after observing the data adjust to what the data shows rather than to what the decision requires. Post-hoc criteria are indistinguishable from post-hoc rationalization.

Decision logic that is implicit in the code rather than specified in writing cannot be contested. Parties who believed they understood the logic may have understood something else. Errors in implicit logic have no reference specification to be checked against.

CRAFT addresses the full chain. Garbage in, garbage out names the input-stage case. CRAFT solves the general case.

The adversarial complement to this framing: garbage can be crafted, not merely accumulated through poor specification. An actor who has read a chain's specification can reverse-engineer inputs that satisfy every condition while producing the outcome the chain was meant to prevent. The chain's precision is the attack surface: the attacker does not exploit imprecision; they exploit the gap between what the conditions check and what the conditions were meant to prevent. A CRAFT-conformant chain must be both legible and adversarially robust. These are not the same requirement.

### 2.3 The impressionistic failure

An impressionistic claim is one derived from the evaluator's gestalt perception rather than from pre-specified, independently verifiable criteria. Impressionistic evaluation may be accurate. It is not falsifiable: because no criteria were specified in advance, there is no standard against which the evaluation can be shown to be wrong. A reviewer who says "this project has strong impact" and a reviewer who says "this project has weak impact" cannot be adjudicated against each other, because neither has applied a specified criterion. The disagreement is not evidence of a measurement problem; it is evidence of the absence of a measurement.

This failure is not confined to human reviewers. Algorithmic evaluation systems that apply criteria not specified before deployment are impressionistic in the same structural sense. The algorithm replaces the gestalt; the structural gap is identical.

---

## 3. The Implicit Specification Gap

### 3.1 The gap defined

Every system that processes external information to support decisions makes design choices. Some of those choices are explicit: they are written down, published, and reviewable by anyone who looks. Most are implicit: they are embedded in the implementation, derivable in principle by reading the code or the procedure manual, but not stated as design choices with stated rationale and stated scope.

Implicit design choices create a structural gap between what the system was intended to do and what it can be held responsible for doing. When the design is implicit, there is no authoritative record of what behavior is within scope, what conditions the system was designed to handle, what adversarial conditions it was designed to resist, and what constitutes misuse versus use.

### 3.2 Why the gap matters for accountability

Consider a funding program that disburses against milestones but never states, before the round opens, what counts as a delivered milestone or what evidence a grantee must produce to demonstrate it. A grantee then reports a milestone complete on terms the program never excluded: a feature shipped to a private branch, a pilot run with the team's own members, a metric counted in a way the program never defined. The program is dissatisfied but cannot hold the grantee accountable, because the grantee did exactly what the unstated specification permitted. "We met the milestone as written" is an unanswerable defense when nothing was written about what the milestone required.

The structure is general. When a system's designers have not written down what the system is for, what conditions it was designed to handle, and what behaviour falls outside its intended use, the system cannot be held accountable to a specification that does not exist. Behaviour that operates within the system's stated parameters is behaviour the system invited by leaving its design unstated.

This is the implicit specification gap. CRAFT closes it by requiring that design choices be explicit before the system operates. It is the same gap that CROSS, the grants domain application built on this specification, closes on the funding side.

### 3.3 The gap across domains

The implicit specification gap is present in any evaluation system that makes design choices without stating them. A selection process that applies criteria not published before it begins cannot be audited for bias, because there is no baseline to audit against. A review panel that applies its standard after reading submissions cannot be assessed for consistency, because consistency requires a prior standard. An audit that applies judgment without a documented framework produces conclusions an independent party cannot reproduce, because no framework was published.

A grant program is a clear instance. A program that applies evaluation criteria after reading applications cannot be assessed for consistency across applicants, and a program that disburses against milestones it never defined cannot hold a grantee accountable for failing to meet them.

In each case the implicit specification gap creates the same structural problem: accountability requires an articulated standard, and the standard was never articulated.

---

## 4. Core Principle: Legibility as the Condition for Refutability

CRAFT's organizing principle is legibility. An evaluation chain is legible when every stage is structured such that an independent observer can inspect it, understand what it claims to produce, and determine whether it produced that or something else.

Legibility has four dimensions:

**Ontological legibility:** the constructs the system measures are defined precisely enough that two independent observers applying the definition to the same real-world phenomenon would reach the same classification in the overwhelming majority of cases.

**Epistemological legibility:** the measurement instruments and evaluation criteria are specified before data collection begins, and the specification is structured such that reality can refute it. A specification that cannot specify under what circumstances it would be wrong is not epistemologically legible. Falsifiability is the epistemological sub-case of legibility: the relevant observer is reality itself.

**Pedagogical legibility:** the evaluation chain is legible to the parties it affects, not only to the parties who designed it. A specification that is technically complete but practically opaque to applicants, grantees, collateral providers, or other affected parties is epistemologically legible and pedagogically illegible. Both conditions are required for CRAFT compliance.

**Decisional legibility:** the logic by which evaluation outputs produce decisions is explicit and independently reviewable before outcomes are produced. Implicit decision logic embedded only in code or procedure is not decisionally legible.

These dimensions are not independent. An ontologically illegible system cannot be epistemologically legible, because the criteria cannot be specified if the constructs are undefined. A system that is epistemologically legible but pedagogically illegible can satisfy the letter of CRAFT requirements while leaving affected parties unable to act on them. Decisional legibility requires both ontological and epistemological legibility as prior conditions.

The principle that unifies all four dimensions: a chain of evaluation legibility is legible when any party with relevant knowledge can determine, from the published specification alone and without access to internal implementation, what the system claims to be doing and what would constitute evidence that it is not doing that.

---

## 5. The Six Conditions

A CRAFT-compliant evaluation chain satisfies all six of the following conditions. Each condition states what must be true; the compliance requirements in Section 6 state what must be produced to demonstrate that each condition is satisfied.

### Condition 1 (Decision Context Specification)

The decision the evaluation is designed to support must be specified before any data collection or evaluation design begins. The specification must name the decision, the parties for whom it is being made, the conditions under which the evaluation would constitute a good input to the decision (stated in terms that reality can refute), and the conditions under which the evaluation would be invalid for the decision. Out-of-scope uses must be declared explicitly, naming both the purpose for which the evaluation has not been calibrated and the population and deployment context for which it has not been validated. A chain validated for one population or use context is not valid for a different population or use context by default; the scope boundary must be declared before deployment, not only detected through Condition 6 feedback after deployment.

Seven structural elements must be specified at this stage and carried into every downstream stage of the chain:

**Boundary population and frame specification.** The specification must name the boundary population: the set of entities within scope for the decision and the criteria that determine membership. It must also name the frame: the mechanism by which entities enter the evaluation.

The relationship between the boundary population and the evaluated population is a distinct required declaration. Not every entity in the boundary population will necessarily be evaluated. The operator must state which entities were evaluated, which were not, and the basis for that selection.

A chain that evaluates a population that does not match the boundary population without documenting the divergence produces valid outputs for the wrong population. This is not an instrument failure or a criteria failure. The error originates at this stage, and a feedback mechanism that traces it no further back than the instruments cannot locate the source.

This element is a carried requirement: the boundary population specification, once named here, must be present at every downstream stage. Any instrument, criterion, or decision logic that applies to a different population than the one named here is out of compliance with the decision context.

**Estimand specification.** The specification must name the causal contrast the evaluation is designed to support. The causal contrast is not the same as the decision. A decision names what will happen based on the evaluation's output. The causal contrast names what specific comparison between states of the world the evaluation claims to measure.

The same decision can be supported by structurally different causal questions, and those questions require different evidence. An evaluation designed to measure whether a condition improves above a threshold is not designed to measure whether the intervention caused the improvement. An evaluation designed to measure the effect of an intervention relative to a counterfactual of no intervention requires different instrument design than one designed to measure absolute performance. These are not different ways of asking the same question; they are different questions.

A chain that does not specify the causal contrast before designing instruments cannot be assessed for whether its instruments are capable of producing the evidence the decision requires. The estimand must be specified here, before any design decisions are made at subsequent stages.

**Claim object type declaration.** The chain's primary claim must be classified as either criterion-type or construct-type. This classification is a carried requirement through all downstream stages.

A criterion-type claim is one whose object is directly observable or has an established external validation standard. The criterion standard is the established reference against which the chain's measurements are calibrated. For criterion-type chains, the criterion standard must be named if one exists. If no established criterion standard exists, this must be declared: the specification states that the chain's criterion is novel, and names what evidence base the chain uses in the criterion standard's absence. A criterion-type claim whose criterion standard is unnamed and not declared absent is under-specified in the same structural sense as an undefined construct.

A construct-type claim is one whose object is abstract and not directly observable. A construct-type declaration must further declare the indicator direction, which selects the validation regime.

Reflective: the indicators reflect a latent construct that stands behind them. A nomological network declaration is required at this stage: naming the construct, its sub-constructs, the observable criteria that proxy for each sub-construct, and the expected relationships between them. The nomological network declaration has three valid states: established (with an evidence reference), partial (with named gaps declared explicitly), or absent-declared (explicitly stated as a current gap). A declared-partial or absent-declared nomological network is a legible gap that a resolving party can evaluate; an undeclared absence is not legible and is not a valid operating state.

Causal-formative: the indicators cause or constitute the construct rather than reflecting it. The validation regime is selected by the direction of the indicator-construct relation, not by a latent-construct network. This distinction is adopted with the dissent in the measurement literature named rather than resolved.

Composite-aggregate: the object is a stipulated weighted combination of indicators. Validity does not apply to a composite-aggregate object. The declaration specifies what sub-claims are combined, how they are weighted or ordered, and what the composite is claimed to represent, and does not assert a nomological-network validity claim. A composite-aggregate object declared as criterion-type or as a reflective construct is mis-declared.

A construct's indicator direction can be contested or undecidable by inspection. The declaration discipline governs: the chain declares and justifies the indicator direction from the decision context, and the resolving party assesses the coherence of the declaration rather than reading the property off the object.

**Enabling context conditions.** The specification must name the conditions that must be present in the external context for the evaluation's mechanism to produce valid outputs. These are enabling context conditions: they name what the evaluation requires of its environment to function as designed.

Enabling context conditions are distinct from the exclusion conditions required by the first paragraph of this condition. Exclusion conditions name states of the world that make the evaluation invalid when present. Enabling context conditions name states of the world that must be present for the evaluation to function. An evaluation run in the absence of an enabling context condition may satisfy all six conditions as written while producing outputs that are not interpretable for the decision.

**Risk reduction statement (required).** The specification must state what risk this chain reduces, for whom it reduces it, and what would demonstrate that the chain is no longer reducing that risk. The risk reduction statement is not the same as the falsifiability statement, though the two are connected. The falsifiability statement names the test by which the chain output can be shown to be wrong. The risk reduction statement names what is at stake when that test fails: whose exposure to hazard increases when the chain misjudges.

The specification must identify the three inputs that combine to produce risk: the hazard (the latent condition with harm potential), the uncertainty (the epistemic gap about probabilities and outcomes), and the exposure (the degree of contact between a party and the hazard). The chain's specification must state which of these three inputs it is designed to address, and for whom.

This distinction matters: a chain that reduces uncertainty for the operator does not necessarily reduce exposure for the risk-bearer. A chain that names its purpose as uncertainty reduction while leaving the risk-bearer's exposure unchanged has not addressed the risk it may appear to address.

**Risk-bearer identification (required).** The specification must identify who bears losses when the chain fails. Risk-bearers are the parties whose exposure to the hazard increases when the chain produces incorrect outputs. They are not necessarily the same as the parties who control the chain, who operate the chain, or who benefit from the chain's outputs under normal conditions.

A funding program's administrators do not bear the primary risk of an evaluation chain that systematically excludes certain kinds of work; the applicants whose work is misclassified, and the people that work would have served, bear it. As a rule, the party that operates an evaluation chain is frequently not the party most exposed to its errors.

Risk-bearer identification is a required declaration because the parties most exposed to chain failure are frequently absent from the specification design process. Making that identification explicit in the specification is the structural mechanism by which their exposure enters the design before data collection begins.

This element is a carried requirement: the risk-bearer identification, once named here, must be present at every downstream stage. A gate, criterion, instrument, or decision logic that does not account for the exposure of the identified risk-bearers is out of compliance with the decision context, in the same way that one applying to a different population than the boundary population is. A risk-bearer named here and then consulted only at entry has been declared but not carried.

**Affected-party reach ceiling (risk-bearer identification above the ceiling).** When the chain's affected population is past the affected-party reach ceiling specified in the Coordination Scaling Standard Section 10, the risk-bearers identified here cannot be named by direct knowledge: the affected population exceeds what the deploying organization can identify and reach, so an impressionistic naming of who bears the loss is the structural fingerprint of the crossing rather than a reliable identification. Above the reach ceiling, risk-bearer identification must route through the structurally authorized proxy or guardian channel the Structural Power Obligation Standard Section 4.1 specifies, which the Coordination Scaling Standard makes a minimum condition above the ceiling; an impression of the risk-bearer held by the deploying organization does not satisfy this requirement above the ceiling. The honest scope of that routing is legibility of the affected-party relationship, not knowledge of the affected parties' full exposure: the identification becomes answerable rather than impressionistic, not complete. Below the reach ceiling, direct identification of risk-bearers suffices and the channel is not required by scale.

For population-level chains, an additional declaration is required: the specification must name why individual-instance falsification is not the appropriate evaluation unit for this domain. This prevents domain complexity from serving as an unverifiable defense against accountability. A justification is acceptable only if it names the specific property of the domain's risk structure that makes calibration-based evaluation the appropriate framework.

**Adversarial threat model (required).** The specification must declare the adversarial threat model for this chain. Required content: who are the potential adversarial actors for this chain, what do they know about its specification, and what is their capability and motivation to produce inputs that satisfy the conditions while defeating the chain's purpose?

The adversarial threat model must also name scale-based coordination function breaks as an explicit threat class. Scale-based coordination function breaks do not require an adversarial actor with specialized knowledge of the chain specification; they exploit the organizational context in which the chain operates. When the deploying organization's coordination functions have broken at its effective scale, the chain's feedback mechanism and adversarial gate have structural gaps that any actor can exploit without reverse-engineering the specification. The threat model must state: what CSS effective Radius the chain was designed to operate at, and which attack surfaces named in the Coordination Scaling Standard become active when the deploying organization operates below CSS minimum conditions for that Radius.

The adversarial declaration belongs in Condition 1 because it is a design input to every subsequent condition. A chain specified with this declaration in view produces different instrument choices at Condition 3, different calibration benchmarks at Condition 4, and different detection thresholds at Condition 6 than a chain specified only for honest use. A chain that names no adversarial actors has implicitly declared that it faces no adversarial threat. That declaration must be made explicitly if it is the intended position, because the independent attester is responsible for assessing whether it is accurate.

The adversarial threat model field does not replace the adversarial robustness conditions in Condition 3. The threat model is the design input; the robustness conditions are the instrument-level response. Both are required.

This condition is prior to all others. An ontology that is not derived from a decision context is a folk ontology. Measurement instruments that are not derived from an ontology are data collection processes without a defined purpose. The decision context is what makes every downstream specification choice principled rather than arbitrary.

A system that begins by designing measurement instruments and then retrospectively articulates a decision context has inverted the chain. The decision context must be the prior constraint, not the post-hoc rationalization.

### Condition 2 (Technical Ontology Adequate to the Decision Context)

The constructs the evaluation claims to measure must be defined operationally: precisely enough that two independent observers applying the definition to the same phenomenon would reach the same classification in the overwhelming majority of cases, and explicitly enough that the exclusion criteria are stated alongside the inclusion criteria.

An ontology adequate to a decision context is one where every category required by the decision is present, and where every category in the ontology is required by the decision. An ontology with categories that do not map to the decision context is measuring the wrong things. An ontology missing categories required by the decision context is leaving the decision unsupported.

**Construct-to-estimand adequacy statement.** The specification must state the grounds on which the ontology constructs are adequate to operationalize the estimand declared in Condition 1. Grounds take one of three forms: empirical validation (the constructs have been shown to predict or track the estimand-relevant outcome in the relevant population); logical derivation (the constructs are necessary and sufficient components of the estimand by the definition of the estimand itself); or documented precedent (the constructs have been validated against this estimand class in a comparable population, with the validation study cited).

This requirement applies PFDS Corollary 1 (Operational Definition) to the bridge between this condition and Condition 1: the claim "this ontology is adequate to operationalize this estimand" is itself a claim that must meet the independent observer test. A specification that states what it measures without stating why that constitutes an operationalization of the estimand has not closed the gap between Condition 2 and Condition 1. The adequacy claim depends on the specifier's judgment unless the grounds are explicitly stated and auditable.

The specification must also state the conditions under which the ontology would be judged inadequate for the estimand: what evidence or findings would require the ontology to be revised. An adequacy claim without stated falsification conditions is an assertion, not a specification element.

The adequacy grounds must apply to the risk-bearers identified in Condition 1, not merely to a formally similar population or estimand class. Empirical validation against a population that excludes the actual risk-bearers, documented precedent from a domain where cost-bearers occupy different structural positions, or logical derivation that holds for the estimand in the abstract but not as applied to the parties who bear the cost of an invalid operationalization: each of these satisfies the precision dimension of this requirement while leaving the non-harming dimension unaddressed. An adequacy claim grounded in a population or context that does not include the actual risk-bearers has been derived from the precision dimension of the unified PFDS principle only.

**Temporal scope declaration.** For each construct, the specification must declare whether it is a present-state construct (its value is measured at the time of the evaluation), a predictive construct (its value at the time of the evaluation is a proxy for a future-state outcome), or a historical construct (its value is derived from past observations). This declaration is required because construct validity requirements differ by temporal scope: the inferential distance between measurement and decision-relevant outcome is different in each case.

A present-state construct used as a proxy for a future-state claim requires the inferential step to be declared at this condition and validated at Condition 3. Leaving the inferential step implicit is a specification gap that produces the same structural failure as an implicit design choice in Section 3: the assumption cannot be audited because it was never stated.

Known gaps in the ontology must be stated. Unstated gaps become invisible failure modes that produce systematic errors indistinguishable from valid output.

### Condition 3 (Valid Measurement Instruments within the Ontology)

The instruments used to collect data must actually measure the constructs specified in the ontology, and must be specified to resist the failure modes relevant to the domain.

A measurement instrument for a financial construct must specify the adversarial robustness conditions: what market conditions, manipulation strategies, or coordinated actor behavior would cause the instrument to produce a false reading, and what requirements the instrument must satisfy to resist those conditions.

A measurement instrument for a qualitative construct must specify the inter-rater reliability conditions: what criteria must be present for two independent evaluators to produce the same classification from the same evidence.

An instrument with no specified failure mode is not a measurement instrument. It is a data collection process whose relationship to the construct it claims to measure is unverified.

**Uncertainty quantification as a carried requirement.** Every measurement instrument specification must include a statement of the instrument's uncertainty. Uncertainty in the metrology sense is the range within which the true value is expected to lie, given the instrument's known error sources. This range is not optional supplementary information about the instrument; it is part of the instrument's specification.

The uncertainty statement must distinguish two classes of error. Systematic error is directional: it pushes measurements consistently in one direction, and it compounds at every downstream stage. Random error is non-directional: it varies across measurements and averages out across a sufficient number of observations. An instrument can have both. An instrument specification that does not name its systematic error sources leaves downstream stages unable to account for the direction of the bias.

Systematic uncertainty is a carried requirement. Once named at this stage, it must be referenced in Condition 4 and in Condition 5. A decision threshold specified without reference to the instrument's systematic uncertainty may fall within the range the instrument cannot resolve, making the threshold operationally meaningless even if formally pre-specified.

**Resolution floor (cohort-size declaration).** Random error averages out only across a sufficient number of observations. An instrument specification whose uncertainty depends on cohort size must declare the cohort size below which the instrument cannot resolve a reading against the Condition 4 thresholds it feeds. Below the declared floor the instrument's statistical output is not relied upon, and the chain neither runs the statistical conditions as though they had resolved nor falls silent. It routes to the determinate-resolution signal class (Section 7.2, fourth condition), which does not depend on statistical power and so remains valid at any cohort size, recording the outcome as `indeterminate` (Section 12.2) where the statistical reading cannot be resolved; and where the chain accumulates evidence over time it aggregates across collection periods toward the floor, using the calibration-tracking process declared for population-level chains, rather than exempting the small cohort from evaluation. Exemption below the floor is refused because the party most exposed to a missed finding is the risk-bearer identified in Condition 1, for whom the un-run evaluation is the costly failure. An undeclared floor is the small-cohort form of the failure this condition already guards: an instrument run below the size at which it can resolve produces readings it cannot support, recorded as though it could.

**Multi-hop inferential validation.** When the evaluation chain contains multiple inferential steps between the measurement instrument and the decision-relevant outcome, each step requires independent validation against the decision-relevant outcome, not against adjacent proxy constructs.

The full inferential chain must be declared: the specification must name every intermediate construct between the measurement instrument and the decision context declared in Condition 1, and must state the validation evidence for each inferential step. A step validated only against adjacent constructs (instrument measures construct A, construct A correlation with construct B is validated, but construct B's relationship to the decision outcome is not validated) does not satisfy this requirement.

The principle is general: every evaluation chain in which instrument scores substitute for direct measurement of the decision-relevant outcome must demonstrate that the substitution is valid, not merely assumed. A funding program that scores expected impact and then validates that score only against a proxy, such as a team's prior funding or its reputation, rather than against the outcomes the funding was meant to produce, has not validated the inferential step that carries the decision. The instrument's internal consistency does not rescue it; the substitution of proxy for outcome was never shown to hold.

A multi-hop failure has a characteristic shape: a chain of two or more inferential steps, each plausible on its own, where no single step is validated against the decision-relevant outcome. A program that funds on the chain "a team ships code, shipped code indicates capability, capability indicates future impact" has three steps and may have validated none of them against realized impact, yet the chain can appear rigorous because each link cites the one before it. The appearance of validity is produced by the citations between adjacent steps, not by any step reaching the outcome.

**Calibration measurement instrument (for population-level chains).** For evaluation chains operating in domains with irreducible per-instance uncertainty, where calibration-based evaluation is the appropriate framework as declared in Condition 1, the specification must declare how actual accuracy is tracked against the calibration benchmark over time. This is a distinct instrument from those measuring individual instances: it specifies the data collection and tracking process that enables Condition 4's calibration benchmark to function as an operative criterion rather than a stated aspiration.

### Condition 4 (Pre-Specified Evaluation Criteria)

The thresholds, rubrics, and criteria that determine whether a data point or claim is accepted or rejected must be specified before any data is collected or reviewed. Criteria specified after observing the data are adjusted to the data. Criteria adjusted to the data cannot distinguish signal from noise; they optimize for the appearance of coherent output rather than for the accuracy of the evaluation.

Pre-specification is necessary but not sufficient. A pre-specified criterion must itself be falsifiable: it must specify the conditions under which a data point would be rejected. A criterion that accepts all data points under all conditions is not a criterion; it is a formal structure with no functional content.

**Threshold meaningfulness below the resolution floor.** A threshold relied upon below the instrument's declared resolution floor (Condition 3) is operationally meaningless in the same way as a threshold that falls within the range the instrument's systematic uncertainty cannot resolve: in both cases the criterion is formally pre-specified, but the instrument cannot produce a reading that resolves against it. Where a chain may operate below the floor, the criteria specification must state that outcomes in that region are recorded as `indeterminate` (Section 12.2) rather than forced to an accept or a reject the instrument cannot support.

Pre-specified criteria without adversarial gate conditions are gamed under high-stakes incentives. A funding program that accepts a simple count, such as the number of users a project reports, as its success criterion will find that grantees optimize the count rather than the value beneath it: users are registered who never return, or the metric is defined in whatever way is easiest to report. The criterion was stated before evaluation began, which is necessary, but its statement alone did not make it robust to an applicant with an incentive to satisfy the letter of it.

**Criterion standard anchoring (for criterion-type chains).** For chains declaring a criterion-type claim in Condition 1's claim object type declaration: the evaluation criteria must reference the declared criterion standard. The criteria are anchored to that standard; the attesting party's review confirms that the criteria are calibrated against the standard, not solely against the chain operator's internal judgment.

If the Condition 1 declaration states that no established criterion standard exists, the evaluation criteria must include the evidence basis named in the claim object type declaration. The criteria do not gain external anchor from an established standard in this case; they are assessed against the evidence basis declared in Condition 1, and the absence of an established standard is a finding that the attester must note.

For construct-type chains: the evaluation criteria must be consistent with the nomological network declared in Condition 1. Criteria that measure surface properties rather than the constructs specified in the nomological network are an ontology-criteria mismatch. This mismatch must be identified before deployment, not after.

**Calibration benchmark (for population-level chains).** For evaluation chains operating with a calibration framework as declared in Condition 1, a calibration benchmark is required in addition to individual-instance acceptance thresholds. The calibration benchmark must state: what accuracy rate is necessary to meaningfully reduce the risk named in Condition 1's risk reduction statement, declared before data collection begins.

The benchmark must state its basis: whether it derives from self-declared expectations or from externally validated domain benchmarks. Self-declared benchmarks satisfy the pre-specification requirement; they do not require external validation authority to exist before the specification can be written. The basis must be stated because the independent attester's sandbagging check applies to calibration benchmarks as it applies to all acceptance criteria: the attester confirms the benchmark is not set so low that chain failure is structurally undemonstrable regardless of actual performance.

Benchmarks are revised upward over time as domain performance data accumulates. Each revision is governed by the same pre-specification discipline: the revised benchmark is declared before the next collection period begins, not after observing the results. This revision is a Condition 6 event: observed calibration performance propagates back to Condition 4 criteria and to Condition 1's risk reduction statement.

### Condition 5 (Explicit Decision Logic)

The logic by which evaluation outputs produce decisions must be specified in writing before any outputs are produced. Implicit decision logic embedded only in code or process is not CRAFT-compliant.

Explicit decision logic makes two things possible that implicit logic cannot provide: independent verification that the logic matches the stated decision context, and accountability for cases where the logic produces outcomes that diverge from the decision context's stated intent.

Where decision logic is implemented in executable code, the code is a valid implementation of the decision logic, but the decision logic specification must still exist as a readable document that can be evaluated independently of the code. Code is an implementation; it is not a specification.

**Consequence level declaration.** The decision logic specification must declare the consequence level of the chain's primary claims: the potential harm magnitude to the risk-bearers identified in Condition 1 if the chain produces incorrect outputs that are acted on. The consequence level must state: what level applies (high, medium, or low, with the basis for the classification), who bears the harm in the high-harm scenario, and what adversarial review intensity that consequence level requires.

The consequence level calibrates the adversarial gate intensity. High-consequence claims require more rigorous adversarial review than low-consequence claims. A high-consequence claim that specifies only standard adversarial gate review without justification is a compliance gap: the decision logic specification must explain either that the claim's consequence level does not require elevated gate intensity or that the gate intensity has been calibrated to the declared consequence level. This requirement implements the PFDS Corollary 10 consequence-calibrated evidence bar at the chain level: the evidence standard required to support a claim scales to the harm potential of acting on a false version of that claim.

**Coupled evaluation-intervention structure.** Some evaluation chains are structured such that the evaluating entity and the intervening entity are the same party acting on the same subject. In these chains, the evaluation output does not travel to an external consuming system; it feeds back into the evaluating party's own actions on the entity being evaluated. The standard CRAFT Condition 5 model assumes evaluation and intervention are separable: outputs travel to consuming systems external to the chain, and Condition 5 specifies how those outputs produce effects in those systems.

In coupled structures, Condition 5 changes character. The evaluation IS the intervention in a functional sense, and the specification must reflect this. Three additional requirements apply to coupled structures:

The evaluation scope and the intervention scope must be separately specified at entry. Consent to being evaluated is structurally distinct from consent to the specific interventions that evaluation findings may trigger. These cannot be collapsed into a single consent declaration.

Each evaluative action that may trigger an intervention must specify what intervention it may trigger, before the evaluation begins. A standing claim about what the evaluation produces in the subject is not sufficient; the action-to-intervention mapping must be explicit for each class of evaluative finding.

The feedback loop between evaluation output and intervention action must be declared as a carried requirement through Condition 6: when an intervention triggered by an evaluation finding produces outcomes that were not anticipated, that signal propagates back to both the evaluation specification and the intervention scope specification.

### Condition 6 (Feedback Mechanism with Propagation)

The evaluation chain must include a mechanism by which detected errors propagate back to every prior stage. A feedback mechanism that corrects individual outputs without evaluating whether the error reflects a structural gap at a prior stage does not satisfy this condition.

A confirmed error at the data point level must be evaluable against the measurement instrument specification, the ontology specification, and the decision context document to determine whether the error is isolated or systemic. A systemic error requires revision of the relevant stage specification, versioning of the revised specification, and assessment of prior outputs produced under the superseded specification.

A nominally compliant feedback mechanism (a dispute endpoint exists) is not sufficient. The feedback mechanism is operative only if confirmed disputes trigger genuine re-evaluation at prior stages. The test of operativeness is whether the feedback mechanism has ever caused a specification revision. A feedback mechanism with no revision history is a candidate for adversarial gate review.

**Loop depth requirement.** The feedback mechanism must support three depths of response, addressing structurally different objects at each depth.

Single-loop response corrects a specific instance within the existing response framework. It applies the designated fix to the individual failure without questioning the framework that produced it. Single-loop response is appropriate when the failure is isolated and the framework is not implicated.

Double-loop response revises the response framework when that framework is generating failures. Double-loop is triggered when a class of failures persists despite correct single-loop responses at each instance: the pattern signals that the framework is the source, not the instances. Double-loop examination produces revisions to evaluation criteria (Condition 4), ontology definitions (Condition 2), or measurement instrument specifications (Condition 3).

Triple-loop response examines the values and commitments that generated the decision context (Condition 1). It is triggered when the coordination system cannot process its own error signals through either single-loop or double-loop correction: the structure that produced the decision context is generating failures that the evaluation framework, even when revised, cannot address. Triple-loop examination produces revisions at Condition 1 or, in cases where the decision context itself reflects values that require examination, produces a recommendation to suspend the chain pending decision context re-specification.

The ASEP (Adverse Signal Engagement Protocol) structure for Cynefin-domain-conditional loop routing establishes the structural grounding for this requirement: systems that structurally prevent the transition from single-loop to double-loop cap themselves at single-loop learning regardless of signal volume. The same principle applies here. A feedback mechanism with correct propagation paths but no specified loop depth requirement can satisfy the propagation path requirement of this condition while being structurally incapable of the learning that would prevent systematic failures from recurring. The Structural Consent Legibility Standard (SCLS) Section 6.3 provides the mechanism explanation: systems that do not invest in ontological bandwidth structurally cap themselves at single-loop learning.

Frame Language consequence: a Uniplex authority structure controlling the decision context (Condition 1) is structurally incompatible with genuine triple-loop feedback, because revising the decision context requires authority that the evaluation chain does not hold. Frame Language assessment detects this blockage at design time. A specification whose decision context is controlled by a Uniplex authority structure must declare this as a known constraint on triple-loop capacity, and the independent attester must note it in the attestation record.

**Deployment-context evidence as a named feedback trigger.** Deployment-context evidence is a distinct feedback trigger category alongside instance-level findings and calibration drift. A chain whose declared scope (from Condition 1) no longer accurately represents the actual population or use context in which the chain is operating has an external validity failure at the chain level. The feedback protocol must include a mechanism for detecting when the deployment context has diverged from the declared scope. When divergence is confirmed, the signal propagates back to Condition 1's scope declaration using the same propagation requirements as instance-level findings. Systematic divergence (the chain is routinely used outside its declared scope) is a double-loop trigger: the scope declaration, and potentially the decision context, requires revision.

**Deployment scale context declaration (required).** The feedback protocol specification must include a deployment scale context declaration with three fields:

`effective_radius`: the CSS effective Radius at which the deploying organization is assessed to be operating at chain deployment. This is the Radius at which CSS minimum conditions apply for this chain's feedback mechanism.

`minimum_css_conformance`: the CSS adoption architecture level required for this chain's Condition 6 requirements to function as specified. A chain specifying propagation targets that depend on role legibility cannot credibly guarantee its feedback protocol will function below CSS-Operational (the minimum conditions level at which role legibility and coordination operability are installed). Permitted values: `css-assessed`, `css-operational`, `css-instrumented`, `css-loop-closed`, `css-auditable`.

`conformance_gap_handling` (required when the deploying organization does not currently meet the declared minimum): a prose statement of how the feedback protocol accounts for the CSS minimum condition gaps. This field makes explicit what would otherwise be a hidden structural assumption. A chain whose feedback protocol requires coordination operability but whose deployment scale context acknowledges a gap in CSS-Operational conformance has made a legible declaration; a chain that simply omits the declaration has made no claim and produced no legible gap.

For population-level chains: the deployment scale context declaration must additionally state how the chain's long-term calibration tracking infrastructure meets the CSS infrastructure integrity requirement (Radius 150 minimum condition) for the chain's intended operational lifetime. Population-level chains that track calibration drift across time require organizational infrastructure that must survive organizational changes; this infrastructure requires named redundancy. A population-level chain that cannot demonstrate this either acknowledges the gap in the `conformance_gap_handling` field or operates below the CSS conformance level required for its calibration drift detection to function.

**Version monitoring in lifecycle persistence.** The lifecycle persistence commitment must name version monitoring as a responsibility: a declared procedure for detecting revisions to any inherited standard listed in the inheritance receipt (Section 10), and a specified response when a revision occurs. When an inherited standard revises, the inheritance receipt enters a version-bump-pending state for that standard until the new version's obligations are assessed and the receipt is updated. This version-bump-pending state is a Condition 6 feedback event at the specification layer: it propagates to Section 10 and requires re-assessment of the affected standard's obligations before the receipt is declared current. The propagation requirement applies at the specification layer in the same way it applies at the data evaluation layer: a revision that does not trigger re-assessment of the affected downstream declarations is a propagation failure.

**Calibration drift (for population-level chains).** For evaluation chains operating with a calibration framework, systematic directional drift in population outputs is a chain failure signal even when no individual prediction error is statistically anomalous. Calibration drift means the chain's accuracy is moving systematically in one direction across a population of outputs over time.

Calibration drift is a double-loop trigger at minimum: when drift is confirmed, the specification requires revision of the calibration benchmark (Condition 4) and examination of the ontology (Condition 2) for constructs that have shifted meaning over the evaluation period. Persistent drift after double-loop revision (the revised benchmark continues to show drift after the next collection period) escalates to triple-loop: examine whether the decision context itself has changed in a way that makes the original estimand no longer appropriate.

Calibration drift must also be examined for scale-induced cause. If the deploying organization's CSS effective Radius has changed since the chain was specified, the calibration drift may originate in a coordination function break rather than in the chain's measurement design. The CSS Radius change is both a Condition 6 double-loop event and a CSS scale threshold signal: the two obligations run simultaneously.

**Direction-origin validation.** The feedback mechanism must support examination from at least two directional origins before any revision is accepted as complete. The deploying organization's directional origin is insufficient on its own, because the deploying organization's interpretive framework constitutes a concentration of what counts as correct assessment. Different directional origins reveal structurally different failure classes at the same loop depth.

Running triple-loop from the deploying organization's directional origin asks: what values and commitments generated our criteria? Running triple-loop from the affected party's directional origin asks: what values and commitments generated the premise that the deploying organization defines what matters? These are different questions. The second is invisible from the first. Both are required for the feedback mechanism to be capable of detecting the full class of failure modes this condition is designed to surface.

The structural grounding is the Structural Power Obligation Standard (SPOS) Section 3.2 (Lukes' third dimension of power) and the Information Asymmetry Classification Standard (IACS) Class 3 (Interpretive Asymmetry).

**Affected-party directional origin past the reach ceiling.** When the chain's affected population is past the affected-party reach ceiling (Coordination Scaling Standard Section 10), the affected party's directional origin cannot be obtained by direct reach, for the same reason risk-bearer identification cannot at Condition 1. The affected-party directional origin must then enter through the structurally authorized proxy or guardian channel the Structural Power Obligation Standard Section 4.1 specifies; an impression of the affected party's directional origin held by the deploying organization does not supply the second directional origin above the ceiling. The channel makes the affected-party directional origin legible, not fully known; the requirement is that the second directional origin enter through a structurally authorized channel rather than through the deploying organization's impression of it.

---

## 6. Compliance Requirements

### 6.1 Specification compliance

A CRAFT-compliant evaluation chain requires, before any data collection or evaluation activity begins:

**Published specification documents.** A specification document for each of the six conditions, versioned, dated, and publicly accessible. Each document must be derived from and traceable to the prior stage's specification. A specification document that cannot be traced to the decision context document does not satisfy this requirement.

**Independent overturning basis.** The chain must secure the non-self-adjudication invariant (Section 7.2): the basis on which its output can be overturned is not controlled by the operating organization. This is realized either by ex-ante designated attestation, each specification document attested before data collection by a trusted interpretive intermediary independent of the operating organization, confirming internal consistency, derivability from the prior stage, non-vacuous criteria, and accurate risk-bearer identification; or by ex-post adversarial challenge resolved against the Condition 4 criteria by a resolver set the operating organization does not control, per Section 7.2.

A resolving party with a financial or coordination interest in the outcome does not satisfy the requirement under either realization.

**Adversarial robustness verification.** As an extension of the attestation requirement, the attesting party must verify that the conditions hold under adversarial conditions consistent with the threat model declared in Condition 1. This includes confirming that the declared threat model is not understated in a way that makes adversarial failure structurally undemonstrable: a threat model that names no adversarial actors or names only implausible adversarial actors provides a formal structure for the adversarial gate check while ensuring the gate can never produce a failure finding. Independent attestation is the structural defense against this form of sandbagging.

When the chain declaration includes a deployment scale context with a conformance gap, the attesting party's review must assess whether the gap handling statement adequately accounts for the structural limitations it acknowledges.

**Adversarial gate compliance.** For each specification document, the operator must demonstrate that the specification produces rejections under realistic adversarial conditions. A specification that has never produced a rejection under any realistic test condition is a candidate for re-examination. The adversarial gate is not a single test; it is an ongoing check that the specification retains functional content as conditions change.

### 6.2 Operational compliance

A CRAFT-compliant evaluation chain in operation:

**Produces an evaluation record for each input processed.** The evaluation record must reference the specific version of each specification document in force at the time of evaluation, document the gate check results, identify the collection provenance, state the outcome (accepted or rejected), name the specific condition that triggered rejection if rejected, and carry layer attribution identifying which level of the architectural hierarchy produced each finding. See Section 12 for the evaluation record schema requirements.

**Publishes rejection records.** Each rejection, including the specific condition that caused rejection and the data values at time of evaluation, is logged publicly. Rejection records are part of the compliance record; a compliance record with no rejections is a flag for adversarial gate review.

**Implements the feedback protocol.** Disputes can be filed, reviewed, and resolved according to the published Feedback Protocol. The resolution record, including any specification revisions triggered, is part of the compliance record.

### 6.3 What CRAFT compliance does not guarantee

CRAFT compliance establishes that the structural conditions for a valid evaluation were present. It does not guarantee:

That the evaluation was conducted by competent evaluators. CRAFT specifies the structure; it does not specify the expertise required to execute the evaluation within that structure.

That the decision context was correctly specified. A correctly structured evaluation that answers the wrong question is CRAFT-compliant and wrong. The decision context specification is the responsibility of the operator; CRAFT requires that it be articulated, not that it be correct.

That all validity dimensions have been satisfied. CRAFT compliance creates the structural preconditions for valid claims. Salaudeen et al. (2025) establishes a five-form validity framework (content, criterion, construct, external, consequential) whose requirements are implemented in CRAFT's conditions: criterion-type and construct-type claim grounding in Condition 1; construct-to-estimand adequacy in Condition 2; instrument validity in Condition 3; criterion anchoring in Condition 4; consequence-calibrated gate in Condition 5; external validity detection in Condition 6. This version implements the claim-level and consequence-calibrated additions. Multi-party attestation role declarations (collective review requirements from Salaudeen Section 7) remain pending; they constitute a consequential validity architectural change to Condition 4 beyond the criterion anchoring addition and require their own sensemaking session before specification.

---

## 7. The Enforcement Layer

The three enforcement mechanisms are not separable. Each addresses a failure mode that the others cannot.

### 7.1 The adversarial gate

The adversarial gate tests whether a specification is genuinely falsifiable as stated. Its role is to catch specifications that satisfy the formal requirements for pre-specification while being designed (intentionally or not) to always pass. A specification that has never rejected a data point is not a specification in the meaningful sense; it is a formal label attached to acceptance.

The adversarial gate is applied:

At specification review: does the specification produce rejections under realistic test conditions consistent with the declared threat model?

At attestation: does the gate check produce rejections in normal operation?

At compliance review: has the specification produced rejections over its operating history?

An organization that operates its evaluation chain for an extended period without a single rejection should examine whether its adversarial gate is functioning. Zero rejections is a candidate failure mode, not a performance metric.

The adversarial threat model declared in Condition 1 is the reference for the adversarial gate check: the gate tests the specification against adversarial conditions consistent with the declared threat model. A threat model that excludes realistic adversarial actors makes the gate check structurally unanswerable. This is the specific failure mode the adversarial robustness verification in Section 6.1 is designed to prevent.

### 7.2 Non-self-adjudication

Independent attestation in the prior version is one realization of a more general requirement. The structural problem it answers is specification gaming: a coordination actor that controls both the specification and the determination of whether the specification was met can write the specification to always pass. The invariant that answers it: the basis on which a chain's output can be overturned must not be controlled by the party whose claim is being evaluated.

This invariant is CRAFT's inheritance of the Precision-First Design Standard, not a CRAFT-native principle. It is the independent-observer definition (no direct interest in the outcome; structural distinctness from the decision-making body), the trusted-interpretive-intermediary definition (a body whose determinations are not structurally controlled by any party with a direct interest in the outcome), and Corollary 8 (external falsifiability), applied to the overturning of a chain's output.

The invariant admits two realizations. A chain declares which realization it uses and justifies, structurally rather than nominally, how the resolving party's disinterest is secured.

**Realization A, ex-ante designated attestation.** A trusted interpretive intermediary, identified in the attestation record with reputational exposure and no financial or coordination interest in the outcome, attests before data collection that the specification holds. The attesting party reviews the specification for genuine falsifiability rather than formal completeness; reviews the risk-bearer identification declared in Condition 1 for accuracy and completeness; assesses whether the declared adversarial threat model is realistic given the chain's domain and specification; assesses whether the deployment scale context declaration is consistent with the chain's feedback protocol requirements; and documents the basis for the attestation, including any conditions required of the operator before attesting. An anonymous attestation does not satisfy this realization.

**Realization B, ex-post adversarial challenge.** The output is accepted provisionally against the Condition 4 criteria and is overturnable by a bonded challenge resolved against those pre-specified criteria by a resolver set the claimant does not control. A successful challenge propagates under Condition 6 exactly as an attestation-side correction does, including the isolated-versus-systemic evaluation.

**Required of both realizations.** The disinterest of the resolving party is declared and structurally justified, not asserted by form. The required strength of the disinterest guarantee scales with the consequence level declared in Condition 5: this inherits the Precision-First Design Standard consequence-calibration, under which higher-consequence claims require greater independence of the validating party. Realization B is available at low and moderate consequence; a high-consequence claim requires Realization A, or a Realization B hardened to the independence Realization A provides, with the hardening justified.

**Required of Realization B.** Four structural conditions, each of which Realization A satisfies by construction.

First, disclosure of the resolver set's power distribution. A resolver set is a power-distribution structure under the Structural Power Obligation Standard. The declaration discloses how the capacity to render binding resolutions is distributed: where that capacity derives from stake, both stake-weighted and participation-weighted distribution; the concentration of interpretive capacity over what counts as a correct resolution (Information Asymmetry Classification Standard Class 3); and the external-override exposure of the resolution to a single party whose interests diverge from the cost-bearing parties, stated as the cost of corrupting the resolution relative to the value extractable from the specific claim.

Second, a manipulability floor on the resolution mechanism. A resolver set is itself manipulable, through collusion, bribery, or sybil participation. The declaration characterizes the manipulation surface, names the robustness property the bonding and resolution design buys, and discloses the residual manipulability and the claim-value threshold above which the truthful resolution stops being the equilibrium. A claim of disinterest that names only the cost of corruption, without naming what the resolver set is disinterested toward and the conditions under which it is captured, does not satisfy this condition.

Third, direction-origin validation extended to the resolver. The resolver set is one directional origin. The cost-bearing-party directional origin that Condition 6 requires is not supplied by the resolver and remains owed.

Fourth, availability bounded to determinate-resolution claims. Realization B is available only where disputes about the claim have a resolution a resolver set can converge on without resolving a latent construct: criterion-type claims with a named criterion standard; constitutive or stipulative checks where the instrument is the object; and the computational layer of a composite-aggregate claim (inputs-as-declared and aggregation-rule-applied-correctly). It is not available for reflective or causal-formative construct claims, where the resolution is not resolver-determinate; those keep Realization A. For a composite-aggregate claim, a Realization B challenge resolves the computation, not the validity of the composite, because validity does not apply to a stipulated composite.

### 7.3 The feedback mechanism

The feedback mechanism is the correction layer. Its role is to ensure that the evaluation chain is a learning system, not a static one. The test of an operative feedback mechanism is whether confirmed errors produce specification revisions.

The propagation requirement is the critical condition: a feedback mechanism that corrects individual outputs without tracing the error to its stage of origin does not close the chain. It produces a patched output and a structurally unchanged chain. The same class of error will recur.

The loop depth requirement (Condition 6) applies to the feedback mechanism: a mechanism that can only correct individual instances without examining the framework that produced them satisfies the propagation path requirement while being structurally incapable of preventing systematic failure recurrence.

The propagation requirement applies in both directions: upstream (from output to the stage that produced the error) and downstream (to all outputs produced under the same specification version that may share the same error). Both directions must be operational for the feedback mechanism to satisfy the condition.

---

## 8. Domain Application Inheritance

A domain application of CRAFT is a CRAFT implementation specialized for a specific domain through inside analysis of that domain's evaluation failure modes. The relationship between CRAFT and a domain application is structural inheritance: the domain application inherits all normative requirements from this specification and adds requirements specific to the domain.

A domain application is non-compliant with CRAFT if it:

Omits any of the six conditions without explicit justification and a documented equivalence argument.

Weakens any normative requirement relative to this specification.

Adds requirements that contradict any normative requirement in this specification.

A domain application may add requirements that are stricter than CRAFT's normative requirements. Stricter requirements do not constitute non-compliance.

**The inside analysis requirement.** A domain application cannot be produced by mechanical translation of CRAFT requirements into domain-specific language. It requires inside analysis: examination of the specific evaluation failure modes present in the domain, derived from operational experience or detailed case study research within the domain. The domain application's requirements must be traceable to that analysis.

A grants evaluation domain application, for example, would be produced from inside analysis of grant evaluation failure modes; a different domain would be produced from inside analysis of its own. Each domain requires the same process, and the analysis is not transferable between them.

**The machine-only domain constraint.** The construction grammar and inheritance requirements (Sections 9 and 10) must be satisfiable by domain applications that operate entirely machine-to-machine. A specification running an automated data pipeline with no human intervention is fully accommodatable by the grammar. Any proposed requirement that cannot be satisfied by a machine-only domain is a failure in the proposed requirement, not a domain conformance failure. This constraint applies to all sections of this specification.

---

## 9. Construction Grammar for Domain Applications

This section specifies what a CRAFT-conformant domain application must contain beyond satisfying the six conditions. A domain application that satisfies the six conditions but does not meet the construction grammar requirements is a chain quality standard, not a CRAFT-conformant domain application. A third party evaluating a domain application for CRAFT conformance must check both.

### 9.1 Structural operativity requirement

Each of the six conditions must be structurally operative in the domain application's execution architecture, not compliance-scheduled. The distinction is functional, not terminological.

A condition is structurally operative when:

It is present in the execution path: it runs as a check on every instance of the process the condition governs.

It cannot be bypassed without that bypass being a detectable adverse signal that enters the feedback loop.

Its output is logged as a coordination record entry, not as a periodic compliance report.

A condition is compliance-scheduled when it runs as a periodic audit, a manual review triggered by external request, or a check that can be bypassed by operational decision without triggering a detectable signal. Compliance-scheduled conditions satisfy the letter of the six conditions while being structurally absent from the execution path.

The domain application specification must declare, for each of the six conditions, how that condition is made structurally operative in the domain's execution architecture. A domain application that cannot make this declaration for any condition must name the constraint and propose a structural equivalent that satisfies the operativity requirement.

### 9.2 Response architecture requirement

For each detection condition declared in the chain specification, a corresponding response declaration must exist before deployment. Detection conditions and response declarations are not separable: a detection condition without a response declaration is an incomplete specification.

The response declaration must specify:

The response modality: whether the response is automated, logged, or intervention. For automated responses, the condition triggering execution must be stated precisely. For intervention responses, the trigger for human escalation must be automated, because detection of the relevant patterns also operates faster than unaided human monitoring.

The speed requirement: at what rate the response must execute relative to the speed of the attack vector or failure mode being detected. Speed is a structural variable in this architecture, not a configuration parameter.

The response class: whether the condition being detected is an accidental failure or an adversarial input. These require structurally different responses. Accidental failure calls for chain correction: revise the specification, version the revision, propagate to prior stages. Deliberate manipulation calls for security response, chain suspension, and notification of affected risk-bearers identified in Condition 1.

The response architecture requirement applies regardless of domain. A machine-only domain application running an automated pipeline must specify automated response architectures for its detection conditions. A grants evaluation domain application operating with human reviewers must specify the escalation triggers and human judgment protocols. The modality differs by domain; the requirement to specify it before deployment does not.

### 9.3 Direction validation requirement

A specification must be examined from at least two directional origins before being accepted as compliant. The deploying organization's directional origin is required but not sufficient.

Different directional origins reveal structurally different failure classes at the same loop depth. Running triple-loop examination from the deploying organization's directional origin asks: what values and commitments generated our criteria? Running triple-loop from the affected party's directional origin asks: what values and commitments generated the premise that the deploying organization defines what matters? The second question is structurally invisible from the first directional origin. Both directions are required; neither substitutes for the other.

This requirement applies to domain application specification, not only to individual chain specifications. A domain application specification examined only from the domain operator's directional origin has a class of failures that is structurally invisible from that direction.

### 9.4 Domain bifurcation handling

Within any domain, some instrument classes may face external validation requirements (legal, regulatory, accreditation-based) while others operate with no equivalent external constraint and remain entirely impressionistic. A domain application specification must address this internal bifurcation.

The specification must declare which instrument classes the application covers, which it does not, and the boundary criterion. Covering only the legally-constrained instrument classes while leaving the impressionistic classes unaddressed is a domain application design choice, not a default. If impressionistic instrument classes are out of scope, the specification must state this explicitly so that the affected parties and independent attesters understand what the application does and does not govern.

---

## 10. Inheritance Receipt Structure

A CRAFT-conformant domain application must produce an inheritance receipt. The inheritance receipt is a formal declaration of the full inheritance structure under which the domain application was built and under which it operates.

The inheritance receipt has three components.

**Chain-level receipt.** The decision context, technical ontology, and domain configuration of the chain specification in CRAFT-compliant form, traceable to Conditions 1 through 6 as specified in this document.

**Full Precision Toolkit scope.** A CRAFT-conformant domain application does not inherit from CRAFT alone. Three standards function simultaneously, with context-dependent activity levels, when a domain application is being built or audited:

The CSIS (Coordination Structural Integrity Suite) standards function as the active normative foundation. The receipt must declare which CSIS standards are active for the domain and what obligations each places on the domain specification. A domain application that declares CRAFT conformance without declaring its CSIS inheritance is structurally incomplete: the CSIS standards name the foundational commitments from which CRAFT's requirements are derived, and a domain application not connected to those foundations has no structural basis for knowing when a CRAFT requirement should be interpreted strictly versus when a domain-specific application is appropriate.

Frame Language vocabulary discipline governs what terminology the domain application may use in its specification documents. The receipt must declare what Frame Language constraints apply to the domain's vocabulary. A domain application specification that uses terminology not examined through Frame Language's admissibility and watchlist checks may carry latent authority claims, deference patterns, or vocabulary substitutions that compromise the specification's legibility. Frame Language obligations are foregrounded whenever any specification document at any level of the hierarchy is authored or revised.

CRAFT as the evaluation chain legibility standard connects the CSIS normative foundation and Frame Language discipline to the specific six conditions the domain application must satisfy.

**Activity profile for each declared inheritance.** For each inherited standard declared in the receipt, the activity profile specifies the operating conditions under which that standard's obligations are foregrounded as active demands and the conditions under which they recede to background. The activity profile converts the receipt from a static declaration into an operational specification.

Each declared inheritance must include five elements:

1. The standard name and the specific version against which obligations are declared.
2. Which of the standard's obligations apply to this domain application and what they require.
3. The trigger conditions for foregrounding: the contexts in which this standard's obligations become active demands. Common trigger conditions include: during any authoring or revision of specification documents (Frame Language, PFDS); when Condition 6 escalates to double-loop or triple-loop (ASEP, SCLS, SPOS, IACS); when the deploying organization's CSS Radius changes or is under assessment, or when the chain's affected population crosses the Coordination Scaling Standard affected-party reach ceiling (CSS); during independent attestation (all active standards); during specification version upgrade following an inherited standard's revision.
4. The current background state: `background-satisfied` with a dated reference to when satisfaction was last validated, or `background-unchecked` explicitly declared as a current gap. Background-unchecked is not a valid operating state; it must appear as a finding in any compliance review, because it names an obligation that has not been assessed.
5. Version coupling handling: a procedure for detecting when this standard revises and a named response. When an inherited standard revises, the receipt enters `version-bump-pending` state for that standard, triggering a Condition 6 feedback event at the specification layer. The new version's obligations must be assessed and the receipt updated before the receipt is returned to current status. The lifecycle persistence commitment in Condition 6 must name version monitoring as a responsibility and must reference this procedure.

The distinction between `background-satisfied` and `background-unchecked` is a precision requirement, not a formality. A domain application that lists inherited standards without background state declarations has no legible compliance claim about whether those obligations have been assessed. `background-unchecked` as a declared gap is better than undeclared omission: it is honest, it is legible to an attesting party, and it is actionable.

**Axis-level positioning (where applicable).** For domain applications that implement a per-axis quality assessment architecture, the receipt must declare which CRAFT condition each axis serves and where each axis sits within the domain configuration. Axis-level receipts are preconditions for axis-level quality checks. Per-axis quality assessment architecture is domain-agnostic; domain applications using it are not limited to any single domain.

A receipt that declares CRAFT conformance without also declaring CSIS and Frame Language inheritance is a chain-level receipt without a Precision Toolkit scope declaration. It is structurally incomplete.

---

## 11. Bidirectional Obligations Framework

The relationship between CRAFT and the standards around it is bidirectional. Obligations flow in multiple directions. For each direction, the activity profile names when that direction's obligations are foregrounded.

**CSIS to CRAFT.** CRAFT must remain consistent with CSIS foundational commitments. A CRAFT normative requirement that contradicts a CSIS compressive standard requires resolution at the CSIS level before the CRAFT requirement is finalized. CRAFT cannot introduce requirements that would make CSIS-compliant behavior CRAFT-non-compliant; the inheritance relationship requires downward consistency. Activity profile trigger: when any CRAFT normative requirement is being authored or revised.

**CRAFT to CSIS (via domain signals).** When chain-level structural root cause assessment identifies a gap in the CSIS specification framework, the cross-layer signal path runs through Condition 6 to the specification layer and, where the gap implicates a specific CSIS standard, through the ASEP escalation path to that standard as a revision candidate. Activity profile trigger: when Condition 6 triple-loop examination surfaces a gap that cannot be addressed at the chain level.

The ASEP aggregate pattern obligation applies here: when population-level calibration tracking detects systematic directional drift, that drift is both a CRAFT Condition 6 event (requiring double-loop examination) and an ASEP aggregate adverse signal at the standards layer. The two obligations run simultaneously.

**Per-axis quality architecture to CRAFT (via dimension findings).** When a domain's per-axis quality assessment architecture consistently identifies a structural gap that originates at CRAFT's specification level rather than at the domain application level, that finding is a CRAFT revision signal: structural evidence about whether the construction grammar requirements in Section 9 are adequate for the domain's actual failure modes. Activity profile trigger: when a pattern of such findings persists across multiple domain application instances.

**Domain application to CRAFT.** When inside analysis of a domain reveals that the construction grammar requirements in Section 9 are inadequate for the domain's actual evaluation failure modes, that finding is a CRAFT construction grammar revision candidate. Activity profile trigger: when inside analysis of a new domain produces requirements that cannot be expressed within the current construction grammar.

**CSS to CRAFT (via scale threshold signals).** When a deploying organization's CSS Radius changes, the chain's deployment scale context declaration (Condition 6) requires re-assessment. If calibration drift (Condition 6) is detected in a population-level chain, the drift must be examined for scale-induced cause alongside its chain-level causes. The CSS Radius change is both a CRAFT Condition 6 event and a CSS scale threshold signal: the two obligations fire from the same event observed at two different layers. The affected-party reach axis is the second scale relationship CSS specifies, orthogonal to the Radii: when the chain's affected population crosses the affected-party reach ceiling, Condition 1 risk-bearer identification and Condition 6 direction-origin validation must route through the Structural Power Obligation Standard proxy or guardian channel, which CSS makes a minimum condition above the ceiling. Activity profile trigger: any confirmed change in the deploying organization's effective CSS Radius; any confirmed calibration drift in a population-level chain; any confirmed crossing of the Coordination Scaling Standard affected-party reach ceiling by the chain's affected population.

**Frame Language to all derived work.** Frame Language actively checks vocabulary choices whenever a specification document at any level of the hierarchy is authored or revised. This obligation is not passive background; it fires during every authoring activity regardless of which CRAFT condition or section is being written. The receipt declaration in Section 10 triggers the initial check at domain application inception; subsequent authoring activities trigger it again at each revision. Activity profile trigger: any authoring or revision of any specification document at the CRAFT, domain application, or per-axis quality level.

**Derived work to Frame Language.** When domain analysis requires vocabulary for which Frame Language's current admissibility framework or watchlist cannot provide a Frame 2 alternative without precision loss, that is a Frame Language revision signal. The observation follows the same pattern as domain application to CRAFT: domain-level empirical work surfaces gaps in the foundational standard. Activity profile trigger: when authoring a domain application specification encounters vocabulary that passes admissibility checks but that inside analysis shows to carry structural assumptions not visible in the admissibility screening.
---

## 12. Machine-Readable Output Constraint

CRAFT outputs, domain application outputs, and per-axis quality assessment outputs must be machine-readable in a form that preserves the architectural hierarchy under which they were produced. The architectural hierarchy is: CRAFT base layer, domain application layer nested within it, per-axis quality layer nested within the domain layer where applicable. Outputs that flatten this hierarchy lose the structural information about which layer's specification produced which finding.

A CRAFT-compliant system produces three structurally distinct output types at three structurally distinct times. Each output type answers different questions for different readers. Conflating them produces documents that cannot be reliably processed by automated systems.

### 12.1 Specification schema (specification-time)

The specification-time document declares the chain's design before any data arrives or evaluation begins. It is the reference against which all runtime and audit-time outputs are checked. The base schema is `craft-specification-schema-v0.2.0.json`.

Required addition for domain applications: a `craft_base_version` field at the top level declaring which CRAFT base schema version the domain application conforms to. For documents conforming directly to the base schema, this equals `schema_version`. For domain application documents that extend the base, this field identifies the CRAFT base version the extension is built on, enabling a third party to determine which fields are CRAFT base requirements and which are domain additions.

Domain application schema documents must declare their layer attribution for each field group: which fields satisfy CRAFT base requirements, which satisfy domain-application requirements derived from inside analysis, and which satisfy per-axis quality instrument requirements.

### 12.2 Evaluation record schema (runtime)

The evaluation record documents what the chain did with one input at one point in time. One record per evaluation instance. The evaluation record schema does not yet exist as a formal schema document; this section specifies the minimum required fields.

Required fields:

`record_type`: declared as `evaluation_record`. Required for temporal stage declaration; automated consuming systems must not need to infer the document type.

`specification_id` and `specification_version`: the exact specification document in force at evaluation time.

`evaluation_timestamp`: date and time of evaluation.

`input_provenance`: a reference to the input in sufficient form to allow the finding to be checked independently.

`outcome`: `accepted`, `rejected`, or `indeterminate`. The value derives from the reading evaluated against the Condition 4 threshold, carrying the Condition 3 instrument uncertainty:
- `accepted`: the reading minus its uncertainty still clears the threshold.
- `rejected`: the reading plus its uncertainty still fails the threshold.
- `indeterminate`: the reading plus-or-minus its uncertainty straddles the threshold, so the instrument cannot resolve the outcome.

`indeterminate` is not collapsible into `accepted` or `rejected`. It is its own outcome class and routes through `propagation_targets` as the signal that the chain could not decide, which is itself information the feedback loop must carry.

`condition_findings`: for each condition evaluated, the result and the basis. For rejections, the specific condition that triggered rejection, the data values at evaluation time, and the layer attribution (`craft_base`, `domain_application`, or `per_axis_quality`). Where Condition 3 specified instrument uncertainty for the instrument producing a finding, the finding must carry that uncertainty band, so the `outcome` determination against the Condition 4 threshold is independently checkable and an `indeterminate` outcome is traceable to the band that produced it.

`gate_check_result`: the adversarial gate result at evaluation time.

`propagation_targets`: for rejection and indeterminate findings, the prior condition(s) that the signal must propagate to under Condition 6. An `indeterminate` outcome propagates as its own signal class: the chain could not resolve the reading against the threshold, and that non-resolution is information the feedback loop must carry rather than discard.

A rejection record that does not carry layer attribution cannot be used for root cause analysis: the propagation target at Condition 6 may differ depending on whether the failure originates at the CRAFT base level or the domain application level.

### 12.3 Compliance report schema (audit-time)

The compliance report documents whether a specification document meets CRAFT requirements. It is produced when someone asks whether a chain's design is CRAFT-conformant; it is not produced when the chain evaluates data. The base schema is partially specified in the reference tooling.

Required additions:

`evaluated_specification_id` and `evaluated_specification_version`: which specification document was evaluated. Without these fields, a compliance report cannot be associated with the document it checked.

`layer` field per finding: each `ConditionResult` must declare whether the finding concerns a CRAFT base requirement, a domain-application requirement, or a per-axis quality requirement. Currently all findings are implicitly `craft_base`; when domain applications add requirements, their findings must be distinguishable from base requirements.

The machine-only constraint applies to all three schemas: no field may require human interpretation to be processed by an automated consuming system. A schema field that encodes structural information in natural-language prose that an automated system cannot parse without a human reader is not machine-readable in the relevant sense.

---

## 13. Third-Party Domain Standard Development

Because CRAFT is a meta-standard, organizations and practitioners outside this project can build CRAFT-conformant domain standards for domains not covered by existing domain applications. Third-party development requires no coordination with the CRAFT specification maintainers for the development itself. Conformance is independently attested.

A third-party domain application is CRAFT-conformant when it satisfies all of the following:

It inherits all normative requirements from this specification without omission or weakening.

Its additional requirements derive from inside analysis of the domain's evaluation failure modes, and that derivation is documented.

It produces an inheritance receipt meeting the requirements in Section 10.

It carries independent attestation of its conformance to this specification, produced by a party meeting the independence requirements in Section 6.1.

The attestation is a conformance claim, not a registration requirement. Third parties do not require CRAFT maintainer approval to publish a CRAFT-conformant domain standard. The conformance claim rests on the quality of the independent attestation.

[Needs validation: a registry and conformance marking protocol for third-party domain standards are pending. In their absence, conformance claims should reference the specific version of this specification against which they were attested.]

---

## 14. What CRAFT Provides That No Existing Framework Provides

This section states the novelty claim precisely, because the claim must be defensible against existing adjacent work.

**The chain structure requiring all six conditions and their interdependence.** Existing frameworks address individual stages: construct validity literature addresses the ontology stage; pre-registration addresses the evaluation criteria stage; audit standards address the decision logic stage; dispute resolution addresses the feedback stage. No existing framework requires all six conditions simultaneously, specifies that each must be derived from the prior stage, and requires a feedback mechanism that propagates to every prior stage. CRAFT is the first framework to treat the evaluation chain as a chain: a structure in which every stage's validity depends on the prior stages' validity. Evidence-centered design (Mislevy, Steinberg, and Almond, 1999 onward; the PADI templates) is the closest adjacent prior art: a layered architecture of student, evidence, and task models, with machine-readable inter-layer communication realized as a UML object model with attribute-slot inheritance and shared cross-layer objects, and a delivery cycle that passes observations forward to update a latent-state belief. Against that precedent the chain-structure novelty narrows to what survives the comparison: evidence-centered design is a design framework for measuring persons, whereas CRAFT audits evaluation systems as such; and CRAFT makes explicit decision logic (Condition 5) a required condition of the chain rather than separate delivery machinery. The requirement that all six conditions hold interdependently and that a confirmed error propagate to every prior stage remains CRAFT-specific; the layered-and-machine-communicating property does not, and is credited to evidence-centered design in Section 16.

**The attestation requirement applied to the specification chain.** CRAFT requires that the evaluation chain be attested by independent parties before data collection begins. Existing frameworks in evaluation, audit, and research methodology require documentation and peer review; none require independent attestation of the specification chain as a precondition for operation.

**The adversarial gate as a first-class requirement.** Existing frameworks treat falsifiability as a desirable property of evaluation designs. CRAFT treats falsifiability as a gate condition: a specification that does not produce rejections under realistic adversarial conditions is not accepted. The adversarial gate operationalizes falsifiability as an enforcement mechanism rather than an aspirational standard.

**The implicit specification gap as a design vulnerability.** No existing protocol design standard or evaluation methodology names the implicit specification gap as a security and governance vulnerability. CRAFT formalizes the claim that implicit design choices create unenforceable boundaries, and that making those choices explicit before deployment is a structural security requirement.

**Risk-bearer identification as a required specification element.** No existing evaluation framework requires the specification to name who bears losses when the chain fails as a precondition for compliance. The risk reduction statement and risk-bearer identification requirements in Condition 1 close a gap that is absent from all adjacent frameworks reviewed.

**Construction grammar for CRAFT-conformant domain standards.** The meta-standard function, including the structural operativity requirement, response architecture requirement, direction validation requirement, and domain bifurcation handling, is not present in any adjacent framework reviewed.

Validation status as of 2026-05-28: the chain structure claim is supported by review of seven post-failure reform efforts and six additional domain investigations. Each domain confirmed the same structural failure class, and none of the post-failure reform efforts addressed all six conditions simultaneously. The risk-bearer identification claim has not yet been checked against all adjacent frameworks; validation is pending.

---

## 15. Known Limitations and Open Problems

**The decision context specification problem.** CRAFT requires that a decision context be specified before data collection begins. It does not specify how to derive a correct decision context from a complex, contested, or evolving decision environment. A correctly structured evaluation that answers the wrong question is CRAFT-compliant and wrong. Domain applications must address this within their inside analysis.

**The multi-chain aggregate interaction problem.** CRAFT addresses single-chain specification. Individually-compliant chains can still produce a non-compliant aggregate outcome at the system level, where many separately-sound evaluations combine into a systemic failure that no single chain's specification could have caught. CRAFT's construction grammar and bidirectional obligations framework address intra-chain and cross-layer signals; the inter-chain aggregate failure class is outside CRAFT's appropriate scope. This is a named scope boundary, not an unrecognized gap. It is a candidate for a future CSIS standard addressing system-level interaction between multiple compliant chains.

**The feedback mechanism operationalization problem.** Condition 6 requires an operative feedback mechanism and specifies loop depth requirements. What constitutes a sufficient specification revision at each loop depth is not fully defined. The loop depth requirements name the objects being revised at each depth; they do not fully specify when a revision of the appropriate object is sufficient.

**The pedagogical legibility operationalization problem.** Section 4 requires that the evaluation chain be legible to affected parties. What constitutes sufficient pedagogical legibility in different contexts is not defined here. Domain applications must specify this for their affected populations.

**The evaluation record schema.** Section 12.2 specifies the minimum required fields for runtime evaluation records in prose. The formal schema document does not yet exist. Domain applications operating before a schema is implemented must document their evaluation records in human-readable form pending schema implementation in the reference tooling.

**The inheritance receipt activity profile format.** Section 10's activity profile requirements are normatively specified in prose. The machine-readable format for producing and checking activity profiles is not yet specified. Domain applications must implement the activity profile in human-readable form pending format specification.

**Multi-party attestation role declarations.** Multi-party attestation architecture (collective review requirements from Salaudeen et al. Section 7) constitutes a consequential validity change to Condition 4 beyond the criterion anchoring addition in this version. This is deferred to v0.5.0 and requires a dedicated sensemaking session before specification.

---

## 16. Adjacent Frameworks

**Salaudeen et al., "Measurement to Meaning: A Validity-Centered Framework for AI Evaluation" (NeurIPS 2025).** Proposes a claim-aware framework grounded in five forms of validity from psychometrics: content, external, criterion, construct, and consequential. Four structural contributions integrated in this version: criterion/construct claim type distinction (Condition 1 claim object type declaration), criterion standard anchoring (Condition 4), consequence-calibrated adversarial gate (Condition 5 consequence level declaration), and deployment-context evidence as a Condition 6 feedback trigger. Multi-party attestation architecture remains pending; see Section 15.

**Wang, Hertzmann, Russakovsky, "Benchmark Suites Instead of Leaderboards for Evaluating AI Fairness" (Patterns, 2024).** Argues that single-leaderboard scores collapse heterogeneous performance across multiple validity dimensions into a single ranking, hiding structurally different failure modes. Contributes the composite claim aggregation method specification requirement in Condition 1's claim object type declaration.

**Wang, Ho, Koyejo, "The Inadequacy of Offline LLM Evaluations: A Need to Account for Personalization in Model Behavior" (Patterns, 2025).** Establishes that offline evaluations validated for general-population assessment are not valid for personalized-use contexts without declared scope constraints. Contributes the explicit deployment context scope requirement in Condition 1's first paragraph and the deployment-context evidence feedback trigger in Condition 6.

**Wang, "Identities are not Interchangeable: The Problem of Overgeneralization in Fair Machine Learning" (FAccT, 2025).** Establishes that claim objects over-generalize when sub-population scope boundaries are not declared. Contributes the population granularity dimension of the deployment context scope requirement in Condition 1.

**Total Survey Error framework (Biemer 2010).** Identifies measurement error sources across the full data collection process. Validates CRAFT's multi-stage structure. CRAFT's six conditions map closely to the Total Survey Error stage structure.

**Evidence-Centered Design (Mislevy, Steinberg, and Almond, 1999 onward; the PADI templates, Mislevy et al. 2003 and the PADI technical report series).** A framework for designing educational and psychological assessments as a layered architecture: a student model (the latent constructs claimed), an evidence model (evidence rules and a measurement model that carries belief as a probability distribution), and a task model (the situations that evoke evidence), connected by a four-process delivery cycle. PADI implements the layers as a UML object model with attribute-slot inheritance, shared cross-layer objects, and supporting software. Evidence-centered design is the closest prior art to CRAFT's chain structure and machine-communicating layers (see Section 14): it predates CRAFT in treating evaluation design as layered, object-modeled, and machine-communicating. CRAFT's distinction is that it audits evaluation systems rather than measuring persons, and makes explicit decision logic a required condition. Evidence-centered design's measurement model, which carries the latent-state estimate as a probability distribution rather than a point, is also the external corroboration for CRAFT's treatment of instrument uncertainty as a carried requirement (Condition 3) and for the indeterminate outcome (Section 12.2).

**ETS differential-item-functioning practice (Zwick, ETS RR-12-08, 2012; Holland and Thayer 1988; Dorans).** A long-running operational regime for flagging biased test items that grades severity by two criteria applied jointly, a significance test and an effect-size floor, and sets explicit minimum sample sizes below which the statistical procedure is not relied upon. This is the prior art for CRAFT's two-signal structure (Condition 3 instrument uncertainty together with Condition 4 effect-size thresholds) and for the resolution floor (Condition 3): a deployed system that names the cohort size below which its instrument cannot resolve. CRAFT departs from the prior art's response to a sub-floor cohort: where the ETS regime exempts small groups from analysis, CRAFT refuses exemption on the equity cost-asymmetry the same literature states (the missed detection is the expensive error) and routes the sub-floor case to the determinate signal class and to accumulation over time.

**Pre-analysis plan literature (Ofosu and Posner 2023; Coffman and Niederle 2014).** Documents the limits of pre-specification as a research credibility mechanism. Confirms that pre-specification alone does not eliminate specification gaming. CRAFT's adversarial gate and independent attestation are direct structural responses to the failure modes this literature identifies.

**Optimistic verification (UMA Optimistic Oracle; optimistic rollups; interactive verification, Teutsch and Reitwiessner).** Establishes the ex-post form: an assertion accepted provisionally against a pre-specified rule and overturnable by a bonded challenge resolved by a body the asserter does not control. This is the public prior art for the Section 7.2 ex-post realization and the existence proof that pre-specification and adversarial challenge are two components of one verification structure rather than rivals.

**Procedural justice and the rule of law (nemo iudex in causa sua; Tumey v. Ohio and Caperton v. A. T. Massey Coal Co. on pecuniary interest; Madison, Federalist No. 10).** Establishes that the basis on which a dispute is decided must lie outside the control of any party with a stake in it, realized by pre-specified general rule and by impartial after-the-fact adjudication as two techniques of one requirement. This is the public warrant for the Section 7.2 non-self-adjudication invariant, and the pecuniary-interest line is the warrant for requiring the ex-post realization's disinterest to be structural rather than nominal.

**CROSS.** CROSS, the Common Reporting Outcome Standards Schema, is the first domain application built on this specification: a freely available grants standard. See the CROSS standard for its requirements. How the standards in the suite relate to one another is documented in the framework overview rather than here.

**ASEP (Adverse Signal Engagement Protocol) and SCLS (Structural Consent Legibility Standard).** Both CSIS standards cited as structural dependencies of Condition 6's loop depth requirement.

**SPOS (Structural Power Obligation Standard) and IACS (Information Asymmetry Classification Standard).** Both CSIS standards cited as structural dependencies of Condition 6's direction-origin validation requirement and the construction grammar's direction validation requirement.

**CSS (Coordination Scaling Standard).** CSIS standard cited as the structural dependency of Condition 6's deployment scale context declaration and Condition 1's adversarial threat model scale-based threat class. CSS specifies when coordination functions have broken at each organizational scale; CRAFT's Condition 6 requirements presuppose CSS minimum conditions at the deploying organization's effective Radius.

---

## 17. Sources and Validation Record

- Development sensemaking and validation record retained with the maintainers.
- Salaudeen et al., "Measurement to Meaning" (NeurIPS 2025), arxiv.org/abs/2505.10573
- Wang, Hertzmann, Russakovsky, "Benchmark Suites Instead of Leaderboards" (Patterns, 2024)
- Wang, Ho, Koyejo, "The Inadequacy of Offline LLM Evaluations" (Patterns, 2025)
- Wang, "Identities are not Interchangeable" (FAccT, 2025)
- Total Survey Error framework: Biemer (2010)
- Ofosu and Posner, pre-analysis plan literature (2023)
- Coffman and Niederle, "Pre-Analysis Plans Have Limited Upside" (2014)
- Mislevy, Almond, Lukas, "A Brief Introduction to Evidence-Centered Design" (ETS Research Report RR-03-16 / CSE Report 632, 2003)
- PADI Technical Report series, "Task Templates" (PADI Technical Report 3); Mislevy et al., PADI design patterns (2003)
- Zwick, "A Review of ETS Differential Item Functioning Assessment Procedures" (ETS RR-12-08, 2012)
- Adverse-Signal Engagement Principle, Section 3.3.10

---

## Changelog

v0.4.3 (2026-06-13): Affected-party scale-trigger seam landed at the CRAFT layer, the held seam from v0.4.2 now that the Coordination Scaling Standard (v0.1.4) and the Structural Power Obligation Standard (v0.1.25) have settled, satisfying the Specification Inheritance Check. Condition 1 risk-bearer identification: above the Coordination Scaling Standard Section 10 affected-party reach ceiling, risk-bearer identification must route through the Structural Power Obligation Standard Section 4.1 proxy or guardian channel rather than impressionistic naming; the routing supplies legibility of the affected-party relationship, not knowledge of full exposure. Condition 6 direction-origin validation: above the reach ceiling, the affected-party directional origin must enter through the same channel rather than through the deploying organization's impression of it. Section 10 activity-profile trigger conditions and the Section 11 CSS-to-CRAFT direction extended to name the affected-party reach-ceiling crossing as a foregrounding trigger, the chain-level firing of the CSS and SPOS activity profiles in the inheritance receipt. The six conditions are unchanged in count; no other normative content changed.

v0.4.2 (2026-06-13): Three upward-question resolutions integrated from the CRAFT upward-questions examination record. Condition 3: resolution floor added (an instrument whose uncertainty depends on cohort size declares the size below which it cannot resolve; sub-floor readings route to the determinate-resolution signal class and to over-time accumulation rather than to exemption). Condition 4: threshold meaningfulness below the resolution floor stated, extending the systematic-uncertainty guard. Section 12.2: the runtime evaluation record `outcome` becomes three-valued (accepted, rejected, indeterminate); indeterminate is non-collapsible and propagates as its own signal class; condition findings carry the instrument uncertainty band where Condition 3 specified one. Section 14: the chain-structure novelty claim narrowed against evidence-centered design, credited as the closest prior art for the layered, machine-communicating property; the all-six-conditions interdependence and the propagate-to-every-prior-stage feedback remain CRAFT-specific. Section 16: evidence-centered design (Mislevy and PADI) and ETS differential-item-functioning practice (Zwick) added as adjacent frameworks; Section 17 sources updated. The six conditions are unchanged in count. The affected-party scale-trigger seam (CSS, SPOS, CRAFT) is examined and held: it is normative across three standards and lands only after CSS and SPOS settle, per the Specification Inheritance Check. Multi-party attestation architecture (the prior v0.5.0 reservation) remains deferred and is not in this pass.

v0.4.1 (2026-06-04): Precision-parity edit to Condition 1. Risk-bearer identification, which previously carried only the umbrella statement that Condition 1's structural elements are carried into every downstream stage, now also carries the explicit per-element reminder that boundary population and claim object type already carry, because it is the element most prone to being applied at entry only. The stated count of Condition 1 structural elements is corrected from six to seven; the adversarial threat model added in v0.2.0 was not reflected in the count. No normative requirement changed: the carried status of risk-bearer identification was already established by the umbrella statement, and this edit makes it as explicit for that element as for the two others that already restated it.

v0.4.0 (2026-06-04): Enforcement layer generalized. Section 7.2 (renamed to Non-self-adjudication) and the Section 6.1 independent-attestation requirement restructured: the invariant that the overturning basis must lie outside the claimant's control is stated as CRAFT's inheritance of the Precision-First Design Standard independent-observer and trusted-interpretive-intermediary definitions and Corollary 8, and is given two realizations, ex-ante designated attestation (the prior single-attestor form) and ex-post adversarial challenge resolved against the Condition 4 criteria by a resolver set the claimant does not control. Both realizations must secure disinterest structurally; the required disinterest strength scales with the Condition 5 consequence level, inheriting the consequence-calibration. The ex-post realization carries four structural conditions: disclosure of the resolver set's power distribution per the Structural Power Obligation Standard, a manipulability floor on the resolution mechanism, direction-origin validation extended to the resolver, and availability bounded to determinate-resolution claims. Condition 1 claim object type declaration extended: construct-type claims declare indicator direction as reflective, causal-formative, or composite-aggregate, with validity inapplicable to composite-aggregate objects and the reflective-versus-causal-formative distinction adopted with the dissent named; implements the refined PFDS Corollary 10. Section 16 extended with the optimistic-verification and procedural-justice literatures as the public warrant for the ex-post realization. The six conditions are unchanged in count. Multi-party attestation architecture remains deferred to v0.5.0.

v0.3.0 (2026-05-28): Six sensemaking inputs integrated. Condition 1: claim object type declaration added (criterion/construct distinction, nomological network requirement for construct claims, aggregation method for composite claims; implements PFDS Corollary 10 at the chain level); out-of-scope uses requirement strengthened to require explicit deployment context scope declaration; adversarial threat model extended with scale-based coordination function breaks as a named threat class with CSS effective Radius declaration. Condition 4: criterion standard anchoring added for criterion-type chains; construct-type chains must declare nomological network consistency in evaluation criteria. Condition 5: consequence level declaration added, calibrating adversarial gate intensity to harm potential (implements PFDS Corollary 10 consequence-calibrated evidence bar at the chain level). Condition 6: deployment-context evidence named as a distinct feedback trigger category; deployment scale context declaration added (required: effective_radius, minimum_css_conformance, conformance_gap_handling); version monitoring added to lifecycle persistence commitment; calibration drift extended with scale-induced cause examination requirement. Section 10 (Inheritance Receipt): rewritten with activity profile concept; five required elements per inherited standard; background-satisfied versus background-unchecked distinction; version coupling procedure; WALKRI described as domain-agnostic; "substrate" language replaced with context-dependent activity relationship. Section 11 (Bidirectional Obligations): four new obligation directions added (CSS to CRAFT, Frame Language to all derived work, derived work to Frame Language, WALKRI to domain application and reciprocal); activity profile trigger conditions added to all directions. Section 12 (Machine-Readable Output): rewritten with three named output schemas (specification-time, runtime evaluation record, audit-time compliance report); minimum field specifications for all three; runtime evaluation record schema identified as new and not yet implemented in tooling. Section 6.3: Salaudeen integration partially complete at chain level (four additions); multi-party attestation architecture deferred to v0.4.0. Section 6.2: evaluation record requirements updated to align with Section 12.3 terminology. Sections 10 and 11 working draft markers removed. Section 12 retains pending implementation note for runtime schema and activity profile format.

v0.2.0 (2026-05-28): Major revision. Additions to Condition 1: risk reduction statement, risk-bearer identification, adversarial threat model, population-level chain handling. Condition 2: temporal scope declaration; construct-to-estimand adequacy statement. Condition 3: multi-hop inferential validation; calibration measurement instrument. Condition 4: calibration benchmark. Condition 5: coupled evaluation-intervention structure. Condition 6: loop depth requirement; calibration drift; direction-origin validation. Attestation scope extended. New sections 9-13.

v0.1.0 (2026-05-24): Initial specification. Six conditions established. Adversarial gate, independent attestation, and feedback mechanism as enforcement layer. Domain application inheritance section.
