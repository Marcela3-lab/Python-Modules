import sys
import os
import site

def is_env():
    return sys.prefix == sys.base_prefix    

def outside_env():
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\Scripts\activate # On Windows")
    print()
    print("Then run this program again.")

def inside_env():
    venv_path = sys.prefix
    venv_name = os.path.basename(venv_path)
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")

    try:
        packages_path = site.getsitepackages()[0]
    except Exception:
        packages_path = os.path.join(venv_path, "lib",
                                      f"python{sys.version_info.major}.{sys.version_info.minor}",
                                      "site-packages")

    print(f"Package installation path: {packages_path}")

if __name__ == "__main__" :
    if is_env():
        outside_env()
    else:
        inside_env()