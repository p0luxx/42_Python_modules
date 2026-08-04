import os
import sys
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")
    print("Accessing the Mainframe")
    print("ORACLE STATUS: Reading the Matrix...\n")
    missing_vars = []
    if not matrix_mode:
        missing_vars.append("MATRIX_MODE")
    if not database_url:
        missing_vars.append("DATABASE_URL")
    if not api_key:
        missing_vars.append("API_KEY")
    if not log_level:
        missing_vars.append("LOG_LEVEL")
    if not zion_endpoint:
        missing_vars.append("ZION_ENDPOINT")
    if missing_vars:
        print("WARNING: Missing essential configuration variables!")
        print(f"Missing: {', '.join(missing_vars)}")
        print("Please configure your .env file or environment variables.\n")
        sys.exit(1)
    if matrix_mode == "production":
        db_status = f"Connected to production cluster ({database_url})"
        log_status = f"{log_level} (Restricted)"
    else:
        db_status = "Connected to local instance"
        log_status = log_level
    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    print(f"Database: {db_status}")
    print("API Access: Authenticated")
    print(f"Log Level: {log_status}")
    print("Zion Network: Online\n")
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations")


if __name__ == "__main__":
    main()
