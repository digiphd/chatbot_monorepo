import discord
import requests
from common.config import DISCORD_TOKEN
from loguru import logger

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    logger.debug(f"Author: {message.author}, User: {client.user}")
    user_message = message.content
    server_url='http://127.0.0.1:8000/chat/'
    headers = {'Content-Type': 'application/json'}
    logger.debug(f"Message Content: {message.content}")
    logger.debug(f"Message Type: {message.type}")
    logger.debug(f"Message Embeds: {message.embeds}")
    response = requests.post(server_url, json={'message': user_message, 'expert_type':'youtube'}, headers=headers)
    # Log the server URL and port
    logger.debug(f'Response: {response}')

    response_text = response.json().get('response', 'Sorry, there was an error.')
    await message.channel.send(response_text)

client.run(DISCORD_TOKEN)
