def detect_fault(data):

    ripple = data["output_ripple"]

    current = data["inductor_ripple"]

    if ripple > 0.08:
        return "High ESR Capacitor"

    if current > 2.5:
        return "Low Inductance"

    return "Reduced Capacitance"