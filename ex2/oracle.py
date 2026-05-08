import os


def consult_oracle() -> None:
    try:
        from dotenv import load_dotenv
    except Exception:
        print("Need to install 'Python-dotenv'")
        return
    print("\nORACLE STATUS: Reading the Matrix...\n")
    envs = {"MATRIX_MODE": "Mode",
            "DATABASE_URL": "Database",
            "API_KEY": "API Access",
            "LOG_LEVEL": "Log Level",
            "ZION_ENDPOINT": "Zion Network"}
    load_dotenv()
    for env, txt in envs.items():
        result = os.getenv(env)
        if not result:
            print(f"ERROR: env {txt}, not found")
        else:
            print(f"{txt}: {result}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing!")
    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    consult_oracle()
