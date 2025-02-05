#!/bin/bash

# Ask for minimum value
read -p "Enter the minimum number: " min

# Ask for maximum value
read -p "Enter the maximum number: " max

# Generate random number within range
random_number=$((RANDOM % (max - min + 1) + min))

# Print result
echo "Random number between $min and $max: $random_number"

