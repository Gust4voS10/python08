import importlib
from importlib.metadata import version


def check_import() -> bool:
    module = {"pandas": "Data manipulation",
              "numpy": "Numerical computation",
              "requests": "Network access",
              "matplotlib": "visualization"}
    try:
        for m in module:
            importlib.import_module(m)
            print(f"[ok {m} ({version(m)}) - {module[m]} ready]")
    except ModuleNotFoundError as e:
        print(e)
        print(f'Import {m} with "pip install {m}"')
        return (False)
    return (True)


def analysis() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    data = np.random.randn(1000)
    df = pd.DataFrame(data, columns=["Matrix Signals"])

    print("Generating visualization...\n")
    df.plot(kind="hist")
    plt.title("Matrix Data Analysis")
    plt.savefig("matrix_analysis.png")
    print("Analysis complete!\n"
          "Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    if check_import():
        analysis()
