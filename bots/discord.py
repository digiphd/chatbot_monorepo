import discord
import requests

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    user_message = message.content
    response = requests.post('http://your-fastapi-endpoint/chat', json={'message': user_message})
    response_text = response.json().get('response', 'Sorry, there was an error.')
    await message.channel.send(response_text)

# Replace 'your_discord_token' with the token you got from the Discord Developer Portal
client.run('your_discord_token')
