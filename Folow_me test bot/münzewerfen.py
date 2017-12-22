import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('eingelogt als')
    print(client.user.name + '#' + client.user.discriminator)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.content.startswith('&münze'):
        choice = random.randint(1, 2)
        if choice == 1:
            await client.add_reaction(message, '🌑')
        if choice == 2:
            await client.add_reaction(message, '🌕')

client.run('Mzg3OTA2MzIwODUxOTI3MDQw.DQlR6w.hVcJXvdQpWRATwSUPYzZuZ2otOg')