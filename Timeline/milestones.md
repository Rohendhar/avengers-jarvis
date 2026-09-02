# Project Timeline & Milestone Tracking

> [!WARNING]
> **PRELIMINARY ESTIMATE / DRAFT TIMELINE — NOWHERE NEAR FINAL**  
> All milestone dates, Gantt durations, and sprint phase allocations are ballpark estimates to guide early planning and will be adjusted as university course dates and design deadlines are officially published.

**Lead**: Shyam (Time Management & Gantt Charts)  
**Semester Timeline**: Fall 2026 – Spring 2027 (Senior Design Cycle)  

---

## 🎯 1. Major Milestone Schedule

```mermaid
gantt
    title Automated Drink-Dispensing Table Roadmap
    dateFormat  YYYY-MM-DD
    section Phase 1: Conceptual & Sourcing
    Kickoff & Requirements Gathering       :done,    des1, 2026-08-27, 2026-09-07
    Innovation Challenge First Meeting    :done,    ic1,  2026-09-02, 1d
    1819 Makerspace Hands-On Tour         :         ic_tour, 2026-09-20, 2026-09-26
    IC 5-Min Video Pitch ($150 Stipend)   :crit,    ic_vid, 2026-09-15, 2026-09-30
    Component Sourcing & Bench Testing    :         des3, 2026-09-10, 2026-10-01
    Preliminary Design Review (PDR)       :milestone, m1, 2026-10-05, 0d

    section Phase 2: Subsystem Prototyping
    CAD Modeling & Frame Design           :         sub1, 2026-10-01, 2026-10-25
    Elevator & Linear Motion Test Rig     :         sub2, 2026-10-15, 2026-11-10
    Pump & Fluid Flow Calibration         :         sub3, 2026-10-20, 2026-11-15
    IC Prototype Showcase Day             :crit,    ic_proto, 2026-11-04, 1d
    IC Final Gala & Competition           :crit,    ic_final, 2026-11-18, 1d
    Critical Design Review (CDR)          :milestone, m2, 2026-11-25, 0d

    section Phase 3: Integration & Table Build
    Frame Fabrication & Welding           :         int1, 2026-11-15, 2026-12-15
    Electronics Packaging & Wiring        :         int2, 2026-12-01, 2027-01-15
    UI & AI Feature Integration           :         int3, 2027-01-10, 2027-02-15

    section Phase 4: Testing, Polish & Expo
    System Validation & Spill Tests       :         tst1, 2027-02-15, 2027-03-15
    Acrylic Polish & Demo Aesthetic       :         tst2, 2027-03-01, 2027-03-30
    Senior Design Expo Presentation       :milestone, m3, 2027-04-15, 0d
```

---

### Immediate Action Items & Course Sign-Offs (Week of Sept 2, 2026)
- [x] **Ro**: Offload Jarvis AI Assistant to 24/7 public server (Render cloud deployment complete).
- [x] **Ro**: Fix Jarvis link so URL remains permanent (`https://avengers-jarvis.onrender.com`).
- [x] **All Members**: Attend CEAS Innovation Challenge Kickoff Meeting (Sept 2 @ 5:30 PM, Kautz Attic).
- [ ] **All Members**: Submit Innovation Challenge registration form via Teams.
- [ ] **All Members**: Join the Innovation Challenge Canvas course.
- [ ] **All Members**: Complete Student-Initiated Project Document (Due: **Tonight, Sept 2**).
- [ ] **Ro & Team**: Obtain Professor Jacob Cress sign-off and course approval.
- [ ] **All Members**: Finalize & submit neutral project description (*"a device or system that will automatically pour a user-influenced beverage from a selection of available drink options"*).
- [ ] **Eli**: Create component inventory checklist and upload to Google Drive (Target: **Sept 4**).
- [ ] **Aron**: Set up Purchase Request Excel for 1819 Makerspace material reimbursement.
- [ ] **Team**: Record and submit 5-Minute Pitch Deck Video (Due: **September 30, 2026** — unlocks $150 stipend).

### Milestone 1: PDR & Benchtop Proof-of-Concept (Target: Oct 2026)
- [ ] Requirements document finalized (speed, cup capacity, power draw).
- [ ] Innovation Challenge submission completed.
- [ ] Benchtop test: Single pump dosing calibrated volume (±5% accuracy).
- [ ] Benchtop test: Stepper motor moving carriage vertically with limit switches.

### Milestone 2: CDR & Integrated Alpha Prototype (Target: Dec 2026)
- [ ] Complete SolidWorks/Fusion 360 table CAD model and FEA.
- [ ] Full 4-pump dispensing manifold assembled and tested.
- [ ] Microcontroller state machine handling full sequence (Drop -> Fill -> Raise).
- [ ] Initial web/touchscreen UI operational.

### Milestone 3: Final Expo System & Senior Design Expo (Target: April 2027)
- [ ] Table furniture housing completely assembled with clear viewing acrylic.
- [ ] Integrated AI drink recommendation / voice commands active.
- [ ] Final Capstone Report, Poster, and Video Presentation.
