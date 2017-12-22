import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('eingelogt als')
    print(client.user.name + '#' + client.user.discriminator)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.content.startswith('çtime'):
        lt = time.localtime()

        jahr, monat, tag = lt[0:3]
        datum = ("Datum: {0:02d}.{1:02d}.{2:4d}".format(tag, monat, jahr))

        stunde, minute, sekunde = lt[3:6]
        zeit = ("Aktuelle Uhrzeit: {0:02d}:{1:02d}:{2:02d}".format(stunde, minute, sekunde))
        await client.send_message(message.channel, '```{datum}```'.format(datum=datum))
        await client.send_message(message.channel, '```{zeit}```'.format(zeit=zeit))

client.run('Mzg3OTA2MzIwODUxOTI3MDQw.DQlR6w.hVcJXvdQpWRATwSUPYzZuZ2otOg')