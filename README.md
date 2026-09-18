# Automated Drink-Dispensing Table — Senior Design Project

**Course**: MECH5051 / EECE5001 Senior Design  
**Institution**: University of Cincinnati  
**Project Lead / Documentation & AI**: Ro  
**Current Phase**: 🔬 **Phase 1: Ideation & Concept Exploration** *(Main design is NOT finalized)*  

> [!WARNING]
> **PRELIMINARY ESTIMATE / DRAFT DOCUMENT — NOWHERE NEAR FINAL**  
> All specifications, architecture options, cost estimates, funding targets, and timelines in this document reflect early brainstorming. None of the designs, budgets, or implementations are finalized and all elements remain subject to substantial revision.

## 🌐 Interactive Team Web Hub (Live Jarvis Chat)
> [!TIP]
> **High-Speed Live AI Assistant Link**: [**https://estimated-stem-schemes-suffered.trycloudflare.com**](https://estimated-stem-schemes-suffered.trycloudflare.com)  
> *Teammates can open this link from anywhere to check tasks, deadlines, inspect budget/BOM numbers, and chat with J.A.R.V.I.S. with sub-second response times!*

---

## 📌 1. Project Overview
An automated drink-dispensing table that seamlessly blends mechanical automation, fluidics, electronics, and smart AI interaction into an aesthetically crafted furniture piece.

### Core User Workflow:
1. **Cup Placement / Retrieval**: Mechanism lowers the cup into the table housing.
2. **Dispensing**: Precision fluidic system pours single or mixed drink recipes from integrated reservoirs.
3. **Cup Elevating**: Elevator lifts the filled cup smoothly to the table surface for pickup.
4. **Visual Display**: Clear acrylic/open-sided enclosure showcases internal mechanics for senior design presentations.

---

## 👥 2. Team & Responsibilities

| Team Member | Role & Core Responsibilities | Email / Contact | Focus Areas |
| :--- | :--- | :--- | :--- |
| **Ro** | **Documentation, Minutes & AI Integration** | `rohendrr@mail.uc.edu` | Formal reports, design journals, meeting logs, AI product features (voice/smart recommendation/vision), agent workflows |
| **Aron** | **Procurement, Finance & Budgeting** | `josepha7@mail.uc.edu` | Budget management, expense tracking, parts sourcing, receipt logging, Innovation Challenge funding |
| **Eli** | **Inventory & Resource Management** | `radabaer@mail.uc.edu` | Parts tracking, lab resource management, parts storage & staging |
| **Shyam** | **Time Management & Scheduling** | `patel8s7@mail.uc.edu` | Milestone tracking, due dates, Gantt charts, sprint timelines |

---

## 🤖 3. Project Subagent Ecosystem
All subagents work in tandem and pair directly with team member leads. See full [Subagent Directory & Document Routing Matrix](file:///c:/Users/rohen/Videos/Senior%20Design/Organization/subagent_roster_and_routing_matrix.md).

| Subagent | Team Counterpart | Primary Scope & Responsibilities |
| :--- | :--- | :--- |
| **`engineering_subagent`** | **Ro & Team** | Mechanical design, fluidics calculations, electronics schematics, firmware/C++, CAD models, trade studies. |
| **`budgeting_subagent`** | **Aron** | Master budget tracking, expense logs, receipt auditing, vendor quotes, grant budget narratives. |
| **`inventory_subagent`** | **Eli** | Hardware cataloging, physical storage tracking (Eli's location), datasheets, lead times. |
| **`task_manager_subagent`** | **Shyam** | Milestone scheduling, Mermaid Gantt charts, sprint backlogs, meeting action items. |
| **`funding_and_grants_agent`** | **Aron & Ro** | UC Innovation Challenge, 1819 Venture Lab, Main Street Ventures, Cincinnati startup grants. |
| **`project_reminder_agent`** | **Ro** | Automated reminders, deadline notifications, team email digests via [`Tools/reminders/send_reminder.py`](file:///c:/Users/rohen/Videos/Senior%20Design/Tools/reminders/send_reminder.py). |

---

## 📊 4. Key Constraints & Targets

- **Budget**: Initial prototype estimated at **~$300**; total build target under **$1,000**.
- **Funding**: Pursuing the **Innovation Challenge** (~$300/person) + department grants.
- **Meeting Cadence**: 2x per week, ~3 hours per session (In-person standard; remote for docs).
- **Fabrication Resources**: 3D Printing (FDM/resin), UC Welding Lab, Machine Shop, CAD/FEA simulation tools.

---

## 📂 5. Project Repository Structure

```text
Senior Design/
├── README.md                                      <-- Project Hub & Dashboard (This File)
├── Meeting Notes/
│   ├── 2026-08-27_Kickoff_Meeting_Minutes.docx   <-- Formal Word Document
│   └── 2026-08-27_Kickoff_Meeting_Minutes.md     <-- Markdown Notes & Action Items
├── Architecture/
│   ├── system_overview.md                        <-- Subsystem breakdown (Mech, Fluid, Elec, AI)
│   └── design_concepts_and_trade_study.md        <-- Trade Studies & Competing Concepts (Ideation)
├── Business/
│   └── commercialization_and_market_strategy.md  <-- B2B Vending, QR Ordering & Cincinnati Brewery Fit
├── Funding/
│   └── funding_and_grants_guide.md               <-- UC & Cincinnati Grant Opportunities Guide
├── Budget/
│   └── procurement_and_funding.md                <-- Expense log, BOM & Sourcing Tracker
├── Organization/
│   ├── subagent_roster_and_routing_matrix.md     <-- Subagent mapping & doc ingestion rules
│   └── Project_Rules.md                          <-- Project phase status & standards
├── Research/
│   └── ai_and_features.md                        <-- AI integration ideas (voice, CV, recommendations)
├── Timeline/
│   └── milestones.md                             <-- Schedule, Gantt data, deadlines
└── Tools/
    ├── sync_google_drive.py                      <-- 2-Way Google Drive synchronization engine
    └── reminders/                                <-- Automated reminder bot & team contact roster
```

---

## 🛠️ 6. Agent Capabilities for this Project
As your AI Project Agent, I am configured to:
1. **Track Action Items & Status**: Maintain logs from every team meeting.
2. **Generate Engineering Specs**: BOMs, pinout diagrams, state machines, and wiring schematics.
3. **Produce Formal Reports**: Capstone project proposals, PDR/CDR design reviews, user manuals.
4. **Develop Embedded & AI Code**: Python/C++ code for Raspberry Pi/microcontrollers, voice APIs, computer vision, and GUI.
