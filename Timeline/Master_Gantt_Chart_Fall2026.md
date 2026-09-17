# Project Schedule: Automated Drink-Dispensing Table (Fall 2026)

Course: Senior Design Capstone (MECH5051 / EECE5001) & CEAS Innovation Challenge  
Project: 8-Bottle Mobile Dispensing Table on Wheels  
Team: Rohendhar (Lead), Aron Joseph, Eli Radabaugh, Shyam Patel  

---

## 1. Master Project Schedule

```
Weeks (Fall 2026)              | W1 (8/27) | W2 (9/02) | W3 (9/09) | W4 (9/16) | W5 (9/23) | W6 (9/30) | W7 (10/07) | W8 (10/14) | W9 (10/21) | W10 (10/28) | W11 (11/04) | W12 (11/11) | W13 (11/18) | W14 (11/25) | W15 (12/01) |
-------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+------------+------------+------------+-------------+-------------+-------------+-------------+-------------+-------------+
Phase 1: Planning & Design     |           |           |           |           |           |           |            |            |            |             |             |             |             |             |             |
- Kickoff and team setup       | [=======] | [=======] |           |           |           |           |            |            |            |             |             |             |             |             |             |
- Finalize 8-bottle layout     |           |           | [=======] |           |           |           |            |            |            |             |             |             |             |             |             |
- Sponsor doc to Jacob Cress   |           |           | [=======] | [===X]    |           |           |            |            |            |             |             |             |             |             |             |
- Part quotes and CAD layouts  |           |           |           | [=======] | [======X] |           |            |            |            |             |             |             |             |             |             |
- Team Proposal (Sept 23)      |           |           |           |           |    [X]    |           |            |            |            |             |             |             |             |             |             |
- 5-Minute Pitch Video (Sept 28)|          |           |           |           | [=======] | [==X]     |            |            |            |             |             |             |             |             |             |
- Draft Proposal (Oct 2)       |           |           |           |           |           |    [X]    |            |            |            |             |             |             |             |             |             |
- Preliminary Design Review    |           |           |           |           |           |           |    [X]     |            |            |             |             |             |             |             |             |
-------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+------------+------------+------------+-------------+-------------+-------------+-------------+-------------+-------------+
Phase 2: Part Testing & Builds |           |           |           |           |           |           |            |            |            |             |             |             |             |             |             |
- Parts pre-approval forms     |           |           |           | [=======] | [=======] | [=======] |            |            |            |             |             |             |             |             |             |
- Test PLC and power supply    |           |           |           |           |           |           | [========] | [========] |            |             |             |             |             |             |             |
- Test cup lift motor and rail |           |           |           |           |           |           | [========] | [========] | [========] |             |             |             |             |             |             |
- Test 8 pumps and tubing      |           |           |           |           |           |           |            | [========] | [========] | [=========] |             |             |             |             |             |
- Test cold bay and ice cubes  |           |           |           |           |           |           |            |            | [========] | [=========] |             |             |             |             |             |
- Prototype Day demo (Nov 4)   |           |           |           |           |           |           |            |            |            |             |    [X]      |             |             |             |             |
-------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+------------+------------+------------+-------------+-------------+-------------+-------------+-------------+-------------+
Phase 3: Assembly & Final Event|           |           |           |           |           |           |            |            |            |             |             |             |             |             |             |
- Assemble table and wheels    |           |           |           |           |           |           |            |            |            | [=========] | [=========] | [=========] |             |             |             |
- Wire upper electrical panel  |           |           |           |           |           |           |            |            |            |             | [=========] | [=========] |             |             |             |
- Full system drink tests      |           |           |           |           |           |           |            |            |            |             |             | [=========] | [=======X]  |             |             |
- Final Competition (Nov 18)   |           |           |           |           |           |           |            |            |            |             |             |             |    [X]      |             |             |
- Course Review for Cress      |           |           |           |           |           |           |            |            |            |             |             |             |             |             |    [X]      |
-------------------------------+-----------+-----------+-----------+-----------+-----------+-----------+------------+------------+------------+-------------+-------------+-------------+-------------+-------------+-------------+
[X] = Critical deadline or submission date
```

---

## 2. Key Deadlines and Milestones

| Milestone | Due Date | Lead Person | Deliverable and Notes |
| :--- | :--- | :--- | :--- |
| **Team Lead / Sponsor Document** | Tue, Sept 15, 2026 | Rohendhar | Introductory scope document submitted to Jacob Cress. |
| **Team Design Proposal** | Wed, Sept 23, 2026 | All Leads | Itemized quotes and CAD drawing per section (**Critical**). |
| **5-Minute Pitch Video** | Mon, Sept 28, 2026 | Full Team | Video submission. Unlocks **$600 upfront payment** to buy parts. |
| **Senior Design Draft Proposal** | Fri, Oct 2, 2026 | Rohendhar & Shyam | Draft proposal submission for course grading. |
| **Preliminary Design Review (PDR)** | Mon, Oct 5, 2026 | All Leads | Formal presentation evaluating system design feasibility. |
| **Innovation Challenge Prototype Day** | Wed, Nov 4, 2026 | Eli & Shyam | Live in-person benchtop rig demonstration for judges. |
| **Final Competition and Gala** | Wed, Nov 18, 2026 | Full Team | Final demo. Unlocks **$600 second stipend** plus bonus awards. |
| **Senior Design Final Review** | Tue, Dec 1, 2026 | Full Team | Final course presentation and review with Jacob Cress. |

---

## 3. Team Roles and Technical Duties

### Eli Radabaugh — Electrical Lead & Cup Lift Co-Lead
* Email: radabaer@mail.uc.edu
* Primary Responsibility: Controls, power supply, relays, wiring safety, and limit switches.
* Hardware Specifications:
  - Controller: Click PLC (AutomationDirect) or Siemens LOGO!
  - Power Supply: Mean Well 24V DC (14.6A) power supply
  - Protection: 1N4007 flyback diodes across pump motors; relay isolation board
  - Limit Switches: Optical endstop switches for top and bottom stops
  - Enclosure: Water-resistant box mounted high on the rear panel
* Proposal Deliverable (Due Sept 23): Complete electrical price quotes (PLC, power supply, relays) and single-line wiring diagram.

### Aron Joseph — Finance Lead & Bottling Co-Lead
* Email: josepha7@mail.uc.edu
* Primary Responsibility: Budget tracking, purchase requests, 8 bottles, pumps, and valves.
* Hardware Specifications:
  - Purchase Rule: Submit Canvas purchase request form and receive approval before buying
  - Budget: Use the $600 video pitch payout (Sept 28) as active budget for prototype parts
  - Bottles: 8 flat-bottom glass or PET bottles (500ml-750ml, matching height)
  - Tubing: Food-grade silicone tubing (1/4 inch inner diameter)
  - Flow Control: Adjustable screw pinch valves to balance pouring speed
* Proposal Deliverable (Due Sept 23): Price quotes for 8 bottles, tubing, and valves, plus master purchase request draft.

### Shyam Patel — Operations Lead, Cup Lift & Cooling
* Email: patel8s7@mail.uc.edu
* Primary Responsibility: Master Gantt schedule, cup lift guide rail, motor carriage, and cooling.
* Hardware Specifications:
  - Schedule: Keep master project schedule updated weekly
  - Linear Rail: MGN12H guide rail (350mm-400mm) with long carriage block to prevent cup tipping
  - Lift Screw: 8mm lead screw with NEMA 17 stepper motor (lead screw prevents platform drop on power loss)
  - Cooling: Reusable stainless steel ice cubes in insulated compartment
  - Insulation: Closed-cell foam to prevent water condensation near electronics
* Proposal Deliverable (Due Sept 23): Updated Gantt schedule and CAD layout drawing for the lift mechanism.

### Rohendhar — Project Lead, Systems & Bottling Co-Lead
* Email: rohendrr@mail.uc.edu
* Primary Responsibility: Project coordination, teacher communications, dispensing nozzle head, check valves, and state machine.
* Hardware Specifications:
  - Course Contact: Sponsor and lead document for Jacob Cress
  - Dispenser Head: 3D-printed nozzle head angling all 8 tubes inward to pour into standard cups
  - Bottle Valves: Duckbill silicone valves in corks so air enters as liquid is pumped out
  - Machine Steps: Cup Detected -> Lower Platform -> Pump Drink -> Raise Flush -> Complete
  - Video: Coordinate 5-minute video pitch recording due Sept 28 ($600 team payout)
* Proposal Deliverable (Due Sept 23): Sponsor document for Jacob Cress and CAD drawing of the 8-nozzle dispenser head.

---

## 4. Innovation Challenge Funding and Reimbursement Rules

| Funding Stage | Amount per Student | Team Total (4 Students) | Details and Timing |
| :--- | :--- | :--- | :--- |
| **Pitch Video (Sept 28)** | $150.00 each | $600.00 Total | Paid upon video submission. Used as budget to buy prototype parts. |
| **Prototype Day & Final (Nov 18)** | $150.00 each | $600.00 Total | Paid for showing prototype (Nov 4) and attending Final (Nov 18). |
| **Guaranteed Grant Total** | $300.00 each | $1,200.00 Total | Guaranteed payout for finishing all three requirements. |
| **Top 25% Placement Award** | $300.00 each | $1,200.00 Total | Bonus award if the team places in the top 25% with judges. |
| **Podium Awards (1st - 3rd)** | Up to $700.00 each | Up to $2,800.00 Total | Bonus cash prizes for top three team finishes. |
| **100% Parts Reimbursement** | 100% of receipts | Full Coverage | Covers parts, hardware, fasteners, and 1819 Makerspace costs. |

### Mandatory Reimbursement Rules
1. **Pre-Approval Required**: Submit the Canvas purchase request form and get approval before buying any parts.
2. **Itemized Receipts**: Receipts must show store name, purchase date, item list, unit prices, and sales tax. Gift cards are not allowed.
3. **Covered Expenses**: Hardware parts, raw materials, fasteners, electronics, tubing, and 1819 Makerspace fees.
4. **Not Covered**: Software subscriptions, personal food, alcohol, and general retail goods.
5. **Payment Timing**: Reimbursement checks will be distributed by the Tribunal after the November 18th Final Competition.
