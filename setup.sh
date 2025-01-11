#!/bin/bash

APP_NAME="todocli"
APP_PATH="$(pwd)/$APP_NAME.py"

# Check if the file exists
if [ ! -f "$APP_PATH" ]; then
  echo "Error: $APP_PATH not found!"
  exit 1
fi

# Make the file executable
chmod +x "$APP_PATH"

# Let the user choose the app name
read -p "Enter the command you want to use to execute $APP_NAME (default: $APP_NAME): " CMD_NAME

if [ -z "$CMD_NAME" ]; then
  CMD_NAME="$APP_NAME"
fi

echo "Installing $APP_NAME as $CMD_NAME..."

# Create a symlink in /usr/local/bin
sudo ln -sf "$APP_PATH" /usr/local/bin/$CMD_NAME

echo "Successfully installed $APP_NAME. You can now run it using the command '$CMD_NAME'."
