# MARINE KNOWLEDGE GRAPH SPECIFICATION

## Document Information

Project: NICAI Marine Intelligence System

Version: 1.0

Status: Architecture Design

Owner: Marine Intelligence Team

Purpose:

Define the canonical Marine Knowledge Graph that powers intelligence, reasoning, recommendations, validation, replay and explainability.

---

# 1. Objective

The Marine Knowledge Graph serves as the foundational intelligence fabric of NICAI.

Its purpose is to transform isolated datasets into a connected knowledge ecosystem where every observation, signal, decision and recommendation can be traced through relationships.

The graph enables:

* Explainable Intelligence
* Decision Support
* Risk Assessment
* Recommendation Generation
* Validation
* Replay
* Governance
* Traceability

---

# 2. Core Philosophy

Marine Intelligence is not a collection of datasets.

Marine Intelligence is a connected ecosystem.

Reality
↓
Observation
↓
Signal
↓
Meaning
↓
Relationship
↓
Context
↓
Memory
↓
Evidence
↓
Decision
↓
Validation
↓
Learning

Every intelligence output must be explainable through graph relationships.

---

# 3. Knowledge Graph Layers

The graph is organized into layers.

## Layer 1 — Physical World

Represents real-world entities.

Examples:

* River
* River Reach
* Channel
* Water Body
* Station
* Gauge
* Bridge
* Port
* Jetty
* Terminal
* Logistics Park

---

## Layer 2 — Operational Layer

Represents operational assets.

Examples:

* Vessel
* Crew
* Mission
* Cargo
* Commodity
* Route
* Corridor

---

## Layer 3 — Environmental Layer

Represents environmental conditions.

Examples:

* Weather Cell
* Flood Event
* Water Quality Observation
* River Health Indicator
* Seasonal Condition

---

## Layer 4 — Intelligence Layer

Represents derived intelligence.

Examples:

* Risk
* Constraint
* Opportunity
* Recommendation
* Assessment

---

## Layer 5 — Governance Layer

Represents oversight and validation.

Examples:

* Validation Record
* Authority
* Regulation
* Policy
* Compliance Assessment

---

# 4. Entity Model

Every entity must follow a common structure.

## Mandatory Fields

### Identity

Unique identifier.

Example:

River:GANGA

Terminal:VARANASI_MMT

---

### Attributes

Entity properties.

Example:

River

* Name
* Length
* Basin
* Navigability

Terminal

* Capacity
* Status
* Operator

---

### Lifecycle

Entity lifecycle stages.

Example:

Terminal

Planned
↓
Construction
↓
Operational
↓
Maintenance
↓
Retired

---

### Relationships

Links to other entities.

Example:

Terminal
→ located_in → River Reach

---

### Authority Owner

Responsible authority.

Examples:

* IWAI
* CPCB
* CWC
* Port Authority
* State Government

---

### State

Current operational state.

Examples:

* Active
* Inactive
* Restricted
* Emergency

---

### Version

Version number.

Example:

v1.0

v1.1

v2.0

---

### Traceability

Source records supporting the entity.

Example:

Dataset

Record ID

Timestamp

Source Authority

---

# 5. Core Entities

## River

Represents a navigable river system.

Attributes:

* River ID
* Name
* Basin
* Length
* Navigability Status

Authority:

CWC

Relationships:

* contains River Reach
* contains Stations
* contains Channels

---

## River Reach

A managed river segment.

Attributes:

* Reach ID
* Start Coordinate
* End Coordinate
* Length

Relationships:

* belongs_to River
* contains Stations
* serves Terminals

---

## Channel

Navigable water path.

Attributes:

* Width
* Depth
* Status

Relationships:

* belongs_to Reach
* supports Navigation

---

## Station

Observation location.

Attributes:

* Station ID
* Coordinates
* Type

Relationships:

* observes River
* generates Telemetry

---

## Gauge

Water measurement system.

Attributes:

* Gauge Level
* Water Depth
* Flow Rate

Relationships:

* installed_at Station

---

## Terminal

Cargo or passenger terminal.

Attributes:

* Capacity
* Type
* Operational Status

Relationships:

* serves Cargo
* supports Corridor
* located_in Reach

Authority:

IWAI

---

## Jetty

Landing structure.

Attributes:

* Capacity
* Access Type

Relationships:

* connected_to Terminal

---

## Port

Major logistics facility.

Attributes:

* Capacity
* Cargo Throughput

Relationships:

* serves Corridors

---

## Logistics Park

Intermodal logistics facility.

Attributes:

* Capacity
* Connectivity

Relationships:

* connected_to Terminal
* connected_to Road Network
* connected_to Rail Network

---

## Bridge

Transportation infrastructure.

Attributes:

* Clearance
* Span

Relationships:

* crosses River

---

## Cargo

Goods being transported.

Attributes:

* Cargo Type
* Volume
* Weight

Relationships:

* transported_by Vessel
* originates_from Corridor

---

## Commodity

Commodity classification.

Attributes:

* Commodity Name
* Category

Relationships:

* classified_as Cargo

---

## Vessel

Water transport asset.

Attributes:

* Vessel ID
* Draft
* Capacity
* Type

Relationships:

* carries Cargo
* assigned_to Mission

---

## Crew

Operational personnel.

Attributes:

* Crew Size
* Certifications

Relationships:

* assigned_to Vessel

---

## Mission

Operational activity.

Attributes:

* Objective
* Status

Relationships:

* uses Vessel
* affects Corridor

---

## Weather Cell

Weather observation unit.

Attributes:

* Rainfall
* Wind Speed
* Visibility

Relationships:

* influences Risk

---

## Flood Event

Flood occurrence.

Attributes:

* Severity
* Duration

Relationships:

* impacts Reach
* impacts Terminal

---

## Restriction

Operational restriction.

Attributes:

* Restriction Type
* Validity

Relationships:

* constrains Mission

---

## Regulation

Governance rule.

Attributes:

* Regulation ID
* Scope

Relationships:

* governs Operations

---

## Risk

Identified risk.

Attributes:

* Severity
* Likelihood
* Confidence

Relationships:

* derived_from Evidence

---

## Constraint

Operational limitation.

Attributes:

* Type
* Impact

Relationships:

* weakens Recommendation

---

## Opportunity

Positive operational potential.

Attributes:

* Opportunity Type
* Priority

Relationships:

* strengthens Recommendation

---

## Recommendation

Suggested action.

Attributes:

* Recommendation ID
* Action
* Confidence

Relationships:

* supported_by Evidence
* validated_by SVACS

---

## Decision

Approved action.

Attributes:

* Decision ID
* Status

Relationships:

* generated_from Recommendation

---

## Evidence

Supporting fact.

Attributes:

* Source
* Timestamp

Relationships:

* supports Recommendation
* supports Risk

---

## Sensor

Observation device.

Attributes:

* Sensor Type
* Status

Relationships:

* generates Telemetry

---

## Telemetry Event

Runtime observation.

Attributes:

* Timestamp
* Event Type

Relationships:

* generated_by Sensor

---

## Incident

Operational disruption.

Attributes:

* Severity
* Status

Relationships:

* affects Mission

---

## Maintenance

Maintenance activity.

Attributes:

* Type
* Schedule

Relationships:

* applied_to Asset

---

# 6. Traceability Model

Every node must support:

Entity
↓
Source Dataset
↓
Record
↓
Evidence
↓
Assessment
↓
Recommendation
↓
Decision

Nothing can exist without traceability.

---

# 7. Versioning Model

All entities are version controlled.

Example:

Terminal

v1.0

Operational Capacity = 2 MTPA

v1.1

Operational Capacity = 3 MTPA

Historical versions remain accessible.

---

# 8. Governance Principles

The knowledge graph must remain:

* Deterministic
* Explainable
* Auditable
* Replayable
* Governed
* Traceable

No recommendation may be generated without graph-supported evidence.

---

# 9. Success Criteria

The Marine Knowledge Graph is successful when an operator can ask:

Why was this recommendation generated?

and the system can trace:

Recommendation
↓
Evidence
↓
Risk
↓
Observation
↓
Dataset
↓
Authority

with complete transparency and explainability.