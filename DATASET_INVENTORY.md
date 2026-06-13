# DATASET INVENTORY

## Overview

This inventory documents the datasets currently available for the Namami Gange Geospatial Intelligence Demonstration. These datasets are used to generate location-level intelligence, opportunity assessments, constraint assessments, suitability scoring, and explainable dashboard outputs.

---
 
# Dataset 1: urban_centers_ganga_basin

## Source
Urban Centers Dataset (Namami Gange Internal)

## Purpose
Urban demand and connectivity assessment.

## Coverage
Major urban centers across the Ganga Basin.

## Update Frequency
Periodic

## Fields Available

- city_name
- population_est_2023_lakhs
- has_airport
- has_railway_jn
- has_highway_access
- economic_importance

## Data Quality
High

## Current Usage
Urban demand analysis and connectivity assessment.

## Demo Suitability
High

## Intelligence Contribution

Used for:

- Demand scoring
- Connectivity scoring
- Economic importance assessment
- Opportunity identification

---

# Dataset 2: logistics_parks_ganga_belt

## Source
Logistics Infrastructure Dataset

## Purpose
Assessment of logistics and intermodal opportunities.

## Coverage
Logistics parks and freight infrastructure across the Ganga Belt.

## Update Frequency
Periodic

## Fields Available

- park_name
- location
- park_type
- status
- road_connectivity
- rail_connectivity
- waterway_connectivity

## Data Quality
Medium to High

## Current Usage
Freight and logistics infrastructure assessment.

## Demo Suitability
High

## Intelligence Contribution

Used for:

- Logistics opportunity assessment
- Cargo opportunity assessment
- Intermodal connectivity assessment

---

# Dataset 3: iwai_terminals_nw1

## Source
Inland Waterways Authority of India (IWAI)

## Purpose
Assessment of inland waterway infrastructure.

## Coverage
National Waterway-1 (NW-1)

## Update Frequency
Periodic

## Fields Available

- terminal_name
- terminal_type
- capacity_mtpa
- operational_status
- connectivity

## Data Quality
High

## Current Usage
Waterway infrastructure analysis.

## Demo Suitability
High

## Intelligence Contribution

Used for:

- Infrastructure scoring
- Cargo opportunity assessment
- Waterway readiness assessment

---

# Dataset 4: cpcb_water_quality_ganga

## Source
Central Pollution Control Board (CPCB)

## Purpose
Water quality assessment.

## Coverage
Monitoring stations across the Ganga Basin.

## Update Frequency
Periodic

## Fields Available

- station_name
- river_name
- do_mg_l
- bod_mg_l
- ph
- turbidity
- pollution_class

## Data Quality
High

## Current Usage
Environmental monitoring.

## Demo Suitability
High

## Intelligence Contribution

Used for:

- Environmental assessment
- Ecological constraints
- Water quality scoring

---

# Dataset 5: cwc_river_stations_ganga

## Source
Central Water Commission (CWC)

## Purpose
River condition and navigation assessment.

## Coverage
River monitoring stations across the Ganga Basin.

## Update Frequency
Periodic

## Fields Available

- station_name
- navigability_depth_m
- flood_prone
- flow_stability_index
- water_level_variation_m
- discharge

## Data Quality
High

## Current Usage
Navigation and hydrological assessment.

## Demo Suitability
High

## Intelligence Contribution

Used for:

- Navigation suitability scoring
- Flood risk assessment
- Seasonal variability assessment
- Operational reasoning generation

---

# Dataset Summary

| Dataset | Primary Function | Demo Suitability |
|----------|----------|----------|
| urban_centers_ganga_basin | Demand & Connectivity | High |
| logistics_parks_ganga_belt | Logistics Opportunities | High |
| iwai_terminals_nw1 | Infrastructure Assessment | High |
| cpcb_water_quality_ganga | Environmental Assessment | High |
| cwc_river_stations_ganga | Navigation Assessment | High |

---

# Dataset Readiness

Status: Ready

All five datasets provide sufficient coverage to generate explainable location intelligence for:

- Varanasi
- Patna
- Prayagraj
- Kanpur
- Kolkata

These datasets collectively support:

- Suitability Scoring
- Opportunity Intelligence
- Constraint Intelligence
- Explainable Dashboard Outputs
- Demo Intelligence Payload Generation
