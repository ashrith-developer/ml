import logging
import os
from datetime import datetime

# Define log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H%M')}.log"

# Create absolute path to logs directory
logs_path = os.path.join(os.getcwd(), "logs")

# Create logs directory with proper error handling
try:
    os.makedirs(logs_path, exist_ok=True)
    print(f"Log directory created/verified at: {logs_path}")
except Exception as e:
    print(f"Error creating log directory: {e}")
    # Fallback to current directory if we can't create the logs folder
    logs_path = os.getcwd()
    print(f"Falling back to current directory: {logs_path}")

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
print(f"Log file will be created at: {LOG_FILE_PATH}")

# Configure logging
try:
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    print(f"Logging configured successfully")
except Exception as e:
    print(f"Error configuring logging: {e}")

if __name__ == "__main__":
    logging.info("Logging has started")
    print("Logger initialized successfully")