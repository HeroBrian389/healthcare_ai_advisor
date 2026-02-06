# Theatre utilisation & cancellations — pilot taster

Audience: CEO / Ops / Clinical leadership

Status: draft (shareable)

## Executive summary

Theatre time is expensive and constrained. A large share of cancellations are predictable *early enough* to intervene.

This pilot proposes a 4–6 week, safety‑first AI deployment focused on:

- earlier visibility into cancellation risk,
- structured reasons and bottlenecks,
- workflow changes that reduce avoidable cancellations.

Default posture: no patient notes; rely on operational metadata and scheduling signals.

## What we’ll do (4–6 weeks)

1. Map the workflow (booking → pre-op → day-of-surgery)
2. Identify the top cancellation drivers and where interventions are feasible
3. Implement a small AI-supported workflow (e.g., risk flagging + reason capture + escalation)
4. Run in shadow/assisted mode and measure outcomes

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontFamily": "Karla", "primaryColor": "#F4F3F0", "primaryTextColor": "#2B2D32", "primaryBorderColor": "#D4D3D0", "lineColor": "#3E4048", "secondaryColor": "#E8F0ED", "tertiaryColor": "#EAEAE6"}}}%%
gantt
    title 4–6 week pilot (illustrative)
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b

    section Discovery
    Workflow mapping & baseline: done, a1, 2026-02-10, 5d
    Guardrails & access plan: a2, after a1, 3d

    section Build
    Prototype + integration stub: b1, after a2, 10d

    section Evaluate
    Shadow mode + metrics: c1, after b1, 10d
    Recommendations + next steps: c2, after c1, 3d
```

## What data we need (default)

- Theatre schedule (procedure type/category, session, specialty)
- Booking timestamps + changes
- Operational status changes (confirmed, pending, cancelled)
- Structured cancellation reasons (if available)
- Staffing / capacity constraints (coarse)

## Deliverables

- A short “current state” map + bottleneck analysis
- A prioritised intervention list (what changes *actually* reduce cancellations)
- A small prototype/workflow (UI and/or reporting) to support earlier interventions
- Evaluation plan + measured pilot results

## Success metrics (examples)

- Reduction in same-day cancellations
- Reduction in avoidable cancellations
- Increased theatre utilisation (or fewer overruns)
- Staff time saved in coordination/admin

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontFamily": "Karla", "primaryColor": "#F4F3F0", "primaryTextColor": "#2B2D32", "primaryBorderColor": "#D4D3D0", "lineColor": "#3E4048", "secondaryColor": "#E8F0ED", "tertiaryColor": "#EAEAE6"}}}%%
xychart-beta
    title "Cancellations per week (illustrative)"
    x-axis ["Baseline", "After pilot"]
    y-axis "Cancellations" 0 --> 30
    bar [24, 16]
```

## Safety & governance posture

- Not diagnostic decision support
- Human-in-the-loop: AI suggests/flags; staff decide
- Data minimisation by default
- Access controls + audit logs for any deployment
- Clear “do not use” boundaries (e.g., no clinical advice)

## Why this is a good first pilot

- Operationally meaningful and measurable
- Low risk (no notes by default)
- Generates reusable capability (data mapping, evaluation, governance) for later clinical projects
