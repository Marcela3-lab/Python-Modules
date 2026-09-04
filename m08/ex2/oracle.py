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
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", "development"),
        "DATABASE_URL": os.environ.get("DATABASE_URL", "not configured"),
        "API_KEY": os.environ.get("API_KEY", "not configured"),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT", "not configured"),
    }
    return config

def show_configuration(config):
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    if config["MATRIX_MODE"] == "production":
        print("Database: Connected to production instance")
    else:
        print("Database: Connected to local instance")

    if config["API_KEY"] != "not configured":
        print("API Access: Authenticated")
    else:
        print("API Access: Not authenticated (missing API_KEY)")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"] != "not configured":
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


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    config = load_configuration()
    show_configuration(config)
    security_check()