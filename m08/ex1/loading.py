import sys

try:
    import pandas as pd
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
except ImportError:
    pd = None
    np = None
    matplotlib = None
    plt = None

def check_dependencies():
    print("Checking dependencies:")
    dependencies_ok = True

    try:
        import pandas as pd
        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    except ImportError:
        print("[MISSING] pandas - Data manipulation unavailable")
        dependencies_ok = False

    try:
        import numpy as np
        print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
    except ImportError:
        print("[MISSING] numpy - Numerical computation unavailable")
        dependencies_ok = False

    try:
        import matplotlib
        print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
    except ImportError:
        print("[MISSING] matplotlib - Visualization unavailable")
        dependencies_ok = False

    return dependencies_ok

def show_installation_instructions():
    print()
    print("Missing dependencies detected!")
    print()
    print("Install using pip:")
    print("    pip install -r requirements.txt")
    print()
    print("Or install using Poetry:")
    print("    poetry install")

def explain_pip_vs_poetry():
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

def generate_matrix_data(n_samples=100):
    np.random.seed(97)
    tempo = np.arange(n_samples)
    atividade_neural = np.random.normal(loc = 50, scale = 15, size = n_samples)
    return tempo, atividade_neural

def create_dataframe(tempo, atividade_neural):
    dados = {
        "tempo": tempo,
        "atividade_neural": atividade_neural
    }
    df = pd.DataFrame(dados)
    return df

def analyze_data(df):
    print("=== Matrix Data Analysis ===")
    print(df.describe())
    return df.describe()

def analytics(df):
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
    explain_pip_vs_poetry()
    print()

    if not check_dependencies():
        show_installation_instructions()
        sys.exit(1)

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
