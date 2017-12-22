import discord
import requests
import io

client = discord.Client()

@client.event
async def on_ready():
    print('eingelogt als')
    print(client.user.name + '#' + client.user.discriminator)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.content.startswith('&png'):
        response = requests.get("https://www.spreadshirt.ch/image-server/v1/mp/designs/14842651,width=178,height=178/daumen-hoch-thumbs-up-outline-1c.png", stream=True)
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='daumen.png', content='Daumen hoch')

client.run('Mzg3OTA2MzIwODUxOTI3MDQw.DQlR6w.hVcJXvdQpWRATwSUPYzZuZ2otOg')