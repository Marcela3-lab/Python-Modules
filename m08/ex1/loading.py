import sys

try:
    import pandas as pd
    print(f"[OK] pandas ({pd.__version__}) - Numerical computation ready")
    ex = 0
except ImportError:
    print("[MISSING] pandas - Data manipulation unavailable")
    ex = 1
try: 
    import numpy as np
    print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
    ex = 0
except ImportError: 
    print("[MISSING] numpy - Data manipulation unavailable")
    ex += 1
try: 
    import matplotlib.pyplot as plt
    import matplotlib as mt
    print(f"[OK] matplotlib ({mt.__version__}) - Numerical computation ready")
    ex = 0
except ImportError:
        print("[MISSING] matplotlib - Visualization unavailable")
        ex +=1
if ex == 3:
    print()
    print("Missing dependencies detected!")
    print()
    print("Install using pip:")
    print("    pip install -r requirements.txt")
    print()
    print("Or install using Poetry:")
    print("    poetry install")
    print()
    print("=== pip vs Poetry ===")
    print("pip:")
    print("  - Uses requirements.txt to list dependencies")
    print("  - Requires manual virtual environment creation")
    print("  - Does not lock exact versions unless specified manually")
    print()
    print("Poetry:")
    print("  - Uses pyproject.toml to list dependencies")
    print("  - Creates and manages virtual environments automatically")
    print("  - Locks exact versions automatically via poetry.lock")
    exit(1)

def generate_matrix_data(n_samples=100) -> tuple:
    np.random.seed(97)
    tempo = np.arange(n_samples)
    atividade_neural = np.random.normal(loc = 50, scale = 15, size = n_samples)
    return tempo, atividade_neural

def create_dataframe(tempo, atividade_neural) -> dict:
    dados = {
        "tempo": tempo,
        "atividade_neural": atividade_neural
    }
    df = pd.DataFrame(dados)
    return df

def analyze_data(df) ->  pd.DataFrame:
    print("=== Matrix Data Analysis ===")
    print(df.describe())
    return df.describe()

def analytics(df) -> None:
    plt.figure(figsize=(10, 5))
    plt.plot(df["tempo"], df["atividade_neural"])
    plt.title("Matrix Neural Activity Over Time")
    plt.xlabel("Tempo")
    plt.ylabel("Atividade Neural")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")
    print()
    print()
    print("Analyzing Matrix data...")

    n_samples = 1000
    print(f"Processing {n_samples} data points...")

    tempo, atividade = generate_matrix_data(n_samples)
    df = create_dataframe(tempo, atividade)
    analyze_data(df)

    print("Generating visualization...")
    analytics(df)

    print()
    print("Aanalysis complete!")
