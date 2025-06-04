#!/usr/bin/env python3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Print all environment variables
print("Environment Variables:")
print(f"DATABASE_URL: {os.getenv('DATABASE_URL', 'Not set')}")
print(f"DEV_DATABASE_URL: {os.getenv('DEV_DATABASE_URL', 'Not set')}")
print(f"TEST_DATABASE_URL: {os.getenv('TEST_DATABASE_URL', 'Not set')}")
print(f"SECRET_KEY: {os.getenv('SECRET_KEY', 'Not set')}")
print(f"DEBUG: {os.getenv('DEBUG', 'Not set')}")

# Print current working directory
print(f"\nCurrent working directory: {os.getcwd()}")

# Check if .env file exists
env_path = os.path.join(os.getcwd(), '.env')
print(f".env file exists: {os.path.exists(env_path)}")

# If .env exists, print its contents
if os.path.exists(env_path):
    print("\nContents of .env file:")
    with open(env_path, 'r') as f:
        print(f.read())
