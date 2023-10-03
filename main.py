import subprocess
import os
import sys
import asyncio
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO", format="<green>{time}</green> <level>{message}</level>")
os.environ['PYTHONPATH'] = f"{os.environ.get('PYTHONPATH', '')}:/workspace/api"

async def run_command(cmd, description):
    logger.info(f"Starting {description}")
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=sys.stdout, stderr=sys.stderr
    )
    await process.communicate()
    logger.info(f"{description} terminated with return code {process.returncode}")

async def main():
    logger.info("Starting uvicorn server for Fast API and discord bot")
    uvicorn_cmd = "uvicorn api.main:app --host 0.0.0.0 --port 8000"
    discord_bot_cmd = "python bots/discord_bot.py"

    # Run Uvicorn and Discord bot in parallel
    await asyncio.gather(
        run_command(uvicorn_cmd, "Uvicorn server"),
        run_command(discord_bot_cmd, "Discord bot")
    )

if __name__ == "__main__":
    asyncio.run(main())
