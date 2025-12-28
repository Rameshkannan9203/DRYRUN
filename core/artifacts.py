import json

def artifacts(binary):
    with open("knowledge_base/windows_events.json", "r") as f:
        events = json.load(f)

    return events.get(binary, ["Unknown Event"])
