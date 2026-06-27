# RELATIONSHIP REGISTRY

## Purpose

The Relationship Registry defines how entities interact with each other inside the Marine Intelligence System.

Entities alone do not create intelligence.

Relationships create intelligence.

For example:

A river by itself is only a geographic feature.

A river connected to a terminal, cargo corridor, flood event, navigation restriction and economic zone becomes operational intelligence.

This registry defines the meaning of every relationship so that all systems reason consistently.

---

# Why Relationships Matter

Marine Intelligence is not built from isolated objects.

It is built from connected knowledge.

Example:

River
↓
Supports
↓
Navigation

Navigation
↓
Enables
↓
Cargo Movement

Cargo Movement
↓
Supports
↓
Economic Activity

Economic Activity
↓
Creates
↓
Demand

Demand
↓
Strengthens
↓
Infrastructure Investment

Without relationships there is no reasoning.

---

# Relationship Categories

Relationships are divided into:

1. Dependency Relationships
2. Support Relationships
3. Constraint Relationships
4. Causal Relationships
5. Validation Relationships
6. Ownership Relationships
7. Spatial Relationships
8. Temporal Relationships
9. Economic Relationships
10. Operational Relationships
11. Environmental Relationships
12. Governance Relationships

---

# 1. DEPENDS_ON

## Meaning

One entity requires another entity to function properly.

## Example

Terminal
depends_on
River Reach

Cargo Movement
depends_on
Navigation Availability

Recommendation
depends_on
Evidence

## Operational Impact

If the parent entity fails, dependent entities become weaker or invalid.

---

# 2. SUPPORTS

## Meaning

One entity strengthens another entity.

## Example

Terminal
supports
Cargo Operations

Logistics Park
supports
Trade Activity

Navigation Channel
supports
Vessel Movement

## Operational Impact

Supporting entities increase confidence and operational capability.

---

# 3. CONSTRAINS

## Meaning

One entity limits another entity.

## Example

Low Water Depth
constrains
Navigation

Flood Event
constrains
Terminal Operations

Environmental Regulation
constrains
Infrastructure Development

## Operational Impact

Constraints reduce operational flexibility.

---

# 4. ENABLES

## Meaning

One entity makes another activity possible.

## Example

Navigable River
enables
Cargo Transport

Terminal
enables
Cargo Handling

Bridge Clearance
enables
Vessel Passage

## Operational Impact

Without enabling entities the operation cannot occur.

---

# 5. INVALIDATES

## Meaning

One entity makes another entity no longer valid.

## Example

Emergency Restriction
invalidates
Normal Navigation Plan

Terminal Closure
invalidates
Cargo Routing Plan

## Operational Impact

Invalidated recommendations must not be executed.

---

# 6. CONTRADICTS

## Meaning

Two pieces of information conflict with each other.

## Example

Telemetry
contradicts
Manual Report

Sensor Reading
contradicts
Historical Expectation

## Operational Impact

Confidence decreases until validation occurs.

---

# 7. STRENGTHENS

## Meaning

One entity increases confidence in another entity.

## Example

Multiple Sensors
strengthen
Flood Warning

Historical Evidence
strengthens
Risk Assessment

## Operational Impact

Higher confidence.

---

# 8. WEAKENS

## Meaning

One entity reduces confidence in another entity.

## Example

Incomplete Data
weakens
Recommendation

Outdated Dataset
weakens
Risk Model

## Operational Impact

Reduced confidence.

---

# 9. CAUSES

## Meaning

One entity directly contributes to another event.

## Example

Heavy Rainfall
causes
Flood Risk

Terminal Congestion
causes
Cargo Delay

Low Depth
causes
Navigation Restriction

## Operational Impact

Used for causal intelligence.

---

# 10. OBSERVES

## Meaning

An entity collects information about another entity.

## Example

Sensor
observes
River Level

Operator
observes
Terminal Congestion

Gauge Station
observes
Water Depth

## Operational Impact

Forms the observation layer.

---

# 11. DERIVED_FROM

## Meaning

An entity originates from another entity.

## Example

Risk Assessment
derived_from
Signals

Signal
derived_from
Observations

Recommendation
derived_from
Risk Assessment

## Operational Impact

Supports explainability and lineage.

---

# 12. VALIDATED_BY

## Meaning

An entity has been verified by another authority.

## Example

Recommendation
validated_by
SVACS

Dataset
validated_by
Data Authority

Decision
validated_by
Operations Team

## Operational Impact

Increases trust.

---

# 13. OWNED_BY

## Meaning

Defines accountability.

## Example

Terminal
owned_by
IWAI

Dataset
owned_by
CWC

Recommendation
owned_by
NICAI

## Operational Impact

Defines governance responsibility.

---

# 14. GENERATED_BY

## Meaning

Identifies origin of information.

## Example

Signal
generated_by
Telemetry Event

Recommendation
generated_by
NICAI

Alert
generated_by
Runtime System

## Operational Impact

Provides provenance.

---

# 15. CONSUMED_BY

## Meaning

Identifies usage destination.

## Example

Recommendation
consumed_by
Operations Command Center

Observation
consumed_by
NICAI

## Operational Impact

Tracks information flow.

---

# 16. SPATIALLY_RELATED

## Meaning

Two entities share geographic relevance.

## Example

Terminal
spatially_related
River Reach

Bridge
spatially_related
Channel

## Operational Impact

Supports geospatial reasoning.

---

# 17. LOCATED_IN

## Meaning

Entity exists within a location.

## Example

Terminal
located_in
Varanasi

Jetty
located_in
River Reach

## Operational Impact

Supports mapping and spatial analysis.

---

# 18. ADJACENT_TO

## Meaning

Two entities are geographically neighboring.

## Example

Terminal A
adjacent_to
Logistics Park B

## Operational Impact

Used for route and corridor planning.

---

# 19. TEMPORALLY_RELATED

## Meaning

Two events share a time relationship.

## Example

Flood Event
temporally_related
Monsoon Season

## Operational Impact

Supports trend analysis.

---

# 20. PRECEDES

## Meaning

One event occurs before another.

## Example

Heavy Rainfall
precedes
Flood Alert

## Operational Impact

Supports prediction.

---

# 21. FOLLOWS

## Meaning

One event occurs after another.

## Example

Recovery Phase
follows
Emergency Phase

## Operational Impact

Supports lifecycle tracking.

---

# 22. ECONOMICALLY_RELATED

## Meaning

Entities influence economic activity.

## Example

Cargo Corridor
economically_related
Trade Zone

Terminal
economically_related
Industrial Cluster

## Operational Impact

Supports economic intelligence.

---

# 23. OPERATIONALLY_RELATED

## Meaning

Entities interact operationally.

## Example

Vessel
operationally_related
Terminal

Cargo
operationally_related
Mission

## Operational Impact

Supports operational planning.

---

# 24. ENVIRONMENTALLY_RELATED

## Meaning

Entities affect environmental conditions.

## Example

Flood Event
environmentally_related
River Reach

Industrial Zone
environmentally_related
Water Quality

## Operational Impact

Supports environmental intelligence.

---

# 25. REGULATORILY_RELATED

## Meaning

Entities are connected through regulations.

## Example

Cargo Route
regulatorily_related
Navigation Rule

Terminal
regulatorily_related
Safety Regulation

## Operational Impact

Supports compliance management.

---

# 26. AUTHORIZED_BY

## Meaning

An action is approved by an authority.

## Example

Decision
authorized_by
Operations Authority

Mission
authorized_by
Command Center

## Operational Impact

Supports governance.

---

# 27. RECOMMENDS

## Meaning

One entity proposes another action.

## Example

NICAI
recommends
Suspend Operations

Risk Engine
recommends
Alternate Route

## Operational Impact

Supports decision generation.

---

# 28. EXECUTED_BY

## Meaning

Action performer.

## Example

Mission
executed_by
Vessel

Decision
executed_by
Operator

## Operational Impact

Supports accountability.

---

# 29. IMPACTS

## Meaning

One entity influences another.

## Example

Flood
impacts
Cargo Operations

Congestion
impacts
Terminal Efficiency

## Operational Impact

Used in consequence analysis.

---

# 30. LEARNS_FROM

## Meaning

Knowledge improvement relationship.

## Example

NICAI
learns_from
Operational Outcomes

Knowledge Repository
learns_from
Replay Analysis

## Operational Impact

Supports continuous improvement.

---

# Relationship Metadata

Every relationship must contain:

* Relationship ID
* Relationship Type
* Source Entity
* Target Entity
* Created Date
* Version
* Confidence
* Evidence Reference
* Authority Owner
* Validation Status

---

# Governance Rules

1. Every relationship must be explicitly defined.
2. No hidden relationships are allowed.
3. Every relationship must be traceable.
4. Every relationship must support replay.
5. Every relationship must support validation.
6. Every relationship must have an owner.
7. Every relationship must be explainable.

---

# Expected Outcome

The Relationship Registry transforms the Marine Intelligence System from a collection of entities into a connected knowledge ecosystem.

It enables:

* Knowledge Graphs
* Reasoning Engines
* Causal Intelligence
* Decision Intelligence
* Validation Frameworks
* Replay Systems
* Explainable Recommendations

Without relationships there is data.

With relationships there is intelligence.
