# DECISION NEGOTIATION FRAMEWORK

## Purpose

The Decision Negotiation Framework defines how NICAI evaluates, compares, negotiates and selects operational decisions.

The objective is to ensure that recommendations are not generated through isolated rules.

Instead, recommendations emerge from a structured evaluation of:

* Observations
* Evidence
* Context
* Historical Memory
* Risks
* Opportunities
* Operational Objectives
* Governance Rules

Every recommendation must compete against alternative recommendations before becoming the final operational guidance.

---

# Core Principle

Traditional Systems:

Condition

↓

Rule

↓

Recommendation

NICAI:

Observation

↓

Evidence

↓

Context

↓

Risk Assessment

↓

Opportunity Assessment

↓

Decision Candidates

↓

Negotiation

↓

Conflict Resolution

↓

Decision Selection

↓

Validation

↓

Operator Guidance

NICAI does not select the first possible recommendation.

NICAI selects the best explainable recommendation.

---

# Why Negotiation Is Required

Operational environments contain competing priorities.

Examples:

* Safety vs Throughput
* Speed vs Cost
* Capacity vs Risk
* Revenue vs Environmental Protection
* Operational Continuity vs Regulatory Compliance

Without negotiation, recommendations may become inconsistent.

The framework ensures balanced decision-making.

---

# Decision Candidate Generation

Every operational situation must generate multiple candidate decisions.

Example:

Situation:

River depth decreasing.

Candidate A:

Continue Operations

Candidate B:

Reduce Vessel Draft

Candidate C:

Reduce Cargo Load

Candidate D:

Suspend Operations

Each candidate enters the negotiation process.

---

# Decision Candidate Structure

Every candidate contains:

Decision ID

Decision Title

Description

Supporting Evidence

Supporting Risks

Supporting Opportunities

Expected Benefits

Expected Consequences

Confidence

Priority Score

Validation Status

Authority Owner

Timestamp

---

# Decision Evaluation Criteria

NICAI evaluates all candidates using common criteria.

## Safety Impact

Questions:

* Does the decision improve safety?
* Does it reduce operational hazards?

Priority:

Highest

---

## Regulatory Compliance

Questions:

* Does the decision satisfy regulations?
* Does it violate restrictions?

Priority:

Very High

---

## Operational Continuity

Questions:

* Does the decision maintain operations?
* Does it reduce downtime?

Priority:

High

---

## Infrastructure Readiness

Questions:

* Can current infrastructure support this decision?

Priority:

High

---

## Economic Impact

Questions:

* Does the decision improve efficiency?
* Does it reduce losses?

Priority:

Medium

---

## Environmental Impact

Questions:

* Does the decision protect environmental conditions?

Priority:

Medium

---

# Decision Ranking Engine

Candidates are ranked according to:

Safety

↓

Regulatory Compliance

↓

Operational Continuity

↓

Infrastructure Readiness

↓

Economic Benefit

↓

Environmental Benefit

Highest-ranked candidate becomes preferred.

---

# Competing Recommendation Resolution

Operational intelligence often produces conflicting recommendations.

Example:

Recommendation 1:

Increase Cargo Throughput

Reason:

High demand

Recommendation 2:

Reduce Vessel Load

Reason:

Low water depth

Conflict Exists

↓

Negotiation Required

---

# Conflict Resolution Hierarchy

NICAI resolves conflicts using deterministic priorities.

Priority Order:

1. Human Safety
2. Regulatory Compliance
3. Environmental Protection
4. Infrastructure Integrity
5. Operational Continuity
6. Economic Optimization

Higher priorities always override lower priorities.

---

# Example Conflict Resolution

Situation:

Cargo demand increasing.

Opportunity:

Increase Throughput

Risk:

Flood Warning Issued

Conflict:

Revenue Growth

vs

Operational Safety

Resolution:

Flood Risk Overrides Revenue Goal

Decision:

Reduce Operations

Reason:

Safety Priority Dominates

---

# Objective Optimization Framework

NICAI balances multiple objectives simultaneously.

Objectives:

* Safety
* Reliability
* Capacity
* Efficiency
* Sustainability
* Economic Value

Optimization remains deterministic.

No probabilistic black-box optimization is permitted.

---

# Recommendation Strength Assessment

Recommendations are categorized as:

## Mandatory

Must be executed.

Example:

Suspend Operations During Severe Flooding

---

## Strongly Recommended

Execution highly advised.

Example:

Reduce Draft Due To Falling Water Levels

---

## Recommended

Operational improvement opportunity.

Example:

Reroute Cargo To Alternate Terminal

---

## Informational

Awareness only.

Example:

Expected Increase In Seasonal Traffic

---

# Decision Confidence Assessment

Every candidate receives confidence.

Confidence Inputs:

* Dataset Quality
* Data Freshness
* Evidence Strength
* Validation Status
* Contradictions
* Historical Consistency

Example:

Decision A

Confidence:

0.93

Decision B

Confidence:

0.78

Decision A receives preference.

---

# Contradiction Management

Contradictory evidence must trigger negotiation review.

Example:

Evidence A:

River Navigable

Evidence B:

Navigation Restriction Active

Result:

Contradiction Detected

↓

Validation Required

↓

Confidence Reduced

↓

Decision Review Triggered

---

# Alternative Decision Registry

Rejected decisions are not discarded.

NICAI stores:

* Selected Decision
* Alternative Decisions
* Rejection Reasons

Purpose:

Explainability

Example:

Selected:

Reduce Vessel Draft

Rejected:

Suspend Operations

Reason:

Risk below emergency threshold

---

# Escalation Framework

Certain situations require human review.

Triggers:

* Low Confidence
* Contradictory Evidence
* Policy Conflict
* Regulatory Ambiguity
* Emergency Conditions

Escalation Path:

NICAI

↓

SVACS

↓

Operations Command Center

↓

Operator Review

---

# Decision Contract

Every final decision must include:

Decision ID

Decision Title

Decision Type

Supporting Evidence

Evidence Tree

Risks Considered

Opportunities Considered

Alternative Decisions

Selection Reason

Confidence

Validation Status

Authority Owner

Timestamp

Replay Reference

---

# Governance Controls

NICAI cannot bypass governance.

Every decision must satisfy:

* MDU Policies
* SVACS Validation Rules
* Operational Directives
* Regulatory Requirements

Non-compliant decisions are rejected.

---

# Replay Requirements

Every decision must be replayable.

Replay Includes:

Observation

↓

Evidence

↓

Context

↓

Risk Analysis

↓

Opportunity Analysis

↓

Candidate Generation

↓

Negotiation

↓

Conflict Resolution

↓

Decision Selection

↓

Validation

Purpose:

Auditability

---

# Failure Scenarios

## No Valid Decision

Cause:

All candidates violate policy.

Action:

Escalate to Operator.

---

## Conflicting High-Priority Risks

Cause:

Multiple critical risks active.

Action:

Generate emergency review.

---

## Insufficient Evidence

Cause:

Missing data.

Action:

Reduce confidence and request additional evidence.

---

## Governance Rejection

Cause:

Decision violates regulations.

Action:

Block recommendation.

---

# Integration Architecture

Runtime Telemetry

↓

Observation Intelligence

↓

Evidence Fabric

↓

Risk Intelligence

↓

Opportunity Intelligence

↓

Decision Negotiation Framework

↓

NICAI Decision Engine

↓

SVACS Validation

↓

Operations Command Center

---

# Success Criteria

An operator should be able to ask:

"What should I do?"

and NICAI should provide:

Situation

↓

Evidence

↓

Risks

↓

Opportunities

↓

Possible Decisions

↓

Why One Decision Was Selected

↓

Why Others Were Rejected

↓

Confidence

↓

Validation Status

↓

Operator Guidance

without requiring manual analysis.

---

# Final Principle

NICAI does not make decisions because a rule fired.

NICAI makes decisions because evidence, context, memory, risks, opportunities and governance collectively support one decision more strongly than all competing alternatives.

Every decision must be explainable, auditable, replayable and governed.
