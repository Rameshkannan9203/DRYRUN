ATTACK_CHAINS = {
    "Initial Access": ["T1059"],
    "Lateral Movement": ["T1047"],
    "Exfiltration": ["T1041"],

    "Active Directory Attack Path": [
        "T1558",   # Kerberoasting
        "T1003",   # Credential Dumping
        "T1550",   # Pass-the-Hash
        "T1484"    # Domain Policy Modification
    ],

    "Cloud Attack Path": [
        "T1078",   # Valid Accounts
        "T1098",   # Account Manipulation
        "T1528",   # Steal Application Access Token
        "T1567"    # Exfiltration to Cloud Storage
    ]
}
