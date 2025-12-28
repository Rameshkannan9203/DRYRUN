import json

def detect(binary):
    with open("knowledge_base/edr_rules.json", "r") as f:
        rules = json.load(f)

    if binary in rules:
        return rules[binary]

    return {
        "rule": "No Detection Rule",
        "effectiveness": 0.1
    }
