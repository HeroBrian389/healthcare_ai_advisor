# Bon Secours Hospital Dublin — nursing documentation & admin burden (pilot taster)

Audience: Director of Nursing / Quality & Patient Safety

Status: draft (shareable)

## Executive summary

Nursing time is the scarcest resource in a hospital.

This pilot proposes a 4–6 week, safety‑first AI deployment focused on reducing administrative friction without introducing unsafe clinical automation.

Default posture: start with templates, structured inputs, and admin support — not autonomous clinical advice.

## Why Bon Secours Dublin (context)

Bon Secours Hospital Dublin (Glasnevin) is a planned-care private hospital. HIQA describes it as an elective adult-only acute general hospital with 90 inpatient beds and 70 day care beds. That environment tends to amplify the impact of admin friction (handover, documentation, discharge processes, clinic coordination) because throughput and coordination quality show up quickly in patient experience and operational performance.

## What we’ll do (4–6 weeks)

1. Map one documentation/admin workflow end-to-end (choose one ward/unit)
2. Identify where time is being lost (duplication, searching, handoffs)
3. Deploy a small AI-supported workflow (assisted mode)
4. Measure time saved, error reduction, and user adoption

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontFamily": "Karla", "primaryColor": "#F4F3F0", "primaryTextColor": "#2B2D32", "primaryBorderColor": "#D4D3D0", "lineColor": "#3E4048", "secondaryColor": "#E8F0ED", "tertiaryColor": "#EAEAE6"}}}%%
flowchart TB
  A[Shift starts] --> B[Tasks + patient list]
  B --> C[Notes / documentation]
  C --> D[Handover]
  D --> E[Downstream admin]

  subgraph AI_support_assisted
    S1[Summarise structured status]
    S2[Draft non-clinical text]
    S3[Find relevant policy/template]
  end

  C -.-> S1
  C -.-> S2
  C -.-> S3
```

## What data we need (default)

- Documentation templates and policies
- Non-sensitive workflow artefacts (forms, checklists)
- Optional: de-identified example notes for formatting only (if explicitly agreed)

## Deliverables

- Workflow map + pain-point analysis
- Guardrails (“what the tool can/can’t do”)
- Prototype (template assist / checklist assist / policy lookup)
- Evaluation plan + measured pilot results

## Success metrics (examples)

- Time saved per shift on admin/documentation
- Reduced duplication or missing fields
- Higher staff satisfaction / adoption
- Fewer rework loops in handover

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontFamily": "Karla", "primaryColor": "#F4F3F0", "primaryTextColor": "#2B2D32", "primaryBorderColor": "#D4D3D0", "lineColor": "#3E4048", "secondaryColor": "#E8F0ED", "tertiaryColor": "#EAEAE6"}}}%%
xychart-beta
    title "Admin time per shift (illustrative)"
    x-axis ["Baseline", "After pilot"]
    y-axis "Minutes" 0 --> 180
    bar [120, 90]
```

## Safety & governance posture

- Not a clinical decision-maker
- Human-in-the-loop always
- Access controls + audit logs
- Clear boundaries + escalation paths

## Why this is a good first pilot

- Directly protects clinical capacity
- Low-risk when scoped correctly
- Builds trust in governance and evaluation
