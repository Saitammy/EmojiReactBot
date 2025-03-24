import discord
import random
import os
import asyncio
from dotenv import load_dotenv

# This function loads the environment variable.
load_dotenv()
discord_token = os.getenv("DiscordBotToken")

if discord_token is None:
    print("Error - DiscordBotToken not found in .env file!")
    exit(1)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
    if message.author.bot:
        return 

    if message.content == '!p help':
        await message.channel.send(
            'Thank you for reaching out to the help section.\n'
            '1. !p - Sends an image.\n'
            '2. !pg - Sends a random GIF.'
        )

    if message.content or message.attachments or message.stickers:
        await message.add_reaction('🙏')

    if message.content == '!p':
        if os.path.exists('Pray.jpg'):
            await message.channel.send(file=discord.File('Pray.jpg'))
        else:
            await message.channel.send("Image file not found!")

    if message.content == '!pg':
        gif_files = ['1.gif', '2.gif', '3.gif', '4.gif', '5.gif']
        selected_gif = random.choice(gif_files)
        if os.path.exists(selected_gif):
            await message.channel.send(file=discord.File(selected_gif))
        else:
            await message.channel.send("GIF file not found!")

async def main():
    async with client:
        await client.start(discord_token)

if __name__ == "__main__":
    asyncio.run(main()) 
