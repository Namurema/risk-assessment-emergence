import re
from typing import List, Dict

def parse_model_response(response_text: str) -> List[Dict]:
    """Extract risks from model output"""
    risks = []
    # Simple regex parsing - adjust based on actual outputs
    risk_pattern = r"Risk \d+: (.+?)\nSeverity: (\w+)\nExplanation: (.+?)(?=\nRisk|\Z)"
    matches = re.findall(risk_pattern, response_text, re.DOTALL)
    
    for match in matches:
        risks.append({
            'name': match[0].strip(),
            'severity': match[1].strip().lower(),
            'explanation': match[2].strip()
        })
    return risks

def calculate_recall(predicted_risks, ground_truth_risks):
    """How many real risks did the model catch?"""
    # Simple keyword matching for now
    gt_keywords = [r['risk'].lower() for r in ground_truth_risks]
    pred_text = ' '.join([r['name'].lower() for r in predicted_risks])
    
    caught = sum(1 for keyword in gt_keywords if keyword in pred_text)
    return caught / len(gt_keywords) if gt_keywords else 0

def calculate_precision(predicted_risks, ground_truth_risks):
    """How many predicted risks are real?"""
    # Basic implementation - can be refined
    if not predicted_risks:
        return 0
    
    gt_keywords = [r['risk'].lower() for r in ground_truth_risks]
    valid_predictions = sum(
        1 for pred in predicted_risks 
        if any(keyword in pred['name'].lower() for keyword in gt_keywords)
    )
    return valid_predictions / len(predicted_risks)

def evaluate_response(model_output, ground_truth):
    """Full evaluation"""
    parsed_risks = parse_model_response(model_output)
    
    recall = calculate_recall(parsed_risks, ground_truth['ground_truth_risks'])
    precision = calculate_precision(parsed_risks, ground_truth['ground_truth_risks'])
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return {
        'recall': recall,
        'precision': precision,
        'f1_score': f1,
        'num_risks_identified': len(parsed_risks),
        'parsed_risks': parsed_risks
    }