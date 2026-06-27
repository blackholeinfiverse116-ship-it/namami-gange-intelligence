# JSON CONTRACTS

## Project

Marine Intelligence Cognitive Architecture

Version: 1.0

Status: Draft Standard

---

# Purpose

This document defines the standard JSON structures used by the Marine Intelligence System.

Every module in the system must exchange information using these contracts.

These contracts ensure:

* Consistent data exchange
* Explainable intelligence
* Complete traceability
* Replay capability
* Validation support
* Governance compliance

Without standard contracts, different systems may produce inconsistent outputs.

---

# Why JSON Contracts Are Important

The Marine Intelligence System is made up of multiple components:

* Marine MasterDB
* Runtime Telemetry
* NICAI
* SVACS
* Operations Command Center

All of these systems must communicate using the same structure.

Instead of:

Dataset → Recommendation

the system follows:

Observation
↓
Signal
↓
Evidence
↓
Risk / Opportunity
↓
Recommendation
↓
Decision
↓
Validation
↓
Replay

Every step is recorded and traceable.

---

# Contract Categories

The Marine Intelligence System uses the following contracts:

1. Observation Contract
2. Signal Contract
3. Evidence Contract
4. Risk Contract
5. Opportunity Contract
6. Recommendation Contract
7. Decision Contract
8. Validation Contract
9. Event Contract
10. Replay Contract

---

# 1. Observation Contract

## Purpose

Stores raw observations received from:

* Sensors
* Telemetry systems
* Datasets
* Operators
* External agencies

## Example

```json
{
  "observation_id": "OBS-001",
  "timestamp": "2025-08-15T10:30:00Z",
  "source": "CWC",
  "entity": "Varanasi River Station",
  "observation_type": "WaterLevel",
  "value": 4.5,
  "unit": "meters",
  "status": "active"
}
```

## Required Fields

| Field            | Description           |
| ---------------- | --------------------- |
| observation_id   | Unique observation ID |
| timestamp        | Observation time      |
| source           | Data source           |
| entity           | Related entity        |
| observation_type | Type of observation   |
| value            | Recorded value        |
| unit             | Measurement unit      |
| status           | Active or archived    |

---

# 2. Signal Contract

## Purpose

Signals are meaningful patterns derived from observations.

Example:

Observation:

Water Level = 4.5 m

Signal:

Water Level Decreasing

## Example

```json
{
  "signal_id": "SIG-001",
  "derived_from": "OBS-001",
  "signal_type": "DecreasingWaterLevel",
  "severity": "Medium",
  "confidence": 0.85
}
```

## Required Fields

| Field        | Description        |
| ------------ | ------------------ |
| signal_id    | Unique signal ID   |
| derived_from | Source observation |
| signal_type  | Signal name        |
| severity     | Signal severity    |
| confidence   | Confidence score   |

---

# 3. Evidence Contract

## Purpose

Stores supporting evidence used by NICAI.

Evidence explains why the system believes something is true.

## Example

```json
{
  "evidence_id": "EV-001",
  "entity": "Varanasi",
  "evidence_type": "NavigationEvidence",
  "source_dataset": "cwc_river_stations",
  "support_strength": "High",
  "confidence": 0.90
}
```

## Required Fields

| Field            | Description        |
| ---------------- | ------------------ |
| evidence_id      | Evidence ID        |
| entity           | Related entity     |
| evidence_type    | Evidence category  |
| source_dataset   | Supporting dataset |
| support_strength | Evidence strength  |
| confidence       | Confidence score   |

---

# 4. Risk Contract

## Purpose

Represents risks identified by the intelligence system.

Examples:

* Flood Risk
* Navigation Risk
* Cargo Risk
* Weather Risk

## Example

```json
{
  "risk_id": "RISK-001",
  "risk_type": "FloodRisk",
  "location": "Patna",
  "severity": "High",
  "confidence": 0.88,
  "evidence": [
    "EV-001",
    "EV-002"
  ]
}
```

## Required Fields

| Field      | Description         |
| ---------- | ------------------- |
| risk_id    | Risk identifier     |
| risk_type  | Risk category       |
| location   | Related location    |
| severity   | Risk severity       |
| confidence | Confidence score    |
| evidence   | Supporting evidence |

---

# 5. Opportunity Contract

## Purpose

Represents operational opportunities identified by the system.

Examples:

* Cargo Expansion
* New Trade Route
* Terminal Development
* Seaplane Operations

## Example

```json
{
  "opportunity_id": "OPP-001",
  "type": "CargoExpansion",
  "location": "Varanasi",
  "priority": "High",
  "confidence": 0.92,
  "supporting_evidence": [
    "EV-010"
  ]
}
```

## Required Fields

| Field               | Description          |
| ------------------- | -------------------- |
| opportunity_id      | Opportunity ID       |
| type                | Opportunity type     |
| location            | Opportunity location |
| priority            | Priority level       |
| confidence          | Confidence score     |
| supporting_evidence | Evidence list        |

---

# 6. Recommendation Contract

## Purpose

Stores recommendations generated by NICAI.

Recommendations are suggested actions for operators.

## Example

```json
{
  "recommendation_id": "REC-001",
  "recommendation": "Reduce vessel draft",
  "reason": "Water level decreasing",
  "confidence": 0.89,
  "risk_level": "Medium",
  "supporting_evidence": [
    "EV-001"
  ]
}
```

## Required Fields

| Field               | Description               |
| ------------------- | ------------------------- |
| recommendation_id   | Recommendation ID         |
| recommendation      | Suggested action          |
| reason              | Reason for recommendation |
| confidence          | Confidence score          |
| risk_level          | Associated risk           |
| supporting_evidence | Evidence list             |

---

# 7. Decision Contract

## Purpose

Stores final decisions made by operators.

A recommendation becomes a decision only after approval.

## Example

```json
{
  "decision_id": "DEC-001",
  "selected_recommendation": "REC-001",
  "approved_by": "Operations Command Center",
  "timestamp": "2025-08-15T11:00:00Z",
  "status": "Approved"
}
```

## Required Fields

| Field                   | Description           |
| ----------------------- | --------------------- |
| decision_id             | Decision ID           |
| selected_recommendation | Chosen recommendation |
| approved_by             | Decision authority    |
| timestamp               | Decision time         |
| status                  | Decision status       |

---

# 8. Validation Contract

## Purpose

Stores validation results generated by SVACS.

Validation confirms whether intelligence outputs are reliable.

## Example

```json
{
  "validation_id": "VAL-001",
  "object_type": "Recommendation",
  "object_id": "REC-001",
  "validation_status": "Passed",
  "validated_by": "SVACS",
  "validation_time": "2025-08-15T11:05:00Z"
}
```

## Required Fields

| Field             | Description          |
| ----------------- | -------------------- |
| validation_id     | Validation ID        |
| object_type       | Object category      |
| object_id         | Object identifier    |
| validation_status | Validation result    |
| validated_by      | Validation authority |
| validation_time   | Validation timestamp |

---

# 9. Event Contract

## Purpose

Stores runtime events generated by the operational environment.

Examples:

* Flood Warning
* AIS Signal Loss
* Weather Alert
* Terminal Congestion

## Example

```json
{
  "event_id": "EVT-001",
  "event_type": "FloodWarningReceived",
  "timestamp": "2025-08-15T09:00:00Z",
  "source": "IMD",
  "location": "Patna",
  "severity": "High"
}
```

## Required Fields

| Field      | Description    |
| ---------- | -------------- |
| event_id   | Event ID       |
| event_type | Event category |
| timestamp  | Event time     |
| source     | Event source   |
| location   | Event location |
| severity   | Event severity |

---

# 10. Replay Contract

## Purpose

Stores complete intelligence history.

Allows operators to replay and audit decisions.

## Example

```json
{
  "replay_id": "REP-001",
  "decision_id": "DEC-001",
  "observation_chain": [
    "OBS-001"
  ],
  "evidence_chain": [
    "EV-001"
  ],
  "recommendation_chain": [
    "REC-001"
  ],
  "validation_chain": [
    "VAL-001"
  ]
}
```

## Required Fields

| Field                | Description            |
| -------------------- | ---------------------- |
| replay_id            | Replay ID              |
| decision_id          | Related decision       |
| observation_chain    | Observation history    |
| evidence_chain       | Evidence history       |
| recommendation_chain | Recommendation history |
| validation_chain     | Validation history     |

---

# Governance Rules

Every contract must follow these rules:

1. Every object must have a unique ID.
2. Every object must have a timestamp.
3. Every recommendation must have evidence.
4. Every decision must be validated.
5. Every validation must be traceable.
6. Every event must be replayable.
7. Every confidence score must be explainable.
8. Every object must support audit and replay.

---

# Intelligence Lifecycle

```text
Observation
      ↓
Signal
      ↓
Evidence
      ↓
Risk / Opportunity
      ↓
Recommendation
      ↓
Decision
      ↓
Validation
      ↓
Replay
```

This lifecycle ensures that every recommendation generated by the Marine Intelligence System can be traced back to its original observation and fully explained to operators, auditors, validators and decision-makers.

---

# Conclusion

The JSON Contracts define the common language of the Marine Intelligence System.

They ensure that every observation, signal, recommendation and decision is:

* Explainable
* Traceable
* Validatable
* Replayable
* Governed

These contracts form the foundation for trusted marine intelligence operations across NICAI, SVACS, Marine MasterDB, Runtime Telemetry and the Operations Command Center.
