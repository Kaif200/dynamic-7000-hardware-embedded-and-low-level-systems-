from solution.solver import solve


def test_solver_output():

    data = {
        "vin": 24,
        "vout": 12,
        "load_current": 5,
        "switching_frequency": 100000,
        "inductor_ripple": 3.2,
        "output_ripple": 0.05
    }

    result = solve(data)

    assert isinstance(result, dict)


def test_solver_required_keys():

    data = {
        "vin": 24,
        "vout": 12,
        "load_current": 5,
        "switching_frequency": 100000,
        "inductor_ripple": 3.2,
        "output_ripple": 0.05
    }

    result = solve(data)

    required = [
        "fault",
        "recommended_duty_cycle"
    ]

    for key in required:
        assert key in result


def test_solver_duty_cycle_valid():

    data = {
        "vin": 24,
        "vout": 12,
        "load_current": 5,
        "switching_frequency": 100000,
        "inductor_ripple": 3.2,
        "output_ripple": 0.05
    }

    result = solve(data)

    duty = result["recommended_duty_cycle"]

    assert 0 < duty < 1