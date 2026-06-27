# DECISION COGNITION DIAGRAM

## Purpose

This document explains how NICAI (National Intelligence and Cognitive Assessment Infrastructure) thinks before making any operational recommendation.

The objective is to make NICAI behave like an experienced Commodore rather than a simple rule engine.

A rule engine asks:

"If condition is true, what action should be taken?"

A cognitive engine asks:

* What happened?
* Why did it happen?
* What evidence exists?
* What risks exist?
* What opportunities exist?
* What historical situations are similar?
* What are the possible actions?
* Which action is best?
* Why is it best?
* What could go wrong?

Only after answering these questions does NICAI generate a recommendation.

---

# Traditional System

Most systems operate like this:

```text
Input
   ↓
Rule
   ↓
Recommendation
```

Example:

```text
River Depth < 2.0m
       ↓
Reduce Vessel Draft
```

This approach is simple but lacks context.

---

# NICAI Cognitive Decision Model

NICAI operates using multiple reasoning layers.

```text
Observation
      ↓
Evidence
      ↓
Context
      ↓
Memory
      ↓
Constraints
      ↓
Opportunities
      ↓
Risks
      ↓
Decision Candidates
      ↓
Conflict Resolution
      ↓
Decision Selection
      ↓
Validation
      ↓
Operator Guidance
```

---

# Complete Decision Cognition Flow

```text
Reality
   ↓

Observation
   ↓

Signal Detection
   ↓

Pattern Recognition
   ↓

Context Understanding
   ↓

Historical Comparison
   ↓

Constraint Analysis
   ↓

Opportunity Analysis
   ↓

Risk Assessment
   ↓

Decision Generation
   ↓

Decision Comparison
   ↓

Decision Selection
   ↓

Validation
   ↓

Governance Check
   ↓

Operator Recommendation
```

---

# Stage 1: Observation

## Purpose

Collect facts from operational systems.

Examples:

* River depth
* Water level
* Cargo volume
* Terminal utilization
* Vessel location
* Weather alerts

---

## Example

Observation:

```text
River Depth = 2.1m
```

NICAI does not make a decision yet.

It simply records the observation.

---

# Stage 2: Evidence Creation

## Purpose

Convert observations into usable evidence.

---

## Example

Observation:

```text
River Depth = 2.1m
```

Evidence:

```text
Depth is approaching operational threshold.
```

Evidence is stronger than raw data because it has meaning.

---

# Stage 3: Context Understanding

## Purpose

Understand operational conditions.

---

## Questions

NICAI asks:

* Which river?
* Which corridor?
* Which season?
* Which vessels are affected?
* Which terminals are affected?

---

## Example

Depth = 2.1m

During Monsoon:

Low concern

During Dry Season:

High concern

Same observation.

Different context.

Different decision.

---

# Stage 4: Memory Retrieval

## Purpose

Retrieve relevant historical knowledge.

---

## Memory Types

* Operational Memory
* Seasonal Memory
* Historical Memory
* Incident Memory
* Decision Memory

---

## Example

Current Situation:

```text
Depth Falling Rapidly
```

Historical Memory:

```text
Similar event occurred in 2022.
```

Outcome:

```text
Navigation restrictions required after 5 days.
```

NICAI learns from previous situations.

---

# Stage 5: Constraint Analysis

## Purpose

Identify operational limitations.

---

## Examples

Constraints may include:

* Low water depth
* Regulatory restrictions
* Terminal congestion
* Weather warnings
* Environmental protection zones

---

## Example

Constraint:

```text
River depth below safe navigation threshold.
```

---

# Stage 6: Opportunity Analysis

## Purpose

Identify positive operational possibilities.

---

## Examples

Opportunity:

```text
Terminal has spare capacity.
```

Opportunity:

```text
Weather conditions favorable.
```

Opportunity:

```text
Additional cargo can be moved.
```

NICAI always evaluates opportunities alongside risks.

---

# Stage 7: Risk Assessment

## Purpose

Understand possible negative outcomes.

---

## Risk Categories

* Flood Risk
* Navigation Risk
* Cargo Risk
* Infrastructure Risk
* Weather Risk
* Environmental Risk

---

## Example

Inputs:

```text
Low Water Depth
High Vessel Traffic
```

Risk:

```text
Navigation Risk = High
```

---

# Stage 8: Decision Generation

## Purpose

Generate all possible actions.

---

## Example

Situation:

```text
Navigation Risk High
```

Possible Decisions:

```text
Option A
Continue Operations

Option B
Reduce Draft

Option C
Reduce Cargo Load

Option D
Suspend Operations
```

NICAI never selects the first option automatically.

All options are evaluated.

---

# Stage 9: Decision Comparison

## Purpose

Compare competing recommendations.

---

## Decision Evaluation Matrix

```text
Decision A
   ↓
Benefits
Risks
Cost

Decision B
   ↓
Benefits
Risks
Cost

Decision C
   ↓
Benefits
Risks
Cost
```

---

## Example

| Decision     | Safety    | Cost      | Operational Impact |
| ------------ | --------- | --------- | ------------------ |
| Continue     | Low       | Low       | High Risk          |
| Reduce Draft | High      | Medium    | Low Impact         |
| Suspend      | Very High | Very High | Major Impact       |

NICAI evaluates trade-offs.

---

# Stage 10: Conflict Resolution

## Purpose

Resolve competing recommendations.

---

## Example

Recommendation 1:

```text
Increase Cargo Throughput
```

Recommendation 2:

```text
Reduce Vessel Movement
```

Conflict Detected.

NICAI must determine:

* Which objective is more important?
* Which risk is greater?
* Which authority has priority?

Only then can a decision proceed.

---

# Stage 11: Decision Selection

## Purpose

Choose the most appropriate action.

---

## Selection Factors

* Evidence Strength
* Risk Level
* Opportunity Value
* Historical Outcomes
* Policy Compliance
* Operational Objectives

---

## Example

Selected Decision:

```text
Reduce Vessel Draft by 20%
```

Reason:

```text
Lowest risk with minimal operational disruption.
```

---

# Stage 12: Validation

## Purpose

Verify decision correctness.

---

## Validation Checks

* Evidence Available?
* Data Quality Acceptable?
* Contradictions Present?
* Confidence Sufficient?
* Policy Compliant?

---

## Example

```text
Validation Status = PASSED
```

---

# Stage 13: Governance Check

## Purpose

Ensure authority compliance.

---

## Questions

* Is the recommendation permitted?
* Is authorization required?
* Is it compliant with regulations?
* Does it violate operational policy?

---

## Example

Recommendation:

```text
Close Terminal
```

Check:

```text
Port Authority Approval Required
```

Without approval:

```text
Recommendation Blocked
```

---

# Stage 14: Operator Guidance

## Purpose

Deliver actionable intelligence.

---

## Final Output Structure

```text
Situation

Evidence

Risk Assessment

Opportunities

Recommended Action

Confidence

Validation Status

Operational Notes
```

---

# Example Cognitive Decision

## Situation

Water depth decreasing rapidly.

---

## Evidence

* River station measurements
* Telemetry observations
* Historical trend analysis

---

## Risk

High navigation risk.

---

## Opportunities

Cargo movement can continue with restrictions.

---

## Recommendation

Reduce vessel draft by 20%.

---

## Confidence

0.92

---

## Validation

Passed

---

## Governance

Approved

---

# Cognitive Decision Diagram

```text
Observation
      ↓
Evidence
      ↓
Context
      ↓
Memory
      ↓
Constraints
      ↓
Opportunities
      ↓
Risks
      ↓
Decision Options
      ↓
Conflict Resolution
      ↓
Decision Selection
      ↓
Validation
      ↓
Governance
      ↓
Recommendation
      ↓
Operator Action
```

---

# Key Principle

NICAI does not make decisions because a rule fired.

NICAI makes decisions because evidence, context, memory, risks, opportunities, constraints, validation and governance collectively support a specific course of action.

Every recommendation must be explainable.

Every recommendation must be traceable.

Every recommendation must be replayable.

Every recommendation must be defensible.

No decision exists without evidence.

No evidence exists without provenance.

No recommendation exists without validation.
