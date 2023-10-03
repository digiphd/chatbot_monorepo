#!/bin/bash

# Change to the root directory
cd /workspace

# Update PYTHONPATH to include api module
export PYTHONPATH=$PYTHONPATH:/workspace/api

# Kill any running uvicorn and python processes
pkill -f uvicorn
pkill -f discord_bot.py

# Start Uvicorn server
uvicorn api.main:app --host 0.0.0.0 --port 8000 &

# Start Discord bot
python bots/discord_bot.py &


# # Start frontend development server
# (cd frontend && npm start) &