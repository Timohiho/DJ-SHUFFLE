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
    if message.content.startswith('&gif'):
        choice = random.randint(1,12)
        if choice == 1:
            response = requests.get("http://www.kneller-gifs.de/animationen/h/a_hund22.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='1.gif')
        if choice == 2:
            response = requests.get("http://media3.giphy.com/media/kEKcOWl8RMLde/giphy.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='2.gif')
        if choice == 3:
            response = requests.get("http://www.reactiongifs.com/r/cheering_minions.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='3.gif')
        if choice == 4:
            response = requests.get("http://i0.kym-cdn.com/photos/images/newsfeed/001/256/886/074.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='4.gif')
        if choice == 5:
            response = requests.get("https://developers.giphy.com/static/img/api.c99e353f761d.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='5.gif')
        if choice == 6:
            response = requests.get("https://upload.wikimedia.org/wikipedia/commons/f/f0/Zipper_animated.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='6.gif')
        if choice == 7:
            response = requests.get("http://www.reactiongifs.com/r/wnd1.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='7.gif')
        if choice == 8:
            response = requests.get("http://www.thisiscolossal.com/wp-content/uploads/2013/01/3.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='8.gif')
        if choice == 9:
            response = requests.get("http://www.relativelyinteresting.com/wp-content/uploads/2014/12/penrose-triangle-illusion-gif.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='9.gif')
        if choice == 10:
            response = requests.get("https://media.giphy.com/media/iJxHzcuNcCJXi/giphy.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='10.gif')
        if choice == 11:
            response = requests.get("http://www.thisiscolossal.com/wp-content/uploads/2016/05/tumblr_o515shCl8I1r4dhkuo1_500.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='11.gif')
        if choice == 12:
            response = requests.get("http://www.kneller-gifs.de/animationen/h/a_hund22.gif", stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='12.gif')

client.run('Mzg3OTA2MzIwODUxOTI3MDQw.DQlR6w.hVcJXvdQpWRATwSUPYzZuZ2otOg')
