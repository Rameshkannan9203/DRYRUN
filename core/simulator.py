import json
from core.detector import detect
from core.artifacts import artifacts
from core.risk_score import opsec
from core.nist_score import nist
from core.chains import ATTACK_CHAINS
from core.navigator import export_navigator

def start_ctf():
    with open("knowledge_base/techniques.json", "r") as f:
        techniques = json.load(f)

    while True:
        print("\nSelect Attack Chain:\n")
        chains = list(ATTACK_CHAINS.keys())

        for i, chain in enumerate(chains, 1):
            print(f"{i}. {chain}")
        print(f"{len(chains) + 1}. Exit")

        try:
            choice = int(input("\n> "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        # Exit option
        if choice == len(chains) + 1:
            print("\n[✓] Exiting DRYRUN. Stay safe.")
            break

        if choice < 1 or choice > len(chains):
            print("Invalid option. Try again.")
            continue

        chain_name = chains[choice - 1]
        print(f"\n[+] Executing: {chain_name}\n")

        report = []
        navigator_scores = {}

        for tid in ATTACK_CHAINS[chain_name]:
            if tid not in techniques:
                print(f"[!] Technique {tid} missing in database. Skipping.")
                continue

            tech = techniques[tid]
            detection = detect(tech["binary"])
            event_ids = artifacts(tech["binary"])

            nist_risk = nist(tech["impact"], detection["effectiveness"])
            opsec_level = opsec(detection["effectiveness"])

            navigator_scores[tid] = nist_risk

            entry = {
                "Technique": tid,
                "Binary": tech["binary"],
                "Detection Rule": detection["rule"],
                "Event IDs": event_ids,
                "OPSEC": opsec_level,
                "NIST Risk": nist_risk
            }

            report.append(entry)

            print(f"[+] {tid} | Risk: {nist_risk} | OPSEC: {opsec_level}")

        export_navigator(navigator_scores)
        write_report(report)

def write_report(report):
    with open("output/report.txt", "w") as f:
        for r in report:
            for k, v in r.items():
                f.write(f"{k}: {v}\n")
            f.write("-" * 50 + "\n")

    print("\n[✓] Report saved → output/report.txt")
    print("[✓] MITRE Navigator → output/navigator_layer.json")
