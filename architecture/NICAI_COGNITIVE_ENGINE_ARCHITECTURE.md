# NICAI COGNITIVE ENGINE ARCHITECTURE

## Purpose

NICAI (National Cognitive Intelligence Architecture for Inland Navigation) is the central reasoning engine of the Marine Intelligence System.

Its purpose is not to generate recommendations directly from datasets.

Its purpose is to think like an experienced marine operator by combining:

* Observations
* Evidence
* Context
* Historical Memory
* Operational Constraints
* Opportunities
* Risks
* Governance Rules

before producing an explainable operational recommendation.

---

# Core Principle

Traditional Systems:

Dataset
→ Rule
→ Recommendation

NICAI:

Observation
→ Evidence
→ Context
→ Memory
→ Risk Assessment
→ Opportunity Assessment
→ Decision Negotiation
→ Recommendation
→ Validation
→ Operator Guidance

Every step must be traceable and explainable.

---

# Cognitive Objectives

NICAI must answer:

* What is happening?
* Why is it happening?
* What caused it?
* What are the risks?
* What are the opportunities?
* What should be done?
* Why should it be done?
* What evidence supports this?
* How confident are we?
* What alternatives exist?

---

# Cognitive Layers

NICAI operates through multiple intelligence layers.

## Layer 1 — Observation Intelligence

Purpose:

Convert raw data into observations.

Inputs:

* Telemetry
* Sensors
* River Stations
* Weather Data
* Infrastructure Data

Output:

Observation Objects

Example:

Water Level = 3.2m

---

## Layer 2 — Signal Intelligence

Purpose:

Detect meaningful changes.

Example:

Water Level Decreasing

Output:

Signal Objects

Examples:

* Falling Water Level
* Rising Flood Probability
* Terminal Congestion Increase

---

## Layer 3 — Context Intelligence

Purpose:

Understand operational meaning.

Example:

Water level decrease during dry season.

Meaning:

Expected Seasonal Condition

Output:

Context Assessment

---

## Layer 4 — Memory Intelligence

Purpose:

Retrieve historical knowledge.

Sources:

* Seasonal Memory
* Historical Memory
* Incident Memory
* Decision Memory

Example:

Similar event occurred in 2021.

Output:

Historical Context

---

## Layer 5 — Risk Intelligence

Purpose:

Identify operational risks.

Examples:

* Navigation Risk
* Flood Risk
* Cargo Risk
* Environmental Risk

Output:

Risk Register

---

## Layer 6 — Opportunity Intelligence

Purpose:

Identify beneficial actions.

Examples:

* Cargo Expansion
* Route Optimization
* Terminal Utilization

Output:

Opportunity Register

---

## Layer 7 — Decision Intelligence

Purpose:

Generate possible decisions.

Example:

Option A:

Continue Operations

Option B:

Reduce Draft

Option C:

Suspend Operations

Output:

Decision Candidates

---

## Layer 8 — Validation Intelligence

Purpose:

Validate recommendations.

Checks:

* Evidence Completeness
* Policy Compliance
* Regulatory Compliance
* Confidence Threshold

Output:

Validated Recommendation

---

## Layer 9 — Governance Intelligence

Purpose:

Ensure authority compliance.

Checks:

* MDU Policies
* SVACS Rules
* Operational Directives
* Regulatory Constraints

Output:

Governance Approval

---

# Decision Cognition Workflow

NICAI follows a structured reasoning path.

Observation
↓
Signal
↓
Context
↓
Memory
↓
Risk Assessment
↓
Opportunity Assessment
↓
Decision Generation
↓
Decision Comparison
↓
Conflict Resolution
↓
Recommendation
↓
Validation
↓
Operator Guidance

---

# Decision Candidate Model

NICAI never generates only one recommendation.

It generates multiple candidates.

Example:

Candidate 1

Continue Cargo Operations

Candidate 2

Reduce Cargo Load

Candidate 3

Suspend Operations

Each candidate receives:

* Supporting Evidence
* Risks
* Benefits
* Confidence
* Constraints

---

# Decision Negotiation Framework

Competing recommendations are compared.

Evaluation Criteria:

1. Safety
2. Operational Continuity
3. Economic Impact
4. Environmental Impact
5. Regulatory Compliance
6. Infrastructure Availability

Highest ranked recommendation becomes the preferred recommendation.

Alternative recommendations remain visible.

---

# Conflict Resolution Engine

Purpose:

Resolve recommendation conflicts.

Example:

Recommendation A:

Increase Vessel Throughput

Recommendation B:

Reduce Vessel Throughput Due to Flood Risk

Resolution Logic:

Safety Priority

>

Regulatory Priority

>

Operational Priority

>

Economic Priority

Final Result:

Reduce Throughput

Reason:

Flood Risk Overrides Throughput Goal

---

# Objective Optimization

NICAI balances multiple objectives.

Objectives:

* Safety
* Reliability
* Efficiency
* Sustainability
* Cost Optimization
* Mission Success

Optimization is deterministic and rule-based.

No black-box AI decisions are permitted.

---

# Recommendation Contract

Every recommendation must include:

Recommendation ID

Title

Description

Priority

Supporting Evidence

Supporting Datasets

Risks

Opportunities

Confidence

Validation Status

Authority Owner

Timestamp

Replay Reference

---

# Confidence Propagation

Confidence is inherited from supporting evidence.

Inputs:

* Dataset Quality
* Dataset Freshness
* Coverage
* Reliability
* Contradictions

Output:

Recommendation Confidence

Example:

Evidence Confidence = 0.90

Risk Confidence = 0.85

Validation Confidence = 0.95

Final Confidence = 0.90

---

# Operator Guidance Layer

NICAI does not stop at recommendations.

It provides guidance.

Example:

Recommendation:

Reduce Vessel Draft

Reason:

River depth decreasing.

Expected Outcome:

Reduced grounding risk.

Alternative:

Use alternate channel.

Confidence:

0.91

---

# Explainability Requirements

Every recommendation must answer:

* What happened?
* Why did it happen?
* What evidence supports it?
* Which datasets were used?
* Which risks were evaluated?
* Which alternatives were considered?
* Why was this option selected?
* What confidence supports it?

---

# Integration Architecture

Marine MasterDB

Provides:

* Operational Knowledge
* Asset Knowledge
* Infrastructure Knowledge

↓

Runtime Telemetry

Provides:

* Real-Time Observations
* Sensor Events

↓

NICAI Cognitive Engine

Performs:

* Reasoning
* Risk Analysis
* Opportunity Analysis
* Decision Generation

↓

SVACS

Validates:

* Evidence
* Confidence
* Recommendations

↓

Operations Command Center

Displays:

* Recommendations
* Risks
* Confidence
* Explanations

---

# Replay Capability

Every decision must be replayable.

Replay includes:

* Original Observation
* Signals Generated
* Context Retrieved
* Memory References
* Risk Analysis
* Opportunity Analysis
* Decision Comparison
* Final Recommendation

Purpose:

Auditability and operator trust.

---

# Failure Modes

## Missing Data

Impact:

Reduced confidence.

Action:

Flag incomplete evidence.

---

## Contradictory Evidence

Impact:

Recommendation uncertainty.

Action:

Trigger validation review.

---

## Outdated Data

Impact:

Potentially inaccurate recommendations.

Action:

Reduce confidence score.

---

## Validation Failure

Impact:

Recommendation blocked.

Action:

Escalate to operator.

---

# Success Criteria

NICAI is successful when an operator can ask:

"What should I do?"

and receive:

Observation
→ Evidence
→ Context
→ Memory
→ Risks
→ Opportunities
→ Recommendation
→ Confidence
→ Validation
→ Explanation

without requiring manual analysis.

---

# Final Principle

NICAI is not a rule engine.

NICAI is a deterministic cognitive intelligence system that transforms observations into explainable, validated and replayable operational decisions while keeping the human operator in control.
