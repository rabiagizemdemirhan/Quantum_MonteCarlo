# metropolis.py

import numpy as np

def metropolis_sampling(initial_x, steps, step_size=1.0, beta=1.0, potential=None):
    """
    Monte Carlo (Metropolis algoritması) ile parçacık konumlarını örnekler.

    initial_x: Başlangıç konumu
    steps: Toplam adım sayısı
    step_size: Rastgele sapma aralığı
    beta: 1/(kT), sıcaklık faktörü
    potential: Kullanılacak potansiyel fonksiyonu
    """
    if potential is None:
        raise ValueError("Potansiyel fonksiyonu belirtilmelidir.")

    x = initial_x
    samples = []

    for _ in range(steps):
        x_new = x + np.random.uniform(-step_size, step_size)
        delta_V = potential(x_new) - potential(x)
        accept_prob = np.exp(-beta * delta_V)

        if delta_V < 0 or np.random.rand() < accept_prob:
            x = x_new

        samples.append(x)

    return samples
