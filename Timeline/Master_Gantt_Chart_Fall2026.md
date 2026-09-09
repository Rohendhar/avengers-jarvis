# AVENGERS Automated Drink-Dispensing Table — Master Gantt Chart (Fall 2026)

**Semester**: Fall 2026 (MECH5051 / EECE5001 & CEAS Innovation Challenge)  
**Target Delivery**: Automated 8-Bottle Mobile Dispensing Table on Wheels (`30" × 17" × 10"`)  
**Project Lead**: Ro | **Finance Lead**: Aron | **Electrical Lead**: Eli | **Operations/Gantt Lead**: Shyam  

---

## 📊 1. High-Level Master Visual Gantt Chart

```
WEEKS (FALL 2026)             | W1 (8/27) | W2 (9/02) | W3 (9/09) | W4 (9/16) | W5 (9/23) | W6 (9/30) | W7 (10/07) | W8 (10/14) | W9 (10/21) | W10 (10/28) | W11 (11/04) | W12 (11/11) | W13 (11/18) | W14 (11/25) | W15 (12/01) |
=============================================================================================================================================================================================================================
PHASE 1: DESIGN & PROPOSAL    |           |           |           |           |           |           |            |            |            |             |             |             |             |             |             |
• Kickoff & Scope Alignment   | [=======] | [=======] |           |           |           |           |            |            |            |             |             |             |             |             |             |
• 8-Bottle Scope Freeze       |           |           | [=======] |           |           |           |            |            |            |             |             |             |             |             |             |
• Sponsor/Lead Doc (Sept 15)  |           |           | [=======] | [===★]    |           |           |            |            |            |             |             |             |             |             |             |
• Section Quotes & CAD Layouts|           |           |           | [=======] | [======★] |           |            |            |            |             |             |             |             |             |             |
• Team Proposal (Sept 23)     |           |           |           |           |    [★]    |           |            |            |            |             |             |             |             |             |             |
• 5-Min Video Pitch (Sept 28) |           |           |           |           | [=======] | [==★]     |            |            |            |             |             |             |             |             |             |
• Draft Proposal (Oct 2)      |           |           |           |           |           |    [★]    |            |            |            |             |             |             |             |             |             |
• Preliminary Review (Oct 5)  |           |           |           |           |           |           |    [★]     |            |            |             |             |             |             |             |             |
------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+------------+------------+------------+-------------+-------------+-------------+-------------+-------------+-------------+
PHASE 2: SUBSYSTEM BENCH RIGS |           |           |           |           |           |           |            |            |            |             |             |             |             |             |             |
• Purchase Pre-Approval Forms |           |           |           | [=======] | [=======] | [=======] |            |            |            |             |             |             |             |             |             |
• Electrical & PLC Bench Test |           |           |           |           |           |           | [========] | [========] |            |             |             |             |             |             |             |
• Z-Axis Linear Rail Rig      |           |           |           |           |           |           | [========] | [========] | [========] |             |             |             |             |             |             |
• 8-Pump Dosing Manifold Test |           |           |           |           |           |           |            | [========] | [========] | [=========] |             |             |             |             |             |
• Ice & Thermal Integration   |           |           |           |           |           |           |            |            | [========] | [=========] |             |             |             |             |             |
• Prototype Day (Nov 4)       |           |           |           |           |           |           |            |            |            |             |    [★]      |             |             |             |             |
------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+------------+------------+------------+-------------+-------------+-------------+-------------+-------------+-------------+
PHASE 3: INTEGRATION & COMPETITION        |           |           |           |           |           |            |            |            |             |             |             |             |             |             |
• Mobile Table Framing        |           |           |           |           |           |           |            |            |            | [=========] | [=========] | [=========] |             |             |             |
• High Bulkhead Wiring        |           |           |           |           |           |           |            |            |            |             | [=========] | [=========] |             |             |             |
• Full System Dry/Wet Tests   |           |           |           |           |           |           |            |            |            |             |             | [=========] | [=======★]  |             |             |
• IC Final Competition (11/18)|           |           |           |           |           |           |            |            |            |             |             |             |    [★]      |             |             |
• Course Review for Cress     |           |           |           |           |           |           |            |            |            |             |             |             |             |             |    [★]      |
=============================================================================================================================================================================================================================
[★] = Critical Milestone Deadline / Payout Gate
```

---

## 📅 2. Critical Milestones & Financial Payout Gates

| # | Milestone Name | Exact Due Date | Primary Owner | Deliverable & Financial Impact |
| :-: | :--- | :---: | :---: | :--- |
| **M1** | **Team Lead / Sponsor 101 Doc** | **Tue, Sept 15, 2026** | **Ro** (All) | Introductory scope & sponsor alignment to Prof. Jacob Cress. |
| **M2** | **Team Design Proposal** | **Wed, Sept 23, 2026** | **All Leads** | Itemized BOM vendor quotes + visual CAD layout per section (**CRITICAL**). |
| **M3** | **5-Minute Pitch Deck Video** | **Mon, Sept 28, 2026** | **Team** | Unlocks **$600.00 upfront team payout** ($150/person) for prototype capital! |
| **M4** | **Senior Design Draft Proposal** | **Fri, Oct 2, 2026** | **Ro & Shyam** | Formal capstone course draft submission for Jacob Cress. |
| **M5** | **Preliminary Design Review (PDR)** | **Mon, Oct 5, 2026** | **All Members** | Formal course milestone evaluating subsystem feasibility. |
| **M6** | **Innovation Challenge Prototype Day**| **Wed, Nov 4, 2026** | **Eli & Shyam** | Live in-person benchtop rig demonstration for IC judges and mentors. |
| **M7** | **Final Competition & Gala** | **Wed, Nov 18, 2026** | **All Members** | Unlocks **$600.00 second stipend** ($1,200 guaranteed grant) + **$1,200 Top 25% bonus** + podium prizes + **100% material reimbursements**. |
| **M8** | **Senior Design Fall Course Review** | **Tue, Dec 1, 2026** | **All Members** | Formal end-of-semester defense and grading review with Professor Cress. |

---

## 👥 3. Work Breakdown Structure (WBS) & Technical Roles

### ⚡ Subsystem 1: Electrical & Controls
- **Lead**: **Eli Radabaugh** | **Support**: **Ro**
- **Core Scope**: Industrial PLC specification, 24V DC switching power supply, optocoupled relay modules, high-wall spill-proof electrical enclosure, emergency stop circuitry.
- **Key Tasks**:
  1. *Sept 9 – Sept 23*: Select PLC model (e.g. AutomationDirect Click PLC C0-00DD1-D or Siemens LOGO! 24RCE) and prepare BOM quote.
  2. *Sept 9 – Sept 23*: Size 24V DC power supply (10A–15A, Mean Well LRS-350-24) to drive PLC, relays, and pumps simultaneously.
  3. *Sept 23 – Oct 15*: Draft ladder logic state machine (Homing -> Idle -> Cup Drop -> Timed Dosing -> Cup Raise -> Complete).
  4. *Oct 15 – Nov 4*: Assemble high-bulkhead DIN rail box and bench test relays under pump inductive loads.

---

### 🛗 Subsystem 2: Lift Mechanism
- **Co-Leads**: **Shyam Patel** & **Eli Radabaugh**
- **Core Scope**: Precision Z-axis linear guide rail, stepper motor, drive transmission (lead screw vs. closed-loop timing belt), upper/lower optical limit switches, fixed cup platform.
- **Key Tasks**:
  1. *Sept 9 – Sept 23*: Size linear rail (MGN12H / 300mm–400mm) and select stepper motor (NEMA 17 0.45Nm holding torque).
  2. *Sept 9 – Sept 23*: Produce CAD layout drawing showing cup carriage travel and table flush alignment.
  3. *Sept 23 – Oct 15*: Build physical bench test rig for vertical motion repeatability and zero-backlash cup positioning.
  4. *Oct 15 – Nov 4*: Wire upper and lower Normally Closed (NC) limit switches to PLC digital inputs.

---

### 🍾 Subsystem 3: Bottling & Fluidics
- **Co-Leads**: **Ro** & **Aron Joseph**
- **Core Scope**: 8 custom flat-bottom bottles (2x4 array: 4 juice, 4 alcohol), food-grade silicone tubing (1/4" ID), peristaltic dosing pumps, duckbill anti-vacuum cork valves, inline flow regulators.
- **Key Tasks**:
  1. *Sept 9 – Sept 23*: Select uniform flat-bottom bottles (500ml–750ml) and rubber cork closures with vented check valves.
  2. *Sept 9 – Sept 23*: Source 8x 12V DC food-grade peristaltic pumps and inline flow regulators to meter flow and prevent splashing.
  3. *Sept 23 – Oct 15*: Design and 3D-print converging dispensing nozzle manifold (centers all 8 streams into 3.5" cup diameter).
  4. *Oct 15 – Nov 4*: Calibrate pump dispense timing (volumetric calibration ±5% across varying viscosities).

---

### ❄️ Subsystem 4: Ice & Thermal Management
- **Co-Leads**: **Shyam Patel** & **Eli Radabaugh**
- **Core Scope**: Trade study evaluating reusable food-grade 304 stainless steel ice cubes vs. compact thermoelectric (Peltier) cold plate.
- **Key Tasks**:
  1. *Sept 9 – Sept 23*: Complete thermal trade study and select baseline (motorized ice machines permanently ruled out).
  2. *Sept 23 – Oct 15*: Design insulated ice bay / cold chute utilizing closed-cell neoprene insulation to prevent condensation near electrical bay.

---

### 💰 Subsystem 5: Finance, Procurement & Canvas Management
- **Lead**: **Aron Joseph**
- **Core Scope**: Innovation Challenge Purchase Request Excel pre-approvals, itemized receipt tracking, budget variance modeling, working capital allocation.
- **Key Tasks**:
  1. *Sept 9 – Sept 23*: Establish Master Purchase Request Excel sheet matching Innovation Challenge rules (no gift cards, itemized quotes).
  2. *Sept 28 – Oct 5*: Collect and manage the upfront **$600.00 pitch deck video payout** as working capital for prototype components.
  3. *Nov 18*: Submit final reimbursement packet to 1819 Innovation Chair for 100% material payback.

---

## ⏰ 4. Meeting Cadence & Communication Protocol
- **Standing In-Person Meetings**: **Twice Weekly** — immediately **BEFORE (12:45 PM)** and **AFTER (2:45 PM)** Wednesday 1:30 PM class.
- **Real-Time J.A.R.V.I.S. Core**: Live 24/7 at [**https://avengers-jarvis.onrender.com**](https://avengers-jarvis.onrender.com)
- **Document Mirror**: Live on Google Drive at `G:\My Drive\Senior Design`.
