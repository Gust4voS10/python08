import sys
import os
import site


if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environmet: {os.path.basename(sys.prefix)}\n")
        print(f"Environment Path: {sys.prefix}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")
        print("Package installation path:")
        print(site.getsitepackages())
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environmet: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env/Scripts/activate # On Windows")
        print("\nthe run this program again.")
