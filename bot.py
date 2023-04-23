import discord
import random


def run_discord_bot():
    token = ''
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):

        if message.content == 'pray help':
            await message.channel.send('Thank you for reaching out to the help section.\n1. pray for sending '
                                       'image.\n2. pray gif to send random gif.')

        if message.content or message.attachments or message.stickers:
            await message.add_reaction('\U0001F64F')

        if message.content == 'pray':
            with open('Pray.jpg', 'rb') as image:
                await message.channel.send(file=discord.File(image, 'Pray.jpg'))

        if message.content == 'pray gif':
            gif = ['1.gif', '2.gif', '3.gif', '4.gif', '5.gif']
            gifed = random.choice(gif)
            with open(gifed, 'rb') as done:
                await message.channel.send(file=discord.File(done, gifed))

    client.run(token)
