def create_risk_assessment_prompt(scenario_text):
    return f"""You are a financial risk analyst. Analyze the following situation and identify the top 3 risks.

Scenario:
{scenario_text}

For each risk, provide:
1. Risk name
2. Severity (high/medium/low)
3. Brief explanation (1-2 sentences)

Format your response as:
Risk 1: [name]
Severity: [level]
Explanation: [reasoning]

Risk 2: ...
"""

# Keep prompt simple and consistent across all models