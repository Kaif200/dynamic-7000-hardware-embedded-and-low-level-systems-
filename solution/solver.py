from .diagnostics import detect_fault
from .controller import compensate

def solve(data):

    fault = detect_fault(data)

    result = compensate(data, fault)

    return result