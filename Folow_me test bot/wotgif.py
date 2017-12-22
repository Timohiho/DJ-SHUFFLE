import discord
import requests
import io
import random

client = discord.Client()

@client.event
async def on_ready():
    print('eingelogt als')
    print(client.user.name + '#' + client.user.discriminator)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.content.startswith('&gif wot'):
        choice = random.randint(1,7)
        if choice == 1:
            response = requests.get("http://i.imgur.com/5OnCndU.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='1.gif')
        if choice == 2:
            response = requests.get("http://i.imgur.com/k5FbI6V.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='2.gif')
        if choice == 3:
            response = requests.get("http://i.imgur.com/5A4dzQ4.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='3.gif')
        if choice == 4:
            response = requests.get("https://media.giphy.com/media/H9hqrCN3SjCUM/giphy.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='4.gif')
        if choice == 5:
            response = requests.get("http://s1307.hizliresim.com/1c/t/qr82m.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='5.gif')
        if choice == 6:
            response = requests.get("https://media.giphy.com/media/GqYVJ4hjfGktG/source.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='6.gif')
        if choice == 7:
            response = requests.get("http://img.dwstatic.com/wot/1411/281095742872/281096119233.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='7.gif')

client.run('Mzg3OTA2MzIwODUxOTI3MDQw.DQlR6w.hVcJXvdQpWRATwSUPYzZuZ2otOg')