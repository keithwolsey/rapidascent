#!/bin/bash
# Creates users read from a list of names

# Define variables
USER_FILE="usernames.txt" # Input file containing usernames
DEFAULT_PASSWORD="Welcome@123" # Default password for new accounts
LOG_FILE="created_users.log" # Log file for created accounts

# Check if the usernames file exists
if [[ ! -f $USER_FILE ]]; then
  echo "Error: Usernames file '$USER_FILE' not found!"
  exit 1
fi

# Clear or create the log file
> "$LOG_FILE"

# Loop through each line in the usernames file
while IFS= read -r username; do
  # Skip empty lines
  if [[ -z $username ]]; then
    continue
  fi

  # Check if the user already exists
  if id "$username" &>/dev/null; then
    echo "User '$username' already exists. Skipping..."
    continue
  fi

  # Create the user with a home directory and assign the default password
  useradd -m "$username" && echo "$username:$DEFAULT_PASSWORD" | chpasswd
  
  # Check if the user was created successfully
  if [[ $? -eq 0 ]]; then
    echo "User '$username' created successfully."
    echo "$username" >> "$LOG_FILE"
  else
    echo "Failed to create user '$username'."
  fi
done < "$USER_FILE"

echo "User creation process completed. See '$LOG_FILE' for details."

