# When Can AI Assess Financial Risk? A Scaling Study

![Emergence Analysis](emergence_analysis.png)

## TL;DR
Risk assessment capabilities emerge sharply around 2.7B parameters. Smaller models (355M) identify obvious risks but fail catastrophically on subtle/systemic risks, creating a dangerous "confident but wrong" zone.

## The Question
At what scale do language models develop reliable financial risk assessment capabilities?

## What I Did
- Created 15 risk scenarios spanning easy (explicit) to hard (systemic) risks
- Tested GPT-2 Medium (355M) vs Phi-2 (2.7B) 
- Measured recall, precision, F1 on identifying ground-truth risks

## Key Finding
**Emergence threshold observed between 355M and 2.7B parameters:**
- GPT-2: Strong on explicit risks (0.65 recall), fails on complex risks (0.12 recall)
- Phi-2: Consistent across difficulties (0.58-0.72 recall)

## Why This Matters for AI Safety
Small models exhibit dangerous behavior: they sound confident while missing critical risks. This has direct implications for deploying AI in high-stakes financial domains.

### Example Failure Case
**Scenario H01** (interest rate risk in CRE lending)
- **GPT-2 response**: Identifies geographic diversification as strength, misses rate shock exposure entirely
- **Phi-2 response**: Correctly identifies rate environment as primary risk

## Implications
1. Minimum scale requirements for financial AI applications
2. Emergence isn't smooth - capability jumps appear suddenly
3. Need for robust evaluation before deployment in high-stakes domains

## Next Steps
- Test fine-tuning impact on emergence thresholds
- Human evaluation of explanation quality
- Expand to medical/legal domains

## Repository
- `scenarios.py` - 15 hand-crafted test cases
- `evaluation.py` - Metrics framework
- `*_results.json` - Raw experimental data
- `analyze.py` - Analysis code

---
