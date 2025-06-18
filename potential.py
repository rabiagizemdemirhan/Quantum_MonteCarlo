# potential.py

def harmonic_potential(x):
    return 0.5 * x**2

def double_well_potential(x):
    return 0.5 * (x**2 - 1)**2

def barrier_potential(x):
    return 10 if -0.5 < x < 0.5 else 0
