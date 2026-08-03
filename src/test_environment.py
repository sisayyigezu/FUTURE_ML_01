
"""Verify that the project environment is configured correctly."""

import sys

import joblib
import matplotlib
import numpy as np
import pandas as pd
import sklearn
import statsmodels


def main() -> None:
    """Print package and Python versions."""

    print("Environment test successful.")
    print(f"Python version: {sys.version}")
    print(f"pandas version: {pd.__version__}")
    print(f"NumPy version: {np.__version__}")
    print(f"Matplotlib version: {matplotlib.__version__}")
    print(f"scikit-learn version: {sklearn.__version__}")
    print(f"statsmodels version: {statsmodels.__version__}")
    print(f"joblib version: {joblib.__version__}")


if __name__ == "__main__":
    main()