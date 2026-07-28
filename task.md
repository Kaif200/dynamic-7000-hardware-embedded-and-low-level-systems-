
---

# task.md

This is the most important file.

Example:

```markdown
# Task

You are given telemetry collected from a synchronous buck converter.

Each input includes

- Vin
- Vout
- Inductor current ripple
- Output ripple
- Switching frequency
- Load current

Exactly one passive component has degraded.

Possible faults

- High ESR capacitor
- Reduced inductance
- Reduced capacitance

Your task is to

1. Identify the fault.
2. Estimate the degraded parameter.
3. Recommend a corrected duty cycle.
4. Predict resulting ripple.
5. Return JSON.

Input

{
  ...
}

Output

{
  ...
}

Constraints

- Switching frequency remains fixed.
- Converter remains in CCM.
- Duty cycle between 0 and 1.

Evaluation

Correctness

Robustness

Efficiency

Code Quality