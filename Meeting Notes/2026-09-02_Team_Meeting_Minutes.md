# Automated Drink Dispenser — Project Team Meeting Minutes

**Date:** Wednesday, September 2, 2026  
**Time:** 4:00 PM – 4:45 PM EDT  
**Location:** University of Cincinnati / Microsoft Teams  
**Attendees:** Ro (Lead / AI Integration), Aron (Procurement & Finance), Eli (Inventory & Hardware), Shyam (Timeline & Scheduling)  
**Document Owner:** Ro (Lead)

---

## 1. Executive Summary
The team convened to solidify the project scope, technical constraints, venue market strategy, and upcoming course/grant submissions ahead of the CEAS Innovation Challenge. Key consensus points include refining the target demographic to craft breweries and cigar lounges (novelty/convenience rather than bartender replacement), capping the initial proof-of-concept to 3–4 non-carbonated beverages, adopting a mini-fridge table integration approach for cooling, and raising the total project budget cap from $1,000 to $1,500. Ro reported that J.A.R.V.I.S. has been successfully offloaded to a permanent, 24/7 cloud server on Render (`https://avengers-jarvis.onrender.com`), resolving laptop uptime and changing link issues.

---

## 2. Action Items & Deliverables

| Assignee | Action Item / Deliverable | Deadline | Status |
| :--- | :--- | :--- | :--- |
| **All Team Members** | Submit Innovation Challenge registration form via Teams | **Today (Sept 2)** | 🟡 In Progress |
| **All Team Members** | Complete and submit Student-Initiated Project Document | **Tonight (Sept 2)** | 🟡 In Progress |
| **Ro & Team** | Obtain Professor Jacob Cress sign-off & project approval | **This Week** | 🟡 Pending |
| **All Team Members** | Finalize & submit neutral project description | **Tonight (Sept 2)** | 🟡 Final Draft Ready |
| **Eli** | Create component inventory checklist & upload to Google Drive | **Friday, Sept 4** | 🟡 In Progress |
| **Ro** | Offload Jarvis to public cloud server (eliminate laptop dependency) | **Today (Sept 2)** | ✅ **COMPLETED (Render 24/7)** |
| **Ro** | Fix Jarvis link so URL remains permanent across reboots | **Today (Sept 2)** | ✅ **COMPLETED (`avengers-jarvis.onrender.com`)** |

---

## 3. Project Concept & Use Case Refinement
- **Target Market / Venue**: Fancy/high-end hospitality environments—specifically **craft breweries and cigar lounges** rather than high-volume traditional nightclubs.
- **Value Proposition**: A high-tech novelty and table-side convenience amenity, **not** a direct replacement for professional bartenders.
- **Brewery Synergy**: Brewery patrons prioritize relaxed table socialization and predictable pours rather than fast-paced custom mixology.
- **Rollout Strategy**: Single-table prototype validation ➔ gather user telemetry and venue patron feedback ➔ multi-table commercial cluster.
- **Academic & Pitch Framing**: The project must use **neutral, inclusive terminology** (e.g., *"user-influenced automated beverage dispensing system / custom mocktail & craft dispenser"*) to avoid administrative friction regarding alcohol references during university grant evaluations.

---

## 4. Technical Architecture & Constraints
- **Phase 1 Proof-of-Concept Scope**: Strictly validate core fluidics and mechanics using **3 to 4 non-carbonated drinks** (e.g., juices, water, syrups, still mixers).
- **Carbonation Policy**: Carbonated fluids introduce pressure differentials and foam management complexity; carbonation is formally **deferred to Phase 2**.
- **Thermal Management & Cooling**:
  - *Dedicated Ice Machine*: Evaluated and rejected due to excessive bulk, drainage logistics, and external water line plumbing constraints.
  - *Plan B (Selected)*: Structural table shell built directly around a modified **compact thermoelectric or compressor mini-fridge**, providing thermal insulation and chilled beverage reservoirs without plumbing dependencies.
- **Stretch Goals**: Automated cup drop mechanism, internal ice dispenser, and integrated can ejector.

---

## 5. Budget, Grants & Funding Strategy
- **Budget Ceiling Adjustment**: The team approved expanding the formal project budget ceiling from **$1,000 to ~$1,500** to accommodate commercial-grade tubing, food-safe peristaltic pumps, structural framing, and the internal cooling unit.
- **CEAS Innovation Challenge**:
  - Weekly sessions every Wednesday.
  - Funding awards: **$700 for 1st place**, **$300 participation grant**.
- **1819 Venture Lab & Startup Weekend**:
  - A fully functional physical prototype will serve as a massive competitive differentiator against software-only or slide-only teams at Startup Weekend.

---

## 6. J.A.R.V.I.S. AI Integration Status
- **Cloud Migration**: J.A.R.V.I.S. has been deployed live to **Render** at **`https://avengers-jarvis.onrender.com`**.
- **24/7 Availability**: The bot runs independently of Ro's local laptop, eliminating previous restart and dynamic URL constraints.
- **Workspace Sync**: J.A.R.V.I.S. continuously monitors Google Drive documents, syncs team tasks, and dispatches automated schedule alerts.
