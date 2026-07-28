from solution.diagnostics import detect_fault


def test_detect_high_esr():

    data = {
        "output_ripple": 0.12,
        "inductor_ripple": 1.5
    }

    fault = detect_fault(data)

    assert fault == "High ESR Capacitor"


def test_detect_low_inductance():

    data = {
        "output_ripple": 0.03,
        "inductor_ripple": 3.5
    }

    fault = detect_fault(data)

    assert fault == "Low Inductance"


def test_detect_capacitance_fault():

    data = {
        "output_ripple": 0.05,
        "inductor_ripple": 1.2
    }

    fault = detect_fault(data)

    assert fault == "Reduced Capacitance"