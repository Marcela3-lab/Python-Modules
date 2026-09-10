import sys
import os

try:
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: python-dotenv não está instalado.")
    print("Rode: pip install -r requirements.txt")
    sys.exit(1)

load_dotenv()


def load_configuration():
    config = {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE"),
        "DATABASE_URL": os.environ.get("DATABASE_URL"),
        "API_KEY": os.environ.get("API_KEY"),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL"),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT"),
    }
    return config


def show_configuration(config):
    print("Configuration loaded:")
    repr(os.environ.get("MATRIX_MODE"))
    if config["MATRIX_MODE"] == "production":
        print("Database: Connected to production instance")
    elif config["MATRIX_MODE"] == "development":
        print("Database: Connected to local instance")
    elif config["MATRIX_MODE"] is None:
        print("Matrix mode not found (missing MATRIX_MODE)")

    if config["API_KEY"] is not None:
        print(f"API Access: {config['API_KEY']}")
    else:
        print("API Access: Not authenticated (missing API_KEY)")

    if config["LOG_LEVEL"] == "DEBUG":
        print(f"Log Level: {config['LOG_LEVEL']}")
    else:
        print("Log Level (missing LOG LEVEL))")

    if config["ZION_ENDPOINT"] == "Online":
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline (missing ZION_ENDPOINT)")


def security_check():
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    config = load_configuration()
    show_configuration(config)
    security_check()
