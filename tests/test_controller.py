from solution.controller import compensate


def test_controller_returns_dictionary():

    data = {
        "vin": 24,
        "vout": 12
    }

    result = compensate(data, "Low Inductance")

    assert isinstance(result, dict)


def test_contains_duty_cycle():

    data = {
        "vin": 24,
        "vout": 12
    }

    result = compensate(data, "Low Inductance")

    assert "recommended_duty_cycle" in result


def test_duty_cycle_range():

    data = {
        "vin": 24,
        "vout": 12
    }

    result = compensate(data, "Low Inductance")

    duty = result["recommended_duty_cycle"]

    assert 0 < duty < 1