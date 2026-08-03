import importlib.metadata
import importlib.util
import sys


def check_pkg(name):
    if importlib.util.find_spec(name) is None:
        return None
    return importlib.metadata.version(name)


def main():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    packages = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization",
    }
    missing = []
    for pkg, desc in packages.items():
        ver = check_pkg(pkg)
        if ver:
            print(f"[OK] {pkg} ({ver}) - {desc} ready")
        else:
            print(f"[MISSING] {pkg} - {desc} missing")
            missing.append(pkg)
    if missing:
        print("\nERROR: Missing required dependencies!")
        print("\nTo install with pip:")
        print("pip install -r requirements.txt")
        print("\nTo install with Poetry:")
        print("poetry install")
        sys.exit(1)
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    data = np.random.randn(1000)
    df = pd.DataFrame({"signal": data})
    print("Generating visualization...")
    plt.plot(df["signal"])
    plt.title("Matrix Data")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
