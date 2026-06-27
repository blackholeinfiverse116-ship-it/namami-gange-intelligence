# MARINE ONTOLOGY SPECIFICATION

## Document Information

Project: NICAI Marine Intelligence System

Version: 1.0

Status: Architecture Design

Owner: Marine Intelligence Team

Purpose:

Define the canonical ontology used by NICAI to understand relationships, dependencies, operational meaning and reasoning across the Marine Intelligence ecosystem.

---

# 1. Objective

The Marine Ontology provides the semantic foundation for Marine Intelligence.

The Knowledge Graph defines entities.

The Ontology defines what relationships mean.

Without ontology:

River → Terminal

has no intelligence value.

With ontology:

River Reach
supports
Navigation Corridor

Navigation Corridor
enables
Cargo Movement

Cargo Movement
strengthens
Terminal Utilization

Terminal Utilization
supports
Economic Activity

Economic Activity
increases
Operational Importance

Now the system can reason.

---

# 2. Ontology Principles

All relationships must:

* Have meaning
* Be deterministic
* Be explainable
* Be traceable
* Support reasoning
* Support validation
* Support replay

No relationship may exist without semantic meaning.

---

# 3. Relationship Categories

The Marine Ontology contains six major relationship groups.

1. Structural Relationships
2. Operational Relationships
3. Spatial Relationships
4. Temporal Relationships
5. Governance Relationships
6. Intelligence Relationships

---

# 4. Structural Relationships

Structural relationships define physical composition.

---

## contains

Meaning:

Parent entity physically contains child entity.

Examples:

River
contains
River Reach

River Reach
contains
Channel

Terminal
contains
Jetty

---

## belongs_to

Meaning:

Entity is part of a larger entity.

Examples:

Station
belongs_to
River Reach

Channel
belongs_to
River

Cargo
belongs_to
Commodity Group

---

## connected_to

Meaning:

Direct connection exists.

Examples:

Terminal
connected_to
Logistics Park

Jetty
connected_to
Terminal

Bridge
connected_to
Road Network

---

## intersects

Meaning:

Entities physically intersect.

Examples:

Bridge
intersects
River

Corridor
intersects
Administrative Region

---

# 5. Operational Relationships

Operational relationships define operational behavior.

---

## supports

Meaning:

Entity positively contributes to another.

Examples:

Terminal
supports
Cargo Operations

River Reach
supports
Navigation

Logistics Park
supports
Distribution

---

## enables

Meaning:

Entity makes an activity possible.

Examples:

Navigable Channel
enables
Vessel Movement

Cargo Corridor
enables
Trade Flow

Terminal Capacity
enables
Cargo Handling

---

## depends_on

Meaning:

Entity requires another entity.

Examples:

Mission
depends_on
Vessel

Navigation
depends_on
Water Depth

Recommendation
depends_on
Evidence

---

## constrains

Meaning:

Entity limits another entity.

Examples:

Flood Event
constrains
Navigation

Low Water Depth
constrains
Cargo Movement

Weather Alert
constrains
Operations

---

## blocks

Meaning:

Entity prevents execution.

Examples:

Closed Terminal
blocks
Cargo Operations

Emergency Zone
blocks
Mission Execution

---

## impacts

Meaning:

Entity affects performance.

Examples:

Congestion
impacts
Terminal Efficiency

Weather
impacts
Vessel Operations

---

# 6. Intelligence Relationships

These relationships are used during reasoning.

---

## strengthens

Meaning:

Evidence increases confidence.

Examples:

Terminal Capacity
strengthens
Cargo Recommendation

High Water Depth
strengthens
Navigation Assessment

---

## weakens

Meaning:

Evidence reduces confidence.

Examples:

Poor Water Quality
weakens
Seaplane Suitability

Flood Risk
weakens
Operational Recommendation

---

## causes

Meaning:

Direct causal influence.

Examples:

Heavy Rainfall
causes
Flood Event

Flood Event
causes
Navigation Restriction

---

## contributes_to

Meaning:

One factor partially influences another.

Examples:

Tourism Demand
contributes_to
Passenger Traffic

Economic Growth
contributes_to
Cargo Growth

---

## derived_from

Meaning:

Entity originates from source evidence.

Examples:

Risk
derived_from
Observations

Recommendation
derived_from
Assessment

---

## validated_by

Meaning:

Entity verified by authority.

Examples:

Recommendation
validated_by
SVACS

Risk Assessment
validated_by
Authority

---

## contradicts

Meaning:

Evidence conflicts with another.

Examples:

Sensor Reading A
contradicts
Sensor Reading B

Forecast
contradicts
Observed Conditions

---

## confirms

Meaning:

Evidence agrees with another.

Examples:

Telemetry
confirms
Manual Inspection

Gauge Reading
confirms
Hydrological Assessment

---

# 7. Spatial Relationships

Spatial relationships define geography.

---

## upstream_of

Meaning:

Entity exists upstream.

Examples:

Prayagraj
upstream_of
Varanasi

Varanasi
upstream_of
Patna

---

## downstream_of

Meaning:

Entity exists downstream.

Examples:

Patna
downstream_of
Varanasi

Kolkata
downstream_of
Patna

---

## adjacent_to

Meaning:

Located nearby.

Examples:

Terminal
adjacent_to
Logistics Park

River Reach
adjacent_to
Protected Area

---

## located_in

Meaning:

Geographic placement.

Examples:

Terminal
located_in
River Reach

Station
located_in
Administrative Region

---

## crosses

Meaning:

Physical crossing.

Examples:

Bridge
crosses
River

Road Corridor
crosses
Flood Zone

---

# 8. Temporal Relationships

Temporal relationships define time.

---

## before

Meaning:

Occurs earlier.

Examples:

Flood Alert
before
Flood Event

---

## after

Meaning:

Occurs later.

Examples:

Recovery Phase
after
Emergency Phase

---

## during

Meaning:

Occurs within same period.

Examples:

Cargo Delay
during
Flood Event

---

## recurring_with

Meaning:

Repeats seasonally.

Examples:

Monsoon Flooding
recurring_with
Monsoon Season

---

## triggered_by

Meaning:

Time-linked activation.

Examples:

Restriction
triggered_by
Water Level Threshold

---

# 9. Governance Relationships

Governance relationships define ownership.

---

## owned_by

Meaning:

Authority ownership.

Examples:

Terminal
owned_by
IWAI

Gauge Station
owned_by
CWC

---

## regulated_by

Meaning:

Governed by regulation.

Examples:

Cargo Movement
regulated_by
Maritime Policy

---

## approved_by

Meaning:

Requires authorization.

Examples:

Mission
approved_by
Authority

---

## monitored_by

Meaning:

Observed by authority.

Examples:

River Reach
monitored_by
CWC

Water Quality
monitored_by
CPCB

---

# 10. Economic Relationships

---

## supplies

Meaning:

Provides resources.

Examples:

Terminal
supplies
Cargo Network

---

## serves

Meaning:

Supports stakeholders.

Examples:

Port
serves
Trade Region

---

## generates

Meaning:

Produces outcome.

Examples:

Cargo Corridor
generates
Economic Activity

---

## consumes

Meaning:

Uses resources.

Examples:

Vessel
consumes
Fuel

Mission
consumes
Capacity

---

# 11. Environmental Relationships

---

## affects_ecology

Meaning:

Environmental influence.

Examples:

Industrial Activity
affects_ecology
River System

---

## protected_by

Meaning:

Environmental protection.

Examples:

Wetland
protected_by
Environmental Regulation

---

## environmentally_related

Meaning:

Environmental association.

Examples:

Protected Area
environmentally_related
River Reach

---

# 12. Authority Registry

Relationship Governance:

| Relationship | Authority            |
| ------------ | -------------------- |
| supports     | NICAI                |
| enables      | NICAI                |
| depends_on   | NICAI                |
| constrains   | NICAI                |
| causes       | NICAI                |
| validated_by | SVACS                |
| owned_by     | Source Authority     |
| regulated_by | Governance Authority |

---

# 13. Reasoning Example

Observation:

Water Level Decreasing

↓

Signal:

Reduced Navigability

↓

Relationship:

Water Level
constrains
Navigation

↓

Impact:

Navigation
weakens
Cargo Operations

↓

Risk:

Cargo Delay Risk

↓

Recommendation:

Reduce Vessel Draft

↓

Validation:

SVACS Validation

↓

Decision:

Operational Advisory Issued

Every step remains explainable.

---

# 14. Ontology Governance

Ontology changes require:

* Version Update
* Authority Approval
* Relationship Review
* Impact Assessment
* Validation Testing

No uncontrolled ontology changes are permitted.

---

# 15. Success Criteria

The Marine Ontology is successful when the system can answer:

Why was this recommendation generated?

by traversing meaningful relationships rather than static rules.

Every recommendation must be traceable through:

Observation
↓
Signal
↓
Relationship
↓
Context
↓
Risk
↓
Recommendation
↓
Validation
↓
Decision

with complete explainability and governance.
