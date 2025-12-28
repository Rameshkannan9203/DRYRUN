import json

def export_navigator(data):
    layer = {
        "version": "4.5",
        "name": "DRYRUN Attack Simulation",
        "techniques": []
    }

    for tid, score in data.items():
        layer["techniques"].append({
            "techniqueID": tid,
            "score": score
        })

    with open("output/navigator_layer.json", "w") as f:
        json.dump(layer, f, indent=4)
