# MARINE SEMANTIC REGISTRY

## Document Information

Project: NICAI Marine Intelligence System

Version: 1.0

Status: Architecture Design

Owner: Marine Domain Unit (MDU)

Purpose:

The Marine Semantic Registry defines the official meaning of all critical marine intelligence terms used across NICAI, SVACS, Marine MasterDB, Runtime Telemetry and the Operations Command Center.

The objective is to eliminate semantic drift and ensure every system interprets terms consistently.

---

# 1. Objective

A sovereign intelligence system cannot allow multiple meanings for the same term.

For example:

"High Risk"

must mean exactly the same thing in:

* NICAI
* SVACS
* Runtime
* Command Center
* Validation Systems

The Semantic Registry acts as the single source of truth for operational language.

---

# 2. Semantic Governance Principles

Every registered term must contain:

* Definition
* Scope
* Owner
* Allowed Meanings
* Prohibited Meanings
* Examples
* Version
* Authority

No term may be used outside its approved meaning.

---

# 3. Core Marine Terms

## Navigable

Definition:

A water body that allows safe vessel movement under current operational conditions.

Scope:

Navigation Intelligence

Owner:

NICAI

Allowed Meaning:

* Vessel movement possible
* Safe operational passage available

Prohibited Meaning:

* Good economic opportunity
* Good infrastructure

Example:

"The river reach is navigable for vessels with draft below 2.5 meters."

Version:

1.0

---

## Non-Navigable

Definition:

A water body where safe vessel movement is not possible.

Scope:

Navigation Assessment

Owner:

NICAI

Allowed Meaning:

* Unsafe vessel movement
* Insufficient depth
* Physical obstruction

Prohibited Meaning:

* Economic failure
* Environmental degradation

Example:

"The channel is non-navigable due to low water depth."

Version:

1.0

---

## Suitable

Definition:

A location satisfies predefined operational criteria.

Scope:

Decision Intelligence

Owner:

NICAI

Allowed Meaning:

* Meets operational requirements

Prohibited Meaning:

* Guaranteed success

Example:

"Varanasi is suitable for cargo operations."

Version:

1.0

---

## Unsuitable

Definition:

A location does not satisfy required operational conditions.

Scope:

Decision Intelligence

Owner:

NICAI

Example:

"Current conditions are unsuitable for seaplane operations."

---

## Operational

Definition:

An asset or system is available for intended use.

Scope:

Infrastructure Intelligence

Owner:

Authority Owner

Example:

"The terminal is operational."

---

## Non-Operational

Definition:

Asset unavailable for intended use.

Example:

"The jetty is non-operational due to maintenance."

---

# 4. Risk Terminology

## Risk

Definition:

Potential for an undesirable operational outcome.

Scope:

Risk Intelligence

Owner:

NICAI

Allowed Meaning:

* Potential negative impact

Prohibited Meaning:

* Confirmed failure

Example:

"Flood risk is increasing."

---

## Hazard

Definition:

A condition capable of causing harm or disruption.

Scope:

Risk Intelligence

Owner:

NICAI

Example:

"Strong currents are a navigation hazard."

---

## Threat

Definition:

A risk source capable of creating operational consequences.

Example:

"Heavy rainfall is a flood threat."

---

## Vulnerability

Definition:

A weakness that increases risk exposure.

Example:

"Low bridge clearance is a vulnerability."

---

## Critical Risk

Definition:

Risk requiring immediate operational attention.

Example:

"Critical flood risk detected."

---

# 5. Environmental Terms

## Flood

Definition:

River water exceeding safe operational levels.

Scope:

Hydrological Intelligence

Owner:

CWC

Example:

"Flood conditions detected upstream."

---

## River Health

Definition:

Overall ecological and environmental condition of a river.

Scope:

Environmental Intelligence

Owner:

CPCB

Example:

"River health remains stable."

---

## Water Quality

Definition:

Measured environmental condition of water.

Scope:

Environmental Intelligence

Owner:

CPCB

Example:

"Water quality is suitable for operations."

---

## Pollution Event

Definition:

An incident causing measurable degradation in water quality.

Example:

"Industrial discharge triggered a pollution event."

---

# 6. Infrastructure Terms

## Terminal Ready

Definition:

Terminal can immediately support intended operations.

Scope:

Infrastructure Intelligence

Owner:

IWAI

Requirements:

* Operational status
* Available capacity
* Functional access

Example:

"Varanasi terminal is terminal ready."

---

## Cargo Ready

Definition:

Infrastructure can handle planned cargo movement.

Scope:

Cargo Intelligence

Owner:

NICAI

Example:

"Terminal is cargo ready for bulk commodities."

---

## Capacity Constrained

Definition:

Demand exceeds available infrastructure capacity.

Example:

"Terminal capacity is constrained."

---

## Corridor Ready

Definition:

Entire logistics corridor is operationally available.

Example:

"The cargo corridor is corridor ready."

---

# 7. Intelligence Terms

## Observation

Definition:

Raw fact collected from a source.

Examples:

* Gauge Reading
* Sensor Value
* Inspection Result

Owner:

Runtime Telemetry

---

## Signal

Definition:

Meaningful interpretation of observations.

Example:

Observation:

Water Level = 1.5m

Signal:

Low Water Condition

Owner:

NICAI

---

## Assessment

Definition:

Evaluated operational meaning derived from signals.

Example:

"Navigation suitability reduced."

Owner:

NICAI

---

## Recommendation

Definition:

Suggested action generated through explainable reasoning.

Owner:

NICAI

Example:

"Reduce vessel draft."

---

## Decision

Definition:

Approved operational action.

Owner:

Operator

Example:

"Suspend cargo movement."

---

# 8. Confidence Terms

## Confidence

Definition:

Degree of trust in an intelligence output.

Scope:

Confidence Model

Owner:

NICAI

Factors:

* Coverage
* Quality
* Freshness
* Consistency
* Validation

Example:

"Confidence = 0.91"

---

## High Confidence

Definition:

Strong supporting evidence with minimal contradiction.

Range:

0.85 – 1.00

---

## Medium Confidence

Definition:

Reasonable evidence but partial uncertainty.

Range:

0.60 – 0.84

---

## Low Confidence

Definition:

Limited evidence or significant contradiction.

Range:

0.00 – 0.59

---

# 9. Validation Terms

## Validation

Definition:

Verification that intelligence output is supported by evidence.

Owner:

SVACS

Example:

"Recommendation validated."

---

## Contradiction

Definition:

Evidence that conflicts with another evidence source.

Owner:

SVACS

Example:

"Telemetry contradicts manual inspection."

---

## Provenance

Definition:

Traceable origin of information.

Example:

Dataset
↓
Observation
↓
Signal
↓
Assessment

Owner:

SVACS

---

# 10. Emergency Terms

## Watch

Definition:

Condition requiring increased monitoring.

Example:

"River under watch."

---

## Alert

Definition:

Potential operational issue identified.

Example:

"Flood alert issued."

---

## Restricted

Definition:

Operations allowed with limitations.

Example:

"Restricted vessel movement."

---

## Emergency

Definition:

Immediate action required to protect safety or assets.

Example:

"Emergency operations activated."

---

## Recovery

Definition:

Return from emergency toward normal operations.

Example:

"Recovery phase initiated."

---

# 11. Governance Rules

All semantic terms must:

* Have one approved definition.
* Have one responsible owner.
* Have version control.
* Be traceable.
* Be reviewable.
* Be auditable.

No team may redefine a registered term without governance approval.

---

# 12. Versioning Policy

Semantic changes require:

* Change Request
* Domain Review
* Impact Assessment
* Approval
* Version Update

Example:

v1.0

Original Definition

↓

v1.1

Updated Definition

↓

v2.0

Major Semantic Change

---

# 13. Semantic Drift Prevention

The registry prevents:

* Ambiguous terminology
* Multiple interpretations
* Team-specific definitions
* Contradictory documentation
* Inconsistent intelligence outputs

Every system must reference this registry before generating intelligence.

---

# 14. Success Criteria

The Semantic Registry is successful when:

* Every important term has one meaning.
* Every recommendation uses approved terminology.
* Every validation process references the same definitions.
* Every operator interprets intelligence consistently.

A future operator should be able to ask:

"What does this term mean?"

and receive one authoritative answer across the entire Marine Intelligence ecosystem.
