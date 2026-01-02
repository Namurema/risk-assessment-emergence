# scenarios.py

scenarios = [
    # === EASY (5) ===
    {
        "id": "E01",
        "category": "credit_risk",
        "difficulty": "easy",
        "scenario": "StartupX has $500K in the bank with monthly burn of $200K. No revenue. Fundraising typically takes 6 months.",
        "ground_truth_risks": [
            {"risk": "runway depletion", "severity": "high"},
            {"risk": "no revenue", "severity": "high"}
        ]
    },
    {
        "id": "E02", 
        "category": "fraud",
        "difficulty": "easy",
        "scenario": "Company reports $10.0M revenue Q1, $10.0M Q2, $10.0M Q3, $10.0M Q4. All invoices dated last day of quarter. CEO previously involved in accounting scandal.",
        "ground_truth_risks": [
            {"risk": "revenue manipulation", "severity": "high"},
            {"risk": "suspicious timing", "severity": "high"}
        ]
    },
    {
        "id": "E03",
        "category": "credit_risk", 
        "difficulty": "easy",
        "scenario": "E-commerce company gets 85% of revenue from top 2 customers. Both customers are in struggling retail sector.",
        "ground_truth_risks": [
            {"risk": "customer concentration", "severity": "high"},
            {"risk": "sector risk", "severity": "medium"}
        ]
    },
    {
        "id": "E04",
        "category": "market_risk",
        "difficulty": "easy", 
        "scenario": "Hedge fund portfolio: 95% tech stocks, 3x leverage, average correlation 0.85 in normal times, spikes to 0.98 during selloffs.",
        "ground_truth_risks": [
            {"risk": "concentration risk", "severity": "high"},
            {"risk": "leverage amplification", "severity": "high"}
        ]
    },
    {
        "id": "E05",
        "category": "operational_risk",
        "difficulty": "easy",
        "scenario": "Manufacturing company sources 90% of critical components from single supplier in geopolitically unstable region. No alternative suppliers identified.",
        "ground_truth_risks": [
            {"risk": "supplier concentration", "severity": "high"},
            {"risk": "geopolitical exposure", "severity": "high"}
        ]
    },
    
    # === MEDIUM (5) ===
    {
        "id": "M01",
        "category": "credit_risk",
        "difficulty": "medium",
        "scenario": "SaaS company: $5M ARR growing 100% YoY. Gross margin declining from 75% to 68% to 61% over 3 quarters. Customer acquisition cost up 40%. Net revenue retention 95%.",
        "ground_truth_risks": [
            {"risk": "deteriorating unit economics", "severity": "high"},
            {"risk": "rising CAC unsustainable", "severity": "medium"}
        ]
    },
    {
        "id": "M02",
        "category": "fraud",
        "difficulty": "medium",
        "scenario": "Real estate company books $50M land sale to EntityX. EntityX owned by CEO's brother. Sale price 3x recent comparable transactions. Payment terms: 5 years, zero interest.",
        "ground_truth_risks": [
            {"risk": "related party transaction", "severity": "high"},
            {"risk": "suspicious valuation", "severity": "high"}
        ]
    },
    {
        "id": "M03",
        "category": "market_risk",
        "difficulty": "medium",
        "scenario": "Investment fund holds mortgage-backed securities rated AAA. Securities perform well in stress tests assuming 10% home price decline. Housing market currently up 45% in 3 years, historical average is 3% annually.",
        "ground_truth_risks": [
            {"risk": "inadequate stress testing", "severity": "high"},
            {"risk": "asset bubble exposure", "severity": "medium"}
        ]
    },
    {
        "id": "M04",
        "category": "credit_risk",
        "difficulty": "medium",
        "scenario": "Fintech lender: loan book grew 300% last year. Default rate stable at 2%. Average loan vintage is 8 months. Industry standard seasoning period before defaults appear is 18-24 months.",
        "ground_truth_risks": [
            {"risk": "immature loan book", "severity": "high"},
            {"risk": "hidden credit deterioration", "severity": "high"}
        ]
    },
    {
        "id": "M05",
        "category": "operational_risk",
        "difficulty": "medium",
        "scenario": "Biotech company: 100% revenue from single drug. Patent expires in 14 months. Generic competition expected immediately. Pipeline has 2 Phase I trials, typical success rate 10%. Burn rate $30M/year, cash $50M.",
        "ground_truth_risks": [
            {"risk": "patent cliff", "severity": "high"},
            {"risk": "pipeline inadequacy", "severity": "high"}
        ]
    },
    
    # === HARD (5) ===
    {
        "id": "H01",
        "category": "systemic_risk",
        "difficulty": "hard",
        "scenario": "Bank primarily lends to commercial real estate. Portfolio well-diversified geographically. Interest rate environment: rates at historic lows for 8 years, central bank signaling tightening cycle. CRE valuations based on current cap rates. Loan-to-value ratios at origination averaged 70%.",
        "ground_truth_risks": [
            {"risk": "rate shock exposure", "severity": "high"},
            {"risk": "valuation assumption breakdown", "severity": "high"}
        ]
    },
    {
        "id": "H02",
        "category": "fraud",
        "difficulty": "hard",
        "scenario": "Payment processor reports steady 25% revenue growth for 4 years. Customer count growing 5% annually. Revenue per customer growing 19% annually. Industry benchmark: revenue per customer growing 3-5% annually. Company doesn't disclose merchant category breakdown.",
        "ground_truth_risks": [
            {"risk": "revenue quality concerns", "severity": "medium"},
            {"risk": "possible channel stuffing", "severity": "medium"}
        ]
    },
    {
        "id": "H03",
        "category": "regulatory_risk",
        "difficulty": "hard",
        "scenario": "Cryptocurrency exchange generates 60% revenue from retail trading. Business model relies on regulatory arbitrage - operates in jurisdictions with light oversight. Recent global coordination among financial regulators increasing. Major economies drafting comprehensive crypto regulations.",
        "ground_truth_risks": [
            {"risk": "regulatory arbitrage closure", "severity": "high"},
            {"risk": "business model obsolescence", "severity": "high"}
        ]
    },
    {
        "id": "H04",
        "category": "market_risk",
        "difficulty": "hard",
        "scenario": "Pension fund maintains 60/40 stock/bond portfolio. Historical correlation between stocks and bonds: -0.3. Recent 2 years: correlation shifted to +0.5. Fund assumes traditional negative correlation for risk models. Interest rates rising, inflation elevated.",
        "ground_truth_risks": [
            {"risk": "correlation regime change", "severity": "high"},
            {"risk": "diversification failure", "severity": "high"}
        ]
    },
    {
        "id": "H05",
        "category": "strategic_risk",
        "difficulty": "hard",
        "scenario": "Auto parts manufacturer has thrived supplying internal combustion engine components. 90% revenue from ICE parts. EV adoption accelerating faster than industry forecasts. Company R&D spend: 2% of revenue vs industry 5%. Management states 'EVs are a niche market'.",
        "ground_truth_risks": [
            {"risk": "technological disruption", "severity": "high"},
            {"risk": "strategic denial", "severity": "high"}
        ]
    }
]