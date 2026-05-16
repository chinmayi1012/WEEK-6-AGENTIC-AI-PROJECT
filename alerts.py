def check_bp(bp):
    if bp > 140:
        return "High Blood Pressure Alert"
    elif bp < 90:
        return "Low Blood Pressure Alert"
    else:
        return "BP Normal"