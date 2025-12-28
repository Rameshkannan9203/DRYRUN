def opsec(effectiveness):
    if effectiveness >= 0.8:
        return "HIGH – Very Noisy"
    elif effectiveness >= 0.5:
        return "MEDIUM – Detectable"
    else:
        return "LOW – Stealthy"
