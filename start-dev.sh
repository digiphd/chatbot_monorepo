# start.sh
#!/bin/bash

# Change to the root directory
cd /workspace

# Update PYTHONPATH to include api module
export PYTHONPATH=$PYTHONPATH:/workspace/api

# Start Uvicorn server
uvicorn api.main:app --host 0.0.0.0 --port 8000 &

# Start Discord bot
python bots/discord.py &

# Start Telegram bot
python bots/telegram.py &

# Start frontend development server
(cd frontend && npm start) &