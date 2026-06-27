# MARINE STATE MACHINE CATALOGUE

## Document Information

Document Name: Marine State Machine Catalogue

System: NICAI Marine Intelligence System

Version: 1.0

Status: Architecture Specification

Owner: Marine Intelligence Team

---

# 1. Purpose

Marine operations are stateful.

A river is not always in the same condition.

A terminal is not always ready.

A vessel is not always operational.

A recommendation is not always valid.

NICAI requires deterministic state machines to ensure predictable, explainable and governable behavior.

Every major entity in the Marine Intelligence System must have:

* Defined states
* State transitions
* Transition triggers
* Authority ownership
* Recovery paths
* Audit history

No entity may change state without traceable evidence.

---

# 2. State Machine Principles

Every state transition must answer:

* What changed?
* Why did it change?
* Who authorized it?
* What evidence triggered it?
* How can it return to a healthy state?

---

# 3. River State Machine

## Purpose

Represents operational river conditions.

### States

Normal
↓
Watch
↓
Alert
↓
Restricted
↓
Emergency
↓
Recovery
↓
Normal

---

### Normal

Conditions:

* Safe navigation
* Stable water levels
* No active restrictions

Authority:

NICAI

---

### Watch

Trigger:

* Water level trend changing
* Weather concern detected
* Minor navigation issues

Authority:

NICAI

Recovery:

Return to Normal when conditions stabilize.

---

### Alert

Trigger:

* Flood indicators increasing
* Rapid water level variation
* Navigation degradation

Authority:

Operations Command Center

Recovery:

Conditions improve.

---

### Restricted

Trigger:

* Unsafe navigation
* Draft limitations
* Regulatory restrictions

Authority:

River Authority

Recovery:

Restrictions removed.

---

### Emergency

Trigger:

* Severe flooding
* River closure
* Major safety risk

Authority:

Emergency Operations Authority

Recovery:

Emergency resolved.

---

### Recovery

Trigger:

Emergency conditions end.

Authority:

Operations Command Center

Recovery:

Return to Normal.

---

# 4. Terminal State Machine

## States

Planned
↓
Construction
↓
Operational
↓
Congested
↓
Restricted
↓
Maintenance
↓
Operational

---

### Planned

Terminal approved but not operational.

---

### Construction

Infrastructure development underway.

---

### Operational

Normal operations.

---

### Congested

Trigger:

* Utilization above threshold
* Cargo backlog

---

### Restricted

Trigger:

* Capacity limitations
* Safety concerns
* Regulatory restrictions

---

### Maintenance

Trigger:

* Scheduled maintenance
* Emergency repair

Recovery:

Return to Operational.

---

# 5. Vessel State Machine

## States

Registered
↓
Available
↓
Assigned
↓
In Transit
↓
Docked
↓
Maintenance
↓
Available

---

### Registered

Vessel exists in registry.

---

### Available

Ready for assignment.

---

### Assigned

Mission allocated.

---

### In Transit

Active voyage.

---

### Docked

At terminal or jetty.

---

### Maintenance

Under inspection or repair.

Recovery:

Return to Available.

---

# 6. Cargo State Machine

## States

Created
↓
Scheduled
↓
Loaded
↓
In Transit
↓
Delivered
↓
Closed

---

### Created

Cargo registered.

---

### Scheduled

Movement planned.

---

### Loaded

Cargo loaded on vessel.

---

### In Transit

Movement underway.

---

### Delivered

Cargo reached destination.

---

### Closed

Shipment completed.

---

# 7. Corridor State Machine

## States

Available
↓
Monitored
↓
Restricted
↓
Closed
↓
Recovery
↓
Available

---

### Available

Normal corridor operations.

---

### Monitored

Potential issues detected.

---

### Restricted

Operational limitations imposed.

---

### Closed

Movement prohibited.

---

### Recovery

Conditions improving.

---

# 8. Recommendation State Machine

## States

Generated
↓
Under Review
↓
Validated
↓
Approved
↓
Executed
↓
Archived

---

### Generated

Created by NICAI.

---

### Under Review

Pending validation.

---

### Validated

Validated by SVACS.

---

### Approved

Approved by authority.

---

### Executed

Action completed.

---

### Archived

Stored for replay.

---

# 9. Decision State Machine

## States

Candidate
↓
Evaluated
↓
Selected
↓
Approved
↓
Implemented
↓
Closed

---

### Candidate

Potential decision.

---

### Evaluated

Evidence assessed.

---

### Selected

Chosen among alternatives.

---

### Approved

Authorized.

---

### Implemented

Applied operationally.

---

### Closed

Decision lifecycle completed.

---

# 10. Validation State Machine

## States

Pending
↓
Evidence Review
↓
Validated
↓
Rejected
↓
Archived

---

### Pending

Awaiting validation.

---

### Evidence Review

Evidence assessment underway.

---

### Validated

Recommendation accepted.

---

### Rejected

Recommendation failed validation.

---

### Archived

Stored for audit.

---

# 11. Incident State Machine

## States

Detected
↓
Verified
↓
Active
↓
Mitigated
↓
Resolved
↓
Archived

---

### Detected

Incident reported.

---

### Verified

Confirmed by evidence.

---

### Active

Response underway.

---

### Mitigated

Impact reduced.

---

### Resolved

Incident closed.

---

### Archived

Stored in incident memory.

---

# 12. Mission State Machine

## States

Planned
↓
Approved
↓
Assigned
↓
Executing
↓
Completed
↓
Archived

---

### Planned

Mission proposed.

---

### Approved

Mission authorized.

---

### Assigned

Resources allocated.

---

### Executing

Mission underway.

---

### Completed

Objectives achieved.

---

### Archived

Mission history retained.

---

# 13. Transition Contract

Every state transition follows a common structure.

```json
{
  "entity_id": "",
  "entity_type": "",
  "current_state": "",
  "next_state": "",
  "trigger": "",
  "conditions": [],
  "authority": "",
  "evidence_ids": [],
  "timestamp": "",
  "recovery_path": ""
}
```

---

# 14. Event Driven State Changes

State changes occur through events.

Examples:

RiverLevelDropped

FloodWarningReceived

TerminalCapacityExceeded

MaintenanceScheduled

CargoDelivered

MissionCompleted

RecommendationValidated

DecisionApproved

Every event generates a state transition record.

---

# 15. Governance Rules

No state transition may occur without:

* Evidence
* Timestamp
* Authority
* Traceability
* Audit record

Manual overrides must be recorded.

---

# 16. Replay Integration

Every state transition is stored in Replay Memory.

Replay Example:

River

Normal
↓
Watch
↓
Alert
↓
Restricted
↓
Recovery
↓
Normal

Operators can replay the complete lifecycle.

---

# 17. Integration Mapping

Marine MasterDB

Provides:

Entity State Definitions

---

Runtime Telemetry

Provides:

State Triggers

---

NICAI

Evaluates:

State Conditions

Generates:

State Recommendations

---

SVACS

Validates:

State Changes

---

Operations Command Center

Approves:

Critical State Transitions

---

# 18. Success Criteria

The Marine State Machine Catalogue is successful when:

* Every entity has a deterministic lifecycle.
* Every transition is explainable.
* Every state change has evidence.
* Every transition is auditable.
* Every state can be replayed.
* Every authority is defined.
* Every recovery path is documented.

The result is a predictable, governed and explainable Marine Intelligence System where operational behavior is driven by state, evidence and authority rather than ad-hoc rules.
