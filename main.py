from metropolis import metropolis_sampling
import matplotlib.pyplot as plt

def main():
    samples = metropolis_sampling(initial_x=0.0, steps=10000, step_size=1.0, beta=1.0)

    # Histogram çizimi
    
    plt.hist(samples, bins=100, density=True, alpha=0.6, label="Monte Carlo")
    plt.xlabel("Konum (x)")
    plt.ylabel("Olasılık Yoğunluğu")
    plt.title("Harmonik Osilatör Monte Carlo Simülasyonu")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
