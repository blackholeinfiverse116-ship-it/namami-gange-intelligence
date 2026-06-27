# ENTITY REGISTRY

## Purpose

The Entity Registry is the canonical catalogue of all entities used by the Marine Intelligence System.

Every intelligence output, recommendation, decision, risk assessment, validation result and operational action must be traceable to one or more registered entities.

The registry ensures:

* Common understanding across all systems
* Consistent naming
* Traceability
* Governance
* Explainability
* Interoperability

This registry is governed by the Marine Data Unit (MDU).

---

# Entity Classification Framework

Entities are grouped into the following categories:

1. Geographic Entities
2. Waterway Entities
3. Infrastructure Entities
4. Vessel Entities
5. Cargo Entities
6. Environmental Entities
7. Operational Entities
8. Intelligence Entities
9. Governance Entities
10. System Entities

---

# 1. Geographic Entities

## River

### Description

Represents a named river system.

### Examples

* Ganga
* Yamuna
* Brahmaputra

### Owner

Marine MasterDB

### Lifecycle

Active
→ Monitored
→ Restricted
→ Recovery
→ Active

### Traceability

River ID

---

## River Reach

### Description

A defined segment of a river.

### Examples

* NW-1 Reach 001
* Varanasi Reach

### Owner

Marine MasterDB

### Traceability

Reach ID

---

## Administrative Region

### Description

Government administrative area.

### Examples

* Uttar Pradesh
* Bihar
* West Bengal

### Owner

Government Records

### Traceability

Region ID

---

## Economic Zone

### Description

Area used for economic activity analysis.

### Examples

* Logistics Cluster
* Trade Zone

### Owner

Planning Authority

### Traceability

Economic Zone ID

---

## Protected Area

### Description

Environmentally protected region.

### Examples

* Wildlife Sanctuary
* Conservation Zone

### Owner

Environmental Authority

### Traceability

Protected Area ID

---

# 2. Waterway Entities

## Channel

### Description

Navigable water path.

### Attributes

* Width
* Depth
* Flow Characteristics

### Owner

IWAI

### Traceability

Channel ID

---

## Gauge Station

### Description

Station used to measure river conditions.

### Attributes

* Water Level
* Flow Rate
* Depth

### Owner

CWC

### Traceability

Gauge ID

---

## Water Body

### Description

Any navigable water area.

### Examples

* River
* Lake
* Reservoir

### Traceability

Water Body ID

---

# 3. Infrastructure Entities

## Terminal

### Description

Cargo or passenger handling facility.

### Examples

* Varanasi Terminal
* Patna Terminal

### Owner

IWAI

### Lifecycle

Planned
→ Construction
→ Operational
→ Restricted
→ Maintenance
→ Operational

### Traceability

Terminal ID

---

## Jetty

### Description

Small vessel docking facility.

### Owner

Local Authority

### Traceability

Jetty ID

---

## Port

### Description

Large-scale cargo and passenger facility.

### Owner

Port Authority

### Traceability

Port ID

---

## Logistics Park

### Description

Cargo aggregation and distribution facility.

### Owner

Logistics Authority

### Traceability

Logistics Park ID

---

## Bridge

### Description

Infrastructure crossing over waterways.

### Owner

Infrastructure Authority

### Traceability

Bridge ID

---

# 4. Vessel Entities

## Vessel

### Description

Waterborne transport unit.

### Types

* Cargo Vessel
* Passenger Vessel
* Patrol Vessel
* Seaplane Support Vessel

### Lifecycle

Registered
→ Active
→ Maintenance
→ Active
→ Retired

### Traceability

Vessel ID

---

## Crew

### Description

Personnel operating vessels.

### Traceability

Crew ID

---

# 5. Cargo Entities

## Cargo

### Description

Goods transported through waterways.

### Examples

* Coal
* Containers
* Fertilizer
* Cement

### Traceability

Cargo ID

---

## Commodity

### Description

Classification of cargo.

### Traceability

Commodity ID

---

## Cargo Corridor

### Description

Origin-destination trade route.

### Traceability

Corridor ID

---

# 6. Environmental Entities

## Weather Cell

### Description

Weather system affecting operations.

### Examples

* Storm Cell
* Rain Band

### Traceability

Weather Cell ID

---

## Flood Event

### Description

Flood occurrence impacting operations.

### Lifecycle

Detected
→ Watch
→ Warning
→ Active
→ Recovery
→ Closed

### Traceability

Flood Event ID

---

## Environmental Zone

### Description

Ecological management region.

### Traceability

Environmental Zone ID

---

# 7. Operational Entities

## Mission

### Description

Operational objective.

### Examples

* Cargo Movement
* Passenger Service
* Emergency Response

### Traceability

Mission ID

---

## Incident

### Description

Unexpected operational event.

### Examples

* Collision
* Navigation Failure
* Flood Disruption

### Traceability

Incident ID

---

## Inspection

### Description

Operational assessment activity.

### Traceability

Inspection ID

---

## Maintenance Activity

### Description

Infrastructure or vessel servicing activity.

### Traceability

Maintenance ID

---

# 8. Intelligence Entities

## Observation

### Description

Raw operational fact.

### Examples

* Water level increased
* Terminal congestion detected

### Traceability

Observation ID

---

## Signal

### Description

Processed operational indication.

### Traceability

Signal ID

---

## Evidence

### Description

Supporting information used for reasoning.

### Traceability

Evidence ID

---

## Risk

### Description

Potential adverse outcome.

### Examples

* Flood Risk
* Navigation Risk

### Traceability

Risk ID

---

## Constraint

### Description

Operational limitation.

### Examples

* Low Water Depth
* Restricted Channel

### Traceability

Constraint ID

---

## Opportunity

### Description

Potential operational advantage.

### Examples

* Cargo Expansion
* Tourism Growth

### Traceability

Opportunity ID

---

## Recommendation

### Description

Suggested operational action.

### Traceability

Recommendation ID

---

## Decision

### Description

Approved operational action.

### Traceability

Decision ID

---

## Validation Record

### Description

Verification of intelligence outputs.

### Traceability

Validation ID

---

# 9. Governance Entities

## Regulation

### Description

Formal operational rule.

### Traceability

Regulation ID

---

## Restriction

### Description

Temporary operational limitation.

### Traceability

Restriction ID

---

## Authority

### Description

Responsible governing organization.

### Examples

* IWAI
* CWC
* CPCB
* Port Authority

### Traceability

Authority ID

---

# 10. System Entities

## Sensor

### Description

Device generating observations.

### Traceability

Sensor ID

---

## Telemetry Event

### Description

Machine-generated operational event.

### Examples

* Water Level Update
* Vessel Position Update

### Traceability

Telemetry Event ID

---

## Replay Record

### Description

Stored operational history for replay.

### Traceability

Replay ID

---

## Knowledge Record

### Description

Persisted intelligence knowledge.

### Traceability

Knowledge Record ID

---

# Mandatory Entity Metadata

Every entity in the Marine Intelligence ecosystem must contain:

* Entity ID
* Entity Type
* Name
* Description
* Owner
* Authority
* Current State
* Version
* Created Date
* Updated Date
* Relationships
* Traceability Reference

No entity may exist without complete metadata.

---

# Governance Rules

1. Every entity must have a unique identifier.
2. Every entity must have a responsible owner.
3. Every entity must support traceability.
4. Every entity must support version control.
5. Every entity must participate in the ontology model.
6. Every entity must be auditable.
7. Every entity must support replay and provenance tracking.

---

# Expected Outcome

The Entity Registry acts as the foundational catalogue of the Marine Intelligence ecosystem.

All knowledge graphs, reasoning engines, recommendation systems, validation frameworks and decision engines depend on this registry to maintain consistency, traceability and governance across the platform.
