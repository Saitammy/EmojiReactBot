import discord

def run_discord_bot():
    token = 'MTA5ODYyMjI5MTc4NjYwODY0MQ.Gcielx.j8hDTjig_pxfjUML-IQ0jrd5kar8EdvfOG7I_A'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content[0] == 'a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'g' or 'h' or 'i' or 'j' or 'k' or 'l' or 'm' or 'n' or 'o' or 'p' or 'q' or 'r' or 's' or 't' or 'u' or 'v' or 'w' or 'x' or 'y' or 'z':
            await message.add_reaction('\U0001F64F')

        if message.content[0] == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
            await message.add_reaction('\U0001F64F')

        if message.content[0] == '!' or '@' or '#' or '$' or '%' or '^' or '&' or '*' or '(' or ')' or '-' or '_' or '+' or '=' or '`' or '[' or ']' or '|':
            await message.add_reaction('\U0001F64F')

    client.run(token)
