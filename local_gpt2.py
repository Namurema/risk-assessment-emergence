from transformers import AutoModelForCausalLM, AutoTokenizer
import json
from evaluation import evaluate_response
from prompts import create_risk_assessment_prompt
from scenarios import scenarios

print("Loading GPT-2 Medium...")
model_name = "gpt2-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

print("✓ Model loaded! Starting evaluation...")

results = []

for i, scenario in enumerate(scenarios):
    print(f"\n[{i+1}/15] Testing {scenario['id']} - {scenario['difficulty']}")
    
    prompt = create_risk_assessment_prompt(scenario['scenario'])
    inputs = tokenizer(prompt, return_tensors="pt")
    
    outputs = model.generate(
        **inputs,
        max_new_tokens=400,
        temperature=0.1,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id
    )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = response[len(prompt):].strip()
    
    metrics = evaluate_response(response, scenario)
    
    result = {
        'model': 'gpt2-medium',
        'scenario_id': scenario['id'],
        'difficulty': scenario['difficulty'],
        'response': response,
        'metrics': metrics
    }
    results.append(result)
    
    print(f"✓ Recall: {metrics['recall']:.2f}, F1: {metrics['f1_score']:.2f}")

with open('gpt2_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print("\n✓ Done! Results saved to gpt2_results.json")