import discord

client = discord.Client()

folowmeid = '260038096681304074'

@client.event
async def on_ready():
    print('eingelogt als')
    print(client.user.name + '#' + client.user.discriminator)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.content.startswith('&status') and message.author.id == folowmeid:
        game = message.content[6:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, 'Ich habe meinen status zu ' + game + ' geaendert')

client.run('Mzg3OTA2MzIwODUxOTI3MDQw.DQlR6w.hVcJXvdQpWRATwSUPYzZuZ2otOg')