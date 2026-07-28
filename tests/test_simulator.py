import pytest
from solution.simulator import BuckSimulator


def test_current_ripple_positive():
    sim = BuckSimulator(
        vin=24,
        vout=12,
        L=100e-6,
        C=220e-6,
        ESR=0.02,
        fs=100000
    )

    ripple = sim.current_ripple()

    assert ripple > 0


def test_voltage_ripple_positive():
    sim = BuckSimulator(
        vin=24,
        vout=12,
        L=100e-6,
        C=220e-6,
        ESR=0.02,
        fs=100000
    )

    ripple = sim.voltage_ripple()

    assert ripple > 0


def test_duty_cycle():
    sim = BuckSimulator(
        vin=24,
        vout=12,
        L=100e-6,
        C=220e-6,
        ESR=0.02,
        fs=100000
    )

    duty = sim.vout / sim.vin

    assert duty == pytest.approx(0.5)