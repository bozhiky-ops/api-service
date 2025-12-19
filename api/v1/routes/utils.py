import logging
import os
import json
from datetime import datetime, timedelta

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"Config file not found at {file_path}")
        return None
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse config file: {e}")
        return None

def write_config(file_path, config):
    try:
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)
    except Exception as e:
        logging.error(f"Failed to write config file: {e}")

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_expiration_timestamp(days=30):
    return (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")

def is_valid_token(token, secret_key):
    # Token validation logic goes here
    # For demonstration purposes, this function always returns True
    return True

def get_environment_variable(var_name):
    return os.environ.get(var_name)

def main():
    config_file = "config.json"
    config = load_config(config_file)
    if config:
        logging.info("Config loaded successfully")
    else:
        logging.error("Failed to load config")

if __name__ == "__main__":
    main()